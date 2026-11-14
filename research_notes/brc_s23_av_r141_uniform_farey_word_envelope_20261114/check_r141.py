#!/usr/bin/env python3
"""R141 all-m Farey-support lemma: exact finite regression, not proof of universality.
Derived from R140's published Farey intercept-gap enumerator, with new
low-denominator support and per-word representative-horizon checks.
All operations are unbounded integers or fractions; no floating point.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
from math import gcd

def farey_adjacent(m):
    a,b,c,d=0,1,1,m
    while True:
        assert b*c-a*d==1
        yield a,b,c,d
        k=(m+b)//d
        a,b,c,d=c,d,k*c-a,k*d-b
        if a>=b: break

def word_gaps(m):
    words=defaultdict(list)
    ng=0
    for a,b,c,d in farey_adjacent(m):
        A=a*d+b*c
        Q=2*b*d
        cuts=[(0,0,0),(Q,1,0)]
        for j in range(1,m+1):
            p=j*A//Q+1
            cuts.append((p*Q-j*A,p,j))
        cuts.sort()
        assert all(x[0]<y[0] for x,y in zip(cuts,cuts[1:]))
        for (low,p,j),(high,q,k) in zip(cuts,cuts[1:]):
            x=low+high
            prev=x//(2*Q)
            w=0
            for i in range(1,m+1):
                cur=(x+2*i*A)//(2*Q)
                w=(w<<1)|(cur-prev)
                prev=cur
            D=j*b*c-k*a*d+(q-p)*b*d
            assert D>=min(b,d)
            B=b*d-D
            words[w].append((b,d,B))
            ng+=1
    return words,ng

def expected_F(m):
    phi=list(range(m+1))
    for q in range(2,m+1):
        if phi[q]==q:
            for j in range(q,m+1,q):
                phi[j]-=phi[j]//q
    return 1+sum((m+1-q)*phi[q] for q in range(1,m+1))

def support_bounds(w,m):
    s=[0]
    for i in range(m):
        s.append(s[-1]+((w>>(m-1-i))&1))
    lo,hi=Fraction(0),Fraction(1)
    for i in range(m+1):
        for j in range(i+1,m+1):
            length=j-i
            lo=max(lo,Fraction(s[j]-s[i]-1,length))
            hi=min(hi,Fraction(s[j]-s[i]+1,length))
    return lo,hi

def verify(max_m=64):
    assert max_m>=5
    totals={"lengths":0,"word_records":0,"farey_gap_records":0,
            "exception_word_records":0,"support_interval_checks":0}
    samples=[]
    for m in range(5,max_m+1):
        byword,gaps=word_gaps(m)
        assert len(byword)==expected_F(m)
        ext=(1<<(m-1))|1
        complement=ext^((1<<m)-1)
        exceptions={w for w,gs in byword.items()
                    if all(min(b,d)>m-3 for b,d,B in gs)}
        assert exceptions=={ext,complement},(m,exceptions)
        horizons={w:min(max(2,B+2) for b,d,B in gs)
                  for w,gs in byword.items()}
        Urep=max(horizons.values())
        bound=(m-2)**2+1
        assert Urep==bound,(m,Urep,bound)
        assert horizons[ext]==horizons[complement]==bound
        assert all(h<=bound for h in horizons.values())
        if m<=12:
            small_farey={Fraction(p,q)
                         for q in range(1,m-2)
                         for p in range(q+1) if gcd(p,q)==1}
            for w,gs in byword.items():
                lo,hi=support_bounds(w,m)
                assert lo<hi
                meets=any(lo<=x<=hi for x in small_farey)
                assert meets==(w not in exceptions),(m,w,lo,hi)
                totals["support_interval_checks"]+=1
        totals["lengths"]+=1
        totals["word_records"]+=len(byword)
        totals["farey_gap_records"]+=gaps
        totals["exception_word_records"]+=len(exceptions)
        if m in (5,6,7,10,20,40,64):
            samples.append((m,len(byword),len(exceptions),Urep))
    print("R141_FAREY_SUPPORT_PASS")
    print("totals:",totals)
    print("sample rows (m,F,exception_words,U_rep):",samples)
    return totals

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--max-m",type=int,default=64)
    verify(parser.parse_args().max_m)
