# Exact continuation of PREFIX1054 subband, preserving the signed recurrence.
import PREFIX1054_R6_MIDDLE_SUBBAND_CHECK as parent
from fractions import Fraction as F
from math import prod,lcm,ceil,factorial
import sympy as s
Y,t,n,z=parent.Y,parent.t,parent.n,parent.z
a=parent.a; pe=parent.pe; fall=parent.fall; add=parent.add;mul=parent.mul;sc=parent.sc;bern=parent.bern
Dcut=200

def rec(y,r,N,critical=False):
 A=[s.Poly(x.subs(Y,y+t),t) for x in a];m=4 if critical else 5;wlen=8 if critical else 9
 w=[s.Poly(s.expand(sum(A[d].nth(k-m+d)*fall(n-k,d) for d in range(6) if k-m+d>=0)*r**k),n) for k in range(wlen)]
 lim=[-s.LC(x)/s.LC(w[0]) if not x.is_zero else 0 for x in w[1:]]
 if critical:
  P=(1+F(r,4)*z)**5*(1-F(r,12)*z)*(1-F(r,32)*z)
  K=1/((1-r/4)**5*(1-r/12)*(1-r/32))
 else:
  P=a[5].subs(Y,y+r*z)/a[5].subs(Y,y)
  K=1/prod((1-r/abs(y-root))**m for root,m in [(0,5),(4,1),(16,1),(36,1)])
 assert s.expand(1-sum(lim[k-1]*z**k for k in range(1,wlen))-P)==0
 D=s.Poly(w[0].as_expr().subs(n,n+N),n);sg=s.sign(D.LC());D=D.mul_ground(sg);assert all(D.nth(i)>0 for i in range(6))
 e=F(sum(max(abs(d.nth(i))/D.nth(i) for i in range(6)) for d in [s.Poly((-w[k].as_expr()-lim[k-1]*w[0].as_expr()).subs(n,n+N),n).mul_ground(sg) for k in range(1,wlen)]))
 assert K*e<1
 d=lcm(*(int(c.q) for p in w for c in p.all_coeffs()));p=[[int(x.nth(i)*d) for i in range(6)] for x in w]
 return p,K,F(sum(abs(x) for x in lim))+e,e

