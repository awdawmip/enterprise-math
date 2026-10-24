#!/usr/bin/env python3
"""Exact symbolic and integer test for R272 positive BRC auxiliary resets."""
from collections import defaultdict
from math import isqrt
import json
import sympy as S

Z=S.symbols('z')
a=Z**3/(1-Z);b=Z**4/(1-Z)
p=Z**3/(1-Z)**2;q=Z**4*(2-Z)/(1-Z)**2
c=Z**3*(1+Z)/(1-Z)**3;d=Z**4*(4-3*Z+Z**2)/(1-Z)**3
R0=S.Matrix([[a,b],[b,a]])
R1=S.Matrix([[-p,q],[-q,p]])
R2=S.Matrix([[c,d],[d,c]])
G=(S.eye(2)-R0).inv()
left=S.Matrix([[1,0]]);right=S.Matrix([[1],[1]])
actual=[(left*G*right)[0],(left*G*R1*G*right)[0],(left*(G*R2*G+2*G*R1*G*R1*G)*right)[0]]
forms=[(1-Z)/((1-Z-Z**2)*(1+Z**2)),
-Z**3/((1+Z**2)*(1-Z-Z**2)*(1+Z+Z**2)),
Z**3*(1+6*Z+2*Z**2-Z**3)/((1-Z**3)*(1+Z**2)*(1-Z-Z**2)**2)]
assert all(S.cancel(x-y)==0 for x,y in zip(actual,forms))
r=(S.sqrt(5)-1)/2
f=lambda x,j:S.limit((1-Z/r)**j*x,Z,r)
assert S.simplify(f(forms[1],1)/f(forms[0],1)-(1-S.sqrt(5))/4)==0
assert S.simplify(f(forms[2],2)/f(forms[0],1)-(S.Rational(3,2)+7*S.sqrt(5)/10))==0

def coefficients(form,N):
    up,down=S.fraction(S.cancel(form))
    up=dict((int(i[0]),int(v)) for i,v in S.Poly(up,Z).terms())
    down=dict((int(i[0]),int(v)) for i,v in S.Poly(down,Z).terms())
    assert down[0]!=0
    out=[]
    for k in range(N+1):
        t=up.get(k,0)-sum(v*out[k-j] for j,v in down.items() if 1<=j<=k)
        assert t%down[0]==0
        out.append(t//down[0])
    return out

cs=[coefficients(form,150) for form in forms]
T={0:((2,-1,-1),(2,1,-1)),1:((0,-1,-1),(0,1,-1)),2:((1,1,1),(2,1,-1))}
channels=((0,0),(0,1),(1,0),(1,1),(2,0),(2,1))
def step(state,letter):
    q,r,e,k=state
    nq,eta,b=T[q][letter]
    nr=2 if r==2 or (r==1 and letter==0) else (1 if letter==0 else 0)
    return nq,nr,eta*e,eta*k+b

hist={(0,0,1,0):1}
bad=[]; bound_checks=0; words_checked=0; equal_checks=0; anchors={}
for n in range(151):
    assert sum(hist.values())==2**n
    if n<=12:
        raw=defaultdict(int)
        for w in range(1<<n):
            state=(0,0,1,0)
            for i in range(n-1,-1,-1):state=step(state,(w>>i)&1)
            raw[state]+=1
        assert dict(raw)==dict(hist)
        words_checked+=1<<n
    reset={(e,k):v for (q,r,e,k),v in hist.items() if q==r==0}
    totals=(sum(reset.values()),sum(e*k*v for (e,k),v in reset.items()),sum(k*k*v for (e,k),v in reset.items()))
    assert totals==tuple(c[n] for c in cs)
    by=defaultdict(lambda:[0]*6)
    for (q,r,e,k),v in hist.items():by[(e,k)][channels.index((q,int(r==2)))]+=v
    B=max((min(vals) for vals in by.values()),default=0)
    L=max(reset.values(),default=0)
    if n>=7:
        if n>=12:
            assert B==L,('FINITE_OBSERVATION_ONLY',n,B,L)
            equal_checks+=1
        else:
            assert B<L
            bad.append([n,B,L])
    if n>=10:
        m=n-7;num=cs[0][m];second=cs[2][m]
        R=isqrt(2*second//num)
        if R*R*num<2*second:R+=1
        lower=(num+4*(R+1)-1)//(4*(R+1))
        assert B>=lower,(n,B,lower)
        bound_checks+=1
    if n in (37,67):anchors[str(n)]=str(B)
    nxt=defaultdict(int)
    for st,v in hist.items():
        for x in (0,1):nxt[step(st,x)]+=v
    hist=nxt
assert anchors=={'37':'425625','67':'574891639795'}
print(json.dumps({'status':'PASS','symbolic_gf_identities':3,'symbolic_pole_limits':2,
'depth_max':150,'raw_words_checked':words_checked,
'moment_values_checked':453,'finite_lower_bounds_checked':bound_checks,
'finite_equalities_depth_12_to_150':equal_checks,
'finite_exceptions_depth_7_to_11':bad,
'B_37':anchors['37'],'B_67':anchors['67'],
'universal_claim_from_finite_tests':False},ensure_ascii=False,indent=2))
