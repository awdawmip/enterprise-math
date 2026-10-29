#!/usr/bin/env python3
"""Exact symbolic identities and finite 16-leaf checks for the a=49/50 high-b phase.
The interval-wide inequality is in PROOF.md; this is not a formal proof checker.
External finite BRC probability model only; no native heartbeat/phase computation.
"""
from fractions import Fraction as F
import sympy as S

a,b,c,A,B,U,V=S.symbols('a b c A B U V',real=True)
a0=S.Rational(49,50)
s=(A-a+B-b)/2; t=(A-a+3*(B-b))/4; H=B*c/4
rQ=a/6-A*c/6-U/3-V/4
rP=a/6-A*c/6-U/12-V/2
DQ=S.Matrix([s,H-s-rQ,rQ,-H]);DP=S.Matrix([t,H-t-rP,rP,-H])
L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
R=c*(a+3*b-1)/12
c0=(2*a-7*b)/(2*a+4*b)
cp=(7-a-21*b)/(4*a+12*b+2)
e0=b*c0/4; ep=cp*(a+3*b-1)/12
c1=3*b*c0/(a+3*b-1)
poly=37500*b*b+8300*b-2107
gamma=(S.sqrt(38494)-83)/750
beta=S.Rational(1641,1525)-S.sqrt(3002689)/1830

p=(c+4)/(23-2*c);w=(3-7*c)/(23-2*c)
r=2*(1+4*c-c*c)/(23-2*c);v=2*(c*c-2*c+7)/(23-2*c)
l1=c/(7-2*c);l2=7*(1-c)/(7-2*c)
l3=2*c*(2-c)/(7-2*c);l4=2*c*c/(7-2*c)
Q2=H-s-rQ;Q3=H-rQ;Q7=H;P4=rP;P5=t+rP;P6=H-t
checks={
  'L0_event_dual':p*Q2+w*(H-s)+r*P4+v*P5+7*p*(V-B)/4-L0,
  'L3_event_dual':l1*Q3+l2*Q7+l3*P4+l4*P5+7*c*(V-B)/(4*(7-2*c))-L3,
  'R_event_dual':(1-c/3)*Q7+c*P6/3-R-c*(1-A)/12,
  'L0_weight_sum':p+w+r+v-1,
  'L3_weight_sum':l1+l2+l3+l4-1,
  'L0_at_c0':L0.subs(c,c0)-e0,
  'L3_at_c0':L3.subs(c,c0)-e0,
  'L3_at_cp':L3.subs(c,cp)-ep,
  'R_at_cp':R.subs(c,cp)-ep,
  'R_at_c1':R.subs(c,c1)-e0,
  'cp_minus_c0':cp-c0-(1-a)*(5*a+21*b)/(2*(a+2*b)*(2*a+6*b+1)),
  'e_p_minus_e_0_at_a49':(ep-e0).subs(a,a0)-7*poly/(4800*(75*b+37)*(100*b+49)),
  'L3_c1_gap_at_a49':(L3.subs(c,c1)-e0).subs(a,a0)+7*b*(25*b-7)*poly/(4*(100*b+49)*(150*b-1)*(22500*b*b+5150*b-49)),
  'gamma_root':poly.subs(b,gamma),
  'gamma_quadratic':(750*gamma+83)**2-38494,
  'capacity_Q':DQ.subs({A:1,B:(a+3*b-1)/3,c:cp,U:((a+3*b-1)/3)*(1+cp),V:(a+3*b-1)/3})-S.Matrix([(1-a)/3,ep-(1-a)/3,0,-ep]),
  'capacity_P':DP.subs({A:1,B:(a+3*b-1)/3,c:cp,U:((a+3*b-1)/3)*(1+cp),V:(a+3*b-1)/3})-S.Matrix([0,0,ep,-ep]),
  'alternate_Q':DQ.subs({A:a,B:b,c:c0,U:b*(1+c0),V:b})-S.Matrix([0,e0,0,-e0]),
  'alternate_P':DP.subs({A:a,B:b,c:c0,U:b*(1+c0),V:b})-S.Matrix([0,0,e0,-e0]),
}
for label,expr in checks.items():
    for z in (list(expr) if isinstance(expr,S.MatrixBase) else [expr]):
        remainder=S.factor(S.cancel(S.together(z)))
        assert remainder==0,(label,remainder)
