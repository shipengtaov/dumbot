#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import re

from dumbot import plugins

plugins_all = []
def import_plugin():
    if plugins_all:
        return
    for plugin_name in plugins.__all__:
        importlib.import_module('dumbot.plugins.%s' %plugin_name)
        plugins_all.append(getattr(plugins, plugin_name))
import_plugin()

def list_plugin():
    msg = ''
    msg += 'all plugins:\n'
    for iter_plugin in plugins_all:
        msg += ' '*2 + '* ' + iter_plugin.name[0]
        if len(iter_plugin.name) > 1:
            msg += ' '*20 + 'alias: ' + ','.join(iter_plugin.name[1:])
        msg += '\n'
    return msg

# currently disable. 暂时不开放使用
def before_plugin():
    for iter_plugin in plugins_all:
        if getattr(iter_plugin, 'before', None):
            iter_plugin.before(**globals())

def choose_plugin(plugin_name):
    for iter_plugin in plugins_all:
        if plugin_name in iter_plugin.name:
            return iter_plugin
    return None

def parse_plugin_param(plugin_param):
    if not plugin_param:
        return [], {}
    args = []
    kwargs = {}
    for i in plugin_param:
        if re.search('^.+?=.+?$', i):
            i_split = i.split('=', 1)
            kwargs[i_split[0]] = i_split[1]
        else:
            args.append(i)
    return args, kwargs
