# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:49:39 2015

@author: jingyan
"""
a = 'ATGCAGCG'
#generating a list of orf sequences
def orf(list3):
    startcodon = ['ATG','GTG','TTG']
    stopcodon = ['TAA','TGA','TAG']
    orfs = []
    dict1 = {}
    for i in range(len(list3)):
        if list3[i:i+3] in startcodon:
            for j in range(i, len(list3), 3):
                if list3[j:j+3] in stopcodon:   
                    if not (j in dict1) and j-i >500:
                        dict1[j] = i
                        orfs.append(list3[i:j+3])
                    break
    return orfs
#count condon use in a giving list    
def count_condon(list4):
    dict2 = {}
    for i in list4:
        for j in range(0,len(i),3):
    
            if i[j:j+3] not in dict2:
                dict2[i[j:j+3]] = 1
            else:
                dict2[i[j:j+3]] += 1
    return dict2
#looking for reverse orf by first transfering into compliment reverseved verion    
def antisense(list1):
    dict1 = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    comlist = ''
    antilist = ''
    for i in range(len(list1)):
        comlist += dict1[list1[i]]
    antilist = comlist[::-1]
    return antilist
 #open ColiDH1 file   
F = open('ColiDH1.fa', mode = 'rU')
S = ''
for L in F:
    if L[0]!='>':
        S = S+L.strip()
F.close()

reverS = antisense(S[0:100000]) #transfer reversed compliment sequences
seq = orf(reverS) + orf(S[0:100000])#merge two orf lists

dictcondon = count_condon(seq)#count condon use in the combined lists
for i in dictcondon:
    print i +'\t' + str(dictcondon[i])
