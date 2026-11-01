#!/usr/bin/env python3
"""Author-side exact F_(p^2) CM(-24) group/isogeny checks; not native EM evidence."""
from math import gcd, isqrt

class Field:
    def __init__(self,p):
        assert p % 8 == 3 and p >= 11
        self.p=p
        self.z=(0,0);self.one=(1,0);self.rho=(0,1)
    def el(self,a,b=0):return a%self.p,b%self.p
    def add(self,x,y):return ((x[0]+y[0])%self.p,(x[1]+y[1])%self.p)
    def neg(self,x):return ((-x[0])%self.p,(-x[1])%self.p)
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):return ((x[0]*y[0]+2*x[1]*y[1])%self.p,(x[0]*y[1]+x[1]*y[0])%self.p)
    def inv(self,x):
        n=(x[0]*x[0]-2*x[1]*x[1])%self.p
        assert n!=0
        t=pow(n,-1,self.p)
        return ((x[0]*t)%self.p,(-x[1]*t)%self.p)
    def div(self,x,y):return self.mul(x,self.inv(y))
    def pow(self,x,n):
        r=self.one
        while n:
            if n&1:r=self.mul(r,x)
            x=self.mul(x,x);n>>=1
        return r
    def const(self,k):return k%self.p,0

def point_add(F,B,P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P; xx,yy=Q
    if x==xx and F.add(y,yy)==F.z:return None
    if P==Q:
        if y==F.z:return None
        lam=F.div(F.add(F.add(F.mul(F.const(3),F.mul(x,x)),F.mul(F.const(2),x)),B),F.mul(F.const(2),y))
    else:lam=F.div(F.sub(yy,y),F.sub(xx,x))
    z=F.sub(F.sub(F.sub(F.mul(lam,lam),F.one),x),xx)
    w=F.sub(F.mul(lam,F.sub(x,z)),y)
    return z,w

def point_mul(F,B,P,n):
    R=None
    while n:
        if n&1:R=point_add(F,B,R,P)
        P=point_add(F,B,P,P);n>>=1
    return R

def factors(n):
    d={};i=2
    while i*i<=n:
        while n%i==0:d[i]=d.get(i,0)+1;n//=i
        i+=1
    if n>1:d[n]=d.get(n,0)+1
    return d

def exact_order(F,B,P,n,fac):
    assert point_mul(F,B,P,n) is None
    order=n
    for l in fac:
        while order%l==0 and point_mul(F,B,P,order//l) is None:order//=l
    return order

def curve(F):
    # Original oriented mark B=1/8+rho/12.
    return F.add(F.const(pow(8,-1,F.p)),F.mul(F.rho,F.const(pow(12,-1,F.p))))

def enumerate_points(F,B):
    sq={}
    for a in range(F.p):
      for b in range(F.p):
        y=(a,b);sq[F.mul(y,y)]=y
    pts=[]
    for a in range(F.p):
      for b in range(F.p):
        x=(a,b);xx=F.mul(x,x)
        z=F.add(F.add(F.mul(xx,x),xx),F.mul(B,x))
        y=sq.get(z)
        if y is not None:
          pts.append((x,y))
          if y!=F.z:pts.append((x,F.neg(y)))
    return pts

def trace_group_invariants(p):
    if p%24==19:return 2*p,(p-1,p-1),None
    assert p%24==11
    reps=[(x,y) for x in range(1,isqrt(p//2)+2) for y in range(1,isqrt(p//3)+2) if 2*x*x+3*y*y==p]
    assert len(reps)==1
    x,y=reps[0]
    a=3*y*y-2*x*x; b=2*x*y
    n=(a-1)**2+6*b*b
    d=gcd(abs(a-1),abs(b))
    assert n==(p-1)**2+8*x*x
    return 2*a,(d,n//d),(x,y,a,b)

def verify_isogeny(F,B,P):
    # For p=3 mod8, (-2/p)=+1. Choose u in F_p with u²=-2.
    p=F.p
    v=next((a for a in range(p) if a*a%p==(-2)%p),None)
    assert v is not None
    u=F.const(v);assert F.mul(u,u)==F.const(-2)
    bprime=F.sub(F.const(pow(4,-1,p)),B)
    x,y=P
    assert x!=F.z
    X=F.add(F.add(x,F.one),F.div(B,x))
    Y=F.mul(y,F.sub(F.one,F.div(B,F.mul(x,x))))
    xx=F.div(X,F.const(-2))
    yy=F.div(Y,F.mul(F.const(-2),u))
    lhs=F.mul(yy,yy)
    rhs=F.mul(xx,F.add(F.add(F.mul(xx,xx),xx),bprime))
    assert lhs==rhs, (p,B,P,xx,yy)
    # Compose with its conjugate and compare to [-2] multiplication on rational points.
    if xx != F.z:
      X2=F.add(F.add(xx,F.one),F.div(bprime,xx))
      Y2=F.mul(yy,F.sub(F.one,F.div(bprime,F.mul(xx,xx))))
      zz=F.div(X2,F.const(-2))
      ww=F.div(Y2,F.mul(F.const(-2),u))
      test=point_mul(F,B,P,2)
      assert test is not None
      # phi'(phi(P)) is [+-2]P, with differential multiplier u^2=-2, so [-2].
      assert (zz,ww)==(test[0],F.neg(test[1]))
    return True

def isogeny_point(F,B,P,u):
    if P is None:return None
    x,y=P
    if x==F.z:return None  # kernel: O and (0,0)
    X=F.add(F.add(x,F.one),F.div(B,x))
    Y=F.mul(y,F.sub(F.one,F.div(B,F.mul(x,x))))
    return F.div(X,F.const(-2)),F.div(Y,F.mul(F.const(-2),u))

def psi_point(F,B,P,u):
    if P is None:return None
    # F_p-semi-linear Frobenius, rho^p=-rho, followed by phi_{B^p}.
    fr=lambda a:(a[0],(-a[1])%F.p)
    bconj=F.sub(F.const(pow(4,-1,F.p)),B)
    Q=(fr(P[0]),fr(P[1]))
    return isogeny_point(F,bconj,Q,u)

def run(p,full):
    F=Field(p);B=curve(F);Bconj=F.sub(F.const(pow(4,-1,p)),B)
    assert Bconj==F.pow(B,p)
    n_expected,smith,rep=trace_group_invariants(p)
    pts=enumerate_points(F,B)
    n=len(pts)+1; assert n==F.p*F.p+1-n_expected, (p,n,n_expected)
    fac=factors(n)
    target_exponent=smith[1]
    tested=pts if full else pts[::max(1,len(pts)//160)]
    orders=[]
    lcm=1
    for P in tested:
       o=exact_order(F,B,P,n,fac);lcm=lcm//gcd(lcm,o)*o;orders.append(o)
    assert lcm==target_exponent,(p,smith,lcm)
    sample=[u for u in pts if u[0]!=F.z][:30]
    assert len(sample)==30
    u=F.const(next(a for a in range(p) if a*a%p==(-2)%p))
    for P in sample:
        verify_isogeny(F,B,P)
        # psi^2=[-2]*Frob_(p^2) and Frob_(p^2)P=P for rational points.
        PP=psi_point(F,B,psi_point(F,B,P,u),u)
        T=point_mul(F,B,P,2)
        negT=None if T is None else (T[0],F.neg(T[1]))
        assert PP==negT,(p,P,PP,negT)
    return {'p':p,'branch':p%24,'count':n,'smith':smith,'representation':rep,'enumerated_points':len(pts),'tested_point_orders':len(tested),'observed_exponent':lcm,'isogeny_checks':len(sample),'twisted_frobenius_square_checks':len(sample)}

if __name__=='__main__':
    results=[]
    for p,full in [(11,True),(19,True),(43,True),(59,True),(67,False),(83,False),(107,False)]:
        result=run(p,full);results.append(result);print(result,flush=True)
    assert trace_group_invariants(3347)==(-6106,(2,5604258),(40,7,-3053,560))
    print('p=3347 trace -6106; group invariants (2,5604258); norm group order 11208516')
    print('PASS_GH158_GH159_GH160_CM24_GROUP_ISOGENY_FROBENIUS_SQUARE')
