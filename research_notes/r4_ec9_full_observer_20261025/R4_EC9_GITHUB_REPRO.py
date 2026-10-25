# R4-EC9 compact exact reproduction (SymPy; positive BRC, not native X6).
import sympy as s
from collections import defaultdict
x,z=s.symbols('x z',nonzero=True)
S=z+1/z
D=(1+x*x)*(1-x*S+2*x**4-x**6)
Q=(1-x*S)*(1+x*x-x**3*S)
P=s.expand(D*Q)
a=1-x/z;b=1-x*(1+x*x)*z
U={1:a*b/D,-1:x**4*z*z*a/D}
W={1:(a*b-D)/(x*x*D),-1:x*x*z*z*a/D}
V={e:x*z**e*W[e] for e in (1,-1)}
Y={1:x**5*z*a/D,-1:x*z*a*b/D}
for e in (1,-1):
 assert s.cancel(U[e]-(int(e==1)+x*z**(-e)*V[e]))==0
 assert s.cancel(V[e]-x*z**e*W[e])==0
 assert s.cancel(W[e]-x*z**(-e)*(U[e]+W[e]+Y[e]))==0
 assert s.cancel(Y[e]-x*z**(-e)*U[-e])==0
ix=[(q,e) for q in range(3) for e in (1,-1)]
id={k:i for i,k in enumerate(ix)}
M=s.zeros(6);f=s.zeros(6,1)
for e in (1,-1):
 i=id[0,e];M[i,id[1,e]]=x*z**(-e);M[i,id[1,-e]]=x*z**(-e);f[i]=x*z**(-e)*V[-e]
 i=id[1,e];M[i,id[2,e]]=x*z**e;f[i]=x*z**e*Y[e]
 i=id[2,e];M[i,id[0,e]]=x*z**(-e);M[i,id[0,-e]]=x*z**(-e);M[i,id[2,e]]=x*z**(-e)
assert s.cancel((s.eye(6)-M).det()-Q)==0
h=(s.eye(6)-M).inv(method='DM')*f
F={(q,1,e):h[id[q,e]] for q,e in ix}
F.update({(0,0,e):U[e] for e in (1,-1)})
F.update({(1,0,e):V[e] for e in (1,-1)})
F.update({(2,0,e):W[e]+Y[e] for e in (1,-1)})
assert len(F)==12
for v in F.values():
 n=s.cancel(P*v); num,den=s.fraction(n)
 assert not den.has(x) and s.degree(num,x)<=12
w=x**4*z-x**3*z**4-2*x**3*z**2+x**2*z**3-x**2*z-x+2*z**3+z
nstar=x**4*(x*z-1)**2*w/z**3
assert s.cancel(P*F[2,1,1]-nstar)==0
u=s.Poly(s.expand(8*P.subs(z,2)),x,domain=s.ZZ)
v=s.Poly(s.expand(8*nstar.subs(z,2)),x,domain=s.ZZ)
assert (u.degree(),v.degree())==(12,10)
assert s.gcd(s.Poly(u.as_expr(),x,modulus=101),s.Poly(v.as_expr(),x,modulus=101)).degree()==0

def terms(q):
 out=defaultdict(int)
 for term in s.expand(q).as_ordered_terms():
  p=term.as_powers_dict();i=int(p.get(x,0));j=int(p.get(z,0))
  c=s.simplify(term/(x**i*z**j)); assert c.is_integer
  out[i,j]+=int(c)
 return {k:v for k,v in out.items() if v}
coeff=terms(P)
N={k:terms(s.cancel(P*v)) for k,v in F.items()}
state={(0,0,1,0):1};history=[]; checks=0
for n in range(81):
 assert sum(state.values())==1<<n
 obs=defaultdict(int)
 for (q,r,e,t),cnt in state.items():obs[q,int(r==2),e,t]+=cnt
 history.append(obs)
 for (q,dirty,e),numerator in N.items():
  lhs=defaultdict(int)
  for (j,shift),value in coeff.items():
   if j>n:continue
   for (qq,dd,ee,t),cnt in history[n-j].items():
    if (qq,dd,ee)==(q,dirty,e):lhs[t+shift]+=value*cnt
  ts=set(lhs)|{t for (m,t) in numerator if m==n}
  for t in ts:assert lhs[t]==numerator.get((n,t),0);checks+=1
 if n==80:break
 nxt=defaultdict(int)
 for (q,r,e,t),cnt in state.items():
  for bit in (0,1):
   nq,eta,b=(((2,-1,-1),(2,1,-1)) if q==0 else ((0,-1,-1),(0,1,-1)) if q==1 else ((1,1,1),(2,1,-1)))[bit]
   nr=2 if r==2 else (0 if bit else 1 if r==0 else 2)
   nxt[nq,nr,e*eta,t+e*eta*b]+=cnt
 state=nxt
assert history[10][2,0,1,0]==5 and history[10][2,1,1,0]==49
assert history[20][2,0,1,0]==463 and history[20][2,1,1,0]==43307
print('PASS 12 channels; common minimum Laurent order 12; full exact DP n=0..80; comparisons',checks)
