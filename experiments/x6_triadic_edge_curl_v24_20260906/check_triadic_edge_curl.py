#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

V=tuple(range(6))
TRIPLES=tuple(combinations(V,3))
TI={S:i for i,S in enumerate(TRIPLES)}
EDGES=tuple((TRIPLES[i],TRIPLES[j]) for i in range(20) for j in range(i+1,20) if len(set(TRIPLES[i])&set(TRIPLES[j]))==2)
assert len(EDGES)==90

# V18/V20 saturated K basis.
B=[
[0,0,0,0,-1], [0,0,0,-1,0], [0,0,-1,0,0], [0,0,1,1,1],
[0,-1,0,0,0], [-1,0,0,0,0], [1,1,0,0,1], [1,1,1,1,1],
[-1,0,-1,0,-1], [0,-1,0,-1,-1], [0,1,0,1,1], [1,0,1,0,1],
[-1,-1,-1,-1,-1], [-1,-1,0,0,-1], [1,0,0,0,0], [0,1,0,0,0],
[0,0,-1,-1,-1], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]
]
PIV=(14,15,17,18,19)


def image_tri(S,p):return tuple(sorted(p[i] for i in S))
def inverse_perm(p):
    q=[0]*6
    for i,j in enumerate(p):q[j]=i
    return tuple(q)
def action20(x,p):
    out=[0]*20
    for i,S in enumerate(TRIPLES):out[TI[image_tri(S,p)]]=x[i]
    return tuple(out)
def actionK(p):
    M=[[0]*5 for _ in range(5)]
    for c in range(5):
        x=tuple(B[r][c] for r in range(20))
        y=action20(x,p)
        co=tuple(y[r] for r in PIV)
        assert all(y[r]==sum(B[r][k]*co[k] for k in range(5)) for r in range(20))
        for r in range(5):M[r][c]=co[r]
    return M
def trace(M):return sum(M[i][i] for i in range(len(M)))
def compose_perm(p,q):return tuple(p[q[i]] for i in range(6))

S6=tuple(permutations(V))

# Antisymmetric edge character: fixed oriented edge contributes +1; endpoint swap -1.
def edge_char(p):
    ch=0
    for S,T in EDGES:
        U=image_tri(S,p);W=image_tri(T,p)
        if {U,W}=={S,T}:
            ch += 1 if (U==S and W==T) else -1
    return ch

sum_one=0;sum_wedge=0
for p in S6:
    ck=trace(actionK(p))
    ce=edge_char(p)
    p2=compose_perm(p,p)
    ck2=trace(actionK(p2))
    cwedge=(ck*ck-ck2)//2
    sum_one += ck*ce
    sum_wedge += cwedge*ce
mult_one=Fraction(sum_one,720)
mult_wedge=Fraction(sum_wedge,720)
assert mult_one==1
assert mult_wedge==1

# Minimal fields.
def matchings(items):
    items=tuple(items)
    if not items:
        yield ();return
    a=items[0]
    for q in range(1,len(items)):
        b=items[q]
        rest=items[1:q]+items[q+1:]
        for tail in matchings(rest):yield tuple(sorted(((min(a,b),max(a,b)),)+tail))
MATCH=tuple(sorted(set(matchings(V))))
def trade(M):
    v=[0]*20
    for bits in product((0,1),repeat=3):
        S=tuple(sorted(M[r][bits[r]] for r in range(3)))
        v[TI[S]] += 1 if sum(bits)%2==0 else -1
    return tuple(v)
FIELDS=[];META=[]
for mi,M in enumerate(MATCH):
    v=trade(M)
    for sg in (1,-1):FIELDS.append(tuple(sg*x for x in v));META.append((mi,sg))

# d h and Omega are equivariant; Omega has explicit nonzero curl.
def adjacent(S,T):return len(set(S)&set(T))==2
def dh(h,S,T):return h[TI[T]]-h[TI[S]]
def omega(h,k,S,T):return h[TI[S]]*k[TI[T]]-h[TI[T]]*k[TI[S]]
def circulation(form,tri):
    S,T,U=tri
    return form(S,T)+form(T,U)+form(U,S)

def repl(S,T):
    shared=set(S)&set(T)
    leaving=next(x for x in S if x not in shared)
    entering=next(x for x in T if x not in shared)
    return {x:(x if x in shared else entering) for x in S}
def compose_maps(f,g):return {x:f[g[x]] for x in g}
def hol(tri):
    S,T,U=tri
    return compose_maps(repl(U,S),compose_maps(repl(T,U),repl(S,T)))
