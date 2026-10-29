#!/usr/bin/env python3
"""GH-121: exact p=3347 CM isomorphism-fiber / reflected-tail counterexample.
Author portable arithmetic; this is NOT native Enterprise Math execution.
"""
from math import comb

p = 3347
m = (p - 3) // 8
d = 2 * m
N = (p - 1) // 2
assert (m, d, N) == (418, 836, 1673)

# Elements (a,b) mean a + b*r, r^2=2, in F_(p^2).
def C(a): return (a % p, 0)
def add(a,b): return ((a[0]+b[0])%p, (a[1]+b[1])%p)
def neg(a): return ((-a[0])%p, (-a[1])%p)
def sub(a,b): return add(a,neg(b))
def mul(a,b): return ((a[0]*b[0]+2*a[1]*b[1])%p,
                       (a[0]*b[1]+a[1]*b[0])%p)
def norm(a): return (a[0]*a[0]-2*a[1]*a[1])%p
def inv(a):
    z = norm(a)
    assert z
    return (a[0]*pow(z,-1,p)%p, -a[1]*pow(z,-1,p)%p)
def div(a,b): return mul(a,inv(b))
def power(a,n):
    out=C(1)
    while n:
        if n & 1: out=mul(out,a)
        a=mul(a,a); n//=2
    return out
def chi(a):
    n=norm(a)
    return 0 if not n else (1 if pow(n,(p-1)//2,p)==1 else -1)
def sqrt_fp(a):
    a%=p
    if not a: return 0
    x=pow(a,(p+1)//4,p)
    assert x*x%p==a
    return x
def sqrt_fq(a):
    # For p=3 mod4, solve (x+yr)^2=a by its F_p norm.
    if a==C(0):return C(0)
    n=sqrt_fp(norm(a))
    for sign in (1,-1):
        xx=(a[0]+sign*n)*pow(2,-1,p)%p
        if xx and pow(xx,(p-1)//2,p)==1:
            x=sqrt_fp(xx)
            y=a[1]*pow(2*x,-1,p)%p
            ans=(x,y)
            if mul(ans,ans)==a:return ans
    raise AssertionError('nonsquare in F_(p^2)')

# Source path 1: GH-16 direct reflected-h_j recurrence, no elliptic inputs.
h=1; R1=[0]*(N+1)
for j in range(d+1):
    R1[d+1+j]=(8*j+5)*h*pow(d+1+j,-1,p)%p
    if j<d:
        h=h*pow(4*j+3,3,p)*pow((4*j+4)*(4*j+5)*(4*j+6),-1,p)%p

def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
    return out

def poly_legendre(n):
    a,b=[1],[0,1]
    if n==0:return a
    for k in range(1,n):
        out=[0]*max(len(a),len(b)+1)
        for i,t in enumerate(b):out[i+1]=(out[i+1]+(2*k+1)*t)%p
        for i,t in enumerate(a):out[i]=(out[i]-k*t)%p
        a,b=b,[t*pow(k+1,-1,p)%p for t in out]
    return b

# Source path 2: Legendre/Hasse polynomial, followed by GH-108's derivative.
P=poly_legendre(d)
assert all(P[j]==0 for j in range(1,d+1,2))
E=P[::2]
G=[0]*(m+1)
for j,ej in enumerate(E):
    for k in range(j+1):
        G[m-j+k]=(G[m-j+k]+ej*comb(j,k)*(-1)**(j-k))%p
D=comb(3*m+1,m)%p
assert (D,G[0],G[-1])==(3073,3073,1)
A=[(16*j+5)*v%p for j,v in enumerate(G)]
GA=poly_mul(G,A)
R2=[0]*(N+1)
for j,v in enumerate(GA):
    R2[d+1+j]=v*pow(D*D,-1,p)*pow(d+1+j,-1,p)%p
assert R1==R2, 'independent reflected-tail coefficient sources differ'

def evaluate(poly,z):
    out=C(0)
    for coef in reversed(poly):out=add(mul(out,z),C(coef))
    return out

def j_invariant(T):
    num=mul(C(64),power(sub(C(5),mul(C(3),T)),3))
    den=mul(power(add(C(1),T),2),sub(C(1),T))
    return div(num,den)

# The specific -24 CM member and its two alternative 2-torsion origins.
r=(0,1)
assert power(r,2)==C(2) and pow(2,(p-1)//2,p)==p-1
T=div(mul(C(2),r),C(3))
b=div(add(C(1),T),C(8))
z=div(C(1),sub(C(1),power(T,2)))
assert z==C(9)
root3=sqrt_fp(3)
eta=mul(C(root3),r)
assert power(eta,2)==C(6)
w=div(sub(r,C(1)),eta)
assert power(w,2)==div(sub(C(1),T),C(2))
alpha_roots=(div(add(neg(C(1)),w),C(2)),
             div(sub(neg(C(1)),w),C(2)))
assert j_invariant(T)==(938,3053)
assert evaluate(R1,z)==C(0)

rows=[]
for alpha in alpha_roots:
    assert add(add(power(alpha,3),power(alpha,2)),mul(b,alpha))==C(0)
    c2=add(mul(C(3),alpha),C(1))
    assert chi(c2)==1
    lam=sqrt_fq(c2)
    assert power(lam,2)==c2
    bp=div(add(add(mul(C(3),power(alpha,2)),mul(C(2),alpha)),b),power(c2,2))
    Tp=sub(mul(C(8),bp),C(1))
    zp=div(C(1),sub(C(1),power(Tp,2)))
    assert j_invariant(Tp)==j_invariant(T)
    # Explicit coefficient test for f(alpha+c2*X)/lam^6 = X^3+X^2+bp*X.
    assert div(add(mul(C(3),alpha),C(1)),c2)==C(1)
    assert div(add(add(mul(C(3),power(alpha,2)),mul(C(2),alpha)),b),power(c2,2))==bp
    v1=evaluate(R1,zp)
    v2=evaluate(R2,zp)
    assert v1==v2 and v1!=C(0)
    rows.append((alpha,c2,lam,Tp,zp,v1))

expected=[
 ((1066,1977),(3199,2584),(1916,2172),(3207,479),(2907,1526)),
 ((2280,1370),(147,763),(458,813),(2251,2893),(3281,1783))
]
for row,e in zip(rows,expected):
    assert row[0]==e[0] and row[1]==e[1]
    assert row[3]==e[2] and row[4]==e[3] and row[5]==e[4]
assert rows[0][4]!=rows[1][4] and rows[0][5]!=rows[1][5]

print('PASS_GH121_CM_MARKED_FIBER_NONDESCENT')
print('p,m,d,N,D,j,R(9)=',p,m,d,N,D,j_invariant(T),evaluate(R1,z))
for i,(a,c2,lam,Tp,zp,Rp) in enumerate(rows):
    print('branch',i,'alpha',a,'c2',c2,'lambda',lam,'T_prime',Tp,'z_prime',zp,'R(z_prime)',Rp,'norm(c2)',norm(c2))
print('source crosscheck: GH16 h_j == Legendre-Hasse GH108 derivative as all',N+1,'polynomial coefficients')
print('field operations: exact integer mod',p,'; non-F_p marked points are evaluated as F_(p^2) polynomial values')
