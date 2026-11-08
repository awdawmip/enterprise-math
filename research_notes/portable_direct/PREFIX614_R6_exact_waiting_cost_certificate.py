#!/usr/bin/env python3
"""Exact rational certificates for BRC signed-label coverage waiting costs.

Scientific input: PREFIX-610--613 reduced native signed-label experiment,
frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
No original native PREFIX-565 graph re-execution is claimed.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, comb
from pathlib import Path
import json

def polynomial_power(base, exponent):
    coefficients = [Q(1)]
    for _ in range(exponent):
        product = [Q(0)] * (len(coefficients)+len(base)-1)
        for n,x in enumerate(coefficients):
            for m,y in enumerate(base):
                product[n+m] += x*y
        coefficients = product
    return coefficients

def poissonized_moments(d, r):
    """First two moments of maximum of d iid Gamma(r,1) variables."""
    base = [Q(1, factorial(j)) for j in range(r)]
    ez, ez2 = Q(0), Q(0)
    for a in range(1,d+1):
        sign = (-1)**(a+1) * comb(d,a)
        powers = polynomial_power(base,a)
        ez += sign * sum(
            (coef*Q(factorial(n),a**(n+1)) for n,coef in enumerate(powers)),
            Q(0))
        ez2 += 2*sign * sum(
            (coef*Q(factorial(n+1),a**(n+2))
             for n,coef in enumerate(powers)),Q(0))
    return ez,ez2

def finite_markov_moments(q,d,r):
    """Independent capped-count Markov recurrence with symmetric histograms."""
    @lru_cache(maxsize=None)
    def recurse(counts):
        s = sum(counts[:-1])
        if s == 0:
            return Q(0),Q(0)
        next_e,next_e2 = Q(0),Q(0)
        for j in range(r):
            n = counts[j]
            if n == 0:
                continue
            destination = list(counts)
            destination[j] -= 1
            destination[j+1] += 1
            e,e2 = recurse(tuple(destination))
            next_e += n*e
            next_e2 += n*e2
        mean = (q+next_e)/s
        second = (2*q*mean-q+next_e2)/s
        return mean,second
    return recurse((d,)+(0,)*r)

def as_json(x):
    return {"numerator":str(x.numerator),"denominator":str(x.denominator)}

def run():
    checks=0
    result=[]
    for d in (1,2,6,12):
        for r in (1,2,3,4):
            mu,m2 = poissonized_moments(d,r)
            v = m2-mu**2
            assert v >= 0
            checks+=1
            if r == 1:
                assert mu == sum((Q(1,j) for j in range(1,d+1)),Q(0))
                checks+=1
            slot={}
            for q in (12,24):
                e,e2=finite_markov_moments(q,d,r)
                var=e2-e**2
                assert e == q*mu
                assert var == q*q*v-q*mu
                assert var >= 0
                checks+=3
                slot[str(q)] = {
                    "expected_trials":as_json(e),
                    "variance_trials":as_json(var),
                    "expected_trials_decimal":round(float(e),12),
                    "variance_trials_decimal":round(float(var),12),
                }
            a = slot["12"]["expected_trials"]
            b = slot["24"]["expected_trials"]
            e12 = Q(int(a["numerator"]),int(a["denominator"]))
            e24 = Q(int(b["numerator"]),int(b["denominator"]))
            assert e24 == 2*e12
            checks+=1
            a = slot["12"]["variance_trials"]
            b = slot["24"]["variance_trials"]
            v12 = Q(int(a["numerator"]),int(a["denominator"]))
            v24 = Q(int(b["numerator"]),int(b["denominator"]))
            assert v24 == 4*v12+e24
            checks+=1
            result.append({
                "d":d,"r":r,
                "gamma_max_mean":as_json(mu),
                "gamma_max_variance":as_json(v),
                "slot_models":slot,
            })
    return {
        "title":"PREFIX-614-R6 exact native BRC signed-label coverage waiting-time moments",
        "model":"P(Y=(l,s))=(1+48*s*theta_l)/(2*q); neutral 1-d/q; independent trials",
        "frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "calculation":"exact rational; gamma integral + finite capped-count Markov chain",
        "checks":checks,
        "status":"ALL_CHECKS_PASS",
        "results":result,
    }

if __name__=="__main__":
    output=run()
    target=Path(__file__).with_name("PREFIX614_R6_RESULTS.json")
    target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(output["status"],output["checks"])
    for row in output["results"]:
        if row["d"] == 12:
            a=row["slot_models"]
            print("r=",row["r"],"E12=",a["12"]["expected_trials_decimal"],
                  "E24=",a["24"]["expected_trials_decimal"],
                  "Var12=",a["12"]["variance_trials_decimal"])
