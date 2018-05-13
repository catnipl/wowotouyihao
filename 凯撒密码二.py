# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:07:51 2018

@author: dell
"""

plaincode = input('请输入明文：')
for p in plaincode :
  if ord('a') <= ord(p) <= ord('z') or ord('A') <= ord(p) <= ord('Z') :
    print(chr(ord('a') + (ord(p) - ord('a') + 12)%26),end = '') or  print(chr(ord('A') + (ord(p) - ord('A') + 12)%26),end = '')
 
 
   
  else:
    print(p,end = '')
  