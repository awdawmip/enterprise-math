#!/usr/bin/env python3
"""Exact rational certificate: BRC signed-label neutral-thinning time changes.
Scientific context: frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d;
uses the declared signed-label law of PREFIX-610, not a fresh native graph run.
No third-party dependencies or numerical approximation.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb
import json

CHECKS = 0

def check(x, y, context):
    global CHECKS
    assert x == y, (context, x, y)
    CHECKS += 1

def coverage_cdfs(q, d, r, horizon):
    """Capped occupancy process: exact Pr(T<=n), n=0..horizon."""
    done = (r,) * d
    states = {(0,) * d: F(1)}
    cdf = [F(0)]
    for _ in range(horizon):
        nxt = {}
        for state, mass in states.items():
            if state == done:
                nxt[done] = nxt.get(done, F(0)) + mass
                continue
            moves = {state: F(q-d, q)}
            for i in range(d):
                after = list(state)
                after[i] = min(r, after[i]+1)
                after = tuple(after)
                moves[after] = moves.get(after, F(0)) + F(1, q)
            for after, weight in moves.items():
                nxt[after] = nxt.get(after, F(0)) + mass*weight
        states = nxt
        check(sum(states.values()), F(1), ("coverage_mass",q,d,r))
        cdf.append(states.get(done, F(0)))
    return cdf

def signed_probabilities(q, theta):
    d=len(theta)
    weights=[F(1,2*q)*(1+48*sign*x)
             for x in theta for sign in (-1, 1)]
    neutral=F(q-d,q)
    check(sum(weights)+neutral,F(1),("mass",q,theta))
    return weights,neutral

def sign_rule_cdfs(q, theta, horizon):
    """Stop when both direction IDs appear and at least one sees both signs."""
    weights, neutral=signed_probabilities(q,theta)
    d=len(theta)
    def success(state):
        return (all((state>>(2*i))&3 for i in range(d))
                and any(((state>>(2*i))&3)==3 for i in range(d)))
    states={0:F(1)}
    out=[F(0)]
    for _ in range(horizon):
        nxt={}
        for state,mass in states.items():
            if success(state):
                nxt[state]=nxt.get(state,F(0))+mass
                continue
            nxt[state]=nxt.get(state,F(0))+mass*neutral
            for j,weight in enumerate(weights):
                after=state|(1<<j)
                nxt[after]=nxt.get(after,F(0))+mass*weight
        states=nxt
        check(sum(states.values()),F(1),("signed_mass",q))
        out.append(sum(m for s,m in states.items() if success(s)))
    return out

def sign_rule_moments(q,theta):
    """First three raw moments via exact acyclic-progress Markov equations."""
    weights,_=signed_probabilities(q,theta)
    d=len(theta)
    @lru_cache(None)
    def solve(state):
        if all((state>>(2*i))&3 for i in range(d)) and any(((state>>(2*i))&3)==3 for i in range(d)):
            return F(0),F(0),F(0)
        progress=[]
        for j,p in enumerate(weights):
            after=state|(1<<j)
            if after!=state:
                progress.append((p,solve(after)))
        advancing=sum((p for p,_ in progress),F(0))
        assert advancing>0
        a=(1+sum(p*v[0] for p,v in progress))/advancing
        b=(2*a-1+sum(p*v[1] for p,v in progress))/advancing
        c=(3*b-3*a+1+sum(p*v[2] for p,v in progress))/advancing
        return a,b,c
    a,b,c=solve(0)
    return a,b-a*a,c-3*a*b+2*a*a*a

def thinning_transform(f,n):
    # At n global trials, an independent Binomial(n,1/2) number of
    # original experiment draws has occurred.
    return sum((F(comb(n,j),2**n)*f[j] for j in range(n+1)),F(0))

# Entire finite count-process CDF: independent q=24 DP vs q=12 thinning.
for d in (2,4,6):
    for r in (1,2):
        a=coverage_cdfs(12,d,r,16)
        b=coverage_cdfs(24,d,r,16)
        for n in range(17):
            check(thinning_transform(a,n),b[n],("coverage_thin",d,r,n))

# Nontrivial sign-adaptive stopping, with nonuniform conditional signs.
theta=(F(0),F(1,96))
a=sign_rule_cdfs(12,theta,24)
b=sign_rule_cdfs(24,theta,24)
for n in range(25):
    check(thinning_transform(a,n),b[n],("adaptive_thin",n))

# Exact moment transform including third cumulant, plus independently
# calculated nontrivial adaptive-stop values.
a1,a2,a3=sign_rule_moments(12,theta)
b1,b2,b3=sign_rule_moments(24,theta)
check((a1,a2,a3),(F(198,7),F(14090,49),F(2492850,343)),"adaptive_q12")
check((b1,b2,b3),(F(396,7),F(59132,49),F(21184572,343)),"adaptive_q24")
check((b1,b2,b3),(2*a1,4*a2+2*a1,8*a3+12*a2+6*a1),"third_cumulant")

out={
 "result":"ALL_CHECKS_PASS", "assertions":CHECKS,
 "frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "model":"PREFIX-610 signed-label law; independent one-step trials",
 "coverage_test":{"d":[2,4,6],"r":[1,2],"horizon":16},
 "adaptive_test":{"theta":["0","1/96"],"horizon":24,
  "rule":"both labels observed AND one direction has both signs",
  "mean_q12":str(a1),"variance_q12":str(a2),"third_cumulant_q12":str(a3),
  "mean_q24":str(b1),"variance_q24":str(b2),"third_cumulant_q24":str(b3)},
 "new_native_graph_execution":False,"independent_math_review":False
}
print(json.dumps(out,ensure_ascii=False,indent=2))
