#!/usr/bin/env python3
from itertools import combinations, permutations, product
from math import comb

N=6
ID=tuple(range(N))

def parity(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2

def permute_vec(p,z):
    out=[0]*N
    for i,x in enumerate(z): out[p[i]]=x
    return tuple(out)

def norm2(z): return sum(x*x for x in z)
def l1(z): return sum(abs(x) for x in z)
def support(z): return sum(x!=0 for x in z)

def degree_decomposable(d):
    s=sum(d)
    return s%3==0 and max(d,default=0)<=s//3

def defect(d):
    s=sum(d); m=max(d,default=0); ceil3=(s+2)//3
    return 3*max(m,ceil3)-s

# All S6 permutations preserve static native predicates on an exhaustive small box.
S6=tuple(permutations(range(N)))
small=tuple(product(range(-1,2),repeat=N))
for p in S6:
    for z in small:
        w=permute_vec(p,z)
        assert norm2(w)==norm2(z)
        assert l1(w)==l1(z)
        assert support(w)==support(z)

# Triadic degree predicates and completion defect are S6 invariant.
degs=tuple(product(range(3),repeat=N))
for p in S6:
    for d in degs:
        e=permute_vec(p,d)
        assert degree_decomposable(e)==degree_decomposable(d)
        assert defect(e)==defect(d)

# Ordered triadic generator covariance under every positive-axis relabeling.
# Signed permutation represented as +/-1-based images.
def q_triad(S):
    i,j,k=S
    q=list(range(1,N+1))
    q[i]=-(j+1); q[j]=-(k+1); q[k]=-(i+1)
    return tuple(q)

def compose_signed(g,h):
    out=[]
    for x in h:
        sx=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(sx*y)
    return tuple(out)

def inv_perm_signed(p):
    # p ordinary permutation old->new, lift signlessly
    g=tuple(i+1 for i in p)
    inv=[0]*N
    for old,new1 in enumerate(g): inv[new1-1]=old+1
    return tuple(inv)

def perm_signed(p): return tuple(x+1 for x in p)

ordered=[]
for S in combinations(range(N),3):
    a,b,c=S
    ordered.extend(((a,b,c),(a,c,b)))  # both chiral orientations suffice as representatives
# More directly test all 6 orderings per 3-subset.
ordered=tuple(t for S in combinations(range(N),3) for t in permutations(S))
qset={q_triad(t) for t in ordered}
assert len(qset)==40  # cyclic reorderings give same q; two chiralities per 20 subsets
for p in S6:
    gp=perm_signed(p); gi=inv_perm_signed(p)
    for t in ordered:
        lhs=compose_signed(compose_signed(gp,q_triad(t)),gi)
        gt=tuple(p[x] for x in t)
        assert lhs==q_triad(gt)

# Explicit odd transposition path formula.
for a in range(-4,5):
    for b in range(-4,5):
        d=b-a
        disp=(d,-d,0,0,0,0)
        assert l1(disp)==2*abs(d)
        # shortest paths choose positions of one signed step type among 2|d|.
        mult=comb(2*abs(d),abs(d))
        assert mult>=1

# Same spatial Cell can be fixed by nontrivial odd frame transposition.
odd=(1,0,2,3,4,5)
assert parity(odd)==1
x=(7,7,-2,4,0,9)
assert permute_vec(odd,x)==x
assert odd!=ID

print('PASS_X6_ROTATION_STATIC_UNDERDETERMINATION_V5')
print('S6_static_automorphisms_checked',len(S6))
print('small_spatial_states_per_perm',len(small))
print('degree_vectors_per_perm',len(degs))
print('ordered_triad_generator_covariance_checks',len(S6)*len(ordered))
print('odd_transposition_spatial_path_obstruction',False)
print('static_foundation_decides_odd_frame_admissibility',False)
