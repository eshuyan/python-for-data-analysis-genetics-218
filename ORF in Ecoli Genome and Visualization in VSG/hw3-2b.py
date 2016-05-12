# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 16:51:04 2015

@author: jingyan
"""
from VSG_Module import *
F = open('ColiDH1.fa', mode = 'rU')
S = ''
for L in F:
    if L[0]!='>':
        S = S+L.strip()
F.close()
antistartcodon = ['CAT','CAC','CAA']
antistopcodon = ['TTA','TCA','CTA']

orf = {}
for i in range(100000):
    if S[i:i+3] in antistopcodon:
        for j in range(i, 100000, 3):
            if S[j:j+3] in antistartcodon:   
                if not (j in orf) and j-i >500:
                    
                    orf[j]  = i    
                    break
for i in orf:
    print orf[i], i, -(i%3)

for j in sorted(orf.keys()):
    i = orf[j]
    frame =-(i%3)
    vline(x1=i/100, x2 = j/100, y1 = frame*100, y2 =frame*100, strokewidth = 10, stroke = green)
    vline(x1=0, x2=1000, y1=10, strokewidth = 10, stroke = red)
    for j in range(0,100001, 10000):
        vtext(text = str(j), xc=j/100, yc=30, font = "times 12 bold", stroke = black)
        vline(x1 = j/100, x2=j/100, y1=25, y2=15, stroke = black, strokewidth =1)
  
vdisplay()           