#!/usr/bin/env python3
"""Unit185: independent integer enumeration of sharp streaming relative-fiber rank update."""
from collections import Counter
import json, hashlib
N=6
V=tuple(tuple(s if k==i else 0 for k in range(N)) for i in range(N) for s in (1,-1))
ZERO=(0,)*N

def canonical(z):
    m=min(z)
    return tuple(x-m for x in z), m

def depths(a,M):
    if (M-sum(a))%2:return ()
    return tuple(h for h in range(-M-max(a),M+1) if sum(abs(x+h) for x in a)<=M)

def main():
    reachable={ZERO}
    cases=0
    rank_cases=0
    patterns=Counter()
    witnesses={}
    per_horizon=[]
    for M in range(10):
        states={canonical(z)[0] for z in reachable}
        here=Counter()
        for a in states:
            old=depths(a,M)
            if not old:raise RuntimeError('empty current fiber')
            for v in V:
                b,c=canonical(tuple(a[i]+v[i] for i in range(N)))
                new=depths(b,M+1)
                if not new:raise RuntimeError('empty next fiber')
                if any(h+c not in new for h in old):
                    raise RuntimeError('old fiber not included after one edge')
                left=old[0]+c-new[0]
                right=new[-1]-old[-1]-c
                if left not in (0,1) or right not in (0,1):
                    raise RuntimeError(f'margin exceeds one M={M} a={a} v={v} shift=({left},{right})')
                if len(new)!=len(old)+left+right:
                    raise RuntimeError('cardinality/rank interval mismatch')
                for j,h in enumerate(old):
                    if (h+c)-new[0]!=j+left:
                        raise RuntimeError('rank update error')
                    rank_cases+=1
                patterns[(left,right)]+=1
                here[(left,right)]+=1
                if (left,right) not in witnesses:
                    witnesses[(left,right)]={'M':M,'a':list(a),'v':list(v),'next_a':list(b),'carry':c,'old_depths':list(old),'new_depths':list(new)}
                cases+=1
        per_horizon.append({'M':M,'relative_states':len(states),'transitions_checked':sum(here.values()), 'margins':{str(k):v for k,v in sorted(here.items())}})
        reachable={tuple(z[i]+v[i] for i in range(N)) for z in reachable for v in V}
    out={'schema':'X6_UNIT185_STREAM_RANK_EXACT_CHECK_V1','source':'independent signed X6 integer graph',
         'M_tested':'0..9','transition_cases':cases,'rank_cases':rank_cases,'violations':0,
         'margin_counts':{str(k):v for k,v in sorted(patterns.items())},
         'witnesses':{str(k):v for k,v in sorted(witnesses.items())},
         'by_horizon':per_horizon,'status':'FINITE_DIAGNOSTIC_NOT_GLOBAL_PROOF'}
    fn='/mnt/data/x6_unit185_stream_rank_results.json'
    with open(fn,'w',encoding='utf8') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps({'cases':cases,'rank_cases':rank_cases,'margins':out['margin_counts'],
     'sha256':hashlib.sha256(open(fn,'rb').read()).hexdigest()},indent=2))
if __name__=='__main__':main()
