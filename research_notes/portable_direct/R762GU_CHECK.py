#!/usr/bin/env python3
"""Exact integer BRC checks for signed K4 STAR candidate, R762GU.
The signed composite source alphabet is a constructed model, not an admission of
native TRIADIC_CLOSURE_E updates.
"""
from collections import defaultdict
from itertools import combinations, product
from math import factorial
from fractions import Fraction
import json

V = tuple(range(4))
E = tuple(combinations(V, 2))
H = {v: tuple(int(v in e) for e in E) for v in V}
ZERO = (0, 0, 0, 0)

def y_of(z):
    return tuple(z[u]+z[v] for u,v in E)

def recover(y):
    if len(y) != 6:
        return None
    a,b,c,d,e,f=y
    if (a+b+d) % 2 or e != d+c-b or f != d+c-a:
        return None
    z0=(a+b-d)//2
    z1=(a+d-b)//2
    z2=(b+d-a)//2
    z3=c-z0
    z=(z0,z1,z2,z3)
    return z if y_of(z)==tuple(y) else None

def rank(rows):
    a=[[Fraction(x) for x in row] for row in rows]
    p=0
    for j in range(4):
        r=next((i for i in range(p,len(a)) if a[i][j]!=0),None)
        if r is None: continue
        a[p],a[r]=a[r],a[p]
        t=a[p][j]
        a[p]=[x/t for x in a[p]]
        for k in range(len(a)):
            if k!=p:
                t=a[k][j]
                a[k]=[a[k][l]-t*a[p][l] for l in range(4)]
        p+=1
        if p==4: break
    return p

def formula_count(m,z):
    norm=sum(map(abs,z))
    if m<norm or (m-norm)%2: return 0
    q=(m-norm)//2
    ans=0
    for r0 in range(q+1):
      for r1 in range(q-r0+1):
       for r2 in range(q-r0-r1+1):
        r=(r0,r1,r2,q-r0-r1-r2)
        denom=1
        for v in range(4):
            denom*=factorial(r[v]+max(z[v],0))*factorial(r[v]+max(-z[v],0))
        ans+=factorial(m)//denom
    return ans

def run():
    assert E == ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
    assert rank([tuple(int(v in e) for v in V) for e in E])==4
    good4=sum(rank([tuple(int(v in E[i]) for v in V) for i in subset])==4
              for subset in combinations(range(6),4))
    assert good4==12
    # All bounded signed inventories: necessary and sufficient lattice test.
    for z in product(range(-3,4), repeat=4):
        assert recover(y_of(z))==z
    for y in product(range(-2,3), repeat=6):
        z=recover(y)
        if z is not None: assert y_of(z)==y
    # Iterate ordered signed source words while retaining positive integer counts.
    cur={ZERO:1}
    records=[]
    for m in range(13):
        mass=sum(cur.values())
        assert mass==8**m
        assert len(cur)==((m+1)**2*(m*m+2*m+3))//3
        if m<=6:
            assert all(formula_count(m,z)==count for z,count in cur.items())
        zero_count=cur.get(ZERO,0)
        records.append({"length":m,"source_words":mass,
                        "distinct_signed_net_inventories":len(cur),
                        "zero_cell_readout_paths":zero_count})
        if m<12:
            nxt=defaultdict(int)
            for z,n in cur.items():
                for v in V:
                    for s in (-1,1):
                        q=list(z);q[v]+=s
                        nxt[tuple(q)]+=n
            cur=dict(nxt)
    assert records[2]['zero_cell_readout_paths']==8
    assert records[4]['zero_cell_readout_paths']==168
    assert records[6]['zero_cell_readout_paths']==5120
    assert records[1]['zero_cell_readout_paths']==0
    # Compare path enumeration to the recurrence and exact formula independently.
    for m in range(5):
        word_counts=defaultdict(int)
        for w in product(tuple(product(V,(-1,1))),repeat=m):
            z=[0]*4
            for v,s in w:z[v]+=s
            word_counts[tuple(z)]+=1
        assert len(word_counts)==records[m]['distinct_signed_net_inventories']
        assert sum(word_counts.values())==8**m
        assert all(formula_count(m,z)==n for z,n in word_counts.items())
    assert recover((1,0,0,0,0,0)) is None
    assert recover((1,1,0,1,0,0)) is None
    result={"model":"constructed_signed_K4_STAR_candidate",
            "status":"AUTHOR_EXACT_CHECK_PASS",
            "axis_order":["%d%d"%e for e in E],
            "four_axis_full_rank_subsets":good4,
            "full_rank":4,
            "lattice_constraints":["y13=y03+y12-y02", "y23=y03+y12-y01", "y01+y02+y12 even"],
            "length_0_to_12":records,
            "review":"NOT_REVIEWED"}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
