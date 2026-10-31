"""Exact finite certificate for the R5 route-ingress first observer (auxiliary model).

All rational calculations use Python's stdlib Fraction. This does NOT execute
native BRC/X6 arithmetic, and does not establish project admission or reviewer
independence.
"""
from fractions import Fraction as F
from itertools import product, combinations
from functools import reduce
from math import gcd, lcm

ALPHA = (F(1, 4), F(1, 5))
KAPPA = (F(3, 4), F(1, 6))
FULL_KEYS = ('A', 'D', 'Y', 'LD', 'LY', 'LC')
LR_KEYS = ('A', 'D', 'Y', 'L')
LEAVES = ('A', 'D', 'Y', 'C', 'DH', 'YH',
          'LD', 'LY', 'LC', 'L4D', 'L4Y', 'L4C')
T = {'A': 1, 'D': 2, 'Y': 2, 'C': 2, 'DH': 3, 'YH': 3,
     'LD': 3, 'LY': 3, 'LC': 3, 'L4D': 4, 'L4Y': 4, 'L4C': 4}
LAMBDA = {'A': F(1), 'D': F(1, 2), 'Y': F(3, 2),
          'C': F(1), 'DH': F(1, 4), 'YH': F(2),
          'LD': F(1), 'LY': F(1), 'LC': F(1),
          'L4D': F(1), 'L4Y': F(1), 'L4C': F(1)}

def flows(source_actions):
    out = {k: F(0) for k in LEAVES}
    for i, (a, k) in enumerate(zip(ALPHA, KAPPA)):
        b = source_actions[i]
        start = F(1, 2)
        cont = start * b['A']
        out['A'] += start - cont
        d = cont*a
        y = cont*a
        c = cont*(1-2*a)
        if b['D']:
            out['DH'] += 2*d/3
            out['L4D' if b['LD'] else 'LD'] += d/3
        else:
            out['D'] += d
        if b['Y']:
            out['YH'] += y/2
            out['L4Y' if b['LY'] else 'LY'] += y/2
        else:
            out['Y'] += y
        out['C'] += c*(1-k)
        out['L4C' if b['LC'] else 'LC'] += c*k
    assert all(v >= 0 for v in out.values())
    assert sum(out.values()) == 1
    assert sum(out[k]*LAMBDA[k] for k in LEAVES) == 1
    return out

def full_policy(bits):
    return flows([dict(zip(FULL_KEYS, bits[6*i:6*i+6])) for i in range(2)])

def lr_policy(bits):
    b = dict(zip(LR_KEYS, bits))
    return flows([dict((k, b['L' if k.startswith('L') else k])
                       for k in FULL_KEYS) for _ in range(2)])

def det(mat):
    a = [[F(t) for t in row] for row in mat]
    n = len(a)
    assert n and all(len(row) == n for row in a)
    answer = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            answer = -answer
        p = a[j][j]
        answer *= p
        for i in range(j+1, n):
            q = a[i][j]/p
            for h in range(j, n):
                a[i][h] -= q*a[j][h]
    return answer

def affine_rank(points):
    pts = [tuple(p) for p in points]
    base = pts[0]
    basis = {}
    for point in pts[1:]:
        v = [point[j]-base[j] for j in range(len(base))]
        for j in sorted(basis):
            q = v[j]
            if q:
                v = [v[k]-q*basis[j][k] for k in range(len(v))]
        pivot = next((j for j, q in enumerate(v) if q), None)
        if pivot is not None:
            x = v[pivot]
            basis[pivot] = [q/x for q in v]
    return len(basis)

def flow_vector(f):
    return tuple(f[k] for k in LEAVES)

def tq(f):
    return sum(f[k]*T[k] for k in LEAVES)

def reduced3(f):
    return (f['DH'], f['YH'], tq(f))

def reduced4(f):
    return reduced3(f)+(sum(f[k] for k in ('L4D','L4Y','L4C'))+F(1, 2)*f['LC'],)

