#!/usr/bin/env python2
#-*-coding:utf8;-*-
#版权所有仿冒必究
from __future__ import print_function # Python2.x中使用print()函数
from urllib2 import urlopen
from urllib2 import URLError
import sys

class target:
    protocol="http"
    host="www.google.com"
    port="80"
    path="/"
    parameters=""
    url="".join([protocol, "://", host, ":", port, path, parameters])
class record:
    file=sys.stdout

print(target.url)
try:
    response = urlopen(target.url)
    print(response.read(), file=record.file)
except URLError as e:
    print(e, sys.stderr)
