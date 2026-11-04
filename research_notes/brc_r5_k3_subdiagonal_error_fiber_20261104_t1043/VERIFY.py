#!/usr/bin/env python3
"""Exact Fraction checks for the K3 uniform-clock subdiagonal error-fiber theorem.
This is an observer-model calculation over source-labelled finite BRC flows,
not a native X6 physical propagation/heartbeat calculation.
"""
from fractions import Fraction as F
from itertools import product

C=(F(1,8),F(1,6),F(1,16),F(3,32))
WSUM=sum(C)
E=F(1,100)
ONE=F(1)
ZERO=F(0)

def obs(x,y,i,st,r,v,p,q):
    """st stages in {0,1,2,3}, independently or shared across sources."""
    w=(C[0],C[1]*(1-x),C[2]*y,C[3]*i)
    d=w[2]+w[3]
    M=sum(w[s]*int(st[s]>=1) for s in range(4))
    Z=tuple(F(2,3)*w[s]*int(st[s]>=2) for s in range(4))
    U=sum(Z[s]*int(st[s]==3) for s in range(4))
    ztot=sum(Z)
    ep=F(107,128)-F(21,128)*x+d/4-ztot/2+sum(p[s]*Z[s] for s in range(4))/8
    eq=F(13,64)+F(3,64)*x-d/2+ztot/8+sum(q[s]*Z[s] for s in range(4))/32
    tp=3+M+F(3,2)*ztot+r*U
    tq=3+M/2+F(3,8)*ztot+v*U/4
    return (ep,eq,tp,tq)

def dot(n,z): return sum(n[i]*z[i] for i in range(4))

def all_full(r,v,p,q):
    for x,i in ((ZERO,ZERO),(ZERO,ONE),(ONE,ZERO)):
        for y in (ZERO,ONE):
            for st in product(range(4),repeat=4):
                yield (x,y,i,st),obs(x,y,i,st,r,v,p,q)

def all_lr(r,v,p,q):
    for x,y in product((ZERO,ONE),repeat=2):
        for stage in range(4):
            yield (x,y,stage),obs(x,y,(1-x)*y,(stage,)*4,r,v,p,q)

def witness_stage(which, probs):
    av=sum(C[s]*probs[s] for s in range(4))/WSUM
    if which=='P':
        selected=[s for s in range(4) if probs[s]<av]
    else:
        selected=[s for s in range(4) if probs[s]>av]
    st=tuple(2 if s in selected else 1 for s in range(4))
    return st,selected

def check(r,v,p,q,which):
    assert ZERO<v<=r<ONE
    assert all(ZERO<h<ONE for h in (*p,*q))
    probs=p if which=='P' else q
    avg=sum(C[s]*probs[s] for s in range(4))/WSUM
    if which=='P':
        k=E*(4-avg)/12
        n=(-E,ZERO,-F(1,4)-k,ONE)
        expected=E*sum(C[s]*(avg-probs[s]) for s in range(4) if probs[s]<avg)/12
    else:
        k=E*(4+avg)/48
        n=(ZERO,E,-F(1,4)-k,ONE)
        expected=E*sum(C[s]*(probs[s]-avg) for s in range(4) if probs[s]>avg)/48
    lr=list(all_lr(r,v,p,q)); full=list(all_full(r,v,p,q))
    assert len(lr)==16 and len(full)==1536
    lh=max(dot(n,vec) for _,vec in lr)
    fh=max(dot(n,vec) for _,vec in full)
    st,sel=witness_stage(which,probs)
    witness=obs(ZERO,ONE,ONE,st,r,v,p,q)
    assert fh==dot(n,witness),(which,'wrong witness',r,v,fh,dot(n,witness),st)
    assert fh-lh==expected,(which,r,v,fh-lh,expected)
    assert lh==dot(n,obs(ZERO,ONE,ONE,(1,)*4,r,v,p,q)),(which,'LR wrong endpoint',r,v,lh)
    assert expected>ZERO
    dist=expected/sum(abs(u) for u in n)
    print('CASE',which,'r=',r,'v=',v,'p=',','.join(map(str,p)),'q=',','.join(map(str,q)))
    print('  mean',avg,'normal',n,'selected_sources',sel,'FULL_witness_stages',st)
    print('  FULL_support',fh,'LR_support',lh,'gap',expected,'Linf_distance_lower_bound',dist)
    return expected,dist

if __name__=='__main__':
    ph=(F(1,4),F(1,3),F(2,3),F(3,4))
    qh=(F(3,4),F(1,5),F(2,5),F(4,5))
    eq=(F(1,2),)*4
    cases=[
        (F(2,3),F(1,3),ph,eq,'P'),
        (F(2,3),F(1,3),eq,qh,'Q'),
        (F(1,3),F(1,3),ph,eq,'P'),
        (F(1,3),F(1,3),eq,qh,'Q'),
        (F(7,8),F(1,9),ph,qh,'P'),
        (F(7,8),F(1,9),ph,qh,'Q'),
        (F(3,4),F(3,4),ph,qh,'P'),
        (F(3,4),F(3,4),ph,qh,'Q'),
    ]
    results=[check(*c) for c in cases]
    print('TOTAL_MODELS',len(cases),'FULL_DET',1536*len(cases),'LR_DET',16*len(cases))
    print('MIN_SUPPORT_GAP',min(g for g,_ in results))
    print('PASS_EXACT_R5_K3_UNIFORM_CLOCK_SUBDIAGONAL_ERROR_FIBERS')
