#!/usr/bin/env python3
"""Exact arithmetic verification for PREFIX-329's S7-3 projective fiber lemma."""
from itertools import combinations
import json
import sympy as s

I = s.I
A = s.Matrix([
    [4, 4, 0],
    [0, -4, 4],
    [-5 + 3*I, 0, -3 + I],
    [-2 - 2*I, 4 + 4*I, 2 + 2*I],
    [-2, 0, 5 + 2*I],
])
minors = []
for rows in combinations(range(5),3):
    det = s.expand(A[list(rows), :].det())
    re, im = int(s.re(det)), int(s.im(det))
    norm_sq = re*re + im*im
    assert norm_sq > 0
    minors.append({"rows": [j+1 for j in rows], "re": re, "im": im, "norm_sq": norm_sq})
assert len(minors) == 10

x, y, u, v = s.symbols('x y u v', real=True)
z = s.Matrix([x+I*y, u+I*v, 1])
ports = (A*z)/8
q = [s.expand_complex(ports[j] * s.conjugate(ports[j])).simplify() for j in range(5)]
loc = {x:0, y:0, u:1, v:1}
q_loc = [s.factor(qj.subs(loc)) for qj in q]
assert q_loc == [s.Rational(1,2),s.Rational(1,4),s.Rational(5,32),s.Rational(13,8),s.Rational(29,64)]
J = s.Matrix([q[j]/q[4] for j in range(4)]).jacobian([x,y,u,v])
J_loc = J.subs(loc).applyfunc(s.factor)
J_det = s.factor(J_loc.det())
assert J_det == -s.Rational(113901568, 20511149)

z_loc = z.subs(loc)
source_ordered_pairs = 0
for j in range(5):
    vs = [s.expand(A[j,k] * z_loc[k] / 8) for k in range(3)]
    total = 0
    for k in range(3):
        for l in range(3):
            total += vs[k] * s.conjugate(vs[l]); source_ordered_pairs += 1
    assert s.simplify(total - q_loc[j]) == 0
assert source_ordered_pairs == 45
out = {
    "schema":"ENTERPRISE_MATH_PREFIX329_EXACT_CHECK_V1",
    "status":"PASS",
    "matrix":"U=A/8",
    "minor_count":len(minors),
    "all_3_by_3_minors_nonzero":True,
    "minor_table":minors,
    "sample_source":["0", "1+i", "1"],
    "sample_q":[str(a) for a in q_loc],
    "ratio_jacobian": [[str(v) for v in row] for row in J_loc.tolist()],
    "ratio_jacobian_det":str(J_det),
    "source_labelled_ordered_brc_pairs_checked":source_ordered_pairs,
    "degree_six_reason":"Segre P2xP2 has (h1+h2)^4=6; full-minor property gives base-point-free finite degree-six projection. This algebraic argument is in PROOF.md, not implied by the finite test.",
    "regular_fiber_even_reason":"Normalized physical intensity map CP2 to R4 has zero topological degree; regular preimages have signed count zero.",
}
print(json.dumps(out, ensure_ascii=False, sort_keys=True, indent=2))
