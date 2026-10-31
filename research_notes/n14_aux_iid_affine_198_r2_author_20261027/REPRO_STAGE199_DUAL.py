"""Standalone Stage199 dual candidate checker; primal optimum is NOT asserted."""
from fractions import Fraction as F
from functools import cache
p=(F(3,24),F(1,24),F(20,24))
k=F(55173536856,391511335)
T=14
A=(8,5,2);Z=(14,0,0)
def child(s,i):
 n,a,b=s
 return n+1,a+(i==0),b+(i==1)
@cache
def b0(s):
 n,a,b=s
 d={'P':k*F(2**(a+b),3**a),'Q':k}
 if n<T:d['C']=1+sum(p[i]*b0(child(s,i))[0] for i in range(3))
 m=min(d.values())
 return m,tuple(x for x in d if d[x]==m)
@cache
def selected(s):
 if s==A:return 'P'
 if s==Z:return 'Q'
 assert len(b0(s)[1])==1
 return b0(s)[1][0]
@cache
def coeff(s):
 n,a,b=s
 x=selected(s)
 if x=='P':return F(0),F(2**(a+b),3**a),F(0)
 if x=='Q':return F(0),F(0),F(1)
 kids=[coeff(child(s,i)) for i in range(3)]
 return tuple((int(j==0))+sum(p[i]*kids[i][j] for i in range(3)) for j in range(3))
def action_coeff(s,x):
 n,a,b=s
 if x=='P':return F(0),F(2**(a+b),3**a),F(0)
 if x=='Q':return F(0),F(0),F(1)
 kids=[coeff(child(s,i)) for i in range(3)]
 return tuple(int(j==0)+sum(p[i]*kids[i][j] for i in range(3)) for j in range(3))
def minus(v,w):return tuple(v[i]-w[i] for i in range(3))
def cost(v,x):return v[0]+x*(v[1]+v[2])
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(states)==680
changes=[];flat=[]
for s in states:
 old=selected(s)
 for alt in ('P','Q')+(('C',) if s[0]<14 else ()):
  if alt==old:continue
  d=minus(action_coeff(s,alt),action_coeff(s,old))
  gap=cost(d,k);rate=-d[1]-d[2]
  assert gap>=0
  if gap==0:flat.append((s,old,alt,rate))
  if gap>0 and rate<0:changes.append((-gap/rate,s,old,alt))
assert set(s for s,*_ in flat)=={A,Z}
assert next(v for s,a,b,v in flat if s==A)==F(391511335,46438023168)
changes.sort();step,s,old,new=changes[0]
assert s==(7,0,1) and old=='C' and new=='Q'
assert step==F(526723126413056,596287815169735)
knew=k-step
@cache
def bn(s):
 n,a,b=s
 d={'P':knew*F(2**(a+b),3**a),'Q':knew}
 if n<14:d['C']=1+sum(p[i]*bn(child(s,i))[0] for i in range(3))
 v=min(d.values())
 return v,tuple(t for t in d if d[t]==v),tuple(q-v for q in d.values() if q>v)
assert knew==F(213288424,1523041)
assert bn((0,0,0))[0]==F(13641932749948792109334011,125149469578557848027136)
assert {s:bn(s)[1] for s in states if len(bn(s)[1])>1}=={(7,0,1):('Q','C'),Z:('P','Q')}
positive=[q for s in states for q in bn(s)[2]]
assert len(positive)==1238 and min(positive)==F(2057512212551,276277395483648)
print('STAGE199_INDEPENDENT_DUAL_PASS',len(states),len(positive),step)
