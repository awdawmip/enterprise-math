#!/usr/bin/env python3
"""Exact Fraction certificate: K-answer neutralization leaves a J-source answer facet.
R5 positive two-law three-key auxiliary stopping DAG, fixed delay lambda=1.
"""
from fractions import Fraction as Q
from itertools import product

Z, ONE, HALF = Q(0), Q(1), Q(1, 2)
K = {
    'C':  (Q(3, 4), Q(1, 4), Q(1, 4), Q(1, 8)),
    'I':  (Q(1, 4), Q(3, 4), Q(3, 4), Q(1, 4)),
    'BJ': (Q(2, 3), Q(1, 3), Q(1, 3), Q(1, 6)),
    'IJ': (Q(1, 3), Q(2, 3), Q(2, 3), Q(1, 3)),
}
J = {'B': (Q(2, 5), Q(3, 5)), 'I': (Q(3, 5), Q(2, 5))}
checks = 0
flows = 0

def check(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError(label)

def add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(4))

def sc(a, v):
    return tuple(a * x for x in v)

def stop(t):
    return (ONE, Z, Q(t), Q(t))

def answer(t, p, q):
    return (p, ONE-q, Q(t), Q(t))

def full(s, x, jB, jI, kC, kI, kBJ, kIJ, jblend=Z):
    global flows
    flows += 1
    def knode(source, k):
        p0, q0, dP, dQ = K[source]
        p = (ONE-s)*p0 + s*HALF
        q = (ONE-s)*q0 + s*HALF
        return add(sc(k, stop(3)), sc(ONE-k, (p, ONE-q, Q(4)+dP, Q(4)+dQ)))
    def jnode(source, j, k):
        p0, q0 = J[source]
        p = (ONE-jblend)*p0 + jblend*HALF
        q = (ONE-jblend)*q0 + jblend*HALF
        daughter = 'BJ' if source == 'B' else 'IJ'
        cont = add(sc(HALF, knode(daughter, k)), sc(HALF, answer(3, p, q)))
        return add(sc(j, stop(2)), sc(ONE-j, cont))
    i = add(sc(x, stop(1)), sc(ONE-x,
        add(sc(HALF, jnode('I', jI, kIJ)), sc(HALF, knode('I', kI)))))
    return add(sc(HALF, i), sc(Q(1,4), jnode('B', jB, kBJ)), sc(Q(1,4), knode('C', kC)))

def lr(s, x, y, z, jblend=Z):
    return full(s, x, y, y, z, z, z, z, jblend=jblend)

def E(v):
    return v[0]+v[1]

def D(v):
    return v[2]-v[3]

def det(a):
    m = [row[:] for row in a]
    sign = ONE
    for j in range(len(m)):
        k = next((r for r in range(j, len(m)) if m[r][j] != 0), None)
        if k is None:
            return Z
        if k != j:
            m[j],m[k] = m[k],m[j]
            sign = -sign
        p = m[j][j]
        sign *= p
        for r in range(j+1,len(m)):
            fac = m[r][j]/p
            for c in range(j+1,len(m)):
                m[r][c] -= fac*m[j][c]
            m[r][j] = Z
    return sign

FC = list(product((Z, ONE), repeat=7))
LC = list(product((Z, ONE), repeat=3))
check(len(FC) == 128 and len(LC) == 8, 'vertex cardinalities')
for p0,q0,dP,dQ in K.values():
    for v in (p0,q0,dP,dQ):
        check(Z < v < ONE, 'strictly positive K natural/answer kernels')
for p,q in J.values():
    check(Z < p < ONE and Z < q < ONE, 'strictly positive J answer kernels')

# Each fixed deterministic observation is affine in s. The claimed envelopes
# are affine on each of [0,2/5] and [2/5,1]. Endpoint inequalities,
# combined with common endpoint-attaining policies, prove all-real envelopes.
def bounds(s):
    if s <= Q(2,5):
        return (Q(5,6)+s/6, Q(39,40), Q(7,6)-s/6, Q(137,120)-s/6)
    return (Q(17,20)+s/8, Q(39,40), Q(23,20)-s/8, Q(9,8)-s/8)

