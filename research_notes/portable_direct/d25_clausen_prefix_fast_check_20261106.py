#!/usr/bin/env python3
"""Exact second-unit test: low/high signed boundary by one-pass prefix transfer.
Run after d25_clausen_signed_triangle_check_20261106.py in the same directory.
All p-adic quantities are in Z/pZ. Author-side, not native benchmark.
"""
import json
from math import isqrt


def primes(limit):
    for p in range(7, limit + 1):
        if p % 6 == 1 and all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def signed_boundary_prefix(p):
    assert p % 6 == 1
    m = (p - 1) // 6
    e = pow(10, -1, p)
    d = 1
    e_prefix = 0
    re_prefix = 0
    J = 0
    S0 = 1
    for i in range(1, m + 1):
        d = d * (6 * i - 5) * (3 * i - 2) * pow(36 * i * i, -1, p) % p
        if i > 1:
            e = e * 36 * (i-1)**2 * pow((6 * i - 1) * (3 * i - 1), -1, p) % p
        e_prefix = (e_prefix + e) % p
        re_prefix = (re_prefix + i * e) % p
        J = (J + d * ((1 + 6 * i) * e_prefix - 6 * re_prefix)) % p
        S0 = (S0 + d) % p
    return J, S0


def main():
    with open('20261106_d25_clausen_triangle_results.json',encoding='utf8') as f:
        old=json.load(f)
    for row in old['all_rows']:
        J,S=signed_boundary_prefix(row['p'])
        assert J == row['J_mod_p'], (row['p'],'J')
        assert S == row['S_mod_p'], (row['p'],'S')
    large=[]
    for p in primes(10007):
        if p <= 997:
            continue
        J,S = signed_boundary_prefix(p)
        target=p%24 in (13,19)
        if target:
            large.append({'p':p,'J_mod_p':J,'S_mod_p':S})
        assert not target or S == 0, (p,'potential counterexample to observed first factor',S)
    print(json.dumps({'status':'EXACT_FINITE_EXECUTED_NOT_UNIFORM_PROOF',
                      'previous_p6_1_checked':len(old['all_rows']),
                      'larger_target_checked':len(large),
                      'largest_target':large[-1] if large else None,
                      'p19_boundary_J':signed_boundary_prefix(19)[0],
                      'p373_boundary_J':signed_boundary_prefix(373)[0],
                      'assertion_failures':0},indent=2))


if __name__=='__main__':
    main()
