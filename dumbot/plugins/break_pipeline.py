#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = ['break_pipeline']

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    tip = 'break pipeline?'
    if plugin_args:
        tip = plugin_args[0]
    elif plugin_kwargs.get('break_pipeline'):
        tip = plugin_kwargs.get('break_pipeline')

    choose_your_own_way = raw_input(tip+'(Y/n)')
    if choose_your_own_way in ['y', 'yes', 'Y']:
        pipeline['break'] = True
    return dict(result=str(choose_your_own_way), pipeline=pipeline)
