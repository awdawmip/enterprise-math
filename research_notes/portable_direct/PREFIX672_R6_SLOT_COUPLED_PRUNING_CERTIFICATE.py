#!/usr/bin/env python3
"""Exact rational implication certificate for R6 PREFIX-672-SC.

Checks positivity of the slot-coupled cubic Bernstein polynomial.
Predecessors: PREFIX-659, 660, 670. This is not a replay of 189 layers.
"""
from fractions import Fraction as F
from math import comb
import json

N=245197
q0, dq=F(12),F(12)
a0,a1=F(451,12), F(11347,24)
b0,b1=F(12800000,12), F(51500000,24)
l0,l1=F(76650,12), F(306490,24)

def poly_add(*polys):
    out=[F(0)]*max(map(len,polys))
    for pol in polys:
        for i,x in enumerate(pol):out[i]+=x
    return out

def poly_mul(x,y):
    out=[F(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):out[i+j]+=a*b
    return out

def bernstein_of_degree(poly,d):
    return [
        sum((poly[k]*F(comb(j,k),comb(d,k))
             for k in range(min(j,len(poly)-1)+1)),F(0))
        for j in range(d+1)
    ]

q=[q0,dq]
A=[a0,a1-a0]; B=[b0,b1-b0]
ell=[l0,l1-l0]
L=poly_mul(q,ell)
C=poly_add([F(15000,2)*x for x in poly_mul(q,q)],
           [F(221,2)*x for x in q])
P=poly_add([F(2,N)*x for x in poly_mul(B,L)],
           [F(2,N*N)*x for x in poly_mul(B,C)],
           [-x for x in poly_mul(q,poly_mul(A,A))])
assert len(P)==4
beta=bernstein_of_degree(P,3)
assert all(x>0 for x in beta)
assert min(beta)==beta[3]
assert b0<b1
assert beta[3]/(2*b1)>F(1,300000)
assert L[0]==76650 and sum(L)==306490
assert C[0]==1081326 and sum(C)==4322652
assert F(1,64)>F(1,N)

# N+1 is outside the guarantee of the *same sufficient certificate* at q=24.
N2=N+1
p2=F(1,N2)
D24=F(24)*a1*a1/(2*b1)
assert F(306490)*p2+F(4322652)*p2*p2-D24<0
assert F(306490,N)+F(4322652,N*N)-D24>F(1,300000)

results={
    "result_id":"PREFIX-672-SC-R6",
    "scientific_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "q_interval":[12,24],
    "p_interval":[f"1/{N}","1/64"],
    "z_interval":["607/4096","609/4096"],
    "competitor":["0","19/128"],
    "margin_lower_bound":"1/300000",
    "polynomial_P_power_coefficients":[str(x) for x in P],
    "bernstein_degree_3_coefficients":[str(x) for x in beta],
    "P_min_rational":str(beta[3]),
    "b_max_rational":str(b1),
    "p_remaining_width_improvement_factor":"245197/61317",
    "excluded_fraction":"245133/245197",
    "next_denominator_bound_negative":True,
    "status":"AUTHOR_DERIVED_EXACT_RATIONAL_IMPLICATION_CHECKED_UNREVIEWED_NOT_ADMITTED"
}

if __name__=="__main__":
    print("ALL_CHECKS_PASS: slot-coupled cubic Bernstein coefficients strictly positive")
    print(json.dumps(results,ensure_ascii=False,indent=2))
