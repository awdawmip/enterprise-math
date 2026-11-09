#!/usr/bin/env python3
"""Independent native signed-X6 witness check for H2/Hh, h=11..13."""
from collections import Counter
OP='acdefg'
C={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)

def analyze(word,h,expected):
    q=0
    for c in word:q=T[q][OP.index(c)]
    assert len(word)==h and SIG[q]==expected,(h,word,SIG[q],expected)
    counts=Counter(word);z=counts['e'];x=h+1-counts['g'];y=h+1-2*z-counts['f']
    assert z==counts['a']+1 and min(x,y,z)>0
    assert counts['c']+counts['d']==x+y-h-1
    steps=tuple(t for c in word for t in C[c]);actual=Counter(steps)
    assert tuple(actual[i]-actual[-i] for i in range(1,7))==(2,0,0,0,0,0)
    assert (actual[1],actual[2],actual[3])==(x,y,z)
    return (x,y,z),steps

def check(h):
    base={1:'de',2:'ed',4:'ce',8:'ec'}
    high={1:'gfe'+'g'*(h-4)+'d',2:'fe'+'g'*(h-3)+'d',4:'fe'+'g'*(h-3)+'c',8:'gfe'+'g'*(h-4)+'c'}
    keys=set();prefixes=set()
    for H,paths in ((2,base),(h,high)):
        for s,word in paths.items():
            k,steps=analyze(word,H,s);keys.add(k)
            for n in range(1,len(steps)+1):prefixes.add(steps[:n])
    assert keys=={(3,1,1),(4,h-2,1)}
    assert len(prefixes)==4*h+42
    print('h',h,'words',high,'keys',sorted(keys),'native_prefixes',len(prefixes),'PASS')

for h in (11,12,13):check(h)
