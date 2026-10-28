#!/usr/bin/env python3
"""Exact symbolic duals and 16-leaf P/Q readout for BU-bit N4 algebraic optimum.
Whole-real-space optimality is proved by event certificates, not finite sampling.
"""
from collections import defaultdict
from pathlib import Path
import json
import sympy as S

q=S.Rational
ZERO=S.Integer(0)
simpl=S.simplify
a=q(1,2); b=q(1,40); z=S.Integer(1)
c0=(S.sqrt(2674)-34)/23
e0=(2*S.sqrt(2674)-101)/600
assert simpl(23*c0**2+68*c0-66)==0
assert simpl(e0-b*c0/(4+c0))==0
assert q(3,4)<c0<q(4,5)
A=a+3*e0; B=b-e0; U=B*(1+c0); V=B
assert simpl(B-4*b/(4+c0))==0
assert 0<B<b and a<A<a+3*b<1 and 0<U<2*b<A and V==B

AA,BB,UU,VV,aa,bb,zz,cc=S.symbols('A B U V a b z c')
s=(AA-aa+BB-bb)/2
t=(AA-aa+3*(BB-bb))/4
H=BB*cc/4
rq=aa*zz/6-AA*cc/6-UU/3-VV/4
rp=aa*zz/6-AA*cc/6-UU/12-VV/2
Q1=s;Q2=H-s-rq;Q3=H-rq;Q7=H
P4=rp;P5=t+rp;P6=H-t
al=(cc+4)/(23-2*cc);be=(3-7*cc)/(23-2*cc)
ga=2*(1+4*cc-cc*cc)/(23-2*cc);eta=2*(cc*cc-2*cc+7)/(23-2*cc)
w1=7*(1-cc)/20;w2=(7*cc-3)/20;w3=(3*cc+1)/10;w4=(7-3*cc)/10
l1=cc/(7-2*cc);l2=7*(1-cc)/(7-2*cc)
l3=2*cc*(2-cc)/(7-2*cc);l4=2*cc*cc/(7-2*cc);mu=7*cc/(4*(7-2*cc))
g1=cc/(4+cc);g2=2*(2-cc)/(4+cc);g3=2*cc/(4+cc)
low=(4*aa*zz-14*bb+aa*zz*cc-4*aa*cc-(aa+3*bb)*cc**2)/(2*(23-2*cc))
mid=(2*aa*zz-7*bb-(2*aa-bb)*cc)/20
high=cc*(aa*(zz-cc)-3*bb*cc)/(2*(7-2*cc))
growth=bb*cc/(4+cc)
checks={
 'weights_low':al+be+ga+eta-1,
 'weights_mid':w1+w2+w3+w4-1,
 'weights_high':l1+l2+l3+l4-1,
 'weights_growth':g1+g2+g3-1,
 'dual_low':al*Q2+be*(H-s)+ga*P4+eta*P5+7*al*(VV-BB)/4-low,
 'dual_mid':w1*Q2+w2*Q3+w3*P4+w4*P5+S.Rational(7,20)*(VV-BB)-mid,
 'dual_high':l1*Q3+l2*Q7+l3*P4+l4*P5+mu*(VV-BB)-high,
 'dual_growth':g1*Q1+g2*Q7+g3*P6-growth}
for name,value in checks.items():
 assert simpl(value)==0,(name,simpl(value))
assert simpl(high.subs({aa:a,bb:b,zz:z,cc:c0})-e0)==0
assert simpl(growth.subs({bb:b,cc:c0})-e0)==0
assert q(1767,90160)>q(3,640)>e0
assert simpl((140-322*cc+46*cc*cc).subs(cc,q(3,4)))<0
assert simpl(S.diff(140-322*cc+46*cc*cc,cc).subs(cc,1))<0
sr=(A-a+B-b)/2;tr=(A-a+3*(B-b))/4;Hr=B*c0/4
rqr=a*z/6-A*c0/6-U/3-V/4
rpr=a*z/6-A*c0/6-U/12-V/2
assert all(simpl(x-y)==0 for x,y in zip((sr,tr,Hr,rqr,rpr),(e0,0,e0,0,e0)))

cond={'A':{'U':q(1,3),'V':q(2,3)},'B':{'U':q(1,2),'V':q(1,2)}}
lr={'AU':(q(9,10),q(11,10)),'AV':(q(1,4),q(1,4)),
    'BU':(q(1,5),q(9,5)),'BV':(S.Integer(2),S.Integer(2))}
leaves=[]
for first in ('A','B'):
 for second in ('U','V'):
  for k in (0,1):
   for j in (0,1):
    Q=q(1,2)*cond[first][second]/4
    P=Q*lr[first+second][k]
    leaves.append((first,first+second,k,j,P,Q))
assert len(leaves)==16
assert sum(row[4] for row in leaves)==sum(row[5] for row in leaves)==1
assert all(row[4]>0 and row[5]>0 for row in leaves)

def obs(candidate,law):
 out=defaultdict(lambda:ZERO)
 for first,prefix,k,j,P,Q in leaves:
  mass=P if law=='P' else Q
  r1=(A if first=='A' else B) if candidate else (a if first=='A' else b)
  r2=({'AU':c0,'BU':c0,'AV':U/A,'BV':V/B}[prefix] if candidate else
      {'AU':z,'BU':ZERO,'AV':ZERO,'BV':ZERO}[prefix])
  out[(1,'Q',0)]+=mass*(1-r1)
  out[(2,'Q',0)]+=mass*r1*(1-r2)
  decision=('Q' if prefix=='BU' else 'P') if candidate else ('P' if prefix=='AU' else 'Q')
  out[(3,decision,1 if prefix=='BU' else 0)]+=mass*r1*r2
 assert simpl(sum(out.values())-1)==0
 return out

def tv(first,second):
 return simpl(sum((S.Abs(simpl(first.get(k,ZERO)-second.get(k,ZERO)))
   for k in set(first)|set(second)),ZERO)/2)
for law in ('Q','P'):
 original=obs(False,law); alternative=obs(True,law)
 assert simpl(tv(original,alternative)-e0)==0
 expected=([e0,0,0,-e0] if law=='Q' else [0,0,e0,-e0])
 for key,want in zip([(1,'Q',0),(2,'Q',0),(3,'P',0),(3,'Q',1)],expected):
  assert simpl(original.get(key,ZERO)-alternative.get(key,ZERO)-want)==0
print('PASS_EXACT_N4_BU_NONUNIT_A_ALGEBRAIC_GLOBAL_MINIMAX')
print('exact_value=',e0,'approx=',S.N(e0,18))
print('all_dual_residuals=',{key:str(simpl(value)) for key,value in checks.items()})
print('positive_terminal_leaves=',len(leaves))
print('TV_Q=',tv(obs(False,'Q'),obs(True,'Q')))
print('TV_P=',tv(obs(False,'P'),obs(True,'P')))
