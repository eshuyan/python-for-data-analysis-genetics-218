# -*- coding: utf-8 -*-


F1 = open('mature.fa')

dogseqlist = []
humanseqlist =[]
remaneiseqlist = []
briggsaeseqlist = []
elegansseqlist = []
list_seq = F1.readlines()

n = len(list_seq)
for i in range(0, n, 2):
    if list_seq[i][0] == '>' and 'elegans' in list_seq[i]:
        elegansseqlist.append(list_seq[i+1].strip('\n'))
    if list_seq[i][0] == '>' and 'remanei' in list_seq[i]: 
        remaneiseqlist.append(list_seq[i+1].strip('\n'))
    if list_seq[i][0] == '>' and 'briggsae' in list_seq[i]: 
        briggsaeseqlist.append(list_seq[i+1].strip('\n'))
    if list_seq[i][0] == '>' and 'Canis' in list_seq[i]: 
        dogseqlist.append(list_seq[i+1].strip('\n'))
    if list_seq[i][0] == '>' and 'Human' in list_seq[i]: 
        humanseqlist.append(list_seq[i+1].strip('\n'))
F1.close() 

F2 = open('myDogsRNA.txt')
F3 = open('mydogrna2.txt', 'w')

for line in F2:
    pos = line.rfind('TCGT')   
    line = line[:pos]              #trimimg Cterminal linker
    line = line.replace('T','U')   #replaceing T with U
    if line not in dogseqlist and line not in humanseqlist and line in elegansseqlist and line in remaneiseqlist and line  in briggsaeseqlist:
        F3.write(line)
        print line
F2.close()
F3.close()