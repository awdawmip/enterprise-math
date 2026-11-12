#!/usr/bin/env python3
"""Independent exact directed-edge graph enumerator for R749SF hidden-sign transport."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json

PORTS=[(i,s) for i in range(6) for s in (-1,1)]
V=[frozenset(v) for v in combinations(PORTS,2) if v[0][0]!=v[1][0]]
def support(v):return frozenset(a for a,s in v)
def adj(u,v):return len(u&v)==1 and len(support(u)|support(v))==3
neighbors={v:[w for w in V if adj(v,w)] for v in V}
D=[(u,v) for u in V for v in neighbors[u]]
assert len(V)==60 and len(D)==960 and all(len(neighbors[v])==16 for v in V)
L=defaultdict(list)
for u,v in D:L[(support(u),support(v))].append((u,v))
assert len(L)==120 and all(len(z)==8 for z in L.values())

def complement(u,v):return u^v
def forced_support(A,B):return A^B
def signmap(edge):
    u,v=edge
    return {a:s for a,s in u|v}

def conditional_next(edge,C,p):
    u,v=edge
    q=(1+15*p)/16
    r=(1-p)/16
    f=complement(u,v)
    target=[w for w in neighbors[v] if support(w)==C]
    assert len(target)==2
    norm=q+r if C==support(f) else 2*r
    assert norm>0
    return {(v,w):(q if w==f else r)/norm for w in target}

def iter_forced(start,p):
    A,B=map(support,start)
    dist={start:Fraction(1)}
    for _ in range(3):
        C=forced_support(A,B)
        nxt=defaultdict(Fraction)
        for e,prob in dist.items():
            for f,pf in conditional_next(e,C,p).items():nxt[f]+=prob*pf
        A,B=B,C
        dist=dict(nxt)
    return dist

checks=0
reset=0
for p in [Fraction(0),Fraction(1,2),Fraction(1)]:
    a=(1+7*p)/8
    theta=8*p/(1+7*p)
    assert theta==(p/a)
    for (A,B),initials in L.items():
        C=forced_support(A,B)
        for ini in initials:
            dist=iter_forced(ini,p)
            assert set(dist).issubset(set(initials)) and sum(dist.values())==1
            x=signmap(ini)
            for out in initials:
                y=signmap(out)
                expect=Fraction(1)
                for axis in x:
                    expect*=((1+theta)/2 if x[axis]==y[axis] else (1-theta)/2)
                assert dist.get(out,0)==expect,(p,A,B,ini,out)
                checks+=1
            if p<1:
                for other in [v for v in (frozenset(x) for x in combinations(range(6),2)) if len(v&B)==1 and v!=C]:
                    z=conditional_next(ini,other,p)
                    assert len(z)==2 and set(z.values())=={Fraction(1,2)}
                    xsign=signmap(ini)
                    for final in z:
                        fsign=signmap(final)
                        assert all(fsign[t]==xsign[t] for t in B)
                    reset+=1
print(json.dumps({'status':'PASS','signed_vertices':len(V),'directed_signed_edges':len(D),'unsigned_directed_edges':len(L),'signed_lifts_per_unsigned_edge':8,'parameter_values':['0','1/2','1'],'conditional_three_cycle_matrix_entries_checked':checks,'unforced_reset_rows_checked':reset,'theta_at_p_half':'8/9','three_cycle_eigenvalues_at_p_half':{'1':1,'8/9':3,'64/81':3,'512/729':1},'native_event_permission':False},indent=2))
