#!/usr/bin/env python3
"""Exact algebraic and complete 16-leaf source checks for enlarged BU N=4 minimax rectangle.
This release is a source-backed independent executable; the exhaustive real-variable
minimax statement follows from the analytic dual and matching strategy proof.
"""
from fractions import Fraction
import sympy as S

a,b,c,A,B,U,V=S.symbols('a b c A B U V', real=True)
H=B*c/4
s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
rQ=a/6-A*c/6-U/3-V/4
rP=a/6-A*c/6-U/12-V/2
DQ=S.Matrix((s,H-s-rQ,rQ,-H))
DP=S.Matrix((t,H-t-rP,rP,-H))
f=(a+3*b)*c*c+(3*a+8*b)*c+14*b-4*a
G=5*a*a+8*a*b-21*b*b-2*b-5
L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
K=b*c/(4+c)
R=c*(a+3*b-1)/12
cp=(7-a-21*b)/(4*a+12*b+2)
ecap=S.factor(cp*(a+3*b-1)/12)
c0=S.Rational(3,7)
w0=(c+4,3-7*c,2*(1+4*c-c*c),2*(c*c-2*c+7))
w3=(c,7*(1-c),2*c*(2-c),2*c*c)
q2=H-s-rQ
p4=rP
p5=t+rP
assertions={
  'dual_K':(c*s+(4-2*c)*H+2*c*(H-t))/(4+c)-K,
  'dual_L0':(w0[0]*q2+w0[1]*(H-s)+w0[2]*p4+w0[3]*p5)/(23-2*c)+7*(c+4)*(V-B)/(4*(23-2*c))-L0,
  'dual_L3':(w3[0]*(H-rQ)+w3[1]*H+w3[2]*p4+w3[3]*p5)/(7-2*c)+7*c*(V-B)/(4*(7-2*c))-L3,
  'dual_R':(1-c/3)*H+(c/3)*(H-t)-c*(a+3*b-A)/12,
  'dual0_weights':sum(w0)/(23-2*c)-1,
  'dual3_weights':sum(w3)/(7-2*c)-1,
  'L3_minus_K':L3-K+c*f/(2*(7-2*c)*(4+c)),
  'f_endpoint_3_7':f.subs(c,c0)-(-124*a+881*b)/49,
  'f_endpoint_half':f.subs(c,S.Rational(1,2))-(-9*a+75*b)/4,
  'f_endpoint_one':f.subs(c,1)-25*b,
  'L0_end':L0.subs(c,c0)-(4*a-23*b)/70,
  'L3_end':L3.subs(c,c0)-3*(4*a-9*b)/602,
  'L3_cap':L3.subs(c,cp)-ecap,
  'R_cap':R.subs(c,cp)-ecap,
  'G_cap_TV':ecap-(1-a)/3-G/(8*(2*a+6*b+1)),
  'f_cap_G':f.subs(c,cp)+3*(5*a+21*b)*G/(4*(2*a+6*b+1)**2),
  'G_beta':G.subs(b,(4*a-1-S.sqrt(121*a*a-8*a-104))/21),
}
for name,expr in assertions.items():
    assert S.simplify(S.cancel(expr))==0,(name,S.factor(expr))
X=b*c/(4+c)
W=4*b/(4+c)
root_sub={A:a+3*X,B:W,U:W*(1+c),V:W}
for vec,target in [(DQ,S.Matrix((X,0,0,-X))),(DP,S.Matrix((0,0,X,-X)))]:
    for expr in vec.subs(root_sub,simultaneous=True)-target:
        num=S.cancel(expr).as_numer_denom()[0]
        poly=S.Poly(num,c,domain=S.QQ.frac_field(a,b))
        assert S.rem(poly,S.Poly(f,c,domain=S.QQ.frac_field(a,b))).is_zero
