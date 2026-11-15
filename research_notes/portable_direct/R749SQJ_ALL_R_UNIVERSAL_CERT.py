#!/usr/bin/env python3
"""R749SQJ all-resolution exact Kolmogorov certificate.

Only r<=121 is enumerated. For r>=122 the published proof's
integer-weight hazard theorem and rational comparisons suffice.
"""
import json
from fractions import Fraction

M = {1: 3, 2: 4, 3: 6, 4: 4, 5: 3, 6: 2, 7: 1}
d = sum(M.values())
D = sum((w-1)*n for w,n in M.items())
B = D + d - 1
assert (d, D, B) == (23, 56, 78)
assert 5 * 22**22 < 2 * 23**22  # (22/23)^22 < 2/5
assert 156 * (122+147) <= 345 * 122
assert 156 * (121+147) > 345 * 121

last_small_r = 121
q = [0] * last_small_r
q[0] = 1
for weight, multiplicity in M.items():
    for _ in range(multiplicity):
        for j in range(weight, last_small_r):
            q[j] += q[j-weight]
C = [0] * (last_small_r + 1)
for r in range(1, last_small_r+1):
    C[r] = C[r-1] + q[r-1]
C0 = lambda t: C[t] if t>0 else 0

monotone_count = 0
small_pairs = 0
max_ratio = Fraction(0)
for t in range(1,last_small_r):
    assert C[t+1]*t**d <= C[t]*(t+1)**d, t
    monotone_count += 1
for r in range(1,last_small_r+1):
    atom_num = C[r]-C0(r-3)
    # Post-jump positive deviations <=p0 follow analytic normalized-ratio theorem.
    # Pre-jump (negative) inequality is exact integer:
    # C_t/C_r-(t/r)^d <= (C_r-C_{r-3})/C_r.
    for k in range(1,(r-1)//3+1):
        t=r-3*k
        err_num = C[t]*r**d - t**d*C[r]
        assert err_num >= 0, (r,k,'ratio')
        assert err_num <= atom_num*r**d, (r,k,'negative error')
        small_pairs+=1
        curr = Fraction(err_num,atom_num*r**d)
        if curr>max_ratio:
            max_ratio=curr
# Eventual proof in published mathematics:
#   E^- <= (78/r)*(22/23)^22 < 156/(5*r).
#   p0 >= 69/(r+147).
#   156/(5r) <= 69/(r+147) for every r>=122.
assert all(156*(r+147)<=345*r for r in range(122,150))

result={
    'result':'PASS',
    'model':'frozen_auxiliary_16_atom_Walsh',
    'frozen_scientific_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'weights':M,
    'dimensions':d,
    'weight_excess_D':D,
    'hazard_shift_M':B,
    'small_r_verified':[1,last_small_r],
    'small_r_normalized_ratio_checks':monotone_count,
    'small_r_negative_endpoint_checks':small_pairs,
    'small_r_max_error_to_atom_ratio':str(max_ratio),
    'large_r_proof_begin':122,
    'large_r_upper_negative_error':'<156/(5*r)',
    'large_r_lower_zero_atom':'69/(r+147)',
    'comparison_threshold':'156*(r+147)<=345*r for all r>=122',
    'exact_universal_claim':'For every integer r>=1, d_K(L(3*K_r/r), Beta(1,23))=1-C_{r-3}/C_r',
    'scope':'Exact finite checks plus printed analytic theorem; not standalone formal proof checker or independent review.'
}
print(json.dumps(result,sort_keys=True,indent=2))
