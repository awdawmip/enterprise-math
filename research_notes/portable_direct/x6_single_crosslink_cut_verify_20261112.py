#!/usr/bin/env python3
"""Exact two-chain one-causal-link order-ideal and interleaving checker.
Conditional typed poset. No native X6 Cell/Link permission is claimed.
"""
from math import comb
import json

def coeffs(a,b,r,s):
    p=[0]*(a+b+1)
    for i in range(a+1):
        for j in range(b+1):
            if j<s or i>=r:
                p[i+j]+=1
    return p

def poly_product_minus_forbidden(a,b,r,s):
    p=[0]*(a+b+1)
    for i in range(a+1):
        for j in range(b+1):p[i+j]+=1
    for i in range(r):
        for j in range(s,b+1):p[i+j]-=1
    return p

def interleavings(a,b):
    def rec(i,j,w):
        if i==a and j==b:
            yield w
        if i<a:yield from rec(i+1,j,w+'A')
        if j<b:yield from rec(i,j+1,w+'B')
    yield from rec(0,0,'')

def formula_words(a,b,r,s):
    # By the first r+s-1 positions, at least r A labels appear.
    t=r+s-1
    return sum(comb(t,j)*comb(a+b-t,a-j) for j in range(max(0,r),min(a,t)+1)
               if 0<=a-j<=a+b-t)

def verify(a,b,r,s):
    p=coeffs(a,b,r,s)
    assert p==poly_product_minus_forbidden(a,b,r,s)
    assert sum(p)==(a+1)*(b+1)-r*(b-s+1)
    words=[]
    for w in interleavings(a,b):
        ar=[i for i,x in enumerate(w) if x=='A'][r-1]
        bs=[i for i,x in enumerate(w) if x=='B'][s-1]
        if ar<bs:words.append(w)
    assert len(words)==formula_words(a,b,r,s)
    return p,len(words)

count=0
for a in range(1,5):
    for b in range(1,5):
        for r in range(1,a+1):
            for s in range(1,b+1):
                verify(a,b,r,s);count+=1
assert count==100
cases=[]
for a,b,r,s in [(3,3,2,2),(2,2,2,1),(3,3,1,3),(4,4,3,2)]:
    p,words=verify(a,b,r,s)
    cases.append({'a':a,'b':b,'r':r,'s':s,'cut_state_counts':p,'total_ideals':sum(p),'linear_extensions':words,'peak_labels':max(p)})
print(json.dumps({'status':'PASS','finite_cases':count,'all_cases_exact':True,'sample_cases':cases,'native_X6_coupled_event_permission_proven':False},indent=2))
