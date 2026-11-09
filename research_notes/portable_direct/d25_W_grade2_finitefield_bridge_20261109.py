"""Exact original 216 grade-2 finite-field transfer regression.
Author-side research code: no native H0/B0 result or Source admission.
"""
from math import comb

def primes_to(n):
    sieve=bytearray([1])*(n+1)
    sieve[:2]=b'\0\0'
    for k in range(2,int(n**0.5)+1):
        if sieve[k]:
            sieve[k*k:n+1:k]=b'\0'*((n-k*k)//k+1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]

def direct(p):
    m=(p-1)//6; M=p**3; inv=pow(216,-1,M); total=0
    for n in range(3*m+1,4*m+1):
        v=comb(2*n,n)**2*comb(3*n,n)
        total+=(6*n+1)*(v%M)*pow(inv,n,M)
    total%=M
    assert total%(p*p)==0
    return total//(p*p)

def recurrence(p):
    m=(p-1)//6; M=p**3; a=1; total=0
    for n in range(4*m+1):
        if 3*m+1<=n<=4*m:
            assert a%(p*p)==0
            total=(total+(6*n+1)*a)%M
        if n<4*m:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,M)%M
    assert total%(p*p)==0
    return total//(p*p)

def finite_poly(p):
    m=(p-1)//6; N=m-1; n0=3*m+1; fac=1
    for i in range(1,n0+1): fac=fac*i%p
    K=(3*m+2)*pow(fac,-4,p)*pow(216,-n0,p)%p
    t=1; H=0
    for j in range(N+1):
        H=(H+(6*j+4)*t)%p
        if j<N:
            # 2(j+3/2)^3 == (2j+3)^3/4 in F_p
            den=pow(2*j+3,3,p)*pow(4,-1,p)%p
            t=t*(j-N)*(j+N+2)*(j+1)*pow(den,-1,p)%p
    return K,H,K*H%p

def run(limit=1000):
    out={}
    for p in primes_to(limit):
        a=direct(p); b=recurrence(p); k,h,c=finite_poly(p)
        assert a==b==c,(p,a,b,k,h,c)
        out[p]=(k,h,c)
    return out

if __name__=="__main__":
    r=run()
    print("PASS:",len(r),"p == 1 (mod 6) primes through 1000")
    for p in (7,13,19,37,43,73,373,379,997):
        if p in r: print(p,r[p])
