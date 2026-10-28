#!/usr/bin/env python3
"""Exact Fraction regressions; universal theorem is proved in PROOF.md."""
from fractions import Fraction
from itertools import product
import json

def f(n):
    return Fraction(n*n)+Fraction(n,3)

def f_per2(n):
    return f(n)+Fraction(n%2,5)

def d2(fun,r,s,t):
    return fun(t+r+s)-fun(t+r)-fun(t+s)+fun(t)

for fun in (f,f_per2):
    assert fun(0)==0
    assert all(fun(n)>0 for n in range(-50,51) if n)

rectangles=0
for fun,rs,ss in (
    (f,(-4,-3,-2,-1,1,2,3,4),(-4,-3,-2,-1,1,2,3,4)),
    (f_per2,(-4,-2,2,4),(-3,-1,1,3)),
):
    for r,s in product(rs,ss):
        K=d2(fun,r,s,0)
        assert all(d2(fun,r,s,t)==K for t in range(-40,41))
        for n in range(-5,6):
            assert fun(r*s*n)+fun(-r*s*n)==r*s*n*n*K
        assert r*s*K>0
        rectangles+=1

gl2=[]
full=[]
for a,b,c,d in product(range(-3,4),repeat=4):
    if abs(a*d-b*c)!=1: continue
    gl2.append((a,b,c,d))
    if a*b*c*d:
        full.append((a,b,c,d))
        assert a*b*c*d>0
        assert abs(a*d-b*c)==1

preservers={}
for label,fun in (('noneven',f),('even',lambda n: Fraction(n*n))):
    found=[]
    for a,b,c,d in gl2:
        if all(fun(a*x+b*y)+fun(c*x+d*y)==fun(x)+fun(y)
               for x,y in product(range(-4,5),repeat=2)):
            assert [bool(a),bool(c)].count(True)==1
            assert [bool(b),bool(d)].count(True)==1
            assert abs(a)+abs(c)==abs(b)+abs(d)==1
            found.append([a,b,c,d])
    preservers[label]=found
assert len(preservers['noneven'])==2
assert len(preservers['even'])==8

print(json.dumps({
 'status':'EXACT_FRACTION_FINITE_REGRESSION_PASS',
 'rectangle_cases':rectangles,
 'unimodular_matrices_tested':len(gl2),
 'all_entry_nonzero_unimodular_tested':len(full),
 'noneven_preservers':preservers['noneven'],
 'even_preservers':preservers['even'],
 'universal_proof':'PROOF.md; not established by finite search',
 'formal_driver_review':False,
 'historical_blobs_recovered':False
},indent=2))
