#!/usr/bin/env python3
"""Exact finite-ring certificate for D25 prime-square Clausen/Euler folding.

All arithmetic is integral modulo p^e; output is author-side finite evidence.
"""
from math import isqrt, comb

def primes_below(n):
    for p in range(5, n):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p

def coefficients(p, e, params, stop=None):
    mod = p**e
    if stop is None: stop = p - 1
    v, out = 1, [1]
    denom_const = 1
    for a, _ in params: denom_const *= a
    for n in range(stop):
        numerator = 1
        for a, b in params: numerator *= a*n+b
        denominator = denom_const*(n+1)**len(params)
        v = v*numerator*pow(denominator,-1,mod)%mod
        out.append(v)
    return out

def square(c, p, euler=False):
    mod=p*p; out=[0]*p
    for i,a in enumerate(c):
        if a%mod==0: continue
        for j,b in enumerate(c[:p-i]):
            out[i+j]=(out[i+j]+a*b)%mod
    if euler:
        return [(out[n]-(out[n-1] if n else 0))%mod for n in range(p)]
    return out

def value(c,z,mod):
    total=0; zpow=1
    for a in c:
        total=(total+a*zpow)%mod
        zpow=zpow*z%mod
    return total

def derivative(c,z,mod):
    return sum(n*a*pow(z,n-1,mod) for n,a in enumerate(c) if n)%mod

def raw_binomial_value(p,base,mod):
    t=0
    for n in range(p):
        if base=="A":
            c=comb(2*n,n)**2*comb(3*n,n)
            t+=c*pow(216,-n,mod)
        else:
            c=comb(2*n,n)**2*comb(4*n,2*n)
            t+=c*pow(2304,-n,mod)
    return t%mod

def main():
    poly={"A":0,"B3":0,"B5":0}
    for p in primes_below(250):
        if p%6==1:
            m=(p-1)//6
            a=coefficients(p,2,[(2,1),(3,1),(3,2)])
            f=coefficients(p,2,[(6,1),(3,1)],2*m)
            assert a==square(f,p),("A",p)
            poly["A"]+=1
        if p%8==3:
            k=(p-3)//8
            b=coefficients(p,2,[(4,1),(2,1),(4,3)])
            g=coefficients(p,2,[(8,1),(8,3)],3*k+1)
            assert b==square(g,p),("B3",p)
            poly["B3"]+=1
        if p%8==5:
            k=(p-5)//8
            b=coefficients(p,2,[(4,1),(2,1),(4,3)])
            h=coefficients(p,2,[(8,5),(8,7)],3*k+1)
            assert b==square(h,p,euler=True),("B5",p)
            poly["B5"]+=1
    count={"13":0,"19":0}; examples={}
    for p in primes_below(3000):
        if p%24 not in (13,19): continue
        mod=p*p; m=(p-1)//6
        k=(p-5)//8 if p%8==5 else (p-3)//8
        f=coefficients(p,2,[(6,1),(3,1)],2*m)
        g=coefficients(p,2,[(8,5),(8,7)] if p%8==5 else [(8,1),(8,3)],3*k+1)
        a=coefficients(p,2,[(2,1),(3,1),(3,2)])
        b=coefficients(p,2,[(4,1),(2,1),(4,3)])
        xa=pow(2,-1,mod); xb=pow(9,-1,mod)
        F=value(f,xa,mod); H=value(g,xb,mod)
        assert F%p==H%p==0,("CM roots",p)
        A=value(a,xa,mod); B=value(b,xb,mod)
        assert A==B==0,("unweighted p2",p)
        assert F*F%mod==A,("A scalar",p)
        assert ((1-xb) if p%8==5 else 1)*H*H%mod==B,("B scalar",p)
        J=sum(n*x*pow(xa,n,mod) for n,x in enumerate(a))%mod
        K=sum(n*x*pow(xb,n,mod) for n,x in enumerate(b))%mod
        W=(A+6*J)%mod; V=(B+8*K)%mod
        assert W%p==V%p==0
        assert W//p%p == 6*(F//p)*derivative(f,xa,mod)%p,("A first",p)
        coef=(128*pow(81,-1,p) if p%8==5 else 16*pow(9,-1,p))%p
        assert V//p%p==coef*(H//p)*derivative(g,xb,mod)%p,("B first",p)
        assert V//p%p==1,("GZ digit",p)
        beta=(81*pow(128,-1,p) if p%8==5 else 9*pow(16,-1,p))%p
        assert (H//p)*derivative(g,xb,mod)%p==beta,("B CM digit",p)
        count[str(p%24)]+=1
        if p in (13,19,37,43,67,373):
            A3=value(coefficients(p,3,[(2,1),(3,1),(3,2)]),pow(2,-1,p**3),p**3)
            B3=value(coefficients(p,3,[(4,1),(2,1),(4,3)]),pow(9,-1,p**3),p**3)
            assert A3==raw_binomial_value(p,"A",p**3)
            assert B3==raw_binomial_value(p,"B",p**3)
            examples[p]={"A_over_p2_mod_p":A3//p**2,"B_over_p2_mod_p":B3//p**2}
    print("POLYNOMIAL_P2_FOLD",poly)
    print("TARGET_P2_ROOT_ZERO",count)
    print("INDEPENDENT_BINOMIAL_P3_WITNESSES",examples)
    print("PASS")

if __name__=="__main__":
    main()
