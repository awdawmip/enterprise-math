"""Exact projective count for the frozen static 5-Port model; SymPy 1.14."""
import sympy as s
I,R=s.I,s.Rational
t,u,v,p,q=s.symbols('t u v p q')
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=A[3:,:]*A[:3,:].inv()
Q=[34000+204144*t,3200+56336*t,58250+1286*t,46600+12936*t,31525+28011*t]
F=[];T=[]
for j in range(2):
 a,b,c=map(s.simplify,B.row(j))
 F.append(s.expand((a+b*u+c*v)*(s.conjugate(a)*Q[0]*u*v+s.conjugate(b)*Q[1]*v+s.conjugate(c)*Q[2]*u)-Q[j+3]*u*v))
 T.append(s.expand((a*p*q+b*q+c*p)*(s.conjugate(a)*Q[0]+s.conjugate(b)*Q[1]*p+s.conjugate(c)*Q[2]*q)-Q[j+3]*p*q))
 assert s.expand(p*p*q*q*F[-1].subs({u:1/p,v:1/q})-T[-1])==0
 assert max(k[0] for k in s.Poly(F[-1],u,v).monoms())==2
 assert max(k[1] for k in s.Poly(F[-1],u,v).monoms())==2
J0=s.Matrix([[s.diff(f,z).subs({u:0,v:0}) for z in (u,v)] for f in F]).det()
Ji=s.Matrix([[s.diff(f,z).subs({p:0,q:0}) for z in (p,q)] for f in T]).det()
assert s.expand(J0-(R(3699,2)-R(1313,2)*I)*(643*t+29125)*(3521*t+200))==0
assert s.expand(Ji-(14796+5252*I)*(12759*t+2125)**2)==0
for cols,expect in [((0,1),R(7,8)-R(37,8)*I),((0,2),R(1,2)-R(1,4)*I)]:
 det=s.simplify(s.det(s.Matrix([[s.conjugate(B[i,k]) for k in cols] for i in (0,1)])))
 assert s.expand(det-expect)==0
res=s.Poly(s.resultant(F[0],F[1],v),u)
assert res.TC()==0
P=s.Poly(s.cancel(res.as_expr()/u),u)
assert P.degree()==6
assert s.expand(P.LC()-(252404-3550672*I)*(12759*t+2125)**3*(643*t+29125))==0
assert s.expand(P.TC()-(252404+3550672*I)*(3521*t+200)**3*(643*t+29125))==0
r2=s.cancel(Q[1]/Q[0]);r3=s.cancel(Q[2]/Q[0])
assert s.cancel(r2.subs(t,0)-R(8,85))==0
assert s.cancel(r2.subs(t,R(1,4))-R(4321,21259))==0
assert s.cancel(r3.subs(t,0)-R(233,136))==0
assert s.cancel(r3.subs(t,R(1,4))-R(117143,170072))==0
assert s.diff(r2,t).subs(t,0)>0 and s.diff(r3,t).subs(t,0)<0
print('PASS_PREFIX367_PROJECTIVE_8_EQUALS_1_PLUS_6_PLUS_1')
