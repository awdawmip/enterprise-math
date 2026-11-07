#!/usr/bin/env python3
"""Exact Fraction verifier for the all-real R5 two-extreme-key four-cube."""
from fractions import Fraction as F
from itertools import product

H=F(1,52); KAP=F(13,10); K=F(353,942)
RM=F(1,10); RP=F(19,10)
RS=(RM,F(1,2),F(3,4),F(1),F(5,4),F(3,2),RP)
SECTION=(
 (F(7129,20000),F(137,500),F(29,400),F(79,1000),F(1039,20000)),
 (F(-2011,104000),F(-3,200),F(-9,2000),F(3,500),F(3649,104000)),
 (F(673,52000),F(1,100),F(23,1000),F(-3,250),F(-843,52000)),
)

def flow(za,zb):
 return tuple(SECTION[0][i]+za*SECTION[1][i]+zb*SECTION[2][i] for i in range(5))

def capacities(u):
 return ((F(13,40)+KAP/80)*u,
         (F(1,10)+F(9,40)*KAP)*u,
         (F(3,40)+F(21,80)*KAP)*u)

def masses(t):
 g,u,x0,x1,x2=t;v0,v1,v2=capacities(u);j=K*x1
 out={
 RM:(509*x0+9*x2)/900+j,
 F(1,2):v0-x0,
 F(3,4):(g-u)/2,
 F(1):1-g+v1+F(382,900)*(x0+x2)-2*j,
 F(5,4):(g-KAP*u)/2,
 F(3,2):v2-x2,
 RP:(9*x0+509*x2)/900+j
 }
 assert all(v>=0 for v in out.values())
 assert sum(out.values())==1 and sum(r*v for r,v in out.items())==1
 A=u/10;B=F(9,40)*KAP*u
 assert (A+B)*j==x1*(F(47,180)*A+F(67,162)*B)
 return out

def timing(t):
 g,u,x0,x1,x2=t
 return (1+g+(3+5*KAP)*u/8+x0/2+x1+3*x2/2,
         1+g+(1+KAP)*u/2+x0+x1+x2)

def corner(t):
 g,u,x0,x1,x2=t;v0,v1,v2=capacities(u);m=masses(t)
 return {
 "g>=0":g,"1-g>=0":1-g,"u0>=0":u,"g-u0>=0":g-u,
 "g-u1>=0":g-KAP*u,"X0>=0":x0,"V0-X0>=0":v0-x0,
 "X1>=0":x1,"V1-X1>=0":v1-x1,"X2>=0":x2,
 "V2-X2>=0":v2-x2,
 "M_1/10 >= 29h/9":m[RM]-F(29,9)*H,
 "M_19/10 >= 11h/9":m[RP]-F(11,9)*H
 }

def check_kernels():
 q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
 q4=((F(509,900),F(382,900),F(9,900)),
     (F(47,180),F(43,90),F(47,180)),
     (F(9,900),F(382,900),F(509,900)),
     (F(67,162),F(14,81),F(67,162)))
 for row,r in zip(q3,(F(3,4),F(5,4))):
  assert min(row)>0 and sum(row)==1
  assert sum(p*x for p,x in zip(row,(F(1,2),F(1),F(3,2))))==r
 for row,r in zip(q4,(F(1,2),F(1),F(3,2),F(1))):
  assert min(row)>0 and sum(row)==1
  assert sum(p*x for p,x in zip(row,(RM,F(1),RP)))==r
 assert K==(F(47,180)/10+F(67,162)*F(9,40)*KAP)/(F(1,10)+F(9,40)*KAP)

def main():
 check_kernels()
 minimum={}
 for za,zb in product((-1,1),repeat=2):
  t=flow(F(za),F(zb))
  assert timing(t)==(F(15,8)+za*H,F(15,8)+zb*H)
  for name,v in corner(t).items():
   minimum[name]=min(minimum.get(name,v),v)
   assert v>0,(za,zb,name,v)
 grid=(-F(1),-F(1,2),F(0),F(1,2),F(1)); count=0
 for za,zb,zc,zd in product(grid,repeat=4):
  t=flow(za,zb)
  assert timing(t)==(F(15,8)+za*H,F(15,8)+zb*H)
  m=masses(t);c=zc*H;d=zd*H
  decl={r:F(1,2) for r in RS}
  decl[RM]+=(10*c+19*d)/(18*m[RM])
  decl[RP]-=(10*c+d)/(18*m[RP])
  assert all(0<=v<=1 for v in decl.values())
  ep=1-sum(r*m[r]*decl[r] for r in RS)
  eq=sum(m[r]*decl[r] for r in RS)
  assert (ep,eq)==(F(1,2)+c,F(1,2)+d)
  count+=1
 assert count==625
 print("H",H,"IMPROVEMENT_FACTOR",H/F(10395,788344))
 for name in sorted(minimum):print("MIN_MARGIN",name,minimum[name])
 print("GRID_POINTS_EXACT",count)
 print("PASS_EXACT_R5_TWO_EXTREME_LABEL_KEYS_FOUR_CUBE_1_OVER_52")

if __name__=="__main__":
 main()
