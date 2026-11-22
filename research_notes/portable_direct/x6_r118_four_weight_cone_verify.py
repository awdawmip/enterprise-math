#!/usr/bin/env python3
"""X6 R118 exact six-pair finite replay for a rational weight section.
The analytic theorem, not the finite replay, covers all real D and all Port >=10.
"""
from fractions import Fraction as Q
from itertools import combinations
import json

ROWS = (
 ((0,1,-1),17,None), ((0,1,1),10,None),
 ((0,2,0),27,Q(181,2)), ((1,-2,0),38,Q(542,7)),
 ((1,0,0),11,Q(107)), ((1,2,0),16,Q(211,2)),
 ((1,-1,-1),21,Q(107)), ((1,-1,1),28,Q(107)),
 ((1,1,-1),6,Q(107)), ((1,1,1),1,Q(107)))
PORTS=(10,11,16,17,21,27,28,38)
DS=(Q(71),Q(75),Q(542,7),Q(78),Q(181,2),Q(91),
    Q(211,2),Q(106),Q(107),Q(110),Q(121))
PAIRS=tuple(combinations(range(4),2))

def inverse(t,m,n):
    assert (m-n)%2==0
    return (10*t-12*m+3*n,-5*t+7*m-2*n,t+(n-3*m)//2)

def canon(a):
    return min(a,tuple(-v for v in a))

def port(a):
    return max(sum(max(v,0) for v in a),sum(max(-v,0) for v in a))

def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[i]-h[j]) for i,j in PAIRS)

VECTORS=[]
for x in range(-38,39):
    for y in range(-38,39):
        for z in range(-38,39):
            a=(x,y,z)
            if a==(0,0,0) or a!=canon(a):
                continue
            p=port(a)
            if p<=38:
                VECTORS.append((p,a,gaps(a)))
assert len(VECTORS)==95133

def check(d):
    den=d.denominator
    w=(11*den,den,60*den,d.numerator)
    Y=w[1]+w[3]
    sums=tuple(w[i]+w[j] for i,j in PAIRS)
    predicted={canon(inverse(*r)) for r,p,lim in ROWS
               if lim is None or d<lim}
    for r,p,lim in ROWS:
        assert port(inverse(*r))==p
    got=set()
    below_eta=0
    by_port={p:set() for p in PORTS}
    for p,a,g in VECTORS:
        if all(gk*Y<6*wk for gk,wk in zip(g,sums)):
            below_eta+=1
        if all(gk*Y<9*wk for gk,wk in zip(g,sums)):
            got.add(a)
            for cap in PORTS:
                if p<=cap:
                    by_port[cap].add(a)
    assert below_eta==0
    assert got==predicted,(str(d),got^predicted)
    for cap in PORTS:
        expected={canon(inverse(*r)) for r,p,lim in ROWS
                  if p<=cap and (lim is None or d<lim)}
        assert by_port[cap]==expected,(str(d),cap)
    witness=inverse(0,1,1)
    assert port(witness)==10
    assert all(g*Y<=6*wk for g,wk in zip(gaps(witness),sums))
    assert any(g*Y==6*wk for g,wk in zip(gaps(witness),sums))
    return {"D":str(d),"eta":str(Q(6,1)/(1+d)),
            "near_at_port38":len(got),
            "port_counts":{str(p):len(by_port[p]) for p in PORTS},
            "violations_below_eta":below_eta,
            "symmetric_difference":len(got^predicted)}

if __name__=="__main__":
    out={"schema":"X6_R118_FOUR_WEIGHT_CONE_D_FAN_EXACT_REPLAY_V1",
         "scope":"all p>=10 by analytic proof; exact replay p<=38",
         "unoriented_vectors_per_case":len(VECTORS),
         "sample_count":len(DS),
         "total_vector_sample_pairs":len(VECTORS)*len(DS),
         "cases":[check(d) for d in DS],
         "review":"AUTHOR_PROOF_NOT_INDEPENDENTLY_REVIEWED"}
    print(json.dumps(out,indent=2))
