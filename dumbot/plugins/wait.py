#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

name = ['wait']

def help():
    return {
        'result': '''Usage: python run.py wait [seconds]

Options:
seconds        sleep <number> seconds. default 1 second'''
    }

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    sleep = None
    if plugin_args:
        sleep = int(plugin_args[0])
    elif plugin_kwargs.get('wait'):
        sleep = int(plugin_kwargs.get('wait'))
    else:
        sleep = 1
    if sleep is None:
        raise SystemExit('there is not param for wait plugin ')
    else:
        time.sleep(sleep)
    return {
        'result' : '',
        'pipeline': pipeline,
    }
