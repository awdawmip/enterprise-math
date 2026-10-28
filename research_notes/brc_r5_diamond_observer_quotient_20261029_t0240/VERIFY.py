"""Exact-rational checks of R5 observable diamond (proof is in RESEARCH.md)."""
from fractions import Fraction as Q
from random import Random
S=(Q(1,2),Q(1),Q(3,2),Q(5,2))
a=Q(1,4)
mu=((Q(7,50),Q(11,75),Q(1,2),Q(16,75)),
    (Q(17,200),Q(23,150),Q(3,5),Q(97,600)))
nu=(((Q(1,2),Q(1,6),Q(1,4),Q(1,12)),(Q(17,100),Q(23,75),Q(1,5),Q(97,300))),
    ((Q(5,12),Q(1,3),Q(1,6),Q(1,12)),(Q(31,120),Q(5,18),Q(1,15),Q(143,360))))
eta=(Q(1,8),Q(1,4),Q(3,8),Q(1,4))
CL=Q(7,450);CR=Q(7,200)
for i in (0,1):
 assert sum(mu[i])==1 and sum(x*y for x,y in zip(S,mu[i]))==Q(3,2)
 for j,r in enumerate((Q(1),Q(3,2))):
  assert sum(nu[i][j])==1 and sum(x*y for x,y in zip(S,nu[i][j]))==r
assert sum(eta)==1 and sum(x*y for x,y in zip(S,eta))==Q(3,2)
assert CL==sum(a*mu[i][1]*nu[i][0][2] for i in (0,1))
assert CR==sum(a*mu[i][2]*nu[i][1][2] for i in (0,1))

def W(U,L,R,M):
 assert 0<=L<=U<=1 and 0<=R<=U and 0<=M<=CL*L+CR*R
 w={}
 def add(t,s,x): w[(t,s)]=w.get((t,s),Q(0))+x
 add(1,S[0],Q(1,2));add(1,S[2],(1-U)/2)
 for i in (0,1):
  for j in (0,3):add(2,S[j],a*U*mu[i][j])
  add(2,S[1],a*mu[i][1]*(U-L));add(2,S[2],a*mu[i][2]*(U-R))
  for b,k in ((0,L),(1,R)):
   for j in (0,1,3):add(3,S[j],a*k*mu[i][b+1]*nu[i][b][j])
 add(3,S[2],CL*L+CR*R-M)
 for j in range(4):add(4,S[j],M*eta[j])
 assert len(w)==14 and all(x>=0 for x in w.values())
 assert sum(w.values())==1 and sum(s*x for (t,s),x in w.items())==1
 return w

def flow(root,left,right,gamma):
 U=root;L=U*left;R=U*right;return (U,L,R,gamma*(CL*L+CR*R))

def recover(f):
 U,L,R,M=f;h=CL*L+CR*R
 return (U,L/U if U else Q(0),R/U if U else Q(0),M/h if h else Q(0))

def O(w,theta):
 m={cell:theta.get(cell,Q(0))*x for cell,x in w.items()}
 return (1-sum(s*x for (t,s),x in m.items()),sum(m.values()),
         sum(t*s*x for (t,s),x in w.items()),sum(t*x for (t,s),x in w.items()))

def add(x,y,p):return tuple((1-p)*a+p*b for a,b in zip(x,y))

def support(c,w):
 a,b,d,e=c
 return a+sum(x*(t*(d*s+e)+max(Q(0),b-a*s)) for (t,s),x in w.items())

vertices=((Q(0),)*4,(Q(1),Q(0),Q(0),Q(0)),
 (Q(1),Q(1),Q(0),Q(0)),(Q(1),Q(1),Q(0),CL),
 (Q(1),Q(0),Q(1),Q(0)),(Q(1),Q(0),Q(1),CR),
 (Q(1),Q(1),Q(1),Q(0)),(Q(1),Q(1),Q(1),CL+CR))

v=(Q(11,1200),Q(23,3600));z=(Q(1,40),Q(1,100))
assert v[0]*z[1]-v[1]*z[0]==-Q(49,720000)
x=((v[0]+z[0])/2,(v[1]+z[1])/2);y=(v[0]/2,v[1]/2)
assert y[0]*x[1]-y[1]*x[0]==-Q(49,2880000)
f1=flow(Q(1),Q(1),Q(0),Q(1));f2=flow(Q(1),Q(0),Q(1),Q(0));fm=add(f1,f2,Q(1,2))
assert recover(fm)==(Q(1),Q(1,2),Q(1,2),Q(4,13))
w1=W(*f1);w2=W(*f2);wm=W(*fm)
assert all(wm[k]==(w1[k]+w2[k])/2 for k in wm)
def theta(cell):return Q(cell[0]+S.index(cell[1])+1,12)
T={k:theta(k) for k in wm}
o1,o2,om=O(w1,T),O(w2,T),O(wm,T)
assert om==add(o1,o2,Q(1,2))
assert om==(Q(42139,69120),Q(16963,57600),Q(4813,2400),Q(3029,1800))
print('exact CL,CR:',CL,CR)
print('source-resolved wedge:',-Q(49,2880000),'but 4-observer midpoint implemented by',recover(fm))
print('O1:',o1);print('O2:',o2);print('Omid:',om)

rng=Random(202610290240)
for _ in range(1600):
 p=[Q(rng.randrange(17),16) for _ in range(4)]
 q=[Q(rng.randrange(17),16) for _ in range(4)]
 lam=Q(rng.randrange(17),16)
 f,g=flow(*p),flow(*q);wf,wg=W(*f),W(*g)
 h=add(f,g,lam);wh=W(*h)
 assert W(*flow(*recover(h)))==wh
 assert all(wh[k]==(1-lam)*wf[k]+lam*wg[k] for k in wh)
 tf={k:Q(rng.randrange(17),16) for k in wf}
 tg={k:Q(rng.randrange(17),16) for k in wg}
 m={k:(1-lam)*wf[k]*tf[k]+lam*wg[k]*tg[k] for k in wh}
 th={k:m[k]/wh[k] if wh[k] else Q(0) for k in wh}
 assert O(wh,th)==add(O(wf,tf),O(wg,tg),lam)
for _ in range(800):
 c=tuple(Q(rng.randrange(-10,11)) for _ in range(4))
 bound=max(support(c,W(*vtx)) for vtx in vertices)
 for j in range(5):
  p=[Q(rng.randrange(13),12) for _ in range(4)]
  w=W(*flow(*p));t={k:Q(rng.randrange(13),12) for k in w}
  assert sum(ci*oi for ci,oi in zip(c,O(w,t)))<=bound
print('1600 exact-rational behavior mixtures; 800 signed support directions; 4000 policies: PASS')
print('PASS_EXACT_R5_DIAMOND_OBSERVER_QUOTIENT')
