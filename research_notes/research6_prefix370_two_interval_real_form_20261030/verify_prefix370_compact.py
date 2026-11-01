#!/usr/bin/env python3
"""Exact two-interval source counts; Python 3 + SymPy 1.14. No floating roots."""
import sympy as s
I,R=s.I,s.Rational
r,u,v,z=s.symbols('r u v z'); eps=R(3,10**9)
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=s.simplify(A[3:,:]*A[:3,:].inv()); D=12759*r*r-3521; N=200-2125*r*r
Q=[x*D+y*N for x,y in ((34000,204144),(3200,56336),(58250,1286),(46600,12936),(31525,28011))]
F=[]
for j in range(2):
 a,b,c=B.row(j)
 F.append(s.Poly(s.expand((a+b*u+c*v)*(s.conjugate(a)*Q[0]*u*v+s.conjugate(b)*Q[1]*v+s.conjugate(c)*Q[2]*u)-Q[j+3]*u*v),v))
a,b,c=F[0].all_coeffs();d,e,f=F[1].all_coeffs()
res=s.expand((a*f-c*d)**2-(a*e-b*d)*(b*f-c*e))
P=s.Poly(s.cancel(res/u),u);L=s.Poly(s.expand(d*b-a*e),u);E=s.Poly(a,u)
M=s.expand(d*c-a*f)
assert s.Poly(res,u).TC()==0 and (P.degree(),L.degree(),E.degree())==(6,3,1)
assert s.expand(a*res-(a*M*M-b*M*L.as_expr()+c*L.as_expr()**2))==0
H=s.Poly(s.cancel(s.expand((1-I*z)**6*P.as_expr().subs(u,r*(1+I*z)/(1-I*z)))),z)
C=-15875761857587332812500*r**3*(3980*r*r-1101)
h=s.Poly.from_list([s.cancel(x/C) for x in H.all_coeffs()],z)
assert h.degree()==6 and all(not x.has(I) and s.denom(x)==1 for x in h.all_coeffs())
assert s.expand(Q[1]-r*r*Q[0])==0
assert B[0,0]*B[1,1]-B[1,0]*B[0,1]!=0

def parts(x):return tuple(s.cancel(y) for y in s.expand(x).as_real_imag())
def norm(x):return sum(abs(y) for y in parts(x))
def syl(p,q):
 m,n=p.degree(),q.degree();rows=[]
 for k in range(n):rows.append([s.Integer(0)]*k+p.all_coeffs()+[s.Integer(0)]*(n-1-k))
 for k in range(m):rows.append([s.Integer(0)]*k+q.all_coeffs()+[s.Integer(0)]*(m-1-k))
 return rows
pairs=[('simple',h,h.diff()),('lift',P,L),('quadratic',P,E)]

def certify(p,q,r0):
 rows=syl(p,q); n=len(rows)
 ps=s.Poly(p.as_expr().subs(r,r0),p.gens[0],extension=I)
 qs=s.Poly(q.as_expr().subs(r,r0),q.gens[0],extension=I)
 assert ps.degree()==p.degree() and qs.degree()==q.degree() and s.gcd(ps,qs).degree()==0
 inv=s.Matrix([[x.subs(r,r0) for x in row] for row in rows]).inv()
 pol=[[s.Poly(x,r,extension=I) for x in row] for row in rows]
 degree=max(x.degree() for row in pol for x in row if not x.is_zero)
 K=R(0)
 for k in range(1,degree+1):
  Z=inv*s.Matrix([[sum(c*s.binomial(j,k)*r0**(j-k) for (j,),c in pol[a][b].terms() if j>=k) for b in range(n)] for a in range(n)])
  K+=eps**k*max(sum(norm(Z[a,b]) for b in range(n)) for a in range(n))
 assert K<R(1,2)
 return n,K

def sturm_count(r0):
 p=s.Poly(h.as_expr().subs(r,r0),z,domain=s.QQ)
 st=[s.Poly(q,z,domain=s.QQ) for q in s.sturm(p.as_expr(),z)]
 def signs(neg):return [int(s.sign(x.LC()))*(-1 if neg and x.degree()%2 else 1) for x in st]
 def var(x):return sum(a!=b for a,b in zip(x,x[1:]))
 return var(signs(True)),var(signs(False))

def nozero(poly,r0):
 p=s.Poly(poly,r,extension=I)
 main=norm(p.eval(r0))
 delta=sum(eps**j*norm(sum(c*s.binomial(k,j)*r0**(k-j) for (k,),c in p.terms() if k>=j)) for j in range(1,p.degree()+1))
 return main>delta

t=lambda x:s.factor((200-2125*x*x)/(12759*x*x-3521))
for r0,n in [(R(5,16),6),(R(2,5),2)]:
 assert R(1,4)<r0-eps<r0+eps<R(1,2)
 assert (3980*(r0+eps)**2-1101)<0 and D.subs(r,r0+eps)<0
 assert 0<t(r0-eps)<t(r0+eps)<R(1,4)
 vminus,vplus=sturm_count(r0)
 assert vminus-vplus==n
 for term in (P.LC(),P.TC(),L.LC(),E.LC(),h.LC()): assert nozero(term,r0)
 cert=[certify(p,q,r0) for _,p,q in pairs]
 print('center',r0,'sturm',vminus,vplus,'physical sources',n)
 print('t_interval',t(r0-eps),t(r0+eps))
 print('sylvester',[(name,size) for (name,_,_), (size,_) in zip(pairs,cert)])
 assert all(K<R(1,2) for _,K in cert)
print('PASS_PREFIX370_EXACT_SIX_AND_TWO_SOURCE_INTERVALS')
