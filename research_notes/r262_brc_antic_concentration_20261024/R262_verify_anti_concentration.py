#!/usr/bin/env python3
"""Exact check of R262's typed BRC 8-state Laurent transfer. No native P000 physics."""
from __future__ import annotations
from collections import Counter,defaultdict
from itertools import product
import sympy as S

EDGE={0:{0:(2,-1,-1),1:(2,1,-1)},1:{0:(0,-1,-1),1:(0,1,-1)},2:{0:(1,1,1),1:(2,1,-1)}}
DFA={0:{0:1,1:0},1:{0:2,1:0},2:{0:2,1:2}}
BASE=((0,1),(2,0),(2,1),(1,0))
STATES=tuple((q,last,e) for q,last in BASE for e in (1,-1))
INDEX={s:i for i,s in enumerate(STATES)}
def twisted(z):
    mat=S.zeros(8)
    for i,(q,last,e) in enumerate(STATES):
        for a,(qq,eta,b) in EDGE[q].items():
            if a==last==0: continue
            ee=eta*e
            mat[INDEX[(qq,a,ee)],i]+=z**(ee*b)
    return mat
def primitive(word):
    q,r,e,k=0,0,1,0
    for a in word:
        qq,eta,b=EDGE[q][a]
        q,r,e,k=qq,DFA[r][a],eta*e,eta*k+b
    return q,r,e,k
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
def run():
    z,x,theta=S.symbols('z x theta',nonzero=True)
    T=twisted(z)
    expected=(x*x+1)*(x**6-(z+z**-1)*x**5+2*x*x-1)
    assert S.cancel((x*S.eye(8)-T).det()-expected)==0
    assert T.subs(z,-1)==-T.subs(z,1)
    assert S.factor(expected.subs(z,1))==(x-1)**2*(x*x+1)*(x*x-x-1)*(x*x+x+1)
    phi=(1+S.sqrt(5))/2
    f=x**6-2*S.cos(theta)*x**5+2*x*x-1
    fl=S.simplify(S.diff(f,x).subs({x:phi,theta:0}))
    ftt=S.simplify(S.diff(f,theta,2).subs({x:phi,theta:0}))
    assert fl==2*S.sqrt(5) and S.simplify(ftt-2*phi**5)==0
    assert S.simplify(ftt/(phi*fl)-S.Rational(3,2)-7*S.sqrt(5)/10)==0
    adjacency=T.subs(z,1)
    cycle=((2,1,1),(1,0,1),(0,1,1),(2,0,-1),
           (2,1,-1),(1,0,-1),(0,1,-1),(2,0,1),(2,1,1))
    assert set(cycle[:-1])==set(STATES)
    for u,v in zip(cycle,cycle[1:]): assert adjacency[INDEX[v],INDEX[u]]==1
    for e in (1,-1):
        assert adjacency[INDEX[(2,1,e)],INDEX[(2,1,e)]]==1
    assert T[INDEX[(2,1,1)],INDEX[(2,1,1)]]==z**-1
    assert T[INDEX[(2,1,-1)],INDEX[(2,1,-1)]]==z

    restricted=Counter({(0,1,1,0):1})
    full=Counter({(0,0,1,0):1})
    words=checks=0
    sample={}
    for m in range(141):
        assert sum(restricted.values())==fib(m+2)
        for (q,last,e,t),v in restricted.items():
            assert full[(q,1 if last==0 else 0,e,e*t)]==v
            checks+=1
        if m<=13:
            raw=Counter(); clean=Counter()
            for w in product((0,1),repeat=m):
                q,r,e,k=primitive(w)
                raw[(q,r,e,k)]+=1
                if r<2: clean[(q,w[-1] if w else 1,e,e*k)]+=1
                words+=1
            assert raw==full and clean==restricted
        if m in (8,13,20,30,50,80,100,140):
            buckets=defaultdict(lambda:[0,0,0])
            for (q,r,e,k),v in full.items(): buckets[(q,e,k)][r]+=v
            sample[m]={'max_r1':str(max([v for (_,last,_,_),v in restricted.items() if last==0],default=0)),
                       'M':str(max((min(vals) for vals in buckets.values()),default=0))}
        if m<140:
            rr=Counter(); ff=Counter()
            for (q,last,e,t),v in restricted.items():
                for a,(qq,eta,b) in EDGE[q].items():
                    if last==a==0: continue
                    ee=eta*e
                    rr[(qq,a,ee,t+ee*b)]+=v
            for (q,r,e,k),v in full.items():
                for a,(qq,eta,b) in EDGE[q].items():
                    ff[(qq,DFA[r][a],eta*e,eta*k+b)]+=v
            restricted,full=rr,ff
    assert words==16383 and checks==75082,(words,checks)
    print('PASS: symbolic determinant/curvature, 8-state primitive cycle, raw_words=',words,
          'atom_crosschecks=',checks,'selected_fibres=',sample)

if __name__=='__main__': run()
