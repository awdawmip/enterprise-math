#!/usr/bin/env python3
"""R222 exact rational finite regression; theorem rests on PSD spectral proof."""
from fractions import Fraction as Q
import json
from R221_markov_source_support_check import weights, markov_moments


def markov(k):
    n = k + 1
    pi = [Q(1,n)] * n
    if k == 0:
        return pi, [[Q(1)]]
    P = [[Q(1,2) if i == j else Q(1,2*k) for j in range(n)]
         for i in range(n)]
    return pi, P


def run():
    cases, diff_checks = 0, 0
    for k in range(4):
        pi, P = markov(k)
        for m in (1,12):
            for L in (1,2):
                w = weights(m,k,L)
                E = [markov_moments(n,w,pi,P)[0] for n in range(L,26)]
                for j in range(9):
                    for t in range(len(E)-j):
                        x = sum(((-1)**(j-h))*__import__('math').comb(j,h)*E[t+h]
                                for h in range(j+1))
                        assert (-1)**j*x >= 0, (k,m,L,j,t,x)
                        diff_checks += 1
                cases += 1

    pi, P = markov(2)
    w = weights(1,2,1)
    exact = [markov_moments(n,w,pi,P)[0] for n in range(1,13)]
    for n, observed in enumerate(exact,1):
        expected = Q(4) + Q(1,3)*Q(1,2)**(n-1) + Q(8,3)*Q(3,4)**(n-1)
        assert observed == expected
    return {
        'schema':'EM_R222_LAZY_REVERSIBLE_EXACT_TEST_V1',
        'status':'PASS',
        'assumption':'stationary positive pi; reversible P with nonnegative real spectrum',
        'families':cases,
        'alternating_difference_exact_checks':diff_checks,
        'non_iid_example':{'k':2,'m':1,'L':1,
                           'P':[[str(y) for y in row] for row in P],
                           'E_n_n1_to_n5':[str(e) for e in exact[:5]],
                           'exact_formula':'4+(1/3)(1/2)^(n-1)+(8/3)(3/4)^(n-1)'},
        'review':'NOT_REVIEWED',
        'native_BRC_executed':False}


if __name__ == '__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
