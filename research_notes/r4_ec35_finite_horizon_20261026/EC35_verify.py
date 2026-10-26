#!/usr/bin/env python3
"""EC35 exact positive-branch BRC finite-horizon observer certificate.

Reuses SHA-pinned EC33 source-transition engine and EC34 rational-rank routine.
This is an auxiliary ordered-source model, not a native Heartbeat computation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations, product
import hashlib
import importlib.util
import json
from pathlib import Path
from functools import lru_cache

UPSTREAM_FILES = {
    'EC33_VERIFY_UPSTREAM_PINNED.py': 'c2c5b183f88e7856c006f6b9ca954d603ac4e2cfd25d65a5558c67c91bc69856',
    'EC34_GITHUB_VERIFY_PINNED.py': '6dda5679426771152f3f09fa1327bf7c69dff3c03a9c50214f635532a9bf2862',
}
LABELS = ('R', 'B')


def load_pin(path: Path, name: str):
    assert hashlib.sha256(path.read_bytes()).hexdigest() == UPSTREAM_FILES[path.name], (path, 'source pin mismatch')
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def weight_from_q(ec33, H: int, q: int, word):
    """Execute existing EC33 BRC transition law from every declared residual state."""
    state_counts = {q: 1}
    for label in word:
        next_counts = {}
        for state, ways in state_counts.items():
            for target, source_multiplicity in ec33.transitions_v(H, state, label):
                next_counts[target] = next_counts.get(target, 0) + ways * source_multiplicity
        state_counts = next_counts
    return sum(state_counts.values())


def closed_weight(a: int, word) -> int:
    n = len(word)
    return 1 if n <= a else ((1 << (n-a)) if all(x == 'R' for x in word[a:]) else 0)


def expected_tv(a: int, b: int, n: int) -> Fraction:
    if a > b: a, b = b, a
    return Fraction(1) - Fraction(1, 1 << (min(n, b) - min(n, a)))


def exact_partition_min(m: int, d: int) -> int:
    """Independent exhaustive bitmask-cover certificate for m<=8.

    Each class has max(capacity)-min(capacity)<=d. Enumerate all legal class
    subsets and solve the exact least set partition by bitmask recursion.
    """
    assert 1 <= m <= 8 and 0 <= d <= m-1
    full = (1 << m) - 1
    @lru_cache(None)
    def solve(mask):
        if mask == full:
            return 0
        first = next(i for i in range(m) if not (mask >> i) & 1)
        avail = [i for i in range(first+1, m) if not (mask >> i) & 1]
        ans = m
        for choices in range(1 << len(avail)):
            group = [first] + [i for j,i in enumerate(avail) if (choices >> j) & 1]
            if max(group) - min(group) > d:
                continue
            addon = sum(1 << i for i in group)
            ans = min(ans, 1 + solve(mask | addon))
        return ans
    return solve(0)


def error_budget_d(m: int, eps: Fraction) -> int:
    assert 0 <= eps <= 1
    return max(d for d in range(m) if Fraction(1) - Fraction(1, 1 << d) <= eps)


def run(max_H: int, max_h: int, max_words: int):
    directory = Path(__file__).resolve().parent
    ec33 = load_pin(directory/'EC33_VERIFY_UPSTREAM_PINNED.py', 'ec33_unchanged')
    ec34 = load_pin(directory/'EC34_GITHUB_VERIFY_PINNED.py', 'ec34_unchanged')
    checks = dict(source_transition=0, exact_word_formula=0, total_mass=0,
                  truncated_rank=0, B_column_entry=0, exact_TV=0,
                  TV_horizon_bound=0, group_minimum=0, sharp_half_gap=0)
    rank_witnesses=[]
    for H in range(1, max_H+1):
        for q in range(H+1):
            for label in LABELS:
                edges = ec33.transitions_v(H, q, label)
                if q < H:
                    assert edges == ((q+1,1),)
                else:
                    assert edges == (((H,2),) if label=='R' else ())
                checks['source_transition'] += 1
        for horizon in range(max_h+1):
            # Exact state-conditioned word-count observer rows, restricted to B^k.
            # By the proof, all full-word rows collapse to the same m classes.
            K = []
            for a in range(H+1):
                row=[]
                for k in range(horizon+1):
                    v = weight_from_q(ec33, H, H-a, ('B',)*k)
                    assert v == int(k<=a)
                    row.append(v)
                    checks['B_column_entry'] += 1
                K.append(row)
            m = min(H+1,horizon+1)
            assert ec34.rank(K) == m
            checks['truncated_rank'] += 1
            if H in (1,4,8,max_H) and horizon in (0,1,2,min(H,max_h),max_h):
                rank_witnesses.append({'H':H,'horizon':horizon,'rank':m,'classes':m})
    # Check complete word histograms using the independent closed counting law.
    for H in range(1, min(9,max_H)+1):
        histograms={}
        for n in range(max_words+1):
            words=list(product(LABELS,repeat=n))
            for a in range(H+1):
                hist={}
                for word in words:
                    observed=weight_from_q(ec33,H,H-a,word)
                    assert observed == closed_weight(a,word)
                    checks['exact_word_formula'] += 1
                    hist[''.join(word)]=observed
                assert sum(hist.values()) == (1<<n)
                checks['total_mass'] += 1
                histograms[(a,n)] = hist
            for a,b in combinations(range(H+1),2):
                tv = ec33.total_variation(histograms[(a,n)],histograms[(b,n)])
                assert tv == expected_tv(a,b,n)
                checks['exact_TV'] += 1
                for horizon in (n,max_words):
                    if horizon >= n:
                        assert tv <= expected_tv(a,b,horizon)
                        checks['TV_horizon_bound'] += 1
                if n == a+1 and a<b:
                    assert tv == Fraction(1,2)
                    checks['sharp_half_gap'] += 1
    epsilons = [Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(2,3),
                Fraction(3,4),Fraction(7,8),Fraction(15,16),Fraction(1)]
    partition_cases=[]
    for m in range(1,9):
        for eps in epsilons:
            d=error_budget_d(m,eps)
            predicted=(m+d)//(d+1)
            exhaustive=exact_partition_min(m,d)
            assert exhaustive==predicted
            checks['group_minimum']+=1
            if m in (3,5,8):
                partition_cases.append({'capacities':m,'epsilon':str(eps),'d':d,'minimum_classes':predicted})
    return {
        'schema':'EM_R4_EC35_FINITE_HORIZON_OBSERVER_CERTIFICATE_V1',
        'status':'PASS',
        'source_pins_sha256':UPSTREAM_FILES,
        'source_commits':{'EC33':'0f84db42704c6e107adb9fd99d5e64cb77589e9d',
                          'EC34':'d90b896f9bdcd61c93d09dd7add5cdbee174b7fa'},
        'model':'EC33 V_H: ordered positive branch BRC; label alphabet R/B; R0,R1 distinct microscopic edges at saturation',
        'domain':{'H_range':[1,max_H],'observer_horizon_range':[0,max_h],
                  'full_word_depth_range':[0,max_words], 'TV_H_range':[1,min(9,max_H)]},
        'checks':checks, 'truncated_rank_witnesses':rank_witnesses,
        'group_partition_witnesses':partition_cases,
        'theorems':{
            'word_weight':'W_a(w)=1 if |w|<=a; else 2^(|w|-a) if suffix after a letters is all R, otherwise 0',
            'TV':'TV_n(a,b)=1-2^[-(min(n,b)-min(n,a))] for a<=b',
            'state_observer_rank':'rank O_(H,h)=min(H+1,h+1)',
            'finite_horizon_equivalence':'a~_h b iff min(a,h)=min(b,h)',
            'diameter_partition':'m=min(H+1,h+1); d=max{0<=j<m : 1-2^-j<=epsilon}; N=ceil(m/(d+1))',
            'half_gap':'epsilon<1/2 cannot merge two different exact horizon observer classes'},
        'scope':'Source-labelled auxiliary BRC only, not full microscopic provenance and not native P000/X6 heartbeat evolution',
        'native_owner_or_claim':'UNVERIFIED; CONTROL_QUOTA',
        'mathematical_acceptance':'AUTHOR_SIDE_ONLY',
        'universal_proofs':'algebraic and combinatorial proofs in EC35 paper, not inferred from finite checks'
    }


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--max-H',type=int,default=16)
    p.add_argument('--max-h',type=int,default=18)
    p.add_argument('--max-words',type=int,default=8)
    p.add_argument('--output',type=Path,default=Path(__file__).with_name('EC35_REPORT.json'))
    args=p.parse_args()
    assert args.max_H >= 1 and args.max_h >= 0 and 0 <= args.max_words <= 12
    output=run(args.max_H,args.max_h,args.max_words)
    args.output.write_text(json.dumps(output,sort_keys=True,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':output['status'],'checks':output['checks']},sort_keys=True))
