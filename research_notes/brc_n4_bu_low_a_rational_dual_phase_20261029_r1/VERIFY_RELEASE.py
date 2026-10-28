#!/usr/bin/env python3
"""Exact symbolic BRC N4 BU low-a dual identity certificate, author-side."""
import sympy as s
A,B,U,V,a,b,c=s.symbols('A B U V a b c')
sg=(A-a+B-b)/2;t=(A-a+3*(B-b))/4;H=B*c/4
rq=(a-A*c)/6-U/3-V/4;rp=(a-A*c)/6-U/12-V/2
q1=sg;q2=H-sg-rq;q3=H-rq;q7=H;p4=rp;p5=t+rp;p6=H-t
al=(c+4)/(23-2*c);be=(3-7*c)/(23-2*c)
ga=2*(1+4*c-c*c)/(23-2*c);eta=2*(c*c-2*c+7)/(23-2*c)
l=[c/(7-2*c),7*(1-c)/(7-2*c),2*c*(2-c)/(7-2*c),2*c*c/(7-2*c)]
mu=7*c/(4*(7-2*c))
g=[c/(4+c),2*(2-c)/(4+c),2*c/(4+c)]
L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
expr=[al+be+ga+eta-1,sum(l)-1,sum(g)-1,
al*q2+be*(H-sg)+ga*p4+eta*p5+7*al*(V-B)/4-L0,
l[0]*q3+l[1]*q7+l[2]*p4+l[3]*p5+mu*(V-B)-L3,
g[0]*q1+g[1]*q7+g[2]*p6-b*c/(4+c)]
assert all(s.cancel(e)==0 for e in expr)
bb=s.Rational(1,40);c0=(2*a-7*bb)/(2*a+4*bb);c1=4*c0/(4-c0);eps=bb*c0/4
assert all(s.factor(e)==0 for e in
 [L0.subs(b,bb).subs(c,c0)-eps,L3.subs(b,bb).subs(c,c0)-eps,
  (b*c/(4+c)).subs({b:bb,c:c1})-eps])
p=2336000*a**3+164000*a*a-54635*a-3969
D=7*a-14*(a+3*bb)*c+2*(a+3*bb)*c*c
assert s.factor(D.subs(c,c1)+p/(5*(240*a+23)**2))==0
assert s.diff(p,a).subs(a,s.Rational(7,80))==27720
assert p.subs(a,s.Rational(3,20))<0<p.subs(a,s.Rational(1,6))
assert c1.subs(a,s.Rational(1,6))<s.Rational(3,7)
print("PASS_SYMBOLIC_BU_N4_LOW_A_DUAL_PHASE_RELEASE")
