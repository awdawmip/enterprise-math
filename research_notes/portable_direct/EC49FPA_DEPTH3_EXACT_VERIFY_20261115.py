#!/usr/bin/env python3
"""Complete finite verifier for EC49FPA; run beside EC49FOZ_evidence/.

The frozen original BRC data and EC49FOZ_verify.py are kept unchanged in the
prior immutable evidence archive. No floating point is used.
"""
from pathlib import Path
from collections import defaultdict, Counter
from functools import lru_cache
import csv, itertools, json, os, sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'EC49FOZ_evidence'))
os.chdir(HERE/'EC49FOZ_evidence')
import EC49FOZ_verify as origin

def prior_weights(rep):
    g=defaultdict(dict)
    with (Path('SOURCE')/f'CLASS_{rep}_PROFILES.csv').open(newline='') as fh:
        for r in csv.DictReader(fh):
            c=int(r['config']); k=(int(r['root']),int(r['subset']))
            g[c][k]=int(r['cost'])
    seq=[tuple(sorted(g[c].items())) for c in sorted(g)]
    multiplicities=Counter(seq)
    profiles=list(dict.fromkeys(seq))
    weights=[multiplicities[p] for p in profiles]
    assert len(weights)==40 and sum(weights)==75
    assert sorted(Counter(weights).items())==[(1,38),(2,1),(35,1)]
    return weights

def verify_one(X, weights):
    n=len(X); q=len(X[0]); assert (n,q)==(40,432)
    full=tuple(range(n))
    # Independent unordered-pair encoding for 780 indistinguishable pairs.
    pairs=list(itertools.combinations(full,2))
    collisions=[sum(1<<j for j,(i,k) in enumerate(pairs) if X[i][a]==X[k][a]) for a in range(q)]
    def partition(ids,a):
        groups=defaultdict(list)
        for i in ids: groups[X[i][a]].append(i)
        return {v:tuple(m) for v,m in groups.items()}
    @lru_cache(None)
    def can_finish(ids):
        if len(ids)<2:return True
        members=set(ids)
        relevant=sum(1<<j for j,(i,k) in enumerate(pairs) if i in members and k in members)
        return any(relevant&col==0 for col in collisions)
    @lru_cache(None)
    def best_second(ids):
        if len(ids)<2:return (0,0)
        opts=[]
        for b in range(q):
            parts=partition(ids,b)
            if any(not can_finish(G) for G in parts.values()): continue
            cost=sum(weights[i] for G in parts.values() if len(G)>1 for i in G)
            opts.append((cost,b))
        return min(opts) if opts else None
    table=[]; witnesses=[]
    for a in range(q):
        root=partition(full,a)
        bad=next(((cost,F) for cost,F in root.items() if len(F)>1 and best_second(F) is None), None)
        if bad:
            witnesses.append((a,bad[0],bad[1]))
            continue
        d2=sum(weights[i] for F in root.values() if len(F)>1 for i in F)
        d3=sum(best_second(F)[0] for F in root.values() if len(F)>1)
        table.append((sum(weights)+d2+d3,a,d2,d3,len(root)))
    assert len(table)==3 and len(witnesses)==429
    return sorted(table),witnesses

def main():
    keys,cases=origin.load()  # SHA256 and original domain checked here.
    result={}
    for rep in (14304,14309):
        X=origin.costs(rep,keys,cases)
        w=prior_weights(rep)
        profile,blocked=verify_one(X,[1]*40)
        configuration,blocked_w=verify_one(X,w)
        assert [(r[1]) for r in profile]==[(r[1]) for r in configuration]
        assert blocked==blocked_w
        assert [r[0] for r in profile]==[73,76,78]
        assert [r[0] for r in configuration]==[177,181,183]
        result[str(rep)]={'uniform_profiles':profile,'uniform_configurations':configuration,
                          'multiplicity_histogram':dict(Counter(w)),
                          'excluded_first_actions':429}
        print('VERIFIED',rep,result[str(rep)],flush=True)
        with (HERE/f'EC49FPA_{rep}_OBSTRUCTION_WITNESSES.tsv').open('w') as f:
            f.write('first_action\tfirst_value\tprofile_indices\n')
            for a,v,F in blocked:f.write(f'{a}\t{v}\t{",".join(map(str,F))}\n')
    (HERE/'EC49FPA_DEPTH3_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print('EC49FPA_EXACT_EXPECTATION_MINIMA_VERIFIED')
if __name__=='__main__':main()