def minor4(p, inds):
    ref = p[inds[0]]
    return det([[p[j][k]-ref[k] for k in range(4)] for j in inds[1:]])

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def primitive(n, c):
    den = lcm(*(v.denominator for v in n+(c,)))
    whole = tuple(int(v*den) for v in n+(c,))
    factor = reduce(gcd, whole)
    return tuple(v//factor for v in whole)

def all_facets_3d(points):
    """Enumerate all supporting 2D hyperplanes of a full 3D polytope."""
    facets = set()
    for ids in combinations(range(len(points)), 3):
        a, b, c = (points[i] for i in ids)
        n = cross(tuple(b[j]-a[j] for j in range(3)),
                  tuple(c[j]-a[j] for j in range(3)))
        if n == (0, 0, 0):
            continue
        cut = sum(n[j]*a[j] for j in range(3))
        signed = [sum(n[j]*p[j] for j in range(3))-cut for p in points]
        if max(signed) <= 0 and min(signed) < 0:
            facets.add(primitive(n, cut))
        elif min(signed) >= 0 and max(signed) > 0:
            facets.add(primitive(tuple(-x for x in n), -cut))
    return facets

def signed4(v):
    x, u, t, s = v
    return -21*x-61*u-19*t+118*s

def observed4(f):
    r = {k:F(1,2) for k in LEAVES}
    r['DH'] += F(1,8)
    for k in ('L4D','L4Y','L4C'):
        r[k] += F(1,4)
    r['LC'] += F(1,8)
    ep = sum(f[k]*LAMBDA[k]*r[k] for k in LEAVES)
    eq = sum(f[k]*r[k] for k in LEAVES)
    tp = sum(f[k]*T[k]*LAMBDA[k] for k in LEAVES)
    t = tq(f)
    return ep,eq,tp,t

def signed_observed(v):
    ep,eq,tp,tqv=v
    return 4024*ep-2608*eq-183*tp+126*tqv

def main():
    assert tuple((1+k*(1-2*a))/a for a,k in zip(ALPHA,KAPPA))==(F(11,2),F(11,2))
    fb=list(product((0,1),repeat=12))
    lb=list(product((0,1),repeat=4))
    full=[full_policy(b) for b in fb]
    lr=[lr_policy(b) for b in lb]
    assert len(full)==4096 and len(lr)==16
    assert affine_rank([flow_vector(f) for f in full])==7
    assert affine_rank([flow_vector(f) for f in lr])==6
    print('ROUTE_SPLIT_TERMINAL_RANK FULL=7 LR=6; 4096+16 exact normalizations PASS')
    x3=[reduced3(f) for f in full]
    y3=[reduced3(f) for f in lr]
    assert affine_rank(x3)==affine_rank(y3)==3
    assert det([[y3[j][k]-y3[0][k] for k in range(3)]
                for j in (8,10,12)]) == -F(2673,128000)
    facets=all_facets_3d(y3)
    required={(-80,-120,40,99),(-1,0,0,0),(0,-1,0,0),
              (0,80,0,9),(3,26,-2,-2),(20,0,0,3),(39,8,-4,-4)}
    assert facets==required
    for normal in facets:
        assert max(sum(normal[j]*v[j] for j in range(3))-normal[3]
                   for v in x3)==0
    # Every facet of a 3D polytope has three affinely independent defining
    # vertices; the enumeration therefore lists its COMPLETE facet system.
    # The FULL polytope lies within these seven half-spaces; LR <= FULL.
    print('3D_HULL_EQUALITY: 7/7 exact complete LR facets contain all 4096 FULL points; det=-2673/128000')
    y4=[reduced4(f) for f in lr]
    x4=[reduced4(f) for f in full]
    assert minor4(y4, (0,8,9,10,12))==-F(513,256000)
    assert affine_rank(y4)==4
    lrmax=max(map(signed4,y4));fullmax=max(map(signed4,x4))
    assert (lrmax,fullmax,fullmax-lrmax)==(-19,-F(27,2),F(11,2))
    wbits=(1,0,0,0,0,1,0,0,0,0,0,0)
    witness=full_policy(wbits)
    assert reduced4(witness)==(F(0),F(0),F(15,8),F(3,16))
    assert observed4(witness)==(F(35,64),F(35,64),F(15,8),F(15,8))
    for f in full+lr:
        x,u,t,s=reduced4(f)
        ep,eq,tp,tqv=observed4(f)
        assert x==F(32,3)*(eq-ep)
        assert u==tp-tqv+F(3,4)*x
        assert s==4*(eq-F(1,2))-F(1,2)*x
        assert signed_observed((ep,eq,tp,tqv))==3*(signed4((x,u,t,s))+236)
    olrmax=max(signed_observed(observed4(f)) for f in lr)
    ofullmax=max(signed_observed(observed4(f)) for f in full)
    assert (olrmax,ofullmax,ofullmax-olrmax)==(651,F(1335,2),F(33,2))
    print('4D_OBSERVER_RANK=4 minor=-513/256000; FULL/LR support gap=11/2 in reduced coordinates')
    print('4D_OBSERVED_SEPARATOR 4024*eP-2608*eQ-183*TP+126*TQ <=651 (LR), FULLmax=1335/2, gap=33/2')
    print('FULL_WITNESS bits=100001000000, O=(35/64,35/64,15/8,15/8)')
    print('CLAIM_SCOPE auxiliary finite rational model only; hull equality 3D; rank-four gap at first route-sensitive example')
    print('PASS_EXACT_R5_ROUTE_INGRESS_3D_HULL_EQUAL_4D_SEPARATOR')

if __name__=='__main__':
    main()
