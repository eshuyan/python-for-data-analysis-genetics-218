# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:37:44 2015

@author: jingyan
"""

F1 = open('ColiDH1.fa')
seqdata = ''
for L in F1:
    if L =='' or L[0] == '>':
        continue
    seqdata += L.strip()
F1.close()

F2 = F1.replace('A', 't')
F3 =F2.replace('T','a')
F4 = F3.replace('G', 'c')
F5= F4.replace('C','g')
F6 = F5[::-1]
F7 = F6.upper()

    