#!/usr/bin/env python3
"""EC49FTX exact reverse-TP2 + full FOSD certificate.
External price-prior postprocessing; no native Bellman/heartbeat computation.
"""
from fractions import Fraction as F
from itertools import product
import json

EPS=F(1,1000)
T=F(27,64)
U=F(3,4)
C=F(16,945)

def peval(p,t):
    return sum((v*t**k for k,v in enumerate(p)),F(0))
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,v in enumerate(p):
        for j,w in enumerate(q):
            r[i+j]+=v*w
    return r
def diff(p):
    return [(i+1)*p[i+1] for i in range(len(p)-1)]
def minus(p,q):
    return [(p[i] if i<len(p) else F(0))-(q[i] if i<len(q) else F(0))
            for i in range(max(len(p),len(q)))]
def m_of_t(t): return F(187,8)-t
def L_of_t(t): return U-t/60
def b_of_t(t): return F(7,16)+t/54
def x_of_t(t): return (8*t+5733)/7560

def h_of_ab(a,b):
    m=F(525,8)*a-F(231,4)*b-F(9,8)
    z=F(35,32)*a-b/16-F(5,96)
    return 1-EPS*m*z

def A_integral(t):
    m=m_of_t(t); L=L_of_t(t)
    return C*((U-L)-EPS*m*(U*U-L*L)/2)

def B_integral(t):
    b=b_of_t(t); x=x_of_t(t); hi=F(49,64)
    p,q,r=F(525,8),-F(231,4)*b-F(9,8),F(35,32)
    v=-b/16-F(5,96)
    return ((hi-x)-EPS*(p*r*(hi**3-x**3)/3
       +(p*v+q*r)*(hi**2-x**2)/2+q*v*(hi-x)))/54

# Closed-form A and B, checked independently by elementary antiderivatives.
Ap=[F(0),F(943170,3402000000),F(907,3402000000),
    F(-8,3402000000)]
Bp=mul([F(441),F(-64)],
       [F(750801415275,2496508125511680000),
        F(606886272,2496508125511680000),
        F(-462848,2496508125511680000)])
for t in [F(0),F(1,16),F(1,8),F(1,4),F(3,8),T]:
    assert A_integral(t)==peval(Ap,t),('A',t)
    assert B_integral(t)==peval(Bp,t),('B',t)
    assert B_integral(t)>0
    if t>0: assert A_integral(t)>0

# Polynomial identity for (B/A)'_t: whole interval, not grid extrapolation.
N=minus(mul(diff(Bp),Ap),mul(Bp,diff(Ap)))
D=F(4246560321495367680000000000)
P=[F(156143408271305245875),F(300310805691601425),
   F(-7230168422976708),F(354330391570944),F(142745649152)]
assert N[:len(P)]==[-c/D for c in P] and all(v==0 for v in N[len(P):])
positive_bound=P[0]+P[2]*T*T
assert positive_bound==F(159889532371621484270967,1024)>0

# Box positivity from exact affine extrema.
a0,a1=F(3,4),F(49,64)
b0,b1=F(7,16),F(57,128)
Ms=[]; Zs=[]
for a,b in product([a0,a1],[b0,b1]):
    M=F(525,8)*a-F(231,4)*b-F(9,8)
    Z=F(35,32)*a-b/16-F(5,96)
    Ms.append(M); Zs.append(Z)
    assert h_of_ab(a,b)>0
assert max(Ms)==F(12213,512)<24 and min(Ms)>0
assert max(Zs)==F(4657,6144)<1 and min(Zs)>0

# Strict reverse TP2: d_m d_z log K = -eps/(1-eps*m*z)^2 < 0.
# Normalized continuous upper tail derivative:
# d_m log H=1/t-eps*(z+U)/(2*N)+eps*(L+U+m/60)/(2*D).
# N,D>976/1000, 1/t>64/27, hence uniform lower bound >0.
log_tail_derivative_lower=F(64,27)-F(1,976)
assert log_tail_derivative_lower>0

# Illustrative mixed-CDF exact regressions; proof is analytic.
def F_mixed(t,z):
    m=m_of_t(t); L=L_of_t(t)
    if z<=L: return F(0)
    if z>=U: return F(1)
    numerator=C*((z-L)-EPS*m*(z*z-L*L)/2)
    return numerator/(peval(Ap,t)+peval(Bp,t))
comparisons=0
for t1,t2 in [(F(3,8),F(1,4)),(F(1,4),F(1,8)),(F(3,8),F(1,16))]:
    assert m_of_t(t1)<m_of_t(t2)
    for z in [F(743,1000),F(747,1000),F(749,1000),F(3,4)]:
        assert F_mixed(t1,z)>=F_mixed(t2,z)
        comparisons+=1

print(json.dumps({
 "schema":"EC49FTX_REVERSE_TP2_MIXED_FOSD_V1",
 "scientific_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
 "parent":"EC49FTW PR2807@50b012f33f4e48f0f1357e6f0a164f10cd725414",
 "model":"external price-prior observer of inherited Bellman optimum only",
 "joint_density_unnormalized":"1 - (1/1000)*(525a/8-231b/4-9/8)*(35a/32-b/16-5/96)",
 "continuous_kernel":"(16/945)*(1-mz/1000)",
 "continuous_log_cross_derivative":"-(1/1000)/(1-mz/1000)^2 < 0",
 "FOSD":"proved on m in (1469/64,187/8)",
 "atom_ratio_derivative":"d(B/A)/dm>0 from exact quartic P(t)>0",
 "quartic_lower_bound":str(positive_bound),
 "continuous_upper_tail_log_m_derivative_lower":str(log_tail_derivative_lower),
 "global_density_lower":">976/1000",
 "clipped_and_continuous_integral_polynomial_check_nodes":6,
 "mixed_cdf_regression_pairs":comparisons,
 "native_bellman_rerun":False,
 "status":"AUTHOR_PROVED_EXACT_FRACTION_VERIFIED_PARENT_DEPENDENT_NOT_REVIEWED"
},indent=2,ensure_ascii=False))
