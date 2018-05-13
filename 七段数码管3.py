# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:24:23 2018

@author: dell
"""

import turtle, datetime

strcol = ['red','blue','gold','violet','purple','green','yellow']

def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
    
    
def drawLine(draw, n):   #绘制单段数码管
    drawGap()
    turtle.pencolor(strcol[n])
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    
    
def drawDigit(digit): #根据数字绘制七段数码管
    drawLine(True,0) if digit in [2,3,4,5,6,8,9] else drawLine(False,0)
    drawLine(True,1) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False,1)
    drawLine(True,2) if digit in [0,2,3,5,6,8,9] else drawLine(False,2)
    drawLine(True,3) if digit in [0,2,6,8] else drawLine(False,3)
    turtle.left(90)
    drawLine(True,4) if digit in [0,4,5,6,8,9] else drawLine(False,4)
    drawLine(True,5) if digit in [0,2,3,5,6,7,8,9] else drawLine(False,5)
    drawLine(True,6) if digit in [0,1,2,3,4,7,8,9] else drawLine(False,6)
    
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) 
    
    
def drawDate(date):  #获得要输出的数字
    for i in date:
        if i == '-':
            turtle.pencolor("black")
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.fd(40) 
        elif i == '=':
            turtle.pencolor("black")
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '+':
            turtle.pencolor("black")
            turtle.write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
            
            
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.hideturtle()
    turtle.done()
    
    
main()