from fractions import Fraction as F
from math import prod, factorial, comb
import sympy as S
n,y,x=S.symbols('n y x')
# inherited ODE
Q=[1152*n**2*(n-1)**2*(2*n-1),-4*n**3*(196*n**2+59),2*(2*n+1)*(14*n**4+28*n**3+28*n**2+14*n+3),-(n+1)**5]
# correction: leading Q2 is 56 n^5; Q1 -784 n^5
Q=[S.Poly(p,n) for p in Q]
a=[-y**2*(y-6),-y**2*(31*y**2-516*y+1020),-6*y**2*(15*y**3-406*y**2+2078*y-1152),-y**3*(65*y**3-2408*y**2+19836*y-27648),-5*y**4*(3*y**3-140*y**2+1568*y-3456),-y**5*(y-36)*(y-16)*(y-4)]
# Euler to ordinary symbolic crosscheck
op={0:S.Integer(1)}; powers=[op]
for _ in range(5):
    op={j:S.expand(y*S.diff(op.get(j,0),y)+y*op.get(j-1,0)) for j in range(len(op)+1)};powers.append(op)
for j in range(6): assert S.expand(sum(y**l*sum(Q[l].nth(k)*powers[k].get(j,0) for k in range(6)) for l in range(4))-a[j])==0
W=10**30
R=F(12,5); N=120
Y=F(1600,841); X=4-Y; assert X==F(42,29)**2 and Y==F(40,29)**2

