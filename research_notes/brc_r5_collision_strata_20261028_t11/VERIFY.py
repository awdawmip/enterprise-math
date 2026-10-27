"""Exact finite exhaustive support and information-partition verification.

Research scope: external sequential P/Q observer; this is not X6 native
motion or BRC-Shor arithmetic. Run with Python 3 stdlib only.
"""
from fractions import Fraction as F
from itertools import product

EPS = F(1, 10000)
LAMBDA = (912, 456, 128, -194)
ROOTS = ('A', 'B')
C_TERMS = ('A_low', 'A_high', 'B_low', 'B_high')
ACT = ('P', 'Q', 'cont')
STOP = ('P', 'Q')


def model(mode):
    """(group, t2 state, terminal identifier, P leaf mass, Q leaf mass)."""
    rows = [
        ('A','C','low', F(1,24), F(1,12)),
        ('A','C','high',F(1,8), F(1,12)),
        ('A','L','side',F(1,12), F(1,3)),
        ('B','C','low', F(1,32), F(1,8)),
        ('B','C','high',F(7,32), F(1,8)),
        ('B','H','side',F(1,2), F(1,4)),
    ]
    if mode == 'tangential':
        # Keep Q(A,C) fixed: collision persists, terminal kernel changes.
        shifts = {0: EPS, 1: -EPS}
    elif mode == 'transverse':
        # Change Q(A,C) while keeping Q(A) fixed: collision splits.
        shifts = {0: EPS, 2: -EPS}
    elif mode == 'original':
        shifts = {}
    else:
        raise ValueError(mode)
    rows = [(g,n,z,p,Q + shifts.get(i,F(0)))
            for i,(g,n,z,p,Q) in enumerate(rows)]
    assert all(p > 0 and q > 0 for _,_,_,p,q in rows)
    assert sum(p for *_,p,q in rows) == 1
    assert sum(q for *_,p,q in rows) == 1
    return rows


def prefix_signatures(rows):
    signatures = {}
    # The root time-1 history is either A or B.
    for g in ROOTS:
        P = sum(p for group,_,_,p,q in rows if group == g)
        Q = sum(q for group,_,_,p,q in rows if group == g)
        signatures[(1,g)] = P / Q
    # t2 history includes group and second-stage observed choice C/L/H.
    for g,n in (('A','C'),('A','L'),('B','C'),('B','H')):
        P = sum(p for gg,nn,_,p,q in rows if (gg,nn)==(g,n))
        Q = sum(q for gg,nn,_,p,q in rows if (gg,nn)==(g,n))
        signatures[(2,g,n)] = P / Q
    for g,n,z,p,q in rows:
        if n == 'C':
            signatures[(3,g,n,z)] = p / q
    return signatures


def check_partition(signatures, mode):
    for t in (1,2,3):
        seq = [(h,r) for h,r in signatures.items() if h[0]==t]
        collisions = [(h,k) for i,(h,r) in enumerate(seq)
                      for k,s in seq[i+1:] if r == s]
        if t==2 and mode!='transverse':
            assert collisions == [((2,'A','C'),(2,'B','C'))], collisions
        else:
            assert collisions == [], (mode,t,collisions)
    ac=signatures[(2,'A','C')]
    bc=signatures[(2,'B','C')]
    return ac==bc, ac, bc


def observation(rows, a_t1, a_c, a_side, a_t3):
    out=[F(0),F(0),F(0),F(0)]
    for group,node,z,p,q in rows:
        i = ROOTS.index(group)
        if a_t1[i] != 'cont':
            time=1; decision=a_t1[i]
        elif node!='C':
            time=2; decision=a_side[i]
        elif a_c[i]!='cont':
            time=2; decision=a_c[i]
        else:
            time=3; decision=a_t3[C_TERMS.index(group+'_'+z)]
        if decision=='Q': out[0]+=p
        else: out[1]+=q
        out[2]+=p*time
        out[3]+=q*time
    return tuple(out)


def score(o):
    return sum(a*b for a,b in zip(o,LAMBDA))


def all_observations(rows, collide):
    complete=set(); compressed=set()
    all_c=list(product(ACT, repeat=2))
    compressed_c=[(c,c) for c in ACT] if collide else all_c
    for a_t1 in product(ACT,repeat=2):
        for a_side in product(STOP,repeat=2):
            for a_t3 in product(STOP,repeat=4):
                for a_c in all_c:
                    complete.add(observation(rows,a_t1,a_c,a_side,a_t3))
                for a_c in compressed_c:
                    compressed.add(observation(rows,a_t1,a_c,a_side,a_t3))
    assert compressed <= complete
    return complete, compressed


def run(mode):
    rows=model(mode)
    sig=prefix_signatures(rows)
    collide,ra,rb=check_partition(sig,mode)
    full,lr=all_observations(rows,collide)
    vmax_full=max(score(o) for o in full)
    vmax_lr=max(score(o) for o in lr)
    assert vmax_full >= vmax_lr
    return {'mode':mode,'collision':collide,'AC_R2':ra,'BC_R2':rb,
            'full_count':len(full),'lr_count':len(lr),
            'max_full':vmax_full,'max_LR':vmax_lr,
            'support_gap':vmax_full-vmax_lr,
            'observable_sets_equal':full == lr}

if __name__=='__main__':
    data=[run(name) for name in ('original','tangential','transverse')]
    for x in data:
        print('MODEL',x['mode'])
        for k,v in x.items():
            if k!='mode': print(' ',k,'=',v)
    assert data[0]['max_full']==868 and data[0]['max_LR']==857
    assert data[0]['full_count']==196 and data[0]['lr_count']==124
    # This exact equal support gap is stronger than the general bound.
    assert data[1]['max_full']==868 and data[1]['max_LR']==F(1071307,1250)
    assert data[1]['support_gap']==F(13693,1250)
    assert data[2]['max_full']==F(1084943,1250)
    assert data[2]['max_LR']==F(1084943,1250)
    assert data[2]['support_gap']==0
    assert data[2]['observable_sets_equal']
    assert EPS==F(1,10000)
    assert F(11)-F(1688)*EPS==F(13539,1250)
    print('TANGENTIAL LOWER BOUND =', F(13539,1250))
    print('ALL EXACT STRATIFIED COLLISION CHECKS PASSED')
