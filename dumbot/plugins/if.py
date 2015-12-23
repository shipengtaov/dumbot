#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = ['if']

def help():
    return dict(result='''
''')

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    if_condition = False

    if plugin_args:
        if_condition = plugin_args[0]

    if pipeline.has_key('if'):
        if_condition = pipeline['if']

    # if True: 继续执行后续的插件
    if if_condition:
        pipeline.update({'break':False})
    # 结束本次后续的插件执行
    else:
        pipeline.update({'break':True})

    return dict(result=if_condition, pipeline=pipeline)
