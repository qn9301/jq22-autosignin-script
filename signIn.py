#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests  
import re
# 模拟浏览器
headers = {'User-Agent':'MMozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}  
# 创建cookie，请手动抓包获取你自己对应的cookie
cookies = dict()
cookies['OUTFOX_SEARCH_USER_ID_NCOO'] = '123123'
cookies['CityCookie'] = 'y'
cookies['ASP.NET_SessionId'] = 'xxxxxx'
cookies['MydlCookie'] = 'yhdlId=xxxx&yhdlPw=xxxx'
cookies['Hm_lvt_b3a3fc356d0af38b811a0ef8d50716b8'] = 'xxxx,xxxx'
cookies['Hm_lpvt_b3a3fc356d0af38b811a0ef8d50716b8'] = 'xxxx'

url = "http://www.jq22.com/signIn.aspx"
r = requests.get(url, headers=headers, cookies=cookies)
# 获取页面上的需要用来签到的键值对，用正则获取
html = r.text
param = {}
pattern = re.compile(r'name="__VIEWSTATEGENERATOR".*?value="(.*?)"',re.S)
res = re.findall(pattern, html)
param['__VIEWSTATEGENERATOR'] =res[0]
pattern = re.compile(r'name="__EVENTVALIDATION".*?value="(.*?)"',re.S)
res = re.findall(pattern, html)
param['__EVENTVALIDATION'] = res[0]
pattern = re.compile(r'name="__VIEWSTATE".*?value="(.*?)"',re.S)
res = re.findall(pattern, html)
param['__VIEWSTATE'] = res[0]
# 神坑，这个字段是必须要的，否则无法签到
param['Button1'] = '签 到'
# print(param)
r = requests.post(url, headers=headers, cookies=cookies, data=param)
# print(r.headers)
# print(r.text)
