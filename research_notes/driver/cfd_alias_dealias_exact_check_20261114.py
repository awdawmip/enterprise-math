#!/usr/bin/env python3
"""Exact stdlib-only CFD alias/dealias witness; no spectralDNS execution."""
from fractions import Fraction
from itertools import product

N = 16
K = 7
NU = (1, -7, 6)
P, Q = (7, 1, 0), (6, 0, -1)
A, B = (1, -7, 0), (0, 1, 0)

def dot(u, v):
    return sum(x*y for x, y in zip(u, v))

def add(u, v):
    return tuple(x+y for x, y in zip(u, v))

def scale(u, c):
    return tuple(c*x for x in u)

def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])

def wrap(u, n):
    return tuple((x+n//2) % n - n//2 for x in u)

def projection(u, k):
    return tuple(Fraction(x) - Fraction(dot(k, u)*z, dot(k, k))
                 for x, z in zip(u, k))

def sum_vectors(vectors):
    return tuple(sum(items, Fraction(0)) for items in zip(*vectors))

# Each cosine contributes two Fourier modes with real amplitudes a/2, b/2.
modes = [(P, scale(A, Fraction(1, 2))),
         (scale(P, -1), scale(A, Fraction(1, 2))),
         (Q, scale(B, Fraction(1, 2))),
         (scale(Q, -1), scale(B, Fraction(1, 2)))]
s = add(P, Q)
k = wrap(s, N)
assert (dot(NU, P), dot(NU, Q), dot(P, A), dot(Q, B)) == (0, 0, 0, 0)
assert s == (13, 1, -1) and k == (-3, 1, -1) and dot(NU, k) == -16
assert all(abs(x) <= K for x in k) and any(abs(x) > K for x in s)

# Coefficients below omit the common i and convection sign.
adv = []
vort = []
contributing_pairs = []
for (m, u), (n, v) in product(modes, repeat=2):
    if wrap(add(m, n), N) != k:
        continue
    contributing_pairs.append((m, n))
    adv.append(scale(v, dot(u, n)))
    vort.append(cross(cross(m, u), v))
assert len(contributing_pairs) == 2
c_adv = projection(sum_vectors(adv), k)
c_vort = projection(sum_vectors(vort), k)
assert c_adv == tuple(Fraction(x, 44) for x in (-1, -7, -4))
assert c_vort == tuple(Fraction(x, 44) for x in (223, 329, -340))

# 3/2 padded grid: w wraps to -11, outside original K=7 retention.
assert wrap(s, 24) == (-11, 1, -1)
assert not all(abs(x) <= K for x in wrap(s, 24))
assert add(P, scale(Q, -1)) == (1, 1, 1)
assert dot(NU, add(P, scale(Q, -1))) == 0

print("PASS exact alias/dealias mode test")
print("N16 alias:", k, "nu dot k:", dot(NU, k))
print("P_k advective Fourier coeff / i:", c_adv)
print("P_k rotational Fourier coeff / i:", c_vort)
print("N24 padded image:", wrap(s, 24), "retained:", False)
