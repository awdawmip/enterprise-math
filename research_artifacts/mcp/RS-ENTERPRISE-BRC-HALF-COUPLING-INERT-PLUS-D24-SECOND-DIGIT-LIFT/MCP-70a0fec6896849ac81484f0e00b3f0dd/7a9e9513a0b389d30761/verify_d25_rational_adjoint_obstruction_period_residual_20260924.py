#!/usr/bin/env python3
"""Deterministic symbolic regression for the D25 rational-adjoint obstruction.

This checker is not the proof. The all-m theorem is the pole-orbit and degree
argument in d25_rational_adjoint_obstruction_period_residual_20260924.md.
"""
import sympy as sp

k, m, h, C = sp.symbols('k m h C')
A = (k-m)*(k-2*m)
B = 2*(k+1)**2
r0 = sp.cancel(A/B)

# Generic coefficient-root shift orbits are disjoint over Q(m).
K = sp.QQ.frac_field(m, h)
g = sp.gcd(sp.Poly(A, k, domain=K), sp.Poly(2*(k+h+1)**2, k, domain=K))
assert g.as_expr() == 1
assert sp.expand(A.subs(k, -h-1) - (h+m+1)*(h+2*m+1)) == 0

# Degree-at-infinity obstruction.
assert sp.limit(r0, k, sp.oo) == sp.Rational(1, 2)
c = sp.symbols('c', nonzero=True)
assert sp.simplify(c*(r0-1)-1) != 0
for d in range(1, 9):
    expr = sp.together(r0*(k+1)**d-k**d)
    assert sp.limit(expr/k**d, k, sp.oo) == sp.Rational(-1, 2)

# Exact variation-of-constants identity for the typed residual period.
H, U = sp.symbols('H U', nonzero=True)
Hn = r0*H
Un = U + C*H
z = U/H
zn = Un/Hn
assert sp.simplify(r0*zn-z-C) == 0

# q2 coordinate of the transpose adjoint decouples exactly.
r1 = (3*k-4*m)/(2*(k+1)**2)
r2 = 1/(k+1)**2
M = sp.Matrix([[r0,0,0],[r1/6,r0,0],[r2/36,r1/6,r0]])
xn, yn, zn0, x, y, z0 = sp.symbols('xn yn zn x y z')
lam_n = sp.Matrix([xn,yn,zn0])
lam = sp.Matrix([x,y,z0])
adj = M.T*lam_n-lam
assert sp.simplify(adj[2] - (r0*zn0-z0)) == 0

print('PASS: generic shift-gcd, degree obstruction, q2 decoupling, and exact period residual verified')
