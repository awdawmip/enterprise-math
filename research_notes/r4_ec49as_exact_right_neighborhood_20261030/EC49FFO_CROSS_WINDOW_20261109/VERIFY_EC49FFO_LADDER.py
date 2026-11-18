#!/usr/bin/env python3
"""Direct native X6/DFA witness verifier for EC49FFO's analytic extension ladder."""
from collections import Counter
import json
ORDER='acdefg'
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),
   (4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
base={4:'fegc',2:'fegd',8:'gfec',1:'gfed'}
high={16:'fegfg',32:'gfefg'}

def obs(w):
    s=0
    for a in w:s=T[s][ORDER.index(a)]
    return SIG[s]
def micro(w):return tuple(v for c in w for v in OPS[c])
def pref(words):
    return {t[:i] for w in words for t in [micro(w)] for i in range(1,len(t)+1)}
def check(h,k,w,signature):
    x,y,z=k
    cc=Counter(w)
    assert cc['a']==z-1 and cc['e']==z and cc['c']+cc['d']==x+y-h-1
    assert cc['f']==h+1-y-2*z and cc['g']==h+1-x
    assert obs(w)==signature
    t=micro(w)
    assert len(t)==2*(x+y+z-1)
    ct=Counter(t)
    assert tuple(ct[i]-ct[-i] for i in range(1,7))==(2,0,0,0,0,0)
    assert tuple(ct[i] for i in (1,2,3))==k

def run():
    rows=[]
    for m in range(1,33):
        words=[]
        for j in range(m+1):
            for signature,root in base.items():
                w=root+'g'*j
                check(4+j,(4,2+j,1),w,signature)
                words.append(w)
        for signature,w in high.items():
            check(5,(4,2,1),w,signature)
            words.append(w)
        actual=len(pref(words)); expected=38+8*m
        assert actual==expected,(m,actual,expected)
        rows.append({'m':m,'keys':m+1,'words':len(words),'cost':actual})
    print(json.dumps({'status':'EXACT_NATIVE_DFA_CHECK_PASS','cases':len(rows),
      'special_22_path_case':rows[3],'first_two':rows[:2],'last':rows[-1]},
      ensure_ascii=False))
if __name__=='__main__':run()
