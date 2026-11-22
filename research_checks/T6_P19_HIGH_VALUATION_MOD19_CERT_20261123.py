#!/usr/bin/env python3
"""Exact finite arithmetic check for the p=19, mass <=2331 valuation-two lemma.
This checks the finite determinant and mass facts; the accompanying proof
explains why H_0..H_6 equalities imply the six modular equations.
"""
import json
from fractions import Fraction
from math import prod

p=19
budget=2331
max_q=(budget+1)//(p*p)
assert p**3>budget+1
assert max_q==6
qs=list(range(1,max_q+1))
invs=[pow(q,-1,p) for q in qs]
mat=[[pow(x,k,p) for x in invs] for k in range(1,7)]

def determinant_mod(A,mod):
    a=[row[:] for row in A]
    det=1
    n=len(a)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]%mod),None)
        if pivot is None:
            return 0
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            det=-det
        x=a[j][j]%mod
        det=det*x%mod
        inv=pow(x,-1,mod)
        for i in range(j+1,n):
            multiplier=a[i][j]*inv%mod
            for k in range(j,n):
                a[i][k]=(a[i][k]-multiplier*a[j][k])%mod
    return det%mod

D=determinant_mod(mat,p)
V=prod(invs)%p
for i in range(len(invs)):
    for j in range(i+1,len(invs)):
        V=(V*(invs[j]-invs[i]))%p
caps=[budget//(p*p*q-1) for q in qs]
assert D==V==11
assert caps==[6,3,2,1,1,1]
assert max(caps)<p
out={
    "schema":"T6_P19_V19_SQUARED_MOD19_UNIVERSAL_CANCEL_CERT_V1",
    "arithmetic":"EXACT_INTEGER_MOD_19",
    "p":p,
    "maximum_side_exponent_mass":budget,
    "p_cubed":p**3,
    "v19_equals_two_denominator_form":"361*q, 1<=q<=6",
    "q_values":qs,
    "signed_multiplicity_abs_maximum_by_q":caps,
    "inverse_q_mod19":invs,
    "rows_k_1_to_6_columns_q_1_to_6":mat,
    "determinant_mod19":D,
    "vandermonde_product_mod19":V,
    "matrix_rank_mod19":6,
    "consequence":"All signed multiplicities for 19^2-divisible denominators vanish when H0..H6 match and both masses <=2331",
    "scope":"Any finite exponent shapes with e_i>=1, H0..H6 equality, and each side sum(e_i)<=2331; mathematical proof supplies the modular reduction",
    "source_admission":"AUTHOR_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED"
}
print(json.dumps(out,ensure_ascii=False,indent=2))
