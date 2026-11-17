"""R5 two-law 16-parameter classification: exact, reproducible corner checks."""
from fractions import Fraction as F
from itertools import product
c=F(2,3)
alpha=(F(1,2),F(2,3),F(1,2),F(3,4))
checks=0

def ck(cond,msg):
 global checks
 checks+=1
 if not cond: raise AssertionError(msg)

def obs(x,y,j,z,t,a,b,p,q):
 x,y,j=map(F,(x,y,j));z=tuple(map(F,z));t=tuple(map(F,t))
 i=(1-x)*j; w=(F(1,4),(1-x)/4,y/8,i/8)
 Q=[w[s]*alpha[s]*z[s] for s in range(4)]
 S=[c*Q[s]*t[s] for s in range(4)];d=y/16+3*i/32
 return (F(107,128)-21*x/128+d/4-sum(p[s]*S[s] for s in range(4)),
         F(13,64)+3*x/64-d/2+sum(q[s]*S[s] for s in range(4))/4,
         3+sum(Q)+sum((1+a[s])*S[s] for s in range(4)),
         3+sum(Q)/2+sum((1+b[s])*S[s] for s in range(4))/4)

def dot(n,v): return sum(n[k]*v[k] for k in range(4))

def bell(n,a,b,p,q):
 n0,n1,n2,n3=n;h=n2+n3/2;hx=-21*n0/128+3*n1/64;hd=n0/4-n1/2
 L=[max(F(0),h+c*max(F(0),-n0*p[s]+n1*q[s]/4+n2*(1+a[s])+n3*(1+b[s])/4)) for s in range(4)]
 return (107*n0/128+13*n1/64+3*(n2+n3)+L[0]/8+
         max(F(0),(hd+L[2])/16)+max(hx,L[1]/6+max(F(0),3*(hd+L[3])/32)))

half=(F(1,2),)*4
edge=(F(1,1000),F(999,1000),F(1,999),F(998,999))
# (label, rho, a=(C,I,BJ,IJ), P-coins, Q-coins, branch, delta)
cases=(
 ('other_fixed',F(1),(F(3,4),F(1,4),F(1,2),F(1,4)),half,half,'other',F(1,1000)),
 ('other_mixed',F(1),(F(3,4),F(1,4),F(1,2),F(1,4)),(F(1,4),F(1,2),F(3,4),F(1,3)),(F(1,3),F(3,4),F(1,2),F(1,4)),'other',None),
 ('other_edge',F(1),(F(3,4),F(1,4),F(1,2),F(1,4)),edge,edge[::-1],'other',None),
 ('other_rho_low',F(4,5),(F(3,4),F(3,8),F(1,2),F(3,8)),half,edge,'other',None),
 ('other_rho_high',F(6,5),(F(3,5),F(1,8),F(2,5),F(1,8)),edge,half,'other',None),
 ('other_tie',F(1),(F(1,2),F(1,4),F(1,2),F(1,4)),half,edge,'other',None),
 ('other_spread',F(1),(F(9,10),F(1,16),F(3,4),F(1,16)),edge,half,'other',None),
 ('ridge_fixed',F(1),(F(3,4),F(1,4),F(1,4),F(1,4)),half,half,'ridge',F(1,1000)),
 ('ridge_rho_low',F(4,5),(F(3,4),F(3,8),F(3,8),F(3,8)),edge,edge[::-1],'ridge',None),
 ('ridge_rho_high',F(6,5),(F(3,5),F(1,8),F(1,8),F(1,8)),edge[::-1],edge,'ridge',None),
)
for name,rho,a,p,q,kind,special in cases:
 b=tuple(rho*(1+u)-1 for u in a)
 ck(all(0<u<1 for u in a+b+p+q),name+' positive')
 if kind=='other':
  ck(0<a[1]==a[3]<a[2]<=a[0]<1,name+' order')
  tau=(a[1]+a[2])/2
  g=min(c*(a[2]-tau)/16,F(25,96)*c*(tau-a[1]))
  vx,vy=1,1; wz=(1,0,1,0); wdiff=(F(3,16),-F(3,32),F(0),F(0)); coef=F(3,16)
 else:
  ck(0<a[1]==a[2]==a[3]<a[0]<1,name+' ridge')
  tau=(a[0]+a[1])/2
  g=min(c*(a[0]-tau)/8,c*(tau-a[1])/16)
  vx,vy=1,0; wz=(1,0,0,0); wdiff=(F(13,64),-F(1,8),F(0),F(0));coef=F(13,64)
 n3=(-c*(1+tau)-1)/(F(1,2)-rho/4);n2=1-rho*n3/4
 delta=special or g/4;ck(0<delta<g,name+' tilt')
 n=(delta,F(0),n2,n3);nt=(F(0),F(0),n2,n3)
 ck(n2+n3/2==-c*(1+tau) and n2+rho*n3/4==1,name+' normal')
 V=obs(vx,vy,vy,(1,)*4,(1,)*4,a,b,p,q)
 W=obs(0,1,1,wz,wz,a,b,p,q)
 ck(tuple(W[k]-V[k] for k in range(4))==wdiff,name+' fiber')
 losses=[]
 for x,y,j in product((0,1),repeat=3):
  for bits in product((0,1),repeat=8):
   ck(dot(n,obs(x,y,j,bits[:4],bits[4:],a,b,p,q))<=dot(n,W),name+' FULL')
 for x,y,z,t in product((0,1),repeat=4):
  v=obs(x,y,y,(z,)*4,(t,)*4,a,b,p,q)
  ck(dot(n,v)<=dot(n,V),name+' LR')
  if (x,y,z,t)!=(vx,vy,1,1): losses.append(dot(nt,V)-dot(nt,v))
 ck(min(losses)==g,name+' exact margin')
 ck(bell(n,a,b,p,q)==dot(n,W),name+' Bellman')
 ck(dot(n,W)-dot(n,V)==coef*delta,name+' gap')
 print('CASE',name,'rho',rho,'tau',tau,'margin',g,'delta',delta,
       'gap',coef*delta,'Linf_lower',(coef*delta)/sum(map(abs,n)))
 if name in ('other_fixed','ridge_fixed'):
  print('FULL_W',*(str(v) for v in W))
  print('LR_V',*(str(v) for v in V))

# Exact affine clock change for source-uniform a,b, including nonbinary controls.
for a0,b0 in ((F(1,4),F(1,2)),(F(3,4),F(1,8)),(F(1,2),F(1,2))):
 ck((b0-1-2*a0)/4!=0,'clock determinant')
 for x,y,j in ((0,0,0),(1,1,0),(0,1,1),(F(1,3),F(2,5),F(4,7))):
  z=(F(1,5),F(1,2),F(3,4),F(4,5));t=(F(1,6),F(2,5),F(1,3),F(5,6))
  v=obs(x,y,j,z,t,(F(0),)*4,(F(0),)*4,half,half)
  R1=4*(v[3]-3)-(v[2]-3);R2=2*(v[2]-3)-4*(v[3]-3)
  w=obs(x,y,j,z,t,(a0,)*4,(b0,)*4,half,half)
  ck((v[0],v[1],3+R1+(1+a0)*R2,3+R1/2+(1+b0)*R2/4)==w,'affine clock')
print('PASS_EXACT_R5_16_PARAMETER_CLASSIFICATION')
print('EXACT_ASSERTIONS',checks,'FULL_CORNERS',len(cases)*2048,'LR_CORNERS',len(cases)*16,'CASES',len(cases))