intervals = [(Z,Q(2,5)), (Q(2,5),ONE)]
for a,b in intervals:
    fa = {t: full(a,*t) for t in FC}; fb = {t: full(b,*t) for t in FC}
    la = {t: lr(a,*t) for t in LC}; lb = {t: lr(b,*t) for t in LC}
    for s,fs,ls in [(a,fa,la),(b,fb,lb)]:
        for v in list(fs.values())+list(ls.values()):
            check(Z <= v[0] <= ONE and Z <= v[1] <= ONE, 'physical answer bounds')
        vals = (min(map(E,fs.values())),min(map(E,ls.values())),
                max(map(E,fs.values())),max(map(E,ls.values())))
        check(vals == bounds(s), 'endpoint support envelope')
    for label, dataA, dataB, index, extremum in [
        ('FULL_min',fa,fb,0,min), ('LR_min',la,lb,1,min),
        ('FULL_max',fa,fb,2,max), ('LR_max',la,lb,3,max)]:
        witnesses = [t for t in dataA if E(dataA[t]) == bounds(a)[index]
                     and E(dataB[t]) == bounds(b)[index]]
        check(len(witnesses) > 0, 'common optimal affine witness '+label)
        print('segment',str(a),str(b),label,'witness',str(witnesses[0]))

# At s=1: the old -E facet is exactly tied, but the opposite E facet
# separates the full and LR convex hulls by 1/40.
s = ONE
fs = {t:full(s,*t) for t in FC}
ls = {t:lr(s,*t) for t in LC}
W_key = (Z,ONE,Z,Z,Z,Z,Z)
W = fs[W_key]
check(W == (Q(51,80), Q(31,80), Q(89,24), Q(337,96)), 'positive E witness')
check(E(W) == Q(41,40) and max(map(E,ls.values())) == ONE,'positive answer separation')
check(min(map(E,fs.values())) == min(map(E,ls.values())) == Q(39,40),'negative answer facet equal')
check(max(map(D,fs.values())) == max(map(D,ls.values())) == Q(7,32),'positive time facet equal')
check(min(map(D,fs.values())) == min(map(D,ls.values())) == Z,'negative time facet equal')

# LR hull rank using exact five-corner affine minor, following predecessor.
qkeys = [(Z,Z,Z),(Z,Z,ONE),(Z,ONE,Z),(ONE,Z,Z),(ONE,Z,ONE)]
pts = [ls[t] for t in qkeys]
LR_det = det([[pts[j][i]-pts[0][i] for j in range(1,5)] for i in range(4)])
check(LR_det == Q(13,98304), 'LR affine rank-four determinant')

# The multi-affine FULL Jacobian columns are endpoint differences; evaluate
# the 4x4 minor in (x,jB,jI,kC) at all seven behavior parameters=1/2.
center = [HALF]*7
columns=[]
for j in (0,1,2,3):
    plus=center.copy();minus=center.copy()
    plus[j]=ONE;minus[j]=Z
    v1,v0=full(s,*plus),full(s,*minus)
    columns.append([v1[i]-v0[i] for i in range(4)])
FULL_minor=det([[columns[j][i] for j in range(4)] for i in range(4)])
check(FULL_minor == Q(47,1310720), 'FULL Jacobian rank-four')

# A second exact non-corner check of the multi-affine s dependence and
# constant temporal readout, independently of the support certificate.
for v in product((Q(1,3),Q(2,3)),repeat=7):
    u0=full(Z,*v);u1=full(ONE,*v)
    for s0 in (Q(1,7),Q(3,5)):
        us=full(s0,*v)
        check(us==tuple((ONE-s0)*u0[i]+s0*u1[i] for i in range(4)),
              'interior s-affinity')
    check(u0[2:]==u1[2:],'K answer interpolation preserves time')

