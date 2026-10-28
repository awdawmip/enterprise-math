#!/usr/bin/env python3
"""Exact four-event dual certificate and algebraic upper witness (SymPy)."""
import sympy as s
x,y,u,v,a,b,z,c=s.symbols('A B U V a b z c')
q=(x-a+y-b)/2; p=(x-a+3*(y-b))/4; h=y*c/4
rq=a*z/6-x*c/6-u/3-v/4
rp=a*z/6-x*c/6-u/12-v/2
Q1=q;Q2=h-q-rq;Q3=h-rq;Q7=h
P4=rp;P5=p+rp;P6=h-p
al=(c+4)/(23-2*c);be=(3-7*c)/(23-2*c)
ga=2*(1+4*c-c*c)/(23-2*c);et=2*(c*c-2*c+7)/(23-2*c)
w1=7*(1-c)/20;w2=(7*c-3)/20;w3=(3*c+1)/10;w4=(7-3*c)/10
l1=c/(7-2*c);l2=7*(1-c)/(7-2*c)
l3=2*c*(2-c)/(7-2*c);l4=2*c*c/(7-2*c);mu=7*c/(4*(7-2*c))
g1=c/(4+c);g2=2*(2-c)/(4+c);g3=2*c/(4+c)
checks=[
 al+be+ga+et-1,w1+w2+w3+w4-1,l1+l2+l3+l4-1,g1+g2+g3-1,
 al*Q2+be*(h-q)+ga*P4+et*P5+7*al*(v-y)/4-
 (4*a*z-14*b+a*z*c-4*a*c-(a+3*b)*c*c)/(2*(23-2*c)),
 w1*Q2+w2*Q3+w3*P4+w4*P5+s.Rational(7,20)*(v-y)-
 (2*a*z-7*b-(2*a-b)*c)/20,
 l1*Q3+l2*Q7+l3*P4+l4*P5+mu*(v-y)-
 c*(a*(z-c)-3*b*c)/(2*(7-2*c)),
 g1*Q1+g2*Q7+g3*P6-b*c/(4+c)]
assert all(s.simplify(t)==0 for t in checks)
C=(s.sqrt(2674)-34)/23;E=(2*s.sqrt(2674)-101)/600
aa=s.Rational(1,2);bb=s.Rational(1,40)
X=aa+3*E;Y=bb-E;V=Y;U=Y*(1+C)
assert s.simplify(23*C*C+68*C-66)==0
assert s.simplify(E-bb*C/(4+C))==0
assert s.Rational(3,4)<C<s.Rational(4,5)
assert 0<Y<bb and aa<X<1 and 0<U<X and V==Y
ss=q.subs({x:X,y:Y,a:aa,b:bb})
tt=p.subs({x:X,y:Y,a:aa,b:bb})
hh=h.subs({y:Y,c:C})
rqq=rq.subs({a:aa,b:bb,z:1,x:X,y:Y,u:U,v:V,c:C})
rpp=rp.subs({a:aa,b:bb,z:1,x:X,y:Y,u:U,v:V,c:C})
assert all(s.simplify(k-j)==0 for k,j in zip((ss,tt,hh,rqq,rpp),(E,0,E,0,E)))
assert s.Rational(1767,90160)>s.Rational(3,640)>E
assert s.simplify(140-322*s.Rational(3,4)+46*s.Rational(3,4)**2)<0
assert s.simplify(s.diff(140-322*c+46*c*c,c).subs(c,1))<0
print('PASS_EXACT_N4_BU_ALGEBRAIC_MINIMAX_DUAL_CERTIFICATE')
print('exact_value=', E, 'approx=',s.N(E,18))
print('all_dual_residuals=',[str(s.simplify(v)) for v in checks])
