#!/usr/bin/env python3
"""Exact arithmetic regression for GEO8 R6 Lassak-template obstruction.

This checker verifies only finite/rational subcertificates of the proof.
The continuous O(5)/O(6) invariance and sign-balancing arguments are proved
in the Research Return and are not replaced by numerical sampling here.
"""

from fractions import Fraction
from itertools import product, combinations

SIGNS = list(product((-1, 1), repeat=5))
R2 = Fraction(3, 7)
ELL2 = Fraction(1, 84)
RHO2 = R2 - ELL2

assert RHO2 == Fraction(5, 12)

# 2 r ell = 1/7, verified without extracting radicals:
TWO_R_ELL_SQ = 4 * R2 * ELL2
assert TWO_R_ELL_SQ == Fraction(1, 49)
TWO_R_ELL = Fraction(1, 7)  # positive root because r, ell > 0
assert 2 * R2 + TWO_R_ELL == 1

# Cap-sector witness a = rho*u - ell*e6 and c = r*e6:
# |a-c|^2 = rho^2 + (r+ell)^2
CAP_SECTOR_DIST2 = RHO2 + R2 + ELL2 + TWO_R_ELL
assert CAP_SECTOR_DIST2 == 1

sector_pair_min = None
sector_pair_count = 0
for sigma, tau in combinations(SIGNS, 2):
    j = next(i for i in range(5) if sigma[i] != tau[i])
    # u_j = 3 sigma_j/sqrt(13), u_i = sigma_i/sqrt(13), and similarly v.
    dot_num = 9 * sigma[j] * tau[j]
    dot_num += sum(sigma[i] * tau[i] for i in range(5) if i != j)
    dot = Fraction(dot_num, 13)
    assert dot <= Fraction(-5, 13)
    dist2 = 2 * RHO2 * (1 - dot)
    assert dist2 >= Fraction(15, 13) > 1
    sector_pair_min = dist2 if sector_pair_min is None else min(sector_pair_min, dist2)
    sector_pair_count += 1

assert sector_pair_count == 496
assert sector_pair_min == Fraction(15, 13)

cap_sector_count = len(SIGNS)
assert cap_sector_count == 32

# The 33-atom incompatibility graph is K_33.
ATOM_COUNT = 1 + len(SIGNS)
INCOMPATIBILITY_EDGES = cap_sector_count + sector_pair_count
assert ATOM_COUNT == 33
assert INCOMPATIBILITY_EDGES == ATOM_COUNT * (ATOM_COUNT - 1) // 2 == 528

# Center-fixed, untruncated R6 hypercube-facet port:
# two same-facet cube directions can be forced to dot -2/3.
CENTER_FIXED_CUBE_DOT = Fraction(-2, 3)
CENTER_FIXED_FACET_DIST2 = 2 * R2 * (1 - CENTER_FIXED_CUBE_DOT)
assert CENTER_FIXED_FACET_DIST2 == Fraction(10, 7) > 1

# Lassak sector diameter certificate remains strict for every legal cap parameter:
# d_delta^2 = 2 r^2 + 2 h ell < 2 r^2 + 2 r ell = 1
# because 0 < delta < r implies h = sqrt(r^2-delta^2/4) < r.
assert 2 * R2 + TWO_R_ELL == 1

print(
    "PASS GEO8 exact Lassak R6 obstruction: "
    f"atoms={ATOM_COUNT} incompatibility_edges={INCOMPATIBILITY_EDGES} "
    f"sector_pair_lb2={sector_pair_min.numerator}/{sector_pair_min.denominator} "
    f"center_fixed_facet_lb2={CENTER_FIXED_FACET_DIST2.numerator}/{CENTER_FIXED_FACET_DIST2.denominator}"
)
