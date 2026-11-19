#!/usr/bin/env python3
"""EC49FTY exact rational certificate; external price-prior observer, NOT native BRC."""
from fractions import Fraction as F
import json
T=F(27,64)
U=F(3,4)
UMAX=F(1048576000,18958647)
EMAX=UMAX/1000
DEN=F(4246560321495367680000000000)
M2,M3=F(1469,64),F(187,8)
A0,A1=F(3,4),F(49,64)
B0,B1=F(7,16),F(57,128)

def mm(a,b): return F(525,8)*a-F(231,4)*b-F(9,8)
def zz(a,b): return F(35,32)*a-b/16-F(5,96)
def add(*polys):
    o={}
    for p in polys:
        for ij,c in p.items(): o[ij]=o.get(ij,F(0))+c
    return {ij:c for ij,c in o.items() if c}
def mul(p,q):
    o={}
    for (i,j),v in p.items():
        for (k,l),w in q.items(): o[i+k,j+l]=o.get((i+k,j+l),F(0))+v*w
    return {ij:c for ij,c in o.items() if c}
def dt(p): return {(i-1,j):i*v for (i,j),v in p.items() if i}
def scale(p,k): return {ij:k*c for ij,c in p.items()}
def ev(p,t,u): return sum((v*t**i*u**j for (i,j),v in p.items()),F(0))

corners=[(a,b) for a in (A0,A1) for b in (B0,B1)]
assert all(mm(a,b)>0 and zz(a,b)>0 for a,b in corners)
assert max(mm(a,b)*zz(a,b) for a,b in corners)==F(18958647,1048576)
assert mm(A1,B0)==F(12213,512) and zz(A1,B0)==F(4657,6144)
assert EMAX==F(1048576,18958647)

A=mul({(1,0):F(1,3402000000)},
      {(0,0):F(960000),(0,1):-F(16830),(1,1):F(907),(2,1):-F(8)})
B=mul({(0,0):F(441,2496508125511680000),
       (1,0):-F(64,2496508125511680000)},
      {(0,0):F(764411904000),(0,1):-F(13610488725),
       (1,1):F(606886272),(2,1):-F(462848)})
P={
(0,0):F(161810711838720000000),
(0,1):-F(5717812295230560000),
(0,2):F(50508727815805875),
(1,1):F(305754824245248000),
(1,2):-F(5444018553646575),
(2,1):-F(7490036957184000),
(2,2):F(259868534207292),
(3,1):F(362941513728000),
(3,2):-F(8611122157056),
(4,2):F(142745649152)}
assert add(mul(dt(B),A),scale(mul(B,dt(A)),-1))==scale(P,-1/DEN)

def original_cont_mass(t,u):
    m=M3-t; lower=U-t/60; eps=u/1000
    return F(16,945)*((U-lower)-eps*m*(U*U-lower*lower)/2)
def original_clipped_mass(t,u):
    b=F(7,16)+t/54; x=(8*t+5733)/7560; hi=A1; eps=u/1000
    p,q=F(525,8),-F(231,4)*b-F(9,8)
    r,v=F(35,32),-b/16-F(5,96)
    return ((hi-x)-eps*(p*r*(hi**3-x**3)/3+
            (p*v+q*r)*(hi**2-x**2)/2+q*v*(hi-x)))/54
for tt in (F(1,64),F(1,8),T/2,T):
    for uu in (F(0),F(1),F(3),UMAX):
        assert ev(A,tt,uu)==original_cont_mass(tt,uu)
        assert ev(B,tt,uu)==original_clipped_mass(tt,uu)

b_upper=-F(5444018553646575)+F(519737068414584)*T+F(570982596608)*T**3
bp_lower=F(519737068414584)-F(51666732942336)*T
ab_slope_lower=-F(14980073914368000)+UMAX*bp_lower
ab_zero=F(305754824245248000)-UMAX*F(5444018553646575)
p0prime_upper=P[(0,1)]+2*P[(0,2)]*UMAX
p_lower=ev(P,F(0),UMAX)
assert b_upper==-F(41797692846880281,8)<0
assert bp_lower==F(497940165454536)>0
assert ab_slope_lower==F(79375391185081466880000,6319549)>0
assert ab_zero==F(29410194168062410752000,6319549)>0
assert p0prime_upper==-F(825835120387682761440000,6319549)<0
assert p_lower==F(2987318260952797009674240000000,39936699563401)>0
n_lower=1-EMAX*M3*U
mn_minus_t_lower=M2*n_lower-T
assert n_lower==F(191933,6319549)>0
assert mn_minus_t_lower==F(55660877,202225568)>0

for tt in (F(1,128),F(1,8),T):
    for uu in (F(0),F(1),F(10),F(50),UMAX):
        assert ev(A,tt,uu)>0 and ev(B,tt,uu)>0
        assert ev(P,tt,uu)>=p_lower>0

print(json.dumps({
 "schema":"EC49FTY_SHARP_EPSILON_NONNEGATIVE_PRIOR_V1",
 "scientific_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
 "external_prior":"1-epsilon*M_*(a,b)*Z_*(a,b)",
 "parent":"EC49FTX PR2809@da282b9f72ee11a8cd05fb6a98d2c8917d736975",
 "epsilon_max":str(EMAX),
 "strictly_positive_epsilon":"[0,epsilon_max)",
 "nonnegative_epsilon":"[0,epsilon_max]",
 "FOSD":"all 0<=epsilon<=epsilon_max and all 1469/64<m<m'<187/8",
 "limiting_mechanism":"GLOBAL_PRIOR_DENSITY_NONNEGATIVITY",
 "max_chart_product":str(mm(A1,B0)*zz(A1,B0)),
 "continuous_N_lower":str(n_lower),
 "continuous_mN_minus_t_lower":str(mn_minus_t_lower),
 "atom_ratio_P_uniform_strict_lower":str(p_lower),
 "b_upper":str(b_upper),
 "bp_lower":str(bp_lower),
 "ab_slope_lower":str(ab_slope_lower),
 "ab_zero":str(ab_zero),
 "p0prime_upper":str(p0prime_upper),
 "mass_integral_checks":16,
 "polynomial_identity":"EXACT_BIVARIATE_COEFFICIENT_EQUALITY",
 "native_bellman_rerun":False,
 "independent_review":False,
 "status":"AUTHOR_PROVED_EXACT_RATIONAL_VERIFIED_PARENT_DEPENDENT_NOT_REVIEWED"
},indent=2))
