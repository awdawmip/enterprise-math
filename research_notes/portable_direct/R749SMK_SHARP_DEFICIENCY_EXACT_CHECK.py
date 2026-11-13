#!/usr/bin/env python3
"""Exact rational regression for R749SMK, the alpha=-1, gamma=0 observer.
The all-real optimum is proved in the companion note; this script tests a finite
parameter grid without using floating point or a numerical optimizer.
"""
from fractions import Fraction as Q
from itertools import product
import json

SIGNS = (-1, 1)
STATES = tuple(product(SIGNS, repeat=3))       # (x,y,t)
OUTS4 = tuple(product(SIGNS, repeat=2))       # (u,v)
OUTS8 = tuple(product(SIGNS, repeat=3))       # (u,v,w)


def channel(beta, source, obs):
    x, y, t = source
    u, v, _w = obs
    zu = y if u == 1 else t
    zminus = t if u == 1 else y
    common = Q(2-u*x, 32)
    return common * (2 + beta*v*zu), common * (2 + beta*v*zminus)


def garble(beta, out, incoming):
    b = abs(beta)
    d = 4 + 3*b
    a, c = (2+b)/d, b/d
    uo, vo, _wo = out
    ui, vi, _wi = incoming
    if uo == ui:
        return a / 2
    if vo == vi:
        return c / 2
    return Q(0)


def tv(lhs, rhs):
    return sum((abs(a-b) for a,b in zip(lhs,rhs)), Q(0)) / 2


def check(beta):
    b = abs(beta)
    predicted = b*(2+b)/(2*(4+3*b))
    col_sums = [sum((garble(beta, out, incoming) for out in OUTS8), Q(0))
                for incoming in OUTS8]
    assert all(x == 1 for x in col_sums)
    max_tv = Q(0)
    for state in STATES:
        f, p = zip(*(channel(beta, state, out) for out in OUTS8))
        assert sum(f) == sum(p) == 1
        simulated = tuple(sum((garble(beta, out, incoming) *
                               channel(beta, state, incoming)[0]
                               for incoming in OUTS8), Q(0)) for out in OUTS8)
        distance = tv(p, simulated)
        assert distance == predicted, (beta, state, distance, predicted)
        max_tv = max(max_tv, distance)
    q = b/(4+3*b)
    lower_a = b*(1-q)/4
    lower_b = (4*q + b*(3-q))/16
    assert lower_a == lower_b == predicted
    return {"beta":str(beta), "deficiency":str(max_tv),
            "optimizer_q":str(q), "sources_checked":len(STATES)}


def main():
    betas = tuple(Q(k, 8) for k in range(-8, 9))
    checked = [check(beta) for beta in betas]
    result = {
        "schema":"ENTERPRISE_MATH_R749SMK_EXACT_CHECK_V1",
        "date":"2026-11-13",
        "observer":"R749SMJ alpha=-1 gamma=0, arbitrary beta in [-1,1]",
        "frozen_scientific_input":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "claim":"delta(F->P)=delta(P->F)=abs(beta)*(2+abs(beta))/(2*(4+3*abs(beta)))",
        "method":"Python fractions.Fraction, full 8x8 outputs, exact channel normalization, explicit stochastic G, TV and algebraic lower-bound equality",
        "parameter_grid":len(checked),
        "source_columns_per_parameter":len(STATES),
        "total_source_column_checks":len(checked)*len(STATES),
        "total_stochastic_G_column_checks":len(checked)*len(OUTS8),
        "status":"PASS",
        "checks":checked
    }
    with open("R749SMK_SHARP_DEFICIENCY_RESULTS.json","w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
        f.write("\n")
    print("PASS", len(checked), "rational parameters,", len(checked)*len(STATES), "source channels")

if __name__=="__main__":
    main()
