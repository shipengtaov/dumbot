#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

name = ['weather']

def help():
    return {
        'result': '''Usage: python run.py weather [options]
'''
    }

# 条件判断: 比如: 是否有雨, 是否有雪; 供 notify 等插件使用
def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    pass
