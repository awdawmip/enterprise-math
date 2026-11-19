#!/usr/bin/env python3
"""EC49FTU exact-rational checker. No external libraries, network or native BRC rerun."""
from fractions import Fraction as F
import json

T=F(27,64)
M2,M3=F(1469,64),F(187,8)
U=F(3,4)
A_MAX=F(49,64)

def L(m): return (8*m+173)/480
def ac(b): return (77+6*b)/105
def bb(m): return (47-m)/54
def Qpoly(t): return 3296*t*t-1733760*t+261457875
def A(t): return t*Qpoly(t)/F(421954312500)
def B(t):
    return (64*t-441)*(109568*t*t-196996464*t-24224009607)/F(35838544379904000)
def r(t): return B(t)/A(t)
def w(z): return F(11,35)+F(32,35)*z
def a(m,z): return (47-m)/945+F(44,45)*z
def b(m,z): return F(1,27)-m/54+F(10,9)*z
def K(m,z): return F(16,945)*(1+a(m,z)+b(m,z))*w(z)
def integral_A(t):
    m=M3-t
    lo=L(m)
    c0=1+(47-m)/945+F(1,27)-m/54
    c1=F(44,45)+F(10,9)
    d0,d1=F(11,35),F(32,35)
    coeffs=[c0*d0,c0*d1+c1*d0,c1*d1]
    return F(16,945)*sum(coeffs[k]*(U**(k+1)-lo**(k+1))/(k+1) for k in range(3))
def integral_B(t):
    m=M3-t
    bm=bb(m)
    x=ac(bm)
    d=A_MAX-x
    c0=1+x+bm
    return (c0*d+(c0+1)*d*d/2+d*d*d/3)/54

# Polynomial operations: ascending-coefficient, all exact rational
def trim(a):
    x=list(a)
    while len(x)>1 and x[-1]==0: x.pop()
    return x
def add(a,b):
    z=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): z[i]+=v
    for i,v in enumerate(b): z[i]+=v
    return trim(z)
def neg(a): return [-v for v in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): z[i+j]+=v*w
    return trim(z)
def scale(a,s): return trim([v*s for v in a])
def deriv(a): return [F(i)*a[i] for i in range(1,len(a))] or [F(0)]
def evalp(a,t): return sum(c*t**i for i,c in enumerate(a))

Ap=scale([0,261457875,-1733760,3296],F(1,421954312500))
Bp=scale(mul([-441,64],[-24224009607,-196996464,109568]),F(1,35838544379904000))
Qp=[F(261457875),F(-1733760),F(3296)]
assert all(A(v)==evalp(Ap,v) and B(v)==evalp(Bp,v) for v in [F(i,256) for i in range(1,108)])
# Verify full polynomial identity r''(t) with no symbolic CAS.
N=sub(mul(deriv(Bp),Ap),mul(Bp,deriv(Ap)))
Nprime=deriv(N)
r2num=sub(mul(Nprime,Ap),scale(mul(N,deriv(Ap)),2))
# r''(t) = r2num / A(t)^3
P=[F(-11591710449861527147026265625),
 F(230598262640418705763920000),
 F(-1967509591224525617119200),
 F(141015426401077236933120),
 F(-928647468742788716544),
 F(1044832421089787904),
 F(1546333976526848)]
# Cross multiply: r'' * 589824*t^3*Q^3 = -875 P
left=scale(mul(r2num,mul([0,0,0,1],mul(mul(Qp,Qp),Qp))),F(589824))
right=scale(mul(P,mul(mul(Ap,Ap),Ap)),F(-875))
assert trim(left)==trim(right)
assert sum(v for v in P if v>0)<-P[0]  # P(t)<0 for 0<t<1
assert F(1733760)**2-4*3296*261457875 < 0 # Q(t)>0 for all real t
# Therefore r''(m)=r''(t)>0 on 0<t<T. Consequently r'_m increasing.
def derivative_m(t):
    return -evalp(N,t)/A(t)**2
