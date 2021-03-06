#! /usr/bin/env python
# coding: utf-8

import urllib.request
from bs4 import BeautifulSoup
import sys

def get_hinanjo_page(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    body = soup.find(id="wrap")
    title = body.h2.text
    print('---')
    print('title:' + title)
    print('---')
    content = body.p.get_text()
    print(content)


def hinanjo(page_num = 1):
    url = 'http://ehime.force.com/PUB_VF_HinanjyoList'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    for i in range(page_num):
        volunteer = soup.find_all("div", {"class": "volunteer"})[0]
        dls = volunteer.find_all("dl")
        dl = dls[i]
        get_hinanjo_page('http://ehime.force.com/' + dl.a.get('href'))

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        hinanjo(int(args[1]))
    else:
        hinanjo()
