#!/usr/bin/env python3
"""Exact four-stage positive P/Q BRC family: full-history vs seedless LR.
General all-delta conclusion uses the convex-envelope endpoint lemma in RESEARCH.md.
All endpoint and witness calculations here use fractions.Fraction only.
"""
from fractions import Fraction as F
from itertools import product

R2=(F(3,4),F(5,4)); Q2=(F(1,2),F(1,2))
R3=(F(1,2),F(1),F(3,2))
Q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
R4=(F(1,10),F(1),F(19,10))
N=(-F(1),-F(1),-F(3,25),F(1,50))
BASE_Q4={
 (0,0):(F(509,900),F(382,900),F(9,900)),
 (1,0):(F(509,900),F(382,900),F(9,900)),
 (0,2):(F(9,900),F(382,900),F(509,900)),
 (1,2):(F(9,900),F(382,900),F(509,900)),
 (0,1):(F(1,90),F(44,45),F(1,90)),
 (1,1):(F(67,162),F(14,81),F(67,162))}


def q4_at(delta):
    a=F(1,90)+delta
    out=dict(BASE_Q4)
    out[0,1]=(a,1-2*a,a)
    return out


def leaf(r,t,decision=None):
    def v(x):return (N[0]*r if x=='Q' else N[1])+(N[2]*r+N[3])*t
    return max(v('Q'),v('P')) if decision is None else v(decision)


def full_support(q4):
    def h3(i,j):
        r=R3[j]
        return max(leaf(r,3),sum(q4[i,j][k]*leaf(s,4) for k,s in enumerate(R4)))
    def h2(i):
        r=R2[i]
        return max(leaf(r,2),sum(Q3[i][j]*h3(i,j) for j in range(3)))
    return max(leaf(F(1),1),sum(Q2[i]*h2(i) for i in range(2)))


def deterministic_lr_value(q4,t1,t2,t3,t4):
    if t1!='C':return leaf(F(1),1,t1)
    total=F(0)
    for i,(r2,q2) in enumerate(zip(R2,Q2)):
        if t2[i]!='C':total+=q2*leaf(r2,2,t2[i]);continue
        for j,(r3,q3) in enumerate(zip(R3,Q3[i])):
            q=q2*q3
            if t3[j]!='C':total+=q*leaf(r3,3,t3[j]);continue
            total+=q*sum(q4[i,j][k]*leaf(s,4,t4[k]) for k,s in enumerate(R4))
    return total


def lr_support(q4):
    best=None;count=0
    for t1 in 'QPC':
     for t2 in product('QPC',repeat=2):
      for t3 in product('QPC',repeat=3):
       for t4 in product('QP',repeat=3):
        v=deterministic_lr_value(q4,t1,t2,t3,t4)
        best=v if best is None or v>best else best
        count+=1
    assert count==5832
    return best,count


def witness(q4,mode):
    # All witnesses continue at time1. Elsewhere use optimal Bayes declaration.
    # LR_LOW: stop at time2 history0, continue history1 and shared r3=1.
    # LR_HIGH: continue both histories and shared r3=1.
    # FULL_LOW: continue both histories; at r3=1 stop history0, continue history1.
    # FULL_HIGH: continue both histories and r3=1 on both paths.
    total=F(0)
    for i,(r2,q2) in enumerate(zip(R2,Q2)):
        if mode=='LR_LOW' and i==0:
            total+=q2*leaf(r2,2);continue
        for j,(r3,q3) in enumerate(zip(R3,Q3[i])):
            q=q2*q3
            cont=(j==1 and not(mode=='FULL_LOW' and i==0))
            if cont:total+=q*sum(q4[i,j][k]*leaf(s,4) for k,s in enumerate(R4))
            else:total+=q*leaf(r3,3)
    return total


def check_probabilities(q4,strict):
    assert sum(Q2)==1 and sum(Q2[i]*R2[i] for i in range(2))==1
    for i in range(2):
        assert sum(Q3[i])==1 and sum(Q3[i][j]*R3[j] for j in range(3))==R2[i]
        for j in range(3):
            row=q4[i,j]
            assert sum(row)==1 and sum(row[k]*R4[k] for k in range(3))==R3[j]
            assert all(x>0 if strict else x>=0 for x in row)

LEFT=-F(1,90); PIVOT=F(13,180); PIVOT2=F(1,10); RIGHT=F(22,45)
records=[]
for d in (LEFT,PIVOT,PIVOT2,RIGHT):
    q=q4_at(d);check_probabilities(q,strict=False)
    hL,count=lr_support(q);hF=full_support(q)
    records.append((d,hL,hF))
assert records==[(LEFT,-F(429,400),-F(107,100)),
                 (PIVOT,-F(429,400),-F(107,100)),
                 (PIVOT2,-F(107,100),-F(107,100)),
                 (RIGHT,-F(207,200),-F(207,200))]
# Affine lower witnesses meeting the convex endpoint upper bounds:
for d in (LEFT,PIVOT):assert witness(q4_at(d),'LR_LOW')==-F(429,400)
for d in (PIVOT,RIGHT):
    assert witness(q4_at(d),'LR_HIGH')==-F(429,400)+F(9,100)*(d-PIVOT)
for d in (LEFT,PIVOT2):assert witness(q4_at(d),'FULL_LOW')==-F(107,100)
for d in (PIVOT2,RIGHT):
    assert witness(q4_at(d),'FULL_HIGH')==-F(107,100)+F(9,100)*(d-PIVOT2)
for d in (-F(1,100),F(0),F(1,16),F(1,12),F(1,9),F(1,4),F(2,5)):
    assert LEFT<d<RIGHT
    q=q4_at(d);check_probabilities(q,strict=True)
    hL,count=lr_support(q);hF=full_support(q)
    expectedL=-F(429,400)+max(F(0),F(9,100)*(d-PIVOT))
    expectedF=-F(107,100)+max(F(0),F(9,100)*(d-PIVOT2))
    assert (hL,hF)==(expectedL,expectedF)
print('PASS_EXACT_R5_KERNAL_PERTURBATION_PHASE_DIAGRAM')
print('LR_policy_count_per_endpoint=5832, endpoints=4, interior_checks=7')
for d,hL,hF in records:
    print('endpoint delta=',str(d),'h_LR=',str(hL),'h_FULL=',str(hF),'gap=',str(hF-hL))
print('strict_positivity_interval= (-1/90,22/45)')
print('hLR= -429/400 + max(0,(9/100)*(delta-13/180))')
print('hFULL= -107/100 + max(0,(9/100)*(delta-1/10))')
print('gap= min(1/400,max(0,(9/100)*(1/10-delta)))')
print('all_real_delta_proof= affine policy payoffs + endpoint convex upper bound + fixed deterministic witnesses')
