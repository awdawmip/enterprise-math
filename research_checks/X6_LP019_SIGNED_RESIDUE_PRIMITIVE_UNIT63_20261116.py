#!/usr/bin/env python3
"""Exact bounded check of the historic BRC pure-algebra signed collapse residual,
not an experiment on the frozen six-axis signed spatial producer."""
from math import gcd
import json

checks = 0
ranges = []
samples = []
for p, max_k in [(2, 20), (3, 12), (4, 9), (5, 6)]:
    count = 0
    for k in range(1, max_k + 1):
        low = k ** p
        high = (k + 1) ** p
        G = high - low
        for d in range(1, G):
            g = gcd(d, G)
            u, v = (G - d) // g, d // g
            rho_low, rho_high = d, d - G
            assert u > 0 and v > 0
            assert u * rho_low + v * rho_high == 0
            assert u + v == G // g
            assert gcd(u, v) == 1
            # Uniqueness of primitive nonnegative integer solution follows from gcd.
            if p == 2 and k == 2 and d in (1, 2):
                samples.append({"p": p, "k": k, "n": low + d, "L": low,
                                "U": high, "G": G, "d": d,
                                "branch_multiplicities_lower_upper": [u, v],
                                "signed_residuals_lower_upper": [rho_low, rho_high],
                                "signed_contributions": [u * rho_low, v * rho_high],
                                "positive_N_total": u + v})
            count += 1
            checks += 1
    ranges.append({"p":p, "k_min":1, "k_max": max_k, "interior_n_checked":count})
assert samples == [
  {"p":2,"k":2,"n":5,"L":4,"U":9,"G":5,"d":1,"branch_multiplicities_lower_upper":[4,1],"signed_residuals_lower_upper":[1,-4],"signed_contributions":[4,-4],"positive_N_total":5},
  {"p":2,"k":2,"n":6,"L":4,"U":9,"G":5,"d":2,"branch_multiplicities_lower_upper":[3,2],"signed_residuals_lower_upper":[2,-3],"signed_contributions":[6,-6],"positive_N_total":5}
]
print(json.dumps({"schema":"X6_LP019_SIGNED_RESIDUE_PRIMITIVE_INTEGER_CERT_V1",
                  "scope":"pure algebraic collapse n between adjacent p-powers; not native signed Cell pathway",
                  "ranges":ranges,"total_interior_n_checked":checks,"failure_count":0,
                  "examples":samples}, ensure_ascii=False, indent=2))
