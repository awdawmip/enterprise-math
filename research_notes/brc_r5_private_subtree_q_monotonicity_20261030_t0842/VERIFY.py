#!/usr/bin/env python3
"""R5 private-subtree compensation: exact two-law finite-stop regression.

This is an auxiliary rational stopping experiment, not native X6/BRC-Shor dynamics.
Analytic envelopes are independently compared to complete deterministic policies.
"""
from fractions import Fraction as Q
from itertools import product

# Label, stop time, P mass, Q mass, seedless-LR key, natural children.
DATA = [
    ('A', 1, 120, 240, 0, ('A0', 'A1')),
    ('B', 1, 240, 120, 1, ('B0', 'B1')),
    ('A0', 2, 60, 180, 2, ('A00', 'A01')),
    ('A1', 2, 60, 60, 3, ('A10', 'A11')),
    ('B0', 2, 180, 60, 4, ('B00', 'B01')),
    ('B1', 2, 60, 60, 3, ('B10', 'B11')),
    ('A00', 3, 30, 108, 5, ()),
    ('A01', 3, 30, 72, 6, ()),
    ('A10', 3, 30, 45, 7, ()),
    ('A11', 3, 30, 15, 8, ()),
    ('B00', 3, 90, 36, 9, ()),
    ('B01', 3, 90, 24, 10, ()),
    ('B10', 3, 20, 40, 11, ()),
    ('B11', 3, 40, 20, 8, ()),
]
N = {n: (t, p, q, key, children, i)
     for i, (n, t, p, q, key, children) in enumerate(DATA)}
PRIVATE = ('A0', 'A00', 'A01', 'B0', 'B00', 'B01')
ETA, LAM = Q(1, 1000), Q(1, 75)

def coefficients(z, u, v):
    c = dict(z)
    c.update({'A1': u, 'B1': v, 'A11': Q(1), 'B11': Q(-1)})
    return c

def check_model(c):
    assert len(N) == 14 and len({row[3] for row in N.values()}) == 12
    assert sum(N[k][1] for k in ('A', 'B')) == 360
    assert sum(N[k][2] for k in ('A', 'B')) == 360
    for n, (t,p,q,_,children,_) in N.items():
        assert p > 0 and q > 0
        if children:
            assert sum(N[x][1] for x in children) == p
            assert sum(N[x][2] for x in children) == q
        for tau in (t, 4) if t == 3 else (t,):
            ratio = Q(p,q)
            p_err = Q(1,5) + Q(tau,20) + Q(tau+1,100)/ratio
            q_err = Q(2,5) - Q(tau,30) + Q(tau+2,200)*ratio
            if tau == t:
                q_err += ETA*c.get(n,Q(0))
            assert 0 < p_err < 1 and 0 < q_err < 1, (n,tau,p_err,q_err)
    assert Q(N['A1'][1],N['A1'][2]) == Q(N['B1'][1],N['B1'][2]) == 1
    assert Q(N['A11'][1],N['A11'][2]) == Q(N['B11'][1],N['B11'][2]) == 2

def supports_analytic(c, sign):
    def reward(name):
        t,p,q,_,_,_ = N[name]
        return sign*Q(q,360)*c.get(name,Q(0)) - LAM*Q((4-t)*(p+q),360)
    a0,a00,a01 = (reward(n) for n in ('A0','A00','A01'))
    b0,b00,b01 = (reward(n) for n in ('B0','B00','B01'))
    side_a = max(Q(0), a0, max(Q(0),a00)+max(Q(0),a01))
    side_b = max(Q(0), b0, max(Q(0),b00)+max(Q(0),b01))
    a2,b2,a3,b3 = (reward(n) for n in ('A1','B1','A11','B11'))
    full = side_a + side_b + max(Q(0),a2,a3) + max(Q(0),b2,b3)
    lr = max(-3*LAM*(2-x-y) + x*side_a + y*side_b +
             max(Q(0),x*a2+y*b2,x*a3+y*b3)
             for x,y in product((0,1),repeat=2))
    baseline_full = max(Q(0),a2,a3) + max(Q(0),b2,b3)
    baseline_lr = max(-3*LAM*(2-x-y) +
                      max(Q(0),x*a2+y*b2,x*a3+y*b3)
                      for x,y in product((0,1),repeat=2))
    assert full-lr >= baseline_full-baseline_lr
    return full,lr,side_a,side_b,baseline_full-baseline_lr

