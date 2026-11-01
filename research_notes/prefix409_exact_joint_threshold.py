#!/usr/bin/env python3
"""PREFIX-409 author-side exact algebraic checker. No randomized/floating proof steps."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as S

R = S.Rational
I = S.I
A = S.Matrix([
    [4, 4, 0],
    [0, -4, 4],
    [-5+3*I, 0, -3+I],
    [-2-2*I, 4+4*I, 2+2*I],
    [-2, 0, 5+2*I],
])
M = S.simplify(A * A[:3, :].inv())
assert S.simplify(M[:3,:] - S.eye(3)) == S.zeros(3)
a,b,c = M[3,0], M[3,1], M[3,2]
d, f = M[4,0], M[4,1]
assert (S.simplify(a), S.simplify(b), S.simplify(c)) == (R(5,2)+R(9,2)*I, R(3,2)+R(7,2)*I, 4*I)
assert (S.simplify(d), S.simplify(f), S.simplify(M[4,2])) == (R(11,4)+R(15,8)*I, R(11,4)+R(15,8)*I, R(5,4)+R(9,4)*I)
e = M[4,2]
x,y = S.symbols('x y', real=True)
v = x + I*y
t = x*x+y*y
h = 2*x+t
for sig in [-1,1]:
    u = sig*I
    j4 = S.expand(S.expand_complex((a+b*u+c*v)*S.conjugate(a+b*u+c*v)))
    j5 = S.expand(S.expand_complex((d*(1+u)+e*v)*S.conjugate(d*(1+u)+e*v)))
    k = S.expand(j5-R(709,32))
    assert S.simplify(j5.subs({x:0,y:0})-R(709,32))==0
    if sig==-1:
        assert S.simplify(j4-(45+24*x-48*y+16*t))==0
        assert S.simplify(k-(R(61,8)*x-23*y+R(53,8)*t))==0
        assert S.simplify(j4-45-(93*h+48*k-43*t)/23)==0
    else:
        assert S.simplify(j4-(37+48*x+8*y+16*t))==0
        assert S.simplify(k-(23*x+R(61,8)*y+R(53,8)*t))==0
        assert S.simplify(j4-37-(728*h+64*k-176*t)/61)==0

# Exact-observation branch collision occurs only at large intensity.
t_minus = R(135424,35881)
t_plus = R(14884,9805)
assert 1<t_plus<t_minus
eta, beta = R(1,10000), R(1,1000000)
assert beta<t_plus

T = S.symbols('T', real=True)
Phi = ((eta-T)/2)**2 + ((39*T-84*eta)/61)**2
P = S.expand(Phi-T)
assert S.simplify(P-(196100000000*T**2-297747300000*T+6389)/R(297680000000))==0
lo, hi = R(2,100000000), R(3,100000000)
assert P.subs(T,lo)>0 and P.subs(T,hi)<0
assert S.diff(P,T).subs(T,0)<0 and S.diff(P,T).subs(T,beta)<0
Tstar = R(2977473,3922000)-R(61,9805000)*S.sqrt(14890729919)
assert S.simplify(P.subs(T,Tstar))==0
assert S.simplify(Tstar-lo)>0 and S.simplify(hi-Tstar)>0
kappa_star = S.simplify(4-(792*eta-176*Tstar)/61)

# Explicit attainment exactly at the two narrow observation upper endpoints.
xx=(eta-Tstar)/2
yy=(39*Tstar-84*eta)/61
assert S.simplify(xx**2+yy**2-Tstar)==0
vv=xx+I*yy
u=I
j4_exact = S.expand_complex((a+b*u+c*vv)*S.conjugate(a+b*u+c*vv))
j5_exact = S.expand_complex((d*(1+u)+e*vv)*S.conjugate(d*(1+u)+e*vv))
assert S.simplify(j4_exact-(41-kappa_star))==0
assert S.simplify(j5_exact-(R(709,32)+eta))==0
assert S.simplify(S.expand_complex((1+vv)*S.conjugate(1+vv))-(1+eta))==0

# Uniform rational enclosures certify contraction and coordinate monotonicity.
assert (eta+beta)/2 < R(1,10000)
assert (39*beta+100*eta)/61 < R(1,5000)
assert R(1,10000)**2+R(1,5000)**2 < beta
assert R(1,10000)+R(78,61)*R(1,5000) < R(1,1000)  # |Phi_T|
assert R(1,10000)+R(184,61)*R(1,5000) < R(1,1000) # |Phi_h|
assert R(16,61)*R(1,5000) < R(1,10000)             # |Phi_k|
assert 728-176*R(1,999)>0 and 64-176*R(1,9990)>0

# The entire minus-sign branch is separated farther from I4=41.
minus_gap = 4-(141*eta+43*beta)/23
plus_upper_gap = 4-(792*eta-176*beta)/61
assert plus_upper_gap<minus_gap
assert 37+792*eta/61<41
assert 45-(141*eta+43*beta)/23>41
assert kappa_star<minus_gap

# Rational enclosure for the algebraic noise threshold.
kap_lo = 4-(792*eta-176*lo)/61
kap_hi = 4-(792*eta-176*hi)/61
assert S.simplify(kappa_star-kap_lo)>0
assert S.simplify(kap_hi-kappa_star)>0

results = {
    'result':'PASS_PREFIX409_EXACT_NARROW_CV_I5_SHARP_ALGEBRAIC_THRESHOLD',
    'source':'exact original 5-port A times A_1:3 inverse',
    'model':'I1=I2=1, Cu=2 exact; I3 in [0,beta], Cv=1+/-eta, I5=709/32+/-eta; I4=41+/-kappa',
    'beta':str(beta),'eta':str(eta),
    'exact_coincidence_thresholds':{'sigma_plus_nonzero_t':str(t_plus),'sigma_minus_nonzero_t':str(t_minus)},
    'Tstar_minimal_polynomial_scaled':'196100000000*T**2-297747300000*T+6389',
    'Tstar_exact':str(Tstar),
    'Tstar_rational_bracket':[str(lo),str(hi)],
    'kappa_star_exact':str(kappa_star),
    'kappa_star_decimal_for_display':str(S.N(kappa_star,22)),
    'kappa_star_rational_bracket':[str(kap_lo),str(kap_hi)],
    'minus_branch_gap_lower':str(minus_gap),
    'source_witness':{'u':'I','v_re':str(xx),'v_im':str(yy),'I3':str(Tstar),'Cv':str(1+eta),'I5':str(R(709,32)+eta),'I4':str(S.simplify(41-kappa_star))},
    'proof_boundaries':'Author-side exact algebra check; analytic contraction/monotonicity proof in manuscript; no native BRC execution or independent review.'
}
Path(__file__).with_name('prefix409_exact_results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(results['result'])
print('Tstar exact:',Tstar)
print('Tstar interval:',lo,'< Tstar <',hi)
print('kappa* exact:',kappa_star)
print('kappa* decimal:',results['kappa_star_decimal_for_display'])
print('kappa* bracket:',kap_lo,'< kappa* <',kap_hi)
print('sigma minus branch gap bound:',minus_gap)
print('explicit witness: I3=',Tstar,'Cv=',1+eta,'I5=',R(709,32)+eta,'I4=',S.simplify(41-kappa_star))
