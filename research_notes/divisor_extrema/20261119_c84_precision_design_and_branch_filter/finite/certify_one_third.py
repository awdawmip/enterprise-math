"""Integer-directed interval certificate for F3(1/3).

Only integer arithmetic and isqrt are used in interval operations and elementary
bounds. Midpoint quadrature uses interval automatic second derivatives. The
first cell at each logarithmic endpoint uses a direct range enclosure instead.
"""
from argparse import ArgumentParser
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json
from time import perf_counter

BITS=120
SCALE=1<<BITS
TERMS=48

def ceildiv(a,b):return -((-a)//b)

@dataclass(frozen=True)
class I:
    lo:int
    hi:int
    def __post_init__(self):
        assert self.lo<=self.hi
    @staticmethod
    def rational(n,d=1):
        assert d>0
        return I((n*SCALE)//d,ceildiv(n*SCALE,d))
    def __add__(self,other):
        other=lift(other);return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-lift(other)
    def __rsub__(self,other):return lift(other)+-self
    def __mul__(self,other):
        if not isinstance(other,(I,int,Fraction)):return NotImplemented
        other=lift(other)
        p=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return I(min(p)//SCALE,ceildiv(max(p),SCALE))
    __rmul__=__mul__
    def inverse(self):
        assert self.lo>0 or self.hi<0
        return I((SCALE*SCALE)//self.hi,ceildiv(SCALE*SCALE,self.lo))
    def __truediv__(self,other):return self*lift(other).inverse()
    def __rtruediv__(self,other):return lift(other)*self.inverse()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I.rational(1)
        if n==1:return self
        if n%2==0:
            h=self**(n//2)
            if h.lo>=0:return I(h.lo*h.lo//SCALE,ceildiv(h.hi*h.hi,SCALE))
            if h.hi<=0:return I(h.hi*h.hi//SCALE,ceildiv(h.lo*h.lo,SCALE))
            return I(0,ceildiv(max(h.lo*h.lo,h.hi*h.hi),SCALE))
        return self*(self**(n-1))
    def abs_upper(self):return max(abs(self.lo),abs(self.hi))

def lift(x):
    if isinstance(x,I):return x
    if isinstance(x,int):return I.rational(x)
    if isinstance(x,Fraction):return I.rational(x.numerator,x.denominator)
    raise TypeError(type(x))

def positive_sqrt(x):
    assert x.lo>=0
    lo=isqrt(x.lo*SCALE); hi=isqrt(x.hi*SCALE)
    if hi*hi<x.hi*SCALE:hi+=1
    return I(lo,hi)

def log_reduced(u):
    # u encloses a point in [1,2], w in [0,1/3] up to outward roundoff.
    w=(u-1)/(u+1); w2=w*w; power=w; total=I.rational(0)
    for j in range(TERMS):
        total+=power/(2*j+1);power*=w2
    tail=2*power/((2*TERMS+1)*(1-w2))
    return I(2*total.lo,2*total.hi+tail.hi)

LN2=log_reduced(I.rational(2))

def point_log(m):
    assert m>0
    k=m.bit_length()-1-BITS
    if k>=0:u=I(m//(1<<k),ceildiv(m,1<<k))
    else:u=I(m<<(-k),m<<(-k))
    return log_reduced(u)+k*LN2

def ilog(x):
    assert x.lo>0
    return I(point_log(x.lo).lo,point_log(x.hi).hi)

def point_atan(m):
    assert 0<=m<=SCALE//2
    x=I(m,m);xx=x*x;term=x;total=I.rational(0)
    for j in range(TERMS):
        total=total+term/(2*j+1) if j%2==0 else total-term/(2*j+1)
        term*=xx
    # TERMS is even, so the truncated sum is a lower bound.
    assert TERMS%2==0
    return I(total.lo,total.hi+(term/(2*TERMS+1)).hi)

def iatan(x):
    assert 0<=x.lo<=x.hi<=SCALE//2
    return I(point_atan(x.lo).lo,point_atan(x.hi).hi)

def ixlogx(x):
    assert x.hi>=0
    lo=max(0,x.lo)
    if lo>0:return I(lo,x.hi)*ilog(I(lo,x.hi))
    if x.hi==0:return I.rational(0)
    if x.hi<=SCALE//4:
        z=I(x.hi,x.hi)*point_log(x.hi)
        return I(z.lo,0)
    # Global x log x >= -1; maximum on [0,h] is max(0,h log h).
    z=I(x.hi,x.hi)*point_log(x.hi)
    return I(-SCALE,max(0,z.hi))

@dataclass(frozen=True)
class D2:
    v:I
    d:I
    dd:I
    @staticmethod
    def constant(x):return D2(lift(x),lift(0),lift(0))
    @staticmethod
    def variable(x):return D2(x,lift(1),lift(0))
    def __add__(self,other):
        other=d_lift(other);return D2(self.v+other.v,self.d+other.d,self.dd+other.dd)
    __radd__=__add__
    def __neg__(self):return D2(-self.v,-self.d,-self.dd)
    def __sub__(self,other):return self+-d_lift(other)
    def __rsub__(self,other):return d_lift(other)+-self
    def __mul__(self,other):
        other=d_lift(other)
        return D2(self.v*other.v,self.d*other.v+self.v*other.d,self.dd*other.v+2*self.d*other.d+self.v*other.dd)
    __rmul__=__mul__
    def inverse(self):
        iv=1/self.v
        return D2(iv,-self.d*iv**2,2*self.d**2*iv**3-self.dd*iv**2)
    def __truediv__(self,other):return self*d_lift(other).inverse()
    def __rtruediv__(self,other):return d_lift(other)*self.inverse()
    def __pow__(self,n):
        if n==0:return D2.constant(1)
        if n==1:return self
        return D2(self.v**n,n*self.v**(n-1)*self.d,n*(n-1)*self.v**(n-2)*self.d**2+n*self.v**(n-1)*self.dd)

def d_lift(x):return x if isinstance(x,D2) else D2.constant(x)

def log(x):
    if not isinstance(x,D2):return ilog(x)
    return D2(ilog(x.v),x.d/x.v,x.dd/x.v-(x.d/x.v)**2)

def sqrt(x):
    if not isinstance(x,D2):return positive_sqrt(x)
    r=positive_sqrt(x.v)
    return D2(r,x.d/(2*r),x.dd/(2*r)-x.d**2/(4*r**3))

def atan(x):
    if not isinstance(x,D2):return iatan(x)
    f=1/(1+x.v*x.v)
    return D2(iatan(x.v),f*x.d,f*x.dd-2*x.v*f*f*x.d*x.d)

def xlogx(x):
    if not isinstance(x,D2):return ixlogx(x)
    assert x.v.lo>0
    return D2(ixlogx(x.v),(ilog(x.v)+1)*x.d,(ilog(x.v)+1)*x.dd+x.d*x.d/x.v)

def atanh(x):return (log(1+x)-log(1-x))/2

def kvalue(variable,left):
    A=Fraction(2,3)
    if left:
        q=variable;z=sqrt(4*A+q*q);D=q
    else:
        z=variable;q=sqrt(z*z-4*A);D=2-z
    b=2-z;k=sqrt(8*A-z*z);K=4*A
    c=Fraction(9,2)*z-12;e=4-z;C0=4-2*z+3*q;P1=-4+Fraction(5,2)*z
    u=atanh(D/z)
    R0=u/z;R1=-(log(1-(D/z)**2))/2
    R2=z*z*R0-D;R3=z*z*R1-D*D/2
    S0=D/(2*z*z*(z*z-D*D))+u/(2*z**3);S2=z*z*S0-R0
    v=(C0*(b*b*D-D**3/3)-Fraction(9,2)*(b*b*D*D/2-D**4/4))/4
    v+=K/4*(P1*(b*b*R0-R2)+Fraction(3,2)*(b*b*R1-R3))-z*K*K/8*(b*b*S0-S2)
    def lm(r,D):
        # Endpoint-safe expressions. r-D is known nonnegative by the domain.
        plus=r+D;minus=r-D
        if isinstance(minus,I):minus=I(max(0,minus.lo),max(0,minus.hi))
        fplus=xlogx(plus);fminus=xlogx(minus)
        L0=fplus-fminus-2*D
        L2=((r*r-r*D+D*D)*fplus-(r*r+r*D+D*D)*fminus)/3-2*r*r*D/3-2*D**3/9
        return L0,L2
    if left:
        Lq0=xlogx(2*q)-2*q
        Lq2=q*q*xlogx(2*q)/3-8*q**3/9
        Aq1=q*q/2;Aq3=q**4/3
    else:
        Lq0,Lq2=lm(q,D)
        minus=q-D
        if isinstance(minus,I):minus=I(max(0,minus.lo),max(0,minus.hi))
        Z=(q+D)*xlogx(minus)-minus*xlogx(q+D)
        Aq1=Z/4+q*D/2
        Aq3=(q*q+D*D)*Z/8+q**3*D/4+q*D**3/12
    Lz0,Lz2=lm(z,D)
    ell=log(lift(4*A)) if left else log(4*(1+2*A-z))
    angle=atan(D/k)
    Lk0=D*ell-2*D+2*k*angle
    Lk2=D**3*ell/3-2*D**3/9+2*k*k*D/3-2*k**3*angle/3
    v+=(c*(b*b*Lq0-Lq2)+e*(b*b*Lk0-Lk2)-(c+e)*(b*b*Lz0-Lz2))/4
    Az0=D*u-z*R1;Az2=D**3*u/3-z*(z*z*R1-D*D/2)/3
    v+=-Fraction(3,4)*(b*b*Aq1-Aq3)+3*z/4*(b*b*Az0-Az2)
    return v*q/z if left else v

def integrate(n):
    total=lift(0);range_cells=0;max_second=0
    width=I.rational(1,3*n)
    for left in [True,False]:
        for j in range(n):
            offset=0 if left else 5*n
            interval=I((offset+j)*SCALE//(3*n),ceildiv((offset+j+1)*SCALE,3*n))
            if j==0:
                # The outer endpoint is integrable but its displayed second
                # derivative need not stay bounded on the entire first cell.
                value=kvalue(interval,left)*width
                range_cells+=1
            else:
                derivatives=kvalue(D2.variable(interval),left)
                max_second=max(max_second,derivatives.dd.abs_upper())
                middle=I.rational(2*(offset+j)+1,6*n)
                value=kvalue(middle,left)*width
                # integral midpoint remainder <= sup |f''| width^3 /24.
                error=ceildiv(derivatives.dd.abs_upper(),24*(3*n)**3)
                value=I(value.lo-error,value.hi+error)
            total+=value
    return total,range_cells,max_second

def f3_certificate(n):
    integral,range_cells,second=integrate(n)
    pi=16*iatan(I.rational(1,5))-4*iatan(I.rational(1,239))
    pi2=pi*pi
    answer=1-lift(Fraction(483,80))/pi2+9*integral/pi2
    return answer,integral,{'midpoint_cells':2*n-range_cells,'range_cells':range_cells,'maximum_interval_second_derivative_upper':str(Fraction(second,SCALE))}

if __name__=='__main__':
    p=ArgumentParser(description=__doc__);p.add_argument('--grid',type=int,default=128);p.add_argument('--output',type=Path)
    args=p.parse_args();start=perf_counter()
    answer,integral,detail=f3_certificate(args.grid)
    result={'scope':'Rigorous integer-directed interval arithmetic and proved midpoint remainder. No ordinary floating arithmetic enters the enclosure.','a':'1/3','binary_scale_bits':BITS,'elementary_series_terms':TERMS,'grid_per_branch':args.grid,'F3_interval':{'lower':str(Fraction(answer.lo,SCALE)),'upper':str(Fraction(answer.hi,SCALE)),'display':[float(Fraction(answer.lo,SCALE)),float(Fraction(answer.hi,SCALE))],'width':str(Fraction(answer.hi-answer.lo,SCALE))},'integral_interval':{'lower':str(Fraction(integral.lo,SCALE)),'upper':str(Fraction(integral.hi,SCALE))},'details':detail,'elapsed_seconds':perf_counter()-start}
    dec=10**9
    lo=answer.lo*dec//SCALE; hi=ceildiv(answer.hi*dec,SCALE)
    result['F3_interval']['outward_decimal_9']=[f'{lo//dec}.{lo%dec:09d}',f'{hi//dec}.{hi%dec:09d}']
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
