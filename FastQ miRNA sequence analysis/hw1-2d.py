# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:56:47 2015

@author: jingyan
"""

File1 = open('fastQfile.txt', mode='rU')
onemutation = 0
mir81 = 'TGAGATCATCGTGAAAGCTAGT' 

for line in File1:
    if  line[0:4] == 'GCAG' and line[26:36] == 'CACTCGGGCA':
        mir = line[4:26]
        count = 0
        for i in range(22):
            if mir[i] != mir81[i]:
                count += 1
            if count >1:
                break
        if count == 1:
            print line
            onemutation += 1
            
print onemutation