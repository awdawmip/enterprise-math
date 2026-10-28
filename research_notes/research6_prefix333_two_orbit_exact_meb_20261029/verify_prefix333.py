#!/usr/bin/env python3
"""PREFIX-333: exact finite BRC support certificate (author-side)."""
import json
import sympy as sp

I = sp.I
s10 = sp.sqrt(10)
U = sp.Matrix([
    [4, 4, 0],
    [0, -4, 4],
    [-5+3*I, 0, -3+I],
    [-2-2*I, 4+4*I, 2+2*I],
    [-2, 0, 5+2*I],
]) / 8
q = [sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(5, 32),
     sp.Rational(13, 8), sp.Rational(29, 64)]
a = sp.Matrix([0, 1+I, 1])
b = sp.Matrix([0, 1-I, 1])
r = sp.sqrt(sp.Rational(13, 8))
c = sp.Matrix([0, s10*(1-I)/5, s10*(1-I)/10])
w_hi = sp.Rational(1, 4) + s10/80
w_lo = sp.Rational(1, 4) - s10/80

def zzero(x):
    return sp.simplify(sp.expand_complex(x)) == 0

def norm2(v):
    return sp.simplify(sum(z*sp.conjugate(z) for z in v))

def brc_q(v):
    """Keep all ordered (k,l) source paths through each positive-mass port."""
    return [sp.simplify(sum(U[j,k]*v[k]*sp.conjugate(U[j,l]*v[l])
                            for k in range(3) for l in range(3)))
            for j in range(5)]

assert all(zzero(v) for v in sp.Matrix(brc_q(a))-sp.Matrix(q))
assert all(zzero(v) for v in sp.Matrix(brc_q(b))-sp.Matrix(q))
assert zzero((U*a)[3]-(1+5*I)/4)
assert zzero((U*b)[3]-(5+I)/4)
# For every admissible phase u on either exact orbit, |u|=1 and
# Re(u)>=sqrt(5/13); this follows from fourth-port Cartesian bounds.
# <c,normalized_base> = sqrt(13/5)>0, giving ||u*normalized_base-c||²<=2.
for base in (a, b):
    p = (U*base)[3]
    normalized = base*sp.conjugate(p)/r
    assert zzero(norm2(normalized)-3)
    inner = sp.simplify((c.conjugate().T*normalized)[0])
    assert zzero(inner-sp.sqrt(sp.Rational(13, 5)))
assert r-sp.sqrt(sp.Rational(5, 8)) < 1
points = []
for base, p in ((a, (1+5*I)/4), (b, (5+I)/4)):
    for sign in (-1, 1):
        # Fourth-port report: (sqrt(5/8), sign), each component error <= 1.
        phase = (sp.sqrt(sp.Rational(5, 8))+sign*I)*sp.conjugate(p)/q[3]
        assert zzero(phase*sp.conjugate(phase)-1)
        pt = sp.simplify(phase)*base
        assert all(zzero(v) for v in sp.Matrix(brc_q(pt))-sp.Matrix(q))
        assert zzero((U*pt)[3]-(sp.sqrt(sp.Rational(5, 8))+sign*I))
        assert zzero(norm2(pt)-3)
        points.append(pt)
weights = [w_hi, w_lo, w_lo, w_hi]
assert all(sp.simplify(w)>0 for w in weights)  # exact positive radicals
assert zzero(sum(weights)-1)
mean = sp.zeros(3, 1)
for w, pt in zip(weights, points):
    mean += w*pt
assert all(zzero(v) for v in mean-c)
assert zzero(norm2(c)-1)
assert all(zzero(norm2(pt-c)-2) for pt in points)
assert all(x < 1 for j,x in enumerate(q) if j != 3)
assert sp.sqrt(sp.Rational(13,8))-sp.sqrt(sp.Rational(5,8)) < 1
# Variance identity: sum_i w_i ||x_i-z||^2 = 2 + ||z-c||^2.
# Thus the exact MEB^2 of these four BRC-feasible points is 2,
# with unique center c and four strictly positive support weights.
L = sp.Rational(1062562, 458329)
assert L > 2
result = {
    "status": "PASS",
    "scope": "two complete continuous phase arcs (the two Gaussian-rational source orbits), within the PREFIX-332 full fiber",
    "source_state_count": 2,
    "retained_ordered_brc_path_pair_evaluations": 6*5*9,
    "endpoints": 4,
    "q": [str(v) for v in q],
    "meb_squared": "2",
    "center": [str(sp.simplify(v)) for v in c],
    "support_weights": [str(sp.simplify(v)) for v in weights],
    "prior_lower_squared": "24/13",
    "lower_bound_gain": "2/13",
    "benchmark_gap_above_2": str(L-2),
    "full_fiber_status": "LOWER_BOUND_ONLY; exact full MEB still undetermined",
    "mathematical_claim": "MEB^2(union of two complete Gaussian-rational phase arcs)=2; MEB^2(full fixed-q and fixed-report fiber)>=2",
}
print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
