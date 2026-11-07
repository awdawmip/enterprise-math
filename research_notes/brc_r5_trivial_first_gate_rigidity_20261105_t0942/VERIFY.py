#!/usr/bin/env python3
"""Exact rational enumeration of the 2026-11-05 R5 degenerate first-gate BRC witness.
Uses Python standard-library Fraction only.  All masses remain exact fractions.
"""
from fractions import Fraction as F
from itertools import product

S = (F(1,2), F(1), F(3,2))
w = (F(1,2),F(1,2))
M = ((F(1,4),F(1,2),F(1,4)), (F(3,8),F(1,4),F(3,8)))
k=F(1)
c=F(5,64)
n=(-F(1),-k,-c,F(0))
STOP_P,STOP_Q,CONT = 0,1,2

def verify_laws():
    assert sum(w)==1
    for row in M:
        assert all(v>0 for v in row)
        assert sum(row)==1
        assert sum(s*q for s,q in zip(S,row))==1
        p=(s*q for s,q in zip(S,row))
        assert sum(p)==1

def observer(stage1,stage2,terminal):
    """stage1,stage2 tuples of 2 actions, terminal tuple of 2x3 declarations."""
    ep=eq=tp=tq=F(0)
    def account(q,r,t,action):
        nonlocal ep,eq,tp,tq
        pm=q*r
        tp+=pm*t; tq+=q*t
        if action==STOP_P: eq+=q
        elif action==STOP_Q: ep+=pm
        else: raise AssertionError('Must stop by time 3')
    for h in range(2):
        q=w[h]
        a1=stage1[h]
        if a1!=CONT:
            account(q,F(1),1,a1)
            continue
        a2=stage2[h]
        if a2!=CONT:
            account(q,F(1),2,a2)
            continue
        for j,s in enumerate(S):
            account(q*M[h][j],s,3,terminal[h][j])
    return ep,eq,tp,tq

def dot(n,o): return sum(a*b for a,b in zip(n,o))

def exact_support_enumerate():
    hLR=None; hFULL=None; count_lr=count_full=0
    for a1,a2 in product(range(3),repeat=2):
        for t in product(range(2),repeat=3):
            v=observer((a1,a1),(a2,a2),(t,t))
            value=dot(n,v)
            hLR=value if hLR is None else max(hLR,value)
            count_lr+=1
    for a in product(range(3), repeat=4):
        for tb in product(range(2), repeat=6):
            t=(tuple(tb[:3]),tuple(tb[3:]))
            v=observer(a[:2],a[2:],t)
            value=dot(n,v)
            hFULL=value if hFULL is None else max(hFULL,value)
            count_full+=1
    assert (count_lr,count_full)==(72,5184)
    return hFULL,hLR,count_full,count_lr

def bellman_support():
    def C(r): return max(-r,-k)
    gs=tuple(sum(prob*C(r) for prob,r in zip(row,S))-C(F(1)) for row in M)
    gbar=sum(ww*g for ww,g in zip(w,gs))
    baseline=C(F(1))-c
    full=baseline+sum(ww*max(g-2*c,0) for ww,g in zip(w,gs))
    lr=baseline+max(gbar-2*c,0)
    return gs,gbar,full,lr

def main():
    verify_laws()
    gs,gbar,bellfull,belllr=bellman_support()
    assert gs==(F(1,8),F(3,16))
    assert gbar==F(5,32)
    full,lr,nf,nl=exact_support_enumerate()
    assert (full,lr)==(bellfull,belllr)==(F(-17,16),F(-69,64))
    delta=full-lr
    assert delta==F(1,64)
    witness=observer((STOP_Q,CONT),(STOP_Q,CONT),((STOP_Q,STOP_Q,STOP_Q),(STOP_Q,STOP_P,STOP_P)))
    assert witness==(F(19,32), F(5,16),F(2),F(2))
    assert dot(n,witness)==full
    norm1=sum(abs(x) for x in n)
    assert norm1==F(133,64)
    assert delta/norm1==F(1,133)
    for tk in (F(0),F(1,16),F(1,8),F(5,32),F(3,16),F(1,4)):
        testn=(-F(1),-k,-tk/2,F(0))
        e_full=None; e_lr=None
        for a in product(range(3),repeat=4):
            for tb in product(range(2),repeat=6):
                val=dot(testn,observer(a[:2],a[2:],(tuple(tb[:3]),tuple(tb[3:]))))
                e_full=val if e_full is None else max(e_full,val)
        for a1,a2 in product(range(3),repeat=2):
            for t in product(range(2),repeat=3):
                val=dot(testn,observer((a1,a1),(a2,a2),(t,t)))
                e_lr=val if e_lr is None else max(e_lr,val)
        expfull=F(-1)-tk/2+sum(ww*max(g-tk,0) for ww,g in zip(w,gs))
        explr=F(-1)-tk/2+max(gbar-tk,0)
        assert (e_full,e_lr)==(expfull,explr),(tk,e_full,e_lr,expfull,explr)
    print('support FULL =', full, 'LR =',lr, 'gap =',delta)
    print('G_A, G_B, Gbar =',*gs,gbar)
    print('n =',n,'W =',witness,'||n||_1 =',norm1)
    print('dist_inf_lower_bound =',delta/norm1)
    print('enumerated full deterministic policies =',nf,'seedless LR =',nl)
    print('threshold grid exact checks = 6; complete policy enumeration repeated')
    print('PASS_EXACT_R5_DEGENERATE_FIRST_GATE_RIGIDITY')

if __name__=='__main__': main()
