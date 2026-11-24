import sympy as s
from fractions import Fraction as F
from math import prod,lcm,ceil
Y,t,n,z,L=s.symbols('Y t n z L')
a=[-Y**2*(Y-6),-Y**2*(31*Y**2-516*Y+1020),-6*Y**2*(15*Y**3-406*Y**2+2078*Y-1152),-Y**3*(65*Y**3-2408*Y**2+19836*Y-27648),-5*Y**4*(3*Y**3-140*Y**2+1568*Y-3456),-Y**5*(Y-36)*(Y-16)*(Y-4)]
A=[s.Poly(x.subs(Y,16+t),t) for x in a]
def polint(polys):
 d=lcm(*(int(c.q) for p in polys for c in p.all_coeffs()));return [[int(p.nth(k)*d) for k in range(6)] for p in polys]
def pe(p,x):
 v=0
 for a in reversed(p):v=v*x+a
 return v
def fall(x,k):return prod(x-i for i in range(k))
def loc(alpha,j):
 r=5; N=300
 w=[s.Poly(s.expand(sum(A[d].nth(k-4+d)*fall(n-k+alpha,d) for d in range(6) if k-4+d>=0)*r**k),n) for k in range(8)]
 lim=[-s.LC(x)/s.LC(w[0]) for x in w[1:]]
 assert s.expand(1-sum(lim[k-1]*z**k for k in range(1,8))-(1+F(5,12)*z)*(1+F(5,16)*z)**5*(1-F(1,4)*z))==0
 D=s.Poly(w[0].as_expr().subs(n,n+N),n);sg=s.sign(D.LC());D=D.mul_ground(sg);assert all(D.nth(i)>0 for i in range(6))
 e=[]
 for k in range(1,8):
  d=s.Poly((-w[k].as_expr()-lim[k-1]*w[0].as_expr()).subs(n,n+N),n).mul_ground(sg)
  e.append(max(abs(d.nth(i))/D.nth(i) for i in range(6)))
 ep=F(sum(e));K=1/(F(7,12)*F(11,16)**5*F(3,4));assert K*ep<1
 p=polint(w); c=[F(int(i==j)*r**i) for i in range(4)] if alpha==0 else [F(1)]
 for i in range(len(c),N):c.append(-sum(pe(p[k],i)*c[i-k] for k in range(1,min(7,i)+1))/pe(p[0],i))
 B=max(abs(v) for v in c[-7:]); T=K*(sum(abs(F(v)) for v in lim)+ep)*B/(1-K*ep)
 # For y=20, t=4; evaluation derivatives, alpha=0 or 3/2. t^alpha=1 or 8.
 aa=F(alpha);fac=1 if aa==0 else 8;q=F(4,5)
 vals=[sum(v*q**i*fac*fall(i+aa,k)/4**k for i,v in enumerate(c)) for k in range(5)]
 # |fall(n+alpha,k)| <=(n+2)^4 for n>=N, k<=4; ratio <=82/100.
 assert q*F(N+3,N+2)**4<F(82,100)
 err=T*q**N*fac*(N+2)**4/F(18,100)
 # integral of (10+t)t^alpha series from 0 to 4
 valI=sum(v*q**i*fac*(40/(i+aa+1)+16/(i+aa+2)) for i,v in enumerate(c))
 errI=T*q**N*fac*56/(1-q)
 return vals+[valI],max(err,errI)
