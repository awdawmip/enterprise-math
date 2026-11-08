#!/usr/bin/env python3
"""Exact signed-X6 independent witness verification for 23 word H4-mixed example."""
from collections import Counter, defaultdict
OP={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
    'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ALPHA='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
KEYS={(3,1,1),(3,2,1),(3,3,1),(3,4,1),(4,6,1)}
ROWS='''2 1 de
2 2 ed
2 4 ce
2 8 ec
3 16 feg
3 32 gef
4 1 gegd
4 8 gegc
4 16 fegg
5 16 feggg
5 32 geggf
6 16 fegggg
6 32 geggfg
7 1 gegggdd
7 2 edggdgg
7 4 ceggggc
7 8 gegggcc
8 1 geggfggd
8 2 fegggggd
8 4 ceggggfg
8 8 gegggcfg
9 16 feggggggf
9 32 geggfgggf'''
REQUIRED={2:{1,2,4,8},3:{16,32},4:{1,8,16},5:{16,32},
          6:{16,32},7:{1,2,4,8},8:{1,2,4,8},9:{16,32}}
edge=set();got=defaultdict(set)
for line in ROWS.splitlines():
    horizon,sigstr,word=line.split();h=int(horizon);sig=int(sigstr)
    counts=Counter(word);a,c,d,e,f,g=(counts[ch] for ch in ALPHA)
    key=(c+d+2*e+f,c+d+g,e)
    assert len(word)==h and e>=1 and a==e-1 and key in KEYS,(line,key)
    q=0;steps=[];endpoint=[0]*6
    for ch in word:
        q=T[q][ALPHA.index(ch)]
        for axis_step in OP[ch]:
            steps.append(axis_step)
            axis=abs(axis_step)-1
            endpoint[axis]+=1 if axis_step>0 else -1
            edge.add(tuple(steps))
    assert SIG[q]==sig and tuple(endpoint)==(2,0,0,0,0,0),(line,key,SIG[q],endpoint)
    assert sig not in got[h]
    got[h].add(sig)
assert dict(got)==REQUIRED,got
assert len(edge)==129,len(edge)
print('PASS: 23 signed X6 words, exact five full BRC keys, all H2-H9 observer signatures, endpoint +2 E1, 129 distinct signed prefix edges')
