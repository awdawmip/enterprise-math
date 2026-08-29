#!/usr/bin/env python3
"""Exact checker for RS-SEED6-BRIDGE-CELL-DEGENERACY-STRATIFICATION."""
from __future__ import annotations
import argparse, json
from collections import Counter
from math import gcd
from pathlib import Path

PAIRINGS=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
EXPECTED={(1,1,1,1):3,(2,1,1):2,(2,2):2,(3,1):1,(4,):1}

def factorint(n):
    if n<1: raise ValueError("positive integers only")
    x=n; out={}; p=2
    while p*p<=x:
        while x%p==0: out[p]=out.get(p,0)+1; x//=p
        p=3 if p==2 else p+2
    if x>1: out[x]=out.get(x,0)+1
    return out

def is_prime(n):
    if n<2:return False
    f=factorint(n); return len(f)==1 and next(iter(f.values()))==1

def is_prime_power(n): return n>=2 and len(factorint(n))==1

def support_class(n):
    if n==1:return "unit"
    f=factorint(n)
    if len(f)==1:
        return "prime" if next(iter(f.values()))==1 else "prime_power"
    return "squarefree_composite" if all(e==1 for e in f.values()) else "mixed_composite"

def partition_type(vals): return tuple(sorted(Counter(vals).values(),reverse=True))

def symbolic_pairings(vals):
    out=set()
    for (i,j),(k,l) in PAIRINGS:
        a=tuple(sorted((vals[i],vals[j]))); b=tuple(sorted((vals[k],vals[l])))
        out.add(tuple(sorted((a,b))))
    return out

def product_states(r,s):
    return [tuple(sorted((6,r*s))),tuple(sorted((2*r,3*s))),tuple(sorted((2*s,3*r)))]

def state_count(r,s): return len(set(product_states(r,s)))

def state_equalities(r,s): return {"P1=P2":r==s,"P0=P1":r==3 or s==2,"P0=P2":r==2 or s==3}

def rect_vertices(r,s): return (2*r,2*s,3*r,3*s)

def rect_vcount(r,s): return len(set(rect_vertices(r,s)))

def predicted_rect_vcount(r,s):
    if r==s:return 2
    if 2*r==3*s or 2*s==3*r:return 3
    return 4

def gcd_labels(r,s):
    a,b,c,d=rect_vertices(r,s)
    return {"top":gcd(a,b),"bottom":gcd(c,d),"left":gcd(a,c),"right":gcd(b,d),"diag_ad":gcd(a,d),"diag_bc":gcd(b,c)}

def gcd_formula(r,s):
    d=gcd(r,s)
    return {"top":2*d,"bottom":3*d,"left":r,"right":s,"diag_ad":gcd(2*r,3*s),"diag_bc":gcd(2*s,3*r)}

def verify_state_theorem(r,s):
    p0,p1,p2=product_states(r,s); e=state_equalities(r,s)
    assert (p1==p2)==e["P1=P2"]
    assert (p0==p1)==e["P0=P1"]
    assert (p0==p2)==e["P0=P2"]

def base_exp(n):
    f=factorint(n)
    if len(f)!=1: raise ValueError(n)
    return next(iter(f.items()))

def verify_prime_power_fibers(limit):
    pps=[n for n in range(2,limit+1) if is_prime_power(n)]
    out=Counter()
    for r in pps:
        pr,ar=base_exp(r)
        for s in pps:
            ps,bs=base_exp(s)
            if pr<=3 or ps<=3: continue
            out["checked_ordered_pairs"]+=1
            if pr!=ps:
                out["disjoint_base"]+=1
                assert state_count(r,s)==3 and rect_vcount(r,s)==4 and gcd(r,s)==1
                g=gcd_labels(r,s); assert g["diag_ad"]==g["diag_bc"]==1
            elif ar!=bs:
                out["same_base_unequal_exponent"]+=1
                assert state_count(r,s)==3 and rect_vcount(r,s)==4
                m=pr**min(ar,bs); g=gcd_labels(r,s); assert g["diag_ad"]==g["diag_bc"]==m
            else:
                out["same_base_equal_exponent"]+=1
                assert r==s and state_count(r,s)==2 and rect_vcount(r,s)==2
    return dict(out)

def run(limit=200):
    eq=Counter(); sc=Counter(); rv=Counter(); sp=Counter(); reson=[]
    for r in range(1,limit+1):
        for s in range(1,limit+1):
            verify_state_theorem(r,s)
            pt=partition_type([2,3,r,s]); m=len(symbolic_pairings([2,3,r,s]))
            assert m==EXPECTED[pt] and state_count(r,s)==m
            assert rect_vcount(r,s)==predicted_rect_vcount(r,s)
            assert gcd_labels(r,s)==gcd_formula(r,s)
            eq["+".join(map(str,pt))]+=1; sc[str(state_count(r,s))]+=1; rv[str(rect_vcount(r,s))]+=1
            sp[f"{support_class(r)}|{support_class(s)}"]+=1
            if r!=s and (2*r==3*s or 2*s==3*r): reson.append((r,s))
    primes=[n for n in range(2,limit+1) if is_prime(n)]
    pps=[n for n in range(2,limit+1) if is_prime_power(n)]
    for p in primes:
        if p>3:
            assert state_count(p,p)==2 and rect_vcount(p,p)==2
            assert state_count(2,p)==state_count(p,2)==2
            assert state_count(3,p)==state_count(p,3)==2
    assert state_count(2,3)==state_count(3,2)==2
    assert state_count(2,2)==state_count(3,3)==1
    if limit>=55:
        assert state_count(35,55)==3 and rect_vcount(35,55)==4
        g=gcd_labels(35,55); assert g["diag_ad"]==g["diag_bc"]==5
    if limit>=6:
        assert state_count(6,4)==3 and rect_vcount(6,4)==3 and rect_vertices(6,4)[0]==rect_vertices(6,4)[3]==12
    assert len(reson)==2*(limit//3)
    return {"task_id":"RS-SEED6-BRIDGE-CELL-DEGENERACY-STRATIFICATION","limit":limit,"ordered_pairs_checked":limit*limit,
            "prime_count":len(primes),"prime_power_count_including_primes":len(pps),"equality_partition_counts":dict(sorted(eq.items())),
            "pairing_state_count_distribution":dict(sorted(sc.items())),"rectangle_vertex_count_distribution":dict(sorted(rv.items())),
            "ratio_resonance_ordered_pair_count":len(reson),"ratio_resonance_formula":"2*floor(limit/3)",
            "prime_power_fiber_checks":verify_prime_power_fibers(limit),"support_pair_class_counts":dict(sorted(sp.items())),"verdict":"PASS"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--limit",type=int,default=200); ap.add_argument("--json-out",type=Path); a=ap.parse_args()
    summary=run(a.limit); text=json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True); print(text)
    if a.json_out: a.json_out.parent.mkdir(parents=True,exist_ok=True); a.json_out.write_text(text+"\n",encoding="utf-8")
if __name__=="__main__": main()
