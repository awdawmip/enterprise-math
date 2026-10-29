#!/usr/bin/env python3
"""BRC N=4 BU: exact zero-loss iff, quantitative bound, improved capacity interval.
Only verifies symbolic identities/finite examples; analytic inequalities are in PROOF.md.
"""
from fractions import Fraction as F
from random import Random
import sympy as S

a,b,c,A,B,U,V=S.symbols('a b c A B U V', real=True)
s=(A-a+B-b)/2; t=(A-a+3*(B-b))/4; H=B*c/4
rQ=a/6-A*c/6-U/3-V/4
rP=a/6-A*c/6-U/12-V/2
DQ=S.Matrix([s,H-s-rQ,rQ,-H]); DP=S.Matrix([t,H-t-rP,rP,-H])
q=S.expand(1372500*b*b-2953800*b+358631)
beta=S.Rational(1641,1525)-S.sqrt(3002689)/1830
cp=(7-a-21*b)/(4*a+12*b+2)
ep=cp*(a+3*b-1)/12
Bp=(a+3*b-1)/3; Up=Bp*(1+cp)
L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
R=c*(a+3*b-1)/12
p=(c+4)/(23-2*c); w=(3-7*c)/(23-2*c)
r=2*(1+4*c-c*c)/(23-2*c); v=2*(c*c-2*c+7)/(23-2*c)
l1=c/(7-2*c); l2=7*(1-c)/(7-2*c)
l3=2*c*(2-c)/(7-2*c); l4=2*c*c/(7-2*c)
Q2=H-s-rQ; Q3=H-rQ; Q7=H; P4=rP; P5=t+rP; P6=H-t
N0=131*a*a+576*a*b-232*a+549*b*b-1746*b+245
G=5*a*a+8*a*b-21*b*b-2*b-5
checks={
 'zero_relation_1':S.expand(s.subs({A:a,B:b})),
 'zero_relation_2':S.expand(t.subs({A:a,B:b})),
 'zero_rQ':rQ.subs({A:a,B:b,c:0,U:2*a/7,V:2*a/7}),
 'zero_rP':rP.subs({A:a,B:b,c:0,U:2*a/7,V:2*a/7}),
 'defect_identity':2*a-7*b-(2*A*c+7*(V-b)+16*rP-4*rQ),
 'B_difference':B-b-(2*t-s),
 'L0_event':p*Q2+w*(H-s)+r*P4+v*(t+rP)+7*p*(V-B)/4-L0,
 'L3_event':l1*Q3+l2*Q7+l3*P4+l4*(t+rP)+7*c*(V-B)/(4*(7-2*c))-L3,
 'R_capacity':(1-c/3)*Q7+c*P6/3-R-c*(1-A)/12,
 'L0_weights':p+w+r+v-1, 'L3_weights':l1+l2+l3+l4-1,
 'capacity_Q':DQ.subs({A:1,B:Bp,c:cp,U:Up,V:Bp})-S.Matrix([(1-a)/3,ep-(1-a)/3,0,-ep]),
 'capacity_P':DP.subs({A:1,B:Bp,c:cp,U:Up,V:Bp})-S.Matrix([0,0,ep,-ep]),
 'N0_beta':q.subs(b,beta),
 'N0_polynomial':N0.subs(a,S.Rational(49,50))-q/2500,
 'L0_margin':L0.subs(c,S.Rational(3,7))-ep-N0/(840*(2*a+6*b+1)),
 'L3_margin':L3.subs(c,S.Rational(3,7))-ep-(19*a+183*b-43)*(31*a+93*b-49)/(7224*(2*a+6*b+1)),
 'L3_at_cp':L3.subs(c,cp)-ep, 'R_at_cp':R.subs(c,cp)-ep,
 'G_gap':3*ep-(1-a)-3*G/(8*(2*a+6*b+1)),
}
for name,value in checks.items():
    for term in (list(value) if isinstance(value,S.MatrixBase) else [value]):
        res=S.factor(S.cancel(S.together(term)))
        assert res==0,(name,res)
assert q.subs(b,S.Rational(9,70))>0 and q.subs(b,S.Rational(13,100))<0
assert S.simplify(beta>S.Rational(9,70))==True
assert S.simplify(beta<S.Rational(13,100))==True
assert S.simplify(beta<S.Rational(1219,9150))==True
print('PASS_EXACT_SYMBOLIC',len(checks),'beta=',S.N(beta,20))

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
ratio={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
       'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(path,q0/4,q0/4*ratio[path][i]) for path,q0 in q2.items() for i in range(2) for j in range(2)]
assert len(leaves)==16 and all(q0>0 and p0>0 for _,q0,p0 in leaves)
assert sum(q0 for _,q0,_ in leaves)==sum(p0 for _,_,p0 in leaves)==1

def obs(A0,B0,c0,U0,V0,target=False):
    A0,B0,c0,U0,V0=map(F,[A0,B0,c0,U0,V0])
    assert 0<=A0<=1 and 0<=B0<=1 and 0<=c0<=1 and 0<=U0<=A0 and 0<=V0<=B0
    rates={'AU':F(1),'BU':F(0),'AV':F(0),'BV':F(0)} if target else {
        'AU':c0,'BU':c0,'AV':U0/A0 if A0 else F(0),'BV':V0/B0 if B0 else F(0)}
    outputs=[]
    for law in (1,2):
        z=[F(0)]*4
        for path,q0,p0 in leaves:
            mass=(q0,p0)[law-1]; x=A0 if path[0]=='A' else B0; y=rates[path]
            z[0]+=mass*(1-x);z[1]+=mass*x*(1-y)
            z[3 if path=='BU' else 2]+=mass*x*y
        assert sum(z)==1
        outputs.append(z)
    return outputs

def errors(a0,b0,A0,B0,c0,U0,V0):
    targ=obs(a0,b0,0,0,0,target=True)
    comp=obs(A0,B0,c0,U0,V0)
    return [sum(abs(x-y) for x,y in zip(t,c))/2 for t,c in zip(targ,comp)]

for aa,bb in ((F(49,50),F(129,1000)),(F(49,50),F(9,70)),(F(49,50),F(3,50))):
    cc=(7-aa-21*bb)/(4*aa+12*bb+2)
    B0=(aa+3*bb-1)/3
    e=cc*(aa+3*bb-1)/12
    assert errors(aa,bb,1,B0,cc,B0*(1+cc),B0)==[e,e]
    print('PASS_RECTANGLE_POINT',str(aa),str(bb),'c=',str(cc),'TV=',str(e))
for aa,bb in ((F(49,50),F(7,25)),(F(1,2),F(1,6)),(F(1,50),F(1,140))):
    assert bb>=2*aa/7
    assert errors(aa,bb,aa,bb,0,2*aa/7,2*aa/7)==[0,0]
print('PASS_ZERO_WEDGE',3)
rng=Random(2026102911)
for _ in range(1000):
    den=100
    aa=F(rng.randint(1,den),den);bb=F(rng.randint(1,den),den)
    AA=F(rng.randint(0,den),den); BB=F(rng.randint(0,den),den)
    cc=F(rng.randint(0,den),den)
    UU=AA*F(rng.randint(0,den),den);VV=BB*F(rng.randint(0,den),den)
    e=max(errors(aa,bb,AA,BB,cc,UU,VV))
    if bb<2*aa/7:
        assert e>=bb*(2*aa-7*bb)/(14+41*bb)
print('PASS_1000_EXACT_CAUSAL_COMPETITORS')
