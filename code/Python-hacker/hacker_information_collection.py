# -*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
import re
import json
start = time.time()

def chax():
    lid = input('请输入你要查询的域名:')
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    pattern = re.compile(r'http://|https://')
    lid = re.sub(pattern, '', lid).rsplit('/')[0]
    url = "http://site.ip138.com/domain/read.do?domain=" + format(lid)
    urldomain = "http://site.ip138.com/{}/domain.htm".format(lid)
    url2 = "http://site.ip138.com/{}/beian.htm".format(lid)
    url3 = "http://site.ip138.com/{}/whois.htm".format(lid)
    rb = requests.get(url, headers=head)
    rb1 = requests.get(urldomain, headers=head)
    rb2 = requests.get(url2, headers=head)
    rb3 = requests.get(url3, headers=head)
    # gf = BeautifulSoup(rb.content, 'html.parser')

    print('[+]IP解析记录')
    gf = rb.content.decode()
    dict_json = json.loads(gf)
    for v in dict_json['data']:
        print('\nIP:【'+ v['ip'] + '】\nSIGN:【' + v['sign'] + '】\n' )
    gf1 = BeautifulSoup(rb1.content, 'html.parser')
    print('[+]子域名查询')
    for v in gf1.find_all('p'):
         link2 = v.get_text()
         print(link2)
    gf2 = BeautifulSoup(rb2.content, 'html.parser')
    print('[+]备案查询')
    for s in gf2.find_all('p'):
        link3 = s.get_text()
        print(link3)
    gf3 = BeautifulSoup(rb3.content, 'html.parser')
    print('[+]whois查询')
    for k in gf3.find_all('p'):
        link4 = k.get_text()
        print(link4)


if __name__ == "__main__":
    chax()
    end=time.time()
    print('查询耗时:',end - start)
