#!/usr/bin/env python3
"""Exact nonnegative weighted-graph and cycle future-observer validation (stdlib)."""
from itertools import combinations, product
import random, json

def q(bits, edges):
    return sum(w * bits[i] * bits[j] for i,j,w in edges)

def partition_check(n, edges, control):
    J=set(control)
    D={}
    inv2obs={}
    for u in product((0,1),repeat=n):
        obs=[]
        for choices in product((None,0,1),repeat=len(control)):
            x=list(u)
            for i,v in zip(control,choices):
                if v is not None: x[i]=v
            obs.append(q(x,edges))
        obs=tuple(obs)
        C=sum(w*u[i]*u[j] for i,j,w in edges if i not in J and j not in J)
        b=tuple(sum(w*u[j if i==p else i] for i,j,w in edges
                    if (i==p and j not in J) or (j==p and i not in J))
                for p in control)
        d=tuple(sum(w for i,j,w in edges if i in J and j in J and p in (i,j))
                for p in control)
        active=tuple(u[p] if b[t]+d[t]>0 else None for t,p in enumerate(control))
        inv=(C,b,active)
        if obs in D: assert D[obs]==inv,(n,control,u,"collision")
        if inv in inv2obs: assert inv2obs[inv]==obs,(n,control,u,"mismatched class")
        D[obs]=inv
        inv2obs[inv]=obs
    assert len(D)==len(inv2obs)
    return len(D)

def necklace_min(k, missing):
    edges=set()
    for i in range(k):
        a,b,z=i,(i+1)%k,k+i
        edges.update(tuple(sorted(e)) for e in ((a,b),(a,z),(b,z)))
    avail=sorted(set(range(2*k))-set(missing))
    best=3*k*10
    for mask in range(1<<len(avail)):
        S={v for i,v in enumerate(avail) if (mask>>i)&1}
        f=2*len(S)+sum(a not in S and b not in S for a,b in edges)
        best=min(best,f)
    return len(edges)+best

def main():
    cases=0
    cycle=[]
    for k in range(3,9):
        edges=[(i,(i+1)%k,1) for i in range(k)]
        for size in range(1,min(k,3)+1):
            for J in combinations(range(k),size):
                partition_check(k,edges,J); cases+=1
    rng=random.Random(20261116)
    weighted=0
    for n in range(3,7):
        for _ in range(40):
            edges=[(i,j,w) for i in range(n) for j in range(i+1,n)
                   if (w:=rng.randrange(4))>0]
            J=tuple(sorted(rng.sample(range(n),rng.randrange(1,min(n,3)+1))))
            partition_check(n,edges,J); weighted+=1
    for k in range(3,15):
        n=k-2
        seen=set()
        for rest in product((0,1),repeat=n):
            C=sum(rest[i]*rest[i+1] for i in range(n-1))
            seen.add((C,rest[0],rest[-1]))
        count=4*len(seen)
        want=8 if k==3 else 16 if k==4 else 16*k-52
        assert count==want,(k,count,want)
        if k<=10:
            assert partition_check(k,[(i,(i+1)%k,1) for i in range(k)],(0,1))==want
        cycle.append({"k":k,"equivalence_classes":count})
    k=6
    su,sv,sboth=(necklace_min(k,X) for X in ({3},{4},{3,4}))
    assert (su,sv,sboth)==(30,30,31)
    result={"status":"PASS_R5_MULTI_CONTROL_RESIDUAL_AND_SOURCE_SEPARATION",
            "input_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
            "exhaustive_cycle_control_families":cases,
            "weighted_graph_cases":weighted,"weighted_seed":20261116,
            "adjacent_control_counts":cycle,"source_minima":[su,sv,sboth]}
    with open("EXACT_R5_MULTI_CONTROL_EVIDENCE.json","w",encoding="utf8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2); f.write("\n")
    print(result["status"]); print(result)
if __name__=="__main__":
    main()
