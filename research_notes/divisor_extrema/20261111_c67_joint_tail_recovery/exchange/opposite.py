"""Exact trace and common-suffix exclusion for the opposite orientations of 02/11."""
import json
from fractions import Fraction as Q
from math import comb,prod
import sympy as sp
from small_moves import polys,core,R,C

BOUND=10**6
NARROW=(Q(16268745,10**7),Q(16268758,10**7))
BROAD=(Q(16268,10000),Q(16271,10000))
LEFT,RIGHT=(0,2),(1,1)

def chart(poly):
    p=sp.Poly(poly,R,C)
    d=p.total_degree()
    return {(j,d-i-j):int(a) for ((i,j),a) in p.terms()}

def axis(coeff,x,y):
    """Coefficients after positive substitution t=(x+y*z)/(1+z) and clearing."""
    n=len(coeff)-1
    ans=[0]*(n+1)
    for i,a in enumerate(coeff):
        if a:
            for j in range(i+1):
                v=a*comb(i,j)*x**(i-j)*y**j
                for h in range(n-i+1):ans[j+h]+=v*comb(n-i,h)
    return ans

def sign_on(poly,w,v):
    d=chart(poly)
    n=max(i for i,j in d)
    m=max(j for i,j in d)
    tmp=[axis([d.get((i,j),0) for i in range(n+1)],*w) for j in range(m+1)]
    allc=[a for i in range(n+1) for a in axis([tmp[j][i] for j in range(m+1)],*v)]
    assert min(allc)>0 or max(allc)<0,(w,v)
    return 1 if min(allc)>0 else -1

def bounds(trace):
    for n,band in [(5000,BROAD),(BOUND,NARROW)]:
        v=(Q(0),Q(1,n));lo,hi=band
        assert sign_on(trace,(Q(1),lo),v)*sign_on(trace,(hi,Q(4)),v)==-1

def finite(trace):
    p=sp.Poly(trace,R,C)
    primes=(17,19,23,29,31)
    value=sp.lambdify((R,C),p.as_expr(),'math')
    residues={q:[{j for j in range(q) if value(i,j)%q==0} for i in range(q)] for q in primes}
    q1,q2=primes[:2]
    mod=q1*q2
    rows=[[c for c in range(mod) if c%q1 in residues[q1][r%q1] and c%q2 in residues[q2][r%q2]] for r in range(mod)]
    surviving=checked=0
    for r in range(2,BOUND):
        if r<5000:lo,hi=r+2,4*r-1
        else:lo,hi=16268*r//10000,16271*r//10000+1
        checked+=hi-lo+1
        for a in rows[r%mod]:
            for c in range(lo+(a-lo)%mod,hi+1,mod):
                if all(c%q in residues[q][r%q] for q in primes[2:]):
                    surviving+=1
                    assert value(r,c)!=0,(r,c)
    return dict(last_r=BOUND-1,band_checked=checked,exact_trace_evaluations=surviving)

class Box:
    def __init__(self,lo,hi=None):
        self.lo=Q(lo)
        self.hi=Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,v):
        v=asbox(v)
        return Box(self.lo+v.lo,self.hi+v.hi)
    __radd__=__add__
    def __sub__(self,v):
        v=asbox(v)
        return Box(self.lo-v.hi,self.hi-v.lo)
    def __rsub__(self,v):return asbox(v).__sub__(self)
    def __mul__(self,v):
        v=asbox(v);ends=[x*y for x in (self.lo,self.hi) for y in (v.lo,v.hi)]
        return Box(min(ends),max(ends))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=asbox(v)
        assert v.lo*v.hi>0
        return self*Box(1/v.hi,1/v.lo)
    def __rtruediv__(self,v):return asbox(v)/self

def asbox(v):return v if isinstance(v,Box) else Box(v)

def cylinder(j,b,m):
    """j pairs and b fives already consumed since the initial stock."""
    u=Box(0,Q(1,BOUND));w=Box(*NARROW)
    k=2+(1-2*j)*u
    n=w-b*u
    rho=prod((k+4*(n-i*u))/(k+n-i*u) for i in range(m+1))/4**m
    tau=(28*prod((k+4*(n-i*u))/(4*k+n-i*u) for i in range(m+1))*
         (k-u+4*(n-m*u))/(k-u+n-m*u)/4**m)
    return tau,rho

def forcing(a,b,c):
    lo,hi=Q(30624,100000),Q(30627,100000)
    signs=[]
    for z in (lo,hi):
        P=core((a*z*z+b*z+c)*z.denominator**2,4)
        signs.append(sign_on(P,NARROW,(Q(0),Q(1,BOUND))))
    assert signs[0]*signs[1]==-1
    z=Box(lo,hi)
    def rounded(z):
        return [z.lo.numerator*100000//z.lo.denominator,-((-z.hi.numerator*100000)//z.hi.denominator)]
    trace=[rounded(z)]
    for j,b0 in ((2,2),(3,6),(4,10)):
        _,rho3=cylinder(j,b0,3)
        t4,rho4=cylinder(j,b0,4)
        t5,rho5=cylinder(j,b0,5)
        # all continuations begin with at least one more block. rho0<2.36 uniformly
        # even after as many as c-2 fives; r decreases by one at the following cut.
        assert cylinder(j+1,0,0)[1].hi<Q(236,100)
        max5=(t5*Q(236,100)+rho5)/(t5*Q(236,100)+1)
        assert rho3.lo>z.hi and 1>z.hi and max5.hi<z.lo,(j,rounded(z),rounded(max5))
        if j==4:
            assert z.hi<rho4.lo
        else:
            z=(z-rho4)/(t4*(1-z))
            trace.append(rounded(z))
    return dict(z_intervals_units_of_1e_minus5=trace)

if __name__=='__main__':
    a,b,c,t=polys(R,C,LEFT,RIGHT)
    trace=core(t,4)
    bounds(trace)
    force=forcing(a,b,c)
    print(json.dumps(dict(finite=finite(trace),large=force),indent=2))
