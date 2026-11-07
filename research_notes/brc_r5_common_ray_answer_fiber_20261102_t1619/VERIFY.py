"""R5 common-ray family: exact rational validation of the source fibre."""
from fractions import Fraction as F
from itertools import product, permutations
S=('C','I','BJ','IJ')
H=F(1,2)
def obs(u, pol):
 x,jb,ji,kc,ki,kbj,kij=map(F,pol)
 ks=(kc,ki,kbj,kij); w=(F(1,4),(1-x)/4,(1-jb)/8,(1-x)*(1-ji)/8)
 D=((1-jb)+(1-x)*(1-ji))/8
 C=sum((m*(1-k) for m,k in zip(w,ks)),F(0))
 U=sum((m*(1-k)*ui for m,k,ui in zip(w,ks,(u[0],u[1],u[2],u[2]))),F(0))
 O=(1-F(2,5)*D-U,F(3,5)*D+U,F(5,2)-F(3,4)*x+2*D+F(3,2)*C,F(5,2)-F(3,4)*x+2*D+F(4,3)*C)
 return tuple(O),(x,D,C,U)
def lr(x,y,z):return (x,y,y,z,z,z,z)
def det(a):
 n=len(a);out=F(0)
 for perm in permutations(range(n)):
  sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  val=F(sign)
  for i in range(n):val*=a[i][perm[i]]
  out+=val
 return out
def jac(u):
 mid=[H]*7;v=[]
 for k in (0,1,3,4):
  a=mid.copy();b=mid.copy();a[k]=0;b[k]=1
  lo=obs(u,a)[0];hi=obs(u,b)[0]
  v.append(tuple(y-x for x,y in zip(lo,hi)))
 return det([[v[k][i] for k in range(4)] for i in range(4)])
cases=[(F(1,2),F(1,4),F(1,3)),(H,H,H),(F(1,3),H,F(1,4)),
       (F(2,5),F(3,5),F(1,5)),(F(1,4),F(1,4),F(2,3)),
       (F(2,3),H,F(2,3)),(F(1,5),F(2,5),F(3,5))]
checks=0
for u in cases:
 assert all(0<a<1 for a in u);checks+=1
 full={v:obs(u,v)[0] for v in product((0,1),repeat=7)}
 lrverts={v:obs(u,lr(*v))[0] for v in product((0,1),repeat=3)}
 assert len(full)==128 and len(lrverts)==8;checks+=1
 for alpha in range(-4,5):
  for beta in range(-4,5):
   if alpha==beta==0:continue
   hF=max(alpha*v[0]+beta*v[1] for v in full.values())
   hL=max(alpha*v[0]+beta*v[1] for v in lrverts.values())
   assert hF==hL,(u,alpha,beta,hF,hL);checks+=1
 for pol,W in full.items():
  x,D,C,U=obs(u,pol)[1]
  assert W[0]==1-F(2,5)*D-U and W[1]==F(3,5)*D+U;checks+=1
  assert D==5*(W[0]+W[1]-1) and U==W[1]-F(3,5)*D;checks+=1
  assert C==6*(W[2]-W[3]);checks+=1
  assert x==F(4,3)*(F(5,2)+2*D+F(3,2)*C-W[2]);checks+=1
 w1=obs(u,(0,1,1,0,1,1,1))[1]
 w2=obs(u,(1,0,1,0,1,1,1))[1]
 assert w1==(0,0,F(1,4),u[0]/4);checks+=1
 assert w2==(1,F(1,8),F(1,4),u[0]/4);checks+=1
 assert w1[3]-(u[0]+u[1])*w1[2]/2==(u[0]-u[1])/8;checks+=1
 assert w2[3]-(2*u[0]+u[2])*w2[2]/3==(u[0]-u[2])/12;checks+=1
 p=list(lrverts.values())
 d=det([[p[k][i]-p[0][i] for k in (1,2,3,4)] for i in range(4)])
 assert d==-(2*u[2]-u[0]-u[1])/2560;checks+=1
 assert jac(u)==-(u[0]-u[1])/10240;checks+=1
 print('TRIPLE',*u,'LR_DET',d,'FULL_JAC',jac(u))
u=(F(1,2),F(1,4),F(1,3))
f=[obs(u,v)[0] for v in product((0,1),repeat=7)]
l=[obs(u,lr(*v))[0] for v in product((0,1),repeat=3)]
n=(-256,-244,-155,171)
dot=lambda p:sum((a*b for a,b in zip(n,p)),F(0))
hF=max(map(dot,f));hL=max(map(dot,l))
W=obs(u,(0,1,1,0,1,1,1))[0]
assert W==(F(7,8),F(1,8),F(23,8),F(17,6));checks+=1
assert (hF,hL,hF-hL)==(F(-1725,8),-216,F(3,8));checks+=1
assert dot(W)==hF;checks+=1
assert (hF-hL)/sum(map(abs,n))==F(3,6608);checks+=1
print('EXACT_FACET',n,'W',W,'FULL',hF,'LR',hL,'GAP',hF-hL,'DISTANCE_LINF_LOWER',F(3,6608))
# Non-binary aggregation when all three kernels coincide.
u=(F(2,5),)*3
v=(F(1,7),F(2,7),F(3,7),F(4,7),F(5,7),F(6,7))
for shift in range(72):
 p=[v[(shift+3*i+i*i)%6] for i in range(7)]
 x,jb,ji,kc,ki,kbj,kij=p
 y=(jb+(1-x)*ji)/(2-x)
 w=(F(1,4),(1-x)/4,(1-jb)/8,(1-x)*(1-ji)/8)
 z=sum((m*k for m,k in zip(w,(kc,ki,kbj,kij))),F(0))/sum(w,F(0))
 assert obs(u,p)[0]==obs(u,lr(x,y,z))[0];checks+=1
print('PASS_EXACT_R5_COMMON_RAY_FIBER',checks,'exact assertions')
