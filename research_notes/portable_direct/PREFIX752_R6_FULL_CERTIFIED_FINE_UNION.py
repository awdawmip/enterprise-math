#!/usr/bin/env python3
"""PREFIX-752: certified-sign /768 Gamma-grid historical union.
Run at the published Enterprise Math source commit from research_notes/portable_direct.
Needs numpy and PREFIX751_R6_FULL_MACRO_FINE_SUPPORT_CHECK.py + its pinned JSON dependencies.
Sci pin f42f2906d77f24085c123f3ccfe9667d41caa96d; author check, unreviewed.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import json
from collections import defaultdict
from functools import lru_cache
from math import comb, ldexp
from pathlib import Path
import numpy as np
from PREFIX751_R6_FULL_MACRO_FINE_SUPPORT_CHECK import MACRO, FINE, OLD

N, WD, DEN = 189, 1 << 18, 768
U = 2.0**-53
assert np.finfo(float).eps == 2.0**-52

@lru_cache(None)
def inside(n, k, x):
    return 40*(n+1)*comb(n,k)*x**k*(WD-x)**(n-k) > WD**n
@lru_cache(None)
def wide(n,k):
    if k>n//2: return wide(n,n-k)
    mid=k*WD//n
    assert inside(n,k,mid)
    if k==0: lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
            if inside(n,k,x): b=x
            else: a=x
        lo,hi=a,b
    a,b=mid,WD
    while b-a>1:
        x=(a+b)//2
        if inside(n,k,x): a=x
        else: b=x
    if 4*(a-hi)>WD: return True
    if 4*(b-lo)<WD: return False
    raise ArithmeticError('width not decided')

def check_round(num, den, val, tolerance_units=1):
    p,q=float(val).as_integer_ratio()
    assert abs(num*q-p*den)*(1<<53) <= tolerance_units*den*q

rows=[{0:1}]
for n in range(1,N+1):
    cnt=defaultdict(int)
    for k,v in rows[-1].items(): cnt[k]+=v;cnt[k+1]+=v
    rows.append({k:v for k,v in cnt.items() if wide(n,k)})
assert not rows[N] and sum(map(len,rows[:N]))==9529

def tails(a,d):
    b=d-a; ap=[1];bp=[1]
    for _ in range(N): ap.append(ap[-1]*a);bp.append(bp[-1]*b)
    ans=[];den=1
    for n,row in enumerate(rows[:N]):
        if n: den*=d
        num=sum(v*ap[k]*bp[n-k] for k,v in row.items())
        f=num/den
        check_round(num,den,f)
        ans.append(f)
    return np.asarray(ans,dtype=np.float64)

T=np.stack([tails(i,DEN) for i in range(385)])
Tstar=tails(3,20)
C=np.empty((N,N),dtype=np.float64)
D=np.empty((N,N),dtype=np.float64)
for n in range(N):
    for m in range(N):
        c=comb(n+m,n);den=1<<(n+m+1)
        C[n,m]=ldexp(float(c),-(n+m+1))
        D[n,m]=(n+m+1)*C[n,m]
        check_round(c,den,C[n,m])
        check_round((n+m+1)*c,den,D[n,m],500)

A=T.sum(axis=1)
B=T@np.arange(1,N+1,dtype=np.float64)
MU=A[:,None]+A[None,:]-(T@C@T.T)
M2=2*(B[:,None]+B[None,:])-(T@D@T.T)
ones=np.arange(1,N+1,dtype=np.float64)
mue=T[0].sum()+Tstar.sum()-T[0]@C@Tstar
m2e=2*(T[0]@ones+Tstar@ones)-T[0]@D@Tstar
We=m2e-mue*mue
G=We-M2[1:,1:]+MU[:-1,:-1]**2-np.maximum(0,(mue-MU[:-1,:-1])/2)

# Certified forward error (proof in PREFIX752 note): < 1/100 for EVERY G entry.
# Each exact input rounding is checked by cross-multiplied integer inequalities above.
# Positive sums, IEEE binary64, <=189 terms per matrix dot, gamma_1000 bound.
assert G.shape==(384,384)
assert np.all(np.isfinite(G))
margin=float(np.min(np.abs(G)))
assert margin>0.01, ('unresolved signs; exact fallback needed',margin)
mask=G>0
assert int(mask.sum())==137168
assert len(MACRO)==3782 and len(FINE)==15128
old_overlap=sum(bool(mask[u,v]) for u,v in FINE)
assert old_overlap==13142,old_overlap
extra=set().union(*OLD.values())
assert len(extra)==1850 and all(not mask[u,v] for u,v in extra)
extra_overlap=len(extra&FINE)
assert extra_overlap==342
union=139018+len(FINE)-old_overlap-extra_overlap
assert union==140662
record={
    'schema':'PREFIX752_R6_FULL_FINE_UNION_CERTIFIED_SIGN_V1',
    'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'original_fine_grid':[384,384], 'full_old_712_positive':int(mask.sum()),
    'full_old_712_min_abs_binary64_gap':margin,
    'sign_error_upper_bound': '1/100',
    'later_macro':len(MACRO),'later_fine':len(FINE),
    'later_intersect_original_712':old_overlap,
    'later_intersect_extra_713_718':extra_overlap,
    'earlier_extra_disjoint_original_712':True,
    'complete_author_union_fine':union,
    'total_original_fine':147456,
    'remaining_fine':147456-union,
    'accepted_level':'AUTHOR_CERTIFIED_SIGN_EXACT_FINITE_COUNT / UNREVIEWED / NOT_ADMITTED',
    'runtime':'CPython binary64 + NumPy; BLAS single threaded',
}
out=Path(__file__).with_name('PREFIX752_R6_FULL_CERTIFIED_FINE_UNION_RESULTS.json')
out.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX752-R6',json.dumps(record,ensure_ascii=False))
