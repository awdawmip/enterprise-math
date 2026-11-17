from fractions import Fraction as F
from itertools import product
z,o=F(0),F(1)
H=(F(5),z,F(5),F(-8)); J=(F(-3),z,F(-1),z)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def obs(v,t):
 p1,p2,q1,q2,qb,r,k1,k2,l1,l2,lb=v
 assert z<t<F(5,6)
 y=[z,z,z,z]; mass=[z,z]
 def put(a,b,s,time):
  assert a>=0 and b>=0
  mass[0]+=a;mass[1]+=b
  y[0 if s=='P' else 1]+=a if s=='P' else b
  y[2]+=a*time;y[3]+=b*time
 for p,q,k,l in ((p1,q1,k1,l1),(p2,q2,k2,l2)):
  a=b=F(1,8);put(a*p,b*p,'P',1);a*=1-p;b*=1-p
  put(a/2,3*b/4,'Q',2);a/=2;b/=4
  put(a*q,b*q,'P',2);a*=1-q;b*=1-q
  put(3*a/5,b/2,'Q',3);a*=F(2,5);b/=2
  put(a/2,b/2,'P',3);a/=2;b/=2
  put(a*k,b*k,'P',3);a*=1-k;b*=1-k
  put(a/4,b/2,'Q',4);a*=F(3,4);b/=2
  put(a*l,b*l,'P',4);put(a*(1-l),b*(1-l),'Q',5)
 a,b=F(1,4),F(1,8);put(a*qb,b*qb,'P',2);a*=1-qb;b*=1-qb
 put(a*(1-F(6,5)*t),b*(1-t),'P',4)
 a*=F(6,5)*t;b*=t
 put(a*lb,b*lb,'P',4);put(a*(1-lb),b*(1-lb),'Q',5)
 put(F(1,2)*r,F(5,8)*r,'Q',1)
 put(F(1,2)*(1-r),F(5,8)*(1-r),'P',3)
 assert mass==[o,o]
 return tuple(y)
def lr(p,q,r,k,l,t):return obs((p,p,q,q,q,r,k,k,l,l,l),t)
def delta(a,b):return tuple(x-y for x,y in zip(a,b))
def det(M):
 if len(M)==1:return M[0][0]
 return sum((-1)**i*x*det([r[:i]+r[i+1:] for r in M[1:]]) for i,x in enumerate(M[0]))
def verify(t):
 full=[(obs(v,t),v) for v in product((z,o),repeat=11)]
 restr=[(lr(*v,t),v) for v in product((z,o),repeat=5)]
 a=lambda l:-F(3,8)+l/4
 def forms(v):
  p1,p2,q1,q2,qb,r,k1,k2,l1,l2,lb=v
  h=-F(33,8)+F(5,2)*r-qb/4+(1-qb)*(F(1,4)-t+t*lb)
  c=r/2+3*(1-r)+F(5,4)*qb+(1-qb)*(F(7,4)-F(3,5)*t*(1-lb))
  for p,q,k,l in ((p1,q1,k1,l1),(p2,q2,k2,l2)):
   h+=13*p/16-p*q/8+q/8+a(l)*(1-p)*(1-q)*(1-k)/8
   c+=p/2+(1-p)*(F(1,8)+5*q/16+(1-q)*(F(3,16)+3*k/40+(1-k)*(F(19,320)+3*l/160)))
  return h,c
 for x,v in full:
  h,c=forms(v);assert dot(H,x)==h and -dot(J,x)==c
 for x,(p,q,r,k,l) in restr:
  h,c=forms((p,p,q,q,q,r,k,k,l,l,l));assert dot(H,x)==h and -dot(J,x)==c
 fH=-F(143,32)+min(z,F(1,2)-t); lH=min(-F(33,8),-F(127,32)-t)
 fC=F(399,160);lC=min(F(21,8),F(479,160)-3*t/5)
 assert min(dot(H,x) for x,_ in full)==fH
 assert min(dot(H,x) for x,_ in restr)==lH
 assert min(-dot(J,x) for x,_ in full)==fC
 assert min(-dot(J,x) for x,_ in restr)==lC
 assert lH>=fH and lC>fC
 X=lr(z,z,z,o,o,t); B=delta(lr(o,z,z,o,o,t),X)
 C=delta(lr(z,o,z,o,o,t),X)
 V=lr(o,o,z,o,o,t);D=tuple(V[i]-X[i]-B[i]-C[i] for i in range(4))
 E=delta(lr(z,z,o,o,o,t),X)
 assert det((B,C,D,E))==F(59,10240)
 print(f'eta={t}: H_FULL={fH} H_LR={lH} H_gap={lH-fH}; C_FULL={fC} C_LR={lC} J_gap={lC-fC}; rank_det=59/10240')
 if t==F(1,2):
  v=(z,z,z,z,o,o,z,z,z,z,o);w=obs(v,t)
  assert w==(F(11,40),F(55,64),F(267,160),F(187,128))
  print('eta=1/2 FULL witness:',w,'J gap',lC-fC,'Linf distance lower',(lC-fC)/4)
for eta in (F(1,8),F(1,3),F(1,2),F(2,3),F(4,5)):verify(eta)
print('PASS_EXACT_R5_BYPASS_L_ONE_PARAMETER_PHASE_AND_PERSISTENT_J_GAP (10400 deterministic observations)')
