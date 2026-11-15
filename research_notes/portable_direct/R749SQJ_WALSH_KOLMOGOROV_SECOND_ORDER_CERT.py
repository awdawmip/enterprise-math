#!/usr/bin/env python3
"""Exact certificate for R749SQJ; Python 3 standard library only."""
from fractions import Fraction
from math import comb, factorial, prod
import json

MULT = {1: 3, 2: 4, 3: 6, 4: 4, 5: 3, 6: 2, 7: 1}
MAX_R = 10000
counts = [0] * MAX_R
counts[0] = 1
for weight, multiplicity in MULT.items():
    for _ in range(multiplicity):
        for t in range(weight, MAX_R):
            counts[t] += counts[t-weight]
C = [0] * (MAX_R + 1)
for r in range(1, MAX_R + 1):
    C[r] = C[r-1] + counts[r-1]
C0 = lambda t: C[t] if t > 0 else 0

W = prod(w ** n for w, n in MULT.items())
assert W == 94058496000 and sum(MULT.values()) == 23
A = sum(Fraction(n * (w-1), 2) for w,n in MULT.items())
L2 = sum(Fraction(n * (w-1) * (5-w), 24) for w,n in MULT.items())
B = A*A/2+L2
b = 23 * (11 + A)
c = 30107 + 23 * 231 * A + 23*22*B
assert (A, L2, B, b, c) == (28,Fraction(13,12),Fraction(4717,12),897,Fraction(2266627,6))
a23 = Fraction(1, factorial(23)*W)
a22 = Fraction(39, factorial(22)*W)
a21 = Fraction(c, factorial(23)*W)

# Independent 420-step quasipolynomial interpolation.
sequence = [C[1+420*j] for j in range(24)]
differences = []
while sequence:
    differences.append(sequence[0])
    sequence = [v-u for u,v in zip(sequence,sequence[1:])]
d21,d22,d23 = [differences[k] for k in (21,22,23)]
j23 = Fraction(d23,factorial(23))
j22 = Fraction(d22,factorial(22)) - 253*j23
j21 = Fraction(d21,factorial(21)) - Fraction(231*d22,factorial(22)) + 30107*j23
assert j23 == a23*420**23
assert j22 == (23*a23+a22)*420**22
assert j21 == (comb(23,2)*a23+22*a22+a21)*420**21

for t in range(1, MAX_R):
    assert C[t+1] * t**23 <= C[t] * (t+1)**23, t

resolutions = (120,420,840,1680,2940,3360,5000,10000)
comparisons = 0
for r in resolutions:
    atom_num = C[r]-C0(r-3)
    for k in range((r-1)//3+1):
        t = r-3*k
        left_num = t**23*C[r] - C0(t-3)*r**23
        assert abs(left_num) <= atom_num*r**23,(r,k,'post-jump')
        comparisons += 1
        if k:
            right_num = t**23*C[r] - C[t]*r**23
            assert abs(right_num) <= atom_num*r**23,(r,k,'pre-jump')
            comparisons += 1

print(json.dumps({
  "result":"PASS", "frozen_science":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
  "weight_multiplicities":MULT, "W":W, "A":str(A), "L2":str(L2), "B":str(B),
  "b":str(b), "c":str(c), "zero_atom_coefficients":{"r^-1":69,"r^-2":-4968,"r^-3":372623},
  "quasipolynomial_independent_top_coefficient_check":"PASS",
  "normalized_C_over_r23_monotone_range":[1,MAX_R],
  "kolmogorov_endpoint_resolutions":list(resolutions), "endpoint_comparisons":comparisons,
  "verification_scope":"Exact integer/Fraction checks; infinite claims are from the accompanying proof."
},sort_keys=True,indent=2))
