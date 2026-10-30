#!/usr/bin/env python3
"""Exact interval (not sampling) certificate, PREFIX-369; needs SymPy 1.14."""
import sympy as s
I,R=s.I,s.Rational
r,u,v,z=s.symbols('r u v z'); r0=R(1,3); eps=R(1,10**8)
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=s.simplify(A[3:,:]*A[:3,:].inv());D=12759*r*r-3521;N=200-2125*r*r
Q=[x*D+y*N for x,y in ((34000,204144),(3200,56336),(58250,1286),(46600,12936),(31525,28011))]
F=[]
for j in range(2):
 a,b,c=B.row(j)
 F.append(s.Poly(s.expand((a+b*u+c*v)*(s.conjugate(a)*Q[0]*u*v+s.conjugate(b)*Q[1]*v+s.conjugate(c)*Q[2]*u)-Q[j+3]*u*v),v))
a,b,c=F[0].all_coeffs();d,e,f=F[1].all_coeffs()
res=s.expand((a*f-c*d)**2-(a*e-b*d)*(b*f-c*e))
P=s.Poly(s.cancel(res/u),u); L=s.Poly(s.expand(d*b-a*e),u); E=s.Poly(a,u)
assert s.expand(s.Poly(res,u).TC())==0 and P.degree()==6 and L.degree()==3 and E.degree()==1
M=s.expand(d*c-a*f)
assert s.expand(a*res-(a*M*M-b*M*L.as_expr()+c*L.as_expr()**2))==0
H=s.Poly(s.cancel(s.expand((1-I*z)**6*P.as_expr().subs(u,r*(1+I*z)/(1-I*z)))),z)
C=-15875761857587332812500*r**3*(3980*r*r-1101)
h=s.Poly.from_list([s.cancel(x/C) for x in H.all_coeffs()],z)
assert h.degree()==6 and all(not x.has(I) and s.denom(x)==1 for x in h.all_coeffs())
base=[7677444377,13405512300,-268186356798,-871817823240,-277296710751,191951130444,75139396712]
h0=s.Poly(h.as_expr().subs(r,r0),z);p0=s.Poly.from_list(base,z)
assert s.expand(h0.as_expr()*p0.LC()-p0.as_expr()*h0.LC())==0
st=[s.Poly(x,z,domain=s.QQ) for x in s.sturm(p0.as_expr(),z)]
var=lambda a:sum(x!=y for x,y in zip(a,a[1:]))
sgn=lambda p,neg:int(s.sign(p.LC()))*((-1)**p.degree() if neg else 1)
assert (var([sgn(x,True) for x in st]),var([sgn(x,False) for x in st]))==(5,1)

def parts(x):return tuple(s.cancel(y) for y in s.expand(x).as_real_imag())
def syl(p,q):
 m,n=p.degree(),q.degree();rows=[]
 for k in range(n):rows.append([s.Integer(0)]*k+p.all_coeffs()+[s.Integer(0)]*(n-1-k))
 for k in range(m):rows.append([s.Integer(0)]*k+q.all_coeffs()+[s.Integer(0)]*(m-1-k))
 return rows

def certify(p,q):
 rows=syl(p,q);n=len(rows)
 ps=s.Poly(p.as_expr().subs(r,r0),p.gens[0],extension=I)
 qs=s.Poly(q.as_expr().subs(r,r0),q.gens[0],extension=I)
 assert ps.degree()==p.degree() and qs.degree()==q.degree() and s.gcd(ps,qs).degree()==0
 inv=s.Matrix([[x.subs(r,r0) for x in row] for row in rows]).inv()
 pol=[[s.Poly(x,r,extension=I) for x in row] for row in rows]
 degree=max(x.degree() for row in pol for x in row if not x.is_zero)
 K=0
 for k in range(1,degree+1):
  mat=s.Matrix([[sum(c*s.binomial(j,k)*r0**(j-k) for (j,),c in pol[a][b].terms() if j>=k) for b in range(n)] for a in range(n)])
  Z=inv*mat
  nk=max(sum(sum(abs(t) for t in parts(Z[a,b])) for b in range(n)) for a in range(n))
  K+=eps**k*nk
 assert K<R(1,2)
 return n,K
results=[certify(h,h.diff()),certify(P,L),certify(P,E)]
for x in (P.LC(),P.TC(),L.LC(),E.LC(),h.LC()):
 poly=s.Poly(x,r,extension=I);norm=lambda y:sum(abs(a) for a in parts(y))
 assert norm(poly.eval(r0))>eps*sum(k*norm(a) for (k,),a in poly.terms() if k)
assert 0<r0-eps<r0+eps<R(1,2) and 3980*R(1,2)**2-1101<0
assert (B[0,0]*B[1,1]-B[1,0]*B[0,1])!=0
# t'(r)=9860650*r/(12759*r*r-3521)**2 >0 and 0<t<1/4 here.
t=lambda x:s.factor((200-2125*x*x)/(12759*x*x-3521))
assert 0<t(r0-R(1,1000))<t(r0+R(1,1000))<R(1,4)
assert t(r0)==R(65,3786)
print('PASS_PREFIX369_EXACT_UNIFORM_FOUR_SOURCE_INTERVAL')
print('exact_t_interval',t(r0-eps),t(r0+eps))
for (n,k),q in zip(results,(30,6,1000)):
 assert k<R(1,q)
 print('sylvester_size',n,'norm <1/'+str(q))
print('physical_U1_source_count_for_every_t_in_closed_interval',4)
