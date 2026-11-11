#!/usr/bin/env python3
"""R715: odd-ring joint peak/area optimum exact checker, standard Python 3."""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
import json

PAIRS=list(combinations(range(1,6),2))
ADJ={p:tuple(q for q in PAIRS if not set(p).intersection(q)) for p in PAIRS}
W={p:p[1]-p[0]-1 for p in PAIRS}
C={p:tuple(int(p[0]<=t<p[1]) for t in range(1,5)) for p in PAIRS}

def canon(xs):
    q=list(xs)
    return min([tuple(q[i:]+q[:i]) for i in range(len(q))]
              +[tuple(q[::-1][i:]+q[::-1][:i]) for i in range(len(q))])

def simple(n):
    out=set()
    def rec(s):
        if len(s)==n:
            if s[0] in ADJ[s[-1]]:out.add(canon(s))
            return
        for v in ADJ[s[-1]]:
            if v not in s:rec(s+[v])
    for v in PAIRS:rec([v])
    return out

def all_profiles(m):
    k=(m-5)//2
    d={}
    for r in range(k+1):
        for s in range(k-r+1):
            t=k-r-s
            D=(2+r+s,2+t,2+s,2+r+t)
            d[D]=8*m*comb(r+s,s)*comb(r+t,t)
    return d

def dp_profiles(m):
    found=Counter()
    for start in PAIRS:
        dp={(start,W[start],C[start]):1}
        for _ in range(1,m):
            nxt=defaultdict(int)
            for (prev,w,D),count in dp.items():
                for v in ADJ[prev]:
                    w2=w+W[v]
                    if w2>3:continue
                    D2=tuple(a+b for a,b in zip(D,C[v]))
                    nxt[(v,w2,D2)]+=count
            dp=nxt
        for (end,w,D),count in dp.items():
            if w==3 and start in ADJ[end]:found[D]+=count
    return dict(found)

def previous_U(m):
    k=(m-5)//2
    v=[40,168,576,1848]
    while len(v)<=k:
        i=len(v)
        v.append(6*v[i-1]-11*v[i-2]+6*v[i-3]-v[i-4])
    return v[k]

def joint_V(m):
    return 8*m if m%4==1 else 8*m*(2+((m-3)//4)**2)

def main():
    cy={n:simple(n) for n in (5,7,9)}
    assert [len(cy[n]) for n in (5,7,9)]==[12,0,20]
    five=[x for x in cy[5] if sum(W[v] for v in x)==3]
    assert len(five)==4 and min(sum(W[v] for v in x) for x in cy[5])==3
    assert all(sum(W[v] for v in x)>=5 for x in cy[9])
    for x in five:
        assert tuple(sum(C[v][j] for v in x) for j in range(4))==(2,2,2,2)
        remaining=[v for v in PAIRS if W[v]==0 and v not in x]
        assert all(b not in ADJ[a] for a,b in combinations(remaining,2))
    checked=[]
    for m in range(5,18,2):
        exact=dp_profiles(m); predicted=all_profiles(m)
        assert exact==predicted,(m,exact,predicted)
        checked.append(dict(m=m,profiles=len(exact),rooted_walks=sum(exact.values())))
    rows=[]
    for m in range(5,102,2):
        profiles=all_profiles(m)
        U=sum(profiles.values())
        peak=(m+6)//4
        joint={D:n for D,n in profiles.items() if max(D)==peak}
        V=sum(joint.values())
        assert U==previous_U(m),(m,U,previous_U(m))
        assert V==joint_V(m),(m,V,joint_V(m))
        assert len(joint)==(1 if m%4==1 else 3)
        rows.append({"m":m,"U_m":U,"V_m":V,"peak":peak,"joint_profiles":
          {",".join(map(str,D)):v for D,v in joint.items()}})
    print(json.dumps({
      "status":"R714_ODD_RING_JOINT_OPTIMAL_PROFILE_PASS",
      "scope":"all odd m>=5 theorem; exact DP m=5..17; closed/recurrent checks m=5..101",
      "Petersen_cycles":{"five":len(cy[5]),"seven":len(cy[7]),"nine":len(cy[9]),"minimal_five":len(five)},
      "independent_dp":checked,"exact_rows":rows
    },indent=2,ensure_ascii=False))

if __name__=="__main__":main()
