#!/usr/bin/env python3
"""Exact domain regression: successor couplings, CRT obstruction, and history repair.

This is not a new general-purpose calculus, a native Cell placement algorithm,
or an independent mathematical review. It reuses composition_safe_collapse.
Run from EM root with PYTHONPATH=src, or supply --source-root for a verified
source snapshot. Outputs are deterministic JSON; all mathematics uses integers
and fractions.Fraction, never floating-point decisions.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import importlib
import json
from math import gcd, lcm
from pathlib import Path
import sys
from typing import Any

EXPECTED_BLOB = '384d166f642fb65c53fc7f2431f43dc99880693a'
SOURCE_SHA = 'bcaaffe18fe17656a4f926a86907957b88387b0a'


def positive(n: int) -> None:
    if type(n) is not int or n < 1:
        raise ValueError('positive integer required')


def floor_fraction(x: F) -> int:
    return x.numerator // x.denominator


def overlap(m: int, n: int) -> dict[tuple[int, int], F]:
    """Common-interval coupling of two ordered uniform populations."""
    positive(m); positive(n)
    ans: dict[tuple[int, int], F] = {}
    i = j = 0
    while i < m and j < n:
        left = max(F(i, m), F(j, n))
        right = min(F(i + 1, m), F(j + 1, n))
        if left < right:
            ans[i, j] = right - left
        a, b = F(i + 1, m), F(j + 1, n)
        if a <= b:
            i += 1
        if b <= a:
            j += 1
    return ans


def successor(n: int) -> dict[tuple[int, int], F]:
    positive(n)
    return {(i, j): F(w, n * (n + 1))
            for i in range(n) for j, w in ((i, n-i), (i+1, i+1))}


def marginals(p: dict[tuple[int, int], F]) -> tuple[dict[int, F], dict[int, F]]:
    rows: dict[int, F] = defaultdict(F)
    cols: dict[int, F] = defaultdict(F)
    for (i, j), w in p.items():
        assert w > 0
        rows[i] += w; cols[j] += w
    return dict(rows), dict(cols)


def component_count(m: int, n: int, p: dict[tuple[int, int], F]) -> int:
    parent = list(range(m+n))
    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for i, j in p:
        parent[find(i)] = find(m+j)
    return len({find(i) for i in range(m+n)})


def phi(n: int) -> int:
    return sum(gcd(k, n) == 1 for k in range(1, n+1))


def cuts(h: int) -> list[F]:
    positive(h)
    return sorted({F(k, n) for n in range(1, h+1) for k in range(n+1)})


def signatures(h: int) -> tuple[list[F], list[tuple[int, ...]], list[F]]:
    f = cuts(h)
    mid = [(a+b)/2 for a, b in zip(f, f[1:])]
    words = [tuple(floor_fraction(n*t) for n in range(1,h+1)) for t in mid]
    weights = [b-a for a,b in zip(f,f[1:])]
    return mid, words, weights


def interval_chain(h: int) -> dict[tuple[F, F, int], F]:
    """Posterior-interval lift; at most two positive successors per state."""
    states = {(F(0), F(1), 0): F(1)}
    for n in range(1, h):
        out: dict[tuple[F,F,int], F] = defaultdict(F)
        for (a,b,i), mass in states.items():
            assert mass == b-a
            for j in (i, i+1):
                c,d = max(a,F(j,n+1)), min(b,F(j+1,n+1))
                if c < d:
                    out[c,d,j] += mass*(d-c)/(b-a)
        states = dict(out)
        assert len(states) == sum(phi(k) for k in range(1,n+2))
        assert sum(states.values(), F()) == 1
        by_rank: dict[int,F] = defaultdict(F)
        for (a,b,i),mass in states.items():
            assert mass == b-a
            by_rank[i] += mass
        assert by_rank == {i:F(1,n+1) for i in range(n+1)}
    return states


def exhaustive_integer_couplings(n: int) -> tuple[int,int]:
    """Enumerate scaled tables with row n+1 and column n for n<=3."""
    if n not in (2,3):
        raise ValueError('intentionally bounded to n=2 or 3')
    total = 0
    best = n*(n+1)
    def row_vectors(cap: tuple[int,...], s: int, ix: int=0, sofar: tuple[int,...]=()):
        if ix == len(cap):
            if s == 0:
                yield sofar
            return
        for v in range(min(cap[ix],s)+1):
            yield from row_vectors(cap,s-v,ix+1,sofar+(v,))
    def rec(r: int, cap: tuple[int,...], edges: int) -> None:
        nonlocal total,best
        if r == n:
            if not any(cap):
                total += 1; best=min(best,edges)
            return
        for row in row_vectors(cap,n+1):
            rec(r+1,tuple(a-b for a,b in zip(cap,row)),edges+sum(v>0 for v in row))
    rec(0,(n,)*(n+1),0)
    return total,best


def run(source_root: Path) -> dict[str, Any]:
    src = source_root / 'enterprise_math' / 'composition_safe_collapse.py'
    b=src.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if blob != EXPECTED_BLOB:
        raise ValueError('reuse source hash mismatch: use the pinned immutable module')
    sys.path.insert(0,str(source_root))
    tool=importlib.import_module('enterprise_math.composition_safe_collapse')
    pair_checks=0
    for m in range(1,41):
        for n in range(1,41):
            p=overlap(m,n); r,c=marginals(p)
            assert r == {i:F(1,m) for i in range(m)}
            assert c == {j:F(1,n) for j in range(n)}
            assert len(p) == m+n-gcd(m,n)
            assert component_count(m,n,p) == gcd(m,n)
            pair_checks += 1
    for n in range(1,201):
        p=successor(n)
        assert p==overlap(n,n+1) and len(p)==2*n
        r,c=marginals(p)
        assert r=={i:F(1,n) for i in range(n)}
        assert c=={j:F(1,n+1) for j in range(n+1)}
        common=F(1,n*(n+1))
        tv=1-sum((min(w,common) for w in p.values()),F())
        assert tv==F(n-1,n+1)
        cost=sum((w*(F(2*i+1,2*n)-F(2*j+1,2*(n+1)))**2
                  for (i,j),w in p.items()),F())
        assert cost==F(2*n*n+2*n-1,12*n*n*(n+1)**2)
    # Natural cyclic CRT is a representative of the generic coprime-quotient law.
    crt_checks=0
    for n in range(2,61):
        pairs={(t%n,t%(n+1)) for t in range(n*(n+1))}
        assert len(pairs)==n*(n+1)
        assert len(pairs.intersection(successor(n)))==2*n
        crt_checks+=1
    # Memoryless composition of the adjacent laws vs a retained common phase.
    p23=successor(2); p34=successor(3)
    memoryless: dict[tuple[int,int],F]=defaultdict(F)
    for (i,j),w in p23.items():
        for (j0,k),v in p34.items():
            if j==j0:
                memoryless[i,k]+=w*3*v  # second law conditional on uniform C3
    bad=sum((w for (i,k),w in memoryless.items() if k//2 != i),F())
    assert bad==F(1,6)
    actual=overlap(2,4)
    assert all(k//2==i for i,k in actual)
    tv_24=sum((abs(memoryless.get(z,F())-actual.get(z,F()))
               for z in set(memoryless)|set(actual)),F())/2
    assert tv_24==F(1,6)
    # Full pair labels cannot be recovered from floor partitions in rank six.
    floor_pairs={(i//3,i//2) for i in range(6)}
    assert len(floor_pairs)==4
    # Execute the exact repository T6 repair, not a replacement implementation.
    horizon=60
    mids,words,weights=signatures(horizon)
    domain=tuple(range(len(mids)))
    coarse={i:0 for i in domain}
    counts=[]
    for n in range(1,horizon+1):
        observed={i:words[i][n-1] for i in domain}
        coarse=tool.coarsest_one_step_repair(domain,coarse,observed)
        assert tool.descends_through(domain,coarse,observed)
        assert tool.class_count(coarse)==sum(phi(k) for k in range(1,n+1))
        counts.append(tool.class_count(coarse))
    assert tool.class_count(coarse)==len(mids)==len(set(words))
    coarse3={i:words[i][2] for i in domain}
    observed4={i:words[i][3] for i in domain}
    witness=tool.fiber_constancy_witness(domain,coarse3,observed4)
    assert witness is not None
    # Phase successor and both additive/multiplicative carry formulas.
    carry_checks=0
    for t in mids[::max(1,len(mids)//100)]:
        for n in range(1,21):
            qn=floor_fraction(n*t); rn=n*t-qn
            assert floor_fraction((n+1)*t)-qn in (0,1)
            for m in range(1,11):
                qm=floor_fraction(m*t); rm=m*t-qm
                assert floor_fraction((n+m)*t)==qn+qm+floor_fraction(rn+rm)
                assert floor_fraction((n*m)*t)==m*qn+floor_fraction(m*rn)
                assert floor_fraction((n*m)*t)//m==qn
                carry_checks+=1
    # Exact interval updater reconstructs all feasible full-history intervals.
    lifted=interval_chain(40)
    f40=cuts(40)
    assert {(a,b) for a,b,_ in lifted}==set(zip(f40,f40[1:]))
    table_checks={str(n): {'table_count':t,'minimum_support':s}
                  for n in (2,3) for t,s in (exhaustive_integer_couplings(n),)}
    assert all(v['minimum_support']==2*int(k) for k,v in table_checks.items())
    states_by_h={str(h):sum(phi(k) for k in range(1,h+1)) for h in (10,20,40,60,100)}
    for h in (1,2,3,4,5,10):
        q=lcm(*range(1,h+1))
        for n in range(1,h+1):
            counts_grid=Counter((n*t)//q for t in range(q))
            assert set(counts_grid.values())=={q//n}
    return {
        'status':'PASS_EXACT_FINITE_REGRESSION_NOT_FORMAL_PROOF_OR_ADMISSION',
        'source_snapshot':SOURCE_SHA,
        'reuse':{'tool':'T6_OPERATION_SAFE_QUOTIENT', 'state':'REUSE_EXECUTED',
                'source':'src/enterprise_math/composition_safe_collapse.py',
                'git_blob_sha1':blob,
                'methods':['coarsest_one_step_repair','descends_through','fiber_constancy_witness','class_count']},
        'general_minimum_support_pair_checks':pair_checks,
        'adjacent_kernel_tv_and_quadratic_cost_checks':200,
        'cyclic_crt_pair_checks':crt_checks,
        'exhaustive_scaled_coupling_tables':table_checks,
        'memoryless_2_to_4_wrong_coarsening_mass':str(bad),
        'memoryless_vs_common_phase_2_to_4_total_variation':str(tv_24),
        'rank_6_floor_pair_support':len(floor_pairs),
        'rank_6_canonical_crt_pair_support':6,
        't6_refinement_horizon':horizon,
        't6_final_signature_classes':len(mids),
        't6_q3_to_q4_witness_phases':[str(mids[i]) for i in witness],
        'exact_additive_and_multiplicative_carry_cases':carry_checks,
        'posterior_interval_chain_horizon':40,
        'posterior_interval_state_count':len(lifted),
        'finite_horizon_state_counts':states_by_h,
        'locality_observer':'explicit ordered rank, not native X6 metric',
        'excluded_claims':['unique native selector','CRT uniformity preserved by rank-phase repair',
                           'native cell adjacency or equidistribution','new Polya or Farey theorem',
                           'state-free composition','independent review','Foundation admission']}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2]/'src')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args()
    result=run(args.source_root.resolve())
    data=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(data,encoding='utf-8')
    print(data,end='')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