assert S.simplify(beta>S.Rational(9,70)) is S.true
assert S.simplify(beta<S.Rational(13,100)) is S.true
assert S.simplify(gamma>S.Rational(3,20)) is S.true
assert S.simplify(gamma<S.Rational(4,25)) is S.true
assert S.simplify(beta<gamma) is S.true
assert S.simplify(S.Rational(9,70)>S.Rational(196,1525)) is S.true
print('PASS_SYMBOLIC_IDENTITIES',len(checks),'gamma=',S.N(gamma,20),'beta=',S.N(beta,20))

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
ratios={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
        'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(path,q/4,q*ratios[path][i]/4) for path,q in q2.items() for i in range(2) for j in range(2)]
assert len(leaves)==16 and all(x>0 and y>0 for _,x,y in leaves)
assert sum(x for _,x,y in leaves)==sum(y for _,x,y in leaves)==1

def observed(A1,B1,c1,U1,V1,target=False):
    A1,B1,c1,U1,V1=map(F,(A1,B1,c1,U1,V1))
    assert 0<=A1<=1 and 0<=B1<=1 and 0<=c1<=1 and 0<=U1<=A1 and 0<=V1<=B1
    rates={'AU':F(1),'BU':F(0),'AV':F(0),'BV':F(0)} if target else {
        'AU':c1,'BU':c1,'AV':U1/A1 if A1 else F(0),'BV':V1/B1 if B1 else F(0)}
    out=[]
    for law in ('Q','P'):
        z=[F(0)]*4
        for path,q,p in leaves:
            mass=q if law=='Q' else p
            initial=A1 if path[0]=='A' else B1
            step=rates[path]
            z[0]+=mass*(1-initial)
            z[1]+=mass*initial*(1-step)
            z[3 if path=='BU' else 2]+=mass*initial*step
        assert sum(z)==1
        out.append(z)
    return out

def errors(aa,bb,AA,BB,cc,UU,VV):
    target=observed(aa,bb,0,0,0,target=True)
    candidate=observed(AA,BB,cc,UU,VV)
    return [sum(abs(z-w) for z,w in zip(p,q))/2 for p,q in zip(target,candidate)]

a0F=F(49,50)
capacity_tests=(F(3,50),F(9,70),F(129,1000),F(13,100),F(3,20))
for bb in capacity_tests:
    cpF=(7-a0F-21*bb)/(4*a0F+12*bb+2)
    BF=(a0F+3*bb-1)/3
    epF=BF*cpF/4
    assert errors(a0F,bb,1,BF,cpF,BF*(1+cpF),BF)==[epF,epF]
    print('PASS_CAPACITY_16LEAF',str(bb),str(epF))
alt_tests=(F(151,1000),F(4,25),F(1,5),F(1,4),F(7,25))
for bb in alt_tests:
    ca=(2*a0F-7*bb)/(2*a0F+4*bb)
    eps=bb*ca/4
    assert errors(a0F,bb,a0F,bb,ca,bb*(1+ca),bb)==[eps,eps]
    print('PASS_ALTERNATE_16LEAF',str(bb),str(eps))
for bb in (F(7,25),F(3,10),F(1,2),F(1)):
    assert errors(a0F,bb,a0F,bb,0,2*a0F/7,2*a0F/7)==[0,0]
print('PASS_ZERO_16LEAF',4)

bb=F(4,25)
ca=(2*a0F-7*bb)/(2*a0F+4*bb)
cc=(7-a0F-21*bb)/(4*a0F+12*bb+2)
e_alt=bb*ca/4;e_cap=cc*(a0F+3*bb-1)/12
assert (ca,e_alt,e_cap,e_cap-e_alt)==(F(21,65),F(21,1625),F(437,33600),F(181,2184000))
assert e_cap>e_alt
print('PASS_STRICT_RATIONAL_SWITCH_WITNESS',str(e_alt),'old_capacity=',str(e_cap),'gain=',str(e_cap-e_alt))
print('PASS_EXACT_GAMMA_SWITCH_HIGH_B_RELEASE')
