from fractions import Fraction as F
from math import lcm, comb, ceil
import sympy as s
L,n,z=s.symbols('L n z')
P=[-14929920*L*(L-3)*(L-2)*(L-1)*(2*L-3),15552*L*(L-2)*(L-1)*(316*L**2-632*L+437),-432*L*(L-1)*(2*L-1)*(368*L**2-368*L+409),4*L*(2536*L**4+2903*L**2+216),-2*(2*L+1)*(40*L**4+80*L**3+98*L**2+58*L+15),(L+1)**5]
r=s.Integer(20); D=s.Poly(-P[0].subs(L,n+s.Rational(3,2)),n)
R=[s.Poly(r**k*P[k].subs(L,n+s.Rational(3,2)-k),n) for k in range(1,6)]
E=s.zeros(5); E[0,:]=s.Matrix([[p.as_expr() for p in R]])
for i in range(1,5): E[i,i-1]=D.as_expr()
V=s.Matrix([[s.Rational(256,6561),s.Rational(256,729),s.Rational(32,27),s.Rational(1,16),s.Rational(256,625)],[s.Rational(64,729),s.Rational(16,27),s.Rational(4,3),s.Rational(1,8),s.Rational(64,125)],[s.Rational(16,81),s.Rational(8,9),1,s.Rational(1,4),s.Rational(16,25)],[s.Rational(4,9),1,0,s.Rational(1,2),s.Rational(4,5)],[1,0,0,1,1]])
S=s.diag(*[(r/16)**i for i in range(4,-1,-1)])*V*s.diag(1,s.Rational(1,8),s.Rational(1,64),1,1)
Si=S.inv(); B=(Si*E*S).applyfunc(s.expand)
N=3000; J=N-1; K=400
# Entire half-line contraction, not sampled norms.
dp=s.Poly(((4*n-9)*D.as_expr()).subs(n,N+z),z)
bp=[[s.Poly((4*n*B[i,j]).subs(n,N+z),z) for j in range(5)] for i in range(5)]
assert all(dp.nth(k)>0 for k in range(7))
assert all(dp.nth(k)>=sum(abs(bp[i][j].nth(k)) for j in range(5)) for i in range(5) for k in range(7))
assert all(c>0 for c in s.Poly(D.as_expr().subs(n,N+z),z).all_coeffs())
Sn=max(sum(abs(x) for x in S.row(i)) for i in range(5)); Sin=max(sum(abs(x) for x in Si.row(i)) for i in range(5))
assert Sn==3 and Sin<60000
# Fixed-point recurrence with exact directed residual bound.
pols=[s.Poly(x,n) for x in [D.as_expr()]+[p.as_expr() for p in R]+list(B)]
scale_den=lcm(*(int(c.q) for p in pols for c in p.all_coeffs()))
ps=[[int(p.nth(k)*scale_den) for k in range(6)] for p in pols]
def pe(p,x):
    v=0
    for a in reversed(p): v=v*x+a
    return v
M=10**800; c=[M]; err=0; errors=[0]
for i in range(1,N):
    d=pe(ps[0],i); assert d!=0
    v=sum(pe(ps[k],i)*c[i-k] for k in range(1,min(5,i)+1)); c.append(v//d)
    b=[pe(p,i) for p in ps[6:]]
    bn=max(sum(abs(x) for x in b[j:j+5]) for j in range(0,25,5))
    err=(bn*err+abs(d)-1)//abs(d)+ceil(Sin); errors.append(3*err)
assert max(errors)<10**600
# Keep transformed terminal vector, avoiding product of condition numbers.
u=Si*s.Matrix(c[-1:-6:-1]); H=F(sum(abs(x) for x in S.row(0)))*(max(abs(F(x)) for x in u)+err)/M
assert H<F(162,10**10)
# n>J: |c_n|<=H*(J/n)^(9/4); integral majorants.
T0=H*F(4,5)*J; T1=4*H*J**2
# For 199/10<=x<=20, |F_n(x)|<=30000+1040*n.
assert 4*F(161,10)**2<1040
T=sum((30000+1040*i)*F(abs(c[i])+errors[i],M) for i in range(K+1,N))+30000*T0+1040*T1
Rerr=sum((30000+1040*i)*F(errors[i],M) for i in range(K+1))
a=[F(0)]*(K+3)
for i in range(K+1):
    A=F(30)/(i+F(5,2)); C=1/(i+F(7,2))
    f=[19368-5184*i-564*A,F(r)*(-970+288*i+12*A+564*C),F(r)**2*(12-4*i-12*C)]
    for j in range(3): a[i+j]+=F(c[i],M)*f[j]
d=K+2
bern=[sum(a[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)) for k in range(d+1)]
assert min(bern)>2256 and T<998 and Rerr<1
assert min(bern)-T-Rerr>1257
print('N',N,'H',float(H),'tail',float(T),'Bernstein min',float(min(bern)))
print('PREFIX1051_CRITICAL_TAIL_CERTIFICATE_PASSED')