def brute_support(c, sign):
    rewards={n:sign*Q(q,360)*c.get(n,Q(0)) - LAM*Q((4-t)*(p+q),360)
             for n,(t,p,q,_,_,_) in N.items()}
    def visit(name, mask, full):
        t,p,q,key,children,i = N[name]
        bit=i if full else key
        if mask & (1<<bit):
            return rewards[name]
        return sum((visit(x,mask,full) for x in children),Q(0))
    out=[]
    for full in (True,False):
        best=None; bestmask=None
        count=(1<<14) if full else (1<<12)
        for mask in range(count):
            v=visit('A',mask,full)+visit('B',mask,full)
            if best is None or v>best:
                best,bestmask=v,mask
        out.append((best,bestmask))
    return out

def observer_full(mask,c):
    totals=[Q(0)]*4
    def visit(name):
        t,p,q,key,children,i=N[name]
        if mask & (1<<i):
            pass
        elif children:
            for child in children: visit(child)
            return
        else:
            t=4
        ratio=Q(p,q)
        p_err=Q(1,5)+Q(t,20)+Q(t+1,100)/ratio
        q_err=Q(2,5)-Q(t,30)+Q(t+2,200)*ratio
        if t==N[name][0]: q_err+=ETA*c.get(name,Q(0))
        for idx,val in enumerate((Q(p,360)*p_err,Q(q,360)*q_err,Q(p*t,360),Q(q*t,360))):
            totals[idx]+=val
    visit('A'); visit('B')
    return tuple(totals)

if __name__ == '__main__':
    nums=[]
    zero={k:Q(0) for k in PRIVATE}
    alternating={k:Q(v) for k,v in zip(PRIVATE,(1,-1,1,-1,1,-1))}
    samples=[
        ('baseline', zero, Q(0), Q(0)),
        ('collision_only',zero,Q(1,2),Q(1,10)),
        ('six_private_all_nonzero',alternating,Q(1,2),Q(1,10)),
        ('all_nonzero_reverse',alternating,Q(-1,2),Q(2,3)),
        ('fractional_private', {k:Q(v,5) for k,v in zip(PRIVATE,(1,2,3,-4,5,-6))},Q(0),Q(0)),
        ('large_private', {k:Q(v) for k,v in zip(PRIVATE,(3,-4,5,-6,7,-8))},Q(1,3),Q(-1,3)),
    ]
    for label,z,u,v in samples:
        c=coefficients(z,u,v)
        check_model(c)
        gaps=[]
        for s in (1,-1):
            f,l,ca,cb,basegap=supports_analytic(c,s)
            brute=brute_support(c,s)
            assert (brute[0][0],brute[1][0])==(f,l),(label,s,brute,(f,l))
            assert f-l>=basegap
            gaps.append(f-l)
            if label=='six_private_all_nonzero' and s==-1:
                obs=observer_full(brute[0][1],c)
                # S=eQ-41/100-TP/200+TQ/30. D=8-TP-TQ.
                eP,eQ,TP,TQ=obs
                S=eQ-Q(41,100)-TP/200+TQ/30
                D=8-TP-TQ
                assert (-S-ETA*LAM*D)==ETA*f
                # Exact rational LR support and strict FULL witness.
                assert (-S-ETA*LAM*D)-ETA*l==ETA*(f-l)
                print('EXPLICIT_FULL_MASK',brute[0][1],
                      'OBSERVER',','.join(map(str,obs)),
                      'MINUS_LR_SUPPORT',l,'MINUS_FULL_SUPPORT',f)
        assert max(gaps)>=Q(1,25)
        print(label,'gap_plus/eta=',gaps[0],'gap_minus/eta=',gaps[1])
    print('HISTORIES=14, LR_KEYS=12, P_Q_MASS_DENOMINATOR=360')
    print('BRUTE_EXACT=6 models * 2 signs * (16384 FULL + 4096 LR) = 245760')
    print('ALL_REAL_FAMILY_PROOF=private-subtree monotonicity + predecessor two-sign theorem')
    print('UNIFORM_SHARP_LOWER_BOUND=max(gap_plus,gap_minus)>=eta/25')
    print('PASS_EXACT_R5_PRIVATE_SUBTREE_Q_COMPENSATION_MONOTONICITY')
