#!/usr/bin/env python3
"""Pending integration verifier; run in pinned Enterprise Math Source checkout.

PYTHONPATH=src python research_notes/research6_prefix270_brc_threshold_tomography_20261026/verify_prefix270_source.py

This has NOT been executed in the author-side session of 2026-10-26.
"""
from fractions import Fraction as F
from itertools import product
from enterprise_math.brc_weighted_recurrent import finite_recurrent_mass_analysis


def mass_star(m):
    a = finite_recurrent_mass_analysis(m)
    assert a.stable and a.star is not None and a.verify_stable_certificate()
    return a.star


def add(m, i, j, t):
    b = [list(row) for row in m]
    b[i][j] += t
    return tuple(tuple(row) for row in b)


checks = 0
matrices = 0
for n in (1, 2, 3):
    for bits in product((0, 1), repeat=n*n):
        w = tuple(tuple(F(bits[i*n+j], 4) for j in range(n)) for i in range(n))
        r = mass_star(w)
        matrices += 1
        for i in range(n):
            for j in range(n):
                tij = F(1, 1) / r[j][i] if r[j][i] else None
                probes = (F(0), F(1), F(100)) if tij is None else (F(0), tij/2, tij, tij*2)
                for t in probes:
                    x = finite_recurrent_mass_analysis(add(w, i, j, t))
                    assert x.stable == (tij is None or t < tij)
                    if x.stable:
                        den = 1 - t*r[j][i]
                        expected = tuple(tuple(r[u][v] + t*r[u][i]*r[j][v]/den
                                               for v in range(n)) for u in range(n))
                        assert x.star == expected
                    checks += 1
assert matrices == 530 and checks == 17528
print("PREFIX270_SOURCE_IMPORT_BRC_PASS 530 matrices 17528 checks")
