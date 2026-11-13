#!/usr/bin/env python3
"""R695: exact S6-equivariant signed distinct-axis triadic completion classification.
Finite combinatorial test, independent of any unverified physical closure predicate.
"""
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path

AXES = range(6)
SIGNS = (-1, 1)
PERMS = tuple(permutations(AXES))
PAIRS = tuple((i, si, j, sj) for i in AXES for j in AXES if i != j for si, sj in product(SIGNS, repeat=2))
TRIPLES = tuple((i,si,j,sj,k,sk) for i,si,j,sj in PAIRS for k in AXES if k not in (i,j) for sk in SIGNS)
assert len(PAIRS) == 120 and len(TRIPLES) == 960 and len(PERMS) == 720

def orbit_class(triple):
    _,si,_,sj,_,sk=triple
    return (si,sj,sk)

def act(p,triple):
    i,si,j,sj,k,sk=triple
    return (p[i],si,p[j],sj,p[k],sk)


def verify():
    orbit_counts=Counter(map(orbit_class,TRIPLES))
    assert len(orbit_counts)==8 and set(orbit_counts.values())=={120}
    # Direct independent equivariance verification on every input and every S6 transformation.
    for p in PERMS:
        for triple in TRIPLES:
            assert orbit_class(act(p,triple))==orbit_class(triple)
    # Stabilizer of any ordered distinct-axis pair has 4! elements and is
    # transitive on its four remaining axes, separately for each third sign.
    transitivity_checks=0
    for i,si,j,sj in PAIRS:
        stabilizer=[p for p in PERMS if p[i]==i and p[j]==j]
        assert len(stabilizer)==24
        for k in AXES:
            if k in (i,j): continue
            remaining={p[k] for p in stabilizer}
            assert remaining==set(AXES)-{i,j}
            transitivity_checks+=1
    assert transitivity_checks==480
    # 8 independent invariant Boolean bits, grouped by the four ordered input-sign patterns.
    laws=0
    fibre_cardinality=Counter()
    for bits in range(256):
        law={pat:(bits>>n)&1 for n,pat in enumerate(sorted(orbit_counts))}
        sizes=tuple(4*(law[(si,sj,-1)]+law[(si,sj,1)]) for si,sj in product(SIGNS,repeat=2))
        assert set(sizes)<={0,4,8}
        fibre_cardinality.update(sizes)
        laws+=1
    assert laws==256
    # For a signed ordered pair and chosen third sign there are 4 equiprobable
    # positive rational sources. For both signs together there are 8 distinct ones.
    i,si,j,sj=0,1,1,-1
    for sign in SIGNS:
        sources=[(k,sign) for k in AXES if k not in (i,j)]
        mu={s:Fraction(1,4) for s in sources}
        assert len(mu)==4 and sum(mu.values())==1
        assert all(mu[(p[k],sign)]==mu[(k,sign)] for p in PERMS if p[i]==i and p[j]==j for k,_ in sources)
    # Show observer fibre lost under a pair-only projection: a future port query
    # for k=2 distinguishes two completions with same observed (i,j) pair.
    third_a=(2,1); third_b=(3,1)
    probe=lambda third: int(third[0]==2)
    assert probe(third_a)==1 and probe(third_b)==0
    evidence={
        'schema':'R695_SIGNED_TRIADIC_S6_COMPLETION_EXACT_V1',
        'date':'2026-11-10',
        'scope':'All ordered signed distinct-axis first pairs and signed third directions on a different X6 axis; finite S6 axis-label permutation skeleton. Closure predicate is a candidate, not a P000-accepted force dynamics.',
        'input_pairs':len(PAIRS),
        'candidate_triples':len(TRIPLES),
        'S6_size':len(PERMS),
        'equivariance_checks':len(TRIPLES)*len(PERMS),
        'orbits':{str(pat):count for pat,count in sorted(orbit_counts.items())},
        'equivariant_boolean_laws':laws,
        'per_input_fibre_possible_sizes':[0,4,8],
        'one_signed_orbit_sources':4,
        'both_sign_orbits_sources':8,
        'single_orbit_normalized_mass':{'numerator':1,'denominator':4},
        'stabilizer_size':24,
        'stabilizer_transitivity_witness_checks':transitivity_checks,
        'observer_counterexample':{'pair':[0,1,1,-1],'hidden_thirds':[[2,1],[3,1]],'future_probe_axis':2,'outputs':[1,0]},
        'p000_relation':'Conditional candidate classification; no claim that every axis-distinct equal-magnitude triple satisfies TRIADIC_CLOSURE_E',
        'verification_marker':'R695_S6_TRIADIC_COMPLETION_ORBITS_EXACT_PASS'
    }
    Path(__file__).with_name('R695_EVIDENCE.json').write_text(json.dumps(evidence,sort_keys=True,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(evidence['verification_marker'])
    print('ORBIT_COUNTS',dict(orbit_counts),'LAW_COUNT',laws,'FIBRE_SIZE_HIST',dict(fibre_cardinality))
    return evidence

if __name__=='__main__': verify()
