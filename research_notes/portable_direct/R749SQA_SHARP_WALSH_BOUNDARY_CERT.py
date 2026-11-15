#!/usr/bin/env python3
"""R749SQA exact integer checker. Symbolic universal proof is in the paired note."""
from collections import defaultdict, Counter
from fractions import Fraction
import json

facets=[(-1,-1,-1,-2),(-1,-1,1,-2),(-1,1,-1,-2),(-1,1,1,-2),
        (1,-1,-1,-2),(1,-1,1,-4),(1,1,-1,-4),(1,1,1,-2)]
P=[(h,u,v) for h in range(-2,3) for u in range(-2,3) for v in range(-2,3)
   if all(a*h+b*u+c*v>=t for a,b,c,t in facets)]
assert len(P)==33
pairs=defaultdict(list)
for i in range(len(P)):
    for j in range(i,len(P)):
        pairs[tuple(P[i][k]+P[j][k] for k in range(3))].append((i,j))
ids=set()
for alternatives in pairs.values():
    if len(alternatives)==1: ids.update(alternatives[0])
F=[P[i] for i in sorted(ids)]
B=[(h,2-u,v) for h,u,v in F if u<2]
assert len(F)==25 and len(B)==23
assert sorted(p for p in F if p[1]==2)==[(-1,2,-1),(0,2,0)]
assert sum(p==(0,1,1) for p in B)==1
assert all(d>=1 and v<=d for h,d,v in B)

def patterns(D):
    dp=[defaultdict(int) for _ in range(D+1)]
    dp[0][(0,0,0)]=1  # number of B letters, H, V
    for h,d,v in B:
        for e in range(d,D+1):
            for (m,H,V),c in list(dp[e-d].items()):
                dp[e][(m+1,H+h,V+v)]+=c
    return [(k,m,H,V,c) for k in range(D//2+1)
            for (m,H,V),c in dp[D-2*k].items() if V>=0]

cases=[]
for D in range(2,13):
    rows=patterns(D)
    N=sum(c for *_,c in rows)
    W=sum(k*c for k,m,H,V,c in rows)
    def signed(n):
        z=defaultdict(int)
        for k,m,H,V,c in rows:
            if k and k+m+V<=n:
                z[H-V]+=c;z[H-V-k]-=c
        return {h:c for h,c in z.items() if c}
    full=signed(2*D)
    assert signed(2*D-3)==full and signed(2*D-4)!=full
    assert sum(h*c for h,c in full.items())==W
    Hstar=-(D-2)
    tailgap=sum(c for h,c in full.items() if h>=Hstar)-sum(
        c for h,c in signed(2*D-4).items() if h>=Hstar)
    assert tailgap==1
    def nw(n):
        a=[(k,c) for k,m,H,V,c in rows if k+m+V<=n]
        return sum(c for k,c in a),sum(k*c for k,c in a)
    assert nw(2*D-1)==(N-1,W)
    assert nw(2*D-2)==(N-4,W)
    assert nw(2*D-3)[1]==W and nw(2*D-4)[1]==W-1
    if D in (2,4,6,8):
        assert (N,W)=={2:(15,1),4:(176,16),6:(1468,192),8:(9584,1660)}[D]
    x=Fraction(W,20*N)
    cases.append({'D':D,'N':N,'W':W,'sharp_signed_n':2*D-3,
                  'tail_gap_one':tailgap,'mass_at_2D_minus_2':N-4,
                  'mass_at_2D_minus_1':N-1,
                  'saturated_W1_prefactor':str(x)})

s=Counter(2*d-1-v for h,d,v in B if (h,d,v)!=(0,1,1))
s[3]+=1  # the optional letter
assert dict(sorted(s.items()))=={1:3,2:4,3:6,4:4,5:3,6:2,7:1}
g=[0]*8;g[0]=1
for j,multiplicity in sorted(s.items()):
    for _ in range(multiplicity):
        for i in range(j,8): g[i]+=g[i-j]
C=[sum(g[:r]) for r in range(1,9)]
assert C==[1,4,14,42,113,279,651,1437]
layer=[]
for r,target in enumerate(C,1):
    D=max(2,2*r-2)
    def missing(d):
        return sum(c for k,m,H,V,c in patterns(d) if k+m+V>2*d-r)
    assert missing(D)==target and missing(D+1)==target
    prev=missing(D-1) if r>=3 else None
    if r>=3: assert prev==target-1
    layer.append({'r':r,'threshold_D':D,'missing':target,'previous_D_missing':prev})
print(json.dumps({'schema':'R749SQA_SHARP_WALSH_BOUNDARY_V1',
    'status':'PASS','scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'predecessor_commit':'b4507430ced229f67db20fe0424e3988ca747c7a',
    'model':'auxiliary signed 16-atom Walsh source, t=1/10, s=1/2',
    'arithmetic':'Python integers and Fraction only; no floating tolerance',
    'first_grid_points':len(P),'forced_source_types':len(F),
    'slack_multiplicities':dict(sorted(s.items())),'slack_g0_to_g7':g,
    'boundary_layer_constants_C1_to_C8':C,'layer_checks':layer,
    'exact_D_cases':cases,'universal_scope':'symbolic proof in accompanying note',
    'review':'AUTHOR_EXACT_NOT_REVIEWED'},indent=2))
