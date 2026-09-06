#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import permutations, product

N=6
CANON=(-1,-1,-1)


def sgn(x): return 1 if x>0 else -1

def ax(t): return tuple(abs(x)-1 for x in t)

def twisted_step(t,alpha):
    a=ax(t); s=tuple(sgn(x) for x in t)
    return tuple(alpha[r]*s[r]*(a[(r+1)%3]+1) for r in range(3))

def R(t): return twisted_step(t,CANON)

def old_R(t): return (-t[1],-t[2],-t[0])

def passage(t):
    a=ax(t)
    return frozenset((a[r],a[(r+1)%3]) for r in range(3))

def permute_axes(t,p):
    return tuple(sgn(x)*(p[abs(x)-1]+1) for x in t)

def gauge_frame(t,eps):
    return tuple(eps[abs(x)-1]*x for x in t)

def gauge_alpha(t,alpha,eps):
    a=ax(t)
    return tuple(eps[a[r]]*eps[a[(r+1)%3]]*alpha[r] for r in range(3))

def alpha_state(t):
    s=tuple(sgn(x) for x in t)
    return tuple(-s[r]*s[(r+1)%3] for r in range(3))

FRAMES=tuple(
    tuple(signs[r]*(axes[r]+1) for r in range(3))
    for axes in permutations(range(N),3)
    for signs in product((-1,1),repeat=3)
)
assert len(FRAMES)==960 and len(set(FRAMES))==960

# Concrete falsifier for the historical tuple-reordering formula.
w=(1,-2,3)
assert R(w)==(-2,3,-1)
assert old_R(w)==(2,-3,-1)
assert R(w)!=old_R(w)

# Correct canonical tokenwise Q gives 160 exact C6 orbits and preserves the
# unsigned directed passage cycle.
seen=set(); orbits=[]
for t in FRAMES:
    if t in seen: continue
    orb=[]; x=t
    while x not in orb:
        orb.append(x); seen.add(x); x=R(x)
    assert x==t and len(orb)==6 and len(set(orb))==6
    assert len({passage(y) for y in orb})==1
    assert len({alpha_state(y) for y in orb})==1
    orbits.append(tuple(orb))
assert len(orbits)==160

# Four C6 orbit sectors lie over every one of the 40 unsigned directed passages.
by_passage=defaultdict(list)
for orb in orbits: by_passage[passage(orb[0])].append(orb)
assert len(by_passage)==40 and set(map(len,by_passage.values()))=={4}
TWISTS={a for a in product((-1,1),repeat=3) if a[0]*a[1]*a[2]==-1}
assert len(TWISTS)==4
for p,obs in by_passage.items():
    assert {alpha_state(o[0]) for o in obs}==TWISTS

# Shell/closure lift remains 1920 states in 160 exact C12 cycles.
def F(st):
    t,mode=st
    return (t,1) if mode==0 else (R(t),0)
for t in FRAMES:
    for mode in (0,1):
        st=(t,mode); x=st; seq=[]
        for _ in range(12): seq.append(x); x=F(x)
        assert x==st and len(set(seq))==12

# Canonical family is covariant under unsigned axis relabelings.
gens=[]
for i in range(N-1):
    p=list(range(N));p[i],p[i+1]=p[i+1],p[i];gens.append(tuple(p))
for t in FRAMES:
    for p in gens:
        assert R(permute_axes(t,p))==permute_axes(R(t),p)

# But naive canonical equivariance under independent sign gauges is false.
eps=(-1,1,1,1,1,1)
assert R(gauge_frame(w,eps))!=gauge_frame(R(w),eps)

# Full signed-frame covariance is restored by the four-twist bundle.
# alpha' = eps(source)*eps(target)*alpha, product remains -1.
gauge_checks=0
for t in FRAMES:
    active=ax(t)
    for local_eps in product((-1,1),repeat=3):
        eps=[1]*N
        for a,e in zip(active,local_eps): eps[a]=e
        eps=tuple(eps)
        for alpha in TWISTS:
            ap=gauge_alpha(t,alpha,eps)
            assert ap in TWISTS
            lhs=twisted_step(gauge_frame(t,eps),ap)
            rhs=gauge_frame(twisted_step(t,alpha),eps)
            assert lhs==rhs
            gauge_checks+=1

# Starting from the canonical twist, sign gauges reach all four twist patterns.
t=(1,2,3)
reached={gauge_alpha(t,CANON,eps+(1,1,1)) for eps in product((-1,1),repeat=3)}
assert reached==TWISTS

# Unsigned PF-10 quotient cardinalities remain unchanged.
io=Counter(frozenset(ax(t)) for t in FRAMES)
pc=Counter(passage(t) for t in FRAMES)
assert len(io)==20 and set(io.values())=={48}
assert len(pc)==40 and set(pc.values())=={24}

print('PASS_X6_SIGNED_INTERNAL_Q_CORRECTION_V5')
print('historical_R_counterexample',w)
print('correct_C6_orbits',len(orbits))
print('directed_passages',len(by_passage))
print('signed_orbit_sectors_per_passage',4)
print('signed_generator_twists',len(TWISTS))
print('full_signed_gauge_covariance_checks',gauge_checks)
print('PF10_IO_states',len(io))
print('PF10_passage_states',len(pc))
