"""Exact author checks for corrected Clausen high Hasse port and p^2 tail.

Finite arithmetic only; neither native CM evidence nor theorem admission.
"""
from math import factorial

def primes_upto(n):
    out=[]
    for x in range(7,n+1):
        if x%6==1 and all(x%d for d in range(2,int(x**0.5)+1)):
            out.append(x)
    return out

def linear_product(factors,degree,mod):
    a=[1]+[0]*degree
    for v,w in factors:
        for k in range(degree,0,-1):
            a[k]=(v*a[k]+w*a[k-1])%mod
        a[0]=v*a[0]%mod
    return a

def forcing(p,precision,degree):
    m,n,mod=(p-1)//6,p-1,p**precision
    numerator=linear_product(
        [(i-m,-1) for i in range(p)]
        +[(i-2*m,-2) for i in range(p)],degree,mod)
    denominator=linear_product(
        [(2*j-p,-6) for j in range(1,p)],degree,mod)
    scale=pow(2,n,mod)*pow(factorial(n),-1,mod)%mod
    inv=pow(denominator[0],-1,mod)
    out=[0]*(degree+1)
    for k in range(degree+1):
        term=sum(denominator[j]*out[k-j] for j in range(1,k+1))
        out[k]=(scale*numerator[k]-term)*inv%mod
    return out

def high_formula(p):
    m,n,mod=(p-1)//6,p-1,p*p
    a=2*(-1)**m*factorial(m)*factorial(5*m)*factorial(2*m)*factorial(4*m)
    a=a*pow(factorial(n)**2,-1,mod)%mod
    q2=((2**n-1)//p)%p
    q3=((3**n-1)//p)%p
    w=((factorial(n)+1)//p)%p
    hm=sum(pow(j,-1,mod) for j in range(1,m+1))
    h2m=sum(pow(j,-1,mod) for j in range(1,2*m+1))
    return a,a*(1+p*(q2-q3+w-hm-h2m))%mod

def main():
    ps=primes_upto(373)
    assert len(ps)==35
    checks=0
    for p in ps:
        degree=2*p+8 if p<=103 else p+5
        coef=forcing(p,2,degree)
        a,high=high_formula(p)
        assert -coef[2]%(p*p)==-a%(p*p),(p,"J2")
        assert -coef[p+1]%(p*p)==high,(p,"Jp+1")
        assert all(coef[k]%(p*p)==0 for k in range(p+2,degree+1)),p
        checks+=degree-p-1
    assert forcing(7,3,9)[9]==196
    assert checks==806
    print("PASS primes=35 high_port_formula=35 beyond_p_plus_one_zero_mod_p2="
        +str(checks)+" p7_t9_unsigned_mod343=196 AUTHOR_CHECKED_NOT_ADMITTED")

if __name__=="__main__":
    main()
