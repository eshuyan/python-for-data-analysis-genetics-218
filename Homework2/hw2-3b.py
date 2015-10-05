# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 17:03:47 2015

@author: jingyan
"""

F1 = open('ColiDH1.fa')
seqdata = ''
for L in F1:
    if L =='' or L[0] == '>':
        continue
    seqdata += L.strip()
F1.close()
base1 = ['A', 'T', 'G', 'C']
qnucleotide_sequences1=[]                 ## an array that will contain all sixteen dinucleotide sequences
qnucleotide_instances1=[0]*16*16
for b1 in base1:
    for b2 in base1:
        for b3 in base1:
            for b4 in base1:
                q = b1 + b2 +b3 +b4
                qnucleotide_sequences1.append(q)

#print qnucleotide_sequences1
lenSeq1=len(seqdata)
                         
seqdata+=seqdata[:10]                            
for i1 in range(lenSeq1):  
    SeqWord1=seqdata[i1:(i1+4)]                
    #SeqWord1=seqdata[i1] + seqdata[i1+1]+seqdata[i1+2] +seqdata[i1+3]                 
    Seq_index1=qnucleotide_sequences1.index(SeqWord1) 
    qnucleotide_instances1[Seq_index1]+=1
for i2 in range(16*16):                       ## Output the index, sequence, and number of hits for each
        print (str(i2)+'\t'+qnucleotide_sequences1[i2]+'\t'+str(qnucleotide_instances1[i2]))
                
                