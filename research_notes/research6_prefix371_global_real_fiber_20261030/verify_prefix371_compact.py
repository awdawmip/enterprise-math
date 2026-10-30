#!/usr/bin/env python3
"""Exact global generic-fiber source counts; H3 exceptional point excluded."""
import sympy as s
I,R=s.I,s.Rational
r,u,v,z,x=s.symbols('r u v z x')
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=s.simplify(A[3:,:]*A[:3,:].inv());D=12759*r*r-3521;N=200-2125*r*r
Q=[a*D+b*N for a,b in ((34000,204144),(3200,56336),(58250,1286),(46600,12936),(31525,28011))]
assert s.expand(Q[0]+78885200)==0 and s.expand(Q[1]-r*r*Q[0])==0
F=[]
for j in range(2):
 a,b,c=B.row(j)
 F.append(s.Poly(s.expand((a+b*u+c*v)*(s.conjugate(a)*Q[0]*u*v+s.conjugate(b)*Q[1]*v+s.conjugate(c)*Q[2]*u)-Q[j+3]*u*v),v))
a,b,c=F[0].all_coeffs();d,e,f=F[1].all_coeffs()
res=s.expand((a*f-c*d)**2-(a*e-b*d)*(b*f-c*e));P=s.Poly(s.cancel(res/u),u)
L=s.Poly(s.expand(d*b-a*e),u); E=s.Poly(a,u);M=s.expand(d*c-a*f)
assert s.Poly(res,u).TC()==0 and (P.degree(),L.degree(),E.degree())==(6,3,1)
assert s.expand(a*res-(a*M*M-b*M*L.as_expr()+c*L.as_expr()**2))==0
C=-15875761857587332812500*r**3*(3980*r*r-1101)
H=s.Poly(s.cancel(s.expand((1-I*z)**6*P.as_expr().subs(u,r*(1+I*z)/(1-I*z)))),z)
h=s.Poly.from_list([s.cancel(q/C) for q in H.all_coeffs()],z)
assert h.degree()==6 and all(not q.has(I) for q in h.all_coeffs())
lo,hi=R(8,85),R(4321,21259)
assert 0<lo<hi<R(3521,12759)<R(1101,3980)
assert not s.cancel(P.LC()/(3980*r*r-1101)).has(r)
assert not s.cancel(P.TC()/(r**6*(3980*r*r-1101))).has(r)
assert not L.LC().has(r) and not E.LC().has(r)
def even(q):
 p=s.Poly(q,r,extension=I);assert all(m[0]%2==0 for m,c in p.terms())
 d={(m[0]//2,):c for m,c in p.terms()}
 return s.Poly.from_dict(d,x,domain='QQ') if all(c.as_real_imag()[1]==0 for c in d.values()) else s.Poly.from_dict(d,x,extension=I)
fac=s.factor_list(s.discriminant(h.as_expr(),z))[1]
assert sorted((s.degree(q,r),e0) for q,e0 in fac)==[(1,12),(6,2),(24,1)]
G=even(next(q for q,e0 in fac if s.degree(q,r)==6))
J=even(next(q for q,e0 in fac if s.degree(q,r)==24))
assert G.count_roots(lo,hi)==1 and J.count_roots(lo,hi)==2
assert s.gcd(G,G.diff()).degree()==s.gcd(J,J.diff()).degree()==s.gcd(G,J).degree()==0
boxes=[(J,R(1082409950,10**10),R(1082409951,10**10)),
       (G,R(1422183178,10**10),R(1422183179,10**10)),
       (J,R(1462481329,10**10),R(1462481330,10**10))]
for poly,left,right in boxes:
 assert lo<left<right<hi and poly.count_roots(left,right)==1 and poly.eval(left)*poly.eval(right)<0
pl=s.factor_list(s.resultant(P.as_expr(),L.as_expr(),u))[1]
assert sorted((s.degree(q,r),e0) for q,e0 in pl)==[(1,12),(2,6),(6,2)]
assert even(next(q for q,e0 in pl if s.degree(q,r)==6)).monic()==G.monic()
pe=s.factor_list(s.resultant(P.as_expr(),E.as_expr(),u))[1]
assert sorted((s.degree(q,r),e0) for q,e0 in pe)==[(1,6),(2,1),(6,1)]
K=even(next(q for q,e0 in pe if s.degree(q,r)==6))
kr=s.Poly.from_dict({m:s.re(c) for m,c in K.terms()},x,domain='QQ')
ki=s.Poly.from_dict({m:s.im(c) for m,c in K.terms()},x,domain='QQ')
assert s.gcd(kr,ki).degree()==0
for rv,want in ((R(5,16),6),(R(1,3),4),(R(2,5),2)):
 q=s.Poly(h.as_expr().subs(r,rv),z,domain='QQ'); chain=[s.Poly(w,z,domain='QQ') for w in s.sturm(q.as_expr(),z)]
 def V(neg):
  signs=[int(s.sign(p.LC()))*(-1 if neg and p.degree()%2 else 1) for p in chain]
  return sum(a!=b for a,b in zip(signs,signs[1:]))
 assert V(True)-V(False)==want
print('discriminant_degree_x',G.degree(),J.degree(),'physical_critical_counts',1,2)
print('critical_x_boxes',[(str(a),str(b)) for _,a,b in boxes])
print('counts','6, 5 at fold a, 4, H3 unresolved, 4, 3 at fold b, 2')
print('PASS_PREFIX371_GENERIC_FIBERS_AND_TWO_FOLD_BOUNDARY_COUNTS')
