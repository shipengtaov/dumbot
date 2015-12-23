#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

name = ['browser']

def help():
    return {
        'result': '''python run.py browser <url>'''
    }

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    if plugin_args:
        url = plugin_args[0]
        # pipeline.update(dict(url=url))
    elif plugin_kwargs.get('browser'):
        pass
    elif pipeline.get('url'):
        url = pipeline.get('url')
    elif pipeline.get('content'):
        url = pipeline.get('content')

    if url:
        os.system("open %s" %url)

    return {
        "result": url,
        "pipeline": pipeline,
    }
