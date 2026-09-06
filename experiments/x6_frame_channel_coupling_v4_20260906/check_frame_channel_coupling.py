#!/usr/bin/env python3
from collections import Counter, deque
from itertools import combinations, permutations, product

N=6
SID=tuple(range(1,N+1))
PID=tuple(range(N))

def scompose(g,h):
    out=[]
    for x in h:
        sx=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(sx*y)
    return tuple(out)

def pcompose(g,h): return tuple(g[h[i]] for i in range(N))
def positive_projection(g): return tuple(abs(x)-1 for x in g)

def q_triad(t):
    i,j,k=t
    q=list(SID)
    q[i]=-(j+1); q[j]=-(k+1); q[k]=-(i+1)
    return tuple(q)

def rho(t):
    i,j,k=t
    p=list(PID); p[i]=j; p[j]=k; p[k]=i
    return tuple(p)

# Generator-level coupling U=pi(Q)=rho for all oriented triads.
ordered=tuple(t for S in combinations(range(N),3) for t in permutations(S))
for t in ordered:
    assert positive_projection(q_triad(t))==rho(t)

# Build the triadic frame group and verify image/fiber sizes.
gens=tuple({q_triad(t) for t in ordered})
R={SID}; dq=deque([SID])
while dq:
    x=dq.popleft()
    for g in gens:
        y=scompose(g,x)
        if y not in R:
            R.add(y); dq.append(y)
assert len(R)==23040
images=Counter(positive_projection(g) for g in R)
assert len(images)==360 and set(images.values())=={64}

# Image is A6; test parity even.
def parity(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2
assert all(parity(p)==0 for p in images)

# Projection homomorphism on exact sample pairs.
Rs=tuple(R)
for g,h in product(Rs[:80],Rs[-80:]):
    assert positive_projection(scompose(g,h))==pcompose(positive_projection(g),positive_projection(h))

# One Q cycle projects C6 -> C3, with half-turn in kernel.
q=q_triad((0,1,2)); r=rho((0,1,2))
def spow(g,n):
    out=SID
    for _ in range(n): out=scompose(g,out)
    return out
def ppow(g,n):
    out=PID
    for _ in range(n): out=pcompose(g,out)
    return out
assert spow(q,6)==SID
assert ppow(r,3)==PID
assert positive_projection(spow(q,3))==PID
for n in range(7):
    assert positive_projection(spow(q,n))==ppow(r,n)

# All channel 3-cycles generate A6 (360 elements).
pgens=tuple({rho(t) for t in ordered})
A={PID}; qd=deque([PID])
while qd:
    x=qd.popleft()
    for g in pgens:
        y=pcompose(g,x)
        if y not in A:
            A.add(y); qd.append(y)
assert len(A)==360
assert set(A)==set(images)

print('PASS_X6_FRAME_CHANNEL_COUPLING_V4')
print('triadic_frame_group_order',len(R))
print('unsigned_channel_image_order',len(images))
print('frame_states_per_channel_permutation',next(iter(images.values())))
print('channel_group','A6')
print('single_Q_frame_period',6)
print('single_Q_channel_period',3)
print('channel_is_independent_group_in_minimal_coupling',False)
