# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:10:10 2015

@author: jingyan
"""

F1 = open('mature.fa')

dogseqlist = []

elegansseqlist = []
list_seq = F1.readlines()

n = len(list_seq)
for i in range(0, n, 2):
    if list_seq[i][0] == '>' and 'elegans' in list_seq[i]:
        
        elegansseqlist.append(list_seq[i+1].strip('\n'))
    if list_seq[i][0] == '>' and 'Canis' in list_seq[i]:
        
        dogseqlist.append(list_seq[i+1].strip('\n'))
F1.close() 

F2 = open('myDogsRNA.txt')
F3 = open('mydogrna.txt', 'w')

for line in F2:
    pos = line.rfind('TCGT')   
    line = line[:pos]              #trimimg Cterminal linker
    line = line.replace('T','U')   #replaceing T with U
    if line not in dogseqlist and line in elegansseqlist:
        F3.write(line)
        print line
F2.close()
F3.close()
