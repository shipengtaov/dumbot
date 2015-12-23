#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import types
import copy
from argparse import ArgumentParser
import traceback

from dumbot import plugins
from dumbot import plugin_util

# 包括后台运行的参数
def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-l', '--list', dest="list_plugin", action="store_true", help="list all plugins")
    parser.add_argument('plugin', nargs='?', help="run plugin")
    parser.add_argument('plugin_param', nargs='*', help="plugin params")
    parser.add_argument('-p', '--pipeline', help="pipeline plugins; split with ','")
    parser.add_argument('-D', dest="daemon", action="store_true", help="run in background?")
    args = parser.parse_args()
    return parser, args

# 允许返回多个结果并依次返回或依次pipeline?
def run_plugin(plugin, parser_args):
    plugin_args, plugin_kwargs = plugin_util.parse_plugin_param(parser_args.plugin_param)
    try:
        result = plugin.results(plugin_args=plugin_args,
                                plugin_kwargs=plugin_kwargs,
                                parser_args=parser_args)
    except:
        print('%s error: %s' %(plugin.name[0], traceback.format_exc()))
        return
    if type(result) is types.GeneratorType:
        results = result
    else:
        results = [result]
    pipeline = parser_args.pipeline
    for result_iter in results:
        result = copy.deepcopy(result_iter)
        if pipeline:
            for pipe in pipeline.split(','):
                pipe_plugin = plugin_util.choose_plugin(pipe)
                if not pipe_plugin:
                    raise SystemExit('there is no plugin named: %s' %pipe)
                if result.get('pipeline'):
                    if result['pipeline'].get('break'):
                        break
                    try:
                        result = pipe_plugin.results(plugin_kwargs=plugin_kwargs,
                                                    pipeline=result['pipeline'],
                                                    parser_args=parser_args)
                    except:
                        print('%s error: %s' %(pipe_plugin.name[0], traceback.format_exc()))
                        return
                else:
                    break

        if result.get('result'):
            print(result['result'])
        if result.get('html'):
            pass

def main():
    parser, args = parse_args()

    if args.list_plugin:
        print(plugin_util.list_plugin())
        return

    plugin = plugin_util.choose_plugin(args.plugin)
    if not plugin:
        print("sorry, there is no plugin named: %s" %args.plugin)
        return False
    return run_plugin(plugin, args)
