"""D25 signed 216/2304 two-variable tangent; author-side exact checks.
Use: python d25_affine_two_variable_tangent_reproducer_20261109.py
"""
from math import comb, isqrt

def primes(n):
    sieve = bytearray(b'\1') * n
    sieve[:2] = b'\0\0'
    for k in range(2, isqrt(n - 1) + 1):
        if sieve[k]:
            sieve[k*k:n:k] = b'\0' * ((n-1-k*k)//k+1)
    return [p for p in range(5, n) if sieve[p]]

def streams(p, modulus):
    a=b=1; w=v=dw=dv=0
    for n in range(p):
        w=(w+(6*n+1)*a)%modulus
        v=(v+(8*n+1)*b)%modulus
        dw=(dw+n*(6*n+1)*a)%modulus
        dv=(dv+n*(8*n+1)*b)%modulus
        if n+1<p:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,modulus)%modulus
            b=b*(2*n+1)*(4*n+1)*(4*n+3)*pow(288*(n+1)**3,-1,modulus)%modulus
    return w,v,dw,dv

def literal(p, modulus, x=1, y=1):
    iw=pow(216,-1,modulus);iv=pow(2304,-1,modulus)
    w=v=dw=dv=0
    for n in range(p):
        a=comb(2*n,n)**2*comb(3*n,n)*pow(iw,n,modulus)%modulus
        b=comb(4*n,2*n)*comb(2*n,n)**2*pow(iv,n,modulus)%modulus
        w=(w+(6*n+1)*a*pow(x,n,modulus))%modulus
        v=(v+(8*n+1)*b*pow(y,n,modulus))%modulus
        dw=(dw+n*(6*n+1)*a)%modulus
        dv=(dv+n*(8*n+1)*b)%modulus
    return w,v,dw,dv

for p in primes(4000):
    _,_,a,b=streams(p,p)
    chi=1 if p%3==1 else -1
    assert (3*a+8*chi*b)%p==0,('tangent counterexample',p,a,b)

for p in (5,7,13,19,37,43,73,373):
    mod=p*p;chi=1 if p%3==1 else -1
    w,v,a,b=streams(p,mod)
    assert (w,v,a,b)==literal(p,mod)
    assert (w-2*v+p*chi)%mod==0
    slope=(-4*chi*pow(3,-1,p))%p
    for yy in (1+p,1+p*slope):
        wa,vb,*_=literal(p,mod,1+p,yy)
        predicted=(w-2*v+p*chi+p*(a-2*((yy-1)//p)*b))%mod
        assert (wa-2*vb+p*chi)%mod==predicted
    if p in (13,19,373):
        mod=p**3
        v0=(-4*chi*pow(3,-1,p))%p
        wa,vb,*_=literal(p,mod,1+p,1+p*v0)
        defect=((wa-2*vb+p*chi)%mod)//(p*p)
        w2=defect*pow(2*(b%p),-1,p)%p
        w3,v3,*_=literal(p,mod,1+p,1+p*v0+p*p*w2)
        assert (w3-2*v3+p*chi)%mod==0
        print('SECOND_JET',p,'slope',v0,'defect',defect,'lift',w2)
print('PASS',len(primes(4000)),'primes, 8 independently verified binomial anchors')
