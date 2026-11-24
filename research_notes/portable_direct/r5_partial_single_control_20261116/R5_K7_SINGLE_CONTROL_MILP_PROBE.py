#!/usr/bin/env python3
"""Numerical MILP for k=7 named Set_0, slack=2, scoped future-safe family.
SciPy/HiGHS integer optimizer; verifies returned upper witnesses exactly.
Not an exact all-belief lower certificate; solver dual bound is numerical.
Frozen scientific source: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
import json
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

K, S = 7, 2
U = 1 << K


def q(x):
    return sum((x >> i & 1) * (x >> ((i+1) % K) & 1) for i in range(K))


def partial_loss(r, u):
    d = r & ~u
    e = r | (1 & ~d)
    return q(e) - q(e & ~d)


def build_beliefs(mode):
    if mode == 'static':
        return [frozenset(u for u in range(U) if (u & ~r) == 0 and q(r)-q(u) <= S)
                for r in range(U)], list(range(U))
    if mode == 'future':
        return [frozenset(u for u in range(U) if (u & ~r) == 0 and partial_loss(r,u) <= S)
                for r in range(U)], list(range(U))
    if mode == 'inert':
        static, _ = build_beliefs('static')
        cs = list(range(1,U,2))
        return [frozenset(t for t in range(U//2)
                          if 2*t in static[r] and 2*t+1 in static[r]) for r in cs], cs
    raise ValueError(mode)


def solve(mode):
    beliefs, centers = build_beliefs(mode)
    active = sorted(set().union(*beliefs))
    rows, low, high = [], [], []
    for u in active:
        rows.append({r:1 for r,b in enumerate(beliefs) if u in b})
        low.append(1.0)
        high.append(np.inf)
    if mode == 'future':
        for r,B in enumerate(beliefs):
            for v in (0,1):
                image = {(u & ~1) | v for u in B}
                targets = [s for s,C in enumerate(beliefs) if image <= C]
                row = {r:-1}
                for s in targets:
                    row[s] = row.get(s,0)+1
                rows.append(row)
                low.append(0.0)
                high.append(np.inf)
    A = lil_matrix((len(rows),len(beliefs)),dtype=np.float64)
    for i,row in enumerate(rows):
        for j,val in row.items(): A[i,j] = val
    result = milp(c=np.ones(len(beliefs)),integrality=np.ones(len(beliefs)),
                  bounds=Bounds(np.zeros(len(beliefs)),np.ones(len(beliefs))),
                  constraints=LinearConstraint(A.tocsc(),np.array(low),np.array(high)),
                  options={'mip_rel_gap':0})
    assert result.status == 0, result.message
    chosen = [i for i,x in enumerate(result.x) if x > 0.5]
    assert len(chosen) == round(result.fun)
    assert set().union(*(beliefs[i] for i in chosen)) == set(active)
    transitions = {}
    if mode == 'future':
        for i in chosen:
            transitions[str(centers[i])] = []
            for v in (0,1):
                im = {(u & ~1) | v for u in beliefs[i]}
                destinations = [j for j in chosen if im <= beliefs[j]]
                assert destinations
                transitions[str(centers[i])].append(centers[destinations[0]])
        for i in chosen:
            assert all(partial_loss(centers[i],u) <= S for u in beliefs[i])
    return {'mode':mode, 'reported_optimum':round(result.fun),
            'reported_dual_bound':float(result.mip_dual_bound),
            'reported_gap':float(result.mip_gap),
            'solver_status':result.status, 'candidate_centers':len(beliefs),
            'rows':len(rows), 'selected_centers':[centers[i] for i in chosen],
            'transitions_by_source_center':transitions,
            'exact_integer_witness_checked':True,
            'lower_certificate_scope':'numerical_HiGHS_MILP_only'}


def main():
    cases=[solve(m) for m in ('static','future','inert')]
    print(json.dumps({'status':'PASS_R5_K7_SCOPED_MILP_WITH_EXACT_WITNESS_CHECK',
        'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'model':{'k':7,'s':2,'J':[0]}, 'cases':cases,
        'conclusion_scope':'future is maximal future-safe B_r only; arbitrary belief transducer unresolved',
        'proof_status':'EXACT_UPPER_WITNESSES_NUMERICAL_MILP_LOWER_BOUNDS',
        'independent_review':'NOT_REVIEWED'},sort_keys=True,indent=2))
if __name__=='__main__':main()
