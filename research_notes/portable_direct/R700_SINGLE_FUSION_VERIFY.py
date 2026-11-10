#!/usr/bin/env python3
"""Exact R700 finite verification of static E* BRC-derived histogram observer."""
from collections import defaultdict
from pathlib import Path
import json

N=(24,18,6,12)
def uv(v):
    e,t,c,z=v
    return 4*e+5*t+z,2*e+2*c+z
def w(v,k=46):
    u,a=uv(v)
    return u+k*a
def dec(s,W):
    Q=W-47*s
    c=(5*Q)%7
    H=(Q-45*c)//7
    assert (Q-45*c)%7==0
    ans=[]
    for e in range(H%6,25,6):
        t=(7*e-H)//6
        z=s-e-t-c
        if 0<=t<=18 and 0<=z<=12 and w((e,t,c,z))==W:
            ans.append((e,t,c,z))
    return ans
def diff(k):
    short={0:(-1,1,1,-1),1:(0,0,-1,1),2:(0,-1,2,-1),3:(0,-2,1,1),6:(-1,-2,1,2)}
    if k in short:return short[k]
    assert k in (4,5) or 7<=k<=45
    n=k-1
    y=next(y for y in range(4) if (n-3*y)%4==0)
    x=(n-3*y)//4
    assert x>=0
    if x-y>5:x,y=x-3,y+4
    return -x,-y,1+x-y,2*y-1
S=defaultdict(list)
for e in range(25):
 for t in range(19):
  for c in range(7):
   for z in range(13):
    s=e+t+c+z
    if s:S[s].append((e,t,c,z))
assert len(S)==60 and sum(map(len,S.values()))==43224
gap={}
for s,ls in S.items():
    arr=sorted((w(v),v) for v in ls)
    assert len(set(x for x,v in arr))==len(arr)
    assert all(dec(s,x)==[v] for x,v in arr)
    if len(arr)>1:gap[s]=min(arr[i+1][0]-arr[i][0] for i in range(len(arr)-1))
assert gap=={s:4 if s in (1,59) else 3 if s in (2,58) else 1 for s in range(1,60)}
C={}
for k in range(46):
    d=diff(k)
    assert sum(d)==0 and all(abs(a)<=n for a,n in zip(d,N))
    assert w(d,k)==0
    p=tuple(max(a,0) for a in d);m=tuple(max(-a,0) for a in d)
    assert p!=m and sum(p)==sum(m) and w(p,k)==w(m,k)
    C[str(k)]={"delta":d,"v_plus":p,"v_minus":m}
    seen=False
    for ls in S.values():
        sig=set()
        for v in ls:
            x=w(v,k)
            if x in sig:seen=True;break
            sig.add(x)
        if seen:break
    assert seen,k
result={"title":"R700 exact integer fusion", "input_caps":N,"histograms":43224,
        "smallest_integer_coefficient":46,"gaps_by_total":gap,
        "state_counts":{s:len(v) for s,v in S.items()},
        "collision_certificates":C,
        "scope":"frozen static candidate; no V29/V39 native execution"}
Path("R700_SINGLE_FUSION_RESULTS.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print("R700_SINGLE_FUSION_MINIMAL_COEFFICIENT_EXACT_PASS",43224,len(C))
