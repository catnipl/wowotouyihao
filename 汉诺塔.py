# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:38:19 2018

@author: dell
"""

def hanoi(a,b,c,n):
    if n == 1:
        print(a + "-->" + c)
    else:
        hanoi(a,c,b,n-1)
        hanoi(a,b,c,1)
        hanoi(b,a,c,n-1)
        
        
hanoi('a','b','c',3)