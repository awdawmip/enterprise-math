#!/usr/bin/env python3
"""Exact three-policy obstruction for the frozen BRC N=4 S23 nine-label bank."""
from fractions import Fraction as F

M20 = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A=(0,0,0,1,1,1); B=(2,2,3,2,2,4); C=(5,6,7,8,9,10)
GROUP=(0,0,1,2,2,3)
SPECS=('34 24 34 24','34 23 34 34','34 34 34 23',
       '24 24 12 12','12 12 24 34','12 13 23 24',
       '23 34 12 13','24 34 12 14','13 12 13 13')
W=(F(1),F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0),F(0))
H=(F(1,3),F(1),F(0),F(0),F(0),F(1),F(0),F(1),F(0),F(0),F(0))
U=(F(0),F(0),F(1),F(0),F(1,3),F(0),F(0),F(0),F(0),F(0),F(1,2))
POLICIES=(('W',W),('H',H),('U',U))
SHARP=((F(1,3),F(1,3),F(1,3),F(0)),
       (F(1,3),F(1,3),F(0),F(1,3)),
       (F(1,3),F(1,3),F(0),F(1,3)),
       (F(2,3),F(1,3),F(0),F(0)))

def prepared(z):
    latent=[]
    for x in range(6):
        a,b,c=z[A[x]],z[B[x]],z[C[x]]
        latent.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
    return tuple(tuple(sum((F(M20[i][x],20)*latent[x][t] for x in range(6)),F(0))
                       for t in range(4)) for i in range(6))

def decoded(rows):
    return tuple(tuple(sum((F(M20[i][x],20)*rows[GROUP[x]][t] for x in range(6)),F(0))
                       for t in range(4)) for i in range(6))

def pair_rows(spec):
    result=[]
    for token in spec.split():
        row=[F(0)]*4
        for j in token: row[int(j)-1]+=F(1,2)
        result.append(tuple(row))
    return tuple(result)

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2

def loss(p,q):
    return max(tv(p[i],q[i]) for i in range(6))

BANK=tuple(decoded(pair_rows(spec)) for spec in SPECS)
assert len(BANK)==9 and all(sum(row)==1 and min(row)>=0 for row in SHARP)
assert all(sum(row)==1 for z in (W,H,U) for row in prepared(z))
EXPECTED=(F(1),F(2,3),F(2,3))
ATOMS=((F(0),F(0),F(0),F(1)),
       (F(1),F(0),F(0),F(0)),
       (F(0),F(1),F(0),F(0)))
for (name,z),want,atom in zip(POLICIES,EXPECTED,ATOMS):
    p=prepared(z)
    old=tuple(loss(p,q) for q in BANK)
    new=loss(p,decoded(SHARP))
    assert p[3]==atom, (name,p[3])
    assert min(old)==want, (name,old)
    assert new==F(2,3), (name,new)
    print(name,'original_nine_min='+str(min(old)),
          'new_tenth_loss='+str(new),'BU_prepared='+','.join(map(str,p[3])))
# For EVERY stochastic tenth decoder, grouped BU row q lies in Delta_4.
# Targets e4,e1,e2 give TV(e_j,q)=1-q_j. Since q1+q2+q4<=1,
# at least one of those three target errors is >=2/3.
assert max(F(1)-SHARP[2][j] for j in (3,0,1))==F(2,3)
print('SHARP_THREE_POLICY_INF_SUP=2/3; FULL_11D_FIXED_NINE_ANY_REAL_TENTH_LOWER=2/3')
print('PASS_BRC_N4_S23_FIXED_NINE_THREE_ATOM_2_3_20261101')
