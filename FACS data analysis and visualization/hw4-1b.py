# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:05:36 2015

@author: jingyan
"""

from VSG_Module import *

class cell:                                     
    def __init__( self, H , V ):                                                      
        for i in range( len(H) ):
            setattr( self, H[i] , max(0.1, float(V[i])) )
            

F=open('NormalMarrowFlow.txt', mode='rU')        
Header_List=F.next().strip().split('\t') 
N_CD4 = 0
N_CD8 = 0
S_CD4high = 0
S_CD4low = 0
S_CD8low = 0
S_CD8high = 0
D1={} 
for L0 in F:                                     
    L1=L0.strip().split('\t')
    c=cell(Header_List,L1)
    if c.CD3>5.0 and c.CD4>0.1 and c.CD8>0.1:                         
        if c.CD4 >= 10 and c.CD8 < 20:
            N_CD4 += 1
            S_CD4high += c.CD4
            S_CD8low += c.CD8
        if c.CD4 <10 and c.CD8 >= 20:
            N_CD8 += 1
            S_CD4low += c.CD4
            S_CD8high += c.CD8
        x_key=int(log(c.CD4)*10) ## Calculating the integer part of  log(x)*10 for each x splits x values into bins,
        y_key=int(log(c.CD8)*10) 
        if not((x_key,y_key) in D1):
            D1[(x_key,y_key)]=0
        D1[(x_key,y_key)]+=1

for (x_key,y_key) in D1:
    xp=e**(x_key/10.0) ## This arithmetic converts the index value x_key back into the original (pre-log) x value for each bin
    yp=e**(y_key/10.0) 
    vrect( xc=10*x_key , yc=10*y_key, r=5 , fill=D1[(x_key,y_key)] , xg=xp , yg=yp) 

vgrid( gylog=True, gxlog=True, gxlabel='CD4', gylabel='CD8', gtitle='QuadGate.py')

## plot some lines for the desired quadrant gate
vline(x1=100*log(0.1),y1=100*log(20),x2=100*log(1000),y2=100*log(20),stroke=red, strokewidth=2)
vline(x1=100*log(10),y1=100*log(0.1),x2=100*log(10),y2=100*log(1000),stroke=red, strokewidth=2)
vcircle(x1 = 10*int(log(S_CD4high/N_CD4)*10), yc= 10*int(log(S_CD8low/N_CD4)*10), r = 10, fill = 'red')
vcircle(x1 = 10*int(log(S_CD4low/N_CD8)*10), yc= 10*int(log(S_CD8high/N_CD8)*10), r = 10, fill = 'red')
vcolorkey() ## vcolorkey() displays something like a color key for color values that have been set using VSG's numerical spectrum 

vdisplay()
print N_CD4, N_CD8
print S_CD4high/N_CD4, S_CD8low/N_CD4, S_CD4low/N_CD8, S_CD8high/N_CD8

F.close()