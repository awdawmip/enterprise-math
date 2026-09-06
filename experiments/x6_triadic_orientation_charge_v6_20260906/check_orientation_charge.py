#!/usr/bin/env python3
from itertools import combinations, permutations, product

N=6
ID=tuple(range(N))

def parity(p):
    return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2

def compose(p,q): return tuple(p[q[i]] for i in range(N))

# Orientation torsor = S6/A6 has exactly two parity classes.
S6=tuple(permutations(range(N)))
classes={0:[],1:[]}
for p in S6: classes[parity(p)].append(p)
assert len(classes[0])==360 and len(classes[1])==360

# Every triadic generator's positive-axis projection is a 3-cycle, hence even.
triadic=[]
for S in combinations(range(N),3):
    for t in (S,(S[0],S[2],S[1])):
        a,b,c=t
        p=list(ID); p[a]=b; p[b]=c; p[c]=a
        triadic.append(tuple(p))
assert len(triadic)==40
assert all(parity(p)==0 for p in triadic)

# Serial event orientation increment is additive mod 2.
for p,q in product(S6[:40],S6[-40:]):
    assert parity(compose(p,q))==(parity(p)+parity(q))%2

# Triadic words remain in even sector.
state=ID
for g in triadic[:20]:
    state=compose(g,state)
    assert parity(state)==0

# Any odd event flips sector; two odd events restore it.
odd=next(p for p in S6 if parity(p)==1)
even=next(p for p in S6 if parity(p)==0 and p!=ID)
assert parity(odd)==1
assert parity(compose(odd,even))==1
assert parity(compose(odd,odd))==0

# Independent-event serialization has same C2 total charge because addition mod2 commutes.
sample=(odd,even,odd)
charges=set()
for order in permutations(range(3)):
    x=ID
    for i in order: x=compose(sample[i],x)
    charges.add(parity(x))
assert charges=={0}

print('PASS_X6_TRIADIC_ORIENTATION_CHARGE_V6')
print('orientation_sectors',2)
print('frames_per_orientation_sector',360)
print('triadic_positive_axis_generators_checked',len(triadic))
print('triadic_orientation_charge',0)
print('odd_frame_orientation_charge',1)
print('dependency_serialization_changes_charge',False)
