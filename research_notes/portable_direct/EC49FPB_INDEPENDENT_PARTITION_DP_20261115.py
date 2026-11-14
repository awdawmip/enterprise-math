#!/usr/bin/env python3
"""EC49FPB. Independently verify unrestricted-depth optimality by exact
tuple-fiber partition recursion, not the bitmask recurrence. Requires the
original frozen EC49FOZ archive and EC49FPA_CONFIG_WEIGHTED_3.py alongside
this file in the same evidence folder. Python 3.10+; integer arithmetic only.
"""
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'EC49FOZ_evidence'))
sys.path.insert(0,str(ROOT))
os.chdir(ROOT/'EC49FOZ_evidence')
import EC49FOZ_verify as origin
from EC49FPA_CONFIG_WEIGHTED_3 import weights_for

def independent_optimal(X, weights):
    n=len(X); q=len(X[0]); universe=tuple(range(n))
    @lru_cache(None)
    def solve(F):
        if len(F)==1: return 0
        W=sum(weights[i] for i in F)
        partitions=set()
        for a in range(q):
            cells=defaultdict(list)
            for i in F: cells[X[i][a]].append(i)
            block=tuple(sorted(tuple(group) for group in cells.values()))
            if len(block)==1: continue
            partitions.add(block)
        assert partitions, 'distinct profiles cannot be separated'
        best=None
        for partition in partitions:
            candidate=W+sum(solve(group) for group in partition if len(group)>1)
            if best is None or candidate<best: best=candidate
            if best==W: break
        return best
    minimum=solve(universe)
    first=[]
    for a in range(q):
        cells=defaultdict(list)
        for i in universe: cells[X[i][a]].append(i)
        p=[tuple(v) for v in cells.values()]
        if len(p)==1: continue
        s=sum(weights)+sum(solve(group) for group in p if len(group)>1)
        if s==minimum: first.append(a)
    return {'minimum':minimum, 'optimal_first_queries':first,
            'memo_states':solve.cache_info().currsize}

if __name__=='__main__':
    keys,cases=origin.load() # SHA-256 checks enforced by frozen input loader.
    result={}
    for rep in (14304,14309):
        X=origin.costs(rep,keys,cases)
        result[str(rep)]={}
        for name,weights in [('profiles',[1]*40),
                             ('configurations',weights_for(rep))]:
            t=independent_optimal(X,weights)
            expect=(73,[78,99,177]) if (rep,name)==(14304,'profiles') else \
                   (73,[119,153,191]) if name=='profiles' else \
                   (177,[78]) if rep==14304 else (177,[119])
            assert (t['minimum'],t['optimal_first_queries'])==expect
            result[str(rep)][name]=t
            print('INDEPENDENT_VERIFIED',rep,name,t,flush=True)
    (ROOT/'EC49FPB_INDEPENDENT_PARTITION_DP_RESULT.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('EC49FPB_UNRESTRICTED_GLOBAL_OPTIMALITY_INDEPENDENT_PASS')
