from fractions import Fraction as F
from itertools import product
alpha=(F(1,2), F(2,3), F(1,2), F(3,4))
VF=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
VL=((0,0,0),(0,1,1),(1,0,0),(1,1,0))
stages=((0,0,0),(1,0,0),(1,1,0),(1,1,1))
cstar=(F(1,8),F(1,6),F(1,16),F(3,32))
checks=0
def check(a,b):
 global checks
 checks+=1
 assert a==b,(a,b)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def obs(t,x,y,i,rows):
 x,y,i=map(F,(x,y,i));d=y/16+3*i/32
 w=(F(1,4),(1-x)/4,y/8,i/8)
 M=[w[s]*alpha[s]*rows[s][0] for s in range(4)]
 S=[F(2,3)*M[s]*rows[s][1] for s in range(4)]
 U=[S[s]*rows[s][2] for s in range(4)]
 return (F(107,128)-21*x/128+d/4-sum(S)/2+sum((t['p'][s]*S[s]/8 for s in range(4)),F(0)),
         F(13,64)+3*x/64-d/2+sum(S)/8+sum((t['q'][s]*S[s]/32 for s in range(4)),F(0)),
         3+sum(M)+F(3,2)*sum(S)+sum((t['r'][s]*U[s] for s in range(4)),F(0)),
         3+sum(M)/2+F(3,8)*sum(S)+sum((t['v'][s]*U[s]/4 for s in range(4)),F(0)))
def brute(t,n,full):
 ans=None
 for x,y,i in (VF if full else VL):
  js=product(range(4),repeat=4) if full else ((j,)*4 for j in range(4))
  for j in js:
   val=dot(n,obs(t,x,y,i,tuple(stages[k] for k in j)))
   ans=val if ans is None else max(ans,val)
 return ans

def normals(tau,r,v):
 eta=F(3,2)+2*r-v
 s=eta if 2*r>=v else F(3,2)
 def n(A,B,h):
  D=-4*h/s
  return (F(A),F(B),-D/2,D)
 return n(8,0,4-tau),n(0,-32,4+tau)
def predicted(vec,tau):
 return F(2,3)*min(sum((c*max(z-tau,0) for c,z in zip(cstar,vec)),F(0)),
                     sum((c*max(tau-z,0) for c,z in zip(cstar,vec)),F(0)))

def check_kernel(t,tau):
 nP,nQ=normals(tau,t['r'][0],t['v'][0]);
 for n,vec in ((nP,t['p']),(nQ,t['q'])):
  f=brute(t,n,True);lr=brute(t,n,False)
  check(f-lr,predicted(vec,tau))
 return nP,nQ

spread=(F(1,4),F(1,2),F(3,4),F(1,2)); reverse=tuple(reversed(spread))
base=dict(p=spread,q=(F(3,4),F(1,2),F(1,4),F(1,2)),r=(F(3,4),)*4,v=(F(3,4),)*4)
for r,v in ((F(3,4),F(3,4)),(F(1,5),F(4,5)),(F(2,5),F(4,5)),(F(7,8),F(1,4))):
 for p,q in ((spread,base['q']),((F(1,3),)*4,spread),(reverse,(F(2,3),)*4)):
  t=dict(p=p,q=q,r=(r,)*4,v=(v,)*4)
  for tau in (F(1,4), F(2,5), F(1,2),F(3,5),F(3,4)):
   check_kernel(t,tau)
# Real-behaviour pooling in the source-uniform p,q,r,v subfamily.
for r,v in ((F(3,4),F(3,4)),(F(1,5),F(4,5)),(F(7,8),F(1,4))):
 t=dict(p=(F(2,5),)*4,q=(F(3,7),)*4,r=(r,)*4,v=(v,)*4)
 for x,y,i in ((F(0),F(1),F(1)),(F(1,5),F(2,3),F(1,2)),(F(2,3),F(3,8),F(1,6))):
  rows=((F(1,3),F(1,2),F(1,4)),(F(2,3),F(3,5),F(1,2)),
        (F(4,5),F(1,7),F(3,4)),(F(3,7),F(5,6),F(2,3)))
  w=(F(1,4),(1-x)/4,y/8,i/8)
  M=sum((w[s]*alpha[s]*rows[s][0] for s in range(4)),F(0))
  S=sum((F(2,3)*w[s]*alpha[s]*rows[s][0]*rows[s][1] for s in range(4)),F(0))
  U=sum((F(2,3)*w[s]*alpha[s]*rows[s][0]*rows[s][1]*rows[s][2] for s in range(4)),F(0))
  d=y/16+3*i/32;yp=32*d/(5-3*x);ip=(1-x)*yp
  T=F(1,8)+(1-x)/6+d
  zp=M/T;tp=3*S/(2*M) if M else F(0);up=U/S if S else F(0)
  check(all(0<=a<=1 for a in (yp,ip,zp,tp,up)),True)
  check(obs(t,x,y,i,rows),obs(t,x,yp,ip,((zp,tp,up),)*4))
nP,nQ=normals(F(1,2),F(3,4),F(3,4)); W=obs(base,0,1,1,(stages[1],stages[1],stages[3],stages[1]))
check(dot(nP,W),brute(base,nP,True));check(dot(nQ,W),brute(base,nQ,True))
check(brute(base,nP,True)-brute(base,nP,False),F(1,96))
check(brute(base,nQ,True)-brute(base,nQ,False),F(1,96))
print('normals',nP,nQ)
print('witness',W)
print('supports P',brute(base,nP,True),brute(base,nP,False))
print('supports Q',brute(base,nQ,True),brute(base,nQ,False))
print('gaps',F(1,96),F(1,96))
print('distance_inf_lower_bounds',F(1,96)/sum(map(abs,nP)), F(1,96)/sum(map(abs,nQ)))
print('kernels',12,'thresholds',5,'pooling_examples',9,'assertions',checks)
print('PASS_EXACT_R5_K3_COMMON_LABEL_UNIFORM_CLOCK_RIGIDITY')
