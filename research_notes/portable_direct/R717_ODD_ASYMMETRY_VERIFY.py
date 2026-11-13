#!/usr/bin/env python3
"""R717: exact odd-ring BRC residual-asymmetry checks (integer arithmetic)."""
from collections import Counter
from fractions import Fraction
from math import comb
import json

PAIRS=[(p,q) for p in range(1,6) for q in range(p+1,6)]
ADJ=[[j for j,v in enumerate(PAIRS) if set(u).isdisjoint(v)] for u in PAIRS]
EXCESS=[q-p-1 for p,q in PAIRS]

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def lucas(n):
    if n==0:return 2
    if n==1:return 1
    a,b=2,1
    for _ in range(2,n+1):a,b=b,a+b
    return b

def predicted(k):
    return [comb(k+r+1,2*r+1) for r in range(k+1)]

def complete_rooted_hist(m):
    counts=Counter()
    total=0
    def rec(first,last,length,excess,D):
        nonlocal total
        if excess>3:return
        if length==m:
            if excess==3 and first in ADJ[last]:
                r=D[0]-D[2]
                assert r==D[3]-D[1] and 0<=r<=(m-5)//2
                counts[r]+=1
                total+=1
            return
        for nxt in ADJ[last]:
            p,q=PAIRS[nxt]
            rec(first,nxt,length+1,excess+EXCESS[nxt],
                tuple(D[z]+int(p<=z+1<q) for z in range(4)))
    for i,(p,q) in enumerate(PAIRS):
        rec(i,i,1,EXCESS[i],tuple(int(p<=z+1<q) for z in range(4)))
    return [counts[r] for r in range((m-5)//2+1)],total

def verify():
    enumerations=[]
    for m in [5,7,9,11,13,15,17]:
        k=(m-5)//2
        got,total=complete_rooted_hist(m)
        assert got==[8*m*a for a in predicted(k)]
        enumerations.append({"m":m,"rooted_words":total,"R_histogram":got})

    # H_k(u)=sum_r binom(k+r+1,2r+1)u^r; exact derivatives at u=1.
    a0,a1=1,3
    b0,b1=0,1
    c0,c1=0,0
    moments=[]
    for k in range(501):
        if k==0: a,b,c=a0,b0,c0
        elif k==1: a,b,c=a1,b1,c1
        else:
            a2=3*a1-a0
            b2=a1+3*b1-b0
            c2=2*b1+3*c1-c0
            a0,a1,b0,b1,c0,c1=a1,a2,b1,b2,c1,c2
            a,b,c=a2,b2,c2
        hist=predicted(k)
        assert sum(hist)==a==fib(2*k+2)
        assert sum(r*x for r,x in enumerate(hist))==b
        assert sum(r*(r-1)*x for r,x in enumerate(hist))==c
        F,L=fib(2*k+2),lucas(2*k+2)
        mean=Fraction(b,a)
        variance=Fraction(c+b,a)-mean*mean
        assert mean==Fraction((k+1)*L,5*F)-Fraction(3,5)
        assert variance==(Fraction(2*(k+1)*L,25*F)
                         -Fraction(4*(k+1)**2,25*F*F)-Fraction(2,25))
        assert hist[0]==k+1
        if k>0:assert hist[1]==comb(k+2,3)
        if k in (0,1,2,5,10,20,50,100,500):
            moments.append({"m":2*k+5,"k":k,"bracelets":4*F,
                            "R0_bracelets":4*hist[0],
                            "R1_bracelets":4*(hist[1] if k else 0),
                            "mean":{"num":mean.numerator,"den":mean.denominator},
                            "variance":{"num":variance.numerator,"den":variance.denominator}})
    return {"status":"R717_ODD_RING_ASYMMETRY_EXACT_PASS",
            "frozen_scientific_input":"enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
            "full_rooted_enumerations":enumerations,
            "integer_coefficient_moment_checks":501,
            "selected_exact_moments":moments,
            "typed_history_factor":"2^m independent positive-event source orderings"}

if __name__=="__main__":
    result=verify()
    with open("R717_ODD_ASYMMETRY_RESULTS.json","w",encoding="utf8") as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
    print(result["status"])
    print([(row["m"],row["rooted_words"]) for row in result["full_rooted_enumerations"]])
    print("CHECKED_PARAMETER_SETS",result["integer_coefficient_moment_checks"])
