#!/usr/bin/env python3
"""Exact extra minimal-common-face certificate for all 49 frozen R5 sharp edges.
Requires same-directory VERIFY_SHARP_FACE.py. Runs the independently saved
full exact enumeration first, then verifies rank and relative-interior support.
"""
from pathlib import Path
from runpy import run_path
state = run_path(str(Path(__file__).with_name('VERIFY_SHARP_FACE.py')))
C = state['C']; ARCS = state['ARCS']; Ebar = state['Ebar']; Eprime = state['Eprime']
feasible = state['feasible']; F = state['F']
U = [k for k, v in enumerate(Ebar) if v > 0]
Z = {arc for arc, v in zip(ARCS,Ebar) if v == 0}
assert Z == {(0,3),(1,3),(6,1),(6,3)}
assert len(U) == 26 and C[:,U].rank() == 15
assert len(U) - C[:,U].rank() == 11
assert len(feasible) == 49
assert all(all(rec[4][k] == 0 for k,a in enumerate(ARCS) if a in Z) for rec in feasible)
assert Eprime[ARCS.index((6,1))] > 0
assert state['observer'](Ebar) == state['observer'](Eprime) == state['OBS0']
# The average of 49 strict edge-midpoints is positive on every coordinate
# attained positive in the union. Hence its support defines the unique
# minimal face containing all 49 edges. Rank gives exact affine dimension.
print('MINIMAL_FACE_FORBIDDEN_ARCS', sorted(Z))
print('MINIMAL_FACE_ALLOWED_ARCS', len(U))
print('MINIMAL_FACE_RESTRICTED_RANK', C[:,U].rank())
print('MINIMAL_COMMON_FACE_DIMENSION', len(U)-C[:,U].rank())
print('SOURCE3_ONLY_FACE_DIMENSION', 12)
print('STRICT_PROPER_SUBFACE_CERTIFICATE_E_6_1', Eprime[ARCS.index((6,1))])
print('PASS_R5_MINIMAL_SHARP_COMMON_FACE_11D')
