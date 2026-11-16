#!/usr/bin/env python3
"""R432 exact parity proof certificate, Python 3 standard library."""
from math import comb
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path
def choose(n,k): return comb(n,k) if 0<=k<=n else 0
def cat(n): return choose(2*n,n)//(n+1)
def raw_h(r,s):
    if s<2 or s>r:return 0
    return choose(r+s,2*s)*sum(choose(r-s,j)*(choose(2*s,r-2*j)-choose(2*s,r-2*j-1)) for j in range(r-s+1))
def cat_h(r,s):
    if not 2<=s<=r:return 0
    if r%2:
        k=(r-1)//2
        z=sum(choose(s-1,2*t)*4**t*cat(k-t) for t in range((s-1)//2+1) if k-t>=0)
    else:
        k=r//2
        z=sum(choose(s-1,2*t+1)*2*4**t*cat(k-1-t) for t in range((s-2)//2+1) if k-1-t>=0)
    return choose(r+s,2*s)*z
def eb(k):
    return [F(1),F(2*(k-1)*(2*k+3),15),
      F((k-1)*(k+2)*(2*k+3)*(8*k-9),420),
      F((k-2)*(k-1)*(k+2)*(2*k+3)*(2*k+5)*(4*k-3),4725),
      F((k-2)*(k-1)*(k+2)*(k+3)*(2*k+3)*(2*k+5)*(64*k*k-184*k+75),1247400)]
def ob(k):
    return [F(1),F((k+2)*(4*k+1),15),
      F((k-1)*(k+2)*(2*k+5)*(8*k+5),420),
      F((k-1)*(k+2)*(k+3)*(2*k+5)*(32*k*k-16*k-33),18900),
      F((k-2)*(k-1)*(k+2)*(k+3)*(2*k+5)*(2*k+7)*(64*k*k-8*k-57),1247400)]
def nb(b):
    _,x,y,z,w=b
    return x**4-3*x*x*y+y*y+2*x*z-w
def E(k):
    return 3968*k**6+188352*k**5+265950*k**4+383275*k**3+298515*k*k+172752*k+10188
def P(k):
    return 7936*k**7-309248*k**6-3408516*k**5-14300148*k**4-33616293*k**3-46354824*k*k-35761465*k-11787442
def target(r):
    k=r//2
    return F(-(k-1)*(2*k+3)*E(k),436590000) if r%2==0 else F(-(k+2)*P(k),436590000)
def det4(M):
    z=0
    for p in permutations(range(4)):
        sign=-1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1
        v=1
        for i,j in enumerate(p):v*=M[i][j]
        z+=sign*v
    return z
def leftminor(r):
    n=r-2;a=[raw_h(r,r-h) for h in range(n+1)]
    cols=(n-1,n,n+1,n+2)
    return det4([[a[j-i] if 0<=j-i<=n else 0 for j in cols] for i in range(4)])
def run():
    # Each b_s is an exact polynomial of degree <=2(s-2), so normalized M has degree<=8.
    # Nine evaluations per parity are a complete polynomial identity certificate.
    assert all(nb(eb(k))==target(2*k) for k in range(3,12))
    assert all(nb(ob(k))==target(2*k+1) for k in range(2,11))
    assert P(48)==-71552034705250 and P(49)==52661023196976
    checks=norms=minors=0;special=[]
    for r in range(4,202):
        for s in range(2,min(r,9)+1):
            assert raw_h(r,s)==cat_h(r,s);checks+=1
        if r>=6:
            B=raw_h(r,2);k=r//2
            b=ob(k) if r%2 else eb(k)
            assert all(F(raw_h(r,s),B)==b[s-2] for s in range(2,7))
            norms+=5
            m=leftminor(r)
            assert F(m,B**4)==target(r)
            assert (m<0)==(r%2==0 or r>=99)
            minors+=1
            if r in (6,12,14,15,97,99,101):
                special.append({"r":r,"H2":str(B),"M":str(m),"normalized":str(target(r))})
    res={"status":"R432_EXACT_PASS","catalan_checks":checks,"normalized_checks":norms,
         "left_minor_checks":minors,"P48":str(P(48)),"P49":str(P(49)),
         "certificate":"nine exact distinct points per parity + degree<=8",
         "special":special,"admission":"AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED"}
    Path(__file__).with_name("R432_EXACT_EVIDENCE.json").write_text(json.dumps(res,indent=2,ensure_ascii=False)+"\n")
    print("R432_EXACT_PASS",checks,norms,minors,"P48",P(48),"P49",P(49))
if __name__=="__main__":run()
