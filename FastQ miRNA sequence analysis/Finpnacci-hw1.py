# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:32:28 2015

@author: jingyan
"""

Last = int(raw_input('Please input the last number:'))
SecondtoLast = int(raw_input('please input another number:'))
Repeats = int(raw_input('Please input how many numbers you want to appear in the Finonpnacci:'))
i = 0


for i in range(Repeats):
    NewLast = Last - SecondtoLast
    SecondtoLast = Last
    Last = NewLast
    print Last
    i += 1
    
    
    