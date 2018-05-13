# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:49:43 2018

@author: dell
"""

def multi(*a):
    if len(a) == 0:
        return 0
    t = 1
    for i in a:
        t = t * i
    return t

print( multi())