#!/usr/bin/env python3
"""R749SB finite exact verifier: 8:1 quotient hidden-source posterior and parameter information."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb
import json

ports=[(i,s) for i in range(6) for s in (-1,1)]
V=[frozenset((x,y)) for x,y in combinations(ports,2) if x[0]!=y[0]]
idx={v:i for i,v in enumerate(V)}
U=[frozenset(x) for x in combinations(range(6),2)]
uidx={u:i for i,u in enumerate(U)}
proj=lambda x:uidx[frozenset(i for i,_ in V[x])]
adj=lambda a,b:len(a&b)==1 and len({i for i,_ in a|b})==3
N=[[j for j,w in enumerate(V) if adj(v,w)] for v in V]
NU=[[j for j,y in enumerate(U) if len(x&y)==1] for x in U]
D=[(u,v) for u in range(len(V)) for v in N[u]]
DU=[(a,b) for a in range(len(U)) for b in NU[a]]
f=lambda u,v:idx[V[u]^V[v]]
fu=lambda a,b:uidx[U[a]^U[b]]
lifts={}
for u,v in D:lifts.setdefault((proj(u),proj(v)),[]).append((u,v))
assert (len(V),len(D),len(U),len(DU))==(60,960,15,120)
assert all(len(x)==16 for x in N) and all(len(x)==8 for x in NU)
assert len(lifts)==120 and all(len(x)==8 for x in lifts.values())

hist_K=Counter()
hist_KJ=Counter()
checked_unsigned=0
checked_signed=0
for a,b in DU:
    for c in NU[b]:
        for d in NU[c]:
            k=int(c==fu(a,b))+int(d==fu(b,c))
            hist_K[k]+=1
            counts=Counter()
            for u,v in lifts[(a,b)]:
                for w in N[v]:
                    if proj(w)!=c:continue
                    for z in N[w]:
                        if proj(z)!=d:continue
                        j=int(w==f(u,v))+int(z==f(v,w))
                        counts[j]+=1
            for j in range(k+1):
                assert counts[j]==8*2**(2-k)*comb(k,j),(a,b,c,d,k,j,counts)
            assert set(counts)==set(range(k+1))
            assert sum(counts.values())==32
            for p in (Fraction(0),Fraction(1,2),Fraction(1)):
                q=(1+15*p)/16
                r=(1-p)/16
                au=(1+7*p)/8
                bu=(1-p)/8
                signed_weight=sum(Fraction(counts[j],960)*q**j*r**(2-j) for j in counts)
                unsigned_weight=Fraction(1,120)*au**k*bu**(2-k)
                assert signed_weight==unsigned_weight,(p,k,signed_weight,unsigned_weight)
            for j,cnt in counts.items():hist_KJ[(k,j)]+=cnt
            checked_unsigned+=1
            checked_signed+=sum(counts.values())
assert hist_K=={0:5880,1:1680,2:120}
assert hist_KJ=={(0,0):188160,(1,0):26880,(1,1):26880,(2,0):960,(2,1):1920,(2,2):960}
assert checked_unsigned==7680 and checked_signed==245760
p=Fraction(1,2)
I_signed=Fraction(15,1)/((1+15*p)*(1-p))
I_unsigned=Fraction(7,1)/((1+7*p)*(1-p))
I_hidden=Fraction(8,1)/((1+15*p)*(1+7*p)*(1-p))
assert (I_signed,I_unsigned,I_hidden)==(Fraction(60,17),Fraction(28,9),Fraction(64,153))
assert I_signed-I_unsigned==I_hidden
assert I_unsigned/I_signed==Fraction(119,135)
result={
 "schema":"EM_R749SB_HIDDEN_SOURCE_INFORMATION_V1",
 "status":"PASS",
 "signed_vertices":60,
 "signed_directed_edges":960,
 "unsigned_vertices":15,
 "unsigned_directed_edges":120,
 "unsigned_four_vertex_blocks_checked":checked_unsigned,
 "signed_four_vertex_lifts_checked":checked_signed,
 "exact_probability_parameters":["0","1/2","1"],
 "histogram_K":{str(k):n for k,n in sorted(hist_K.items())},
 "histogram_K_J":{f"{k},{j}":n for (k,j),n in sorted(hist_KJ.items())},
 "fisher_signed_at_p_half":str(I_signed),
 "fisher_unsigned_at_p_half":str(I_unsigned),
 "fisher_hidden_at_p_half":str(I_hidden),
 "fisher_unsigned_fraction":str(I_unsigned/I_signed),
 "native_cell_link_port_license":False,
 "formal_claim":False
}
print(json.dumps(result,sort_keys=True,indent=2))
