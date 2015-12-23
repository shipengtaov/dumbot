#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import requests

name = ['hacker_news']

hacker_news_urls = {
    'top': 'https://hacker-news.firebaseio.com/v0/topstories.json',
    'new': 'https://hacker-news.firebaseio.com/v0/newstories.json',
}
item_api_base_url = 'https://hacker-news.firebaseio.com/v0/item/%d.json'
user_api_base_url = 'https://hacker-news.firebaseio.com/v0/user/%s.json'

item_base_url = 'https://news.ycombinator.com/item?id=%d'

default_length = 30

def help():
    return {
        'result': '''Usage: python run.py hacker_news [options]

Options:
    top                top stories
    new                newest stories
    item <item_id>     get one item
    user <user_name>   get one user
    length=<number>    number of result. default:'''+str(default_length)
    }

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    if not plugin_args:
        news_type = 'top'
    else:
        news_type = plugin_args[0]
        if news_type not in ['top', 'new', 'item', 'user']:
            yield help()
            return
        if news_type in ['item', 'user'] and len(plugin_args)<2:
            yield help()
            return

    length = int(plugin_kwargs['length']) if plugin_kwargs.get('length') else default_length

    if news_type in ['top', 'new']:
        try:
            ret = requests.get(hacker_news_urls[news_type], timeout=10)
            all_news = ret.json()
        except:
            yield dict(result='hacker_news 接口请求出错')
            return
        if length > len(all_news):
            length = len(all_news)
        for i in xrange(length):
            news_id = all_news[i]
            item = requests.get(item_api_base_url %news_id).json()

            item_url = item_base_url %item['id']
            title = item['title']

            result = '%d: %s\n' %(i+1, title)
            result += ' '*6 + 'score: %d  by: %s  time: %s  type: %s\n' %(
                            item['score'], item['by'], 
                            datetime.datetime.fromtimestamp(item['time']).strftime('%Y-%m-%d %H:%M:%S'),
                            item['type'])
            result += ' '*6 + 'item_url: %s\n' %item_url
            if item.get('url'):
                result += ' '*6 + 'url: %s\n' %item['url']

            pipeline.update(dict(content=result, url=item_url, say=title))

            yield dict(result=result, pipeline=pipeline)

    elif news_type == 'item':
        pass
    elif news_type == 'user':
        pass
