#!/usr/bin/env python3
"""Exact symbolic/rational certificate for the fixed-contrast global Chernoff crossing."""
from fractions import Fraction as Q
import sympy as S

k=S.symbols('k')
N=5
zero=[S.Integer(0)]*N
one=[S.Integer(1)]+[S.Integer(0)]*(N-1)
def simp(a): return S.cancel(a)
def add(A,B):return [simp(A[i]+B[i]) for i in range(N)]
def scale(A,c):return [simp(a*c) for a in A]
def mul(A,B):return [simp(sum(A[j]*B[i-j] for j in range(i+1))) for i in range(N)]
def inv(A):
    B=[1/A[0]]
    for i in range(1,N):B.append(simp(-sum(A[j]*B[i-j] for j in range(1,i+1))/A[0]))
    return B
def div(A,B):return mul(A,inv(B))
def log_series(A):
    u=add(A,scale(one,-1));term=one;res=zero
    for n in range(1,N):
        term=mul(term,u)
        res=add(res,scale(term,S.Rational((-1)**(n+1),n)))
    return res

L=[S.Rational(1,2*j+1) for j in range(N)]
Lk=[S.Rational(1,2*j+1)*k**(2*j) for j in range(N)]
r=[S.binomial(S.Rational(1,2),j)*(-1)**j for j in range(N)]
D=add(L,scale(Lk,k)); R=div(D,scale(L,1+k)); P=div(scale(Lk,k),D)
psi=add(scale(log_series([1,-1,0,0,0]),S.Rational(1,2)),log_series(L))
psik=add(scale(log_series([1,-k*k,0,0,0]),S.Rational(1,2)),log_series(Lk))
T=scale(add([1-k,0,0,0,0],scale(r,2*k)),1/(1+k))
f=add(scale(log_series([1,-k*k,0,0,0]),S.Rational(1,2)),log_series(R))
f=add(f,scale(mul(P,add(psik,scale(psi,-1))),-1))
f=add(f,scale(log_series(T),-(1+k)/2))
assert f[0]==f[1]==0
p2=10*k**2+18*k-1
p3=484*k**5+1364*k**4+1960*k**3+2360*k**2+661*k-79
p4=268784*k**8+1029808*k**7+1837568*k**6+2341248*k**5+2721600*k**4+3101952*k**3+1606957*k**2+245942*k-56159
F_expected={2:k*(1-k)*p2/(72*(1+k)),3:k*(1-k)*p3/(6480*(1+k)**2),4:k*(1-k)*p4/(5443200*(1+k)**3)}
for j in (2,3,4):
    assert simp(f[j]-F_expected[j])==0
G_expected={2:(1+k)*p2/144,3:p3/12960,4:p4/(10886400*(1+k))}
for j in (2,3,4):
    assert simp(f[j]*(1+k)**2/(2*k*(1-k))-G_expected[j])==0
q3=2420*k**4+5456*k**3+5880*k**2+4720*k+661
q4=1881488*k**8+8329120*k**7+16396496*k**6+20390400*k**5+19871040*k**4+17090304*k**3+10912813*k**2+3213914*k+302101
dG={2:(30*k*k+56*k+17)/144,3:q3/12960,4:q4/(10886400*(1+k)**2)}
for j in (2,3,4):
    assert simp(S.diff(G_expected[j],k)-dG[j])==0
assert all(c>0 for c in S.Poly(q3,k).all_coeffs())
assert all(c>0 for c in S.Poly(q4,k).all_coeffs())
assert S.simplify(G_expected[2].subs(k,0))==-S.Rational(1,144)
assert S.simplify(G_expected[2].subs(k,1))==S.Rational(3,8)
assert G_expected[3].subs(k,0)<0 and G_expected[4].subs(k,0)<0
assert G_expected[3].subs(k,1)>0 and G_expected[4].subs(k,1)>0

# The analytic majorant arithmetic is exact rational arithmetic.
M=Q(25,78)+Q(65,31)+Q(225,47)*(Q(17,26)+Q(7,24))+Q(9,8)*Q(10,11)
assert M==Q(39835405,5000424) and M<8
assert Q(3,4)-Q(1,9)-Q(5,4)*Q(1,4)==Q(47,144)
assert Q(5,4)*(Q(1,4)+Q(1,9))/(Q(3,4)*Q(8,9))==Q(65,96)
assert Q(5,4)*Q(5,4)/Q(47,144)==Q(225,47)
assert Q(25,117)<Q(1,4)
assert Q(3087,387200)<Q(1,125)
x=Q(1,441); z=Q(4,441)
tail_deriv=Q(1280)*z**5/(1-z)
tail_value=Q(256)*z**5/(1-z)
lead_deriv=Q(17,144)*x*x
assert tail_deriv < lead_deriv
assert tail_value < x*x/Q(144)
assert tail_value < Q(3,8)*x*x
print('Phi complex majorant < 8:',M)
print('Cauchy derivative tail:',tail_deriv)
print('Leading global derivative bound:',lead_deriv)
print('Strict derivative lower:',lead_deriv-tail_deriv)
print('Endpoint value tail:',tail_value)
print('PASS_BRC_S23_GLOBAL_UNIQUE_FINITE_CHERNOFF_CAUCHY_CERT_20261104')
