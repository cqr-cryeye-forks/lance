#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-12-07 11:18:32
# Email : b4zinga@outlook.com
# Func  :

import requests

def run(url):
    """Docker Remote API unauth"""
    url = url + ":2375/info"
    req = requests.get(url)
    if "Containers" in req.text:
        print(req.text)
        return "Docker Remote API unauth Vulnerable"
    else:
        return False