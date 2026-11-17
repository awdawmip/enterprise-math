#!/usr/bin/env python3
"""R749STR: exact collision witnesses and uniform six-phase Bernstein separator."""
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

W=(1,1,2,3,6)
N=100
part=[0]*(N+1)
part[0]=1
for weight in W:
    for i in range(weight,N+1):
        part[i]+=part[i-weight]
C=[0]*(N+1)
T=[0]*(N+1)
for n in range(1,N+1):
    C[n]=C[n-1]+part[n-1]
    T[n]=T[n-1]+C[n-1]

def S(n):
    return 18*n**4+54*n**3-345*n**2+2070*n-16315

def Y(n,e,d):
    return F(n**3*(T[n]+e),C[n]+d)-F(S(n),108)

def inverse_two(n,y0,y1):
    x0=(y0+F(S(n),108))/n**3
    x1=(y1+F(S(n+6),108))/(n+6)**3
    v0=C[n]*x0-T[n]
    v1=C[n+6]*x1-T[n+6]
    assert x0!=x1
    d=(v0-v1)/(x1-x0)
    e=v0+x0*d
    return e,d

witnesses=[]
for h,E,D in ((1,F(-2,5),F(19,10)),(2,F(7,5),F(2))):
    n=73+6*h
    e,d=inverse_two(73,Y(n,E,D),Y(n+6,E,D))
    assert all(-2<=z<=2 for z in (e,d,E,D))
    assert Y(73,e,d)==Y(n,E,D)
    assert Y(79,e,d)==Y(n+6,E,D)
    witnesses.append({'gap_h':h,'p':n,'e':str(e),'d':str(d),'E':str(E),'D':str(D)})

lam=F(21,20)
a=F(73**3,C[73]+2)-lam*F(79**3,C[79]-2)
b=F(73**3*(T[73]-2),(C[73]+2)**2)-lam*F(79**3*(T[79]+2),(C[79]-2)**2)
assert a>0 and b>0
qmin=Y(73,-2,2)-lam*Y(79,-2,2)
p91max=Y(91,2,2)-lam*Y(97,2,2)
gap=qmin-p91max
assert qmin==F(33210791290663,51995544553800)
assert p91max==F(1740831760941127,2855570604280200)
assert gap==F(148157200542443986379,5091802077550505078161)>0

t,u,v=sp.symbols('t u v',nonnegative=True)
k=t+3
n=73+6*k
nn=n+6
Pc=lambda z:(z+13)*(z+14)*(54*z**3+2097*z**2+27103*z+116595)/sp.Integer(30)
Pt=lambda z:(z+12)*(z+13)*(z+14)*(216*z**3+8532*z**2+112161*z+490715)/sp.Integer(120)
c=Pc(k);cc=Pc(k+1)
tn=Pt(k);tnn=Pt(k+1)
e=2-4*u;d=-2+4*v
P=sp.expand((sp.Rational(p91max.numerator,p91max.denominator)
           +sp.Rational(1,108)*S(n)-sp.Rational(21,20)*sp.Rational(1,108)*S(nn))
            *(c+d)*(cc+d)-n**3*(tn+e)*(cc+d)
            +sp.Rational(21,20)*nn**3*(tnn+e)*(c+d))
assert sp.Poly(P,t,u,v).degree(t)==10
assert sp.Poly(P,t,u,v).degree(u)<=1
assert sp.Poly(P,t,u,v).degree(v)<=2
bernstein={}
zero_count=0
for ui in (0,1):
    poly_v=sp.Poly(P.subs(u,ui),v)
    a0,a1,a2=(poly_v.nth(i) for i in range(3))
    for vi,B in ((0,a0),(1,a0+a1/2),(2,a0+a1+a2)):
        cfs=[sp.Rational(z) for z in sp.Poly(sp.expand(B),t).all_coeffs()]
        assert len(cfs)==11
        assert all(z>=0 for z in cfs),(ui,vi)
        zero_count+=sum(int(z==0) for z in cfs)
        bernstein[f'u{ui}_v{vi}']=[str(z) for z in cfs]
assert zero_count==1
assert bernstein['u0_v2'][-1]=='0'
assert P.subs({t:0,u:0,v:1})==0

out={
 'unit':'R749STR','evidence':'AUTHOR_EXACT_NOT_REVIEWED',
 'frozen_science_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'weights':list(W),'q':73,'p':'73+6h (h>=1)',
 'two_read_collision_witnesses_h_1_2':witnesses,
 'separator_lambda':str(lam),'q_exact_minimum':str(qmin),
 'p_global_maximum_h_ge_3':str(p91max),
 'sharp_uniform_gap':str(gap),'gap_equality':'h=3, (e,d,E,D)=(-2,2,2,2)',
 'noise_threshold_per_raw_read_strict':'eta < '+str(gap/F(41,10)),
 'q_partial_e_lower_bound':str(a),'q_negative_partial_d_lower_bound':str(b),
 'Bernstein_degree_u_v':[1,2],'Bernstein_t_degree':10,
 'Bernstein_coefficient_polynomials_high_to_low':bernstein,
 'Bernstein_zero_coefficients':zero_count,
 'scope':'all positive integer h; all real nuisance quadruples in [-2,2]^4, fixed per candidate; auxiliary scalar observer only',
 'next':'classify single-read overlap for h>=3 and construct native BRC Port/Cell observer correspondence'
}
path=Path(__file__).with_name('R749STR_FULL_TWO_READ_GAP_CLASSIFICATION_RESULTS.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS: h1/h2 exact two-read collisions, h>=3 sharp uniform separator, 65 positive +1 zero Bernstein coefficients')
print('uniform gap',gap,'eta <',gap/F(41,10))
