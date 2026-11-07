#!/usr/bin/env python3
"""S23/AV exact near-resonance 7^510 versus 10^431.
Finite exact certificates (510 threshold rows, 20,026 integer return rows)
and the previously proved all-t scaling lemma yield 2,671 anomalies.
"""
from fractions import Fraction
A = Fraction(10**431, 7**510)
assert A < 1
for s in range(1, 511):
    i = 0
    while 10**(i+1) < 7**s:
        i += 1
    assert i <= s and 10**i < 7**s
    assert Fraction(10**i, 7**s) <= A
print('PASS_BASE_ADJACENCY_T510: 10^431/7^510 and 1 are neighboring thresholds')

# k=K(v) is least integer with R(v)=7^(k+v)/10^k<1.
# Maintain N=7^(k+v), D=10^k by exact multiplicative recurrences.
N = D = 1
k = 0
A7, A10 = 7**510, 10**431
for v in range(20026):
    if v:
        N *= 7
    while N >= D:
        N *= 7
        D *= 10
        k += 1
    assert N < D
    assert k == 0 or N*10 >= D*7  # predecessor at k-1 is >= 1
    assert N*A7 <= D*A10, (v, k)  # no entry to (10^431/7^510,1)
print('PASS_NO_RETURN_FOR_V_0_TO_20025: exact recurrence, final k=', k)

# For 0<=t<=20025, J_t=(10^431/7^(510+t),7^-t) is an adjacent
# interval by the proven scaling lemma. Any prefix n<=20025-t
# has ell<=n, hence v=ell+t<=20025, so J_t is unoccupied.
# Therefore N(510+t) >= 20026-t.
assert 7**20535 < 10**17355
assert 7**20535 >= 10**17354
# For t<=2670, n=20025-t >=17355, and n+h=20535.
# So 7^(n+h)<10^n, proving n_tail(h)<=20025-t < N(h).
assert 20025-2670 == 17355
print('PASS_2671_CONSECUTIVE_STRICT_ANOMALIES: h=510..3180, N(510+t)>=20026-t>n_tail')

def n_tail(h):
    lo, hi = 1, 6*h
    while lo < hi:
        mid=(lo+hi)//2
        if 7**(mid+h)<10**mid:
            hi=mid
        else:
            lo=mid+1
    assert 7**(lo+h)<10**lo
    assert lo==1 or 7**(lo-1+h)>=10**(lo-1)
    return lo

for t in (0, 25, 2670, 2671):
    h = 510+t
    print('BOUND h=',h,'N>=',20026-t,'n_tail=',n_tail(h),
          'proven_excess>=',20026-t-n_tail(h))
print('PASS_S23_AV_NEAR_RESONANCE_2671_STRICT_ANOMALIES_20261108')
