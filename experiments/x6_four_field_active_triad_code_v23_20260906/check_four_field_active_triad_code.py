#!/usr/bin/env python3
from itertools import combinations, product

V=tuple(range(6))
TRIPLES=tuple(combinations(V,3))
TI={S:i for i,S in enumerate(TRIPLES)}


def matchings(items):
    items=tuple(items)
    if not items:
        yield ();return
    a=items[0]
    for q in range(1,len(items)):
        b=items[q]
        rest=items[1:q]+items[q+1:]
        for tail in matchings(rest):
            yield tuple(sorted(((min(a,b),max(a,b)),)+tail))
MATCH=tuple(sorted(set(matchings(V))))
assert len(MATCH)==15


def trade(M):
    v=[0]*20
    for bits in product((0,1),repeat=3):
        S=tuple(sorted(M[r][bits[r]] for r in range(3)))
        v[TI[S]] += 1 if sum(bits)%2==0 else -1
    return tuple(v)

FIELDS=[];META=[]
for mi,M in enumerate(MATCH):
    v=trade(M)
    for sign in (1,-1):
        FIELDS.append(tuple(sign*x for x in v));META.append((mi,sign))
assert len(FIELDS)==30


def code(inds,S):return tuple(FIELDS[i][TI[S]] for i in inds)
def injective(inds):return len({code(inds,S) for S in TRIPLES})==20

counts={}
examples={}
for r in range(1,5):
    c=0;ex=None
    for inds in combinations(range(30),r):
        if injective(inds):
            c+=1
            if ex is None:ex=inds
    counts[r]=c;examples[r]=ex
assert counts=={1:0,2:0,3:0,4:480}

# Explicit positive fields from matching indices M0,M4,M8,M10.
# FIELDS ordering is (+v_M,-v_M), hence indices 2*mi.
inds=(0,8,16,20)
assert [META[i] for i in inds]==[(0,1),(4,1),(8,1),(10,1)]
assert injective(inds)

TABLE={S:code(inds,S) for S in TRIPLES}
assert len(set(TABLE.values()))==20
assert TABLE[(0,1,2)]==(0,0,1,1)
assert TABLE[(0,2,4)]==(1,0,0,0)
assert TABLE[(1,3,5)]==(-1,0,0,0)
assert TABLE[(2,3,5)]==(0,0,1,0)
assert TABLE[(3,4,5)]==(0,0,-1,-1)

# Exact inverse lookup.
DECODE={sig:S for S,sig in TABLE.items()}
assert len(DECODE)==20
for S in TRIPLES:assert DECODE[TABLE[S]]==S

# Code is identity-separating but not one-error correcting.
def hamming(a,b):return sum(x!=y for x,y in zip(a,b))
def l1(a,b):return sum(abs(x-y) for x,y in zip(a,b))
min_h=min(hamming(TABLE[S],TABLE[T]) for S,T in combinations(TRIPLES,2))
min_l1=min(l1(TABLE[S],TABLE[T]) for S,T in combinations(TRIPLES,2))
assert min_h==1 and min_l1==1

# Every injective four-field code has trivial pointwise S6 stabilizer: if a
# permutation fixed each field then it would preserve all codewords, and
# injectivity forces it to fix all 20 triads. We verify directly for the example.
from itertools import permutations

def permute_field(f,p):
    out=[0]*20
    for idx,S in enumerate(TRIPLES):
        image=tuple(sorted(p[x] for x in S))
        out[TI[image]]=f[idx]
    return tuple(out)
S6=tuple(permutations(V))
stab=[p for p in S6 if all(permute_field(FIELDS[i],p)==FIELDS[i] for i in inds)]
assert stab==[tuple(V)]

print('PASS_X6_FOUR_FIELD_ACTIVE_TRIAD_CODE_V23')
print('injective_field_set_counts',counts)
print('minimum_fields_for_20_triad_evaluation_code',4)
print('injective_four_field_sets',counts[4])
print('explicit_field_meta',[META[i] for i in inds])
print('codeword_count',len(DECODE))
print('minimum_hamming_distance',min_h)
print('minimum_l1_distance',min_l1)
print('example_pointwise_S6_stabilizer_order',len(stab))
