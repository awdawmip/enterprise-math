#!/usr/bin/env python3
"""Independent Stage490-B finite verifier; full stress source separately archived."""
from collections import Counter
from itertools import product, permutations
from math import factorial
import json

D='ABCDEFGHIJKL'  # +E1..+E6 and -E1..-E6
T='ABGABA';W='GH';j,l=10,11

def edges(s):return Counter(zip(s,s[1:]))
def E(a,b):
    ea,eb=edges(a),edges(b)
    return Counter({e:ea[e]-eb[e] for e in product(D,repeat=2)})
def edit(s,i,z):return s[:i-1]+z+s[i:]

def interaction():
    n=nonzero=0
    for a,b,c,d in product('ABGH',repeat=4):
        s=a+b+c+d
        for x,y in product(D,repeat=2):
            delta=E(a+x+y+d,s)
            d1=E(a+x+c+d,s);d2=E(a+b+y+d,s)
            correction=Counter({p:int(p==(x,y))-int(p==(x,c))
                                  -int(p==(b,y))+int(p==(b,c)) for p in product(D,repeat=2)})
            assert all(delta[e]==d1[e]+d2[e]+correction[e] for e in product(D,repeat=2))
            n+=1
            nonzero+=int(any(correction.values()))
    return n,nonzero

def q_only_pair():
    left=T+W+'A'+'AAAABA'+'A';right=T+W+'A'+'AAABAA'+'A'
    def vec(s):return tuple(s.count(D[i])-s.count(D[i+6]) for i in range(6))
    def eq(a,b):return len(a)==len(b) and vec(a)==vec(b) and edges(a)==edges(b)
    todo=[(left,right,0,0,0,0)];seen=set()
    while todo:
        a,b,pop,app,sj,sl=todo.pop()
        if (a,b,pop,app,sj,sl) in seen:continue
        seen.add((a,b,pop,app,sj,sl))
        assert eq(a,b)
        if not pop and len(a)>1:todo.append((a[:-1],b[:-1],1,app,sj,sl))
        if not app:todo.extend((a+z,b+z,pop,1,sj,sl) for z in D)
        if not sj:todo.extend((edit(a,j,z),edit(b,j,z),pop,app,1,sl) for z in D)
        if not sl:todo.extend((edit(a,l,z),edit(b,l,z),pop,app,sj,1) for z in D)
    return len(seen)

def euler_star():
    star='A'+''.join(x+'A' for x in D[1:])
    assert len(star)==23 and len(edges(star))==22
    classes=11*10*9;mass=factorial(8);total=factorial(11)
    assert classes*mass==total
    keys=[''.join(z) for z in permutations(D[1:],3)]
    assert len(keys)==classes and keys==sorted(keys)
    for k in (0,classes//2,classes-1):
        assert keys.index(keys[k])==k
    small=Counter(''.join(t[:2]) for t in permutations('BCGHI'))
    assert len(small)==20 and sum(small.values())==120
    assert set(small.values())=={6}
    return {'active_signed_directions':12,'active_directed_edges':22,
            'classes':classes,'mass_per_class':mass,'raw_population':total,
            'small_exact_histories':120,'small_classes':20}

if __name__=='__main__':
    print(json.dumps({'interaction_checks':interaction(),
                      'exhaustive_Q_states':q_only_pair(),
                      'signed_Euler':euler_star()},sort_keys=True))
