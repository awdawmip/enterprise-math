#!/usr/bin/env python3
"""Independently verify the native signed-X6 H2/Hh witnesses and prefix costs."""
from collections import Counter
ORDER='acdefg'
CODE={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),
   (4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIGN=(0,0,4,1,16,32,8,2,0)
def check_path(word,h,signature):
    assert len(word)==h
    q=0
    for symbol in word:
        q=T[q][ORDER.index(symbol)]
    assert SIGN[q]==signature,(h,word,signature,SIGN[q])
    count=Counter(word);e=count['e']
    assert e==count['a']+1 and e>=1
    full_key=(h+1-count['g'],h+1-2*e-count['f'],e)
    assert min(full_key)>0
    signed_steps=tuple(i for symbol in word for i in CODE[symbol])
    hist=Counter(signed_steps)
    assert tuple(hist[i]-hist[-i] for i in range(1,7))==(2,0,0,0,0,0)
    assert tuple(hist[i] for i in (1,2,3))==full_key
    return full_key,signed_steps
def check(h):
    assert h>=4
    baseline={1:'de',2:'ed',4:'ce',8:'ec'}
    longer={1:'gfe'+'g'*(h-4)+'d',2:'fe'+'g'*(h-3)+'d',
            4:'fe'+'g'*(h-3)+'c',8:'gfe'+'g'*(h-4)+'c'}
    keys=set();prefixes=set()
    for depth,words in ((2,baseline),(h,longer)):
        for sig,word in words.items():
            key,steps=check_path(word,depth,sig)
            keys.add(key)
            prefixes.update(steps[:i] for i in range(1,len(steps)+1))
    assert keys=={(3,1,1),(4,h-2,1)}
    assert len(prefixes)==4*h+42,(h,len(prefixes))
    return len(prefixes)
if __name__=='__main__':
    samples=[(h,check(h)) for h in range(31,101)]
    print({'range':[31,100],'verified_instances':len(samples),
           'all_pass':True,'first':samples[0],'last':samples[-1]})
