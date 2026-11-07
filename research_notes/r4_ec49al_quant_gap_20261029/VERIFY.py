#!/usr/bin/env python3
"""EC49AL author-side exact checks; universal result is proved in PROOF.md."""
from fractions import Fraction as F
from itertools import product
import json

K = F(177, 172)
A = F(27, 172)
C1 = F(43, 48)
CUT = F(25, 32)
LABELS = ("A0", "A1", "B0", "B1")
COST = {"A0": 1, "A1": 1, "B0": 2, "B1": 2, "STOP": 0}

def t(eta, w, u):
    return F(1, 2) + (2 * u - 1) * (1 - w) * eta

def assess(eta, rows, r):
    """Compute lawful observed-atom best terminal decision, exactly."""
    assert all(sum(v.values(), F()) == 1 for v in rows)
    c1 = sum(F(COST[c], 3) * x for row in rows for c, x in row.items())
    assert c1 == C1
    alpha = beta = c2 = F()
    for c, u in product(LABELS, range(2)):
        q = [rows[w].get(c, F()) * t(eta, w, u) / 3 for w in range(3)]
        mass = sum(q)
        rc = r.get((c, u), F())
        assert 0 <= rc <= 1
        c2 += rc * mass
        for z in range(3):
            pp = sum((q[w] * (F(1, 2) if z == w else F(1, 4)) for w in range(3)), F())
            qq = mass / 3
            if pp - K * qq > 0:
                alpha += rc * pp
                beta += rc * qq
    return c1, c2, alpha, beta, alpha - K * beta

grid = 0
for q0 in range(25):
    for q1 in range(25 - q0):
        q2 = 24 - q0 - q1
        q = (q0, q1, q2)
        v = sum(max(0, 43 * z - 16 * 24) for z in q)
        assert 27 * 24 - v >= 32 * (24 - max(q)), q
        grid += 1
assert grid == 325
assert 27 * 24 - sum(max(0, 43 * z - 16 * 24) for z in (12, 12, 0)) == 32 * 12

eta_samples = [F(0), F(1, 200), F(3, 10), F(49, 100)]
for eta in eta_samples:
    assert all(t(eta, w, u) > 0 for w, u in product(range(3), range(2)))
    pp = qq = F()
    for w, u, z in product(range(3), range(2), range(3)):
        pp += t(eta, w, u) * (F(1, 6) if z == w else F(1, 12))
        qq += t(eta, w, u) / 9
    assert pp == qq == 1

pure_rows = [
    {"A0": F(1)}, {"A1": F(1)},
    {"B0": F(11, 32), "STOP": F(21, 32)},
]
pure_checks = 0
for eta, c2 in product(eta_samples, [F(0), F(1, 2), F(31, 40), CUT]):
    prob = c2 / CUT
    checked = assess(eta, pure_rows, {(c, u): prob for c, u in product(LABELS, range(2))})
    assert checked[1] == c2
    assert checked[2] == c2 / 2 and checked[3] == c2 / 3
    assert checked[4] == A * c2
    pure_checks += 1

eta = F(3, 10)
mixed_rows = [
    {"A0": F(1)}, {"A1": F(1)},
    {"A0": F(11, 16), "STOP": F(5, 16)},
]
r = F(39, 43)
c1, c2, alpha, beta, h = assess(
    eta, mixed_rows, {(c, u): r for c, u in product(LABELS, range(2))}
)
assert c2 == F(13, 16)
gap = A * c2 - h
rho = (1 - 2 * eta) / (1 + 2 * eta)
lower = F(32, 172) * rho * (c2 - CUT)
assert gap >= lower > 0

fmt = lambda x: str(x)
report = {
    "schema": "EC49AL_EXACT_GAP_V1",
    "status": "PASS_EXACT_FRACTION_AUTHOR_UNREVIEWED",
    "grid_compositions_checked": grid,
    "pure_boundary_exact_checks": pure_checks,
    "positive_source_eta_samples": list(map(fmt, eta_samples)),
    "universal_theorem_source": "PROOF.md (case analysis + capacity inequalities)",
    "bound": "Gap >= (8/43)*((1-2*eta)/(1+2*eta))*max(0,C2-25/32)",
    "post_cutoff_example": {
        "eta": fmt(eta), "C1": fmt(c1), "C2": fmt(c2), "r": fmt(r),
        "alpha": fmt(alpha), "beta": fmt(beta), "H": fmt(h),
        "gap": fmt(gap), "lower_certificate": fmt(lower),
        "first_stage": mixed_rows and "w0:A0, w1:A1, w2:11/16 A0 + 5/16 STOP",
    },
    "native_BRC": "NOT_CLAIMED",
    "independent_review": "NOT_PERFORMED",
}
print(json.dumps(report, ensure_ascii=False, indent=2))
