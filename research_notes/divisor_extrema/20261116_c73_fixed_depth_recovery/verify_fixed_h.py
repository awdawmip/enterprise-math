"""Jacobian and dyadic linear coefficients for the fixed single original H."""
import sympy as sp
from fractions import Fraction as Q
from math import prod

def inverse_coeff(n,v,k):
    return Q((v+k-1)*prod(range(n+k+1,n+4*k+1)),28*(4*v+k-1)*prod(range(v+k,v+4*k)))

def derivatives(gaps):
    n=sum(gaps)+2; rates=[]
    for i,m in enumerate(gaps[:-1]):
        k=2*(len(gaps)-1-i)+1
        rates.append(inverse_coeff(n,n-m,k));n-=m
    W=Q((n+2)*(n+3)*(n+4),840)
    def term(j,uj,index):
        z=1/(1+j*W); h=z*W/uj if index==len(rates) else 0
        for i in reversed(range(len(rates))):
            v=z
            z=1/(1+rates[i]*z)
            h=-rates[i]*h*z*z+(v*z if i==index else 0)
        return h/z
    return [term(Q(1,2),6,i)-term(Q(5),Q(3,32),i) for i in range(len(rates)+1)]

def check_rank():
    x=sp.symbols('x:3',positive=True); s=[z**4 for z in x]; x0=(1,*x); s0=(1,*s)
    real,dr,center,dc=0,1,0,1
    for i in (3,2,1):
        d=3*(2*(3-i+1)+1)
        rate=4*(x0[i]/x0[i-1])**d
        scale=sp.Rational(7,16)*rate**5
        a=rate/scale
        dr=dr*scale*(1-rate)/(1+scale*real)**2
        real=(rate+scale*real)/(1+scale*real)
        dc=-dc*a/(1+a*center)**2
        center=1/(1+a*center)
    G=dr*x[-1]**-3/real; C= -dc*x[-1]**-12/center
    unit=112
    a1=(1/s[0])**21/unit; a2=(s[0]/s[1])**15/unit; a3=(s[1]/s[2])**9/unit
    compact= a1*a2*a3/(s[2]**3*(1+a2)*(1+a2+a1))
    subst=dict(zip(x,map(sp.Rational,['6/7','11/15','5/8'])))
    assert C.subs(subst)==compact.subs(subst)
    p=1000000007
    for L in [s0[i]-s0[i+1] for i in range(3)]+[s[-1]]:
        D=sp.Matrix([[f.diff(t).subs(subst) for t in x] for f in [G,C,L]])
        val=sp.factor(D.det());n,d=val.as_numer_denom()
        yield int(n)*pow(int(d),-1,p)%p

if __name__=='__main__':
    cert=list(check_rank());assert all(cert)
    # same adic coefficients, two separated tails
    ex=derivatives((20,43,51,66));assert all(ex)
    print('rank determinants mod 1000000007:',cert)
    print('nonzero logarithmic derivatives of the centered ratio:',[bool(x) for x in ex])
