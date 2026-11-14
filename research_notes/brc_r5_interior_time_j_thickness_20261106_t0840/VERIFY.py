from fractions import Fraction as F
from itertools import product
from random import Random
q=lambda a,b=1:F(a,b)
a=q(47,180); b=q(67,162); d=b-a
Q3=((q(13,20),q(1,5),q(3,20)),(q(1,40),q(9,20),q(21,40)))
H=((-282,323,41),(-160,160,-41),(-216,188,-139),(-2,1,-4),(2,-3,-4),(236,-274,-179),(80,-80,-23),(146,-123,23))
T=((q(1),q(1)),(q(483,160),q(221,80)),(q(519,160),q(239,80)),(q(613,160),q(293,80)),(q(4),q(4)),(q(559,160),q(293,80)),(q(211,80),q(117,40)),(q(203,80),q(113,40)))
P=((q(0),)*6,(q(1),q(0),q(1),q(0),q(0),q(21,80)),(q(1),q(0),q(1),q(0),q(9,40),q(21,80)),(q(1),q(1),q(1),q(0),q(13,40),q(27,80)),(q(1),q(1),q(1),q(27,80),q(13,40),q(27,80)),(q(1),q(1),q(1),q(27,80),q(13,40),q(0)),(q(1),q(1),q(0),q(13,40),q(1,10),q(0)),(q(1),q(1),q(0),q(13,40),q(0),q(0)))
C=(q(1,2),q(1,4),q(1,4),q(27,640),q(13,320),q(27,640)); TC=(q(15,8),)*2
def cap(x):return [sum(Q3[i][j]*x[i+1]/2 for i in range(2)) for j in range(3)]
def valid(x):
 g,u,v,*X=x
 return 0<=u<=g<=1 and 0<=v<=g and all(0<=z<=V for z,V in zip(X,cap(x)))
def time(x):
 g,u,v,x0,x1,x2=x
 return 1+g+(3*u+5*v)/8+x0/2+x1+3*x2/2,1+g+(u+v)/2+x0+x1+x2
def slack(i,t):return H[i][0]*t[0]+H[i][1]*t[1]-H[i][2]
def blend(x,y,s):return tuple(s*j+(1-s)*k for j,k in zip(x,y))
def width(x):
 _,u,v,_,X,_=x; A=u/10;B=9*v/40; S=A+B
 lo=max(a*X,b*X-d*A); hi=min(b*X,a*X+d*B)
 assert 0<=lo<=hi and hi-lo==d*min(A,B,X,S-X)
 if S:assert lo<=X*(a*A+b*B)/S<=hi
 return hi-lo
def witness(t):
 lam=min(slack(i,t)/slack(i,TC) for i in range(8)); assert 0<=lam<=1
 if lam==1:return lam,C
 boundary=blend(t,TC,q(1,1)/(1-lam))
 for j in range(8):
  k=(j+1)%8
  axis=next(h for h in (0,1) if T[j][h]!=T[k][h])
  s=(boundary[axis]-T[k][axis])/(T[j][axis]-T[k][axis])
  if 0<=s<=1 and blend(T[j],T[k],s)==boundary:
   x=blend(C,blend(P[j],P[k],s),lam)
   assert valid(x) and time(x)==t
   return lam,x
 raise AssertionError('missing boundary representation')
assert d==q(247,1620) and valid(C) and time(C)==TC
assert all(slack(i,TC)>0 for i in range(8))
assert all(valid(p) and time(p)==t for p,t in zip(P,T))
assert all([j for j,t in enumerate(T) if slack(i,t)==0]==([i,i+1] if i<7 else [0,7]) for i in range(8))
seen=set()
for g,u,v,z0,z1,z2 in product((q(0),q(1)),repeat=6):
 x=(g,g*u,g*v,*[p*z for p,z in zip(cap((g,g*u,g*v,0,0,0)),(z0,z1,z2))]);seen.add(time(x))
 assert valid(x) and all(slack(i,time(x))>=0 for i in range(8))
assert len(seen)==26 and width(C)==q(247,64800)
N=0
for j in range(8):
 for k in range(9):
  bd=blend(T[j],T[(j+1)%8],q(k,8))
  for r in range(1,13):
   t=blend(TC,bd,q(r,13)); lam,x=witness(t)
   assert lam>0 and width(x)>=q(247,64800)*lam;N+=1
rng=Random(202611060840)
for j in range(240):
 w=[q(rng.randint(1,49)) for _ in range(8)];tot=sum(w)
 t=tuple(sum(w[i]*T[i][h] for i in range(8))/tot for h in (0,1))
 assert all(slack(i,t)>0 for i in range(8))
 lam,x=witness(t); assert lam>0 and width(x)>=q(247,64800)*lam;N+=1
for j in range(8):
 for t in (T[j],blend(T[j],T[(j+1)%8],q(1,2))):
  lam,x=witness(t);assert lam==0 and width(x)==0
assert witness(TC)==(q(1),C)
print('center=',tuple(map(str,TC)),'J_width=',width(C))
print('center slacks=',tuple(map(str,(slack(i,TC) for i in range(8)))))
print('deterministic policies=64, distinct time values=',len(seen))
print('interior radial exact checks=',N)
print('PASS_EXACT_R5_INTERIOR_J_THICKNESS_RADIAL_CERTIFICATE')