def calc(y,r,N,r0,N0,ell,sgn,critical=False,old=False):
 m=4 if critical or old else 5
 if old:
  p,K,L,e=parent.p,parent.K,parent.L,parent.e;p0,K0,L0,e0=parent.p0,parent.K0,parent.L0,parent.e0
  M=parent.M;delta=parent.delta
 else:
  p,K,L,e=rec(y,r,N,critical);p0,K0,L0,e0=rec(y,r0,N0,critical);M=10**5000;delta=F(1,10**80)
 q=ell/r;assert 0<q<1 and N>Dcut
 E=[0]*m
 for i in range(m,N0):
  d=abs(pe(p0[0],i));E.append(1+(sum(abs(pe(p0[k],i))*E[i-k] for k in range(1,min(len(p0)-1,i)+1))+d-1)//d)
 E0=max(max(E),ceil(K0*(L0*max(E[-(len(p0)-1):])+1)/(1-K0*e0)))
 assert F(E0,M)*(r/r0)**N<delta
 R=[[pe(pk,i) for pk in p] for i in range(m,N)]
 out=[]
 for j in range(m):
  assert (M*r**j).denominator==1
  c=[int(i==j)*int(r**i*M) for i in range(m)]
  for i,row in enumerate(R,m):c.append(-sum(row[k]*c[i-k] for k in range(1,min(len(row)-1,i)+1))//row[0])
  B=F(max(abs(x) for x in c[-(len(p)-1):]),M)+delta
  T=max(K*L*B/(1-K*e),F(max(abs(x) for x in c[Dcut+1:]),M)+delta)
  W=10**50;eta=delta+F(1,W);u=[F(x*W//M,W)*(sgn*q)**i for i,x in enumerate(c[:Dcut+1])]
  jets=[sum(u[i]*fall(i,k)*(F(sgn)/ell)**k for i in range(k,len(u))) for k in range(5)]
  er=[]
  for k in range(5):
   ratio=q*F(Dcut+2,Dcut+1)**k;assert ratio<1
   er.append((eta*(Dcut+1)**(k+1)+T*q**(Dcut+1)*(Dcut+1)**k/(1-ratio))/ell**k)
  integ=mul([y-6,sgn*ell],u);v=[F(0)]+[sgn*ell*x/(i+1) for i,x in enumerate(integ)]
  vi=sum(v);ve=ell*(abs(y-6)+ell)*er[0]
  H=parent.polylist(s.Poly((Y**2*(36-Y)**2).subs(Y,y+sgn*ell*t),t))
  Hp=parent.polylist(s.Poly(s.diff(Y**2*(36-Y)**2,Y).subs(Y,y+sgn*ell*t),t))
  P=parent.polylist(s.Poly((Y*(Y-36)*(17*Y-91)).subs(Y,y+sgn*ell*t),t))
  df=[F(sgn*i)/ell*u[i] for i in range(1,len(u))]
  b=add(sc(mul(Hp,u),4),sc(mul(H,df),4),sc(mul(P,u),-2),sc(mul([11+y,sgn*ell],v),12))
  be=4*(4*36**3*er[0]+36**4*er[1])+2*36**2*(17*36+91)*er[0]+12*47*ve
  out.append((jets+[vi],er+[ve],b,be))
 return out

def rnd(x,e):
 W=10**30;v=F(x*W//1,W);return v,F(ceil((e+abs(x-v))*W),W)
def combine(out,Q,qe,v0,ve):
 state=[];se=[]
 for k in range(6):
  x=sum(q*o[0][k] for q,o in zip(Q,out))+(v0 if k==5 else 0)
  e=sum(abs(q)*o[1][k]+d*(abs(o[0][k])+o[1][k]) for q,d,o in zip(Q,qe,out))+(ve if k==5 else 0)
  v,er=rnd(x,e);state.append(v);se.append(er)
 return state,se

def certify(out,Q,qe,v0,ve,y,ell,sgn):
 b=add(*[sc(o[2],q) for o,q in zip(out,Q)],[12*(11+y)*v0,12*sgn*ell*v0]);lo,hi=bern(b)
 err=sum(abs(q)*o[3]+d*(max(abs(x) for x in bern(o[2]))+o[3]) for q,d,o in zip(Q,qe,out))+12*47*ve
 print('band',float(y),float(y+sgn*ell),'lower',float(lo-err),'error',float(err),flush=True)
 return lo-err

# Evaluate all five real jets and primitive at 7.5 with separate basis uncertainty.
out=calc(F(16),F(9),30000,F(5),300,F(17,2),-1,old=True)
state,se=combine(out,parent.Q,[parent.qe]*4,parent.v0,parent.qe)
print('state7.5',list(map(float,state)),'errors',list(map(float,se)),flush=True)
low=[]
for y,r,N,r0,N0,ell in [(F(15,2),F(21,8),3000,F(7,8),100,F(7,4)),(F(23,4),F(21,16),300,F(7,16),100,F(7,8))]:
 out=calc(y,r,N,r0,N0,ell,-1)
 Q=[state[j]/factorial(j) for j in range(5)];qe=[se[j]/factorial(j) for j in range(5)]
 low.append(certify(out,Q,qe,state[5],se[5],y,ell,-1))
 state,se=combine(out,Q,qe,state[5],se[5]);print('state',float(y-ell),list(map(float,state)),'errors',list(map(float,se)),flush=True)
# Analytic basis at 4. Match four derivatives; existence inherited from PREFIX1052.
y=F(4);ell=F(7,8)
out=calc(y,F(3,2),300,F(3,2),300,ell,1,critical=True)
A=s.Matrix([[o[0][k] for o in out] for k in range(4)]);Ai=A.inv();Q=list(map(F,Ai*s.Matrix(state[:4])))
# componentwise residual and matrix perturbation via absolute inverse.
Ai=[[abs(F(Ai[i,j])) for j in range(4)] for i in range(4)]
D=[[o[1][k] for o in out] for k in range(4)]
K=max(sum(Ai[i][k]*sum(D[k]) for k in range(4)) for i in range(4));assert K<1
b=[se[k]+sum(D[k][j]*abs(Q[j]) for j in range(4)) for k in range(4)]
qe0=[sum(Ai[i][k]*b[k] for k in range(4)) for i in range(4)];tail=K*max(qe0)/(1-K)
qe=[e+tail for e in qe0]
Q,qe=map(list,zip(*(rnd(x,e) for x,e in zip(Q,qe))))
v0=state[5]-sum(q*o[0][5] for q,o in zip(Q,out));ve=se[5]+sum(abs(q)*o[1][5]+d*(abs(o[0][5])+o[1][5]) for q,d,o in zip(Q,qe,out));v0,ve=rnd(v0,ve)
print('local4 Q',list(map(float,Q)),'errors',list(map(float,qe)),'v',float(v0),'err',float(ve),flush=True)
box4=[(int((x-e)*100//1),ceil((x+e)*100)) for x,e in zip(Q+[v0],qe+[ve])]
print('local4 exact hundredth box',box4,flush=True)
low.append(certify(out,Q,qe,v0,ve,y,ell,1))
print('new bands minimum',float(min(low)),flush=True)
assert all(x>b for x,b in zip(low,[18466000,17052000,15387000]))
print('PREFIX1054_MIDDLE_COMPLETION_CERTIFICATE_PASSED',flush=True)
