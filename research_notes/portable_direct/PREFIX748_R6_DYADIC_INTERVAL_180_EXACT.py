#!/usr/bin/env python3
"""PREFIX-748-R6: rigorous outward 2**96 dyadic Gamma enclosure (standard library).
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run in this directory: python PREFIX748_R6_DYADIC_INTERVAL_180_EXACT.py [row_j]
All comparisons are integer and Fraction, no floating-point certificate.
"""
import json,sys
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
N,WD,B=189,1<<18,1<<96
@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(WD-x)**(n-k)>WD**n
@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*WD//n
    assert inside(n,k,mid)
    if k==0:lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
            if inside(n,k,x):b=x
            else:a=x
        lo,hi=a,b
    a,b=mid,WD
    while b-a>1:
        x=(a+b)//2
        if inside(n,k,x):a=x
        else:b=x
    if 4*(a-hi)>WD:return True
    if 4*(b-lo)<WD:return False
    raise ArithmeticError("frozen width undecided")
rows=[{0:1}]
for n in range(1,N+1):
    c=defaultdict(int)
    for k,v in rows[-1].items():
        c[k]+=v;c[k+1]+=v
    rows.append({k:v for k,v in c.items() if wide(n,k)})
assert not rows[N] and sum(len(r) for r in rows[:N])==9529
for n,r in enumerate(rows[:N]):
    assert all(0<=v<=comb(n,k) for k,v in r.items())
    assert all(r.get(k,0)==r.get(n-k,0) for k in range(n+1))
    assert all(r.get(k+1,0)*comb(n,k)>=r.get(k,0)*comb(n,k+1)
               for k in range(n//2))
@lru_cache(maxsize=300)
def surv(q):
    a,d=q.numerator,q.denominator
    pa=[1];pb=[1]
    for _ in range(N):
        pa.append(pa[-1]*a);pb.append(pb[-1]*(d-a))
    lo=[];hi=[];dn=1
    for n,r in enumerate(rows[:N]):
        numerator=sum(v*pa[k]*pb[n-k] for k,v in r.items())
        u,rem=divmod(numerator*B,dn)
        lo.append(u);hi.append(u+(rem!=0))
        dn*=d
    return lo,hi
Klo=[];Khi=[]
for n in range(N):
    a=[];b=[]
    for m in range(N):
        u,r=divmod(comb(n+m,n)*B,1<<(n+m+1))
        a.append(u);b.append(u+(r!=0))
    Klo.append(a);Khi.append(b)
B3=B**3
@lru_cache(maxsize=1000)
def pair(p,z):
    (pl,ph),(zl,zh)=surv(p),surv(z)
    xlo=xhi=ylo=yhi=0
    for n in range(N):
        if ph[n]==0:continue
        for m in range(N):
            if zh[m]==0:continue
            low=pl[n]*zl[m]*Klo[n][m]
            high=ph[n]*zh[m]*Khi[n][m]
            xlo+=low;xhi+=high
            ylo+=(n+m+1)*low;yhi+=(n+m+1)*high
    al=sum(pl)+sum(zl);ah=sum(ph)+sum(zh)
    bl=sum((n+1)*(pl[n]+zl[n]) for n in range(N))
    bh=sum((n+1)*(ph[n]+zh[n]) for n in range(N))
    mu_lo=F(al*B*B-xhi,B3);mu_hi=F(ah*B*B-xlo,B3)
    m2_lo=F(2*bl*B*B-yhi,B3);m2_hi=F(2*bh*B*B-ylo,B3)
    assert 0<=mu_lo<=mu_hi and 0<=m2_lo<=m2_hi
    return mu_lo,mu_hi,m2_lo,m2_hi
new_e=pair(F(0),F(73,500))
new_Wlo=new_e[2]-new_e[1]**2
old_e=pair(F(0),F(3,20))
old_Whi=old_e[3]-old_e[0]**2
assert new_Wlo>0
def cell_gap_lower(i,j,s=8):
    best=None
    for di in range(s):
        for dj in range(s):
            a=F(s*i+di,384*s);b=F(s*j+dj,384*s)
            c=F(s*i+di+1,384*s);d=F(s*j+dj+1,384*s)
            L=pair(a,b)[0];H=pair(c,d)[3]
            g0=new_Wlo-H+L**2
            g=min(g0,g0-(new_e[1]-L)/2)
            if best is None or g<best:best=g
    return best
def old_unsplit_gap_upper(i,j):
    Lhi=pair(F(i,384),F(j,384))[1]
    Hlo=pair(F(i+1,384),F(j+1,384))[2]
    g0=old_Whi-Hlo+Lhi**2
    return min(g0,g0-(old_e[0]-Lhi)/2)
def microfloor(x):
    return (1000000*x.numerator)//x.denominator
def run(argv):
    with open("PREFIX748_R6_DYADIC_INTERVAL_180_RESULTS.json",encoding="utf-8") as fh:
        data=json.load(fh)
    selected=data["cells"]
    if argv:
        if len(argv)!=1:raise SystemExit("usage: checker.py [row_j]")
        selected=[r for r in selected if r[1]==int(argv[0])]
        if not selected:raise SystemExit("unknown row")
    for i,j,exp,old_exp in selected:
        got=microfloor(cell_gap_lower(i,j))
        assert got==exp,(i,j,got,exp)
        assert got>33333,(i,j,got)
        old=microfloor(old_unsplit_gap_upper(i,j))
        assert old==old_exp and old<0,(i,j,old,old_exp)
        print("PASS",i,j,got,old,flush=True)
    if not argv:
        assert len(selected)==90
        assert len({(i,j) for i,j,*_ in selected}|{(j,i) for i,j,*_ in selected})==180
        assert min(r[2] for r in selected)==40470
        assert max(r[3] for r in selected)==-191027926
        assert 141942+2*(102+90)==142326
    print("ALL_CHECKS_PASS PREFIX748-R6",len(selected),flush=True)
if __name__=="__main__":run(sys.argv[1:])
