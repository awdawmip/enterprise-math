#!/usr/bin/env python3
"""Exact fractions verifier for R5 multi-origin one-collision stop-loss theorem.
Scientific scope: finite two-law stop/continue/declare model, no native X6 simulation.
"""
from fractions import Fraction as F
from itertools import product

S = tuple(map(F, (F(1,2), F(3,4), F(5,4), F(3,2))))
Q = (
    (F(1,5), F(3,10), F(3,10), F(1,5)),
    (F(3,10), F(1,5), F(1,5), F(3,10)),
    (F(1,4), F(1,4), F(1,4), F(1,4)),
)
ORIGIN_WEIGHTS = tuple(F(1,3) for _ in Q)
ZERO=F(0)
ONE=F(1)

def dot(u,v):
    return sum((x*y for x,y in zip(u,v)), ZERO)

def F_kernel(row, a, b):
    return sum((p*min(a*s,b) for p,s in zip(row,S)), ZERO)

def bellman(a,b,c,d):
    h=c+d
    stop=min(a,b)+h
    D=tuple(h+F_kernel(row,a,b)-min(a,b) for row in Q)
    full=stop+sum((w*min(ZERO,z) for w,z in zip(ORIGIN_WEIGHTS,D)),ZERO)
    lr=stop+min(ZERO,dot(ORIGIN_WEIGHTS,D))
    return full,lr,D

def plan_vector(row, plan):
    # Per-unit (Q=P=1) origin contribution: four-vector eP,eQ,TP,TQ
    if plan=='STOP_P': return (ZERO,ONE,ONE,ONE)
    if plan=='STOP_Q': return (ONE,ZERO,ONE,ONE)
    bits=plan
    return (sum((p*s for p,s,declare_p in zip(row,S,bits) if not declare_p),ZERO),
            sum((p for p,declare_p in zip(row,bits) if declare_p),ZERO),
            F(2),F(2))

PLANS=('STOP_P','STOP_Q')+tuple(product((False,True),repeat=len(S)))
ORIGIN_PLANS=tuple(tuple(plan_vector(row,p) for p in PLANS) for row in Q)

def aggregate(vectors):
    return tuple(sum((w*v[k] for w,v in zip(ORIGIN_WEIGHTS,vectors)),ZERO) for k in range(4))

LR_VECTORS=tuple(aggregate(tuple(vals[j] for vals in ORIGIN_PLANS)) for j in range(len(PLANS)))

def enumerate_min(w):
    full=sum((weight*min(dot(w,v) for v in vecs) for weight,vecs in zip(ORIGIN_WEIGHTS,ORIGIN_PLANS)),ZERO)
    lr=min(dot(w,v) for v in LR_VECTORS)
    return full,lr

assert sum(ORIGIN_WEIGHTS)==ONE
for row in Q:
    assert all(v>0 for v in row)
    assert sum(row)==ONE
    assert dot(row,S)==ONE # Positive P kernel s*Q, mean likelihood 1

# Central explicit source/path positivity and witness
w=(ONE,ONE,F(3,16),ZERO)
full,lr,Ds=bellman(*w)
assert Ds==(F(1,80),-F(1,80),ZERO)
assert (full,lr,lr-full)==(F(71,60),F(19,16),F(1,240))
assert enumerate_min(w)==(full,lr)
all_full=(aggregate(vs) for vs in product(*ORIGIN_PLANS))
assert min(dot(w,v) for v in all_full)==full
bits=(False,False,True,True)
witness=aggregate((plan_vector(Q[0],'STOP_Q'), plan_vector(Q[1],bits), plan_vector(Q[2],'STOP_Q')))
assert witness==(F(23,30),F(1,6),F(4,3),F(4,3))
assert dot(w,witness)==full
assert (lr-full)/sum(map(abs,w))==F(1,525)

# Finite-breakpoint exact global max over t>=0 for a=1 and optimized h
support_values={}
for t in S:
    f=tuple(F_kernel(row,ONE,t) for row in Q)
    mean=dot(ORIGIN_WEIGHTS,f)
    spread=sum((weight*abs(value-mean) for weight,value in zip(ORIGIN_WEIGHTS,f)),ZERO)/2
    h=min(ONE,t)-mean
    assert h>=0
    fval,lval,_=bellman(ONE,t,h,ZERO)
    assert lval-fval==spread
    assert enumerate_min((ONE,t,h,ZERO))==(fval,lval)
    support_values[t]=spread
assert max(support_values.values())==F(1,240)

# Independently check general all-signed Bellman formula on an exact grid
count=0
for a in (F(-2),F(-1),ZERO,F(1),F(2)):
    for b in (F(-3,2),ZERO,F(3,4),F(1),F(2)):
        for c in (F(-1,2),ZERO,F(3,16),F(1,2)):
            for d in (F(-1,4),ZERO,F(1,4)):
                w2=(a,b,c,d)
                assert enumerate_min(w2)==bellman(*w2)[:2]
                count+=1
assert count==300

# New fixed-kernel structural test: if kernels identical, every full deterministic
# vector is exactly a convex combination of 18 seedless LR plan vectors.
for plans in product(range(len(PLANS)),repeat=3):
    same_vec=aggregate(tuple(plan_vector(Q[2],PLANS[i]) for i in plans))
    lrv=tuple(plan_vector(Q[2],p) for p in PLANS)
    mix=tuple(sum((ORIGIN_WEIGHTS[k]*lrv[plans[k]][j] for k in range(3)),ZERO) for j in range(4))
    assert same_vec==mix

print('PASS_EXACT_R5_MULTI_ORIGIN_STOP_LOSS')
print('origins:',len(Q),'terminal-signatures:',len(S),'policies-LR:',len(PLANS),'policies-full:',len(PLANS)**len(Q))
print('signed_grid_checked:',count)
print('all_signature_spreads:',','.join(f'{t}:{v}' for t,v in support_values.items()))
print('D_at_t1:',','.join(str(v) for v in Ds))
print('full_optimum:',full,'LR_optimum:',lr,'gap:',lr-full)
print('witness:',','.join(str(x) for x in witness))
print('linfty_distance_lower_bound:',F(1,525))
