# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 21:27:02 2018

@author: dell
"""


import turtle
A = 200
turtle.setup(500,500,10,10)

while A > 2:
    B = 0
    turtle.seth(B)
    turtle.fd(A)
    
    B = B + 120
    turtle.seth(B)
    turtle.fd(A)
    
    A = A - 2
    B = B + 120
    turtle.seth(B)
    turtle.fd(A)
    
  
    
    A = A - 2
turtle.done()
