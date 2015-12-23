#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import types

import requests

name = ['zhihu_daily']

daily_today = 'http://news.at.zhihu.com/api/1.2/news/latest'
daily_choose = 'http://news.at.zhihu.com/api/1.2/news/before/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
}

def help():
    return {
        'result': '''python run.py zhihu_daily [date]

Options:
    date    format example: 20150824. default:today'''
    }

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    day = None
    if plugin_args:
        day = plugin_args[0]
        day = (datetime.datetime.strptime(day, '%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
    try:
        if not day:
            url = daily_today
            ret = requests.get(url, headers=headers, timeout=10)
        else:
            url = daily_choose + day
            ret = requests.get(url, headers=headers, timeout=10)
    except:
        yield dict(result='zhihu_daily 接口请求出错', pipeline=pipeline)
        return

    for k,v in ret.json().items():
        if type(v) is not types.ListType:
            continue
        for item in v:
            # result = k + ':\n'
            result = ''
            result += item['title'] + '\n'
            result += item['share_url']
            result += '\n'

            pipeline.update(dict(
                            url=item['share_url'],
                            say=item['title'],
                            content=result, 
                            ))

            yield dict(result=result, pipeline=pipeline)
