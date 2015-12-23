#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# 打印机
#

name = ['print']

def help():
    return {
        'result': '''Usage: python run.py print <text>'''
    }

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    text = plugin_args[0] if plugin_args else pipeline.get('content', '')
    if not text:
        return dict(result='', pipeline=pipeline)
    return dict(result='not available', pipeline=pipeline)
