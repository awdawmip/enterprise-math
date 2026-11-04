"""D25 exact finite Green-adjoint signed transport.
Original 216/2304 coefficient sources; modular arithmetic only.
This verifies finite inputs and is not a universal bridge proof.
"""
import json
from math import isqrt
from fractions import Fraction
from math import factorial

def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))

def pfree_factorials(p, maxn, mod):
    f=[1]*(maxn+1)
    for k in range(1,maxn+1):
        x=k
        while x%p == 0:
            x//=p
        f[k]=f[k-1]*x%mod
    return f

def coef(p,mod,f,n,family):
    if family=="A":
        v=(2*n)//p+(3*n)//p
        if v>=3:
            return 0
        return pow(p,v,mod)*f[2*n]*f[3*n]*pow(
            f[n]**5*pow(216,n,mod)%mod,-1,mod)%mod
    v=4*n//p
    if v>=3:
        return 0
    return pow(p,v,mod)*f[4*n]*pow(
        f[n]**4*pow(2304,n,mod)%mod,-1,mod)%mod

def check(p):
    assert is_prime(p) and p>=5
    mod=p**3; N=p-1
    inv288=pow(288,-1,mod); inv576=pow(576,-1,mod)
    factorials=pfree_factorials(p,4*N,mod)
    a=[coef(p,mod,factorials,n,"A") for n in range(p)]
    b=[coef(p,mod,factorials,n,"B") for n in range(p)]
    forcing=[]
    for j in range(N):
        rb=(4*j+1)*(4*j+2)*(4*j+3)*inv576*pow(j+1,-3,mod)%mod
        fj=a[j]*(2*j+1)*(56*j*(j+1)+13)*inv288*pow(j+1,-3,mod)%mod
        assert (a[j+1]-rb*a[j]-fj)%mod==0,(p,j,"forward")
        forcing.append(fj)
    K=[0]*N
    K[-1]=6*N+1
    for j in range(N-2,-1,-1):
        n=j+1
        rb=(4*n+1)*(4*n+2)*(4*n+3)*inv576*pow(n+1,-3,mod)%mod
        K[j]=(6*(j+1)+1+rb*K[j+1])%mod
    band=[0,0,0,0]
    for j in range(N):
        valuation=2*j//p+3*j//p
        band[min(valuation,3)]=(band[min(valuation,3)]+forcing[j]*K[j])%mod
    thetaB=sum(n*b[n] for n in range(p))%mod
    direct=sum((6*n+1)*a[n]-(8*n+1)*b[n] for n in range(p))%mod
    response=(sum(band)-2*thetaB)%mod
    assert response==direct,(p,"signed Green",response,direct)
    assert sum(band)%mod==sum((6*n+1)*(a[n]-b[n]) for n in range(p))%mod
    if p%6==1:
        h=(p-1)//2
        normalized=(forcing[h]//(p*p))%p
        chi=1 if pow(6,(p-1)//2,p)==1 else -1
        assert forcing[h]%(p*p)==0
        assert normalized==chi*pow(18,-1,p)%p,(p,"seam")
    return {"p":p,"mod":mod,"green_bands":band,"twice_quartic_theta":2*thetaB%mod,
            "direct_signed":direct,"green_signed":response}

def exact_fraction_check(p):
    A=[Fraction(factorial(2*n)*factorial(3*n),factorial(n)**5*216**n)
       for n in range(p)]
    B=[Fraction(factorial(4*n),factorial(n)**4*2304**n)
       for n in range(p)]
    f=[A[j]*Fraction((2*j+1)*(56*j*(j+1)+13),288*(j+1)**3)
       for j in range(p-1)]
    K=[sum((6*n+1)*B[n]/B[j+1] for n in range(j+1,p))
       for j in range(p-1)]
    assert sum(f[j]*K[j] for j in range(p-1))==sum(
        (6*n+1)*(A[n]-B[n]) for n in range(p))
    return p

if __name__=="__main__":
    samples=[check(p) for p in (5,7,11,13,19,37,373)]
    tested=[check(p) for p in range(7,2001) if p%6==1 and is_prime(p)]
    assert len(tested)==148
    print(json.dumps({"exact_fraction_primes":[exact_fraction_check(p) for p in (13,19)],
       "finite_primes":len(tested),"nonzero_bridges_in_range":sum(bool(x["direct_signed"]) for x in tested),
       "samples":samples},indent=2))
