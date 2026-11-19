#!/usr/bin/env python3
"""Exact integer necessary actuator-height bounds for R284AY; stdlib only."""
from math import factorial
import json
from pathlib import Path


def ceil_root(a, n):
    assert a >= 0 and n >= 1
    lo, hi = 0, 1
    while hi**n < a:
        hi *= 2
    while lo + 1 < hi:
        m = (lo + hi)//2
        if m**n < a:
            lo = m
        else:
            hi = m
    return hi


def lower_bound_K(n, H, delta_integer_gap=1):
    assert n >= 2 and H >= 1 and delta_integer_gap >= 1
    N = H ** (n*n)
    denom = 2 * factorial(n)
    target = ((N-1)*delta_integer_gap + denom - 1)//denom
    return max(0, ceil_root(target, n)-H)


def main():
    table = []
    for n, H in ((2,2),(3,2),(4,2),(8,2),(16,2),(32,2),(8,3),(16,3)):
        K = lower_bound_K(n,H)
        M = factorial(n)*(H+K)**n
        assert 2*M+1 >= H**(n*n)
        if K > 0:
            assert 2*factorial(n)*(H+K-1)**n+1 < H**(n*n)
        table.append(dict(n=n,H=H,min_necessary_K=K))
    # Closed-error intervals with minimum required integer-valued gap floor(2 delta)+1.
    for n, H in ((2,2),(3,2),(4,2),(8,2)):
        assert lower_bound_K(n,H,2) >= lower_bound_K(n,H,1)
    result = dict(research_unit='R284AY',status='PASS',cases=len(table),tables=table,
                  check='integer nth-root monotonicity and exact cardinality inequality',
                  scope='necessary bounds only; no tightness or independent review',review='NOT_REVIEWED')
    Path(__file__).with_name('R284AY_dynamic_range_exact_bounds.json').write_text(
        json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
