#!/usr/bin/env python3
"""Exact S3 dependency / parity-residual checks for X6 upper V40-V41."""
from itertools import permutations, product

S3=tuple(permutations((0,1,2)))
ID=(0,1,2)

def comp(p,q):
    # p after q
    return tuple(p[q[i]] for i in range(3))

def inv(p):
    out=[0]*3
    for i,x in enumerate(p): out[x]=i
    return tuple(out)

def parity(p):
    return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

def order(p):
    x=ID
    for n in range(1,7):
        x=comp(p,x)
        if x==ID:return n
    raise AssertionError

trans=tuple(p for p in S3 if parity(p)==1)
even=tuple(p for p in S3 if parity(p)==0)
cycles3=tuple(p for p in even if p!=ID)
assert len(trans)==3 and len(even)==3 and len(cycles3)==2
assert all(order(p)==2 for p in trans)
assert all(order(p)==3 for p in cycles3)

# Exact commutation classification.
commuting={(p,q) for p in S3 for q in S3 if comp(p,q)==comp(q,p)}
for p in S3:
    centralizer={q for q in S3 if (p,q) in commuting}
    if p==ID: assert len(centralizer)==6
    elif p in trans: assert centralizer=={ID,p}
    else: assert centralizer==set(even)

# V39 port updates commute iff holonomies commute; current coordinate additions
# are represented by arbitrary integer pairs and always commute.
def update(state,jp,hp):
    j,h=state
    return ((j[0]+jp[0],j[1]+jp[1]),comp(hp,h))

for hp,hq,h0 in product(S3,S3,S3):
    p=((2,-3),hp); q=((-5,7),hq); state=((11,13),h0)
    pq=update(update(state,p[0],p[1]),q[0],q[1])
    qp=update(update(state,q[0],q[1]),p[0],p[1])
    assert (pq==qp)==((hp,hq) in commuting)

# Odd-pair residual classification.
for a in trans:
    for b in trans:
        r=comp(b,a)  # execute a then b
        assert parity(r)==0
        if a==b:
            assert r==ID
        else:
            assert r in cycles3
            rr=comp(a,b)
            assert rr==inv(r) and rr!=r

# Concrete V37 packet pair.
hA=(0,2,1) # (12)
hB=(1,0,2) # (01)
assert hA in trans and hB in trans and hA!=hB
AB=comp(hB,hA)
BA=comp(hA,hB)
assert AB==(2,0,1)
assert BA==(1,2,0)
assert AB==inv(BA)
assert AB in cycles3 and BA in cycles3
assert parity(AB)==parity(BA)==0

# Commutator is nontrivial even element.
comm=comp(inv(hB),comp(inv(hA),comp(hB,hA)))
assert comm in cycles3

print('PASS_X6_HOLONOMY_DEPENDENCY_V40_V41')
print('S3_elements',len(S3))
print('commuting_ordered_pairs',len(commuting))
print('transpositions',trans)
print('even_kernel',even)
print('AB_residual',AB)
print('BA_residual',BA)
print('odd_plus_odd_parity',0)
print('distinct_odd_pair_full_memory_nontrivial',True)
