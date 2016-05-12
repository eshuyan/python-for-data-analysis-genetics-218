# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:50:50 2015

@author: jingyan
"""

File1 = open('fastQfile.txt', mode='rU')
upstreammir81 = 0
mir81 = 'TGAGATCATCGTGAAAGCTAGT' 

for line in File1:
    if mir81 in line and line[0:4] == 'GCAG':
        mir81pos = line.find(mir81)
        if mir81pos != 4:
            upstreammir81 += 1
            print line
print upstreammir81