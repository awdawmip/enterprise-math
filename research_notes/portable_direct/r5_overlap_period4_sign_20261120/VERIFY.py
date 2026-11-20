"""Exact R5 overlap/period-4 sign verifier, Python standard library only."""
from collections import defaultdict
from itertools import product
from math import comb

S0={214,215,216,217,218}
S1={214,216,217,218,219,220,221}
S2={215,216,217,218,219,220,221}
SETS=(S0,S1,S2)
P=(844733,351287,8090,-34448,-1022181,-373965,-185538)

def g(n):
    if n < 0 or n%2: return 0
    t=n//2
    return sum(comb(t-2*j+3,3) for j in range(t//2+1))

def h_rational(m):
    return 2*g(m-1)+g(m-2)+6*g(m-3)+2*g(m-4)+4*g(m-5)

def k_numerator(m):
    """Exactly 547*K_m/C_1 (an integer)."""
    return 8*sum(v*g(m-1-j) for j,v in enumerate(P))

def k_quasipolynomial(m):
    assert m>=1
    t,r=divmod(m-1,4)
    if r==0:
        v=-8*(t+1)*(2*t+1)*(177448*t*t-1794370*t-2534199)
    elif r==1:
        v=-8*(t+1)*(57126*t**3-1279126*t*t-2752739*t-1053861)
    elif r==2:
        v=-16*(t+1)*(2*t+3)*(88724*t*t-808461*t-1693511)
    else:
        v=-16*(t+1)*(t+2)*(28563*t*t-639563*t-1028025)
    assert v%3==0
    return v//3

def overlap_dp(m):
    state={(0,0,0):1}
    for p in range(214,222):
        membership=tuple(int(p in s) for s in SETS)
        after=defaultdict(int)
        for v,w in state.items():
            for n in range(m):
                key=tuple(min(m,v[i]+n*membership[i]) for i in range(3))
                after[key]+=w*(-1 if p%2 and n%2 else 1)
        state=after
    return sum(w*max(sum(x<m for x in v)-1,0) for v,w in state.items())

def overlap_direct(m):
    total=0
    for n in product(range(m),repeat=8):
        a=[sum(n[p-214] for p in s)<m for s in SETS]
        sign=(-1 if sum(n[p-214] for p in (215,217,219,221))%2 else 1)
        total+=sign*max(sum(a)-1,0)
    return total

def moment(m,s):
    coeff=[1]+[0]*(m-1)
    deriv=[0]*m
    for p in sorted(s):
        nxt=[0]*m; nxtd=[0]*m
        for j in range(m):
            sign=(-1 if p%2 and j%2 else 1)
            for k in range(m-j):
                nxt[k+j]+=coeff[k]*sign
                nxtd[k+j]+=(deriv[k]-p*j*coeff[k])*sign
        coeff,deriv=nxt,nxtd
    return sum(coeff),sum(deriv)

def original_k_numerator(m,h):
    a,d0=moment(m,S0)
    c,_=moment(m,S1)
    b,d2=moment(m,S2)
    return 107*(12792*a+d0)+440*(12569*b+d2)+47080*c-94160*h

for m in range(1,20):
    h=h_rational(m)
    assert h==overlap_dp(m),(m,h)
    assert k_numerator(m)==original_k_numerator(m,h),m
for m in range(1,5):
    assert overlap_direct(m)==h_rational(m),m
for m in range(1,1001):
    assert k_numerator(m)==k_quasipolynomial(m),m
assert [h_rational(m) for m in (1,2,3,5,8,17)]==[2,1,14,50,46,2310]
assert [k_numerator(m) for m in (1,2,3,5,8,17)]==[
    6757864,2810296,27096176,66417936,52448800,824701320]
assert all(k_numerator(m)>0 for m in range(1,47))
thresholds={1:49,2:102,3:47,0:100}
for residue,first in thresholds.items():
    assert first%4==residue
    assert all(k_numerator(m)>0 for m in range(1,first) if m%4==residue)
    assert all(k_numerator(m)<0 for m in range(first,1001,4))
assert all(k_numerator(m)<0 for m in range(100,1001))
for m in [1,2,3,5,8,17,46,47,48,49,98,99,100,101,102,103]:
    print(m, h_rational(m), k_numerator(m))
print("PASS: m-independent generating identities and exact integer checks")
