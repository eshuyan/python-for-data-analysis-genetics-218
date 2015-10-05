# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:46:13 2015

@author: jingyan
"""

File1 = open('fastQfile.txt', mode='rU')
linkerbrokenMir81 = 0
mir81 = 'TGAGATCATCGTGAAAGCTAGT'

for line in File1:
    if mir81  in line and line[0:4] != 'GCAG':
        linkerbrokenMir81 += 1
        print line
print linkerbrokenMir81
        