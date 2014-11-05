#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@version: 0.1
@author: 0x7c0
'''

import os, sys
from pyfiglet import Figlet
from nginxparser import load

## 參數定義
vhost_path = "/usr/local/etc/nginx/vhost";

def init():
    printTitle();
    getProjects(vhost_path);

def printTitle():
    # 腳本頭部
    script_name = "NGINX vhost tools"
    f = Figlet()
    print f.renderText(script_name)
    print "Author: JackLam(jack@wizmacau.com)"
    print ("-"*80)[:80]

# 掃描項目
def getProjects(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            getProjectInfo(dirpath + "/" + filename)


def getProjectInfo(file_path):
    print file_path
    print load(open(file_path, "r"))

init();