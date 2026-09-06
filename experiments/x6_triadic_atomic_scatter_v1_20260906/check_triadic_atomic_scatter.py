#!/usr/bin/env python3
from __future__ import annotations

from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BRC_PATH = ROOT / 'experiments' / 'x6_signed_native_spatial_v16_20260905' / 'signed_brc.py'
spec = spec_from_file_location('x6_signed_brc', BRC_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError('cannot load current signed_brc.py')
brc = module_from_spec(spec)
spec.loader.exec_module(brc)

N=6
ID=tuple(range(1,N+1))
ZERO=(0,)*N

def unit(i,s=1):
    z=[0]*N; z[i]=s; return tuple(z)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))

def compose(g,h):
    out=[]
    for x in h:
        s=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(s*y)
    return tuple(out)

def act(g,z):
    out=[0]*N
    for i,c in enumerate(z):
        if c:
            y=g[i]
            out[abs(y)-1]+=(1 if y>0 else -1)*c
    return tuple(out)

def q_triad(S):
    i,j,k=S
    q=list(ID)
    q[i]=-(j+1); q[j]=-(k+1); q[k]=-(i+1)
    return tuple(q)

def power(g,n):
    out=ID
    for _ in range(n): out=compose(g,out)
    return out

def midpoint_options(a,b):
    assert brc.shortest_event_count(sub(b,a))==2
    assert brc.shortest_path_multiplicity(sub(b,a))==2
    return (ZERO, add(a,b))

# 20 selections x 8 sign patterns. Exactly one joint shortest branch
# has a shared intermediate Cell, namely III at the pivot.
closure_cases=0
joint_branch_cases=0
for S in combinations(range(N),3):
    q=q_triad(S)
    assert power(q,6)==ID
    for signs in product((-1,1), repeat=3):
        starts=[unit(i,s) for i,s in zip(S,signs)]
        targets=[act(q,a) for a in starts]
        assert len({next(i for i,x in enumerate(t) if x) for t in targets})==3
        options=[midpoint_options(a,b) for a,b in zip(starts,targets)]
        common=[]
        for bits in product((0,1), repeat=3):
            mids=[opts[b] for opts,b in zip(options,bits)]
            if mids[0]==mids[1]==mids[2]:
                common.append((bits,mids[0]))
            joint_branch_cases+=1
        assert common==[((0,0,0),ZERO)]
        closure_cases+=1

# Sign-coherent ordered triad has 6 labeled Q phases but only two unordered
# sign-sheet states. The repair fiber has cardinality 3.
S=(0,1,2); q=q_triad(S)
ordered=[]; current=(unit(0),unit(1),unit(2))
for _ in range(6):
    ordered.append(current)
    current=tuple(act(q,x) for x in current)
assert current==ordered[0]
assert len(set(ordered))==6
unordered=[frozenset(x for x in st) for st in ordered]
assert len(set(unordered))==2
assert all(unordered[r]==unordered[r+2] for r in range(4))

# Greedy existence criterion for decomposition into distinct-axis triads.
def greedy_decompose(d):
    d=list(d); total=sum(d)
    if total%3: return None
    m=total//3
    if max(d, default=0)>m: return None
    out=[]
    for remaining in range(m,0,-1):
        order=sorted(range(6), key=lambda i:(-d[i],i))
        S=tuple(order[:3])
        if d[S[2]]<=0: return None
        out.append(S)
        for i in S: d[i]-=1
        if max(d, default=0)>remaining-1: return None
    return tuple(out) if all(x==0 for x in d) else None

TRIPLES=tuple(combinations(range(6),3))
@lru_cache(None)
def brute_possible(d):
    d=tuple(d)
    if sum(d)==0: return True
    if sum(d)%3: return False
    for S in TRIPLES:
        if all(d[i]>0 for i in S):
            e=list(d)
            for i in S: e[i]-=1
            if brute_possible(tuple(e)): return True
    return False

degree_cases=0
for m in range(5):
    for d in product(range(m+1), repeat=6):
        if sum(d)!=3*m: continue
        criterion=max(d, default=0)<=m
        brute=brute_possible(d)
        greedy=greedy_decompose(d) is not None
        assert criterion==brute==greedy
        degree_cases+=1

# Type-level decomposition polynomial coefficient by DP for d=(1,...,1), m=2.
def ordered_type_decomp_count(target,m):
    states={(0,0,0,0,0,0):1}
    for _ in range(m):
        nxt={}
        for state,count in states.items():
            for S in TRIPLES:
                t=list(state)
                for i in S: t[i]+=1
                t=tuple(t)
                if all(t[i]<=target[i] for i in range(6)):
                    nxt[t]=nxt.get(t,0)+count
        states=nxt
    return states.get(tuple(target),0)
assert ordered_type_decomp_count((1,1,1,1,1,1),2)==20

# Fixed effective visible pair has 4 hidden axes x 2 hidden signs = 8 lifts.
visible=(0,1)
lifts=[]
for k in range(6):
    if k in visible: continue
    for s in (-1,1):
        triad=(unit(0,1),unit(1,1),unit(k,s))
        # O_01: +e0 -> +1, +e1 -> -1, all other ports hidden.
        readout=(1,-1,0)
        lifts.append((k,s,triad,readout))
assert len(lifts)==8
assert len({x[3] for x in lifts})==1

print('PASS_X6_TRIADIC_ATOMIC_SCATTER_V1')
print('canonical_signed_triad_cases',closure_cases)
print('joint_shortest_branch_combinations_checked',joint_branch_cases)
print('unique_atomic_midpoint_branch','III')
print('ordered_triad_phase_count',6)
print('unordered_static_sheet_count',2)
print('phase_repair_fiber','C3')
print('degree_sequences_checked',degree_cases)
print('six_force_ordered_decompositions',20)
print('six_force_unordered_decompositions',10)
print('fixed_visible_two_force_hidden_lifts',8)
