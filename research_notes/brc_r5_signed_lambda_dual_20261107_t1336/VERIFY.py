#!/usr/bin/env python3
"""Exact Fraction verifier for R5 signed support perturbations +/-1/10.

Both gap identities are affine in seven flow variables, so equality at
the origin plus all seven unit vectors certifies equality for all real flows.
"""
from fractions import Fraction as F
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
Z=F(0)
CERT={
 F(1,10):(F(27083,116250),(F(-43037,348750),F(81727,348750)),
  (F(13079,558000),F(332837,2790000),F(67769,558000),F(112541,2790000),F(21983,162000))),
 F(-1,10):(F(16456,58125),(F(21007,348750),F(9403,348750)),
  (F(13781,558000),F(46481,930000),F(54791,558000),F(183499,2790000),F(17537,162000)))
}
def model(g,a,b,u,v,w,z,legal=False):
 c0=F(13,40)*a+b/80
 c1=a/10+F(9,40)*b
 c2=F(3,40)*a+F(21,80)*b
 tp=1+g+(3*a+5*b)/8+u/2+v+F(3,2)*w
 tq=1+g+(a+b)/2+u+v+w
 m0=F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100
 m6=u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w
 mm=(m0,c0-u,(g-a)/2,
   1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
   (g-b)/2,c2-w,m6)
 sl=(g-b,u,c1-v,w,F(9,40)*b-v+z)
 if legal:
  assert 0<=a<=g<=1 and 0<=b<=g
  assert 0<=u<=c0 and 0<=v<=c1 and 0<=w<=c2
  assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
  assert min(mm)>=0 and sum(mm,Z)==1
  assert sum((mj*rj for mj,rj in zip(mm,R)),Z)==1
 for lam,(bound,(np,nq),mu) in CERT.items():
  ss=sum((max(Z,1-(1+lam)*rj)*mj for mj,rj in zip(mm,R)),Z)
  gap=bound+np*(tp-F(31,10))+nq*(tq-F(31,10))-ss
  assert gap==sum((x*y for x,y in zip(mu,sl)),Z)
  if legal and tp==tq==F(31,10):
   assert gap>=0
 return tp,tq,mm
model(*(Z,)*7)
for k in range(7):
 x=[Z]*7;x[k]=F(1);model(*x)
print("PASS_16_EXACT_AFFINE_CERTIFICATE_BASES")
for j in range(94):
 q=F(j,93)
 fl=(q,q,q,Z,F(13,40)*q,Z,q/10)
 tp,tq,m=model(*fl,legal=True)
 assert tp==tq==1+F(93,40)*q
 assert m==(F(143,1200)*q,F(27,80)*q,Z,
   1-F(137,150)*q,Z,F(27,80)*q,F(143,1200)*q)
 assert 9*fl[2]*fl[6]==4*fl[1]*(fl[4]-fl[6])
 for lam in CERT:
  e=[m[k] if 1-(1+lam)*R[k]>0 else Z for k in range(7)]
  eQ=sum(e,Z); eP=1-sum((x*rj for x,rj in zip(e,R)),Z)
  U=eQ-(1+lam)*(1-eP)
  expected=F(3869,34875)*(tp-1) if lam>0 else F(1,10)+F(3041,34875)*(tp-1)
  assert U==expected
 if q==F(28,31):
  assert tp==F(31,10)
  assert m==(F(1001,9300),F(189,620),Z,F(407,2325),Z,F(189,620),F(1001,9300))
print("PASS_94_SEEDLESS_RATIONAL_FLOWS_PLUS_TWO_DIRECTIONS")
for j in range(1,30):
 gg=F(j,30);aa=gg*F(2,3);bb=gg*F(4,5)
 c0=F(13,40)*aa+bb/80
 c1=aa/10+F(9,40)*bb
 c2=F(3,40)*aa+F(21,80)*bb
 vv=c1*F(2,5)
 zz=vv*(aa/10)/c1
 model(gg,aa,bb,c0/3,vv,c2/4,zz,legal=True)
print("PASS_29_ASYMMETRIC_LEGAL_FULL_HIST_CHECKS")
print("SHARP_T_31_10_PLUS eP=9728/11625 eQ=959/2325 U=27083/116250")
print("SHARP_T_31_10_MINUS eP=7693/11625 eQ=1366/2325 U=16456/58125")
print("PASS_EXACT_R5_SIGNED_PERTURBATION_TWO_SLOPES_REAL_INTERVAL")
