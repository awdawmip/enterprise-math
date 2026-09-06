#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations, product

V=tuple(range(6))
TRIPLES=tuple(combinations(V,3))
TI={S:i for i,S in enumerate(TRIPLES)}
S6=tuple(permutations(V))


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


def permute_vec(x,p):
    out=[0]*20
    for i,S in enumerate(TRIPLES):
        image=tuple(sorted(p[a] for a in S))
        out[TI[image]]=x[i]
    return tuple(out)

FIELDS=[];META=[]
for mi,M in enumerate(MATCH):
    v=trade(M)
    for sign in (1,-1):
        FIELDS.append(tuple(sign*x for x in v));META.append((mi,sign))
assert len(FIELDS)==30 and len(set(FIELDS))==30

# One S6 orbit of size 30; every point stabilizer has order 24.
base=FIELDS[0]
orbit={permute_vec(base,p) for p in S6}
assert orbit==set(FIELDS)
STABS=[]
for h in FIELDS:
    st=frozenset(p for p in S6 if permute_vec(h,p)==h)
    assert len(st)==24
    STABS.append(st)

ID=tuple(V)
def compose(p,q):return tuple(p[q[i]] for i in V)
def order(p):
    x=ID
    for k in range(1,13):
        x=compose(p,x)
        if x==ID:return k
    raise AssertionError

# Two-field intersection census; nontrivial in every case.
pair_census=Counter(); pair_group_types=Counter()
for i,j in combinations(range(30),2):
    H=STABS[i]&STABS[j]
    pair_census[len(H)]+=1
    ords=Counter(order(p) for p in H)
    if len(H)==3:
        assert ords==Counter({3:2,1:1});pair_group_types['C3']+=1
    elif len(H)==4:
        assert ords==Counter({2:3,1:1});pair_group_types['V4']+=1
    elif len(H)==24:
        # Must be opposite orientations of same matching.
        assert META[i][0]==META[j][0] and META[i][1]==-META[j][1]
    else:
        raise AssertionError(H)
assert pair_census==Counter({3:240,4:180,24:15})
assert pair_group_types==Counter({'C3':240,'V4':180})

# Three-field census: trivial stabilizers appear for the first time.
triple_census=Counter(); free=[]
for inds in combinations(range(30),3):
    H=STABS[inds[0]]&STABS[inds[1]]&STABS[inds[2]]
    triple_census[len(H)]+=1
    if len(H)==1: free.append(inds)
    elif len(H)==3:
        assert Counter(order(p) for p in H)==Counter({3:2,1:1})
    elif len(H)==4:
        assert Counter(order(p) for p in H)==Counter({2:3,1:1})
    else:raise AssertionError(H)
assert triple_census==Counter({1:3360,3:400,4:300})
assert len(free)==3360

# Explicit free triple M0+, M1+, M3+.
explicit=(0,2,6)
assert [META[i] for i in explicit]==[(0,1),(1,1),(3,1)]
H=STABS[explicit[0]]&STABS[explicit[1]]&STABS[explicit[2]]
assert H=={ID}
# Its labeled S6 orbit has size 720 exactly.
ref=tuple(FIELDS[i] for i in explicit)
orb={tuple(permute_vec(h,p) for h in ref) for p in S6}
assert len(orb)==720

print('PASS_X6_THREE_FIELD_RELATIONAL_FRAME_V22')
print('minimal_field_states',len(FIELDS))
print('single_field_stabilizer_order',24)
print('two_field_stabilizer_census',dict(sorted(pair_census.items())))
print('two_field_residual_group_types',dict(pair_group_types))
print('three_field_stabilizer_census',dict(sorted(triple_census.items())))
print('free_three_field_contexts',len(free))
print('minimum_labeled_fields_for_trivial_S6_stabilizer',3)
print('explicit_free_triple_meta',[META[i] for i in explicit])
print('free_triple_orbit_size',len(orb))
