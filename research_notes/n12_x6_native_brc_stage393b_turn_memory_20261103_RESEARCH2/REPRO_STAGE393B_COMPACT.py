"""Independent compact exact verifier for Stage393-B native signed-X6 BRC.
Research-only combinatorial kernels; not a heartbeat propagator.
Python standard library only.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial

A = tuple((i, s) for i in range(6) for s in (1, -1))
ZERO = (0,) * 6

def shift(z, d):
    a = list(z)
    a[d[0]] += d[1]
    return tuple(a)

def endpoint(w):
    z = ZERO
    for d in w:
        z = shift(z, d)
    return z

def turns(w):
    return sum(w[i] != w[i-1] for i in range(1, len(w)))

def readout(z):
    triples = []
    for S in combinations(range(6), 3):
        lo = min(z[i] for i in S)
        triples.append(tuple(z[i] - lo for i in S))
    return (tuple(triples), min(z))

def compositions(k, n):
    if n == 1:
        yield (k,)
    else:
        for v in range(k+1):
            for tail in compositions(k-v, n-1):
                yield (v,) + tail

def endpoint_kernel(m, z, weights=None):
    base = sum(abs(x) for x in z)
    if m < base or (m-base)%2:
        return 0
    positive = tuple(max(x, 0) for x in z)
    negative = tuple(max(-x, 0) for x in z)
    total = Fraction(0)
    for k in compositions((m-base)//2, 6):
        term = Fraction(factorial(m), 1)
        for i in range(6):
            a, b = positive[i]+k[i], negative[i]+k[i]
            term /= factorial(a) * factorial(b)
            if weights is not None:
                term *= weights[(i,1)]**a * weights[(i,-1)]**b
        total += term
    return total

def decorated_dp(M, weights=None):
    D = {(ZERO, 0, None): Fraction(1)}
    layers = []
    for m in range(1, M+1):
        E = defaultdict(Fraction)
        for (z,c,last),mass in D.items():
            for d in A:
                mul = 1 if weights is None else weights[d]
                E[(shift(z,d), c+(last is not None and last!=d), d)] += mass*mul
        D = dict(E)
        layers.append(D)
    return layers

weights = {d: Fraction(2+d[0]+(d[1]>0), 7) for d in A}
assert endpoint_kernel(4, ZERO) == 396
assert endpoint_kernel(5, shift(ZERO, A[0])) == 1660
assert endpoint_kernel(4, (2,0,0,0,0,0)) == 64
assert endpoint_kernel(3, (1,0,0,0,0,0)) == 33

comparisons = 0
for wt, bound in ((None,5),(weights,4)):
    for m, layer in enumerate(decorated_dp(bound, wt),1):
        totals = defaultdict(Fraction)
        for (z,c,last),mass in layer.items():
            totals[z] += mass
        for z, mass in totals.items():
            assert mass == endpoint_kernel(m,z,wt), (m,z,wt)
            comparisons += 1

W = {}
for d in A:
    j = (d[0]+1)%6
    alpha=(j,1)
    w=(alpha,(j,-1),(d[0],-d[1]),d)
    assert endpoint(w)==ZERO and len(w)==4 and turns(w)==3
    assert readout(endpoint(w)) == readout(ZERO)
    W[d]=w
for d in A:
    for e in A:
        if d != e:
            assert endpoint(W[d]+(d,)) == endpoint(W[e]+(d,))
            assert turns(W[d]+(d,))==3
            assert turns(W[e]+(d,))==4

for mask in range(1<<len(A)):
    L={A[i] for i in range(len(A)) if mask & (1<<i)}
    signatures={d if d in L else None for d in A}
    assert len(signatures)==len(L)+(L!=set(A))

B0=(A[0],A[2],A[3],A[1])
B1=(A[0],A[4],A[5],A[1])
for n in range(1,8):
    family={tuple(y for x in blocks for y in (B0 if x==0 else B1))
            for blocks in product((0,1), repeat=n)}
    assert len(family)==2**n
    assert all(endpoint(w)==ZERO and turns(w)==4*n-1 and w[-1]==A[1]
               for w in family)

u=(A[0],A[0],A[1],A[0])
v=(A[0],A[1],A[0],A[0])
assert (endpoint(u), turns(u), u[-1]) == (endpoint(v),turns(v),v[-1])
assert endpoint_kernel(4,endpoint(u))==64
assert endpoint(u[:-1])==endpoint(v[:-1])==(1,0,0,0,0,0)
assert turns(u[:-1]) == 1 and turns(v[:-1]) == 2

print('STAGE393B_COMPACT_SIGNED_BRC_PASS')
print('full_signature_masks=4096;last_label_fiber=12;ordered_pairs=132')
print('endpoint_comparisons='+str(comparisons)+';return_4=396;one_step_5=1660')
print('POP_examples=64_to_33_with_turns_1_and_2;history_families_n=1..7')
