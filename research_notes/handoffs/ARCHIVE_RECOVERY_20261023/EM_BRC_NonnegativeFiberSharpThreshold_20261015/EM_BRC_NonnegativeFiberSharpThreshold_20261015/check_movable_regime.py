"""Exact all movable representatives at p=5,r<=2 and p=7,r<=1.
Does not enumerate all possible non-movable states (except separately at p=5,N=6).
"""
from verify_threshold import model
from itertools import combinations_with_replacement
from collections import defaultdict
from math import comb
import json
from pathlib import Path
out=[]
for p,max_r in [(5,2),(7,1)]:
    X,ports,K,Y,B=model(p)
    n=len(X)
    point_to_ports=[[j for j,(_,_,L) in enumerate(ports) if x in L] for x in range(n)]
    for r in range(max_r+1):
        labels={};seen_states=set();counter=0
        for direction in range(p+1):
            lines=[tuple(sorted(L)) for d,t,L in ports if d==direction]
            for H in combinations_with_replacement(range(n),r):
                key=(direction,H)
                fingerprints=set()
                for L in lines:
                    state=tuple(sorted(L+H))
                    assert state not in seen_states
                    seen_states.add(state)
                    sums=[0]*n
                    for x in state:
                        for j in point_to_ports[x]:sums[j]+=1
                    sig=bytes(v%p for v in sums)
                    fingerprints.add(sig)
                    assert sig not in labels or labels[sig]==key,('collision',p,r,labels[sig],key)
                    labels[sig]=key
                    counter+=1
                assert len(fingerprints)==1,(p,r,key,len(fingerprints))
        expected=(p+1)*comb(n+r-1,r)
        assert len(labels)==expected and counter==expected*(p-1)
        out.append({'p':p,'N':p+r,'r':r,'movable_components_exact':expected,
                    'movable_states_exact':counter,'different_components_sharing_residue':0,
                    'all_parallel_line_moves_preserve_residue':True})
print(json.dumps(out,indent=2))
Path('/mnt/data/EM_BRC_NonnegativeFiberSharpThreshold_20261015/movable_regime_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
