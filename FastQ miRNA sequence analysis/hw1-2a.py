# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
File1 = open('fastQfile.txt', mode='rU')
perfectMir81 = 0
mir81 = 'TGAGATCATCGTGAAAGCTAGT'

for line in File1:
    if line[0:4] == 'GCAG' and line[4:26]== mir81 and line[26:36] == 'CACTCGGGCA':
        
        perfectMir81 += 1
print 'Mir81:', perfectMir81
        
