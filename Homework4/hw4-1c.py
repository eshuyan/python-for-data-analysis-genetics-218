# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:45:23 2015

@author: jingyan
"""

#from VSG_Module import *
class cell:                                     
    def __init__( self, H , V ):                                                      
        for i in range( len(H) ):
            setattr( self, H[i], max(0.1 , float(V[i])))
F=open('NormalMarrowFlow.txt',mode='rU')        
Header_List=F.next().strip().split('\t')

n = len(Header_List)

S_CD4 = [0]*n
S_CD8 = [0]*n
N_CD4 = 0
N_CD8 = 0
for L0 in F:                                     
    L1=L0.strip().split('\t')
    c=cell(Header_List,L1)
    if c.CD3>5.0 and c.CD4 >= 10 and 0.1 < c.CD8 < 20:
        N_CD4 += 1
        for i in range(n): 
            S_CD4[i] += getattr(c, Header_List[i])       
    if c.CD3> 5.0 and 0.1< c.CD4 <10 and c.CD8 >= 20:
        N_CD8 += 1
        for i in range(n):
            
            S_CD8[i] += getattr(c, Header_List[i])
Average_CD4high = [0]*n
Average_CD8high = [0]*n

print 'Attribute' +'\t'+'CD4+CD8- mean' +'\t' +'CD4-CD8+ mean'+'\t'+'ratio'
for i in range(n):
    Average_CD4high[i] +=S_CD4[i]/N_CD4
    Average_CD8high[i] +=S_CD8[i]/N_CD8
    print Header_List[i] + '\t' +str(Average_CD4high[i]) +'\t' +str(Average_CD8high[i]) +'\t' +str(Average_CD4high[i]/Average_CD8high[i])
F.close()
           