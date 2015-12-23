#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

name = ['output']

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    if plugin_args:
        output = plugin_args[0]
        pipeline.update(dict(content=output))
    else:
        output = pipeline.get('content', '')

    print(output)
    return {
        "result": output,
        "pipeline": pipeline,
    }