# Second independent analytical boundary: additionally neutralize both J answer
# kernels with t in [0,1] at s=1. The signed +E gap is (1-t)/40,
# and the -E gap is zero. At t=1, E is the constant 1, so rank <=3.
for t in (Z,Q(1,3),Q(2,3),ONE):
    ff=[full(ONE,*k,jblend=t) for k in FC]
    ll=[lr(ONE,*k,jblend=t) for k in LC]
    for k,v in zip(FC,ff):
        x,jb,ji,*rest=k
        check(E(v)==ONE+(ONE-t)*(jb+(ONE-x)*(ONE-ji)-ONE)/40,
              'source-resolved J neutralization formula')
    for k,v in zip(LC,ll):
        x,y,z=k
        check(E(v)==ONE-(ONE-t)*x*(ONE-y)/40,
              'LR J neutralization formula')
    check(min(map(E,ff)) == min(map(E,ll)) == ONE-(ONE-t)/40,
          'both negative answer envelopes equal')
    check(max(map(E,ff))==ONE+(ONE-t)/40 and max(map(E,ll))==ONE,
          'positive gap scales with (1-t)')
    if t==ONE:
        check(all(E(v)==ONE for v in ff+ll), 'answer constant causes rank collapse')

# A genuinely source-asymmetric J experiment: change B's J-answer pair to
# the I pair (3/5,2/5), while preserving separate B/I histories, K-neutral
# answers, and the positive distinct K time carriers. Both E supports agree
# and both hull/map ranks are four, but an oblique signed separator persists.
J['B'] = (Q(3,5), Q(2,5))
fa = {k:full(ONE,*k) for k in FC}
la = {k:lr(ONE,*k) for k in LC}
check(min(map(E,fa.values())) == min(map(E,la.values())) == ONE,
      'source-aligned J min E support')
check(max(map(E,fa.values())) == max(map(E,la.values())) == Q(21,20),
      'source-aligned J max E support')
normal = (2,-1,1,0)
def signed(v):
    return sum(Q(normal[i])*v[i] for i in range(4))
hf = max(map(signed,fa.values()))
hl = max(map(signed,la.values()))
check(hf == Q(71,15) and hl == Q(93,20) and hf-hl == Q(1,12),
      'source-aligned J oblique exact support difference')
W2key = (Z,Z,Z,ONE,Z,ONE,Z)
W2 = fa[W2key]
check(W2 == (Q(57,80),Q(27,80),Q(175,48),Q(167,48)) and signed(W2)==hf,
      'oblique FULL witness')
pts = [la[t] for t in qkeys]
LR_new_det = det([[pts[j][i]-pts[0][i] for j in range(1,5)] for i in range(4)])
check(LR_new_det == -Q(49,61440), 'aligned-J LR rank-four affine minor')
columns=[]
for j in (0,1,2,3):
    plus=center.copy();minus=center.copy();plus[j]=ONE;minus[j]=Z
    v1,v0 = full(ONE,*plus),full(ONE,*minus)
    columns.append([v1[i]-v0[i] for i in range(4)])
FULL_new_minor = det([[columns[j][i] for j in range(4)] for i in range(4)])
check(FULL_new_minor == Q(23,1966080), 'aligned-J FULL rank-four Jacobian minor')
print('aligned-J FULL/LR E support ranges',ONE,Q(21,20))
print('aligned-J oblique normal',normal,'hFULL',hf,'hLR',hl,'gap',hf-hl)
print('aligned-J FULL witness',W2,'infinity distance lower bound',Q(1,48))
print('aligned-J LR affine minor',LR_new_det,'FULL Jacobian minor',FULL_new_minor)

print('s=1 witness FULL',W_key,W)
print('s=1 LR E upper',max(map(E,ls.values())),'FULL E upper',max(map(E,fs.values())))
print('s=1 signed support gap E',Q(1,40),'infinity distance lower bound',Q(1,80))
print('s=1 signed support gap -E',Z,'time supports both directions equal')
print('J-neutralization at K s=1: positive E gap=(1-t)/40; t=1 forces E==1 and rank<=3')
print('LR affine det',LR_det,'FULL Jacobian minor',FULL_minor)
print('two exact affine-envelope intervals, total corner strategies',len(FC),len(LC))
print('checks',checks,'physical_evaluations',flows)
print('PASS_EXACT_R5_K_ANSWER_NEUTRALIZATION_FACET_MIGRATION')
