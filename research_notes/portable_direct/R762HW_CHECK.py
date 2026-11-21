#!/usr/bin/env python3
"""R762HW: rooted parity surplus and spectral gap, exact integer checks.

Independent: positive source-count DP and twisted-class characteristic-polynomial
Newton traces. No floating point is used for mathematical assertions.
"""
from collections import defaultdict
from itertools import combinations
from fractions import Fraction

PORTS = list(combinations(range(6), 2))
EDGES = [[] for _ in PORTS]
for p, a in enumerate(PORTS):
    for q, b in enumerate(PORTS):
        if len(set(a) & set(b)) == 1:
            EDGES[p].append((q, sum(1 << i for i in set(a)|set(b))))
assert len(PORTS) == 15 and all(len(e) == 8 for e in EDGES)

def pmul(a,b):
    z = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j] += x*y
    return z

def ppow(a,n):
    x=[1]
    for _ in range(n): x=pmul(x,a)
    return x

# Ascending coefficients; spectra inherited from HV but the formula is newly used.
poly = {
    0: pmul(pmul([-8,1],ppow([-2,1],5)),ppow([2,1],9)),
    1: pmul(pmul(ppow([2,1],5),[-32,-2,1]),ppow([-2,-2,1],4)),
    2: pmul(pmul(pmul(ppow([0,1],3),ppow([2,1],2)),[4,1]),pmul(ppow([-4,-2,1],3),[32,-28,-2,1])),
    3: pmul(pmul(ppow([0,1],5),[-28,0,1]),pmul(ppow([-6,-2,1],2),ppow([-6,2,1],2)))
}
assert all(len(v)==16 and v[-1]==1 for v in poly.values())

def traces(coeffs,nmax):
    c=list(reversed(coeffs))
    out=[15]
    for n in range(1,nmax+1):
        if n<=15:
            x=-sum(c[j]*out[n-j] for j in range(1,n))-n*c[n]
        else:
            x=-sum(c[j]*out[n-j] for j in range(1,16))
        out.append(x)
    return out

N=80
T={k:traces(p,N) for k,p in poly.items()}
# Complete positive BRC branch-count DP over root, current Port, axis parity.
state={(0,0):1}
E=[1]
P=[1]
for m in range(1,N+1):
    ns=defaultdict(int)
    for (p,bits),mass in state.items():
        for q,delta in EDGES[p]: ns[q,bits^delta]+=mass
    state=ns
    E.append(state.get((0,0),0))
    P.append(sum(mass for (p,bits),mass in state.items() if p==0))
    assert sum(state.values())==8**m
    if m%2==0:
        assert P[m] == (8**m+14*2**m)//15
        # New exact orbit-spectrum class formula.
        numerator=2*T[0][m]+12*T[1][m]+30*T[2][m]+20*T[3][m]
        assert numerator%960==0 and E[m]==numerator//960,(m,E[m],numerator//960)
        assert E[m]>P[m]//32
    else:
        assert E[m]==0

# Verify strict descent of the exact parity-conditioned ratio for 2,4,..,80.
ratios=[Fraction(E[m],P[m]) for m in range(2,N+1,2)]
assert all(x>y for x,y in zip(ratios,ratios[1:]))
assert ratios[0]==1 and ratios[1]==Fraction(7,12)
# Confirm exact decomposition of the positive surplus and positivity of every twisted trace.
for m in range(2,N+1,2):
    assert all(T[k][m]>=0 for k in (1,2,3))
    assert Fraction(E[m],1)-Fraction(P[m],32) == Fraction(T[1][m],80)+Fraction(T[2][m],32)+Fraction(T[3][m],48)

print('PASS R762HW: full positive parity BRC DP 1..80; 4 spectral class Newton recurrences 1..80; exact orbit identity; 39 strict monotonic steps; surplus positive')
print('m,E_m,P_m,relative_even_fraction')
for m in (2,4,6,8,10,12,14,16,20,26,40,60,80):
    print(m,E[m],P[m],f'{float(Fraction(E[m],P[m])):.12g}',sep=',')
