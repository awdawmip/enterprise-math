#!/usr/bin/env python3
"""R142 exact Farey support denominator filter for external S23.
All calculations use unbounded Python integers and Fraction.
Run: python check_r142.py 30
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd
import json
import sys

def farey_adjacent(m):
    a,b,c,d=0,1,1,m
    while True:
        assert b*c-a*d==1
        yield a,b,c,d
        k=(m+b)//d
        a,b,c,d=c,d,k*c-a,k*d-b
        if a>=b:
            break

def word_gaps(m):
    words=defaultdict(list)
    for a,b,c,d in farey_adjacent(m):
        A=a*d+b*c
        Q=2*b*d
        cuts=[(0,0,0),(Q,1,0)]
        for j in range(1,m+1):
            p=j*A//Q+1
            cuts.append((p*Q-j*A,p,j))
        cuts.sort()
        for (low,p,j),(high,q,k) in zip(cuts,cuts[1:]):
            x=low+high
            old=x//(2*Q)
            w=0
            for i in range(1,m+1):
                new=(x+2*i*A)//(2*Q)
                w=(w<<1)|(new-old)
                old=new
            D=j*b*c-k*a*d+(q-p)*b*d
            assert D>=min(b,d)
            words[w].append((a,b,c,d,p,j,q,k,D))
    return words

def support(w,m):
    s=[0]
    for i in range(m):
        s.append(s[-1]+((w>>(m-1-i))&1))
    lo,hi=Fraction(0),Fraction(1)
    for i in range(m):
        for j in range(i+1,m+1):
            width=j-i
            a=Fraction(s[j]-s[i]-1,width)
            b=Fraction(s[j]-s[i]+1,width)
            if a>lo:
                lo=a
            if b<hi:
                hi=b
    return lo,hi

def rational_support(lo,hi,n):
    for q in range(1,n+1):
        for p in range(q+1):
            if gcd(p,q)==1 and lo*q<=p<=hi*q:
                return p,q
    return None

def expected_F(m):
    phi=list(range(m+1))
    for q in range(2,m+1):
        if phi[q]==q:
            for j in range(q,m+1,q):
                phi[j]-=phi[j]//q
    return 1+sum((m+1-q)*phi[q] for q in range(1,m+1))

def threshold(m):
    return (m-2)*((m-1)//2)+1

def verify(max_m):
    rows=[]
    for m in range(5,max_m+1):
        words=word_gaps(m)
        assert len(words)==expected_F(m),(m,len(words),expected_F(m))
        E=threshold(m)
        n=(m-3)//2
        guaranteed=0
        avoid=0
        critical=0
        witness_checks=0
        for w,gs in words.items():
            lo,hi=support(w,m)
            assert lo<hi
            h=min(max(2,b*d-D+2) for a,b,c,d,p,j,q,k,D in gs)
            if h>E:
                critical+=1
            z=rational_support(lo,hi,n)
            if z:
                guaranteed+=1
                p,q=z
                assert h<=q*(m-1)+2<=E,(m,w,h,z,E)
                if m in (5,7,10,12,16,20):
                    for K in (E,E+10**40+17):
                        L=K-1
                        candidates=[g for g in gs if max(2,g[1]*g[3]-g[8]+2)<=E]
                        assert candidates,(m,w,K)
                        a,b,c,d,p,j,qq,k,D=candidates[0]
                        bottom=Fraction((L+k)*a,b)-qq
                        N=bottom.numerator//bottom.denominator+1
                        left=max(Fraction(a,b),Fraction(N+p,L+j))
                        right=min(Fraction(c,d),Fraction(N+qq,L+k))
                        assert left<right,(m,w,K,left,right)
                        theta=(left+right)/2
                        got=0
                        for i in range(m):
                            u=(L+i+1)*theta
                            v=(L+i)*theta
                            got=(got<<1)|((u.numerator//u.denominator)-(v.numerator//v.denominator))
                        assert got==w,(m,w,K,theta,got)
                        witness_checks+=1
            else:
                avoid+=1
        assert guaranteed+avoid==len(words)
        rows.append(dict(m=m,E=E,q_max=n,words=len(words),
                         guaranteed=guaranteed,avoidant=avoid,critical=critical,
                         witness_checks=witness_checks))
        if m in (5,6,7,8,10,12,16,20,24,30):
            print(rows[-1],flush=True)
    print("R142_SUPPORT_DENOMINATOR_FILTER_PASS")
    print("totals", {k:sum(row[k] for row in rows)
                     for k in ("words","guaranteed","avoidant","critical","witness_checks")})
    return rows

if __name__=="__main__":
    max_m=int(sys.argv[1]) if len(sys.argv)>1 else 30
    verify(max_m)
