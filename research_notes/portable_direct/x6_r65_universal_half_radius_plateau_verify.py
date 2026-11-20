#!/usr/bin/env python3
"""Exact integer checks for X6 R65: plateau onset of shared-bias BRC star moments.
Run with Python 3; no third-party dependencies.
The universal statement is proved in the companion Markdown, not by finite checks.
"""
from itertools import product
from math import comb, factorial
import json


def signed_stirling_first(n):
    coefficients = [1]
    for k in range(n):
        nxt = [0] * (len(coefficients) + 1)
        for j, v in enumerate(coefficients):
            nxt[j] -= k * v
            nxt[j + 1] += v
        coefficients = nxt
    return coefficients


def osc(values):
    return max(values) - min(values)


def witness(D):
    a = {d: (-1) ** d * comb(D + 1, d + 1) for d in range(2, D + 1)}
    p_plus = sum(max(v, 0) for v in a.values())
    p_minus = sum(max(-v, 0) for v in a.values())
    p0 = 2 ** D - D - 1
    assert p_plus == p0 and p_minus <= p0
    c = [0] * (D + 1)
    cp = [0] * (D + 1)
    for d, v in a.items():
        c[d] = max(v, 0)
        cp[d] = max(-v, 0)
    cp[0] += p_plus - p_minus
    assert sum(c) == sum(cp) == p0
    moment_differences = [sum((c[d]-cp[d]) * d**t for d in range(D+1))
                          for t in range(1, D+1)]
    assert osc(moment_differences) == 2
    assert [v-moment_differences[0] for v in moment_differences] == [1+(-1)**t if t>=2 else 0 for t in range(1, D+1)]
    return {
        'D': D, 'plateau_port_threshold': p0, 'a_2_to_a_D': list(a.values()),
        'positive_mass': p_plus, 'negative_mass': p_minus,
        'moment_differences': moment_differences,
        'ambiguous_histogram_c': c, 'ambiguous_histogram_c_prime': cp,
        'eta_at_and_above_threshold': '1/2'
    }


def last_coordinate_mask_check(D):
    s = signed_stirling_first(D)
    den = factorial(D)
    survivors = []
    for mask in range(1, 1 << (D-1)):
        num = 2 * sum(s[t] for t in range(2, D+1) if mask & (1 << (t-2)))
        if num % den == 0:
            survivors.append(mask)
    expected = sum(1 << (t-2) for t in range(2, D+1) if t%2 == 0)
    assert survivors == [expected], (D,survivors,expected)
    return {'D': D, 'nonzero_one_sided_width_two_patterns_tested': (1 << (D-1))-1,
            'integral_a_D_survivors': len(survivors)}


def finite_small_port_check(D, p):
    min_osc = None
    count = 0
    for a in product(range(-p,p+1), repeat=D-1):
        if not any(a):
            continue
        pp = sum(max(v,0) for v in a)
        pn = sum(max(-v,0) for v in a)
        if max(pp,pn) > p:
            continue
        count += 1
        z = [0] + [sum(a[d-2]*(d**t-d) for d in range(2,D+1)) for t in range(2,D+1)]
        delta = osc(z)
        if min_osc is None or delta < min_osc:
            min_osc = delta
    return {'D':D,'p':p,'feasible_nonzero_vectors_checked':count,
            'minimum_oscillation':min_osc,'eta_star':f'{min_osc}/4'}


def main():
    family=[witness(D) for D in range(2,13)]
    patterns=[last_coordinate_mask_check(D) for D in range(2,13)]
    rows=[]
    for D, populations in ((2,range(2,5)),(3,range(3,6)),(4,range(4,12)),(5,range(5,9))):
        for p in populations:
            rows.append(finite_small_port_check(D,p))
    expected={
        (3,3):6,(3,4):2,(4,4):14,(4,5):12,(4,10):12,(4,11):2,
        (5,5):30,(5,6):30,(5,7):30,(5,8):30
    }
    for r in rows:
        if (r['D'],r['p']) in expected:
            assert r['minimum_oscillation']==expected[(r['D'],r['p'])],r
    out={'schema':'X6_R65_EXACT_INTEGER_AUTHOR_CHECK_V1',
         'scope':'D=2..12 universal witnesses and necessary last-coordinate mask checks; full lattice minimum only for the listed small D,p cases',
         'status':'PASS','plateau_witnesses':family,
         'one_sided_width_two_pattern_checks':patterns,
         'finite_small_port_lattice_checks':rows,
         'pattern_count':sum(p['nonzero_one_sided_width_two_patterns_tested'] for p in patterns),
         'finite_lattice_vector_count':sum(r['feasible_nonzero_vectors_checked'] for r in rows)}
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