threshold=F(3011497578173713436500,1113761136900667642209)
assert derivative_m(T)==threshold
assert 0<threshold<3
checks=0
for i in range(1,108):
    t=T*F(i,108)
    assert A(t)==integral_A(t)
    assert B(t)==integral_B(t)
    assert A(t)>0 and B(t)>0
    assert derivative_m(t)>threshold
    checks+=1

# Continuous K1 / K0 varies strictly with discount z, independent of m,
# and is positive over the box: min(1+a-ac(b))=6661/6720.
assert 1+F(3,4)-ac(F(57,128))==F(6661,6720)
minors=[]
for mlo,mhi in [
    (M2+F(1,256),M2+F(1,128)),
    (M2+F(1,128),M2+F(1,64)),
    (M2+F(1,64),M2+F(1,32)),
    (M2+F(1,128),M2+F(1,32))
]:
    zlo,zhi=F(749,1000),F(1499,2000)
    assert L(mhi)<zlo<zhi<U
    minor=K(mlo,zlo)*K(mhi,zhi)-K(mlo,zhi)*K(mhi,zlo)
    assert minor>0
    minors.append(str(minor))

# Smooth bump: psi=exp(-1/s²)/J on s>0, identically 0 on s<=0.
# At fixed b its integral over a in [ac(b),49/64] is delta(b).
# Added amplitude 54*A(t)*lambda*t/delta makes clipped atom = B(t)+lambda*t*A(t).
p,q=M2+F(1,128),M2+F(1,64)
def full_ratio_at_m(m,lam):
    t=M3-m
    return r(t)+lam*t
def atomprob(m,lam):
    R=full_ratio_at_m(m,lam)
    return R/(1+R)
lam=F(3)
ratio_gap=full_ratio_at_m(p,lam)-full_ratio_at_m(q,lam)
atom_gap=atomprob(p,lam)-atomprob(q,lam)
assert ratio_gap==F(1922825655930000265002959,1768321928463564335718115584)>0
assert atom_gap==F(179422707606140184727956110208,1841092654109728505799184921900171)>0

out={
 "schema":"EC49FTU_JOINT_CONTINUOUS_ATOM_SHARP_THRESHOLD_V1",
 "source_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
 "parent":"EC49FTT PR2799@d3cdbff82125e422b7de00eb26ad89689fe1a4b7",
 "scope":"external conditional price prior under inherited author Bellman optimum",
 "price_prior":"h_{1,lambda}=(1+a+b)(1+a-a_c(b)) + lambda*[54*A1(m(b))*t(b)/delta(b)]*psi((a-a_c(b))/delta(b))",
 "smooth_bump":"psi is standard normalized positive C-infinity flat bump with integral 1",
 "continuous_kernel":"K1=16/945*(1+a(m,z)+b(m,z))*(11+32*z)/35",
 "conditional_continuous_law_changed":True,
 "continuous_kernel_TP2":"strict",
 "range_m":["1469/64","187/8"],
 "A1_t":"t*(3296*t^2-1733760*t+261457875)/421954312500",
 "B1_t":"(64*t-441)*(109568*t^2-196996464*t-24224009607)/35838544379904000",
 "sharp_lambda_1":str(threshold),
 "sharp_lambda_1_decimal":format(float(threshold),".15f"),
 "valid_exact_parameter_interval":f"0 <= lambda <= {threshold}",
 "failing_lambda":str(lam),
 "witness_m_early":str(p),"witness_m_late":str(q),
 "atom_ratio_early_minus_late":str(ratio_gap),
 "top_atom_probability_early_minus_late":str(atom_gap),
 "r_second_derivative_numerator_positive_certificate":"P(t)<0 since sum(positive polynomial coefficients)<abs(constant), and 0<t<27/64<1",
 "polynomial_identities_checked":True,
 "fraction_integral_regression_cases":checks,
 "strict_TP2_minor_cases":len(minors),
 "native_BRC_rerun":False,
 "formal_independent_review":False,
 "status":"AUTHOR_PROVED_EXACT_RATIONAL_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED"
}
print(json.dumps(out,ensure_ascii=False,indent=2))
