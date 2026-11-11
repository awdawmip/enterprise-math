#!/usr/bin/env python3
"""R714: exact six-axis Boolean triad degree fibers and local trade connectivity.
Uses integer operations only; no external packages. ~1m exact source states.
"""
import itertools
import json
from array import array
from collections import Counter, defaultdict

V=range(6)
TRI=list(itertools.combinations(V,3))
PAIR=list(itertools.combinations(V,2))
T={x:i for i,x in enumerate(TRI)}
E={x:i for i,x in enumerate(PAIR)}
WEIGHT=[sum(5**E[p] for p in itertools.combinations(t,2)) for t in TRI]
N=1<<20

def ledger(b):
    return sum(WEIGHT[i] for i in range(20) if b>>i&1)

def walk_states():
    """Gray order bijects onto all 2^20 states; update exact base-5 ledger."""
    old=0;degree=0
    for k in range(N):
        b=k^(k>>1)
        if k:
            q=(b^old).bit_length()-1
            degree += WEIGHT[q] if (b>>q)&1 else -WEIGHT[q]
        old=b
        yield b,degree

pasch=[]
for idx in itertools.combinations(range(20),4):
    quartet=[TRI[i] for i in idx]
    pe=Counter(p for t in quartet for p in itertools.combinations(t,2))
    vd=Counter(x for t in quartet for x in t)
    if len(pe)!=12 or any(v!=1 for v in pe.values()):continue
    if len(vd)!=6 or any(v!=2 for v in vd.values()):continue
    missing=set(PAIR)-set(pe)
    if len(missing)!=3 or len({x for p in missing for x in p})!=6:continue
    eligible={i for i,t in enumerate(TRI) if not any(p in missing for p in itertools.combinations(t,2))}
    other=eligible-set(idx)
    if len(eligible)!=8 or len(other)!=4:continue
    a=sum(1<<i for i in idx);b=sum(1<<i for i in other)
    if a<b:pasch.append((a,b))
assert len(pasch)==15 and all(ledger(a)==ledger(b) for a,b in pasch)

parent=array('i',range(N))
def root(a):
    while parent[a]!=a:
        parent[a]=parent[parent[a]];a=parent[a]
    return a

def union(a,b):
    a=root(a);b=root(b)
    if a!=b:parent[b]=a

def apply_trades(trades):
    edge_count=0
    for p,q in trades:
        assert not p&q and ledger(p)==ledger(q)
        rem=[1<<i for i in range(20) if not (p|q)>>i&1]
        x=0
        for k in range(1<<len(rem)):
            if k:x^=rem[(k&-k).bit_length()-1]
            union(x|p,x|q)
            edge_count+=1
    return edge_count

pasch_edges=apply_trades(pasch)
first={};size=Counter();components=defaultdict(set)
for b,deg in walk_states():
    if deg not in first:first[deg]=b
    size[deg]+=1
    components[deg].add(root(b))

fibers=len(first)
hist=Counter(size.values())
disconnected=[deg for deg,cs in components.items() if len(cs)>1]
disconnected_hist=Counter(first[deg].bit_count() for deg in disconnected)
assert fibers==995085 and len(disconnected)==240
assert Counter((len(components[d]),size[d]) for d in disconnected)=={(2,2):240}

# Identify the 15 primitive 6+6 obstructions by independent Gray scan.
base={deg:[first[deg]] for deg in disconnected if first[deg].bit_count()==6}
for b,deg in walk_states():
    if deg in base and b!=base[deg][0]:base[deg].append(b)
assert len(base)==15 and all(len(t)==2 for t in base.values())
extra=[]
for a,b in base.values():
    assert not a&b and a.bit_count()==b.bit_count()==6 and ledger(a)==ledger(b)
    extra.append((a,b))
extra_edges=apply_trades(extra)

# Verify connectivity of every fiber under all 30 move types.
remaining=set()
for b,deg in walk_states():
    if root(b)!=root(first[deg]):remaining.add(deg)
assert not remaining

# Exact rational rank of the 15x20 incidence matrix (fraction-free elimination).
mat=[[int(E[p] in [E[z] for z in itertools.combinations(t,2)]) for t in TRI] for p in PAIR]
rank=0
for col in range(20):
    pivot=next((r for r in range(rank,15) if mat[r][col]),None)
    if pivot is None:continue
    mat[rank],mat[pivot]=mat[pivot],mat[rank]
    for r in range(15):
        if r!=rank and mat[r][col]:
            a,b=mat[r][col],mat[rank][col]
            mat[r]=[b*mat[r][c]-a*mat[rank][c] for c in range(20)]
    rank+=1
    if rank==15:break
assert rank==15

wA,wB=extra[0]
result={
  'verdict':'R714_BRC_PAIR_DEGREE_MARKOV_BASIS_EXACT_PASS',
  'domain':'All 2^20 Boolean triad sets on labeled X6 axes; abstract pair-incidence model',
  'states':N,'pair_coordinates':15,'triad_coordinates':20,
  'rational_incidence_rank':rank,'rational_kernel_dimension':20-rank,
  'distinct_pair_degree_fibers':fibers,
  'fiber_size_histogram':{str(k):hist[k] for k in sorted(hist)},
  'largest_fiber':max(size.values()),
  'pasch_4_to_4_move_types':len(pasch),'pasch_edges':pasch_edges,
  'fibers_disconnected_with_only_pasch':len(disconnected),
  'disconnected_fiber_size_histogram':{str(k):disconnected_hist[k] for k in sorted(disconnected_hist)},
  'additional_6_to_6_move_types':len(extra),'additional_move_edges':extra_edges,
  'fibers_disconnected_after_combined_moves':len(remaining),
  'sample_6_to_6_A':[list(TRI[i]) for i in range(20) if wA>>i&1],
  'sample_6_to_6_B':[list(TRI[i]) for i in range(20) if wB>>i&1],
  'limits':'Finite census certifies six-axis Boolean fibers and moves, not native V29/V39 event validity or canonical admission.'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
