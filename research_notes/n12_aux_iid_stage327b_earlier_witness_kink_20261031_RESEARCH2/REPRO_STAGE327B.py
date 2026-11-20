#!/usr/bin/env python3
"""Stage327-B exact-rational witness check; finite positive Bernoulli BRC only."""
from fractions import Fraction as Q
from math import comb

P = tuple(Q(k,160) for k in (61,21,9,9))
XS = (Q(231083940855521,10**15), Q(231083940855522,10**15))
YS = (Q(555508857277,10**12), Q(555508857278,10**12))
X = Q(24001,100000)
q = (Q(2354398,10**7), Q(5688542,10**7))

def B(k,z): return z**k*(1-z)**(3-k)
def r(k,x,y): return Q(4,5)*B(k,x)+Q(1,5)*B(k,y)-P[k]
def bisect_decreasing(f,lo,hi,steps=96):
    assert f(lo)>0 and f(hi)<0
    for _ in range(steps):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    assert f(lo)>0>f(hi)
    return lo,hi

def poly_range(k,zrange):
    lo,hi=zrange
    values=[B(k,lo),B(k,hi)]
    if k in (1,2) and lo <= Q(k,3) <= hi:
        values.append(B(k,Q(k,3)))
    return min(values),max(values)

def abs_range(iv):
    lo,hi=iv
    return max(Q(0),lo,-hi),max(abs(lo),abs(hi))

def r_range(k,xi,yi):
    a,b=poly_range(k,xi); c,d=poly_range(k,yi)
    return Q(4,5)*a+Q(1,5)*c-P[k],Q(4,5)*b+Q(1,5)*d-P[k]

def b_range(xi,yi):
    return tuple(sum(Q(5*comb(3,k),32)*abs_range(r_range(k,xi,yi))[i] for k in range(4)) for i in (0,1))

def D_range(a,zi):
    return tuple(sum(Q(comb(3,k),2)*abs_range((B(k,a)-poly_range(k,zi)[1],B(k,a)-poly_range(k,zi)[0]))[i] for k in range(4)) for i in (0,1))

def c_range(xi,yi):
    factors=[(Q(63,256),D_range(Q(1,4),xi)),(Q(1,256),D_range(Q(3,4),xi)),
             (Q(9,256),D_range(Q(1,4),yi)),(Q(7,256),D_range(Q(3,4),yi))]
    return tuple(sum(weight * iv[i] for weight,iv in factors) for i in (0,1))

def exact(z):return (z,z)
def floor12(z):return z.numerator*10**12 // z.denominator

y = bisect_decreasing(lambda z:r(1,X,z),Q(58,100),Q(59,100))
bs,bx,bq=b_range(XS,YS),b_range(exact(X),y),b_range(exact(q[0]),exact(q[1]))
cs,cx,cq=c_range(XS,YS),c_range(exact(X),y),c_range(exact(q[0]),exact(q[1]))
eps=(bx[0]-bs[1],bx[1]-bs[0])
slack=(bs[0]+bx[0]-2*bq[1],bs[1]+bx[1]-2*bq[0])
gain=(cs[0]+cx[0]-2*cq[1],cs[1]+cx[1]-2*cq[0])
assert Q(2863,10**6)<eps[0] and eps[1]<Q(2864,10**6)
assert slack[0]>Q(2,10**8) and gain[0]>Q(5,10**8)
assert r_range(3,exact(X),y)[1]<0
assert X>XS[1] and y[0]>YS[1]
print('MODEL auxiliary three future Bernoulli observations, two labeled source blocks')
print('INHERITED_MINIMIZER_BRACKETS', XS, YS)
print('RIGHT_BRANCH_R1_EQ_ZERO', 'X',X, 'Y_BRACKET',y)
print('RATIONAL_SYMMETRIC_COMPETITOR',q)
print('EPSILON_INTERVAL_TRILLIONTH',floor12(eps[0]),floor12(eps[1])+1)
print('PUBLIC_BUDGET_SLACK_INTERVAL_TRILLIONTH',floor12(slack[0]),floor12(slack[1])+1)
print('TAGGED_COST_GAIN_INTERVAL_TRILLIONTH',floor12(gain[0]),floor12(gain[1])+1)
print('R3_RIGHT_BRANCH_NEGATIVE', True)

# Exact interior tagged-observer kink: at y_dagger=(1+sqrt(13))/8.
YD = (Q(575693909432998,10**15), Q(575693909432999,10**15))
XD = (Q(237806902,10**9), Q(237806904,10**9))
F=lambda z: 16*z*z-4*z-3
assert F(YD[0])<0<F(YD[1])
assert r(1,XD[0],YD[0])<0<r(1,XD[1],YD[1])
# r1_x>0 and r1_y<0 throughout these narrow boxes.
assert XD[0]<Q(1,3)<YD[0] and YD[1]<Q(2,3)
assert r_range(0,XD,YD)[1]<0
assert r_range(2,XD,YD)[0]>0
assert r_range(3,XD,YD)[1]<0
# All tagged-word gaps besides (a=3/4, z=Y_dagger, k=2) stay nonzero.
for a,zi,label in [(Q(1,4),XD,'x low'),(Q(3,4),XD,'x high'),(Q(1,4),YD,'y low'),(Q(3,4),YD,'y high')]:
    for k in range(4):
        if a==Q(3,4) and label=='y high' and k==2:
            continue
        lo,hi=poly_range(k,zi)
        gap_lo,gap_hi=B(k,a)-hi,B(k,a)-lo
        assert gap_hi<0 or gap_lo>0,(label,k)
# B2(3/4)-B2(y)=(4y-3)(16y^2-4y-3)/64; single transverse zero.
assert B(2,Q(3,4))==Q(9,64)
assert all((Q(4)*z-3)*F(z)/64==B(2,Q(3,4))-B(2,z) for z in YD)
# All interval expressions below are positive, using rational monotonicity.
def a1(z):return (1-z)*(1-3*z)
def denom(z):return (1-z)*(3*z-1)
def g2(z):return z*(2-3*z)
yprime=(4*a1(XD[1])/denom(YD[1]),4*a1(XD[0])/denom(YD[0]))
gx=(g2(XD[0]),g2(XD[1]))  # increasing on (0,1/3)
gy=(g2(YD[1]),g2(YD[0]))  # decreasing on (1/3,2/3)
bprime=(Q(15,16)*(Q(4,5)*gx[0]+Q(1,5)*gy[0]*yprime[0]),
        Q(15,16)*(Q(4,5)*gx[1]+Q(1,5)*gy[1]*yprime[1]))
cjump=(Q(21,256)*gy[0]*yprime[0],Q(21,256)*gy[1]*yprime[1])
slope_jump=(cjump[0]/bprime[1],cjump[1]/bprime[0])
assert bprime[0]>0 and cjump[0]>0
assert Q(11665,100000)<slope_jump[0] and slope_jump[1]<Q(11666,100000)
print('TAGGED_K2_KINK_Y_INTERVAL',YD)
print('TAGGED_K2_KINK_X_INTERVAL',XD)
print('TAGGED_K2_CANDIDATE_COST_SLOPE_UPWARD_JUMP',floor12(slope_jump[0]), floor12(slope_jump[1])+1, 'units 1e-12')
print('KINK_SCOPE','candidate C(b) on r1=0 only, not globally optimal Pareto frontier')

print('STAGE327B_EARLIER_WITNESS_AND_TAGGED_CUSP_EXACT_PASS')
