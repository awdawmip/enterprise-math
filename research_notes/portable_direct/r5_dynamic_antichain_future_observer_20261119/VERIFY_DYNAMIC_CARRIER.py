#!/usr/bin/env python3
"""Exact finite verification of abstract support-antichain dynamics.
No BRC arithmetic, no spatial dynamics or native X6 claims.
"""
from itertools import product
import json

def subset(s, t):
    return (s & t) == s

def maximal_masks(masks):
    masks = set(masks)
    return tuple(sorted(x for x in masks if not any(x != y and subset(x, y) for y in masks)))

def is_monotone(table, n):
    return all(subset(table[x], table[y]) for x in range(1 << n)
               for y in range(1 << n) if subset(x, y))

def antichain_formula(table, profile):
    return maximal_masks(table[b] for b in maximal_masks(profile))

def actual_updated(table, profile):
    return maximal_masks(table[x] for x in profile)

def check_function_space(n, m):
    domain = tuple(range(1 << n))
    all_profiles = [tuple(x for x in domain if (s >> x) & 1)
                    for s in range(1, 1 << len(domain))]
    functions = 0
    monotone_count = 0
    formula_count = 0
    for table in product(range(1 << m), repeat=len(domain)):
        functions += 1
        monotone = is_monotone(table, n)
        formula_works = all(antichain_formula(table, p) == actual_updated(table, p)
                            for p in all_profiles)
        assert monotone == formula_works, (n, m, table)
        monotone_count += monotone
        formula_count += formula_works
    return {'n': n, 'm': m, 'maps': functions, 'nonempty_profiles': len(all_profiles),
            'monotone_maps': monotone_count, 'formula_valid_maps': formula_count}

def components(integer_mask, L):
    out = []
    start = None
    for z in range(L + 1):
        inside = z < L and bool(integer_mask & (1 << z))
        if inside and start is None:
            start = z
        if not inside and start is not None:
            out.append((start, z - 1))
            start = None
    return out

def atomic_carrier(state_masks, L, extra_breaks=()):
    """One exact support per nonempty endpoint singleton or between-endpoint cell."""
    endpoints = {x for mask in state_masks for interval in components(mask, L)
                 for x in interval}
    endpoints.update(extra_breaks)
    ordered = sorted(endpoints)
    cells = []
    lower = 0
    for e in ordered:
        if lower <= e-1:
            cells.append((lower, e-1))
        cells.append((e,e))
        lower=e+1
    if lower<L:
        cells.append((lower,L-1))
    def support(z):
        return sum(1 << i for i,a in enumerate(state_masks) if (a>>z)&1)
    assert all(support(a)==support(b) for a,b in cells)
    assert len(cells)<=2*len(endpoints)+1
    return cells, tuple(support(a) for a,b in cells)

def exhaustive_endpoint_refinement():
    L = 5
    choices=[m for m in range(1,1<<L) if len(components(m,L))<=2]
    windows=[(a,b) for a in range(L) for b in range(a,L)]
    families=0
    windows_tested=0
    for states in product(choices,repeat=3):
        families+=1
        cells,masks = atomic_carrier(states,L)
        raw=tuple(sum(1 << i for i,mask in enumerate(states) if (mask>>z)&1)
                  for z in range(L))
        assert maximal_masks(masks)==maximal_masks(raw)
        for a,b in windows:
            win = sum(1<<z for z in range(a,b+1))
            clipped=tuple(s&win for s in states)
            refined, support_masks=atomic_carrier(clipped,L,extra_breaks=[a,b])
            brute=tuple(sum(1<<i for i,mask in enumerate(clipped) if (mask>>z)&1)
                        for z in range(L))
            assert maximal_masks(support_masks)==maximal_masks(brute)
            windows_tested+=1
    assert len(choices)==30 and families==27000 and windows_tested==405000
    return {'chain_length':L,'states':3,'state_set_choices':len(choices),
            'families':families,'clipping_windows_each':len(windows),
            'family_window_checks':windows_tested}

def geometric_counterexample():
    L=5
    a1=(1<<L)-1
    left=(1<<0)|(1<<1)
    right=(1<<3)|(1<<4)
    W=sum(1<<z for z in range(3))
    def B(a,b):
        return maximal_masks(sum(1<<i for i,v in enumerate((a,b)) if (v>>z)&1)
                             for z in range(L))
    before=[B(a1,left),B(a1,right)]
    after=[B(a1&W,left&W),B(a1&W,right&W)]
    assert before[0]==before[1]==(3,)
    assert after[0]==(3,) and after[1]==(1,)
    return {'universe':[0,4],'A1':[0,4],'A2_left':[0,1],
            'A2_right':[3,4],'gate':[0,2], 'before':[list(v) for v in before],
            'after':[list(v) for v in after]}

def main():
    result={'schema':'R5_DYNAMIC_ANTICHAIN_CARRIER_EXACT_FINITE_V1',
            'map_tests':[check_function_space(2,2),check_function_space(3,1)],
            'atom_refinement':exhaustive_endpoint_refinement(),
            'gate_counterexample':geometric_counterexample(),
            'scope':'Finite Boolean incidence profiles and exact discrete closed interval families; not native X6 dynamics'}
    print(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False))
    print('PASS_R5_DYNAMIC_CARRIER_MONOTONE_36_20_AND_REFINED_405000')

if __name__=='__main__':
    main()
