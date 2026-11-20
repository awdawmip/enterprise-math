#!/usr/bin/env python3
"""Named positive-BRC repeated-A star observer check, conditional branch model.
All p=1,2,3 labeled Boolean incidence matrices and t=1,2,3, exact integers."""
from itertools import product
for p in (1,2,3):
    for bits in range(1 << (p*p)):
        rows = [[j for j in range(p) if (bits >> (i*p+j)) & 1] for i in range(p)]
        counts = [sum(len(row)==d for row in rows) for d in range(p+1)]
        for t in (1,2,3):
            # Preserve each named A_i, B_{j_1},...,B_{j_t} branch.
            positive_brc_mass = sum(sum(1 for _ in product(row, repeat=t)) for row in rows)
            quotient_star_moment = sum(counts[d]*d**t for d in range(p+1))
            assert positive_brc_mass == quotient_star_moment
print("PASS: 530 labeled relations, 1590 exact named positive-BRC star checks")
