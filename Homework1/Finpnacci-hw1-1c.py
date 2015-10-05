# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:32:28 2015

@author: jingyan
"""

Last = 4
SecondtoLast = 1
i = 0

for i in range(610):
    NewLast = Last - SecondtoLast
    SecondtoLast = Last
    Last = NewLast
    i += 1
    if i == 60 or i == 600:
        print Last
    
    