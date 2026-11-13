#!/usr/bin/env python3
"""Independent exact Fraction check of the 55 emitted gap-class witnesses.
The full 162,027,001 threshold ordering is verified by VERIFY_GAP_CLASS.cpp.
"""
from fractions import Fraction as F
from pathlib import Path
import re
Q=10**26
lo=545569623581288298975349314
hi=lo+1
H=18000
N=2455069
def log_atanh(z, terms=45):
    s=F(0)
    term=z
    for j in range(terms):
        s+=2*term/(2*j+1)
        term*=z*z
    return s, s+2*term/((2*j+3)*(1-z*z))
l2,u2=log_atanh(F(1,3));l9,u9=log_atanh(F(1,9));l15,u15=log_atanh(F(1,15))
a,b=3*l2-u15,3*u2-l15
c,d=l9+l15,u9+u15
assert F(lo,Q)<a/d and b/c<F(hi,Q)
assert F(5455696235812,10**12) <= F(lo,Q) < F(hi,Q) < F(5455696235813,10**12)
lines=Path(__file__).with_name('RUN_H18000.txt').read_text().splitlines()
assert lines[0] == 'PASS_THRESHOLD_ORDER H=18000 M=162027001 BOUNDED=162027000 CLASSES=55'
count=0; maxlen=0; classes=0; largest=None
for line in lines[1:]:
    if not line.startswith('CLASS '):continue
    m=re.fullmatch(r'CLASS (-?\d+) (-?\d+) COUNT=(\d+) MAXV=(\d+) MAXJ=(\d+) MINSUM=(\d+) WITNESS=(\d+),(\d+) MAXLENGTH=(\d+)',line)
    assert m,line
    dv,dj,c,v,j,s,K,L,n=map(int,m.groups())
    assert L>=v and K>=j and K+L-s==n and n<=N
    assert K*Q>hi*L and (K+dj)*Q<lo*(L+dv)
    classes+=1;count+=c;maxlen=max(maxlen,n)
    if c>100_000_000:largest=(dv,dj,c,K,L,n)
assert classes==55 and count==162027000 and maxlen==N
assert largest==(79,431,152976286,2074774,380295,2455069)
ell=H*Q//lo+1
k=hi*H//Q+1
assert lo*ell>Q*H and k*Q>hi*H and (ell,k)==(3300,98203)
print('PASS_INDEPENDENT_EXACT_FRACTION_LOG_BOUNDS',lo,hi,Q)
print('PASS_INDEPENDENT_55_CLASS_WITNESSES',count,maxlen,largest)
print('PASS_INDEPENDENT_OUTER_WITNESSES',ell,k)
