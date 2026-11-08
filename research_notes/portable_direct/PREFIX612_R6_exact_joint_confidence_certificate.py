#!/usr/bin/env python3
"""PREFIX-612-R6: exact confidence and count-only stopping for BRC signed labels.
Original BRC graph source is inherited from PREFIX-610/611, NOT re-executed here.
"""
from fractions import Fraction
from math import comb
from itertools import product
import json
from pathlib import Path

SCIENCE_PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
NATIVE_BLOB = "7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41"
PREVIOUS_COMMIT = "9b5a1df1a87eca3478a0b2f665b887135ae14711"
BETA = Fraction(1, 240)

def occupancy_counts(nmax, d, q, r):
    """D_0(n)=(q-d)^n; D_i(n)=sum_(m>=r) C(n,m)D_(i-1)(n-m)."""
    assert 1 <= d <= q and 1 <= r <= nmax
    prev = [(q-d)**n for n in range(nmax + 1)]
    for i in range(1, d + 1):
        cur = [0] * (nmax + 1)
        for n in range(i*r, nmax + 1):
            cur[n] = sum(comb(n, m)*prev[n-m] for m in range(r,n+1))
        prev = cur
    return prev

def brute_occupancy(n, d, q, r):
    return sum(1 for w in product(range(q), repeat=n)
               if all(w.count(i) >= r for i in range(d)))

def one_hit_formula(n, d, q):
    return sum((-1)**a*comb(d,a)*(q-a)**n for a in range(d+1))

def two_hit_formula(n, d, q):
    total = 0
    for j in range(d+1):
        sub, falling = 0, 1
        for a in range(min(j,n)+1):
            if a: falling *= n-a+1
            sub += comb(j,a)*falling*(q-j)**(n-a)
        total += (-1)**j*comb(d,j)*sub
    return total

def binomial_mass(m, k, p):
    return comb(m,k)*p**k*(1-p)**(m-k)

def exact_cp_accepts(m, k, p, beta=BETA):
    if m == 0:
        assert k == 0
        return True
    upper = sum(binomial_mass(m,i,p) for i in range(k,m+1))
    lower = sum(binomial_mass(m,i,p) for i in range(k+1))
    return upper >= beta/2 and lower >= beta/2

def sharp_threshold(row, q, d, r, success):
    for n in range(d*r,len(row)):
        if row[n]*success.denominator >= success.numerator*q**n:
            assert n==0 or row[n-1]*success.denominator < success.numerator*q**(n-1)
            return n
    raise ValueError("Search window insufficient")

def run():
    checks = 0
    for q,d in ((3,2),(4,2)):
        for r in (1,2,3):
            row = occupancy_counts(7,d,q,r)
            for n in range(8):
                assert row[n] == brute_occupancy(n,d,q,r)
                assert 0 <= row[n] <= q**n
                checks += 1
    for q,d in ((3,2),(12,12),(24,12)):
        for r,formula in ((1,one_hit_formula),(2,two_hit_formula)):
            row=occupancy_counts(25,d,q,r)
            for n in range(26):
                assert row[n]==formula(n,d,q)
                checks += 1
    assert (1-BETA)**12 >= Fraction(19,20)
    checks += 1
    cp_rows=[]
    for m in range(13):
        for p in (Fraction(0),Fraction(1,10),Fraction(1,5),
                  Fraction(1,2),Fraction(3,4),Fraction(1)):
            covered=sum((binomial_mass(m,k,p) for k in range(m+1)
                         if exact_cp_accepts(m,k,p)), Fraction(0))
            assert covered >= 1-BETA
            cp_rows.append((m,str(p),str(covered)))
            checks += 1
    rows=[]
    for r in (3,4):
        for q in (12,24):
            words=occupancy_counts(320,12,q,r)
            for target in (Fraction(19,20),Fraction(99,100)):
                n=sharp_threshold(words,q,12,r,target)
                rows.append({"r":r,"d":12,"q":q,"target":str(target),
                             "minimum_N":n})
                checks += 2
    assert [(x["r"],x["q"],x["target"],x["minimum_N"]) for x in rows] == [
       (3,12,"19/20",110),(3,12,"99/100",133),
       (3,24,"19/20",224),(3,24,"99/100",270),
       (4,12,"19/20",131),(4,12,"99/100",155),
       (4,24,"19/20",265),(4,24,"99/100",314)]
    H12=sum((Fraction(1,i) for i in range(1,13)),Fraction(0))
    assert H12 == Fraction(86021,27720)
    checks += 1
    result={"status":"ALL_CHECKS_PASS",
            "status_level":"AUTHOR_PROVED / EXACT_ARITHMETIC_CHECKED / UNREVIEWED / NOT_ADMITTED",
            "science_pin":SCIENCE_PIN,"native_blob":NATIVE_BLOB,
            "upstream_prefix611_commit":PREVIOUS_COMMIT,
            "scope":"Independent one-step BRC signed-label experiment; count-only stopping",
            "confidence":"CP binomial tails >= beta/2; m=0 yields full parameter interval",
            "beta":str(BETA),"joint_coverage":"(1-beta)^d >= 19/20 for d<=12",
            "occupancy":"D0(n)=(q-d)^n; Di(n)=sum(m>=r) C(n,m)*D(i-1)(n-m)",
            "sharp_threshold_rows":rows,
            "first_hit_expectations":{"q12":str(12*H12),"q24":str(24*H12)},
            "confidence_grid_size":len(cp_rows),"exact_checks":checks,
            "native_graph_reexecuted":False}
    Path(__file__).with_name("PREFIX612_R6_RESULTS.json").write_text(
      json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"checks":checks,
        "thresholds":[(x["r"],x["q"],x["target"],x["minimum_N"]) for x in rows]}))

if __name__=="__main__":
    run()
