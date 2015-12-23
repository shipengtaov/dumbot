#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime

name = ['when']

def help():
    return {
        'result': '''Usage: python run.py when [date]
Options:
    date        format: %Y-%m-%d_%H:%M:%S 可以只传递一部分值
Kwargs:
    when=date'''
    }

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    pass