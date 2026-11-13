#!/usr/bin/env python3
"""Exact BRC-N4 BU adaptive-root dual certificate and 16-leaf P/Q witness.

External finite-model mathematics only. Universal event duals L0/L3 and
causal S2->S23 reduction are inherited AUTHOR-SIDE dependencies, not
re-certified by this script. All tested arithmetic is exact.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

a, b, u = S.symbols('a b u', real=True)
X = a+3*b
R = 7*(X-1)/(6*X)
C = (7-a-21*b)/(4*X+2)
delta = (1-a)/3
D = b-delta
E = S.factor(D*C/4)
H = b*(2*a-7*b)/(8*(a+2*b))
G = 5*a**2+8*a*b-21*b**2-2*b-5
T = a**2+38*a*b-7*a+105*b**2-14*b
L0 = (4*a-14*b-3*a*u-X*u**2)/(2*(23-2*u))
L3 = u*(a-X*u)/(2*(7-2*u))

identities = {
    'adaptive_L0_gap': L0.subs(u,R)-E + 3*T/((2*X+1)*(62*X+7)),
    'adaptive_L3_factor': L3-E - (6*X*u-7*X+7)*((4*X+2)*u+a+21*b-7)/(24*(2*u-7)*(2*X+1)),
    'adaptive_L3_root': L3.subs(u,R)-E,
    'capacity_L3_root': L3.subs(u,C)-E,
    'capacity_G_identity': E-delta-G/(8*(2*X+1)),
    'phase_T_identity': E-H-(1-a)*T/(24*(a+2*b)*(2*X+1)),
    'L0_derivative': S.diff(L0,u)-(a*(2*u**2-46*u-61)+b*(6*u**2-138*u-28))/(2*(2*u-23)**2),
    'L3_derivative': S.diff(L3,u)-(a*(2*u**2-14*u+7)+b*(6*u**2-42*u))/(2*(2*u-7)**2),
    'C_partial_a': S.diff(C,a)+(30-72*b)/(4*X+2)**2,
    'C_partial_b': S.diff(C,b)+(72*a+126)/(4*X+2)**2,
    'R_from_X': R-(S.Rational(7,6)-S.Rational(7,6)/X),
    'attainment_s': (1-a+D-b)/2-delta,
    'attainment_t': (1-a+3*(D-b))/4,
    'attainment_rQ': a/6-C/6-D*(1+C)/3-D/4,
    'attainment_rP': a/6-C/6-D*(1+C)/12-D/2-E,
}
assert all(S.cancel(v)==0 for v in identities.values()), {k:S.factor(v) for k,v in identities.items() if S.cancel(v)!=0}

# Entire positive-area closed rational rectangle, without sampling inference.
a0,a1 = F(481,500),F(241,250)
b0,b1 = F(151,1000),F(1511,10000)
def ev(expr, aa, bb):
    return S.cancel(expr.subs({a:S.Rational(aa),b:S.Rational(bb)}))

assert ev(S.diff(G,a),a0,b0) == S.Rational(2707,250) > 0
assert ev(S.diff(G,b),a1,b0) == -S.Rational(63,100) < 0
assert ev(G,a0,b1) == S.Rational(843019,100000000)>0
assert ev(S.diff(T,a),a0,b0) == S.Rational(331,500)>0
assert ev(S.diff(T,b),a0,b0) == S.Rational(27133,500)>0
assert ev(T,a1,b1) == -S.Rational(6927,4000000)<0
assert ev(R,a1,b1) == S.Rational(9737,28346)<S.Rational(3,7)
assert ev(C,a1,b1) == S.Rational(9543,25564)>ev(R,a1,b1)
assert ev(C,a0,b0) == S.Rational(2867,7660)<1
assert ev(D,a0,b0) == S.Rational(83,600)>0
assert 2*S.Rational(b1)<1
assert ev(S.diff(C,a),a1,b0)<0 and ev(S.diff(C,b),a0,b1)<0
assert ev(S.diff(R,a),a0,b0)>0 and ev(S.diff(R,b),a0,b0)>0
# Strict non-overlap with earlier closed parameter domains.
assert b0>F(3,20) and a1<F(193,200) and b0>F(15095,100000)

# Independent reconstruction from all 16 positive source leaves.
q_mass={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
likelihood={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
            'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(cat,j,l,q_mass[cat]/4,q_mass[cat]*likelihood[cat][j]/4)
        for cat in ('AU','AV','BU','BV') for j in range(2) for l in range(2)]
assert len(leaves)==16 and all(Q>0 and P>0 for _,_,_,Q,P in leaves)
assert sum(row[3] for row in leaves)==sum(row[4] for row in leaves)==1

def observed(law, first, second):
    out=defaultdict(F)
    for cat,j,l,Q,P in leaves:
        mass=Q if law=='Q' else P
        x=first[cat[0]]
        y=second[cat]
        z=int(cat=='BU')
        out[(1,'Q',0)]+=mass*(1-x)
        out[(2,'Q',0)]+=mass*x*(1-y)
        out[(3,'Q' if z else 'P',z)]+=mass*x*y
    assert sum(out.values())==1
    return out

def TV(v,w):return sum(abs(v.get(k,F())-w.get(k,F())) for k in set(v)|set(w))/2

test_cases=[(F(963,1000),b1),(a0,b0),(a0,b1),(a1,b0),(a1,b1)]
for aa,bb in test_cases:
    dd=(1-aa)/3
    BB=bb-dd
    cc=(7-aa-21*bb)/(4*(aa+3*bb)+2)
    EE=BB*cc/4
    UU=BB*(1+cc)
    assert F(0)<BB<=bb and 0<cc<1 and 0<UU<=1 and 0<BB<=1
    f1={'A':aa,'B':bb}; g1={'A':F(1),'B':BB}
    f2={'AU':F(1),'AV':F(0),'BU':F(0),'BV':F(0)}
    g2={'AU':cc,'AV':UU,'BU':cc,'BV':F(1)}
    assert g2['AU']==g2['BU']
    for law in ('Q','P'):
        v=observed(law,f1,f2); w=observed(law,g1,g2)
        assert TV(v,w)==EE,(law,aa,bb,TV(v,w),EE)
        keys=((1,'Q',0),(2,'Q',0),(3,'P',0),(3,'Q',1))
        signed=tuple(v.get(key,F())-w.get(key,F()) for key in keys)
        expected=(dd,EE-dd,F(),-EE) if law=='Q' else (F(),F(),EE,-EE)
        assert signed==expected,(law,aa,bb,signed,expected)
    print('FULL_16_LEAF_Q_AND_P_TV',aa,bb,EE)

wita,witb=F(963,1000),F(1511,10000)
assert ev(E,wita,witb)==S.Rational(119224157,9198240000)
assert ev(G,wita,witb)==S.Rational(1926399,100000000)
assert ev(T,wita,witb)==-S.Rational(48011,20000000)
assert ev(R,wita,witb)==S.Rational(29141,84978)
assert ev(C,wita,witb)==S.Rational(28639,76652)
assert ev(L0.subs(u,R)-E,wita,witb)==S.Rational(720165,36337110556)>0

# The requested outgoing (0.961,0.151) has G<0, while T<0: an exact
# obstruction to the E-attaining capacity *policy*, not a minmax falsifier.
aa,bb=F(961,1000),F(151,1000)
assert ev(G,aa,bb)==-S.Rational(291,125000)<0
assert ev(T,aa,bb)==-S.Rational(2289,250000)<0
assert ev(E,aa,bb)==S.Rational(16491,1276000)
assert ev(delta,aa,bb)==S.Rational(13,1000)>ev(E,aa,bb)
print('CONTINUUM_IDENTITIES',len(identities))
print('BOX_G_MIN',ev(G,a0,b1),'BOX_T_MAX',ev(T,a1,b1))
print('ANCHOR_E',ev(E,wita,witb),'ANCHOR_L0_MARGIN',ev(L0.subs(u,R)-E,wita,witb))
print('OUTGOING_G',ev(G,aa,bb),'OUTGOING_T',ev(T,aa,bb))
print('PASS_BRC_N4_BU_ADAPTIVE_ROOT_R_T_CERTIFICATE_20261030')
