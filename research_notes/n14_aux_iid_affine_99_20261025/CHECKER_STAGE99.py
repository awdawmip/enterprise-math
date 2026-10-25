#!/usr/bin/env python3
"""Standalone Stage99 finite exact author checker; Python stdlib only."""
from fractions import Fraction as F
from functools import cache
from collections import defaultdict
p=(F(1,8),F(1,24),F(5,6));q=(F(1,12),F(1,12),F(5,6))
A=(11,3,0);B=(12,0,1);K=F(6696,5);LP=F(6312,5)
a0=F(2586269937332842327,7450150876955541504)
v0=F(757686022002985135,58204303726215168)
s0=F(12366057190345211,20889600000000000)
def child(v,i):
 n,a,b=v;return n+1,a+(i==0),b+(i==1)
@cache
def bell(v):
 n,a,b=v;opts={'P':K*F(2**(a+b),3**a),'Q':LP}
 if n<14:opts['C']=1+sum((p[i]*bell(child(v,i))[0] for i in range(3)),F())
 m=min(opts.values())
 return m,next(z for z in ('C','P','Q') if opts.get(z,None)==m),opts
def action(v):return 'C' if v in (A,B) else bell(v)[1]
@cache
def suffix(v):
 z=action(v)
 if z=='P':return F(0),F(1),F(0),F(0),1
 if z=='Q':return F(1),F(0),F(0),F(0),1
 w=[suffix(child(v,i)) for i in range(3)]
 return (sum((p[i]*w[i][0] for i in range(3)),F()),sum((q[i]*w[i][1] for i in range(3)),F()),
         1+sum((p[i]*w[i][2] for i in range(3)),F()),1+sum((q[i]*w[i][3] for i in range(3)),F()),sum(t[4] for t in w))
def propagate(u,s):
 layer={(0,0):(F(1),F(1),1)};acc=[F(0) for _ in range(4)]
 hits={A:[F(0),F(0),0],B:[F(0),F(0),0]}
 for n in range(15):
  out=defaultdict(lambda:(F(0),F(0),0))
  for (a,b),(x,y,c) in layer.items():
   v=n,a,b
   if v==A:
    hits[A][0]+=x;hits[A][1]+=y;hits[A][2]+=c
    acc[1]+=y*u;x*=1-u;y*=1-u
   elif v==B:
    hits[B][0]+=x;hits[B][1]+=y;hits[B][2]+=c
    acc[0]+=x*s;x*=1-s;y*=1-s
   else:
    z=action(v)
    if z=='P':acc[1]+=y;continue
    if z=='Q':acc[0]+=x;continue
   assert n<14
   acc[2]+=x;acc[3]+=y
   for i in range(3):
    aa,bb=a+(i==0),b+(i==1);xx,yy,cc=out[(aa,bb)]
    out[(aa,bb)]=(xx+x*p[i],yy+y*q[i],cc+c)
  layer=dict(out)
 assert not layer
 return acc,hits
if __name__=='__main__':
 gaps=[];ties=[]
 for n in range(15):
  for a in range(n+1):
   for b in range(n-a+1):
    v=(n,a,b);d,z,opts=bell(v)
    for other,val in opts.items():
     if other==z:continue
     gap=val-d;gaps.append(gap)
     if gap==0:ties.append((v,z,other))
 assert bell.cache_info().currsize==680 and len(gaps)==1240 and sum(x>0 for x in gaps)==1238
 assert not any(x<0 for x in gaps) and min(x for x in gaps if x>0)==F(12889,699840)
 assert set(ties)=={(A,'C','P'),(B,'C','Q')}
 zero,hits=propagate(F(0),s0)
 assert zero[0]==zero[1]==a0 and zero[2]==v0
 assert tuple(hits[A])==(F(21484375,286654464),F(21484375,967458816),165)
 assert tuple(hits[B])==(F(48828125,725594112),F(48828125,362797056),12)
 ra,rb=suffix(A),suffix(B)
 assert ra==(F(41,13824),F(569,576),F(69,64),F(167,144),9)
 assert rb==(F(63,64),F(1,144),F(9,8),F(13,12),5)
 pa,qa,_=hits[A];pb,qb,_=hits[B]
 X=pa*ra[0];Y=qa*(1-ra[1]);E=pb*(1-rb[0]);H=qb*rb[1]
 h=(X+Y)/(E+H);eta=E*h-X
 assert h==F(26961,108800) and eta==Y-H*h==F(107421875,2806920511488)
 assert 0<s0<s0+h<1
 assert a0+eta==F(2586555057332842327,7450150876955541504)
 assert v0-(LP+K)*eta==F(751890958002985135,58204303726215168)
 assert bell((0,0,0))[0]==v0+(LP+K)*a0==F(125467347054807071603,136951302885212160)
 diffs=[]
 for u in (F(0),F(1,7),F(1,2),F(1)):
  (ep,eq,tp,tq),_=propagate(u,s0+h*u)
  assert ep==eq==a0+eta*u and tp==v0-(LP+K)*eta*u and tp>tq
  assert tp+LP*ep+K*eq==bell((0,0,0))[0]
  if u in (F(0),F(1)):diffs.append(tp-tq)
 assert diffs==[F(1207595370727759775,1862537719238885376),F(1137415722727759775,1862537719238885376)]
 print('STAGE99_AUTHOR_EXACT_FINITE_PASS')