def hol_parity(tri):
    S=tri[0];H=hol(tri)
    q=tuple(S.index(H[x]) for x in S)
    return sum(q[i]>q[j] for i in range(3) for j in range(i+1,3))%2

TRIANGLES=tuple(tri for tri in combinations(TRIPLES,3) if all(adjacent(a,b) for a,b in combinations(tri,2)))
assert len(TRIANGLES)==120

h=FIELDS[0] # M0+
k=FIELDS[2] # M1+
# every gradient circulation is zero
for tri in TRIANGLES:assert circulation(lambda S,T:dh(h,S,T),tri)==0
witness=((0,2,3),(0,2,4),(0,3,4))
assert witness in TRIANGLES
assert hol_parity(witness)==1
assert circulation(lambda S,T:omega(h,k,S,T),witness)==-3

# Equivariance of Omega on all adjacent edges for adjacent-transposition generators.
for a in range(5):
    p=list(V);p[a],p[a+1]=p[a+1],p[a];p=tuple(p)
    hp=action20(h,p);kp=action20(k,p)
    for S,T in EDGES:
        assert omega(hp,kp,image_tri(S,p),image_tri(T,p))==omega(h,k,S,T)

# Pair-context census: residual C3 type gives 36/36 nonzero flat/curved;
# V4 type gives 32/32. Opposite orientations of same matching have zero wedge.
field_stabs=[]
for f in FIELDS:
    field_stabs.append(frozenset(p for p in S6 if action20(f,p)==f))
census=Counter()
for i,j in combinations(range(30),2):
    h0,k0=FIELDS[i],FIELDS[j]
    if META[i][0]==META[j][0]:
        assert all(omega(h0,k0,S,T)==0 for S,T in EDGES)
        continue
    inter=len(field_stabs[i]&field_stabs[j])
    nonzero={0:0,1:0}
    for tri in TRIANGLES:
        c=circulation(lambda S,T,h0=h0,k0=k0:omega(h0,k0,S,T),tri)
        if c:nonzero[hol_parity(tri)]+=1
    if inter==3:assert nonzero=={0:36,1:36}
    elif inter==4:assert nonzero=={0:32,1:32}
    else:raise AssertionError(inter)
    census[(inter,nonzero[0],nonzero[1])]+=1
assert census==Counter({(3,36,36):240,(4,32,32):180})

# Directed rational loop ratio for witness: rho^(2 curl) = rho^-6.
for rho in (Fraction(2),Fraction(3,2),Fraction(5,7)):
    c=circulation(lambda S,T:omega(h,k,S,T),witness)
    forward=rho**c
    reverse=rho**(-c)
    assert forward/reverse==rho**(2*c)==rho**-6

# Explicit V23 balanced-ternary potential: all values distinct, greedy cycles only length 2.
inds=(0,8,16,20)
coeff=(1,3,9,27)
J={S:sum(c*FIELDS[i][TI[S]] for c,i in zip(coeff,inds)) for S in TRIPLES}
assert len(set(J.values()))==20
succ={}
for S in TRIPLES:
    neigh=[T for T in TRIPLES if adjacent(S,T)]
    mx=max(neigh,key=lambda T:J[T])
    assert sum(J[T]==J[mx] for T in neigh)==1
    succ[S]=mx
cycles=[];seen=set()
for S in TRIPLES:
    if S in seen:continue
    path=[];pos={};x=S
    while x not in pos and x not in seen:
        pos[x]=len(path);path.append(x);x=succ[x]
    seen.update(path)
    if x in pos:cycles.append(tuple(path[pos[x]:]))
assert sorted(map(len,cycles))==[2,2,2]
# Each backtrack cycle has identity connection holonomy.
for S,T in cycles:
    H=compose_maps(repl(T,S),repl(S,T))
    assert all(H[x]==x for x in S)

print('PASS_X6_TRIADIC_EDGE_CURL_V24')
print('dim_Hom_K_to_edge_antisym',mult_one)
print('dim_Hom_wedge2K_to_edge_antisym',mult_wedge)
print('single_field_linear_channel','gradient only')
print('two_field_wedge_channel_unique_up_to_scale',True)
print('curved_witness',witness)
print('curved_witness_circulation',-3)
print('minimal_field_pair_curl_census',dict(census))
print('balanced_ternary_greedy_cycle_lengths',sorted(map(len,cycles)))
print('static_scalar_potential_generates_nontrivial_holonomy',False)
