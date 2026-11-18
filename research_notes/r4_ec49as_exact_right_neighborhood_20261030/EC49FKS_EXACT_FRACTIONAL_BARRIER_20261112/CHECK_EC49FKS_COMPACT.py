#!/usr/bin/env python3
"""EC49FKS exact rational LP primal-dual verifier; Python 3 standard library only.
Reconstructs all admissible BRC words from the frozen EC49FGW generator.
No linear/integer optimizer and no floating-point proof operations are invoked.
"""
import collections
import json
import pathlib
import sys
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE.parent / 'EC49FJD_RELEASE_B11_COMPLETE_20261111' / 'EC49FGW_RADIUS5_SCREEN.py'
if not SOURCE.is_file():
    SOURCE = HERE / 'EC49FGW_RADIUS5_SCREEN.py'
assert SOURCE.is_file(), 'Frozen generator absent: ' + str(SOURCE)
sys.path.insert(0, str(SOURCE.parent))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key

BASE = {(2,1,1),(3,0,1),(3,1,1),(4,2,1)}
EXTRA = [
    ((5,4,1),(5,5,1)),
    ((5,4,1),(6,4,1)),
    ((6,3,1),(6,4,1)),
    ((6,3,1),(7,3,1))
]


def check(idx, rec):
    keys = BASE | set(EXTRA[idx])
    words = [(a,pref(w)) for a,w in all_words() if raw_key(w) in keys]
    labels = sorted({a for a,ps in words})
    nodes = sorted({p for a,ps in words for p in ps}, key=lambda p:(len(p),p))
    assert len(labels)==24 and len(nodes)==rec['nodes'] and len(words)==rec['words']
    ids = {p:j for j,p in enumerate(nodes)}
    parents = [ids.get(p[:-1],-1) for p in nodes]
    terminal = collections.defaultdict(set)
    for a,ps in words:
        terminal[a].add(ids[ps[-1]])
    all_term = set().union(*terminal.values())

    # Feasible primal: distribute terminal fractions; every ancestor takes max.
    x = [Fraction(0)] * len(nodes)
    seen = set()
    for item in rec['terminal_x']:
        j,s = item.split(':')
        j=int(j)
        v=Fraction(s)
        assert j in all_term and j not in seen and v>0
        seen.add(j)
        while j>=0:
            if x[j]<v:
                x[j]=v
            j=parents[j]
    assert all(par<0 or x[j]<=x[par] for j,par in enumerate(parents))
    assert all(sum(x[j] for j in terminal[a])>=1 for a in labels)
    primal = sum(x)

    # Feasible dual: demand weights and greedy bottom-up nonnegative edge flows.
    weights = [Fraction(s) for s in rec['weights']]
    assert len(weights)==24 and all(a>=0 for a in weights)
    charge = [Fraction(0)]*len(nodes)
    for a,weight in zip(labels,weights):
        for j in terminal[a]:
            charge[j] += weight
    children_flow = [Fraction(0)]*len(nodes)
    flow_edges=0
    for j in range(len(nodes)-1,-1,-1):
        excess = charge[j]+children_flow[j]-1
        if parents[j]>=0:
            f=max(Fraction(0),excess)
            children_flow[parents[j]] += f
            if f: flow_edges+=1
        else:
            assert excess<=0, (idx,'dual root constraint',j,excess)
    dual=sum(weights)
    assert primal==dual==Fraction(rec['objective']), (idx,primal,dual)
    return dict(index=idx,words=len(words),nodes=len(nodes),exact_lp_optimum=str(primal),
                integer_ceiling=(primal.numerator+primal.denominator-1)//primal.denominator,
                terminal_support=len(seen),dual_flow_edges=flow_edges)


def main():
    cert=json.loads((HERE/'EC49FKS_COMPACT_CERT.json').read_text(encoding='utf-8'))
    assert cert['schema']=='EC49FKS_COMPACT_RATIONAL_LP_DUAL_PRIMAL_V1'
    assert cert['frozen_science_pin']==PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
    for idx in range(4):
        print('CERTIFIED',check(idx,cert['certificates'][str(idx)]),flush=True)
    print('EC49FKS_ALL_FOUR_RATIONAL_LP_OPTIMA_PASS')


if __name__=='__main__':
    main()
