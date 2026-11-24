#!/usr/bin/env python3
"""R5 exact overlapping triangle-chain graph-source kernel; Python stdlib."""
import json,sys
from itertools import product
from pathlib import Path
OLD=((0,1,2,5),(0,1,3,5),(0,2,3,5),(0,2,4,5),(0,2,4,6))
A=(((1,2,3,5),1),((1,2,4,5),1),((1,2,4,6),1),
   ((1,3,4,5),0),((1,3,4,6),0))
AB=A+(((1,2,3,6),1),)
def hd(a,b): return (a^b).bit_count()
def rho(t,z):
    C,b,y=t; j,s,x=z
    return len(set(C)-set(OLD[j]))+(b!=s)+hd(y,x)
def chain(k):
    n=2*k+1; E=[]
    for i in range(k):
        a=i; b=i+1; w=k+1+i
        E.extend(((a,b),(a,w),(b,w)))
    return n,E
def candidate(k,S):
    n,E=chain(k); Y=sorted((1<<u)|(1<<v) for u,v in E)
    src=[(1,0,y) for y in Y]
    src += [(j,1,1<<v) for v in sorted(S) for j in (0,4)]
    src += [(0,1,(1<<u)|(1<<v)) for u,v in E if u not in S and v not in S]
    return Y,src
def exhaustive(k,W):
    n,E=chain(k); opt=10**9; witness=None; count=0
    for bits in range(1<<n):
        if any((bits>>v&1) and v not in W for v in range(n)): continue
        S={v for v in range(n) if bits>>v&1}
        score=2*len(S)+sum(u not in S and v not in S for u,v in E)
        if score<opt: opt=score;witness=S;count=1
        elif score==opt: count+=1
    return opt,witness,count
def transfer(k,W):
    d={a:2*a for a in (0,1) if not a or 0 in W}
    for i in range(k):
        nxt={}
        for a,value in d.items():
            for b,c in product((0,1),repeat=2):
                if b and (i+1) not in W: continue
                if c and (k+1+i) not in W: continue
                cost=value+2*b+2*c+(1-a)*(1-b)+(1-a)*(1-c)+(1-b)*(1-c)
                nxt[b]=min(nxt.get(b,10**9),cost)
        d=nxt
    return min(d.values())
def main():
    assert [tuple(len(set(C)-set(o)) for o in OLD) for C,t in AB]==[
      (1,1,1,2,3),(1,2,2,1,2),(2,3,3,2,1),
      (2,1,2,2,3),(3,2,3,3,2),(2,2,2,3,2)]
    B=((1,2,4,5),1,0);C=((1,2,4,6),1,0);D=((1,3,4,5),0,0)
    for j,s in product(range(5),(0,1)):
        assert sum(rho(t,(j,s,1))<=2 for t in (B,C,D))<=1
    rows=[]; tested=0
    for k in range(1,8):
        n,E=chain(k);W=set(range(n))
        minimum,S,number=exhaustive(k,W)
        assert minimum==(3 if k==1 else 2*k)
        assert transfer(k,W)==minimum
        Y,src=candidate(k,S)
        assert len(set(Y))==3*k and len(set(src))==len(src)
        assert len(src)==3*k+minimum
        assert all(any(rho((C,t,y),z)<=2 for z in src) for y in Y for C,t in A)
        assert all({y for y in Y if hd(y,1<<v)==1}==
                   {(1<<u)|(1<<w) for u,w in E if v in (u,w)} for v in range(n))
        if k<=4:
            for mask in range(1<<n):
                available={v for v in range(n) if mask>>v&1}
                assert exhaustive(k,available)[0]==transfer(k,available)
                tested+=1
        if k>=2:
            f,g=0,1
            for _ in range(k-1):f,g=g,f+g
            assert number==f
        rows.append(dict(k=k,suffix_bits=n,target_edges=len(E),
                    subsets_examined=1<<n,optimal_graph_subsets=number,
                    kappa_a=3*k+minimum,kappa_ab_prior=6*k,
                    selected_helper_vertices=sorted(S),labeled_witness=src))
    assert tested==680
    out=dict(frozen_pin="435e77af0d180eac32bd1f9c4c464bc4010b7551",
             status="PASS_R5_OVERLAPPING_TRIANGLE_CHAIN",all_W_masks_tested=tested,
             proof="analytic graph-source reduction and triangle run bound",
             exact_finite_scope="k=1..7 all graph subsets; k=1..4 all helper-availability languages; labeled source coverage",
             cases=rows)
    if len(sys.argv)>1: Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(out["status"])
    print([(r["k"],r["kappa_a"],r["kappa_ab_prior"]) for r in rows])
if __name__=="__main__":main()
