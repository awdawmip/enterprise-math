#!/usr/bin/env python3
"""Exact p17 one-power q13(6,7) all-q0 moment classification. Serial integer arithmetic."""
from collections import defaultdict
from math import lcm
from bisect import bisect_right
from fractions import Fraction
import json

P = (2, 3, 5, 7, 11, 13, 17)
B = 2331

def smooth(n):
    for p in P:
        while n % p == 0:
            n //= p
    return n == 1

# Full admissible vertical catalog: denominators 17*(17q+r).
A = [(q,r,17*q+r,289*q+17*r-1) for q in range(1,8)
     for r in range(1,17) if smooth(17*q+r)]
assert len(A) == 60

# q0 denominators 17j, 17-adic valuation 1. The q6 minimum mass leaves 565,
# so j can reach floor((565+1)/17)=33, including 18,20,... and not only 1..16.
J = tuple(j for j in range(1,34) if smooth(j) and j % 17)
L = lcm(*(x[2] for x in A), *J)
assert L == 99891792000
atom = [(q,w,L//a,(L//a)**2) for q,r,a,w in A]

def vertical_rosters(order):
    out = []
    def walk(start, rem, mass, n, m1, m2, mask, indices):
        if rem == 0:
            out.append((mass,n,m1,m2,mask,tuple(indices)))
            return
        for i in range(start,len(atom)):
            q,w,x,y = atom[i]
            if q <= rem and mass+w <= B:
                indices.append(i)
                walk(i, rem-q, mass+w, n+1, m1+x, m2+y,
                     mask | (1<<i), indices)
                indices.pop()
    walk(0,order,0,0,0,0,0,[])
    return out

R6,R7 = vertical_rosters(6),vertical_rosters(7)
assert (len(R6),len(R7)) == (11105,1907)
assert min(v[0] for v in R6) == 1766
assert min(v[0] for v in R7) == 2039
max_q0_cost = B-min(v[0] for v in R6)
assert max_q0_cost == 565

# Generate all admissible named q0 multisets up to the larger q6 residual.
# Every j in 1..33 is visited; invalid j contributes multiplicity zero.
Q = []
def q0_walk(j,remaining,cost,n,m1,m2,mask,counts):
    if j == 34:
        Q.append((cost,n,m1,m2,mask,tuple(counts)))
        return
    unit = 17*j-1
    x = L//j if j in J else 0
    allowed = remaining//unit if j in J else 0
    for k in range(allowed+1):
        counts.append(k)
        q0_walk(j+1,remaining-k*unit,cost+k*unit,n+k,
                m1+k*x,m2+k*x*x,mask | ((1<<(j-1)) if k else 0),counts)
        counts.pop()
q0_walk(1,max_q0_cost,0,0,0,0,0,[])
Q.sort(key=lambda x:x[0])
assert len(Q) == 55811
qcost = [x[0] for x in Q]

# Exact H0/H1 key. Integer L/d is the cofactor-scaled reciprocal of the
# original denominator (the common factor 17 cancels between the two sides).
negative = defaultdict(list)
num_negative = 0
for v in R7:
    for q in Q[:bisect_right(qcost,B-v[0])]:
        negative[(v[1]+q[1], v[2]+q[2])].append((v,q))
        num_negative += 1
assert (num_negative,len(negative)) == (55347,47514)

num_positive=0; h01=0; h01_disjoint=0; h012=0; h012_nonempty_q0=0
survivors=[]
for v in R6:
    for q in Q[:bisect_right(qcost,B-v[0])]:
        num_positive += 1
        row=negative.get((v[1]+q[1],v[2]+q[2]),())
        h01 += len(row)
        for v2,q2 in row:
            if (v[4]&v2[4]) or (q[4]&q2[4]):
                continue
            h01_disjoint += 1
            if v[3]+q[3] != v2[3]+q2[3]:
                continue
            h012 += 1
            if q[1]+q2[1]:
                h012_nonempty_q0 += 1
            survivors.append((v,q,v2,q2))
assert (num_positive,h01,h01_disjoint,h012,h012_nonempty_q0) == (7050875,453914,17156,1,0)
v,q,v2,q2=survivors[0]
assert q[1] == q2[1] == 0
plus=tuple(sorted(A[i][2] for i in v[5]))
minus=tuple(sorted(A[i][2] for i in v2[5]))
assert (plus,minus) == ((21,30,84),(20,35,70))
assert (v[0],v2[0]) == (2292,2122)

def moment(k,cofactors):
    return sum((Fraction(17*a-1,17*a)**k for a in cofactors),Fraction(0))
delta3 = moment(3,plus)-moment(3,minus)
assert delta3 == Fraction(1,1083316500)
for k in range(3):
    assert moment(k,plus)==moment(k,minus)

cert={
 'schema':'T6_P17_ONE_POWER_Q13_SPLIT6_7_FULL_Q0_H013_CERT_V1',
 'task_id':'RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND',
 'scope':'ONE_POWER_MAXIMAL_P17_Q13_SPLIT6_7_FULL_NAMED_Q0',
 'budget_per_side':B,
 'scaled_reciprocal_lcm':L,
 'admissible_q0_j_range':[1,33],
 'admissible_q0_j_list':list(J),
 'vertical_rosters_q6_q7':[len(R6),len(R7)],
 'full_q0_multisets_up_to_565':len(Q),
 'all_side_combinations_q6_q7':[num_positive,num_negative],
 'H0H1_candidate_pairs_before_cancellation':h01,
 'H0H1_pairs_after_opposite_named_support_removal':h01_disjoint,
 'H0H1H2_survivors':h012,
 'H0H1H2_survivors_with_nonempty_q0':h012_nonempty_q0,
 'sole_H012_alias':{
   'q6_cofactors':list(plus), 'q7_cofactors':list(minus),
   'q6_denominators':[17*a for a in plus],
   'q7_denominators':[17*a for a in minus],
   'masses':[v[0],v2[0]],
   'q0_positive':[], 'q0_negative':[],
   'first_scaled_reciprocal_each':str(Fraction(13,140)),
   'second_scaled_reciprocal_each':str(Fraction(69,19600)),
   'original_H3_difference':str(delta3)
 },
 'H0_H1_H2_H3_collisions':0,
 'computation':'exact integer finite exhaustive scan; no affine solver',
 'status':'AUTHOR_EXACT_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED',
 'parent_objective':'OPEN'
}
print(json.dumps(cert,indent=2,ensure_ascii=False))
