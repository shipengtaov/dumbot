#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
# from chardet import detect

name = ['say']

def help():
    return dict(result='Usage: python run.py say <words>')

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    if plugin_args:
        say_what = plugin_args[0]
        pipeline.update(dict(content=say_what))
    elif plugin_kwargs.get('say'):
        say_what = plugin_kwargs['say']
    elif pipeline.get('say'):
        say_what = pipeline['say']
    else:
        say_what = pipeline.get('content', '')

    if isinstance(say_what, unicode):
        say_what = say_what.encode('utf-8')

    os.system("say " + say_what)
    return {
        # 朗读不打印结果
        # "result": say_what,
        "result": '',
        "pipeline": pipeline,
    }
