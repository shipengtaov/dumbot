#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import requests

name = ['qiushibaike', 'qb']

qiushibaike_baseurl = 'http://www.qiushibaike.com'

qiushibaike_urls = {
    'hot': 'http://m2.qiushibaike.com/article/list/suggest?count=20&page=%d',
}

def help():
    return {
        "result": '''Usage: python run.py quishibaike [options]
Options:
    hot; default:hot
    quibai_page=<number> : page number'''
    }

def results(plugin_args=[], plugin_kwargs={}, pipeline={}, parser_args=None):
    url_type = plugin_args[0] if plugin_args else 'hot'
    url = qiushibaike_urls.get(url_type)
    if not url:
        yield {
            'result': "sorry, 没有 %s 选项" %url_type,
            'pipeline': pipeline
        }
        return

    page = int(plugin_kwargs.get('qiubai_page')) if plugin_kwargs.get('qiubai_page') else 1
    url = url %page
    try:
        ret = requests.get(url, timeout=10)
        ret_dict = ret.json()
    except:
        yield {
            'result': '请求糗事百科api出现错误',
            'pipeline': pipeline
        }
        return

    items = ret_dict.get('items')
    qiubai_count = int(plugin_kwargs.get('qiubai_count', 1))
    for i in range(qiubai_count):
        if i > len(items)-1:
            break
        if qiubai_count == 1:
            item = random.choice(items)
        else:
            item = items[i]
        url = qiushibaike_baseurl+'/article/'+str(item['id'])

        result = ''
        result += item.get('content', '').encode('utf-8') + '\n'
        result += 'url: %s\n' % url

        pipeline.update({
            'url': url,
            'say': item.get('content', '').encode('utf-8'),
            'content': result,
        })

        # yield dict(result=result, pipeline=pipeline)
        yield dict(result=result, pipeline=pipeline)
