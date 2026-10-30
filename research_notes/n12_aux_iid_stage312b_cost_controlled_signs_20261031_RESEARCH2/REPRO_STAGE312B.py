#!/usr/bin/env python3
"""Stage312-B exact-rational evidence for a FULL eight-real-rate Pareto interval.

All checks use fractions.Fraction. Finite enumeration checks 128 rational (S,h,bits)
atoms for MAP and witnesses; the continuum proof is in PROOF_STAGE312B.md.
"""
from fractions import Fraction as F
from itertools import product

P = (F(1, 4), F(3, 4))
M = {
    (0, 0, 0): (63, 1), (0, 0, 1): (21, 3),
    (0, 1, 0): (21, 3), (0, 1, 1): (7, 9),
    (1, 0, 0): (9, 7), (1, 0, 1): (3, 21),
    (1, 1, 0): (3, 21), (1, 1, 1): (1, 63),
}
assert len(M) == 8 and sum(a + b for a, b in M.values()) == 256
assert all(a > 0 and b > 0 and a != b for a, b in M.values())
assert max(F(a+b, abs(a-b)) for a,b in M.values()) == 8

U = F(3, 50)
R = F(3, 25)
def q(u): return F(9,128)*u + F(3,32)*u*u - F(1,8)*u**3
def g(u): return F(117,4096)*u - F(123,1024)*u*u + F(23,256)*u**3
def A(z): return 1-3*z*z+2*z**3
def B(z,k): return z**k*(1-z)**(3-k)
def D3(x,y):
    return sum(abs(B(x,sum(b))-B(y,sum(b))) for b in product((0,1),repeat=3))/2
MAP_RESIDUAL_00=[(B(P[0],k)-B(P[1],k))/32 for k in range(4)]
assert MAP_RESIDUAL_00==[F(13,1024),F(3,1024),-F(3,1024),-F(13,1024)]
assert [(-v) for v in MAP_RESIDUAL_00]==[-F(13,1024),-F(3,1024),F(3,1024),F(13,1024)]
assert B(F(37,100),1)>B(P[0],1)

# The COST barrier for ANY displacement of >= 3/25; the all-zero (or all-one)
# event is monotone and has the minimum inward boundary change 42957/250000.
barrier_event = F(3,4)**3 - (F(3,4)-R)**3
assert barrier_event == F(42957,250000)
barrier = barrier_event/F(128)
assert barrier == F(42957,32000000)
assert g(U) == F(166509,128000000)
assert barrier-g(U) == F(5319,128000000) > 0
assert q(U) == F(18117,4000000)
assert q(U) > F(726808599,10**12)

# On [p0-R,p0+R]=[13/100,37/100], exact D3(p0,t)
# is the all-zero-event difference. By bit reversal it is the all-one
# difference for p1. Check boundary and internal rational witnesses.
for xx in [F(13,100),F(1,5),F(1,4),F(3,10),F(1,3),F(37,100)]:
    assert D3(P[0],xx) == abs(B(P[0],0)-B(xx,0))
    assert D3(P[1],1-xx) == abs(B(P[1],3)-B(1-xx,3))

# Exact per-word sensitivity coefficients via |B'_k|/|B'_0| throughout
# [13/100,37/100]; the monotonic derivations are given in the proof.
coeffs = [F(1), F(61,261), F(3293,11907), F(1369,3969)]
assert coeffs[1] == (1-3*F(13,100))/(3*(1-F(13,100)))
assert coeffs[2] == (F(37,100)*(2-3*F(37,100)))/(3*(1-F(37,100))**2)
assert coeffs[3] == (F(37,63))**2
base = [F(13,1024),F(3,1024),F(3,1024),F(13,1024)]
margins = [base[k] - 8*coeffs[k]*g(U) for k in range(4)]
assert margins == [F(4577,2000000),F(115407,232000000),F(6499,126000000),F(191221,21000000)]
assert min(margins)>0

# q strictly increasing/convex, g strictly increasing/concave on [0,R].
# g' decreasing, g'' increasing, q'' decreasing; endpoint signs suffice.
def qp(u): return F(9,128)+F(3,16)*u-F(3,8)*u*u
def qpp(u): return F(3,16)-F(3,4)*u
def gp(u): return F(117,4096)-F(123,512)*u+F(69,256)*u*u
def gpp(u): return -F(123,512)+F(69,128)*u
assert qpp(R)>0 and qp(0)>0 and gp(R)>0 and gpp(R)<0
assert gp(0)/qp(0) == F(13,32)

# Heavy-fiber movement <1/100 by the tagged excess lower bound and
# D3>=|p-t|, since the heavy fibers have |a-b|=62.
assert F(62,256)*F(1,100) > g(U)
# H'-(4q)' is (3/4-u)[189(3/4-u)-390(1/4+u)]/256>0 on [0,1/100].
assert 189*(F(3,4)-F(1,100))-390*(F(1,4)+F(1,100)) > 0

BITS = list(product((0,1),repeat=3))
def tv(d,e):
    return sum(abs(d.get(x,F(0))-e.get(x,F(0))) for x in (d.keys() | e.keys()))/2

def risks(changed=None):
    target_public={}; cmp_public={}; target_tag={}; cmp_tag={}
    for h,(a,b) in M.items():
        j,w,y=h
        t=P[0] if a>b else P[1]
        if changed is not None:
            which,u=changed
            if which == h:
                t = P[0]+u if a>b else P[1]-u
        for s,n in enumerate((a,b)):
            weight=F(n,256)
            for bits in BITS:
                out=(w,y)+bits
                tagged=(s,j,w,y)+bits
                tar=weight*B(P[s],sum(bits))
                cmp=weight*B(t,sum(bits))
                target_public[out]=target_public.get(out,F(0))+tar
                cmp_public[out]=cmp_public.get(out,F(0))+cmp
                target_tag[tagged]=target_tag.get(tagged,F(0))+tar
                cmp_tag[tagged]=cmp_tag.get(tagged,F(0))+cmp
    assert sum(target_public.values())==sum(cmp_public.values())==1
    assert sum(target_tag.values())==sum(cmp_tag.values())==1
    assert len(target_tag)==128 and len(target_public)==32
    return tv(target_public,cmp_public),tv(target_tag,cmp_tag)

P0,T0=risks()
assert P0==F(11,256) and T0==F(77,1024)
for u in [F(0),F(1,100),F(1,40),U]:
    for h in [(1,0,0),(0,1,1)]:
        pub,tag=risks((h,u))
        assert pub==P0-q(u),(h,u,pub,P0-q(u))
        assert tag==T0+g(u),(h,u,tag,T0+g(u))

print('MODEL=8_POSITIVE_RATIONAL_SOURCE_FIBERS; TAGGED_ATOMS=128; PUBLIC_ATOMS=32')
print('P0=',P0,'T0=',T0)
print('radius=',R,'U=',U,'epsilon_new=',q(U),'epsilon_decimal=',float(q(U)))
print('epsilon_old=',F(726808599,10**12),'increase_ratio=',q(U)/F(726808599,10**12))
print('witness_tagged_excess=',g(U),'global_outside_radius_barrier=',barrier,'gap=',barrier-g(U))
print('per_word_coefficients=',','.join(str(c) for c in coeffs))
print('four_strict_sign_margins=',','.join(str(m) for m in margins))
print('heavy_radius_le_1_over_100=PASS; strict_concave_exchange=ENDPOINT_SIGNS_PASS')
print('MAP_AND_EIGHT_EXACT_SYMMETRIC_WITNESSES=PASS')
print('STAGE312B_COST_CONTROLLED_SIGN_PARETO_EXACT_PASS')
