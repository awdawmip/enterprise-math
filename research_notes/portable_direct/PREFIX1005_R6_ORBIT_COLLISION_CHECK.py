#!/usr/bin/env python3
"""PREFIX-1005: exact orbit compression of the typed Stage46 Z2 BRC observer.
BRC integer numerators and last-port fibres are taken from PREFIX-1004.
Only after the BRC joint-fibre identity is derived do we evaluate scalar
multinomial collisions. Nothing here models a heartbeat time step.
Requires Python 3 and sympy.
"""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import factorial, prod
import sympy as sp

N = sp.symbols('n', integer=True, positive=True)
DIM = 6
Z = (0,) * DIM
E = [tuple(int(i == j) for i in range(DIM)) for j in range(DIM)]

def add(a, b): return tuple(x + y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def sub(a, b): return add(a, neg(b))
def scale(c, p): return {k: c*v for k, v in p.items()}
def shift(p, v): return {add(k, v): c for k, c in p.items()}
def polsum(*ps):
    out = defaultdict(lambda: sp.Integer(0))
    for p in ps:
        for key, c in p.items(): out[key] += c
    return {key: sp.expand(v) for key, v in out.items() if v != 0}
def mul(p, q):
    out = defaultdict(lambda: sp.Integer(0))
    for a, x in p.items():
        for b, y in q.items(): out[add(a, b)] += x*y
    return {k: sp.expand(v) for k, v in out.items() if v != 0}

def B(j, k, S, SU):
    return polsum(scale(k-1, SU), {Z:-36*(k-3)},
                  scale(-6, shift(S, neg(E[0]))),
                  scale(-6, shift(S, neg(E[j]))))

def canonical(delta):
    return min(tuple(sorted(delta)), tuple(sorted(neg(delta))))

def correlation(p):
    out = defaultdict(lambda: sp.Integer(0))
    for a, v in p.items():
        for b, w in p.items(): out[sub(a,b)] += v*w
    return {k: sp.expand(v) for k,v in out.items() if v != 0}

# Laurent group ring of native chart displacements; these are not spatial axes.
S = {axis: sp.Integer(1) for axis in E}
U = {neg(axis): sp.Integer(1) for axis in E}
SU = mul(S,U)
P = [polsum(mul(S,B(j,N,S,SU)),
            scale(-1,shift(B(j,N-1,S,SU),E[0])),{E[0]:25})
     for j in range(DIM)]
Q = [mul(shift({Z:1},neg(E[r])),
         mul(S,mul(polsum(S,{E[r]:-6}),polsum(S,{E[0]:-1}))))
     for r in range(DIM)]
# F^L_{n,j}= z_j S^(n-4) P_j; N^L_{n,r}=S^(n-4) Q_r.
# Each terminal port is squared separately, never coherently mixed.
D = polsum(*[correlation(p) for p in P+Q])
co = defaultdict(lambda: sp.Integer(0))
size = Counter()
for delta, c in D.items():
    key = canonical(delta)
    co[key] += c
    size[key] += 1
co = {k:sp.factor(v) for k,v in co.items() if v != 0}

EXPECTED = {
 (0,0,0,0,0,0):30*(722*N**2-4610*N+8055),
 (-1,0,0,0,0,1):60*(378*N**2-2371*N+5924),
 (-2,0,0,0,0,2):-60*(57*N**2-235*N+185),
 (-2,0,0,0,1,1):-480*(63*N**2-340*N+458),
 (-1,-1,0,0,1,1):-720*(69*N**2-451*N+749),
 (-3,0,0,0,0,3):60*(N-4)*(2*N+1),
 (-3,0,0,0,1,2):1440*(2*N**2-9*N+2),
 (-3,0,0,1,1,1):1440*(2*N**2-10*N+5),
 (-2,-1,0,0,1,2):6480*(2*N**2-11*N+8),
 (-2,-1,0,1,1,1):8640*(2*N**2-12*N+11),
 (-1,-1,-1,1,1,1):1440*(2*N**2-13*N+14),
}
assert len(D)==1281 and len(co)==len(EXPECTED)==11
assert all(sp.expand(co[k]-v)==0 for k,v in EXPECTED.items())
assert sum(size.values()) == 1281

@lru_cache(maxsize=None)
def compositions(parts, total):
    if parts == 1: return ((total,),)
    return tuple((a,) + x for a in range(total+1)
                 for x in compositions(parts-1,total-a))

@lru_cache(maxsize=None)
def H(m, delta):
    ff = factorial(m)
    out=0
    for a in compositions(DIM,m):
        b=add(a,delta)
        if any(z<0 for z in b):continue
        out += (ff//prod(factorial(i) for i in a))*(ff//prod(factorial(i) for i in b))
    return out

def value(n):
    numerator = sum(int(c.subs(N,n))*H(n-4,d) for d,c in co.items())
    return str(Fraction(numerator,36**n))

KNOWN={5:'5285/419904',6:'9715/1259712',7:'1341545/272097792',
       8:'259181485/78364164096',9:'2182586395/940369969152',
       10:'172091043715/101559956668416',
       12:'130785910556945/131621703842267136',
       14:'3036179298003535/4738381338321616896',
       16:'5427336630506440015/12281884428929630994432',
       20:'89379684726508120031933065/371319292745659279662190166016'}
for k, old in KNOWN.items():
    new=value(k)
    assert new==old,(k,new,old)

result={
 'schema':'PREFIX1005_X6_BRC_ORBIT_COLLISION_V1',
 'source':'PREFIX-1004 exact joint-port Laurent packets; frozen P000 V5 @f42f2906',
 'native_carrier':'N-weighted Z2 phase cover, signed character on joint terminal Cell/last incoming port',
 'observer':'single Link {0,e1} absorbing mask; first interior (one negative step)',
 'identity':'36^n M^L_(n,1) = sum_{orbits O} coeff_O(n) H_(n-4)(delta_O), for all n>=5',
 'raw_distinct_laurent_shifts':len(D),
 'orbit_count':len(co),
 'orbits':[
      {'representative':list(k),'raw_shift_count':size[k],
       'coefficient_polynomial':str(co[k])}
      for k in sorted(co,key=lambda k:(sum(abs(x) for x in k),k))],
 'exact_old_certificate_rechecks':{str(k):value(k) for k in KNOWN},
 'verification':'symbolic exact group-ring expansion; integer multinomial collision sums; exact comparisons to PREFIX-1004 certificate',
 'formal_review':'NOT_REVIEWED',
 'future_operation_scope':'fixed final scalar only; no intermediate/history/field gate compression authorization'
}
print(json.dumps(result,indent=2,ensure_ascii=False))
