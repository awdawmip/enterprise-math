#!/usr/bin/env python3
"""Exact complete signed-cycle / primitive-direction phase atlas for B6 and R_triad."""
from collections import Counter, defaultdict
from itertools import permutations, product
from math import factorial

N=6
IDP=tuple(range(N))

def parity(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2

def cycles(p):
    seen=set();out=[]
    for i in range(N):
        if i in seen: continue
        C=[];j=i
        while j not in seen:
            seen.add(j);C.append(j);j=p[j]
        out.append(tuple(C))
    return tuple(out)

def signature(p,eps):
    pos=[];neg=[]
    for C in cycles(p):
        h=1
        for i in C:h*=eps[i]
        (pos if h==1 else neg).append(len(C))
    return (tuple(sorted(pos,reverse=True)),tuple(sorted(neg,reverse=True)))

def dir_partition(sig):
    pos,neg=sig; out=[]
    for l in pos: out.extend((l,l))
    for l in neg: out.append(2*l)
    return tuple(sorted(out,reverse=True))

def ori_of_signature(sig):
    c=len(sig[0])+len(sig[1])
    return (N-c)%2

def centralizer_order(sig):
    z=1
    for side in sig:
        C=Counter(side)
        for l,m in C.items(): z*=(2*l)**m * factorial(m)
    return z

def splits_under_even(sig):
    pos,neg=sig
    if any(l%2==0 for l in pos+neg): return False
    return all(m==1 for side in sig for m in Counter(side).values())

# Enumerate all 46080 signed frames by positive permutation + source-axis signs.
sig_counts=Counter(); partition_by_ori={0:Counter(),1:Counter()}
for p in permutations(range(N)):
    po=parity(p)
    for eps in product((-1,1),repeat=N):
        sig=signature(p,eps)
        assert ori_of_signature(sig)==po
        sig_counts[sig]+=1
        partition_by_ori[po][dir_partition(sig)]+=1

assert sum(sig_counts.values())==46080
assert len(sig_counts)==65
for sig,count in sig_counts.items():
    assert count==46080//centralizer_order(sig)

split_sigs={sig for sig in sig_counts if splits_under_even(sig)}
assert len(split_sigs)==5
assert split_sigs=={
    ((5,1),()),
    ((5,),(1,)),
    ((1,),(5,)),
    ((),(5,1)),
    ((3,),(3,)),
}
# 65 full-B6 classes become 70 R_triad conjugacy classes: each split type adds one.
assert 65+len(split_sigs)==70

# Primitive-direction orbit lengths alone are a coarser observer: 40 partitions,
# with 18 appearing in both Ori6 sectors.
even_parts=set(partition_by_ori[0]); odd_parts=set(partition_by_ori[1])
assert len(even_parts)==31
assert len(odd_parts)==27
assert len(even_parts|odd_parts)==40
assert len(even_parts&odd_parts)==18

# Key examples.
assert partition_by_ori[0][(12,)]==0
assert partition_by_ori[1][(12,)]==3840
assert partition_by_ori[0][(6,6)]==640
assert partition_by_ori[1][(6,6)]==3840

# Verify full R_triad conjugacy orbit count directly using R = all signed frames
# whose underlying positive-axis permutation is even.
def signed(p,eps): return tuple(eps[i]*(p[i]+1) for i in range(N))
def compose(g,h):
    out=[]
    for x in h:
        s=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(s*y)
    return tuple(out)
def inv(g):
    out=[None]*N
    for i,y in enumerate(g): out[abs(y)-1]=(1 if y>0 else -1)*(i+1)
    return tuple(out)
def conj(h,g): return compose(compose(h,g),inv(h))
def sig_signed(g):
    p=tuple(abs(x)-1 for x in g);eps=tuple(1 if x>0 else -1 for x in g)
    return signature(p,eps)

B6={signed(p,eps) for p in permutations(range(N)) for eps in product((-1,1),repeat=N)}
R={signed(p,eps) for p in permutations(range(N)) if parity(p)==0 for eps in product((-1,1),repeat=N)}
assert len(B6)==46080 and len(R)==23040
unseen=set(B6); orbit_sig=defaultdict(list); orbit_count=0
while unseen:
    g=next(iter(unseen))
    orb={conj(r,g) for r in R}
    unseen-=orb
    orbit_sig[sig_signed(g)].append(len(orb));orbit_count+=1
assert orbit_count==70
for sig,ors in orbit_sig.items():
    assert len(ors)==(2 if sig in split_sigs else 1)
    if sig in split_sigs:
        assert ors[0]==ors[1]==sig_counts[sig]//2
    else:
        assert ors[0]==sig_counts[sig]

print('PASS_X6_SIGNED_CYCLE_ATLAS_V12')
print('B6_signed_cycle_types',len(sig_counts))
print('R_triad_conjugacy_orbits',orbit_count)
print('split_signed_cycle_types',len(split_sigs))
print('primitive_direction_orbit_partitions',len(even_parts|odd_parts))
print('partitions_shared_by_both_Ori6_sectors',len(even_parts&odd_parts))
print('global_C12_counts_even_odd',(partition_by_ori[0][(12,)],partition_by_ori[1][(12,)]))
print('C6_plus_C6_counts_even_odd',(partition_by_ori[0][(6,6)],partition_by_ori[1][(6,6)]))
