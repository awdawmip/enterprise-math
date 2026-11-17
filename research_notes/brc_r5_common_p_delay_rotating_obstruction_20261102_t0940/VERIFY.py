#!/usr/bin/env python3
"""R5 common-P-delay family: all-real exact rotating-separator certificate."""
from fractions import Fraction as Q
from itertools import product

Z, ONE, HALF = Q(0), Q(1), Q(1, 2)
Q_DELAY = {'C': Q(1,8), 'I': Q(1,4), 'BJ': Q(1,6), 'IJ': Q(1,3)}
FC = list(product((Z, ONE), repeat=7))
LC = list(product((Z, ONE), repeat=3))
checks = evaluations = 0

def check(assertion, label):
    global checks
    checks += 1
    if not assertion:
        raise AssertionError(label)

def add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(4))

def scale(c, v):
    return tuple(c * a for a in v)

def stop(time):
    return (ONE, Z, Q(time), Q(time))

def answer(time, p, q):
    return (p, ONE-q, Q(time), Q(time))

def full(t, x, jB, jI, kC, kI, kBJ, kIJ):
    global evaluations
    evaluations += 1
    def knode(source, k):
        return add(scale(k, stop(3)),
                   scale(ONE-k, (HALF, HALF, Q(4)+t, Q(4)+Q_DELAY[source])))
    def jnode(source, j, k):
        daughter = 'BJ' if source == 'B' else 'IJ'
        return add(scale(j, stop(2)),
                   scale(ONE-j, add(scale(HALF, knode(daughter,k)),
                                    scale(HALF, answer(3,Q(3,5),Q(2,5))))))
    i = add(scale(x,stop(1)),scale(ONE-x,
            add(scale(HALF,jnode('I',jI,kIJ)),scale(HALF,knode('I',kI)))))
    return add(scale(HALF,i), scale(Q(1,4),jnode('B',jB,kBJ)),
               scale(Q(1,4),knode('C',kC)))

def lr(t,x,y,z):
    return full(t,x,y,y,z,z,z,z)

def normal(t):
    return (Q(15)-72*t,Q(10)-48*t,Q(-12),Q(12))

def score(t,v):
    return sum(a*b for a,b in zip(normal(t),v))

def full_formula(x,jB,jI,kC,kI,kBJ,kIJ):
    return (jB+(ONE-jB)*kBJ+4*kC
            -(ONE-x)*(3*(jI+kIJ-jI*kIJ)+2*kI)-5*x)/16

def lr_formula(x,y,z):
    return -(ONE-z)*(2*y+x*(5-3*y))/16

def det(rows):
    m = [list(row) for row in rows]
    val = ONE
    for i in range(len(m)):
        idx=next((j for j in range(i,len(m)) if m[j][i]),None)
        if idx is None:
            return Z
        if idx != i:
            m[i],m[idx]=m[idx],m[i]
            val=-val
        pivot=m[i][i]
        val*=pivot
        for j in range(i+1,len(m)):
            fac=m[j][i]/pivot
            for k in range(i+1,len(m)):
                m[j][k]-=fac*m[i][k]
            m[j][i]=Z
    return val

def rank_certificates(t):
    qkeys=[(Z,Z,Z),(Z,Z,ONE),(Z,ONE,Z),(ONE,Z,Z),(ONE,Z,ONE)]
    pts=[lr(t,*key) for key in qkeys]
    ld=det([[pts[j][i]-pts[0][i] for j in range(1,5)] for i in range(4)])
    center=[HALF]*7
    cols=[]
    for j in (0,1,2,3):
        a=center.copy();b=center.copy();a[j]=ONE;b[j]=Z
        va,vb=full(t,*a),full(t,*b)
        cols.append([va[i]-vb[i] for i in range(4)])
    fd=det([[cols[j][i] for j in range(4)] for i in range(4)])
    return ld,fd

check(len(FC)==128 and len(LC)==8,'complete deterministic strategy count')
for q in Q_DELAY.values():
    check(Z<q<ONE,'strict natural terminal Q probability')
for t in (Z,Q(1,4),HALF,Q(3,4),ONE):
    n=normal(t)
    base=Q(15)-72*t
    fl=[(key,full(t,*key)) for key in FC]
    ll=[(key,lr(t,*key)) for key in LC]
    for key,v in fl:
        check(score(t,v)-base==full_formula(*key),'FULL score identity')
        check(Z<=v[0]<=ONE and Z<=v[1]<=ONE,'FULL physical answers')
    for key,v in ll:
        check(score(t,v)-base==lr_formula(*key),'LR score identity')
        check(Z<=v[0]<=ONE and Z<=v[1]<=ONE,'LR physical answers')
    hf=max(score(t,v) for _,v in fl)
    hl=max(score(t,v) for _,v in ll)
    check(hl==base and hf==base+Q(5,16),'exact supports')
    ld,fd=rank_certificates(t)
    check(ld==Q(3,8192),'LR affine determinant')
    check(fd==-Q(1,81920),'FULL center Jacobian minor')
    print('node',str(t),'n',normal(t),'hFULL',hf,'hLR',hl,
          'gap',hf-hl,'LR_det',ld,'FULL_minor',fd)

# Every behavioral score is multiaffine; each fixed-behavior score
# difference has polynomial degree <=2 in t. The exact 5 nodes certify
# its identity for all real t. Each determinant has degree <=4 in t,
# so 5 exact nodes certify the constant rank formula for all real t.
for t in (Q(1,7),Q(5,24),Q(2,3),Q(6,7)):
    x,jB,jI,kC,kI,kBJ,kIJ=(Q(1,3),Q(2,7),Q(4,7),Q(3,8),Q(5,9),Q(1,5),Q(7,9))
    f=full(t,x,jB,jI,kC,kI,kBJ,kIJ)
    check(score(t,f)-(Q(15)-72*t)==full_formula(x,jB,jI,kC,kI,kBJ,kIJ),
          'real interior FULL formula')
    l=lr(t,Q(2,5),Q(4,9),Q(3,8))
    check(score(t,l)-(Q(15)-72*t)==lr_formula(Q(2,5),Q(4,9),Q(3,8)),
          'real interior LR formula')

Wkey=(Z,Z,Z,ONE,Z,ONE,Z)
for t in (Q(1,7),Q(5,24),HALF,Q(6,7)):
    W=full(t,*Wkey)
    expected=(Q(57,80),Q(27,80),3*(t+9)/8,Q(167,48))
    check(W==expected,'explicit FULL witness')
    check(score(t,W)==Q(15)-72*t+Q(5,16),'witness exact support')
    check(Z<t<ONE,'strict positive representative')
    bound=Q(5,16)/(5*abs(5-24*t)+24)
    print('witness at t=',t,'W=',W,'infinity-distance-lower-bound=',bound)

check(normal(Q(5,24))==(Z,Z,Q(-12),Q(12)),'pure-time phase normal')
check(Q(5,16)/12==Q(5,192),'pure-time support gap')
print('certified parameter domain t in (0,1) for strict positivity; [0,1] algebraic extension')
print('five exact degree-4 interpolation nodes; 128 FULL, 8 LR corner strategies/node')
print('checks',checks,'complete_flow_evaluations',evaluations)
print('PASS_EXACT_R5_COMMON_P_DELAY_ROTATING_OBSTRUCTION_AND_RANK4')
