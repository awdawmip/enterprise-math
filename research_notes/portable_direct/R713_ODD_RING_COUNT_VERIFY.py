#!/usr/bin/env python3
"""R713 integer certificate for five-phase odd full-ring candidate schedules.
Counts preserve typed + and - events; signed current only as readout.
"""
from itertools import combinations
from collections import defaultdict
import json

V=tuple(combinations(range(1,6),2))
N=len(V)
W=tuple(b-a-1 for a,b in V)
ADJ=tuple(tuple(j for j,v in enumerate(V) if set(u).isdisjoint(v)) for u in V)

def determinant_bounded_y():
    # Leibniz subset DP, coefficient polynomials of det(I-z*A*D(y)) mod y^4.
    dp={(0,0,0):1}
    for row in range(N):
        nd=defaultdict(int)
        for (mask,zd,yd),c in dp.items():
            assert mask.bit_count()==row
            for col in range(N):
                if (mask>>col)&1:continue
                sgn=-1 if ((mask>>(col+1)).bit_count()&1) else 1
                mask1=mask|(1<<col)
                if col==row:
                    nd[(mask1,zd,yd)]+=sgn*c
                elif col in ADJ[row] and yd+W[col]<=3:
                    nd[(mask1,zd+1,yd+W[col])]-=sgn*c
        dp={k:v for k,v in nd.items() if v}
    coeff=tuple({zd:c for (mask,zd,yd),c in dp.items() if yd==k}
                for k in range(4))
    want=({0:1,2:-3,4:1},
          {2:-2,4:2},
          {2:-4,4:11,6:-2},
          {2:-4,4:16,5:-8,6:-6})
    assert coeff==want,(coeff,want)
    assert all(deg%2==0 for k in range(3) for deg in coeff[k])
    assert {deg:c for deg,c in coeff[3].items() if deg%2}=={5:-8}
    return coeff

def closed_walk_counts(max_m):
    out=defaultdict(int)
    for s in range(N):
        states={(s,W[s]):1}
        for m in range(1,max_m+1):
            if m>=5 and m%2:
                out[m]+=sum(c for (last,w),c in states.items()
                    if w==3 and s in ADJ[last])
            nd=defaultdict(int)
            for (last,w),c in states.items():
                for j in ADJ[last]:
                    if w+W[j]<=3:
                        nd[(j,w+W[j])]+=c
            states=nd
    return dict(out)

def rational_counts(max_m):
    c=[]
    for k in range((max_m-5)//2+1):
        forcing={0:40,1:-72,2:8}.get(k,0)
        v=forcing
        for lag,coef in ((1,6),(2,-11),(3,6),(4,-1)):
            if k>=lag:v+=coef*c[k-lag]
        c.append(v)
    return {2*k+5:v for k,v in enumerate(c)}

def peak_hist(m,expected):
    delta=tuple(tuple(int(a<=t<b) for t in range(1,5)) for a,b in V)
    counts=defaultdict(int)
    for s in range(N):
        states={(s,W[s],delta[s]):1}
        for step in range(m-1):
            nd=defaultdict(int)
            for (i,w,d),c in states.items():
                for j in ADJ[i]:
                    if w+W[j]<=3:
                        nd[(j,w+W[j],tuple(d[t]+delta[j][t] for t in range(4)))]+=c
            states=nd
        for (i,w,d),c in states.items():
            if w==3 and s in ADJ[i]:counts[d]+=c
    assert sum(counts.values())==expected
    peak=(m+6)//4
    return {"m":m,"U_m":expected,
       "joint_peak_area_count":sum(c for d,c in counts.items() if max(d)==peak),
       "peak_profiles":{",".join(map(str,d)):c for d,c in sorted(counts.items()) if max(d)==peak},
       "all_area_minimal_profile_kinds":len(counts)}

if __name__=="__main__":
    det=determinant_bounded_y()
    direct=closed_walk_counts(101)
    formula=rational_counts(101)
    assert direct==formula
    peaks=[peak_hist(m,direct[m]) for m in range(5,22,2)]
    obj={"verdict":"R713_ODD_RING_AREA_OPTIMAL_ENTROPY_PASS",
       "source_pin":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
       "candidate_model":"five phases, pairwise disjoint phase subsets on adjacent edges, odd full cycle",
       "coefficient_identity":"8*z^5*(5-9*z^2+z^4)/(1-3*z^2+z^4)^2",
       "det_y0_to_y3":[dict(sorted(x.items())) for x in det],
       "verified_odd_sizes":len(direct),"max_m":101,
       "untyped_area_min_counts":{str(m):v for m,v in sorted(direct.items())},
       "selected_typed":{str(m):{"U_m":direct[m],"T_m":(2**m)*direct[m],
         "minimum_bits":m+(direct[m]-1).bit_length()} for m in (5,7,9,11,13,19,31,101)},
       "peak_profiles":peaks,"independent_review":"PENDING"}
    print(json.dumps(obj,ensure_ascii=False,indent=2))
