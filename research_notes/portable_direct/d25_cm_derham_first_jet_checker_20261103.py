#!/usr/bin/env python3
"""D25 external E3/E4 de Rham first-jet transport certificate.
Exact symbolic coefficient identities: SymPy 1.14.0.
Finite checks use named Fp2 coordinates; NOT native H0/B0.
"""
import json
import sympy as sp
x,t=sp.symbols('x t')
s=sp.sqrt(2)
t3=(2-s)/4
t4=(3-2*s)/6
d=3*s
alpha=sp.simplify(d/sp.Integer(12)-sp.Rational(1,3))
f3=x**3+(x+t/sp.Integer(27))**2/4
f4=x**3+x**2+t*x/4
def certificate(f,a,b,P):
    residue=-sp.diff(f,t)-(2*(a+b*x)*f+4*sp.diff(P,x)*f-2*P*sp.diff(f,x))
    assert sp.simplify(sp.together(sp.expand(residue)))==0
certificate(f3,-1/(3*(t-1)),-3/(t*(t-1)),
            1/(108*(t-1))+((9-4*t)/(12*t*(t-1)))*x+3*x*x/(t*(t-1)))
certificate(f4,-1/(4*(t-1)),-1/(2*t*(t-1)),
            ((2-t)/(4*t*(t-1)))*x+x*x/(2*t*(t-1)))
def theta_coeff(t0,a,b):
    factor=t*(t-1)/(2*t-1)
    return tuple(sp.simplify((factor*v).subs(t,t0)) for v in (a,b))
c3,q3=theta_coeff(t3,-1/(3*(t-1)),-3/(t*(t-1)))
c4,q4=theta_coeff(t4,-1/(4*(t-1)),-1/(2*t*(t-1)))
assert sp.simplify(c3-(s-1)/6)==0
assert sp.simplify(q3-3*s)==0
assert sp.simplify(c4-(3*s-4)/32)==0
assert sp.simplify(q4-3*s/8)==0
A=sp.simplify(c4+q4*alpha-(d*q4/q3)*c3)
B=sp.simplify(d*q4/q3)
assert sp.simplify(A-(s-2)/32)==0
assert sp.simplify(B-d/8)==0
assert sp.simplify((1+16*A)/d-sp.Rational(1,6))==0
assert sp.simplify(16*B/d-2)==0
def mul(a,b,p):
    return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def power(a,n,p):
    y=(1,0)
    while n:
        if n&1:y=mul(y,a,p)
        a=mul(a,a,p);n//=2
    return y
def prime_check(p):
    dd=(0,3);q=p*p;sgn=-1 if p%24==13 else 1
    assert power(dd,(q-1)//2,p)==(sgn%p,0)
    Afield=((-2*pow(32,-1,p))%p,pow(32,-1,p))
    Bfield=(0,3*pow(8,-1,p)%p)
    assert Afield!=(0,0) and Bfield!=(0,0)
    assert mul(Bfield,(8,0),p)==dd
    return dict(p=p,p_mod24=p%24,quadratic_twist_sign=sgn,
                first_jet_mixing_A=list(Afield),first_jet_derivative_B=list(Bfield),
                all_checked=True)
rows=[prime_check(p) for p in (13,19,37,43,109,373)]
print(json.dumps(dict(schema="D25_EXTERNAL_CM_FIRST_JET_CERTIFICATE_V1",
    symbolic_GM_identities=True,first_jet_transport=True,
    symmetric_square_weighted_observer_factor="1/6",
    actual_source="external_elliptic_dR_not_native_H0_B0",cases=rows),indent=2))
