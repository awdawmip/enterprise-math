"""Stage200 exact dual candidate scan starting from Stage199, no primal claim."""
from fractions import Fraction as F
from functools import cache
P=(F(3,24),F(1,24),F(20,24))
K=F(213288424,1523041); B=(7,0,1); Z=(14,0,0)
def nxt(s,i):
 n,a,b=s
 return n+1,a+int(i==0),b+int(i==1)
def lr(s):
 _,a,b=s
 return F(2**(a+b),3**a)
@cache
def h(s):
 vals={'P':K*lr(s),'Q':K}
 if s[0]<14: vals['C']=1+sum(P[i]*h(nxt(s,i))[0] for i in range(3))
 v=min(vals.values())
 return v,tuple(a for a in ('P','Q','C') if a in vals and vals[a]==v)
@cache
def sel(s):
 if s in (B,Z):return 'Q'
 assert len(h(s)[1])==1,(s,h(s)[1])
 return h(s)[1][0]
@cache
def coeff(s):
 return coeff_action(s,sel(s))
def coeff_action(s,a):
 if a=='P':return F(0),lr(s),F(0)
 if a=='Q':return F(0),F(0),F(1)
 kids=[coeff(nxt(s,i)) for i in range(3)]
 return tuple(F(j==0)+sum(P[i]*kids[i][j] for i in range(3)) for j in range(3))
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
closings=[];ties=[]
for s in states:
 old=sel(s)
 for a in ('P','Q')+(('C',) if s[0]<14 else ()):
  if a==old:continue
  x=coeff_action(s,a);y=coeff(s)
  d=tuple(x[i]-y[i] for i in range(3))
  gap=d[0]+K*(d[1]+d[2]);slope=d[1]+d[2]
  assert gap>=0,(s,a,gap)
  if gap==0: ties.append((s,old,a))
  if gap>0 and slope>0:closings.append((gap/slope,s,old,a))
assert {x[0] for x in ties}=={B,Z}
step,s,old,new=min(closings)
assert (s,old,new)==((7,5,2),'C','P')
assert step==F(137621064921653408,15756764499968999)
knew=K-step
assert knew==F(1358449620408,10345594439)
@cache
def nh(s):
 vals={'P':knew*lr(s),'Q':knew}
 if s[0]<14:vals['C']=1+sum(P[i]*nh(nxt(s,i))[0] for i in range(3))
 best=min(vals.values())
 return best,tuple(a for a in ('P','Q','C') if a in vals and vals[a]==best),tuple(v-best for v in vals.values() if v>best)
assert nh((0,0,0))[0]==F(1821575844832789801808808179,17710532969288194722889728)
assert {s:nh(s)[1] for s in states if len(nh(s)[1])>1}=={(7,5,2):('P','C'),Z:('P','Q')}
gaps=[v for s in states for v in nh(s)[2]]
assert len(states)==680 and len(gaps)==1238 and min(gaps)==F(136269916,10345594439)
print("STAGE200_DUAL_SCAN_PASS",knew,nh((0,0,0))[0],step)
