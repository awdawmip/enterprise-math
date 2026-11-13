#!/usr/bin/env python3
"""R749SC: exact MAP reconstruction of complete signed-Port paths from unsigned blocks."""
from itertools import combinations
from fractions import Fraction
from collections import Counter
import json

ports=[(i,s) for i in range(6) for s in (-1,1)]
V=[frozenset((a,b)) for a,b in combinations(ports,2) if a[0]!=b[0]]
U=[frozenset(x) for x in combinations(range(6),2)]
vi={x:i for i,x in enumerate(V)}
ui={x:i for i,x in enumerate(U)}
proj=lambda x:ui[frozenset(i for i,_ in V[x])]
adj=lambda a,b:len(a&b)==1 and len({i for i,_ in a|b})==3
N=[[j for j,w in enumerate(V) if adj(v,w)] for v in V]
NU=[[j for j,w in enumerate(U) if len(v&w)==1] for v in U]
D=[(u,v) for u in range(60) for v in N[u]]
DU=[(u,v) for u in range(15) for v in NU[u]]
assert len(D)==960 and len(DU)==120
f=lambda u,v:vi[V[u]^V[v]]
fu=lambda u,v:ui[U[u]^U[v]]
lifts={}
for u,v in D:lifts.setdefault((proj(u),proj(v)),[]).append((u,v))
assert all(len(x)==8 for x in lifts.values())
hist=Counter()
for u,v in DU:
    for w in NU[v]:
        for z in NU[w]:
            k=int(w==fu(u,v))+int(z==fu(v,w))
            hist[k]+=1
assert hist=={0:5880,1:1680,2:120}
summary={}
for p in (Fraction(0),Fraction(1,2),Fraction(1)):
    q=(1+15*p)/16
    r=(1-p)/16
    a=(1+7*p)/8
    b=(1-p)/8
    optimal=Fraction(0)
    positive=0
    for u,v in DU:
        for w in NU[v]:
            for z in NU[w]:
                k=int(w==fu(u,v))+int(z==fu(v,w))
                weights=[]
                for i,j in lifts[(u,v)]:
                    for h in N[j]:
                        if proj(h)!=w:continue
                        for l in N[h]:
                            if proj(l)!=z:continue
                            ns=int(h==f(i,j))+int(l==f(j,h))
                            weights.append(Fraction(1,960)*q**ns*r**(2-ns))
                assert len(weights)==32
                unsigned_mass=Fraction(1,120)*a**k*b**(2-k)
                assert sum(weights)==unsigned_mass
                if unsigned_mass:
                    positive+=1
                    conditional_MAP=Fraction(1,8)*(q/(q+r))**k*Fraction(1,2)**(2-k)
                    assert max(weights)/unsigned_mass==conditional_MAP
                optimal+=max(weights)
    assert optimal==Fraction(1,8)*((1+p)/2)**2
    summary[str(p)]={"MAP_success_n4":str(optimal),"positive_unsigned_blocks":positive}
print(json.dumps({"schema":"EM_R749SC_EXACT_MAP_HIDDEN_SOURCE_V1",
                  "status":"PASS","unsigned_blocks_checked":7680,
                  "signed_path_lifts_checked_per_parameter":245760,
                  "histogram_K":{str(k):n for k,n in sorted(hist.items())},
                  "exact_results":summary,
                  "native_event_permission":False},sort_keys=True,indent=2))
