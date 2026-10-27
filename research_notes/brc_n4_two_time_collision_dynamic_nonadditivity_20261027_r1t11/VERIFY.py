from fractions import Fraction as F
import json
r=(F(1,2),F(1),F(3,2),F(2))
a=(F(1,4),)*4
b=(F(3,8),F(3,8),F(1,8),F(1,8))
va=(1,-2,1,0);vb=(0,1,-2,1)
def sm(x):return sum(x,F(0))
def dot(x,y):return sm(u*v for u,v in zip(x,y))
def add(x,y):return tuple(u+v for u,v in zip(x,y))
def ker(base,v,t):return tuple(x+t*y for x,y in zip(base,v))
ap=ker(a,va,F(1,12));am=ker(a,va,-F(1,12))
bp=ker(b,vb,F(1,24));bm=ker(b,vb,-F(1,24))
for k,lr in ((ap,F(5,4)),(am,F(5,4)),(bp,F(1)),(bm,F(1))):
 assert min(k)>0 and sm(k)==1 and dot(k,r)==lr
 assert sm(r[i]*k[i]/lr for i in range(4))==1
shift=(F(1,24),F(0),F(0),-F(1,24))
for k in (ap,am):
 u=add(tuple(x/2 for x in k),shift)
 v=add(tuple(x/2 for x in k),tuple(-x for x in shift))
 assert min(u+v)>0 and sm(u)==sm(v)==F(1,2)
 assert dot(u,r)==F(9,16) and dot(v,r)==F(11,16)
 for h,s in ((u,F(9,8)),(v,F(11,8))):
  assert sm(2*x for x in h)==1
  assert sm(2*r[i]*h[i]/s for i in range(4))==1
assert dot((F(3,20),F(3,20),F(3,10),F(2,5)),(F(5,4),F(5,4),F(1),F(13,16)))==1
n=add(tuple(F(3,20)*x for x in a),tuple(F(3,20)*x for x in b))
assert n==(F(15,160),F(15,160),F(9,160),F(9,160))
cases={
 'A':((1,0,F(1,2),F(1,2)),F(1),(0,F(1,6),1,1),F(1,320)),
 'B':((F(1,2),F(1,2),1,0),F(3,2),(0,0,F(2,15),1),F(1,800)),
 'AB':((1,0,1,0),F(1),(0,F(1,10),1,1),F(1,320))}
out={}
for name,(q,t,xprime,want) in cases.items():
 m=tuple(F(3,20)*(q[0]*ap[i]+q[1]*am[i]+q[2]*bp[i]+q[3]*bm[i]) for i in range(4))
 assert sm(m)==F(3,10) and dot(m,r)==F(27,80)
 Sj=tuple(sm((m[i]-n[i])*max(F(0),r[i]-z) for i in range(4)) for z in r)
 D=max((F(0),)+(tuple(Sj[i]/(1+r[i]) for i in range(4))))
 assert D==want
 x=(tuple(F(int(v>t)) for v in r))
 xprime=tuple(F(v) for v in xprime)
 oq=dot(m,x);op=sm(r[i]*m[i]*x[i] for i in range(4))
 nq=dot(n,xprime);np=sm(r[i]*n[i]*xprime[i] for i in range(4))
 assert nq-oq==op-np==D
 out[name]={'D':str(D),'terminal_Q':list(map(str,m)),'S':list(map(str,Sj)),
           'terminal_x':list(map(str,x)),'repair_x':list(map(str,xprime))}
for t,lam,mu in ((F(1),F(3,16),F(9,16)),(F(3,2),F(1,8),F(1,8))):
 assert lam>=0 and mu>=0 and lam+mu<=1
 for base,R in ((a,F(5,4)),(b,F(1))):
  assert sm(base[i]*max(F(0),r[i]-t) for i in range(4))==lam*R+mu*(R-t)
assert F(1,320)<F(1,320)+F(1,800)
assert sum((F(11,20),F(3,20),F(3,10)))==1
assert sum((F(41,80),F(3,20),F(27,80)))==1
print(json.dumps({'status':'PASS_EXACT_FRACTION_TWO_TIME_COLLISION','cases':out,
  'nonadditivity':{'A':'1/320','B':'1/800','AB':'1/320','gap':'1/800'}},sort_keys=True,indent=2))
