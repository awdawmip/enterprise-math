#!/usr/bin/env python3
"""Exact rational checks for the five-vertex exposed-face veto.
Auxiliary affine geometry only; not an X6 / BRC-Shor numerical simulation.
"""
from fractions import Fraction as F
from itertools import product

A = (F(1), F(0), F(0), F(0))
B = (F(0), F(1), F(0), F(0))
C = (F(0), F(0), F(1), F(0))
D = (F(0), F(0), F(0), F(1))
H1 = (F(1), F(-1), F(0), F(1))
H2 = (F(-1), F(1), F(1), F(0))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def separating_certificate(e):
    """Return (bypass witness, rational nonnegative-on-face affine form)."""
    a, b, c, d = e
    assert sum(e) == 1
    if b >= 0:
        return H1, (F(0), F(1), F(0), F(0)), "B_NONNEG"
    if c > 0:
        return H1, (F(0), F(1), -b / c, F(0)), "C_POSITIVE"
    if a >= 0:
        return H2, (F(1), F(0), F(0), F(0)), "A_NONNEG"
    assert d > 0  # follows from sum(e)=1, a,b<0 and c<=0
    return H2, (F(1), F(0), F(0), -a / d), "D_POSITIVE"


grid = tuple(F(k, 2) for k in range(-6, 7))
branches = {k: 0 for k in ("B_NONNEG", "C_POSITIVE", "A_NONNEG", "D_POSITIVE")}
for a, b, c in product(grid, repeat=3):
    e = (a, b, c, F(1) - a - b - c)
    h, form, branch = separating_certificate(e)
    branches[branch] += 1
    assert dot(form, h) == -1
    assert all(dot(form, v) >= 0 for v in (A, B, C, D, e))
assert sum(branches.values()) == len(grid)**3 == 2197

# Six vertices are sufficient for both witness points in abstract affine geometry.
points = (A, B, C, D, H1, H2)
xyz = tuple((v[1], v[2], v[3]) for v in points)
exposers = (
    (F(1), F(1), F(2)),     # A: unique minimum
    (F(-2), F(1), F(-1)),  # B: unique minimum
    (F(1), F(-2), F(0)),   # C: unique minimum
    (F(-1, 2), F(0), F(-1)),  # D: unique minimum (= max x/2+z)
    (F(1), F(0), F(0)),    # H1: unique minimum
    (F(-1), F(-1), F(0)), # H2: unique minimum (= max x+y)
)
for i, normal in enumerate(exposers):
    values = [dot(normal, p) for p in xyz]
    assert values[i] < min(v for j, v in enumerate(values) if j != i)

# Rational off-face penalty example: LR face = conv(A,B,C,D,H1).
# H2 is rejected by l_A; an extra LR point q off face has t=1.
q = (F(10), F(0), F(0), F(1))  # observer coordinates (x,y,z,t)
def ell_A(p):
    x, y, z, _ = p
    return F(1) - x - y - z

def cart(v):
    return (v[1], v[2], v[3], F(0))

m = max(F(0), -ell_A(q) / q[3])
assert m == 9
phi = lambda p: ell_A(p) + m * p[3]
assert all(phi(cart(v)) >= 0 for v in (A, B, C, D, H1))
assert phi(q) == 0 and phi(cart(H2)) == -1
normal_l1 = abs(F(-1)) + abs(F(-1)) + abs(F(-1)) + abs(m)
assert normal_l1 == 12

print("GRID_SIZE", len(grid) ** 3)
print("SEPARATOR_CASE_COUNTS", ",".join(f"{k}={branches[k]}" for k in branches))
print("SIX_VERTICES_ABSTRACT_SHARPNESS", "PASS")
print("OFF_FACE_PENALTY", m, "L_INF_LOWER_BOUND", F(1, normal_l1))
print("PASS_EXACT_R5_FIVE_VERTEX_FACET_VETO")
