# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 19:59:02 2018

@author: dell
"""

plaincode = input('请输入明文：')
for p in plaincode :
  if ord('a' or 'A') <= ord(p) <= ord('z' or 'Z') :
    print(chr(ord('a' or 'A') + (ord(p) - ord('a' or 'A') + 12)%26),end = '')
  else:
    print(p,end = '')
   