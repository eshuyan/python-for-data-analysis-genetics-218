# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:57:06 2015

@author: jingyan
"""

F1 = open('Shakespeare.txt', mode = 'rU')
alltxt = F1.read()
F1.close()
allwords = alltxt.split()


D = {}
for n in range(len(allwords)-5):
    if allwords[n][0] == allwords[n][0].upper() and allwords[n+4][-1] == '!':
        words = str(allwords[n:n+5])
        if words not in D:
            D[words] = 1
        else:
            D[words] += 1
for w in D:
    if D[w] >1:
        print w
    

        