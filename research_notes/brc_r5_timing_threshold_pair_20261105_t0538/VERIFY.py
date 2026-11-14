#!/usr/bin/env python3
"""Exact rational finite BRC support verification; no floating arithmetic.
Lawful P/Q transition kernels: Q_1(h)=P_1(h)=1/2; Q_2(r|h)=K_h(r),
P_2(r|h)=r*K_h(r); Q_3(s|r)=1/2, P_3(s|r)=s/(2r).
At t1 and t2 actions STOP/P, STOP/Q, CONTINUE; at t3 P/Q freely.
"""
from fractions import Fraction as F

r = tuple(map(F, ["1/4", "1/2", "1", "3/2", "7/4"]))
KA = tuple(F(v,1000) for v in (209,184,214,184,209))
KB = tuple(F(v,1000) for v in (191,216,186,216,191))
K0 = tuple(F(1,5) for _ in r)
D = (9,-16,14,-16,9)
w = (F(1,2), F(1,2))
eta = F(1,100)
k = F(3,4)
lam = F(3,20)

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def check_kernel(K):
    assert all(q>0 for q in K)
    assert sum(K)==1 and dot(r,K)==1

for K in (KA,KB,K0):
    check_kernel(K)
assert tuple(KA[i]-K0[i] for i in range(5))==tuple(F(x,1000) for x in D)
assert tuple(KB[i]-K0[i] for i in range(5))==tuple(F(-x,1000) for x in D)
assert sum(D)==dot(r,D)==0

terminal=[]
for x in r:
    s0=x*(1-eta); s1=x*(1+eta)
    # all nature probabilities are strictly positive and normalized under P and Q
    assert s0>0 and s1>0
    assert (s0+s1)/(2*x)==1
    terminal.append((s0,s1))
assert len(set(v for pair in terminal for v in pair))==10

# A unit of Q mass at a node of likelihood ratio x. n=(eP,eQ,TP,TQ).
def stop_score(n,t,x):
    return max(n[0]*x,n[1]) + t*(n[2]*x+n[3])

def terminal_score(n,x):
    return stop_score(n,3,x)

def next_score(n,j):
    x=r[j]
    continued=(terminal_score(n,terminal[j][0])+terminal_score(n,terminal[j][1]))/2
    return max(stop_score(n,2,x),continued)

def supports(n):
    s=stop_score(n,1,F(1))
    values=[dot(K,tuple(next_score(n,j) for j in range(5))) for K in (KA,KB)]
    hf=dot(w,tuple(max(s,c) for c in values))
    hl=max(s,dot(w,values))
    assert hf>=hl
    return hf,hl,values,s

# General two-threshold timing-only classification. For all signs of (a,b),
# the two kernels have the same first-gate action preference.
tm=F(23,28); tp=F(33,28)
def tail_left(K,t): return sum((q*max(F(0),t-x) for q,x in zip(K,r)),F(0))
def tail_right(K,t): return sum((q*max(F(0),x-t) for q,x in zip(K,r)),F(0))
for K in (K0,KA,KB):
    assert tm-1+tail_left(K,tm)==0
    assert 1-tp+tail_right(K,tp)==0
assert sum((F(x)*max(F(0),tm-v) for x,v in zip(D,r)),F(0))==0
assert sum((F(x)*max(F(0),v-tp) for x,v in zip(D,r)),F(0))==0

count=0
for a in range(-24,25):
    for b in range(-24,25):
        hf,hl,_,_=supports((F(0),F(0),F(a),F(b)))
        assert hf==hl, (a,b,hf,hl)
        count+=1

# For n=(-1,-3/4,-3/20,0), going t2->t3 is always strictly dominated:
# Bayes reduction <= eta*x < lam*x for every r=x.
n=(-F(1),-k,-lam,F(0))
for j,x in enumerate(r):
    assert next_score(n,j)==stop_score(n,2,x)
    assert lam>eta

def bayes_gain(K):
    return min(F(1),k)-sum((q*min(x,k) for x,q in zip(r,K)),F(0))
assert bayes_gain(KA)==F(301,2000)
assert bayes_gain(KB)==F(299,2000)
assert (bayes_gain(KA)+bayes_gain(KB))/2==lam
hf,hl,values,s=supports(n)
assert hf==F(-3599,4000), (hf,values,s)
assert hl==F(-9,10), hl
assert hf-hl==F(1,4000)

# FULL witness: A continues at t1, at t2 declares Q on r<k, P on r>k;
# B stops and declares P at t1. Both share likelihood ratio 1 at t1.
eP=sum((w[0]*r[j]*KA[j] for j in range(5) if r[j]<k),F(0))
eQ=w[1]+sum((w[0]*KA[j] for j in range(5) if r[j]>k),F(0))
TP=TQ=F(3,2)
W=(eP,eQ,TP,TQ)
assert W==(F(577,8000),F(1607,2000),F(3,2),F(3,2)),W
assert dot(n,W)==hf
assert dot(n,W)-hl==F(1,4000)
assert dot(tuple(abs(x) for x in n),(F(1),)*4)==F(19,10)
distance_lower_bound=(hf-hl)/sum(map(abs,n))
assert distance_lower_bound==F(1,7600)

print('PASS_EXACT_R5_TIMING_THRESHOLD_BYPASS_WITH_ERROR_SEPARATION')
print('kernel_A',tuple(map(str,KA)))
print('kernel_B',tuple(map(str,KB)))
print('common_timing_threshold_minus',tm)
print('common_timing_threshold_plus',tp)
print('time_directions_checked',count)
print('bayes_gain_A',bayes_gain(KA),'bayes_gain_B',bayes_gain(KB))
print('mixed_direction',tuple(map(str,n)))
print('full_support',hf,'LR_support',hl,'gap',hf-hl)
print('FULL_witness',tuple(map(str,W)))
print('L_infinity_distance_lower_bound',distance_lower_bound)