def ev(p,t): return F(p.eval(t))
def roundbox(a,b=None):
    if b is None:b=a
    return (F(a*W//1,W),F(-((-b*W)//1),W))
def add(*boxes):return (sum(z[0] for z in boxes),sum(z[1] for z in boxes))
def mul(a,b):
    v=[i*j for i in a for j in b];return roundbox(min(v),max(v))
def sc(a,c):return mul(a,(c,c))
def mag(a):return max(map(abs,a))
def widen(a,e):return roundbox(a[0]-e,a[1]+e)
def falling(t,j):return prod(t-i for i in range(j))

def shift(p,offset):return S.Poly(p.as_expr().subs(n,n+offset),n)
def tailratio(alpha):
    d=shift(Q[0],N+alpha); ps=[S.Poly(shift(Q[l],N+alpha-l).as_expr()*R**l,n) for l in range(1,4)]
    assert all(d.nth(k)>0 for k in range(6))
    beta=max(F(sum(abs(p.nth(k)) for p in ps),d.nth(k)) for k in range(6))
    pd=[d.diff()]+[p.diff() for p in ps]
    gamma=max(F(sum(abs(p.nth(k)) for p in pd),d.nth(k)) for k in range(6))
    assert beta<1
    return beta,gamma

def zero_coeff(alpha,log=False):
    b=[F(1)]; e=[F(0)]
    if alpha==0:b.append(F(0));e.append(F(0))
    for i in range(len(b),N):
        den=ev(Q[0],i+alpha)
        b.append(-sum(R**l*ev(Q[l],i+alpha-l)*b[i-l] for l in range(1,min(i,3)+1))/den)
        if log:
            e.append(-(ev(Q[0].diff(),i+alpha)*b[i]+sum(R**l*(ev(Q[l].diff(),i+alpha-l)*b[i-l]+ev(Q[l],i+alpha-l)*e[i-l]) for l in range(1,min(i,3)+1)))/den)
    beta,gamma=tailratio(alpha); B=max(map(abs,b[-3:])); E=F(0)
    if log:E=max(max(map(abs,e[-3:])),gamma*B/(1-beta))
    print('tail',alpha,'beta',float(beta),'B',float(B),'E',float(E),flush=True)
    return b,e,B,E

def tail(B,q,alpha,k):
    # (N+alpha+j)^k <= (N+2)^k (j+1)^k
    return B*q**N*(N+2)**k*factorial(k)/(1-q)**(k+1)

def zerojet(b,alpha,B):
    q=Y/R; ya={F(0):F(1),F(1,2):F(40,29),F(1):Y}[alpha]
    return [widen(roundbox(ya*sum(bi*q**i*(i+alpha)**k for i,bi in enumerate(b))),ya*tail(B,q,alpha,k)) for k in range(5)]

# 4-side modes inherited tail (PREFIX1056 and 1057).
AA=[S.Poly((-1)**j*p.subs(y,4-x),x) for j,p in enumerate(a)]

def fourjet(alpha,j0):
    b=[F(int(i==j0)*(-1)**i) for i in range(4)] if alpha==0 else [F(1)]
    ws=[S.Poly(S.expand(sum(AA[j].nth(k-4+j)*prod(n+alpha-k-i for i in range(j)) for j in range(6) if k-4+j>=0)),n) for k in range(8)]
    for i in range(len(b),101):
        v=[ev(p,i) for p in ws];assert v[0]
        b.append(-sum(v[k]*b[i-k] for k in range(1,min(7,i)+1))/v[0])
    xa=F(1) if alpha==0 else F(42,29)**3
    q=X/F(5,2); T=F(1,10**18)
    dz=[]
    for j in range(5):
        val=sum(bi*falling(i+alpha,j)*X**i*xa/X**j*(-1)**j for i,bi in enumerate(b))
        err=T*xa/X**j*q**101*103**j*factorial(j)/(1-q)**(j+1)
        dz.append(widen(roundbox(val),err))
    return [add(*(sc(dz[j],F(powers[k].get(j,0).subs(y,Y)) if j in powers[k] else F(0)) for j in range(k+1))) for k in range(5)]

b0,e0,B0,E0=zero_coeff(F(0)); b1,e1,B1,E1=zero_coeff(F(1),True); bh,eh,Bh,Eh=zero_coeff(F(1,2))
f0=zerojet(b0,F(0),B0); f1=zerojet(b1,F(1),B1); fh=zerojet(bh,F(1,2),Bh)
# log(y/Y)=0 at matching point, theta^k(product)=k theta^(k-1) f1
fl=zerojet(e1,F(1),E1)
for k in range(1,5):fl[k]=add(fl[k],sc(f1[k-1],k))
cols=[f0,fh,f1,fl]
weights=[(F(235698,100),F(235702,100)),(F(-44062,100),F(-44059,100)),(F(6845,100),F(6848,100)),(F(-1244,100),F(-1242,100)),(F(-135),F(-135))]
modes=[fourjet(F(0),j) for j in range(4)]+[fourjet(F(3,2),0)]
obs=[add(*(mul(w,m[k]) for w,m in zip(weights,modes))) for k in range(5)]
print('obs',[(float(a),float(b)) for a,b in obs],flush=True)
# exact inverse of rational midpoint of first four rows, verified residual
M=[[cols[j][i] for j in range(4)] for i in range(4)]
C=S.Matrix([[(a+b)/2 for a,b in row] for row in M]).inv()
C=[[F(C[i,j]) for j in range(4)] for i in range(4)]
D=[[add(roundbox(int(i==j)),*(sc(M[k][j],-C[i][k]) for k in range(4))) for j in range(4)] for i in range(4)]
beta=max(sum(map(mag,row)) for row in D);assert beta<1
z=[add(*(sc(obs[k],C[i][k]) for k in range(4))) for i in range(4)]
err=beta*max(map(mag,z))/(1-beta)
coeff=[widen(v,err) for v in z]
print('inverse residual',float(beta),'coeff',[(float(a),float(b)) for a,b in coeff],flush=True)
# Optional consistency check fifth row is not used for uniqueness.
assert max(obs[4][0],add(*(mul(coeff[j],cols[j][4]) for j in range(4)))[0])<=min(obs[4][1],add(*(mul(coeff[j],cols[j][4]) for j in range(4)))[1])
# uniform bounds for y <= d. q=y/R. sqrt(y)<=sqrtbound.
d=F(1,240); q=d/R; sqrtbound=F(1,15); assert sqrtbound**2>=d
# |log(y/Y)| times y^a bounded by simple rational inequality: log(Y/y)<= (Y/y)^eps/eps, eps=1/2 gives <=2 sqrt(Y/y); more precise y log(Y/y)<= d log(Y/d) <= 7d (Y/d<e^7 via finite Taylor). y log(Y/y) increasing on [0,d] because Y/d>e, prove with e<3 and Y/d>3. log(Y/d)<7 follows e^7 >= sum through 10.
assert Y/d>3 and sum(F(7)**i/factorial(i) for i in range(11))>Y/d
# bound f series and theta powers after dividing y^alpha

def moments(b,B,start,alpha,k):
    return sum(abs(b[i])*q**i*(i+alpha)**k for i in range(start,len(b)))+tail(B,q,alpha,k)
# f0-1 and theta f0; sqrt branch; y branch; log branch
A,Ch,C1,Cl=coeff
s0=moments(b0,B0,1,F(0),0);t0=moments(b0,B0,1,F(0),1)
sh=moments(bh,Bh,0,F(1,2),0);th=moments(bh,Bh,0,F(1,2),1)
s1=moments(b1,B1,0,F(1),0);t1=moments(b1,B1,0,F(1),1)
sl=moments(e1,E1,0,F(1),0);tl=moments(e1,E1,0,F(1),1)
E0=mag(A)*s0+mag(Ch)*sqrtbound*sh+mag(C1)*d*s1+mag(Cl)*d*(7*s1+sl)
E1=mag(A)*t0+mag(Ch)*sqrtbound*th+mag(C1)*d*t1+mag(Cl)*d*(7*t1+s1+tl)
# exact K(y)=3024+536y-12y^2 >= 3024 on interval.
Cmax=3816+542*d
lo=3024*A[0]-(Cmax+72*(11+d))*E0-5184*E1
print('E0 E1 lower',float(E0),float(E1),float(lo),flush=True)
assert A[0]>4494 and A[1]<4524 and E0<75 and E1<38 and lo>13000000
print('PREFIX1058_ZERO_FROBENIUS_BRIDGE_CERTIFICATE_PASSED')
