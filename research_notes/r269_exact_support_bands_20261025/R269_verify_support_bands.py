#!/usr/bin/env python3
"""R269 exact BRC support-band checker, reusing unmodified R268 transition law.

Dependency: canonical predecessor script ../r268_six_output_support_20261025/
R268_six_output_support.py in the EM source tree, or bundled predecessor/
R268_six_output_support.py in the portable package.
Exact integer arithmetic, no native-X6 claim.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from itertools import product
import json

HERE = Path(__file__).resolve().parent
CANDIDATES = (
    HERE.parent / 'r268_six_output_support_20261025' / 'R268_six_output_support.py',
    HERE / 'predecessor' / 'R268_six_output_support.py',
)
SOURCE = next((p for p in CANDIDATES if p.is_file()), None)
if SOURCE is None:
    raise FileNotFoundError('Unmodified R268_six_output_support.py missing; see predecessor pinned commit')
spec = spec_from_file_location('r268_exact', SOURCE)
r268 = module_from_spec(spec)
spec.loader.exec_module(r268)
STATES = ((0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2))
# Each support at n>=10 and each epsilon is the parity-n integer interval
# [ -n + a, n + b ], where (a,b) are the following constants.
OFFSETS = {
    (0,0):(2,-8),
    (0,2):(4,-4),
    (1,1):(2,-6),
    (1,2):(4,-4),
    (2,0):(0,-6),
    (2,1):(8,-4),
    (2,2):(2,-6),
}

def interval(n, offset):
    a,b=offset
    return set(range(-n+a,n+b+1,2))

def paths_base(n=10):
    c=Counter()
    for bits in product('01',repeat=n):
        c[r268.evaluate(bits)]+=1
    return c

def assert_bands(n,counts):
    assert sum(counts.values())==2**n, ('total',n)
    by_state=defaultdict(set)
    for (q,r,e,k),w in counts.items():
        assert w>0
        assert (q,r) in OFFSETS, ('unexpected control',n,q,r)
        by_state[(q,r,e)].add(k)
    for state in STATES:
        expected=interval(n, OFFSETS[state])
        for eps in (+1,-1):
            assert by_state[(state[0],state[1],eps)]==expected, (n,state,eps,
                sorted(by_state[(state[0],state[1],eps)]),sorted(expected))
    by_effect=defaultdict(set); by_output=defaultdict(set)
    for (q,r,e,k),w in counts.items():
        if w:
            by_effect[e,k].add((q,r))
            by_output[e,k].add((q,int(r==2)))
    return {
        'effect_support':len(by_effect),
        'all_seven_internal_effects':sum(len(x)==7 for x in by_effect.values()),
        'all_six_terminal_effects':sum(len(x)==6 for x in by_output.values()),
        'six_without_seven':sum(len(by_output[g])==6 and len(by_effect[g])<7 for g in by_effect),
    }

def check_symbolic_induction():
    # SOURCE edge/transitions reused verbatim from R268. For each source interval
    # I_n[-n+a,n+b], translate it under one edge into a target interval at n+1;
    # prove each union is contiguous at n=10, where every constituent interval
    # has its minimum width. Every constituent expands outward as n increases,
    # so adjacent/overlapping intervals stay so for all n>=10.
    transformed=defaultdict(list)
    for (q,r),(a,b) in OFFSETS.items():
        for choice in (0,1):
            nq, eta, beta=r268.EDGES[q][choice]
            nr=r268.DELTA[r][choice]
            if eta==1:
                na,nb=a+beta+1,b+beta-1
            else:
                na,nb=-b+beta+1,-a+beta-1
            transformed[(nq,nr)].append(((q,r),choice,(na,nb)))
    assert set(transformed)==set(STATES)
    table={}
    for dest in STATES:
        incoming=transformed[dest]
        assert min(a for _,_,(a,b) in incoming)==OFFSETS[dest][0]
        assert max(b for _,_,(a,b) in incoming)==OFFSETS[dest][1]
        actual=set()
        for _,_,off in incoming:actual.update(interval(11,off))
        expected=interval(11,OFFSETS[dest])
        assert actual==expected,('gap or wrong endpoint',dest)
        table[f'{dest[0]},{dest[1]}']=[{'source':list(src),'choice':choice,'a':a,'b':b}
            for src,choice,(a,b) in incoming]
    return table

def main():
    base=paths_base(10)
    base_stats=assert_bands(10,base)
    induction=check_symbolic_induction()
    # Independent of induction, replay positive path counts through depth 80
    # using the exact R268 forward() interface. Finite replay sanity checks
    # are NOT the proof for the unbounded n assertion.
    p=Counter({(0,0,1,0):1})
    snapshots={}
    for m in range(81):
        if m>=10:
            res=assert_bands(m,p)
            assert res=={
                'effect_support':2*m-2,
                'all_seven_internal_effects':2*m-14,
                'all_six_terminal_effects':2*m-10,
                'six_without_seven':4,
            },(m,res)
            if m in (10,11,12,18,32,64,80): snapshots[str(m)]=res
        if m==10: assert p==base, 'full word enumeration differs from recurrence'
        if m<80:p=r268.forward(p)
    b10={f'{q},{r}':{'plus':sorted(k for qq,rr,e,k in base if (qq,rr,e)==(q,r,+1)),
                        'minus':sorted(k for qq,rr,e,k in base if (qq,rr,e)==(q,r,-1))}
         for q,r in STATES}
    output={
        'schema':'EM_R269_EXACT_AFFINE_SUPPORT_BANDS_V1',
        'status':'PASS',
        'predecessor_path':str(SOURCE),
        'model':'R268 formal positive BRC, same 7 (q,r), six terminal (q,h), authentic (epsilon,k)',
        'base_n':10,
        'base_words_enumerated':1024,
        'base_counts_equal_R268_forward':True,
        'seven_states':list(map(list,STATES)),
        'offsets_minus_n_plus_a_to_n_plus_b':{f'{q},{r}':[a,b] for (q,r),(a,b) in OFFSETS.items()},
        'symbolic_induction_image_offsets':induction,
        'replay_verified_through_n':80,
        'snapshots':snapshots,
        'theorem_formulas_n_ge_10':{
          'all_effect_support':'2*n-2','seven_internal_saturated':'2*n-14',
          'six_terminal_saturated':'2*n-10',
          'six_output_not_seven_internal':'4',
          'seven_effect_intersection_both_signs':'8-n<=k<=n-8, k=n mod 2',
          'six_effect_intersection_both_signs':'4-n<=k<=n-8, k=n mod 2'},
        'logic':'exact base plus symbolic interval-union induction; finite replay independent check only',
        'not_proven':['six-state aggregate affine BRC exists or is impossible',
          'original Enterprise Math native BRC executes this formal update',
          'R193 provenance/time-port correspondence',
          'formal claim or independent Driver acceptance'],
    }
    print(json.dumps(output,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
