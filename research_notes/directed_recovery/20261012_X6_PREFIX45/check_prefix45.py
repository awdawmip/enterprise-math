#!/usr/bin/env python3
"""Portable exact reference for PREFIX-45; no third-party packages."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from math import lcm
I=tuple(range(6)); X=(1,0,2,3,4,5); Y=(0,2,1,3,4,5)
def mul(p,q): return tuple(p[q[i]] for i in range(6))
assert mul(X,Y)!=mul(Y,X)

def classify(predicates,A,B,tail_periods):
    L=lcm(*tail_periods)
    witness=next(((d,tuple(f(d) for f in predicates),
                    tuple(f(d+L) for f in predicates))
                for d in range(A-L+1,B)
                if any(f(d)!=f(d+L) for f in predicates)),None)
    if witness is not None: return (None,L,witness)
    p=next(p for p in range(1,L+1) if L%p==0 and
           all(f(r)==f(r+p) for r in range(L) for f in predicates))
    return (p,L,None)

even=lambda d:d%2==0
div3=lambda d:d%3==0
mod4=lambda d:d%4 in (0,1)
threshold=lambda d:d>=0
exception=lambda d:d%2==0 and d!=0
assert classify((even,div3),-10,10,(2,2,3,3))[0]==6
assert classify((even,div3,mod4),-10,10,(2,2,3,3,4,4))[0]==12
assert classify((lambda d:True,),-1,0,(1,1))[0]==1
assert classify((threshold,),-1,0,(1,1))[0] is None
assert classify((exception,),-1,1,(2,2))[0] is None

def histogram(d,w,predicates):
    q=F(1); effect=I; source=[]
    for j,s in enumerate(w):
        if s in 'ab':
            d+=1 if s=='a' else -1
            q*=F(1,2); effect=mul(X if s=='a' else Y,effect)
            source.append('r')
        else:
            if j!=len(w)-1: return Counter()
            idx=int(s)-1
            if not predicates[idx](d): return Counter()
            q*=F(1,3) if s=='1' else F(1,5)
            source.append('z'+s)
            return Counter({(q,effect,tuple(source)):2 if s=='1' else 1})
    return Counter({(q,effect,tuple(source)):1})

words=[p+(z,) for n in range(3)
       for p in product('ab',repeat=n) for z in ('1','2')]
assert len(words)==14
states=range(-18,19)
profiles={d:tuple(tuple(sorted(histogram(d,w,(even,div3)).items()))
                 for w in words) for d in states}
assert len(set(profiles.values()))==6
for d in states:
    for e in states:
        assert (profiles[d]==profiles[e])==(d%6==e%6)

witnesses=0
for d in range(-9,10):
    for e in range(d+1,10):
        shift=-e
        w=tuple('a'*shift if shift>=0 else 'b'*(-shift))+('1',)
        assert not histogram(d,w,(threshold,))
        assert histogram(e,w,(threshold,))
        witnesses+=1
assert witnesses==171
print('EXACT_REFERENCE_PASS',{'histogram_evaluations':len(states)*len(words),
      'pair_checks':len(states)**2,'profile_classes':6,
      'threshold_witnesses':witnesses,'noncommuting':True})
