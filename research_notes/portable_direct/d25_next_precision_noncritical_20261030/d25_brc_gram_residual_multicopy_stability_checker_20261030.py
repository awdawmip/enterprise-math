#!/usr/bin/env python3
"""Exact author-side integer checks for D25 BRC Gram residual stability.

Auxiliary positive-integer conditional-private-branch model. Not native X6.
"""
import itertools
import json
from fractions import Fraction
from math import isqrt

X = (0, 1, 2)
Y = (0, 1)
C = {0: 0, 1: 0, 2: 1}
R = {0: 0, 1: 2}  # representative for each observed fiber


def vectors(s):
    return tuple((j, s-j) for j in range(s+1))


def run_family(sizes, weights, max_m=3):
    """Exhaust finite observation-row tables (not all state-level V realizations).

    Every observation-row table admits state-level integer V: assign each
    output count to one fixed state in its observation fiber.
    """
    B = len(sizes)
    opts = [tuple(itertools.product(vectors(s), repeat=len(X))) for s in sizes]
    total_configs = 0
    total_source_tuples = 0
    total_target_rows = 0
    exact_cases = 0
    largest_slack = 0
    near_bound = None
    for batch in itertools.product(*opts):
        V = {b: dict(zip(X, table)) for b, table in enumerate(batch)}
        total_configs += 1
        D = {
            x: sum(weights[b] * sum((V[b][x][y] - V[b][R[C[x]]][y])**2 for y in Y)
                   for b in range(B))
            for x in X
        }
        for m in range(1, max_m+1):
            A = len(Y) * sum(weights[b] * sizes[b]**(2*m-2) for b in range(B))
            M = sum(weights[b] * sizes[b]**m for b in range(B))
            assert M > 0
            for xs in itertools.product(X, repeat=m):
                rs = tuple(R[C[x]] for x in xs)
                lhs = 0
                for ys in itertools.product(Y, repeat=m):
                    u = sum(weights[b] * _product(V[b][x][y] for x,y in zip(xs,ys))
                            for b in range(B))
                    r = sum(weights[b] * _product(V[b][x][y] for x,y in zip(rs,ys))
                            for b in range(B))
                    lhs += abs(u-r)
                rhs = sum(isqrt(A * D[x]) for x in xs)
                assert lhs <= rhs, (sizes, weights, V, xs, lhs, rhs)
                assert lhs % 2 == 0, (sizes,weights,xs,lhs)
                total_source_tuples += 1
                total_target_rows += len(Y)**m
                if lhs == rhs and lhs:
                    exact_cases += 1
                    if near_bound is None:
                        near_bound = dict(sizes=sizes, weights=weights, m=m, source=xs,
                                          lhs=lhs, rhs=rhs, total_mass=M)
                largest_slack = max(largest_slack, rhs-lhs)
    return dict(sizes=list(sizes),weights=list(weights),configs=total_configs,
                source_tuples=total_source_tuples,target_row_evaluations=total_target_rows,
                nontrivial_equality_cases=exact_cases,max_integer_bound_slack=largest_slack,
                equality_example=near_bound)


def _product(vals):
    v = 1
    for x in vals: v *= x
    return v


def sharp_history_check(steps=8):
    # X={r,x,c}, C(r)=C(x)=0, C(c)=1; B={0}, w=1, s=2.
    # V(r,r)=1, V(r,c)=1, V(x,x)=2, V(c,c)=2.
    # Every genuine path started at x observes 0 forever. Under the quotient
    # representative r, probability of the all-zero observation word is 2**(-t).
    V = {0: {0:2, 1:0}, 1: {0:1, 1:1}, 2: {0:0, 1:2}}
    rep = {0:1,1:2}
    D = sum((V[0][j]-V[1][j])**2 for j in Y)
    A = 2
    M = 2
    assert D == 2
    assert isqrt(A*D) == 2
    epsilon = Fraction(2,2*M)
    assert epsilon == Fraction(1,2)
    histories = []
    for t in range(1,steps+1):
        # Since only genuine all-zero word has mass, variation is exact 1-2^-t.
        true_path = {tuple([0]*t):Fraction(1,1)}
        # quotient uses 0->0 or 1 equiprobable; 1 stays 1
        P = {(0,): Fraction(1,2),(1,):Fraction(1,2)}
        for k in range(2,t+1):
            Q={}
            for path,p in P.items():
                if path[-1] == 0:
                    for j in (0,1):
                        new=path+(j,)
                        Q[new]=Q.get(new,Fraction())+p/2
                else:
                    new=path+(1,)
                    Q[new]=Q.get(new,Fraction())+p
            P=Q
        all_words=set(true_path)|set(P)
        tv=sum(abs(true_path.get(w,Fraction())-P.get(w,Fraction())) for w in all_words)/2
        target=1-(1-epsilon)**t
        assert tv == target, (t,tv,target)
        histories.append(dict(t=t,tv_num=tv.numerator,tv_den=tv.denominator,
                              upper_num=target.numerator,upper_den=target.denominator))
    return dict(D=D,one_step_tv=[epsilon.numerator,epsilon.denominator],
                t_horizon_exact=histories)


if __name__ == "__main__":
    families = [run_family((2,2),(1,2),3),run_family((2,3),(2,1),2)]
    sharp = sharp_history_check()
    # The equal-total-mass condition is necessary to interpret a normalized
    # quotient as faithful to integer BRC source counts. With a singleton
    # observer every normalized history agrees, but raw counts diverge.
    variable_mass_boundary = []
    for t in range(1,9):
        from_x, from_r = 2**t, 1**t
        assert Fraction(from_x,from_x) == Fraction(from_r,from_r)
        assert from_x != from_r
        variable_mass_boundary.append({"t": t, "integer_count_from_x": from_x,
                                       "integer_count_from_r": from_r})
    out = {
        "status":"PASS", "type":"AUTHOR_EXACT_INTEGER_CHECK", "date":"2026-10-30",
        "model":"auxiliary finite positive-integer BRC kernels, conditionally independent private paths; not native X6",
        "families":families,
        "aggregate_configs":sum(f["configs"] for f in families),
        "aggregate_source_tuples":sum(f["source_tuples"] for f in families),
        "aggregate_target_row_evaluations":sum(f["target_row_evaluations"] for f in families),
        "sharp_one_step_and_horizon":sharp,
        "variable_total_mass_obstruction": variable_mass_boundary,
        "proof_scope":"General finite-domain theorem is proved in companion Markdown; checks are exact finite cross-checks only.",
    }
    print(json.dumps(out,indent=2,ensure_ascii=False))
