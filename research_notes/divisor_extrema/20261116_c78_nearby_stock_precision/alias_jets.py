"""Rational outward Taylor jets (coefficients divided by factorial) through order six."""
from rational_interval import Interval as I,box
from fractions import Fraction as Q


class J:
 n=6
 def __init__(self,l):
    self.a=l if type(l)==list else [box(l)]
    self.a=self.a+[box(0)]*(self.n+1-len(self.a))
 def __add__(self,o):
    o=jj(o);return J([a+b for a,b in zip(self.a,o.a)])
 __radd__=__add__
 def __sub__(self,o):
    o=jj(o);return J([a-b for a,b in zip(self.a,o.a)])
 def __rsub__(self,o):return jj(o)-self
 def __mul__(self,o):
    o=jj(o);return J([sum((self.a[j]*o.a[k-j] for j in range(k+1)),box(0)) for k in range(self.n+1)])
 __rmul__=__mul__
 def log(self):
    a=self.a; u=[box(0)]
    for k in range(1,self.n+1):
        u.append((a[k]-sum((j*u[j]*a[k-j]/k for j in range(1,k)),box(0)))/a[0])
    return J(u)
 def power(self,r):
    a=self.a
    if r.denominator==1:
        b=a[0]**r.numerator
    elif r.denominator==2:
        b=a[0].sqrt()**r.numerator
    elif r.denominator==4:
        b=a[0].sqrt().sqrt()**r.numerator
    else:raise Exception(r)
    u=[b]
    for k in range(1,self.n+1):
        u.append(sum((((r+1)*j-k)*a[j]*u[k-j] for j in range(1,k+1)),box(0))/(k*a[0]))
    return J(u)
def jj(x):return x if type(x)==J else J(x)
def field(x,y):
 X=x.log();Y=y.log(); A=4*x.power(Q(15,4)); D=4*y.power(Q(9,4))* invpow(x,Q(9,4))
 B=A.power(Q(5))*Q(7,16);Z=B*D
 return 9*X-12*Y-(1+112*x.power(Q(15))).log(),-Q(3,4)*Y+ B.log()+5*D.log()+(1-A).log()+(1-D).log()-(1+Z).log()-(A+Z).log()
def invpow(x,r):
 y=x.power(r);a=y.a;u=[1/a[0]]
 for k in range(1,x.n+1):
    u.append(-sum((a[j]*u[k-j] for j in range(1,k+1)),box(0))/a[0])
 return J(u)
def solve(a,b,r):
 d=a[0]*b[1]-a[1]*b[0]
 return ((r[0]*b[1]-r[1]*b[0])/d,(a[0]*r[1]-a[1]*r[0])/d)
def evaluate(M,Y,U):
 f=field(1-M,Y);g=field(U,U-M)
 return [s-t for s,t in zip(f,g)]
def compute(m,y,u):
 N=J.n; J.n=1
 def sl(m1,y1,u1):
    return [r.a[1] for r in evaluate(J([m,box(m1)]),J([y,box(y1)]),J([u,box(u1)]))]
 a,b=sl(0,1,0),sl(0,0,1)
 M=[m,box(1)];Y=[y];U=[u]
 for k in range(1,N+1):
    J.n=k
    res=[-r.a[k] for r in evaluate(J(M),J(Y),J(U))]
    dy,du=solve(a,b,res)
    Y.append(dy);U.append(du)
 J.n=N
 return J(M),J(Y),J(U)
def det(mat):
 if len(mat)==1:return mat[0][0]
 return sum(((-1)**j*v*det([line[:j]+line[j+1:] for line in mat[1:]]) for j,v in enumerate(mat[0])),box(0))
