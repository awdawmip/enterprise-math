#!/usr/bin/env python3
"""Exact bounded X6/P022 signed-BRC endpoint and G-shell type check.

Source identification (read, not executed):
  P000 V5: enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03
  X6 signed_brc.py: same frozen input source.
  Current P022 simple-cubic producer: git blob 46373050168d2430b6cb3952aa763f3081284632.
  Current P022 tests: git blob ef3da1a789186867c538b604da1b642bf6039591.
All computation below is independent, exact integer arithmetic, and not an import of production source.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product
from math import comb, factorial
import json


def require(condition: bool, name: str) -> None:
    if not condition:
        raise AssertionError(name)


def g(v: tuple[int, ...]) -> int:
    return sum(x*x for x in v)


def length(v: tuple[int, ...]) -> int:
    return sum(abs(x) for x in v)


def brc(v: tuple[int, ...]) -> int:
    n = length(v)
    denom = 1
    for x in v:
        denom *= factorial(abs(x))
    require(factorial(n) % denom == 0, 'factorial divisibility')
    return factorial(n) // denom


@lru_cache(None)
def recursive_brc(v: tuple[int, ...]) -> int:
    if all(x == 0 for x in v):
        return 1
    s = 0
    for i,x in enumerate(v):
        if x:
            nxt = list(v)
            nxt[i] += -1 if x>0 else 1
            s += recursive_brc(tuple(nxt))
    return s


def stirling(n: int, k: int) -> int:
    if not 0 <= k <= n:
        return 0
    a = [0]*(k+1)
    a[0] = 1
    for t in range(1,n+1):
        b = [0]*(k+1)
        for j in range(1,min(t,k)+1):
            b[j] = j*a[j] + a[j-1]
        a=b
    return a[k]


def sc_l1_shell_total(d: int, r: int) -> int:
    if r == 0:
        return 1
    return sum(comb(d,k)*2**k*factorial(k)*stirling(r,k)
               for k in range(1,min(d,r)+1))


def main() -> None:
    shell_g25 = [v for v in product(range(-5,6),repeat=3) if g(v)==25]
    shell_l15 = [v for v in product(range(-5,6),repeat=3) if length(v)==5]
    require(len(shell_g25)==30, 'G25 signed slice endpoints')
    require(len(shell_l15)==102, 'L1 radius5 signed slice endpoints')
    require(len(set(shell_g25)&set(shell_l15))==6, 'G25/L15 intersection')
    require(sum(brc(v) for v in shell_g25)==846, 'G25 BRC mass')
    require(sum(brc(v) for v in shell_l15)==1566, 'L15 BRC mass')
    require(sc_l1_shell_total(3,5)==1566, 'P022 closed integer Stirling formula')
    for v in shell_g25+shell_l15:
        require(brc(v)==recursive_brc(v),f'3D independent recursion mismatch {v}')
    six_vectors=[(3,0,0,-4,0,0),(0,-3,0,0,0,4),(1,-1,1,0,0,0),(-2,-2,-1,-1,0,0),(0,0,0,0,0,0)]
    for v in six_vectors:
        require(brc(v)==recursive_brc(v),f'6D independent recursion mismatch {v}')
        require(brc(v)==brc(tuple(-x for x in v)),f'signed reversal {v}')
    require(brc((3,0,0,-4,0,0))==35, 'six-axis 3/4 BRC')
    report={
        'status':'PASS_X6_LP019_P022_TYPED_SHELL_BRIDGE',
        'source_mode':'independent_recalculation_of_pinned_source_formulas',
        'source_version':{'frozen_p000':'59538f585d037d09ef687b28715c4bc1a3f9fe03','p022_producer_blob':'46373050168d2430b6cb3952aa763f3081284632','p022_test_blob':'ef3da1a789186867c538b604da1b642bf6039591'},
        'three_axis_G25':{'endpoints':len(shell_g25),'shortest_path_mass':sum(brc(v) for v in shell_g25),'l1_length_support':[5,7]},
        'three_axis_L1_radius5':{'endpoints':len(shell_l15),'shortest_path_mass':sum(brc(v) for v in shell_l15),'stirling_closed_mass':sc_l1_shell_total(3,5)},
        'endpoint_shell_intersection':len(set(shell_g25)&set(shell_l15)),
        'independent_three_axis_dp_matches':len(shell_g25)+len(shell_l15),
        'independent_six_axis_dp_matches':len(six_vectors),
        'project_admission':'NOT_REVIEWED',
        'production_module_executed':False,
        'claim':'endpoint_signed_BRC_equals_P022_sc_path_formula_for_standard_axis_steps; G_shell_and_L1_shell_are_distinct_summation_domains'
    }
    print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