# Upper fixedpoint from PREFIX1051, use inherited all-order tail H<162/10^10.
P=[-14929920*L*(L-3)*(L-2)*(L-1)*(2*L-3),15552*L*(L-2)*(L-1)*(316*L**2-632*L+437),-432*L*(L-1)*(2*L-1)*(368*L**2-368*L+409),4*L*(2536*L**4+2903*L**2+216),-2*(2*L+1)*(40*L**4+80*L**3+98*L**2+58*L+15),(L+1)**5]
r=s.Integer(20);D=s.Poly(-P[0].subs(L,n+s.Rational(3,2)),n);R=[s.Poly(r**k*P[k].subs(L,n+s.Rational(3,2)-k),n) for k in range(1,6)]
E=s.zeros(5);E[0,:]=s.Matrix([[p.as_expr() for p in R]])
for i in range(1,5):E[i,i-1]=D.as_expr()
V=s.Matrix([[s.Rational(256,6561),s.Rational(256,729),s.Rational(32,27),s.Rational(1,16),s.Rational(256,625)],[s.Rational(64,729),s.Rational(16,27),s.Rational(4,3),s.Rational(1,8),s.Rational(64,125)],[s.Rational(16,81),s.Rational(8,9),1,s.Rational(1,4),s.Rational(16,25)],[s.Rational(4,9),1,0,s.Rational(1,2),s.Rational(4,5)],[1,0,0,1,1]])
S=s.diag(*[(r/16)**i for i in range(4,-1,-1)])*V*s.diag(1,s.Rational(1,8),s.Rational(1,64),1,1);Si=S.inv();B=(Si*E*S).applyfunc(s.expand)
ps=polint([D]+R+[s.Poly(x,n) for x in B]);M=10**800;c=[M];err=0;errors=[0]
Sin=max(sum(abs(x) for x in Si.row(i)) for i in range(5));assert max(sum(abs(x) for x in S.row(i)) for i in range(5))==3
for i in range(1,3000):
 d=pe(ps[0],i);c.append(sum(pe(ps[k],i)*c[i-k] for k in range(1,min(5,i)+1))//d)
 b=[pe(p,i) for p in ps[6:]];bn=max(sum(abs(x) for x in b[j:j+5]) for j in range(0,25,5));err=(bn*err+abs(d)-1)//abs(d)+ceil(Sin);errors.append(3*err)
assert max(errors)<10**600
assert F(sum(abs(x) for x in S.row(0)))*(max(abs(F(x)) for x in Si*s.Matrix(c[-1:-6:-1]))+err) < F(162,10**10)*M
# Upper evaluation through index 299; rest bounded by max of certified finite coefficient envelopes and inherited tail H.
q=F(4,5);N=300;T=max(F(162,10**10),max(F(abs(c[i])+errors[i],M) for i in range(N,3000)));assert q*F(N+3,N+2)**4<F(82,100)
up=[sum(F(c[i],M)*q**i*64*fall(i+F(3,2),k)*F((-1)**k,16**k) for i in range(N)) for k in range(5)]
up.append(sum(F(c[i],M)*q**i*64*(F(256)/(i+F(7,2))-F(480)/(i+F(5,2))) for i in range(N)))
ue=T*q**N*64*max(F((N+2)**4)/F(18,100),F(736)/(1-q))+F(1,10**180)
# Round exact rational enclosures to 20 decimal digits, use simple inverse residual bound.
locs=[loc(0,j) for j in range(4)];cusp,ce=loc(s.Rational(3,2),0)
assert ue<F(1,10**12) and ce<F(1,10**12) and all(e<F(1,10**12) for _,e in locs)
print('upper tail',float(ue),'cusp tail',float(ce),'local tails',[float(e) for _,e in locs],flush=True)
scale=10**20
def rnd(x):return F(x*scale//1,scale)
# Solve first four derivative equations; existence of the full connection is inherited from PREFIX1052.
AA=s.Matrix([[rnd(locs[j][0][i]) for j in range(4)] for i in range(4)])
bb=s.Matrix([rnd(up[i]-F(27,2)*cusp[i]) for i in range(4)])
Q=AA.inv()*bb
norm=lambda A:max(sum(abs(x) for x in A.row(i)) for i in range(A.rows))
eta=max(e for _,e in locs)+F(1,scale);eb=ue+F(27,2)*ce+F(1,scale);inv=F(norm(AA.inv()));assert 4*inv*eta<1
qe=inv*(eb+4*eta*max(abs(F(x)) for x in Q))/(1-4*inv*eta)
# V16 = V20 - integral analytic branch; V20 = U20 - cusp integral.
v=up[5]-F(27,2)*cusp[5]-sum(F(Q[j])*locs[j][0][5] for j in range(4))
ve=ue+F(27,2)*ce+sum(qe*abs(vals[5])+(abs(F(Q[j]))+qe)*e for j,(vals,e) in enumerate(locs))
assert qe<F(1,10**8) and ve<F(1,10**7)
print('Q', [float(x) for x in Q], 'qe',float(qe),'V16',float(v),'ve',float(ve),flush=True)
# Exact intervals reported to six decimals.
for x,e in [(F(x),qe) for x in Q]+[(v,ve)]:print((int((x-e)*10**6//1),ceil((x+e)*10**6)),flush=True)
print('PREFIX1053_CONNECTION_CERTIFICATE_PASSED')
