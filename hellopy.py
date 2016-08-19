#!/usr/bin/env python2.6
#-*-coding:utf8;-*-
#版权所有仿冒必究
from __future__ import print_function # Python2.x中使用print()函数
import urllib2
import sys

class target:
    url="http://www.google.com"
class record:
    file=sys.stdout

response = urllib2.urlopen(target.url)

print(response.read(), file=record.file)
print(target.url, file=sys.stdout)


