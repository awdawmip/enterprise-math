#!/usr/bin/env python3
"""Stage362-B exact algebra/checker for central r1=0 Pareto geometry.

All checked numerical constants are rational. Universal continuum statements
use the analytic sign and local-direction proof in PROOF_STAGE362B.md.
"""
from fractions import Fraction as F
import sympy as S
x, y, s, t = S.symbols('x y s t', real=True)
w=(1,3,3,1); m=(61,21,9,9)
B=lambda k,z:z**k*(1-z)**(3-k)
r=[(4*B(k,x)+B(k,y))/5-S.Rational(m[k],160) for k in range(4)]
assert S.expand(sum(w[k]*r[k] for k in range(4)))==0
xx=(F(229,1000),F(233,1000))
yy=(F(27,50),F(14,25))
anchors=(F(1,4),F(3,4))
sgns={('x',0):(-1,1,1,1),('x',1):(-1,-1,1,1),
      ('y',0):(1,1,-1,-1),('y',1):(-1,-1,1,1)}
def br(k,z):return z**k*(1-z)**(3-k)
def rr(k,a,b):return (4*br(k,a)+br(k,b))/5-F(m[k],160)
for var,ends in [('x',xx),('y',yy)]:
    for ai,a in enumerate(anchors):
        for k in range(4):
            want=sgns[(var,ai)][k]
            for z in ends:
                assert want*(br(k,a)-br(k,z))>0
for var,ends in [('x',xx),('y',yy)]:
    for k in range(4):
        der=S.diff(B(k,x),x)
        for z in ends:
            expected=(-1,1,1,1)[k] if var=='x' else (-1,-1,1,1)[k]
            assert S.sign(der.subs(x,S.Rational(z.numerator,z.denominator)))==expected
r2min=rr(2,xx[0],yy[0])
r3max=rr(3,xx[1],yy[1])
assert r2min>0 and r3max<0
def D_der(z,signs):
    return -S.Rational(1,2)*sum(w[k]*signs[k]*S.diff(B(k,z),z) for k in range(4))
cx=S.factor((63*D_der(x,sgns[('x',0)])+D_der(x,sgns[('x',1)]))/256)
cy=S.factor((9*D_der(y,sgns[('y',0)])+7*D_der(y,sgns[('y',1)]))/256)
assert S.simplify(cx+3*(1-x)*(63-61*x)/256)==0
assert S.simplify(cy-3*y*(1-y)/64)==0
Gm=S.Matrix([S.diff(r[2],z)*S.Rational(15,16) for z in (x,y)])
Gp=S.Matrix([S.diff(r[1]+r[2],z)*S.Rational(15,16) for z in (x,y)])
H=S.Matrix([-cx,-cy])
assert Gm.applyfunc(S.expand)==S.Matrix([3*x*(2-3*x)/4,3*y*(2-3*y)/16]).applyfunc(S.expand)
assert Gp.applyfunc(S.expand)==S.Matrix([3*(1-2*x)/4,3*(1-2*y)/16]).applyfunc(S.expand)
D1=S.factor(S.det(S.Matrix.hstack(Gm,H)))
D2=S.factor(S.det(S.Matrix.hstack(H,Gp)))
D3=S.factor(S.det(S.Matrix.hstack(Gm,Gp)))
assert -F(2,5)*F(3,200)+F(3,256)*F(813,2000)==-F(633,512000)<0
assert F(3,16)*(2*yy[0]-1)==F(3,200)
assert F(3,4)*(1-2*xx[0])==F(813,2000)
bright=S.simplify(-S.Rational(5,16)*r[3])
assert S.simplify(S.diff(bright,x)+3*x**2/4)==0
assert F(3,4)*xx[0]**2>F(39,1000)
assert F(39,1000)-F(3,800)>F(7,200)
assert F(2,5)-F(3,800)>F(39,100)
def bracket_r1(x0):
    lo,hi=F(27,50),F(14,25)
    assert rr(1,x0,lo)>0 and rr(1,x0,hi)<0
    for _ in range(36):
        mid=(lo+hi)/2
        if rr(1,x0,mid)>0:lo=mid
        else:hi=mid
    assert rr(1,x0,lo)>0 and rr(1,x0,hi)<0
    return lo,hi
for x0,sgn in [(F(230,1000),1),(F(232,1000),-1)]:
    a,b=bracket_r1(x0)
    assert rr(0,x0,a)*sgn>0 and rr(0,x0,b)*sgn>0
    print('r1_arc_slice',str(x0),'y_bracket',str(a),str(b),'r0_sign',sgn)
ss=1-x;tt=1-y;A=4*ss**2+tt**2;L=4*ss+tt
assert S.simplify(r[1]-(A-S.Rational(41,16))/5+r[0])==0
assert S.simplify(r[2]-(L-2*A+S.Rational(13,8))/5-r[0])==0
sp,tp=S.symbols('sp tp',positive=True)
z1=(4*sp**2+tp**2-S.Rational(41,16))/5
z2=(4*sp+tp-8*sp**2-2*tp**2+S.Rational(13,8))/5
D=lambda expr:-S.diff(expr,sp)+S.diff(expr,tp)*(4*sp**2/tp**2)
assert S.simplify(D(z1)-8*sp*(sp-tp)/(5*tp))==0
assert S.simplify(D(z2)-4*(sp-tp)*(sp+tp-4*sp*tp)/(5*tp**2))==0
assert 4*F(767,1000)*F(410,1000)-(F(771,1000)+F(467,1000))>0
P=lambda z:(F(41,16)-4*z*z)**3-(F(61,32)-4*z*z*z)**2
slo,shi=F(768916059144,10**12),F(768916059145,10**12)
assert P(slo)<0<P(shi)
assert F(3,16)*(4*(1-2*F(229,1000))+37*(1-2*F(533,1000)))<=-F(411,8000)
assert (F(111)-189*F(767,1000)**2)/256==-F(186621,256000000)<0
print('r2_positive_lower',r2min,'r3_negative_upper',r3max)
print('r1_cusp_cone_det',D1,D2,D3)
print('strict_D2_global_upper',-F(633,512000))
print('right_arc_rational_gain_lower',F(7,200),F(39,100))
print('stage356_root_isolator_s',slo,shi)
print('STAGE362B_R1_KINK_PARETO_STRICT_LOCAL_AND_RATIONAL_DOMINATION_EXACT_PASS')
