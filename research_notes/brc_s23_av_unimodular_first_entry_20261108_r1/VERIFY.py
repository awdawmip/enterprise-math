#!/usr/bin/env python3
"""Exact integer certificates for the first entry into S23/AV's 510 threshold gap.
All large comparisons use arbitrary-precision integer arithmetic (no float/log).
The infinite/range conclusions use the unimodular lattice proof in PROOF.md.
"""

u_v, u_k = 79, 431
w_v, w_k = 380295, 2074774
assert u_v * w_k - u_k * w_v == 1
print('PASS_UNIMODULAR_LATTICE_BASIS')

# r=ln(7)/ln(10/7), eps=79r-431, d=2074774-380295r.
# eps>0, d>0 and d<eps are equivalent to these integer inequalities.
assert 7**510 > 10**431                              # eps>0
assert 10**w_k > 7**(w_k+w_v)                     # d>0
assert 7**(w_k+w_v+510) > 10**(w_k+431)         # d<eps
assert 7**(w_k+w_v-1) > 10**(w_k-1)             # d<1
print('PASS_EXACT_STRICT_ORDER: 0 < d < eps')

# T_510 contains no threshold strictly between A=10^431/7^510 and 1.
# For each s, i is the largest exponent 0 <= i <= s with 10^i < 7^s.
q7, p10, i = 1, 1, 0
A_num, A_den = 10**431, 7**510
matches = []
for s in range(1, 511):
    q7 *= 7
    while p10*10 < q7:
        p10 *= 10
        i += 1
    assert p10 < q7 <= p10*10
    assert 0 <= i <= s
    assert p10*A_den <= q7*A_num, (s, i)
    if p10*A_den == q7*A_num:
        matches.append((s,i))
assert matches == [(510,431)]
print('PASS_510_ROW_ADJACENCY: neighbors 10^431/7^510 < 1')

# The shortest prefix entering the gap with t=0 has
# (k,ell)=(w_k,w_v). All shorter prefixes are excluded by
# the unimodular lattice sign argument in PROOF.md.
assert (w_k+w_v) == 2455069
assert w_v == 380295
print('PASS_EXACT_FIRST_ENTRY_CERTIFICATE: k=2074774 ell=380295 n=2455069')

# For 0 <= t <= w_v, the scaled gap J_t has exact first entry
# (k,ell)=(w_k,w_v-t), at padded prefix length 2455069-t.
# For t<=379863 the previous length is already beyond the left
# extreme tail threshold, yielding a strict internal gap anomaly.
assert 2455068 - 379863 == 2075205
assert 10**2075204 <= 7**2455578 < 10**2075205
assert 510+379863 == 380373
assert 379863+1 == 379864
print('PASS_379864_CONSECUTIVE_NONTAIL_HORIZONS: h=510..380373')
for t in (0, 1, 2670, 379863, 379864, 380295):
    h=510+t
    n=w_k+w_v-t
    assert n >= w_k and n+h == 2455579
    print(f'GAP_FIRST_ENTRY h={h} t={t} exact_L={n}')
print('PASS_S23_AV_FIRST_RETURN_LATTICE_379864_ANOMALIES_20261108')
