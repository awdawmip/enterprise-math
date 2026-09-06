#!/usr/bin/env python3
"""Exact finite checks for the corrected X6 upper bundle integration V2."""
from itertools import permutations, combinations, product
from collections import Counter, defaultdict

N=6

def parity(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2
A6=tuple(p for p in permutations(range(N)) if parity(p)==0)
assert len(A6)==360

def sign(x): return 1 if x>0 else -1
def axes(t): return tuple(abs(x)-1 for x in t)
def R(t):
    a=axes(t); s=tuple(sign(x) for x in t)
    return tuple((-s[r])*(a[(r+1)%3]+1) for r in range(3))
def passage(t):
    a=axes(t)
    return frozenset((a[r],a[(r+1)%3]) for r in range(3))
def twist(t):
    s=tuple(sign(x) for x in t)
    return (-s[0]*s[1],-s[1]*s[2],-s[2]*s[0])
def sector(t): return (passage(t),twist(t))
def act_passage(p,P): return frozenset((p[a],p[b]) for a,b in P)

FRAMES=tuple(
    tuple(s*(a+1) for a,s in zip(A,S))
    for A in permutations(range(N),3)
    for S in product((-1,1),repeat=3)
)
assert len(FRAMES)==960

PASSAGES={passage(t) for t in FRAMES}
TWISTS={twist(t) for t in FRAMES}
SECTORS={sector(t) for t in FRAMES}
assert len(PASSAGES)==40
assert len(TWISTS)==4
assert len(SECTORS)==160
assert all(a*b*c==-1 for a,b,c in TWISTS)

# Every passage × twist combination occurs and contains exactly six C6 phases.
fib=Counter(sector(t) for t in FRAMES)
assert set(fib.values())=={6}
assert len(fib)==40*4
for t in FRAMES:
    assert sector(R(t))==sector(t)
    x=t; orb=[]
    for _ in range(6): orb.append(x); x=R(x)
    assert x==t and len(set(orb))==6
    assert {sector(y) for y in orb}=={sector(t)}

# Add SHELL/CLOSURE stage. Each static sector is exactly one C12 orbit.
def U(st):
    t,m=st
    return (t,1) if m==0 else (R(t),0)
DECORATED=tuple((t,m) for t in FRAMES for m in (0,1))
bysector=defaultdict(set)
for st in DECORATED:
    bysector[sector(st[0])].add(st)
assert len(bysector)==160 and set(map(len,bysector.values()))=={12}
for B,states in bysector.items():
    st=next(iter(states)); orb=[]; x=st
    for _ in range(12): orb.append(x); x=U(x)
    assert x==st and set(orb)==states

# Oriented charts are exactly directed 3-cycles on 3-subsets: same underlying
# A6 homogeneous set as unsigned channel passages, though semantically typed apart.
def oriented_cycle(t):
    a,b,c=t
    return frozenset(((a,b),(b,c),(c,a)))
ORIENTED_CHARTS={oriented_cycle(o) for S in combinations(range(N),3) for o in (S,(S[0],S[2],S[1]))}
assert len(ORIENTED_CHARTS)==40
assert ORIENTED_CHARTS==PASSAGES

# A6 is transitive on selected sets (20), oriented charts/passages (40), and
# ordered visible triples (120), with stabilizers 18,9,3 respectively.
ref_set=frozenset((0,1,2)); ref_pass=oriented_cycle((0,1,2)); ref_ord=(0,1,2)
set_stab=[p for p in A6 if frozenset(p[i] for i in ref_set)==ref_set]
pass_stab=[p for p in A6 if act_passage(p,ref_pass)==ref_pass]
ord_stab=[p for p in A6 if tuple(p[i] for i in ref_ord)==ref_ord]
assert (len(set_stab),len(pass_stab),len(ord_stab))==(18,9,3)
assert len({frozenset(p[i] for i in ref_set) for p in A6})==20
assert len({act_passage(p,ref_pass) for p in A6})==40
assert len({tuple(p[i] for i in ref_ord) for p in A6})==120

# Relative-sign map on 8 sign assignments has four outputs, kernel {s,-s}.
sign_to_twist=defaultdict(list)
for s in product((-1,1),repeat=3):
    a=(-s[0]*s[1],-s[1]*s[2],-s[2]*s[0])
    sign_to_twist[a].append(s)
assert len(sign_to_twist)==4 and set(map(len,sign_to_twist.values()))=={2}
for a,ss in sign_to_twist.items():
    assert ss[1]==tuple(-x for x in ss[0]) or ss[0]==tuple(-x for x in ss[1])

# Current triadic positive permutation dynamics is A6, so global Ori6 parity is
# invariant under every allowed unsigned event generator.
assert all(parity(p)==0 for p in A6)

print('PASS_X6_UPPER_BUNDLE_INTEGRATION_V2')
print('oriented_passage_chart_space',len(PASSAGES))
print('relative_sign_twists',len(TWISTS))
print('static_signed_sectors',len(SECTORS))
print('C6_phase_fiber_per_sector',next(iter(fib.values())))
print('decorated_C12_fiber_per_sector',next(iter(map(len,bysector.values()))))
print('A6_stabilizers_set_oriented_ordered',(len(set_stab),len(pass_stab),len(ord_stab)))
print('sign_to_twist_kernel_size',2)
print('triadic_Ori6_sector_change',False)
