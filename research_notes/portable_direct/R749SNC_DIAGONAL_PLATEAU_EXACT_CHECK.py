#!/usr/bin/env python3
"""Exact vertex certificate for Walsh diagonal minimax at 1/5 <= p <= 3/10.

Enumerates every vertex of a bounded full-dimensional 6D rational polytope
with 18 facet inequalities (16 source-positivity inequalities and two bounds).
Uses integer Bareiss elimination + Fraction back-substitution. No floating
point or external modules are used for the mathematical certificate.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import json


def chi(m, x):
    return (-1) ** ((m & x).bit_count() % 2)


# Columns: A,D,AD,P,AP,Q,DQ, with (A,D,P,Q) independent signs.
R = [tuple(chi(m, x) for m in (3, 12, 15, 1, 2, 4, 8)) for x in range(16)]
M = [tuple([a + d, ad, p0, ap, q, dq]) for a, d, ad, p0, ap, q, dq in R]
M += [(5, 0, 0, 0, 0, 0), (-10, 0, 0, 0, 0, 0)]
B = [-1] * 16 + [1, -3]  # 1 + p(A+D)+hAD+uP+vAP+wQ+zDQ >=0, p bounds


def solve_exact(subset):
    n = 6
    a = [list(M[i]) + [B[i]] for i in subset]
    previous = 1
    for j in range(n - 1):
        pivot_row = next((i for i in range(j, n) if a[i][j]), None)
        if pivot_row is None:
            return None
        if pivot_row != j:
            a[j], a[pivot_row] = a[pivot_row], a[j]
        pivot = a[j][j]
        for i in range(j + 1, n):
            below = a[i][j]
            for k in range(j + 1, n + 1):
                numerator = a[i][k] * pivot - below * a[j][k]
                assert numerator % previous == 0
                a[i][k] = numerator // previous
            a[i][j] = 0
        previous = pivot
    if a[n - 1][n - 1] == 0:
        return None
    z = [None] * n
    for j in range(n - 1, -1, -1):
        z[j] = (F(a[j][-1]) - sum((a[j][k] * z[k] for k in range(j + 1, n)), F(0))) / a[j][j]
    return tuple(z)


def source_law(p, h, u, v, w, z):
    return tuple((1 + p * (a+d) + h*ad + u*p0 + v*ap + w*q + z*dq) / 16
                 for (a, d, ad, p0, ap, q, dq) in R)


def tv(law, center):
    return sum((abs(x-y) for x, y in zip(law, center)), F(0)) / 2


def certify():
    ct = Counter()
    vertices = set()
    for subset in combinations(range(18), 6):
        ct['six_facet_subsets'] += 1
        sol = solve_exact(subset)
        if sol is None:
            continue
        ct['nonsingular_bases'] += 1
        if any(sum((a*b for a, b in zip(row, sol)), F(0)) < low
               for row, low in zip(M, B)):
            continue
        ct['feasible_bases'] += 1
        vertices.add(sol)
    ct['distinct_vertices'] = len(vertices)
    assert (ct['six_facet_subsets'], ct['nonsingular_bases'],
            ct['feasible_bases'], ct['distinct_vertices']) == (18564, 10848, 384, 106)

    slack_free, slack_cal = Counter(), Counter()
    for params in vertices:
        p, h, u, v, w, z = params
        assert p in (F(1, 5), F(3, 10))
        ct['p_1_5' if p == F(1, 5) else 'p_3_10'] += 1
        mu = source_law(*params)
        tau_free = p + F(1, 5)
        eta_free = F(1, 5)
        free = tuple((1 + tau_free * (a+d) + eta_free * ad) / 16 for a,d,ad,*_ in R)
        eta_cal = (1-2*p)/3
        cal = tuple((1 + p * (a+d) + eta_cal * ad) / 16 for a,d,ad,*_ in R)
        assert sum(mu) == sum(free) == sum(cal) == 1
        assert min(mu) >= 0 and min(free) >= 0 and min(cal) >= 0
        df = F(2,5) - tv(mu,free)
        dc = (1+p)/3 - tv(mu,cal)
        assert df >= 0 and dc >= 0, ('vertex counterexample',params,df,dc)
        slack_free[str(df)] += 1
        slack_cal[str(dc)] += 1
    assert ct['p_1_5'] == ct['p_3_10'] == 53
    assert slack_free['0'] == 58 and slack_cal['0'] == 66

    # Explicit lower-bound witnesses and observation events at exact endpoints.
    for p in (F(1,5), F(3,10)):
        mu_ad = source_law(p, F(1), F(0), F(0), F(0), F(0))
        mu_e = source_law(p, -p, F(0), F(0), -2*p, p-1)
        assert min(mu_ad)>=0 and min(mu_e)>=0
        E = [i for i, (a,d,ad,p0,ap,q,dq) in enumerate(R)
             if dq == -1 or (a == 1 and d == -1)]
        H = [i for i, (a,d,ad,p0,ap,q,dq) in enumerate(R)
             if (d == 1 and q == -1) or (a == 1 and d == -1)]
        assert sum(mu_e[i] for i in E) == 1
        assert sum(mu_e[i] for i in H) == 3*(1+p)/4
        assert sum(mu_ad[i] for i in range(16) if R[i][2] == 1) == 1
        ct['lower_bound_endpoint_checks'] += 1
    return {'research_unit':'R749SNC', 'status':'PASS',
            'frozen_science':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'arithmetic':'exact_integer_Bareiss_and_Fraction',
            'interval':['1/5','3/10'],
            'theorems':{'unrestricted_radius':'2/5',
                        'calibrated_radius':'(1+p)/3',
                        'calibration_penalty':'(5*p-1)/15'},
            'counts':dict(sorted(ct.items())),
            'unrestricted_slack_counts':dict(sorted(slack_free.items())),
            'calibrated_slack_counts':dict(sorted(slack_cal.items()))}


if __name__ == '__main__':
    print(json.dumps(certify(), ensure_ascii=False, indent=2))
