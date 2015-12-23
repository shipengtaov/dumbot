#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import importlib

name = ['help']

def help():
    return {
        'result': 'Usage: python run.py help <plugin>'
    }

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    if len(plugin_args) < 1:
        return help()

    plugin_name = plugin_args[0]
    plugin = None
    try:
        import_str = 'dumbot.plugins.%s' %plugin_name
        plugin = importlib.import_module(import_str)
    except ImportError:
        pass
    if not plugin:
        return dict(result='There is no plugin named %s' %plugin_name)

    help_method = getattr(plugin, 'help', None)
    if help_method:
        return help_method()
    else:
        return dict(result='there is no help doc for %s plugin' %plugin_name)
