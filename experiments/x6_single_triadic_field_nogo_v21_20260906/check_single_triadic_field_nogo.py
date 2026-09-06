#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from fractions import Fraction

V=tuple(range(6))
TRIPLES=tuple(combinations(V,3))
TI={S:i for i,S in enumerate(TRIPLES)}


def adjacent(S,T): return len(set(S)&set(T))==2

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
    v=[0]*20;plus=[];minus=[]
    for bits in product((0,1),repeat=3):
        S=tuple(sorted(M[r][bits[r]] for r in range(3)))
        idx=TI[S]
        if sum(bits)%2==0:
            v[idx]+=1;plus.append(idx)
        else:
            v[idx]-=1;minus.append(idx)
    return tuple(v),tuple(plus),tuple(minus)
TRADES=[trade(M) for M in MATCH]
F=[[sum(v[i]*v[j] for v,_,__ in TRADES) for j in range(20)] for i in range(20)]


def mv(M,x):return tuple(sum(M[i][j]*x[j] for j in range(len(x))) for i in range(len(M)))
def permute_vec(x,p):
    out=[0]*20
    for i,S in enumerate(TRIPLES):
        image=tuple(sorted(p[a] for a in S))
        out[TI[image]]=x[i]
    return tuple(out)
def image_tri(S,p):return tuple(sorted(p[i] for i in S))

# Canonical matching/oriented branch field h=F n_+ =12v.
M=MATCH[0]
v,plus,minus=TRADES[0]
np=tuple(1 if i in plus else 0 for i in range(20))
h=mv(F,np)
assert h==tuple(12*x for x in v)
assert Counter(h)==Counter({0:12,12:4,-12:4})

S6=tuple(permutations(V))
H=tuple(p for p in S6 if permute_vec(h,p)==h)
assert len(H)==24

# H-orbits on active triads are exactly 12 zero,4 positive,4 negative.
unseen=set(TRIPLES);orbits=[]
while unseen:
    S=next(iter(unseen))
    orb={image_tri(S,p) for p in H}
    orbits.append((frozenset(orb),h[TI[S]]))
    unseen-=orb
assert sorted((len(o),score) for o,score in orbits)==[(4,-12),(4,12),(12,0)]

# Stabilizer fixed-neighbor criterion and exact max-score tie counts.
fixed_counts=Counter();max_ties=Counter()
for S in TRIPLES:
    HS=tuple(p for p in H if image_tri(S,p)==S)
    neigh=tuple(T for T in TRIPLES if adjacent(S,T))
    fixed=tuple(T for T in neigh if all(image_tri(T,p)==T for p in HS))
    fixed_counts[(h[TI[S]],len(HS),len(fixed))]+=1
    mx=max(h[TI[T]] for T in neigh)
    ties=sum(h[TI[T]]==mx for T in neigh)
    max_ties[(h[TI[S]],mx,ties)]+=1
    if h[TI[S]]!=0:
        assert len(HS)==6 and len(fixed)==0
    else:
        assert len(HS)==2 and len(fixed)==1
        # zero-state triad contains exactly one complete matching pair; fixed
        # neighbour flips its singleton to the matched partner.
        T=fixed[0]
        full=[pair for pair in M if set(pair).issubset(S)]
        assert len(full)==1
        singleton=next(x for x in S if x not in full[0])
        singleton_pair=next(pair for pair in M if singleton in pair)
        partner=next(x for x in singleton_pair if x!=singleton)
        expected=tuple(sorted(set(full[0])|{partner}))
        assert T==expected
assert fixed_counts==Counter({(0,2,1):12,(12,6,0):4,(-12,6,0):4})
assert max_ties==Counter({(0,12,2):12,(12,0,6):4,(-12,12,3):4})

# Transversal cube and flat square faces.
transversals={S for S in TRIPLES if h[TI[S]]!=0}
assert len(transversals)==8
assert all(sum(1 for T in transversals if adjacent(S,T))==3 for S in transversals)

def repl(S,T):
    shared=set(S)&set(T)
    leaving=next(x for x in S if x not in shared)
    entering=next(x for x in T if x not in shared)
    return {x:(x if x in shared else entering) for x in S}
def compose_maps(f,g):return {x:f[g[x]] for x in g}
def hol(loop):
    hh={x:x for x in loop[0]}
    for S,T in zip(loop,loop[1:]): hh=compose_maps(repl(S,T),hh)
    return hh
def parity_hol(hh,S):
    p=tuple(S.index(hh[x]) for x in S)
    return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

# Every induced 4-cycle in the transversal cube is flat.
cycles=set()
for a,b,c,d in permutations(transversals,4):
    if adjacent(a,b) and adjacent(b,c) and adjacent(c,d) and adjacent(d,a) and not adjacent(a,c) and not adjacent(b,d):
        cyc=(a,b,c,d)
        # canonicalize under rotations/reversal
        reps=[]
        for seq in (cyc,tuple(reversed(cyc))):
            for r in range(4):reps.append(seq[r:]+seq[:r])
        cycles.add(min(reps))
assert len(cycles)==6
for cyc in cycles:
    loop=cyc+(cyc[0],)
    hh=hol(loop)
    assert all(hh[x]==x for x in cyc[0])

# Simple-triangle flat/curved score distributions are identical.
triangles=tuple(tri for tri in combinations(TRIPLES,3) if all(adjacent(a,b) for a,b in combinations(tri,2)))
dist=defaultdict(Counter)
for tri in triangles:
    hh=hol(tri+(tri[0],))
    par=parity_hol(hh,tri[0])
    score=sum(h[TI[S]] for S in tri)
    dist[par][score]+=1
assert dist[0]==Counter({0:36,12:12,-12:12})
assert dist[1]==Counter({0:36,12:12,-12:12})

# Exact rational mass equality for several rho values.
for rho in (Fraction(2),Fraction(3,2),Fraction(5,7)):
    z0=sum(Fraction(count)*rho**score for score,count in dist[0].items())
    z1=sum(Fraction(count)*rho**score for score,count in dist[1].items())
    assert z0==z1

print('PASS_X6_SINGLE_TRIADIC_FIELD_NOGO_V21')
print('field_stabilizer_order',len(H))
print('active_triad_orbits',sorted((len(o),score) for o,score in orbits))
print('transversal_fixed_neighbor_exists',False)
print('zero_boundary_unique_fixed_neighbor',True)
print('max_score_tie_types',sorted(max_ties.items()))
print('transversal_cube_square_cycles',len(cycles))
print('flat_curved_triangle_score_distributions_equal',True)
print('one_field_total_deterministic_equivariant_update',False)
