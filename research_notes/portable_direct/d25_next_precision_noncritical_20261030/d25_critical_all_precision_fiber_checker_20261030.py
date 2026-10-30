#!/usr/bin/env python3
"""Exact author-side finite verification for critical square-port all-precision spectrum.

Finite configurations are an audit of the stated arbitrary-L algebraic proof,
not a numerical substitute for that proof. Uses actual modular polynomial
updates and the original two-factor observer (no simulated semantic placement).
"""
from collections import Counter, defaultdict
from itertools import product
import json
from pathlib import Path


def vp_at(x: int, p: int, cap: int) -> int:
    if x == 0:
        return cap
    t = 0
    while t < cap and x % p == 0:
        x //= p
        t += 1
    return t


def observer(x: int, q: int) -> int:
    return ((x + 1) * (pow(x, -1, q) + 1)) % q


def update(x: int, q: int, h: int, d: int) -> int:
    return (x + h * pow(x, d, q)) % q


def expected_critical(p: int, L: int, e: int):
    c = (L + 1) // 2
    m = max(0, L - e)
    records = []
    for t in range(1, c):
        if t < m:
            size = p ** min(t, e)
            classes = (p - 1) * p ** (L - t - 1 - min(t, e))
            mechanism = 'single_square_root_branch'
        else:
            size = 2 * p ** t
            classes = ((p - 1) // 2) * p ** (L - 2*t - 1)
            mechanism = 'two_square_root_branches'
        records.append((f'v={t}', size, classes, mechanism))
    high = max(c, m)
    records.append(('square_zero', p ** (L-high), p ** (high-c), 'zero_square_congruence'))
    assert sum(size * classes for _,size,classes,_ in records) == p ** (L-1)
    return records


def inspect_case(p, L, e, d, lam, full_cycle=False):
    q = p ** L
    h = (p ** e * lam) % q
    m = max(0, L - e)
    c = (L + 1) // 2
    expected = expected_critical(p,L,e)
    expected_counter = Counter()
    for _,size,count,_ in expected:
        expected_counter[size] += 2*count
    groups = defaultdict(list)
    by_layer = defaultdict(lambda: defaultdict(list))
    repair = defaultdict(list)
    observer_reads = 0
    state_updates = 0
    for x in range(1,q):
        residue = x % p
        if residue not in (1,p-1):
            continue
        y = update(x,q,h,d)
        state_updates += 1
        o0,o1=observer(x,q),observer(y,q)
        observer_reads += 2
        s = 1 if residue==1 else -1
        t=vp_at((x-s)%q,p,L)
        label=f'v={t}' if t < c else 'square_zero'
        key=(o0,o1)
        groups[key].append(x)
        by_layer[(s,label)][key].append(x)
        repair[(o0,x%(p**m))].append(x)
    actual=Counter(map(len,groups.values()))
    if actual!=expected_counter:
        raise AssertionError(f'fiber mismatch {(p,L,e,d,lam)}: {actual} != {expected_counter}')
    for s in (1,-1):
        for label,size,count,_ in expected:
            part=by_layer[(s,label)]
            if len(part)!=count or set(map(len,part.values()))!={size}:
                raise AssertionError(f'layer {(p,L,e,d,lam,s,label)} observed {Counter(map(len,part.values()))}, expected {(size,count)}')
    if {tuple(sorted(v)) for v in groups.values()}!={tuple(sorted(v)) for v in repair.values()}:
        raise AssertionError(f'failed source congruence equivalence {(p,L,e,d,lam)}')
    # Canonical finite full-future evidence: actual state permutation period verified.
    # Only selected small configurations: no unverified horizon assumption.
    full_period = None
    if full_cycle:
        period = p ** max(0, L-e)
        for first in (x for grp in groups.values() for x in grp):
            y=first
            for _ in range(period):
                y=update(y,q,h,d)
                state_updates+=1
            if y!=first:
                raise AssertionError(f'period identity fails {(p,L,e,d,lam,first)}')
        for grp in groups.values():
            representative=grp[0]
            for x in grp[1:]:
                u,v=representative,x
                for _ in range(period):
                    if observer(u,q)!=observer(v,q):
                        raise AssertionError(f'future collision failure {(p,L,e,d,lam,representative,x)}')
                    observer_reads+=2
                    u=update(u,q,h,d);v=update(v,q,h,d)
                    state_updates+=2
        full_period=period
    return {'p':p,'L':L,'e':e,'d':d,'lambda':lam,'sources':sum(map(len,groups.values())),
            'fibers':len(groups),'spectrum':{str(k):v for k,v in sorted(actual.items())},
            'expected_layers_per_ball':[{'layer':t,'size':size,'classes':count,'mechanism':mechanism} for t,size,count,mechanism in expected],
            'full_cycle_period_checked':full_period,'observer_reads':observer_reads,'updates':state_updates}


def main():
    records=[]
    # Parameter grid covers the two-root regime, truncated root regime, square-zero
    # regime, and static L<=e. Not meant to cover unbounded p,L,d.
    max_L={3:6,5:5,7:4,11:3}
    for p,max_chain in max_L.items():
        for L in range(1,max_chain+1):
            for e in range(1,L+2):
                for d,lam in product((2,4,6),(1,p-1)):
                    full_cycle=(p in (3,5) and L<=4 and e in (1,L-1,L+1) and d==2 and lam==1)
                    if p==3 and L==6 and e==1 and d==2 and lam==1:
                        full_cycle=True
                    records.append(inspect_case(p,L,e,d,lam,full_cycle))
    stats={'status':'PASS','configuration_count':len(records),
           'labelled_source_configuration_entries':sum(r['sources'] for r in records),
           'actual_two_factor_observer_reads':sum(r['observer_reads'] for r in records),
           'actual_polynomial_updates':sum(r['updates'] for r in records),
           'fully_checked_permutation_period_configurations':sum(r['full_cycle_period_checked'] is not None for r in records),
           'root_branch_double_size_witness':next((r for r in records if r['p']==5 and r['L']==5 and r['e']==4 and r['d']==2 and r['lambda']==1),None),
           'records':records,
           'scope':'finite exhaustive modular arithmetic; independent review and native X6 transfer not attempted',
           'original_observer':'(x+1)*(x^{-1}+1) mod p^L',
           'time_operation':'actual iterations of P(x)=x+p^e lambda x^d mod p^L'}
    out=Path(__file__).with_name('d25_critical_all_precision_fiber_author_check_20261030.json')
    out.write_text(json.dumps(stats,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in stats.items() if k not in ('records','root_branch_double_size_witness')},indent=2))
    print('p=5, L=5, e=4 witness',stats['root_branch_double_size_witness']['spectrum'])

if __name__=='__main__':
    main()
