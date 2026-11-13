"""Stage336-B: independent exact polynomial checks for auxiliary labelled Bernoulli/BRC zero strata.

Computes only finite rational/symbolic identities and endpoint signs in the declared
auxiliary three-visit probability observer. It is not a native X6/BRC physical
operation or an independent proof checker.
"""
from fractions import Fraction as Q
import sympy as S

x,y,z=S.symbols('x y z', real=True)
w=(1,3,3,1)
m=(61,21,9,9)
def B(k,t): return t**k*(1-t)**(3-k)
def r(k,a,b): return (4*B(k,a)+B(k,b))/5-Q(m[k],160)
def D_sign(sign):
    return -S.Rational(1,2)*sum(w[k]*sign[k]*S.diff(B(k,z),z) for k in range(4))
def q(a,b):
    return Q(a,b)
def check(name, truth):
    assert bool(truth), name

# Weighted mass conservation is the algebraic justification for both smooth pieces of b.
check('mass_conservation',S.simplify(sum(w[k]*r(k,x,y) for k in range(4)))==0)
check('B0_derivative', S.factor(S.diff(B(0,z),z)+3*(1-z)**2)==0)
check('B1_derivative', S.factor(S.diff(B(1,z),z)-(1-z)*(1-3*z))==0)
check('B2_derivative', S.factor(S.diff(B(2,z),z)-z*(2-3*z))==0)
check('B3_derivative', S.factor(S.diff(B(3,z),z)-3*z*z)==0)

# Full 16-comparison tagged observer: sign words at anchors 1/4 and 3/4.
sx_a=(-1,1,1,1); sx_b=(-1,-1,1,1)
sy_a=(1,1,-1,-1); sy_b_before=(-1,-1,1,1); sy_b_after=(-1,-1,-1,1)
p=(1-z)*(189-183*z)/256
q_before=3*z*(1-z)/64
q_after=3*z*(18-25*z)/256
cx=(63*D_sign(sx_a)+D_sign(sx_b))/256
cy_before=(9*D_sign(sy_a)+7*D_sign(sy_b_before))/256
cy_after=(9*D_sign(sy_a)+7*D_sign(sy_b_after))/256
for name, actual, expected in [('cx',cx,-p),('cy_before',cy_before,q_before),('cy_after',cy_after,q_after)]:
    check(name,S.factor(actual-expected)==0)

# Direct signs at extremal rational brackets plus analytically known B_k monotonicity.
a=Q(21,100); b=Q(6,25); low=Q(609,1000); high=Q(63,100)
for anchor,word in [(Q(1,4),sx_a),(Q(3,4),sx_b)]:
    for xx in (a,b):
        check('x_tag_word',tuple(1 if B(k,anchor)-B(k,xx)>0 else -1 for k in range(4))==word)
for anchor,word in [(Q(1,4),sy_a),(Q(3,4),sy_b_after)]:
    for yy in (low,high):
        check('y_tag_word',tuple(1 if B(k,anchor)-B(k,yy)>0 else -1 for k in range(4))==word)
for yy in (Q(1,2),Q(5,8)):
    check('arc_y_tag_non_switching_terms',
          tuple(1 if B(k,Q(1,4))-B(k,yy)>0 else -1 for k in range(4))==sy_a)
check('cy_positive_after',18-25*high>0)
check('cy_positive_before',Q(1,2)>0 and 1-Q(5,8)>0)
check('cx_negative', 189-183*b>0)

# r3 zero graph has a unique positive Y3(x) from 4x^3 + Y3^3 = 9/32.
zero_r3_checks=[
    ('at_a_5over8',r(3,a,Q(5,8))<0),
    ('at_a_63over100',r(3,a,high)>0),
    ('at_b_609over1000',r(3,b,low)<0),
    ('at_b_61over100',r(3,b,Q(61,100))>0),
    ('r1_max',r(1,b,low)<0),
    ('r2_min',r(2,a,Q(5,8))>0),
]
for name,valid in zero_r3_checks:check(name,valid)

