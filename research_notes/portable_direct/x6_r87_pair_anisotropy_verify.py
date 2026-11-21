#!/usr/bin/env python3
"""Exact certificate for R87 six paired-precision rays of the conditional BRC observer."""
from fractions import Fraction
from itertools import combinations
import json

S=[(6,-4,1),(9,-5,1),(10,-5,1),(15,-6,1),(24,-14,3),(36,-16,3),(39,-20,4),(45,-21,4),(114,-56,11)]
PAIRS=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
ADJ={(1,2):([10,27],[39,43]),(1,4):([27,49],[16,39]),(2,3):([16,39],[27,49]),(3,4):([39,43],[10,27])}
Q=[max(sum(max(c,0) for c in a),sum(max(-c,0) for c in a)) for a in S]
assert Q==[7,10,11,16,27,39,43,49,125]
G=[]
for x,y,z in S:
    Z=[0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z]
    G.append({(i+1,j+1):abs(Z[i]-Z[j])//2 for i,j in combinations(range(4),2)})
def groups(pair,g):
    h=g[pair]
    lo=g[tuple(k for k in (1,2,3,4) if k not in pair)]
    m=max(v for ij,v in g.items() if len(set(ij)&set(pair))==1)
    return (h,m,lo)
def costs(pair,t):
    return [max(Fraction(h,1)/(2*t),Fraction(m,1)/(1+t),Fraction(lo,2))
            for h,m,lo in [groups(pair,g) for g in G]]
def target(pair,t):
    if pair in ADJ: return min(max(Fraction(1,1)/(2*t),Fraction(1,2)),Fraction(6,1)/(1+t))
    return Fraction(1,1)/(1+t)
res={"schema":"X6_R87_PAIRED_ANISOTROPY_V1","p":">=125","tests":0,"pairs":[]}
for pair in PAIRS:
    tab={str(Q[i]):list(groups(pair,g)) for i,g in enumerate(G)}
    assert groups(pair,G[2])==((1,1,1) if pair in ADJ else (0,1,0))
    assert min(groups(pair,g)[1] for i,g in enumerate(G) if i!=2)==6
    if pair in ADJ:
        low,high=ADJ[pair]
        assert sorted(Q[i] for i,g in enumerate(G) if groups(pair,g)[0]==0 and groups(pair,g)[1]==6)==sorted(low)
        assert sorted(Q[i] for i,g in enumerate(G) if groups(pair,g)[2]==0 and groups(pair,g)[1]==6)==sorted(high)
        assert all(groups(pair,G[Q.index(q)])[2]<=6 for q in low)
        assert all(groups(pair,G[Q.index(q)])[0]<=6 for q in high)
        expected={Fraction(1,22):low,Fraction(1,11):[11]+low,Fraction(1,2):[11],
                  Fraction(1):[11],Fraction(2):[11],Fraction(11):[11]+high,Fraction(22):high}
    else:
        expected={Fraction(1,22):[11],Fraction(1,11):[11],Fraction(1):[11],
                  Fraction(11):[11],Fraction(22):[11]}
    for t,expected_q in expected.items():
        fs=costs(pair,t); mini=min(fs); got=[Q[i] for i,v in enumerate(fs) if v==mini]
        assert mini==target(pair,t) and sorted(got)==sorted(expected_q),(pair,t,got)
    for n in range(1,71):
        for d in range(1,71):
            t=Fraction(n,d)
            assert min(costs(pair,t))==target(pair,t),(pair,t)
            res["tests"]+=1
    res["pairs"].append({"H":list(pair),"kind":"neighbor" if pair in ADJ else "alternating",
                         "triples_by_q":tab,"low_q":ADJ[pair][0] if pair in ADJ else [11],
                         "high_q":ADJ[pair][1] if pair in ADJ else [11]})
res["pass"]=True
with open("x6_r87_pair_anisotropy_results.json","w",encoding="utf-8") as f:
    json.dump(res,f,ensure_ascii=False,indent=2)
print("PASS",res["tests"])
