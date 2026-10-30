#!/usr/bin/env python3
"""Exact integer author-side checks of nonnormalized BRC mass-defect bounds.

Auxiliary finite positive branch source kernels, not native X6. No floats.
"""
import itertools
import json
from collections import defaultdict
from math import isqrt

X = (0, 1, 2)
Y = (0, 1)
C = {0: 0, 1: 0, 2: 1}
R = {0: 0, 1: 2}


def prod(seq):
    n=1
    for a in seq:n*=a
    return n


def run_all_rows():
    # Per-label per-source rows; masses may vary from 1 to 2.
    opts = ((0,1),(1,0),(0,2),(1,1),(2,0))
    W=(1,2)
    count=0
    tuples=0
    target_entries=0
    nonzero_delta=0
    row_defect_examples=0
    equal_bound_cases=0
    for row0 in itertools.product(opts,repeat=3):
        for row1 in itertools.product(opts,repeat=3):
            V={0:dict(zip(X,row0)),1:dict(zip(X,row1))}
            s={b:{x:sum(V[b][x]) for x in X} for b in (0,1)}
            D={x:sum(W[b]*sum((V[b][x][y]-V[b][R[C[x]]][y])**2 for y in Y)
                     for b in (0,1)) for x in X}
            count +=1
            for m in (1,2):
                for xs in itertools.product(X,repeat=m):
                    rs=tuple(R[C[x]] for x in xs)
                    delta=0
                    for ys in itertools.product(Y,repeat=m):
                        val=sum(W[b]*prod(V[b][x][y] for x,y in zip(xs,ys)) for b in (0,1))
                        ref=sum(W[b]*prod(V[b][r][y] for r,y in zip(rs,ys)) for b in (0,1))
                        delta += abs(val-ref)
                    upper=0
                    for i,x in enumerate(xs):
                        sigma=sum(W[b]*prod(s[b][r] for r in rs[:i])**2*
                                  prod(s[b][xj] for xj in xs[i+1:])**2 for b in (0,1))
                        upper += isqrt(len(Y)*D[x]*sigma)
                    mass=sum(W[b]*prod(s[b][x] for x in xs) for b in (0,1))
                    massref=sum(W[b]*prod(s[b][r] for r in rs) for b in (0,1))
                    assert abs(mass-massref)<=delta<=upper,(V,xs,delta,upper,mass,massref)
                    tuples+=1
                    target_entries+=len(Y)**m
                    if delta:
                        nonzero_delta += 1
                    if mass != massref:
                        row_defect_examples += 1
                    if delta==upper and delta:
                        equal_bound_cases += 1
    return dict(configurations=count,source_tuples=tuples,target_row_evaluations=target_entries,
                nonzero_row_residual_instances=nonzero_delta,
                nonzero_row_mass_defect_instances=row_defect_examples,
                nontrivial_bound_equality_instances=equal_bound_cases)


def paths_true(V,initial,t):
    cur={((),initial):1}
    for _ in range(t):
        nxt=defaultdict(int)
        for (word,x),n in cur.items():
            for z,v in V.get(x,{}).items():
                if v: nxt[(word+(C[z],),z)]+=n*v
        cur=nxt
    sums=defaultdict(int)
    for (word,x),n in cur.items():sums[word]+=n
    return dict(sums)


def paths_quotient(V,initial_y,t):
    cur={((),initial_y):1}
    for _ in range(t):
        nxt=defaultdict(int)
        for (word,y),n in cur.items():
            r=R[y]
            for z,v in V.get(r,{}).items():
                if v:nxt[(word+(C[z],),C[z])]+=n*v
        cur=nxt
    sums=defaultdict(int)
    for (word,y),n in cur.items():sums[word]+=n
    return dict(sums)


def finite_time_check():
    # Mass-varying source example: X 0=r, 1=x, 2=c.
    # True x self-loops 2x. Representative r splits one path to r and c.
    # c carries three self-loops; each step expands positive integer paths.
    V={0:{0:1,2:1},1:{1:2},2:{2:3}}
    rows={x:(sum(v for z,v in V[x].items() if C[z]==0),
             sum(v for z,v in V[x].items() if C[z]==1)) for x in X}
    delta=max(sum(abs(a-b) for a,b in zip(rows[x],rows[R[C[x]]])) for x in X)
    Rmax=max(sum(z.values()) for z in V.values())
    Rbar=max(sum(V[R[y]].values()) for y in Y)
    assert (delta,Rmax,Rbar)==(2,3,3)
    obs=[]
    for t in range(1,9):
        p=paths_true(V,1,t)
        q=paths_quotient(V,0,t)
        E=sum(abs(p.get(w,0)-q.get(w,0)) for w in set(p)|set(q))
        upper=delta*sum(Rmax**(t-1-j)*Rbar**j for j in range(t))
        assert E<=upper
        obs.append({"t":t,"l1_integer_history_error":E,"upper_integer":upper,
                    "true_integer_total":sum(p.values()),"quotient_integer_total":sum(q.values())})
    return {"delta":delta,"Rmax":Rmax,"Rbar":Rbar,"checks":obs}


def sharp_singleton():
    # A singleton observer hides variable source multiplicity entirely.
    # x has 2 distinct same-observation self-loop paths, r has 1.
    # R=2, Rbar=1, delta=1: the geometric sum is exactly 2**t-1.
    obs=[]
    for t in range(1,10):
        true_mass=2**t
        ref_mass=1
        err=true_mass-ref_mass
        upper=sum(2**(t-1-j) for j in range(t))
        assert err==upper
        obs.append({"t":t,"original_count":true_mass,"quotient_count":ref_mass,
                    "exact_integer_l1_error":err,"bound":upper})
    return {"delta":1,"Rmax":2,"Rbar":1,"checks":obs}


if __name__=='__main__':
    out={"status":"PASS","type":"AUTHOR_EXACT_INTEGER_CHECK","date":"2026-10-30",
         "scope":"nonnormalized positive-integer conditional-private-branch BRC; auxiliary, not native X6",
         "exhaustive_unequal_masses":run_all_rows(),
         "nonuniform_multistate_history":finite_time_check(),
         "sharp_singleton_history":sharp_singleton(),
         "generality":"Theorems follow from tensor-product telescoping and positive-operator recurrence; enumeration only checks stated finite cases."}
    print(json.dumps(out,indent=2,ensure_ascii=False))
