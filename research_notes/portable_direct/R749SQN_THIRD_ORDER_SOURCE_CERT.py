#!/usr/bin/env python3
"""Exact integer/Fraction checks for R749SQN, auxiliary Walsh source alphabet.
This is a finite validation certificate; the all-r asymptotics use the paper proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
import json

def source_dp(weights, max_r, marked):
    """Exact equality-sum multiplicity/moment DP; return cumulative C_r, M_r."""
    c = [0] * max_r
    m = [0] * max_r
    c[0] = 1
    for i, s in enumerate(weights):
        for q in range(s, max_r):
            c[q] += c[q-s]
            m[q] += m[q-s] + (c[q-s] if i == marked else 0)
    C, M = [0], [0]
    for i in range(max_r):
        C.append(C[-1] + c[i])
        M.append(M[-1] + m[i])
    return C, M

def independent_enum(weights, r, marked):
    @lru_cache(None)
    def walk(i, left):
        if i == len(weights):
            return (1, 0)
        count = moment = 0
        for x in range(left // weights[i] + 1):
            c, m = walk(i + 1, left - weights[i] * x)
            count += c
            moment += m + (x * c if i == marked else 0)
        return count, moment
    return walk(0, r-1)

def smooth_coeff(weights, marked):
    d = len(weights)
    D = sum(s-1 for s in weights)
    Q = sum(s*s-1 for s in weights)
    h = weights[marked]
    A0 = F(1, d+1)
    A1 = F(D+d-1-h*(d+1), 2*(d+1))
    A2 = F(d*((d+1)*(h*h-1)-Q), 12*(d+1))
    A3 = -F(D+d-1, 2)*A2
    return (A0, A1, A2, A3)

def g3_sum(r):
    # S_3(r) = sum over zeta^3=1,zeta!=1 of zeta^{-(r-1)}/(1-zeta)^3.
    return (F(0), F(1,3), F(-1,3))[(r-1)%3]

def checks():
    alphabets = [
        ((1,1,1,2,4),0),((1,1,1,2,4),4),
        ((1,1,2),0),((1,1,2),2),
        ((1,1,3,3,6),0),((1,1,2,5,5),0),
        ((1,1,1,3,6,6),5), ((1,1,2,3,6),3),
    ]
    results = []
    first_moment_tests=0
    enumeration_tests=0
    for ww,j in alphabets:
        C,M = source_dp(ww,256,j)
        for r in range(1,257):
            # Deletion: E[K_r] C_r = sum_{k>=1} C_{r-kh}.
            assert M[r] == sum(C[r-k*ww[j]] for k in range(1,(r-1)//ww[j]+1))
            first_moment_tests+=1
        for r in range(1,35):
            assert (C[r],M[r]) == independent_enum(ww,r,j)
            enumeration_tests+=1
        results.append({"weights":ww,"marked_index":j,"h":ww[j],
                        "D":sum(x-1 for x in ww), "Q":sum(x*x-1 for x in ww),
                        "smooth_coefficients":[str(t) for t in smooth_coeff(ww,j)],
                        "C_256":str(C[256]),"M_256":str(M[256])})
    aa=(1,1,3,3,6);bb=(1,1,2,5,5)
    assert (len(aa),sum(x-1 for x in aa),sum(x*x-1 for x in aa)) == (5,9,51)
    assert (len(bb),sum(x-1 for x in bb),sum(x*x-1 for x in bb)) == (5,9,51)
    assert gcd(gcd(aa[2],aa[3]),aa[4])==3
    assert gcd(gcd(bb[2],bb[3]),bb[4])==1
    assert smooth_coeff(aa,0) == smooth_coeff(bb,0) == (F(1,6),F(7,12),F(-85,24),F(1105,48))
    assert smooth_coeff((1,1,2),2)==(F(1,4),F(-5,8),F(9,16),F(-27,32))
    assert smooth_coeff((1,1,2),0)==(F(1,4),F(-1,8),F(-3,16),F(9,32))
    # Finite values support the asymptotic formula; they are not a proof.
    samples=[]
    Ca,Ma=source_dp(aa,6003,0)
    Cb,Mb=source_dp(bb,6003,0)
    for r in (300,301,302,3000,3001,3002,6000,6001,6002):
        exact = F(Ma[r],r*Ca[r]) - F(Mb[r],r*Cb[r])
        leading = -10*g3_sum(r)
        scaled = exact*r**3
        samples.append({"r":r,"r_mod_3":r%3,"expected_limit":str(leading),
                        "scaled_exact_fraction":str(scaled),
                        "scaled_exact_decimal":format(float(scaled),".12f"),
                        "scaled_minus_limit_decimal":format(float(scaled-leading),".12f")})
        assert abs(scaled-leading) < F(1,1)
    return {"status":"PASS","model":"positive integer labeled-source multisets, auxiliary Walsh source line",
            "first_moment_deletion_checks":first_moment_tests,
            "independent_recursive_enumeration_checks":enumeration_tests,
            "max_r_dp":6002,"alphabet_results":results,
            "g3_periodic_values_n_0_1_2":["0","1/3","-1/3"],
            "matched_signature_example":{"A":aa,"B":bb,"shared_d_D_Q_h":[5,9,51,1],
                 "A_nonunit_gcd":3,"B_nonunit_gcd":1,
                 "predicted_r_cubed_mean_difference_by_r_mod_3":{"0":"10/3","1":"0","2":"-10/3"},
                 "samples":samples},
            "evidence_scope":"integer dynamic-programming and bounded independent enumeration only; infinite claims supplied by explicit pole proof; no independent peer review"}

if __name__=='__main__':
    print(json.dumps(checks(),ensure_ascii=False,indent=2))