Bcap=(a+3*b-1)/3
cap_sub={A:S.Integer(1),B:Bcap,c:cp,U:Bcap*(1+cp),V:Bcap}
assert list(S.simplify(z) for z in (DQ-S.Matrix(((1-a)/3,ecap-(1-a)/3,0,-ecap))).subs(cap_sub,simultaneous=True))==[0]*4
assert list(S.simplify(z) for z in (DP-S.Matrix((0,0,ecap,-ecap))).subs(cap_sub,simultaneous=True))==[0]*4
al=S.Rational(39,40);ah=S.Rational(99,100)
bl=S.Rational(1,50);bh=S.Rational(2,25)
assert f.subs({a:al,b:bh,c:c0})==-S.Rational(2521,2450)
assert G.subs({a:al,b:bh})==S.Rational(3309,40000)
assert G.subs({a:al,b:S.Rational(1,16)})==S.Rational(43,1280)
assert L0.subs({a:al,b:bh,c:c0})==S.Rational(103,3500)
assert L3.subs({a:al,b:bh,c:c0})==S.Rational(477,30100)
assert ecap.subs({a:ah,b:bh})==S.Rational(9959,830400)
assert S.Rational(9959,830400)<S.Rational(1,80)<S.Rational(477,30100)
assert 43-19*ah-183*bh==S.Rational(191,20)
assert 5*al+33*bl-5==S.Rational(107,200)
da_num=a*a+6*a*b+a+9*b*b+30*b-11
db_num=7*a*a+42*a*b-2*a+63*b*b+21*b-14
assert da_num.subs({a:ah,b:bh})==-S.Rational(60971,10000)
assert db_num.subs({a:ah,b:bh})==-S.Rational(37097,10000)
source={
 'AU':(Fraction(1,6),Fraction(1,1),(Fraction(9,10),Fraction(11,10))),
 'AV':(Fraction(1,3),Fraction(1,4),(Fraction(1),Fraction(1))),
 'BU':(Fraction(1,4),Fraction(1,1),(Fraction(1,5),Fraction(9,5))),
 'BV':(Fraction(1,4),Fraction(2,1),(Fraction(1),Fraction(1))),
}
leaves=[]
for branch,(qm,ratio,r3) in source.items():
  for j in (0,1):
    for k in (0,1):
      q=qm/4;p=q*ratio*r3[j]
      assert p>0 and q>0
      leaves.append((branch,j,k,q,p))
assert len(leaves)==16
assert sum((row[3] for row in leaves),Fraction())==1
assert sum((row[4] for row in leaves),Fraction())==1
def TV(vals):
  return S.simplify(sum(abs(S.factor(x)) for x in vals)/2)
def check_witness(a0,b0,cval,which):
  vals={a:a0,b:b0,c:cval}
  if which=='root':
    x=b0*cval/(4+cval);w=4*b0/(4+cval)
    vals.update({A:a0+3*x,B:w,U:w*(1+cval),V:w})
    assert 0<=vals[A]<=1 and 0<=vals[B]<=1 and vals[U]<=vals[A] and vals[V]<=vals[B]
    assert f.subs({a:a0,b:b0,c:cval})==0
    e=x
  else:
    w=(a0+3*b0-1)/3
    vals.update({A:S.Integer(1),B:w,U:w*(1+cval),V:w})
    assert 0<=w<=1 and 0<=vals[U]<=1 and vals[V]<=w
    assert cval==cp.subs({a:a0,b:b0})
    e=ecap.subs({a:a0,b:b0})
  qs=[S.factor(v.subs(vals)) for v in DQ]
  ps=[S.factor(v.subs(vals)) for v in DP]
  assert TV(qs)==e and TV(ps)==e,(a0,b0,which,qs,ps,e)
  assert sum(qs)==0 and sum(ps)==0
  print('WITNESS',which,'a=',a0,'b=',b0,'c=',cval,'exact_tv=',e)
rb=S.Rational(1911,94520)
check_witness(al,rb,S.Rational(9,10),'root')
check_witness(S.Rational(93,95),S.Rational(4,95),S.Rational(4,5),'root')
check_witness(S.Rational(93,95),S.Rational(4,95),S.Rational(4,5),'cap')
check_witness(al,S.Rational(3,40),S.Rational(89,136),'cap')
print('PASS_EXACT_BRC_N4_BU_EXPANDED_2D_RELEASE',len(assertions),'symbolic identities',len(leaves),'positive leaves')