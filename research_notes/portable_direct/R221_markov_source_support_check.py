#!/usr/bin/env python3
"""R221: exact Markov-source principal-ideal moments; standard-library only.

Scientific object: finite paired-event observer monoid J_(m,k,L). This is an
abstract source-label Markov experiment, not a native BRC effect simulation.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial
import json


def stirling(n, r):
    if n == 0:
        return int(r == 0)
    if r == 0 or r > n:
        return 0
    return stirling(n - 1, r - 1) + r * stirling(n - 1, r)


def weights(m, k, depth):
    return [factorial(r) * m ** depth *
            sum(stirling(depth + 1, j + 1) for j in range(min(r, depth) + 1))
            for r in range(k + 1)]


def ideal_sizes(w):
    k = len(w) - 1
    return [sum(comb(k-r, j-r) * w[j] for j in range(r, k+1))
            for r in range(k+1)]


def mask_contained_probability(mask, n, pi, P):
    """P(S_n subset U); provenance 0 is included in every allowed set."""
    if n == 0:
        return Q(1)
    k = len(pi) - 1
    allow = [i for i in range(k + 1) if i == 0 or mask & (1 << (i - 1))]
    v = [pi[i] for i in allow]
    for _ in range(n - 1):
        v = [sum(v[t] * P[allow[t]][i] for t in range(len(allow)))
             for i in allow]
    return sum(v, Q(0))


def markov_moments(n, w, pi, P):
    k = len(w) - 1
    probs = [mask_contained_probability(u, n, pi, P) for u in range(1 << k)]
    first = sum((w[u.bit_count()] * probs[u] for u in range(1 << k)), Q(0))
    second = sum((w[u.bit_count()] * w[v.bit_count()] * probs[u & v]
                  for u in range(1 << k) for v in range(1 << k)), Q(0))
    return first, second, probs


def brute_moments(n, T, pi, P):
    k = len(pi) - 1
    mass = [Q(0)] * (1 << k)
    for seq in product(range(k+1), repeat=n):
        prob = pi[seq[0]]
        mask = 0
        for idx, lab in enumerate(seq):
            if idx:
                prob *= P[seq[idx-1]][lab]
            if lab:
                mask |= 1 << (lab-1)
        mass[mask] += prob
    first = sum((mass[mask] * T[mask.bit_count()] for mask in range(1<<k)), Q(0))
    second = sum((mass[mask] * T[mask.bit_count()]**2 for mask in range(1<<k)), Q(0))
    return first, second, mass


def source_exact_mass(mask, probs):
    sign_sum = Q(0)
    sub = mask
    while True:
        sign_sum += ((-1)**(mask.bit_count()-sub.bit_count())) * probs[sub]
        if sub == 0:
            return sign_sum
        sub = (sub - 1) & mask


def rational(q):
    return f"{q.numerator}/{q.denominator}"


def testcase(m, k, depth, n):
    pi = [Q(i+1, (k+1)*(k+2)//2) for i in range(k+1)]
    P = []
    for i in range(k+1):
        v = [((i+2)*(j+3) % 7)+1 for j in range(k+1)]
        P.append([Q(vj, sum(v)) for vj in v])
    w = weights(m, k, depth)
    T = ideal_sizes(w)
    moment1, moment2, probs = markov_moments(n, w, pi, P)
    check1, check2, mass = brute_moments(n, T, pi, P)
    assert (moment1, moment2) == (check1, check2), (m,k,depth,n)
    for mask in range(1<<k):
        assert source_exact_mass(mask, probs) == mass[mask], (k,n,mask)
    assert sum(mass) == 1
    return (k+1)**n, 1 << k


def run():
    cases = 0
    enumerated_paths = 0
    subset_checks = 0
    for k in range(4):
        for m in (1, 2, 12):
            for depth in (1, 2, 3):
                for n in range(depth, min(5, depth+2)+1):
                    cnt, subsets = testcase(m,k,depth,n)
                    cases += 1
                    enumerated_paths += cnt
                    subset_checks += subsets

    # Concrete non-iid, time-homogeneous counterexample, k=2,m=1,L=1.
    pi = [Q(1),Q(0),Q(0)]
    P = [[Q(0), Q(1), Q(0)],
         [Q(1,2),Q(0),Q(1,2)],
         [Q(0),Q(0),Q(1)]]
    w = weights(1,2,1)
    T = ideal_sizes(w)
    assert w == [1,2,4] and T == [9,6,4]
    E = [markov_moments(n,w,pi,P)[0] for n in range(1,16)]
    assert E[:5] == [Q(9),Q(6),Q(5),Q(5),Q(9,2)]
    for r in range(1,7):
        assert E[2*r] == E[2*r+1] == Q(4)+Q(2,2**r)
        assert E[2*r+2]-2*E[2*r+1]+E[2*r] == -Q(1,2**r)

    # IID specialization: all transition rows equal to the same initial marginal.
    iid_models = 0
    for k in range(4):
        p = [Q(i+1, (k+1)*(k+2)//2) for i in range(k+1)]
        P_iid = [p[:] for _ in p]
        for n in range(1,7):
            for U in range(1<<k):
                q = p[0]+sum((p[i] for i in range(1,k+1) if U & (1<<(i-1))),Q(0))
                assert mask_contained_probability(U,n,p,P_iid)==q**n
                iid_models += 1

    # Six-axis source-label alphabet, k=6,m=12,L=2 uses finite symbolic W,T.
    w6 = weights(12,6,2)
    T6 = ideal_sizes(w6)
    assert w6 == [144,576,1440,4320,17280,86400,518400]
    assert T6 == [1407600,1174176,986400,833760,708480,604800,518400]
    return {
        "schema":"EM_R221_MARKOV_SUPPORT_EXACT_CHECK_V1",
        "status":"PASS",
        "scope":"Exact source-label Markov observers; no native BRC runtime execution",
        "finite_models_checked": cases,
        "brute_paths_evaluated": enumerated_paths,
        "exact_support_mass_checks": subset_checks,
        "iid_reduction_checks": iid_models,
        "counterexample": {
            "m":1,"k":2,"L":1,
            "initial":["1","0","0"],
            "transition":[[rational(v) for v in row] for row in P],
            "W":w,"T":T,
            "E_n_n1_to_n8":[rational(v) for v in E[:8]],
            "delta2_E3":rational(E[4]-2*E[3]+E[2]),
            "infinitely_many_negative_second_differences":True,
            "exact_formula":"Delta^2 E_(2r+1)=-2^-r for all r>=1"
        },
        "native_six_axis_weights":w6,
        "native_six_axis_ideal_sizes":T6,
        "max_markov_recurrence_order_k6":(6+2)*2**(6-1),
        "independent_review":"NOT_REVIEWED"
    }


if __name__ == '__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
