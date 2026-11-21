#!/usr/bin/env python3
"""Exact X6 Stage46 six-axis outer-grade collision law checker.
The scientific input is frozen at P000 V5@f42f2906 and Stage46 C[h,j]=1/6-1[h=j].
Python standard library; no floating arithmetic enters exact identities.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, pi
import json

D = 6
MAX_N = 60

def collision_counts(max_m):
    """A_d(m) = sum_{k1+...+kd=m} multinomial(m;k)^2."""
    a = [1] * (max_m + 1)
    for d in range(2, D+1):
        a = [sum(comb(m,k)**2 * a[m-k] for k in range(m+1))
             for m in range(max_m+1)]
    return a

def independent_word_enumeration(n):
    """Count complete endpoint/terminal-port fibers directly from named words."""
    hist = Counter()
    for word in product(range(D), repeat=n):
        coords = [0]*D
        for j in word:
            coords[j] += 1
        hist[(tuple(coords),word[-1])] += 1
    return sum(v*v for v in hist.values()),len(hist)

def run():
    a = collision_counts(MAX_N)
    rows = []
    for n in range(1,MAX_N+2):
        numerator, denominator = 6*a[n-1],36**n
        value = Fraction(numerator,denominator)
        rows.append(dict(n=n,coherent_pair_count=numerator,
                         denominator=denominator,exact_fraction=str(value),
                         float_value=float(value)))
    assert rows[0]["exact_fraction"] == "1/6"
    assert rows[1]["exact_fraction"] == "1/36"
    checks=[]
    for n in range(1,8):
        observed,fibers = independent_word_enumeration(n)
        expected=6*a[n-1]
        assert observed==expected,(n,observed,expected)
        checks.append(dict(n=n,enumerated_named_words=6**n,
                           enumerated_fibers=fibers,
                           observed_pair_count=observed,
                           recurrence_pair_count=expected))
    const=9/(8*pi**2.5)
    ratios={str(n):rows[n-1]["float_value"]*n**2.5/const
            for n in [4,8,12,20,40,61]}
    return dict(schema="PREFIX996_OUTER_GRADE_COLLISION_EXACT_V1",
        status="AUTHOR_PROOF_EXACT_INTEGER_CHECKED_NOT_REVIEWED",
        frozen_p000="f42f2906d77f24085c123f3ccfe9667d41caa96d",
        stage46="research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md",
        exact_formula="M_n=A_6(n-1)/(6*36**(n-1))",
        recurrence="A_1(m)=1; A_d(m)=sum_{k=0}^m binom(m,k)^2 A_(d-1)(m-k)",
        asymptotic="M_n ~ 9/(8*pi^(5/2))*n^(-5/2)",
        covariance_eigenvalues=["1/3 (multiplicity 4)","1/18 (multiplicity 1)"],
        covariance_determinant="1/1458",max_n_exact=MAX_N+1,
        selected_rows=[r for r in rows if r["n"] in [1,2,3,4,5,6,7,8,10,20,40,61]],
        brute_force_checks=checks,asymptotic_ratio_to_constant=ratios)

if __name__=="__main__":
    out=run()
    with open("PREFIX996_R6_EXACT_RESULTS.json","w",encoding="utf-8") as f:
        json.dump(out,f,ensure_ascii=False,indent=2,sort_keys=True)
        f.write("\n")
    print("BRUTE CHECKS:",out["brute_force_checks"])
    print("SELECTED:",[(r["n"],r["exact_fraction"]) for r in out["selected_rows"]])
    print("ASYMPTOTIC_RATIO:",out["asymptotic_ratio_to_constant"])
    print("ALL_ASSERTIONS_PASSED")
