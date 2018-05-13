# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:12:05 2018

@author: dell
"""

from datetime import datetime
birthday = datetime(1973,2,4)
birthday.strftime("%Y-%m-%d")
birthday.strftime('%b %d, %Y')
birthday.strftime('%d %B %Y')
birthday.strftime('%Y/%m/%d')
birthday.strftime('%m/%d/%Y')
birthday.strftime('%A/%Y/%m/%d')