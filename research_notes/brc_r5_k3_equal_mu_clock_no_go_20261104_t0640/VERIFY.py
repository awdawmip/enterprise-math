#!/usr/bin/env python3
"""Exact Fraction enumeration for R5 K3 equal-threshold clock-hull separation.
All source probabilities strictly rational; this is an auxiliary finite two-law model.
"""
from fractions import Fraction as F
from itertools import product

SOURCES = ('C', 'I', 'BJ', 'IJ')
CAP = (F(1, 8), F(1, 6), F(1, 16), F(3, 32))
MASKS = ((), (0,), (0, 1), (0, 2), (0, 1, 2, 3))

def obs(x, y, i, stages, r, v, p, q):
    w = (F(1, 8), (1-x)/6, y/16, 3*i/32)
    d = y/16 + 3*i/32
    M = tuple(w[s] if stages[s] >= 1 else F(0) for s in range(4))
    Z = tuple(F(2, 3)*M[s] if stages[s] >= 2 else F(0) for s in range(4))
    U = tuple(Z[s] if stages[s] >= 3 else F(0) for s in range(4))
    eP = F(107,128)-F(21,128)*x+d/4-sum(Z)/2+sum(p[s]*Z[s] for s in range(4))/8
    eQ = F(13,64)+F(3,64)*x-d/2+sum(Z)/8+sum(q[s]*Z[s] for s in range(4))/32
    TP = 3+sum(M)+F(3,2)*sum(Z)+sum(r[s]*U[s] for s in range(4))
    TQ = 3+sum(M)/2+F(3,8)*sum(Z)+sum(v[s]*U[s] for s in range(4))/4
    return (eP,eQ,TP,TQ)

def value(o, tau): return o[3] - tau*o[2]

def fmt(o): return '[' + ', '.join(map(str,o)) + ']'

def run(label, mu, r, tau, p, q):
    v = tuple((8*mu*(3+t)-9)/2 for t in r)
    assert all(F(0)<t<1 for t in r+v+p+q)
    assert len(set(r))>1
    assert all((9+2*v[s])/(8*(3+r[s])) == mu for s in range(4))
    upstream_full = [(F(x), F(y), F(i)) for x in (0,1) for y in (0,1) for i in range(2-x)]
    upstream_lr = [(F(x), F(y), F((1-x)*y)) for x,y in product((0,1),repeat=2)]
    Fvec = [obs(x,y,i,st,r,v,p,q) for x,y,i in upstream_full for st in product(range(4),repeat=4)]
    Lvec = [obs(x,y,i,(st,)*4,r,v,p,q) for x,y,i in upstream_lr for st in range(4)]
    assert len(Fvec)==1536 and len(Lvec)==16
    A = F(1,2)-tau
    B = F(3,4)-2*tau
    C = tuple((F(3,4)+v[s]/6)-(2+F(2,3)*r[s])*tau for s in range(4))
    full_formula = 3*(1-tau)+sum(CAP[s]*max(F(0),A,B,C[s]) for s in range(4))
    lr_formula = 3*(1-tau)+max([F(0),sum(CAP)*A,sum(CAP)*B]+[sum(CAP[s]*C[s] for s in mask) for mask in MASKS])
    h_full = max(value(o,tau) for o in Fvec)
    h_lr = max(value(o,tau) for o in Lvec)
    assert h_full==full_formula and h_lr==lr_formula
    assert h_full>h_lr
    stages = tuple(max(range(4), key=lambda j: (F(0),A,B,C[s])[j]) for s in range(4))
    W = obs(F(0),F(1),F(1),stages,r,v,p,q)
    assert value(W,tau)==h_full
    assert len(set(stages))>1
    lower=(h_full-h_lr)/(1+tau)
    assert lower>0
    print(label, 'mu=',mu,'tau=',tau,'r=',fmt(r),'v=',fmt(v))
    print(' stages=',stages,'F_count=',len(Fvec),'LR_count=',len(Lvec))
    print(' normal=(0,0,-%s,1)'%tau,'h_FULL=',h_full,'h_LR=',h_lr,'gap=',h_full-h_lr)
    print(' W=',fmt(W),'dist_inf_lower=',lower)
    return h_full-h_lr

if __name__ == '__main__':
    p=(F(1,4),F(1,3),F(2,3),F(3,4)); q=(F(3,4),F(2,3),F(1,3),F(1,4))
    run('SUBCRITICAL',F(1,3),(F(1,2),F(3,5),F(3,4),F(9,10)),F(1,7),p,q)
    run('CROSSING',F(7,20),(F(3,10),F(1,2),F(4,5),F(9,10)),F(1,4),p,q)
    run('CRITICAL',F(3,8),(F(1,5),F(1,3),F(1,2),F(3,5)),F(11,40),(F(1,2),)*4,(F(1,2),)*4)
    run('SUPERCRITICAL',F(2,5),(F(1,10),F(1,5),F(1,4),F(2,5)),F(5,16),p,q)
    print('PASS_EXACT_R5_K3_COMMON_MU_HETEROGENEITY_NO_GO')
