#!/usr/bin/env python3
"""R690: exact R687 E* S3 square-kernel, minimal polynomials and BRC positive-mass verification."""
from itertools import product, permutations
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json

I=(0,1,2); G=list(permutations(I)); EVEN=(0,2,4); ODD=(1,3,5)
T=(0,2,1); C=(1,2,0); D=(2,0,1)
TAB={(0,0):(0,1,2),(1,0):(0,1,3),(2,0):(0,1,4),
     (0,1):(0,2,3),(1,1):(1,2,3),(2,1):(0,1,3)}
EXPECT={0:Counter({I:24,T:18,C:6,D:12}),
        1:Counter({I:42,C:12,D:6}),
        2:Counter({I:42,T:18})}
MIN={0:[-2,-43,270,-475,250],
     1:[-31,141,-210,100],
     2:[2,-7,5]}

def phase(z):return sum(z[i] for i in EVEN)%3,sum(z[i] for i in ODD)%2
def move(f,s,t):
    gone=next(iter(set(s)-set(t))); new=next(iter(set(t)-set(s)))
    return tuple(new if x==gone else x for x in f)
def square(z,i,j,si,sj):
    init=z; f=TAB[phase(z)]
    for ax,d in ((i,si),(j,sj),(i,-si),(j,-sj)):
        nxt=list(z);nxt[ax]+=d;nxt=tuple(nxt)
        f=move(f,TAB[phase(z)],TAB[phase(nxt)]);z=nxt
    assert z==init
    s=TAB[phase(z)]
    return tuple(s.index(x) for x in f)
def prod(q,p):return tuple(q[x] for x in p)
def eye():return [[F(i==j) for j in range(6)] for i in range(6)]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(6)] for i in range(6)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(6))
                         for j in range(6)] for i in range(6)]
def scale(A,n):return [[n*x for x in row] for row in A]
def matrix_poly(P,a):
    out=scale(eye(),0);t=eye()
    for c in a:
        out=add(out,scale(t,F(c)));t=mul(t,P)
    return out
def charpoly(P):
    B=eye(); c=[]
    for k in range(1,7):
        AB=mul(P,B); ck=-sum(AB[i][i] for i in range(6))/k
        c.append(ck);B=add(AB,scale(eye(),ck))
    assert not any(x for row in B for x in row)
    return c[::-1]+[F(1)]
def conv_poly(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r
def rank(rows):
    A=[[F(v) for v in row] for row in rows]
    h=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(h,len(A)) if A[i][c]),None)
        if pivot is None:continue
        A[h],A[pivot]=A[pivot],A[h];z=A[h][c]
        A[h]=[v/z for v in A[h]]
        for i in range(len(A)):
            if i!=h and A[i][c]:
                z=A[i][c];A[i]=[x-z*y for x,y in zip(A[i],A[h])]
        h+=1
        if h==len(A):break
    return h
def closure(s):
    reached={I};stack=[I]
    while stack:
        p=stack.pop()
        for q in s:
            t=prod(q,p)
            if t not in reached:reached.add(t);stack.append(t)
    return reached
def conv(dist,mu):
    r=Counter()
    for p,w in dist.items():
        for q,m in mu.items():r[prod(q,p)]+=w*m
    return r
def name(g):return ''.join(map(str,g))

def verify():
    evidence={'schema':'R690_ESTAR_BRC_MACRO_COSET_SPECTRUM_V1',
       'date':'2026-11-10','R462_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
       'parent':'R689@b63c3d60ada517586a649a7e92cd268ed55fdbc7',
       'candidate':'R687_ESTAR@028d5612f9562bc22ac7593f03426fc32b1a9259',
       'frozen_science':'RS-X6-TRIADIC-CLOSURE-DYNAMICS@a72226e2430ffa4786321ac86e7f0c599d5f0389',
       'arithmetic':'exact integer source-path enumeration and positive rational BRC group mass',
       'scope':'60 equally weighted returning native four-step squares, repeated from same Cell',
       'observer':'complete V17 S3 frame with source paths retained separately',
       'native_square_cases':360,'phases':{}}
    factors={
       0:[[-1,1],[F(-2,5),1],[F(-1,50),F(-1,2),1],[F(-1,50),F(-1,2),1]],
       1:[[-1,1],[-1,1],[F(31,100),F(-11,10),1],[F(31,100),F(-11,10),1]],
       2:[[-1,1],[-1,1],[-1,1],[F(-2,5),1],[F(-2,5),1],[F(-2,5),1]]}
    for a in range(3):
        for b in range(2):
            z=(a,b,0,0,0,0)
            counts=Counter(square(z,i,j,si,sj) for i in range(6)
                for j in range(i+1,6) for si,sj in product((-1,1),repeat=2))
            assert counts==EXPECT[a],(a,b,counts)
        mu=EXPECT[a];H=closure(mu)
        assert len(H)==[6,3,2][a]
        P=[[F(0) for j in G] for i in G]
        for j,p in enumerate(G):
            for q,w in mu.items():P[G.index(prod(q,p))][j]+=F(w,60)
        assert [sum(P[i][j] for i in range(6)) for j in range(6)]==[1]*6
        expect_char=[F(1)]
        for fac in factors[a]:expect_char=conv_poly(expect_char,fac)
        assert charpoly(P)==expect_char
        pmin=[F(n,MIN[a][-1]) for n in MIN[a]]
        assert matrix_poly(P,pmin)==scale(eye(),0)
        powers=[];power=eye()
        for _ in range(len(MIN[a])-1):
            powers.append([v for row in power for v in row])
            power=mul(power,P)
        assert rank(powers)==len(powers)
        state=Counter({I:1});dist={}
        for k in range(1,9):
            state=conv(state,mu)
            assert sum(state.values())==60**k and set(state)<=H
            if a==2:
                assert F(state[I],60**k)==(1+F(2,5)**k)/2
                assert F(state[T],60**k)==(1-F(2,5)**k)/2
            if k in (1,2,8):dist[str(k)]={name(g):state[g] for g in G if state[g]}
        if a==0:assert dist['2']=={'012':1044,'021':864,'102':324,
                                   '120':432,'201':612,'210':324}
        evidence['phases'][str(a)]={'all_b_identical':True,'macro_counts':
           {name(g):mu[g] for g in G if mu[g]},'reachable_subgroup':
           [name(g) for g in G if g in H],
           'characteristic_polynomial_ascending':[str(x) for x in expect_char],
           'minimal_polynomial_integer_ascending':MIN[a],
           'sample_distributions_integer_counts':dist}
    evidence['verification_marker']='R690_ESTAR_MACRO_COSET_SPECTRUM_EXACT_PASS'
    Path(__file__).with_name('R690_EVIDENCE.json').write_text(
         json.dumps(evidence,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
    print(evidence['verification_marker'])
if __name__=='__main__':verify()
