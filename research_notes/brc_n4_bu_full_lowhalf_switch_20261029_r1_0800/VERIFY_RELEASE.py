#!/usr/bin/env python3
"""Exact symbolic BRC N4 BU switch certificate; finite 16-leaf checks."""
from fractions import Fraction as F
from collections import defaultdict
import sympy as s
A,B,U,V,a,b,c=s.symbols('A B U V a b c',real=True)
x=(A-a+B-b)/2; y=(A-a+3*(B-b))/4; H=B*c/4
r=a/6-A*c/6-U/3-V/4; q=a/6-A*c/6-U/12-V/2
Q1=x;Q2=H-x-r;Q3=H-r;Q7=H;P4=q;P5=y+q;P6=H-y
low=((c+4)/(23-2*c),(3-7*c)/(23-2*c),2*(1+4*c-c*c)/(23-2*c),2*(c*c-2*c+7)/(23-2*c))
mid=(c/(7-2*c),7*(1-c)/(7-2*c),2*c*(2-c)/(7-2*c),2*c*c/(7-2*c))
high=(c/(4+c),2*(2-c)/(4+c),2*c/(4+c))
L0=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c)); g=b*c/(4+c)
checks={
 'low_weight':sum(low)-1,
 'mid_weight':sum(mid)-1,
 'high_weight':sum(high)-1,
 'low_dual':sum(i*j for i,j in zip(low,(Q2,H-x,P4,P5)))+7*low[0]*(V-B)/4-L0,
 'mid_dual':sum(i*j for i,j in zip(mid,(Q3,Q7,P4,P5)))+7*c*(V-B)/(4*(7-2*c))-L3,
 'high_dual':sum(i*j for i,j in zip(high,(Q1,Q7,P6)))-g
}
c0=(2*a-7*b)/(2*a+4*b);c1=4*c0/(4-c0);e0=b*c0/4
f=(a+3*b)*c*c+(3*a+8*b)*c+14*b-4*a
checks.update({
 'L0_c0':L0.subs(c,c0)-e0,
 'L3_c0':L3.subs(c,c0)-e0,
 'g_c1':g.subs(c,c1)-e0,
 'f_c0':f.subs(c,c0)+b*(2*a-7*b)*(5*a+21*b)/(4*(a+2*b)**2),
 'f_c1':f.subs(c,c1)-2*(2*a-7*b)*(16*a*a-50*a*b-329*b*b)/(6*a+23*b)**2,
 'L3_g':L3-g+c*f/(2*(7-2*c)*(4+c)),
 'L3_c1':L3.subs(c,c1)-e0+(2*a-7*b)**2*(16*a*a-50*a*b-329*b*b)/(8*(a+2*b)*(6*a+23*b)*(26*a+217*b))
})
for k,z in checks.items():
 assert s.cancel(z)==0,(k,s.factor(z))
bb=s.Rational(1,40);tau=(25+s.sqrt(5889))/640
assert s.simplify((16*a*a-50*a*bb-329*bb*bb).subs(a,tau))==0
assert s.Rational(7,80)<tau<s.Rational(61,320)<s.Rational(1,2)
assert s.factor(L0.subs({b:bb,c:s.Rational(3,7)})-e0.subs(b,bb)-(80*a-1)*(320*a-61)/(22400*(20*a+1)))==0
assert s.factor(L3.subs({b:bb,c:s.Rational(3,7)})-e0.subs(b,bb)-(240*a-31)*(320*a-61)/(192640*(20*a+1)))==0
def leaves():
 cond={'A':{'U':F(1,3),'V':F(2,3)},'B':{'U':F(1,2),'V':F(1,2)}}
 ratios={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
 out=[]
 for i in 'AB':
  for j in 'UV':
   for k in (0,1):
    for l in (0,1):
     q=F(1,2)*cond[i][j]/4
     out.append((i,i+j,q*ratios[i+j][k],q))
 return out
tree=leaves()
assert len(tree)==16 and all(p>0 and q>0 for _,_,p,q in tree)
assert sum(row[2] for row in tree)==sum(row[3] for row in tree)==1
def obs(aa,kind,law,cc=None):
 bb=F(1,40)
 if kind=='zero': AA=aa;BB=bb;C=F(0);UU=VV=2*aa/7
 elif kind=='linear': C=(2*aa-7*bb)/(2*aa+4*bb);AA=aa;BB=bb;UU=bb*(1+C);VV=bb
 elif kind=='root': C=cc;eps=bb*C/(4+C);AA=aa+3*eps;BB=bb-eps;UU=BB*(1+C);VV=BB
 else: AA=aa;BB=bb;C=UU=VV=F(0)
 assert kind=='target' or (0<=C<=1 and 0<=AA<=1 and 0<=BB<=1 and 0<=UU<=AA and 0<=VV<=BB)
 out=defaultdict(F)
 for i,j,p,q in tree:
  mass=p if law=='P' else q
  t1=AA if i=='A' else BB
  t2=((C if j in ('AU','BU') else UU/AA if j=='AV' else VV/BB)
      if kind!='target' else (F(1) if j=='AU' else F(0)))
  out[(1,'Q',0)]+=mass*(1-t1)
  out[(2,'Q',0)]+=mass*t1*(1-t2)
  dc=(('Q' if j=='BU' else 'P') if kind!='target' else ('P' if j=='AU' else 'Q'))
  out[(3,dc,int(j=='BU'))]+=mass*t1*t2
 assert sum(out.values())==1
 return out
def check_case(aa,kind,expected,cc=None):
 for law in 'PQ':
  goal=obs(aa,'target',law); found=obs(aa,kind,law,cc)
  tv=sum((abs(goal[k]-found[k]) for k in set(goal)|set(found)),F())/2
  assert tv==expected,(aa,kind,law,tv,expected)
for aa in (F(1,20),F(7,80)):
 check_case(aa,'zero',F(0))
for aa in (F(1,8),F(3,20),F(5,32)):
 cc=(2*aa-7*F(1,40))/(2*aa+4*F(1,40))
 check_case(aa,'linear',F(1,40)*cc/4)
for cc in (F(2,5),F(1,2),F(3,5),F(3,4)):
 aa=F(1,40)*(3*cc*cc+8*cc+14)/(4-3*cc-cc*cc)
 check_case(aa,'root',F(1,40)*cc/(4+cc),cc)
print('PASS_EXACT_BU_N4_A_GAP_SWITCH_RELEASE')
print('tau=',s.N(tau,25),'symbolic identities=',len(checks),'exact 16-leaf cases=9')
