#!/usr/bin/env python3
"""Exact finite checks for full signed-unit-shell C12 frames and C24 outer lifts."""
from collections import deque
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, permutations, product
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BRC_PATH=ROOT/'experiments'/'x6_signed_native_spatial_v16_20260905'/'signed_brc.py'
spec=spec_from_file_location('x6_signed_brc',BRC_PATH)
if spec is None or spec.loader is None: raise RuntimeError('cannot load signed_brc')
brc=module_from_spec(spec);spec.loader.exec_module(brc)

N=6
ID=tuple(range(1,N+1))
NEG_ID=tuple(-(i+1) for i in range(N))

def compose(g,h):
    out=[]
    for x in h:
        s=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(s*y)
    return tuple(out)

def inv(g):
    out=[None]*N
    for i,y in enumerate(g):
        s=1 if y>0 else -1
        out[abs(y)-1]=s*(i+1)
    return tuple(out)
def conj(h,g): return compose(compose(h,g),inv(h))
def power(g,n):
    out=ID
    for _ in range(n): out=compose(g,out)
    return out

def perm(g): return tuple(abs(x)-1 for x in g)
def parity_perm(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2
def parity(g): return parity_perm(perm(g))
def sign_product(g):
    out=1
    for x in g: out*=1 if x>0 else -1
    return out

def cycle_lengths(p):
    seen=set();out=[]
    for i in range(N):
        if i in seen: continue
        j=i;L=0
        while j not in seen:
            seen.add(j);L+=1;j=p[j]
        out.append(L)
    return tuple(sorted(out,reverse=True))

def act(g,z):
    out=[0]*N
    for i,c in enumerate(z):
        if c:
            y=g[i];out[abs(y)-1]+=(1 if y>0 else -1)*c
    return tuple(out)
def unit(i,s=1):
    z=[0]*N;z[i]=s;return tuple(z)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))

B6=tuple(tuple(signs[i]*(p[i]+1) for i in range(N))
         for p in permutations(range(N)) for signs in product((-1,1),repeat=N))
assert len(B6)==46080

# Transitive signed-unit-shell frames: exactly underlying 6-cycle + negative sign holonomy.
def signed_unit_orbit(g):
    x=unit(0);orb=[]
    while x not in orb:
        orb.append(x);x=act(g,x)
    return tuple(orb)

GLOBAL=[]
for g in B6:
    transitive=(len(signed_unit_orbit(g))==12)
    criterion=(cycle_lengths(perm(g))==(6,) and sign_product(g)==-1)
    assert transitive==criterion
    if transitive:
        assert parity(g)==1
        assert power(g,6)==NEG_ID
        assert power(g,12)==ID
        GLOBAL.append(g)
assert len(GLOBAL)==120*32==3840

# Current triadic group R=(C2)^6 ⋊ A6 and one conjugacy orbit on GLOBAL.
def q_triad(S):
    i,j,k=S;q=list(ID)
    q[i]=-(j+1);q[j]=-(k+1);q[k]=-(i+1);return tuple(q)
def closure(gens):
    G={ID};Q=deque([ID])
    while Q:
        h=Q.popleft()
        for g in gens:
            x=compose(g,h)
            if x not in G:G.add(x);Q.append(x)
    return G
R=closure(tuple(q_triad(S) for S in combinations(range(N),3)))
assert len(R)==23040
REP=(2,3,4,5,6,-1)
assert REP in GLOBAL
orb={conj(r,REP) for r in R}
assert orb==set(GLOBAL)
assert len(R)//len(orb)==6

# Representative has one 12-state signed unit orbit and a 24-state all-OUTER Cell lift.
phases=signed_unit_orbit(REP)
assert len(phases)==12 and len(set(phases))==12
mids=[add(phases[r],phases[(r+1)%12]) for r in range(12)]
assert len(set(mids))==12
assert not set(phases)&set(mids)
assert len(set(phases+mids))==24
for r in range(12):
    a=phases[r];b=phases[(r+1)%12];m=mids[r]
    d=sub(b,a)
    assert brc.shortest_event_count(d)==2
    assert brc.shortest_path_multiplicity(d)==2
    assert brc.shortest_event_count(sub(m,a))==1
    assert brc.shortest_event_count(sub(b,m))==1

# Every GLOBAL frame has the same 12 macro edges / 24 distinct OUTER Cell cycle property.
for g in GLOBAL:
    ph=signed_unit_orbit(g)
    mids_g=[add(ph[r],ph[(r+1)%12]) for r in range(12)]
    assert len(set(ph+mids_g))==24
    for r in range(12):
        assert brc.shortest_path_multiplicity(sub(ph[(r+1)%12],ph[r]))==2

# One full frame cycle has 2^12 distinct concatenated shortest microtrace loops.
loops=set()
zero=(0,)*N
for bits in product((0,1),repeat=12):
    seq=[phases[0]]
    for r,bit in enumerate(bits):
        a=phases[r];b=phases[(r+1)%12]
        mid=zero if bit==0 else add(a,b)
        seq.extend((mid,b))
    seq=tuple(seq)
    assert seq[0]==seq[-1]
    assert len(seq)==25 # 24 microsteps plus initial state
    loops.add(seq)
assert len(loops)==2**12==4096

print('PASS_X6_GLOBAL_C12_C24_V10')
print('full_integral_frame_count',len(B6))
print('global_signed_direction_C12_generators',len(GLOBAL))
print('R_triad_conjugacy_orbit_size',len(orb))
print('R_triad_stabilizer_order',len(R)//len(orb))
print('global_C12_requires_Ori6',1)
print('outer_native_Cell_cycle_states',24)
print('shortest_microtrace_loops_per_frame_C12',len(loops))
print('microsteps_per_frame_C12',24)
