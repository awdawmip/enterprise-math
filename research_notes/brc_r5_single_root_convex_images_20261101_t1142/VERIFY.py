#!/usr/bin/env python3
"""Exact rational regression for the root-collision convex-image theorem.
A finite model check is not the proof of the universal theorem.
"""
from fractions import Fraction as F
from itertools import product

def det(mat):
    a = [[F(x) for x in row] for row in mat]
    n = len(a)
    out = F(1)
    for i in range(n):
        j = next((j for j in range(i, n) if a[j][i]), None)
        if j is None:
            return F(0)
        if j != i:
            a[i], a[j] = a[j], a[i]
            out = -out
        pivot = a[i][i]
        out *= pivot
        for j in range(i+1, n):
            ratio = a[j][i] / pivot
            for k in range(i, n):
                a[j][k] -= ratio * a[i][k]
    return out

def observable_tree(p0, pL, pH, law_low):
    # terminal masses: stop now, stop low, continue low, stop high, continue high
    v = [p0, (1-p0)*law_low*pL, (1-p0)*law_low*(1-pL),
         (1-p0)*(1-law_low)*pH, (1-p0)*(1-law_low)*(1-pH)]
    assert sum(v) == 1
    return tuple(v)

def bary_mix_policy(pa, pb, lam):
    a0, aL, aH = pa
    b0, bL, bH = pb
    p0 = lam*a0 + (1-lam)*b0
    reach = lam*(1-a0) + (1-lam)*(1-b0)
    if reach:
        pL = (lam*(1-a0)*aL + (1-lam)*(1-b0)*bL)/reach
        pH = (lam*(1-a0)*aH + (1-lam)*(1-b0)*bH)/reach
    else:
        pL = pH = F(0)
    return p0, pL, pH

checks = 0
rvals = [F(0), F(1,3), F(1,2), F(1)]
for pa0,paL,paH,pb0,pbL,pbH,lam in product(rvals, repeat=7):
    pa=(pa0,paL,paH); pb=(pb0,pbL,pbH)
    mixed=bary_mix_policy(pa,pb,lam)
    for kernel in (F(1,3), F(2,3)):
        o=observable_tree(*mixed,kernel)
        a=observable_tree(*pa,kernel)
        b=observable_tree(*pb,kernel)
        assert all(o[j]==lam*a[j]+(1-lam)*b[j] for j in range(5))
        checks+=1
print('DUAL_LAW_FLOW_MIX_CHECKS', checks)

# Dimension-four example K1=K2=conv(e1,e2,e3,e4): the LR actual image
# is 2*conv(0,K). Every FULL point a1*v1+a2*v2 is explicitly LR-realizable.
bary = [tuple(F(i,3) for i in ix) for ix in product(range(4),repeat=4) if sum(ix)==3]
assert len(bary)==20
scalars=[F(0),F(1,5),F(1,2),F(4,5),F(1)]
recon=0
for a1,a2 in product(scalars,repeat=2):
    for v1,v2 in product(bary,repeat=2):
        lhs=tuple(a1*v1[j]+a2*v2[j] for j in range(4))
        a=(a1+a2)/2
        v=tuple((a1*v1[j]+a2*v2[j])/(a1+a2) for j in range(4)) if (a1+a2) else bary[0]
        assert sum(v)==1 and all(x>=0 for x in v)
        assert lhs==tuple(2*a*v[j] for j in range(4))
        recon+=1
assert det([[F(2) if j==i else F(0) for j in range(4)] for i in range(4)])==16
print('FULL_TO_LR_RANK4_EXACT_RECONSTRUCTIONS', recon)
print('LR_FOUR_DIMENSIONAL_DETERMINANT', 16)

# Opposite support signs produce a genuine fixed-root gap.
alpha1=F(1);alpha2=F(-1)
gap=max(0,alpha1)+max(0,alpha2)-max(0,alpha1+alpha2)
assert gap==1
print('OPPOSITE_SIGN_SUPPORT_GAP', gap)

# The bilinear graph is a rank-four abstract mechanism; it is NOT a
# typed (eP,eQ,TP,TQ) stopping-process realization.
base=(F(0),)*4
p1=(F(1),F(0),F(0),F(0))
p2=(F(0),F(1),F(0),F(0))
p3=(F(1),F(1),F(1),F(0))
p4=(F(0),F(0),F(0),F(1))
rank=det([[p[j]-base[j] for j in range(4)] for p in (p1,p2,p3,p4)])
assert rank==1
half=tuple((base[j]+p3[j])/2 for j in range(4))
assert half[2] != half[0]*half[1]
print('ABSTRACT_BILINEAR_HULL_DETERMINANT',rank)
print('ABSTRACT_BILINEAR_MIDPOINT_VIOLATION',half[2]-half[0]*half[1])
print('PASS_EXACT_R5_SINGLE_ROOT_COLLISION_CONVEX_IMAGE_AND_DUAL_LAW_FLOW')
