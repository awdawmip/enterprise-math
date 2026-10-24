#!/usr/bin/env python3
"""R275 finite base certificate; all counts are nonnegative exact integers."""
from collections import defaultdict
import json

S = ((0, 0), (1, 1), (2, 0), (2, 1))
E = {(0,0):((0,(2,1),-1,-1),(1,(2,0),1,-1)),
     (1,1):((1,(0,0),1,-1),),
     (2,0):((0,(1,1),1,1),(1,(2,0),1,-1)),
     (2,1):((1,(2,0),1,-1),)}
RAW = {0:((2,-1,-1),(2,1,-1)),
       1:((0,-1,-1),(0,1,-1)),
       2:((1,1,1),(2,1,-1))}

def blank(): return {s:defaultdict(int) for s in S}

def step(v):
    w = blank()
    for s in S:
        for (eps,k),c in v[s].items():
            for _,t,eta,b in E[s]: w[t][(eta*eps,eta*k+b)] += c
    return w

def brute(n):
    w=blank()
    for x in range(1<<n):
        q,eps,k,last,clean=0,1,0,0,True
        for j in range(n-1,-1,-1):
            a=(x>>j)&1
            if last and not a: clean=False;break
            nq,eta,b=RAW[q][a]
            q,eps,k,last=nq,eta*eps,eta*k+b,1-a
        if clean:w[(q,last)][(eps,k)]+=1
    return w

def hist(v,q):
    out=defaultdict(int)
    for (q0,_),d in v.items():
        if q==q0:
            for g,c in d.items():out[g]+=c
    return out

def dominates(a,b):return all(a.get(g,0)>=c for g,c in b.items())

def main():
    v=blank();v[(0,0)][(1,0)]=1;vs=[]
    for n in range(16):
        vs.append(v)
        assert all(dict(brute(n)[s])==dict(v[s]) for s in S),n
        v=step(v)
    counts=[];sums=[]
    for s in S:
        a,b=vs[13][s],vs[15][s]
        d=[b.get(g,0)-a.get(g,0) for g in set(a)|set(b)]
        assert all(x>0 for x in d)
        counts.append(len(d));sums.append(sum(d))
    assert counts==[22,24,26,20] and sums==[169,274,441,103]
    p=[hist(x,0) for x in vs]; r=[hist(x,2) for x in vs]
    assert all(dominates(r[n],p[n]) for n in (12,13,14))
    assert not dominates(r[11],p[11])
    assert (p[11].get((1,-5)),r[11].get((1,-5)))==(6,5)
    assert all(dominates(r[n-2],p[n]) for n in range(3,16))
    assert dominates(r[12],r[10]) and dominates(r[13],r[11]) and dominates(r[14],r[12])
    assert dominates(p[14],p[12])
    assert vs[12][(2,1)][(-1,4)]==6 and vs[14][(2,1)][(-1,4)]==5
    print(json.dumps({'status':'PASS','raw_words':sum(1<<i for i in range(16)),
         'base_delta_counts':counts,'base_delta_sums':sums,
         'all_n_proof':'T preserves nonnegative cone, and reset word ends identity-effect 01',
         'short_q2_counterexample':{'n':11,'effect':[1,-5],'P':6,'R':5}},sort_keys=True))

if __name__=='__main__':main()
