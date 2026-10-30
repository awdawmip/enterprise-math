"""Exact source-labeled A216/B2304 finite-endpoint checks. No native H0/B0 claim."""
from fractions import Fraction
from math import comb, factorial


def prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1 if d == 2 else 2
    return True


def exact_boundary(N):
    a = [Fraction(comb(2*n,n)**2*comb(3*n,n),216**n) for n in range(N+1)]
    b = [Fraction(comb(2*n,n)**2*comb(4*n,2*n),2304**n) for n in range(N+1)]
    ia = sum((18*n**3-27*n**2-13*n-2)*v for n,v in enumerate(a))
    ib = sum((512*n**3-96*n**2-44*n-6)*v for n,v in enumerate(b))
    assert ia == -(2*N+1)*(3*N+1)*(3*N+2)*a[-1]
    assert ib == -(4*N+1)*(4*N+2)*(4*N+3)*b[-1]


def check_prime(p):
    mod=p**4
    fac=[1]*(4*p-3)
    for n in range(1,len(fac)):
        fac[n]=fac[n-1]*n%mod
    invfac=[0]*p
    invfac[-1]=pow(fac[-1 if False else p-1],-1,mod)
    for n in range(p-1,0,-1):
        invfac[n-1]=invfac[n]*n%mod
    x=y=1
    inv216=pow(216,-1,mod)
    inv2304=pow(2304,-1,mod)
    A=[0]*4
    B=[0]*4
    ae=be=0
    for n in range(p):
        inv=invfac[n]
        a=fac[2*n]*fac[3*n]*pow(inv,5,mod)*x%mod
        b=fac[4*n]*pow(inv,4,mod)*y%mod
        for j in range(4):
            A[j]=(A[j]+pow(n,j,mod)*a)%mod
            B[j]=(B[j]+pow(n,j,mod)*b)%mod
        if n==p-1:
            ae,be=a,b
        x=x*inv216%mod
        y=y*inv2304%mod
    assert ae//p**3==be//p**3==p-1
    ia=(18*A[3]-27*A[2]-13*A[1]-2*A[0])%mod
    ib=(512*B[3]-96*B[2]-44*B[1]-6*B[0])%mod
    assert ia==(-2*p**3)%mod
    assert ib==(-6*p**3)%mod
    assert (3*ia-ib)%mod==0
    assert (ae-be)%mod==0
    return (p,ia//p**3,ib//p**3,ae//p**3,be//p**3)


def independent_endpoint(p):
    n=p-1
    mod=p**4
    a=comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod)%mod
    b=comb(2*n,n)**2*comb(4*n,2*n)*pow(2304,-n,mod)%mod
    assert a//p**3==b//p**3==p-1


if __name__=="__main__":
    for N in range(9):
        exact_boundary(N)
    for p in (5,7,11,13,19,31):
        for r in range(2,min(p,6)):
            assert (factorial(r*(p-1))//p**(r-1))%p==p-1
    primes=[p for p in range(5,1500) if prime(p)]
    for p in primes:
        check_prime(p)
    for p in (5,7,13,19,373):
        independent_endpoint(p)
        print("ENDPOINT",check_prime(p))
    print("EXACT_RATIONAL_N_0_TO_8_PASS")
    print("GENERAL_FACTORIAL_R_2_TO_5_SMALL_PRIMES_PASS")
    print("P4_ALL_PRIMES_5_TO_1499",len(primes))
    print("TARGET_CLASSES",sum(p%24 in (13,19) for p in primes))
    print("PASS_JOINT_ENDPOINT_AND_MOMENT_BOUNDARIES")
