#!/usr/bin/env python3
"""Certified fixed-point interval computation, Python stdlib only.

Checks one strictly non-trivial Chernoff-efficiency crossing for the frozen
paired BRC S23 experiment h=1/42, with correct optimized Bernoulli Chernoff.
All interval endpoints are integer multiples of 10^-70; every operation rounds
outward. There are no floating-point calculations or optimizer guesses used
as proof of a sign.
"""
from math import isqrt
from fractions import Fraction

Q=10**70

def updiv(a,b):
    assert b>0
    return -((-a)//b)

class I:
    __slots__ = ('l','u')
    def __init__(self,l,u):
        assert isinstance(l,int) and isinstance(u,int) and l<=u
        self.l,self.u=l,u
    @classmethod
    def rat(cls,n,d=1):
        if isinstance(n,Fraction): n,d=n.numerator,n.denominator
        elif isinstance(n,I): return n
        elif isinstance(n,str):
            return cls.rat(Fraction(n))
        elif isinstance(n,int): pass
        else: raise TypeError(type(n))
        assert d>0
        return cls(n*Q//d,updiv(n*Q,d))
    def __add__(self,other):
        b=I.rat(other); return I(self.l+b.l,self.u+b.u)
    __radd__=__add__
    def __neg__(self): return I(-self.u,-self.l)
    def __sub__(self,other): return self+-I.rat(other)
    def __rsub__(self,other): return I.rat(other)+(-self)
    def __mul__(self,other):
        b=I.rat(other)
        xs=(self.l*b.l,self.l*b.u,self.u*b.l,self.u*b.u)
        return I(min(xs)//Q,updiv(max(xs),Q))
    __rmul__=__mul__
    def __truediv__(self,other):
        b=I.rat(other)
        assert b.l>0
        xs=(self.l*Q//b.l,self.l*Q//b.u,self.u*Q//b.l,self.u*Q//b.u)
        # More robust for negative: compute original endpoints with floor/ceil for each quotient.
        ps=(self.l*Q,self.u*Q)
        lows=[a//den for a in ps for den in (b.l,b.u)]
        highs=[updiv(a,den) for a in ps for den in (b.l,b.u)]
        return I(min(lows),max(highs))
    def __rtruediv__(self,other): return I.rat(other)/self
    def __repr__(self):
        return f'[{Fraction(self.l,Q)}, {Fraction(self.u,Q)}]'
    def readable(self,places=25):
        m=10**places
        return f'[{self.l*m//Q/float(m):.{min(places,17)}g}, {updiv(self.u*m,Q)/float(m):.{min(places,17)}g}]' if places<=17 else f'[{self.l* m//Q}e-{places}, {updiv(self.u*m,Q)}e-{places}]'
    def width(self): return self.u-self.l

ZERO=I.rat(0);ONE=I.rat(1)

def sqrt_i(x):
    x=I.rat(x);assert x.l>=0
    def root(v): return isqrt(v*Q)
    lo=root(x.l);hi=root(x.u)
    return I(lo, hi if hi*hi <= x.u*Q and hi*hi == x.u*Q else hi+1)

def atanh_pos(x, N=32):
    x=I.rat(x)
    assert 0<=x.l<=x.u<Q//2
    v=x; sq=x*x; total=ZERO
    for k in range(N):
        total=total+v/(2*k+1)
        v=v*sq
    # remainder sum from k=N, k>=N:  <= x^(2N+1)/[(2N+1)*(1-x^2)]
    R=v/((2*N+1)*(ONE-sq))
    return I(total.l,total.u+R.u)

def exp_pos(x, N=35):
    x=I.rat(x)
    assert 0<=x.l<=x.u<Q//8
    t=ONE;total=t
    for k in range(1,N+1):
        t=t*x/k
        total=total+t
    # tail from k=N+1 and ratio <= x/(N+2)
    rem=(t*x/(N+1))/(ONE-x/(N+2))
    return I(total.l,total.u+rem.u)

def exp_i(x):
    x=I.rat(x)
    if x.l>=0: return exp_pos(x)
    if x.u<=0: return ONE/exp_pos(-x)
    return I(min((ONE/exp_pos(I(0,-x.l))).l,ONE.l), max(ONE.u,exp_pos(I(0,x.u)).u))

def log_below_one(z):
    z=I.rat(z)
    assert 0<z.l and z.u<=Q
    return -2*atanh_pos((ONE-z)/(ONE+z))

def approx_str(i, places=34):
    return f'[{i.l*10**places//Q}/10^{places}, {updiv(i.u*10**places,Q)}/10^{places}]'

def E_data(s,h=Fraction(1,42)):
    s=I.rat(s);h=I.rat(h)
    u=s/2;v=1-u;d=s*h
    k=sqrt_i(ONE/4-h*h)
    X=s*k
    Y=sqrt_i(v*v-d*d)
    alpha=atanh_pos(2*h)
    gamma=atanh_pos(d/v)
    T=ONE-s+s*sqrt_i(ONE-4*h*h)
    logT=log_below_one(T)
    E=exp_i(logT/(2-s))
    return s,h,k,X,Y,alpha,gamma,T,logT,E

def coeff_G(data,delta):
    _,_,k,X,Y,a,g,_,_,_=data
    delta=I.rat(delta)
    ea=exp_i(delta*a)
    eg=exp_i(-delta*g)
    return X*ea+Y*eg

def deriv_G(data,delta):
    _,_,k,X,Y,a,g,_,_,_=data
    delta=I.rat(delta)
    return X*a*exp_i(delta*a)-Y*g*exp_i(-delta*g)

def certify_root_endpoint(s_text,delta_text,r_text,side):
    s=Fraction(s_text); d0=Fraction(delta_text); radius=Fraction(r_text)
    d=data=E_data(s)
    E=d[-1]
    center=coeff_G(d,d0)
    dleft=deriv_G(d,d0-radius)
    dright=deriv_G(d,d0+radius)
    assert dleft.u<0,('left derivative sign',s_text,dleft.readable(15))
    assert dright.l>0,('right derivative sign',s_text,dright.readable(15))
    assert 0<d0-radius<d0+radius<1
    max_slope=max(-dleft.l,dright.u)
    gap=I.rat(radius)*I(0,max_slope)
    if side=='LEFT':
        assert center.u<E.l, ('F-negative test',center.readable(30),E.readable(30))
        diff_lo=E.l-center.u
    elif side=='RIGHT':
        assert center.l-gap.u>E.u, ('F-positive test',center.readable(30),E.readable(30),gap.readable(30))
        diff_lo=center.l-gap.u-E.u
    else: raise ValueError(side)
    print(side,'s=',s_text,'optimizer in',str(d0-radius),str(d0+radius), 'certified E/G gap lower integer units', diff_lo)
    return s

def main():
    # root at 0.102439024438...; use narrower-than-1e-10 rational bracketing.
    left=Fraction('0.10243902443');right=Fraction('0.10243902445')
    # δ0 values are rational search points only; their admissibility is proved by derivative signs.
    certify_root_endpoint(str(left),'0.00751349463555','0.00000000003','LEFT')
    certify_root_endpoint(str(right),'0.00751349463546','0.00000000003','RIGHT')
    print('PASS_BRC_S23_CHERNOFF_FINITE_H_RATIONAL_ROOT_BRACKET_20261104')

if __name__=='__main__':main()


def certify_monotonic_on_interval():
    # Envelope theorem on the exact Bernoulli Chernoff minimizer.  The
    # logarithm in the optimizer is evaluated as 2*atanh((r-1)/(r+1)).
    L=Fraction('0.10243902443');R=Fraction('0.10243902445')
    s=I(I.rat(L).l,I.rat(R).u)
    dat=E_data(s)
    _,h,k,X,Y,alpha,gamma,T,logT,_=dat
    ratio=Y*gamma/(X*alpha)
    assert ratio.l>Q and (ratio-ONE).u<(ratio+ONE).l//2
    delta=2*atanh_pos((ratio-ONE)/(ratio+ONE))/(alpha+gamma)
    assert 0<delta.l and delta.u<Q, 'Chernoff optimizer stays interior'
    va=exp_i(delta*alpha); vg=exp_i(-delta*gamma)
    G=X*va+Y*vg
    v=ONE-s/2
    Ys=(-v/2-s*h*h)/Y
    gamma_s=4*h/((2-s)*(2-s)-4*s*s*h*h)
    Gs=k*va+(Ys-Y*delta*gamma_s)*vg
    Ts=sqrt_i(ONE-4*h*h)-ONE
    Fs=Gs/G-Ts/(T*(2-s))-logT/((2-s)*(2-s))
    assert Fs.l>0, ('F derivative interval', Fs.readable(25))
    print('OPTIMIZED_C_CHERNOFF_DERIVATIVE_CERTIFIED_POSITIVE',
          'interval lower bound=',f'{Fs.l*10**15//Q}/10^15',
          'upper bound=',f'{updiv(Fs.u*10**15,Q)}/10^15')

if __name__=='__main__':
    certify_monotonic_on_interval()
    print('PASS_BRC_S23_CHERNOFF_FINITE_H_LOCAL_UNIQUE_ROOT_20261104')
