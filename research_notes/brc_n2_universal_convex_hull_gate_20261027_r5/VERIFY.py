#!/usr/bin/env python3
"""R5: horizon-two seedless LR hull gate, exact rational witness and exhaustive objective check."""
from fractions import Fraction as F
from itertools import product

Y=(F(1,4),F(1),F(7,4))
KA=(F(2,5),F(1,5),F(2,5))
KB=(F(1,20),F(9,10),F(1,20))
K=(KA,KB)
Q0=(F(1,2),F(1,2))
assert all(v>0 for z in K for v in z)
assert all(sum(z)==1 and sum(y*q for y,q in zip(Y,z))==1 for z in K)
assert all(v>0 for z in K for v in [y*q for y,q in zip(Y,z)])

# All reachable first histories a,b have L_1=1; Q(root=>a,b)=P(root=>a,b)=1/2.
# P(terminal Y=y | h) = y * Q(Y=y | h).
def pure_obs(root, first, terminal):
    """root in {P,Q,C}, first[a/b] in {P,Q,C}, terminal[h][j] in {P,Q}."""
    if root != 'C':
        return ((F(1),F(0),F(0),F(0)) if root=='Q'
                else (F(0),F(1),F(0),F(0)))
    ep=eq=F(0)
    tp=tq=F(1)
    for q_h,kernel,action,decisions in zip(Q0,K,first,terminal):
        p_h=q_h
        if action=='P':
            eq+=q_h
        elif action=='Q':
            ep+=p_h
        else:
            tp+=p_h
            tq+=q_h
            for y,q_y,d in zip(Y,kernel,decisions):
                if d=='P':
                    eq+=q_h*q_y
                else:
                    ep+=p_h*y*q_y
    return(ep,eq,tp,tq)

def behavior_obs(root_c,first_c,first_stop_q,terminal_q):
    ep=F(0);eq=1-root_c
    for q_h,kernel in zip(Q0,K):
        eq+=root_c*q_h*(1-first_c)*(1-first_stop_q)
        ep+=root_c*q_h*(1-first_c)*first_stop_q
        for y,q_y,dec_q in zip(Y,kernel,terminal_q):
            qmass=root_c*q_h*first_c*q_y
            eq+=qmass*(1-dec_q)
            ep+=qmass*y*dec_q
    t=root_c+root_c*first_c
    return(ep,eq,t,t)

A=behavior_obs(F(1),F(1),F(0),(F(0),F(1),F(1)))
B=behavior_obs(F(1,2),F(2,3),F(1),(F(0),F(0),F(1)))
mid=tuple((a+b)/2 for a,b in zip(A,B))
C=behavior_obs(F(3,4),F(8,9),F(1),(F(0),F(3,4),F(1)))
assert mid==C==(F(149,240),F(59,120),F(17,12),F(17,12))

# 3 root actions, 3 first-step actions, and 2^3 terminal decisions.
def cost(v):return v[0]+v[1]+v[3]/16
comp_costs=[]; comp_vectors=set()
for root, first, choices in product(('P','Q','C'),('P','Q','C'),product(('P','Q'),repeat=3)):
    v=pure_obs(root,(first,first),(choices,choices))
    comp_costs.append(cost(v));comp_vectors.add(v)
assert len(comp_costs)==72
assert min(comp_costs)==F(153,160)

# 3 root actions, 3^2 branch-specific actions and 2^6 terminal decisions.
full_costs=[]
for root, ab, decisions in product(('P','Q','C'),product(('P','Q','C'),repeat=2),product(('P','Q'),repeat=6)):
    v=pure_obs(root,ab,(decisions[:3],decisions[3:]))
    full_costs.append(cost(v))
assert len(full_costs)==1728
assert min(full_costs)==F(151,160)
assert min(comp_costs)-min(full_costs)==F(1,80)
assert len(comp_vectors)>0

print('ALL EXACT CHECKS PASSED')
print('Q_kernels=',K)
print('P_kernels=',tuple(tuple(y*q for y,q in zip(Y,z)) for z in K))
print('O_A=',A)
print('O_B=',B)
print('O_average=',mid)
print('O_seedless_reconstruction=',C)
print('full_pure_descriptions=',len(full_costs),'compressed_pure_descriptions=',len(comp_costs))
print('distinct_compressed_pure_vectors=',len(comp_vectors))
print('J_full_min=',min(full_costs))
print('J_compressed_min=',min(comp_costs))
print('signed_support_gap=',min(comp_costs)-min(full_costs))
print('scope=finite-N2 rational test; universal convexity theorem has independent flow proof')
