from fractions import Fraction as F
import sympy as s
L,n,z,t=s.symbols('L n z t')
P=[-14929920*L*(L-3)*(L-2)*(L-1)*(2*L-3),15552*L*(L-2)*(L-1)*(316*L**2-632*L+437),-432*L*(L-1)*(2*L-1)*(368*L**2-368*L+409),4*L*(2536*L**4+2903*L**2+216),-2*(2*L+1)*(40*L**4+80*L**3+98*L**2+58*L+15),(L+1)**5]
r=s.Rational(199,10); D=s.Poly(-P[0].subs(L,n+s.Rational(3,2)),n)
R=[s.Poly(r**k*P[k].subs(L,n+s.Rational(3,2)-k),n) for k in range(1,6)]
E=s.zeros(5); E[0,:]=s.Matrix([[p.as_expr() for p in R]])
for i in range(1,5): E[i,i-1]=D.as_expr()
V=s.Matrix([[s.Rational(256,6561),s.Rational(256,729),s.Rational(32,27),s.Rational(1,16),s.Rational(256,625)],[s.Rational(64,729),s.Rational(16,27),s.Rational(4,3),s.Rational(1,8),s.Rational(64,125)],[s.Rational(16,81),s.Rational(8,9),1,s.Rational(1,4),s.Rational(16,25)],[s.Rational(4,9),1,0,s.Rational(1,2),s.Rational(4,5)],[1,0,0,1,1]])
S=s.diag(*[(r/16)**i for i in range(4,-1,-1)])*V*s.diag(1,s.Rational(1,8),s.Rational(1,64),1,1)
Si=S.inv(); B=Si*E*S
norm=lambda A:max(sum(abs(A[i,j]) for j in range(5)) for i in range(5))
q=s.Rational(999,1000)
# Exact shifted coefficient row bound: |B_ij(N+z)| <= sum_k |coeff| z^k
for N in [100,200,500,1000,2000,5000,10000]:
    bp=[[s.Poly(B[i,j].subs(n,N+z),z) for j in range(5)] for i in range(5)]
    dp=s.Poly(D.as_expr().subs(n,N+z),z)
    ratios=[sum(abs(bp[i][j].nth(k)) for j in range(5))/dp.nth(k) for i in range(5) for k in range(6)]
    print(N,float(max(ratios)),flush=True)
    if max(ratios)<q:break
print('norms',float(norm(S)),float(norm(Si)),flush=True)
assert N==5000 and all(dp.nth(k)>0 for k in range(6)) and max(ratios)<=s.Rational(199,200)
q=F(199,200)
assert norm(S)<=3 and norm(Si)<68000
# fixed point exact directed error, including each recurrence step
scale=10**1500
pols=[[F(p.nth(k)) for k in range(6)] for p in R]; den=[F(D.nth(k)) for k in range(6)]
Bpol=[[ [F(s.Poly(B[i,j],n).nth(k)) for k in range(6)] for j in range(5)] for i in range(5)]
def pe(p,x):
    v=F(0)
    for a in reversed(p):v=v*x+a
    return v
def ceil(x):return -((-x.numerator)//x.denominator)
c=[scale]; errors=[0]; err=0
for i in range(1,N):
    d=pe(den,i)
    value=sum(pe(pols[k-1],i)*c[i-k] for k in range(1,min(5,i)+1))/d
    c.append(value.numerator//value.denominator)
    ni=max(sum(abs(pe(Bpol[a][b],i)) for b in range(5)) for a in range(5))/abs(d)
    err=ceil(ni*err)+68000
    errors.append(3*err)
assert max(errors)<10**1400
print('max error exponent',len(str(max(errors))), 'end vector',float(F(max(abs(c[i])+errors[i] for i in range(N-5,N)),scale)),flush=True)
H=F(3*68000*max(abs(c[i])+errors[i] for i in range(N-5,N)),scale)
T0=H*q/(1-q);T1=H*((N-1)*q/(1-q)+q/(1-q)**2)
for K in [60,100,200,300,400,500]:
    T=sum((30000+5200*i)*F(abs(c[i])+errors[i],scale) for i in range(K+1,N))+30000*T0+5200*T1
    print('K',K,'tail',float(T),flush=True)
    if T<100:break
# polynomial using rounded coefficients, algebraic exact; account for all finite rounding
Rerr=sum((30000+5200*i)*F(errors[i],scale) for i in range(K+1))
a=[F(0)]*(K+3)
for i in range(K+1):
    # x=19t; F_i: (36-x)(538-12x) -4(36-x)^2 i -12(47-x)(30/(i+5/2)-x/(i+7/2))
    A=F(30)/(i+F(5,2)); C=1/(i+F(7,2))
    f=[19368-5184*i-564*A,F(r)*(-970+288*i+12*A+564*C),F(r)**2*(12-4*i-12*C)]
    for j in range(3):a[i+j]+=F(c[i],scale)*f[j]
from math import comb
d=K+2
bern=[sum(a[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)) for k in range(d+1)]
print('bern min',float(min(bern)),'round err',float(Rerr),'final',float(min(bern)-T-Rerr),flush=True)
assert K==400 and T<64 and Rerr<1 and min(bern)>2956
assert min(bern)-T-Rerr>2891
print("PREFIX1050_CERTIFICATE_PASSED")
