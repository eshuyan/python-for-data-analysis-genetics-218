# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:05:36 2015

@author: jingyan
"""

class cell:                                     
    def __init__( self, H , V ):                                                      
        for i in range( len(H) ):
            setattr( self, H[i] , max(0.1 , float(V[i])) )
F=open('NormalMarrowFlow.txt',mode='rU')        
Header_List=F.next().strip().split('\t') 
N_CD4 = 0
N_CD8 = 0
D1={} 
for L0 in F:                                     
    L1=L0.strip().split('\t')
    c=cell(Header_List,L1)
    if c.CD3>5.0 and c.CD4<10 and c.CD8 >20:
        N_CD8 += 1
    if c.CD3>5.0 and c.CD4 >10 and c.CD8 < 20:
        N_CD4 += 1
print N_CD4, N_CD8
F.close()            
        