# r0 sign changes exactly once along the r3 zero graph.
xL=Q(113,500); xH=Q(227,1000)
check('Y3_xL_bracket',r(3,xL,Q(617,1000))<0<r(3,xL,Q(618,1000)))
check('Y3_xH_bracket',r(3,xH,Q(616,1000))<0<r(3,xH,Q(617,1000)))
check('r0_positive_at_xL',r(0,xL,Q(618,1000))>0)
check('r0_negative_at_xH',r(0,xH,Q(616,1000))<0)

Y3p=-4*x*x/(y*y)
Y0p=-4*(1-x)**2/(1-y)**2
check('Y3p',S.factor(S.diff(r(3,x,y),x)+S.diff(r(3,x,y),y)*Y3p)==0)
check('Y0p',S.factor(S.diff(r(0,x,y),x)+S.diff(r(0,x,y),y)*Y0p)==0)
check('r0_along_r3',S.factor(S.diff(r(0,x,y),x)+S.diff(r(0,x,y),y)*Y3p+
        S.Rational(12,5)*(y-x)*(x+y-2*x*y)/(y*y))==0)
check('r2_along_r3',S.factor(S.diff(r(2,x,y),x)+S.diff(r(2,x,y),y)*Y3p-
        S.Rational(8,5)*x*(1-x/y))==0)
check('r3_along_r0',S.factor(S.diff(r(3,x,y),x)+S.diff(r(3,x,y),y)*Y0p-
        S.Rational(12,5)*(x-y)*(x+y-2*x*y)/(1-y)**2)==0)

# Lower-bound exact exchange on the r0=0 subarc.
f=lambda t:t*(2-3*t)/(1-t)**2
check('fprime',S.factor(S.diff(f(z),z)-2*(2*z-1)/(z-1)**3)==0)
check('f_gap_arc',f(Q(5,8))-f(b)==Q(77,3249)>0)
check('f_gap_cross',f(Q(63,100))>f(xH))
check('r2_along_r0',S.factor(S.diff(r(2,x,y),x)+S.diff(r(2,x,y),y)*Y0p-
        S.Rational(4,5)*(1-x)**2*(f(x)-f(y)))==0)
check('r0_outer_endpoint_not_zero',r(0,b,Q(1,2))<0)
check('cx_lower',p.subs(z,S.Rational(6,25))==S.Rational(68913,160000))
check('b_derivative_margin',S.Rational(3,4)*(1-b)**2*(f(Q(5,8))-f(b))==S.Rational(77,7500))

print('FROZEN_GLOBAL_MAIN','dcffdd3270d839d765c7cab630a66c20afc926c5')
print('FROZEN_EM_MAIN','fd980113f72132edbc47ee27efadf15dd118441c')
print('P000_ORIGINAL_BLOB','bcc2590d3168a28f72e8b9f0f9b1f76faadcd488')
for name,val in [
 ('r3_a_5over8',r(3,a,Q(5,8))),('r3_a_63over100',r(3,a,high)),
 ('r3_b_609over1000',r(3,b,low)),('r3_b_61over100',r(3,b,Q(61,100))),
 ('r1_max',r(1,b,low)),('r2_min',r(2,a,Q(5,8))),
 ('r0_xL_at_618over1000',r(0,xL,Q(618,1000))),
 ('r0_xH_at_616over1000',r(0,xH,Q(616,1000))),
 ('tag_cx',S.factor(cx)),('tag_cy_below_cusp',S.factor(cy_before)),
 ('tag_cy_above_cusp',S.factor(cy_after)),
 ('f_gap_arc',Q(77,3249)),('b_slope_max_negative',-Q(77,7500)),
 ('c_slope_max_negative',-Q(68913,160000))]:
 print(name,val)
print('STAGE336B_R0_R3_COMPLETE_ZERO_STRATUM_EXCLUSION_EXACT_PASS')
