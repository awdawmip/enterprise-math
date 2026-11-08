"""Exact mod-p^2 Wilson–harmonic lift in original W216 and V2304 grade-one bands.
Standard Python integers; portable only, not native H0/B0.
Usage: python d25_lower_grade_wilson_harmonic_check_20261108.py [prime_bound]
"""
from math import comb, isqrt
import sys

def primes_upto(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * (((limit-d*d)//d)+1)
    return [p for p in range(5,limit+1) if sieve[p]]

def grade_one(p, model):
    mod = p*p
    factorial = [1]*p
    for n in range(1,p):
        factorial[n] = factorial[n-1]*n % mod
    wilson = ((factorial[p-1]+1) % mod)//p
    assert (factorial[p-1]+1) % p == 0
    harmonic = [0]*p
    for a in range(1,p):
        harmonic[a] = (harmonic[a-1]+pow(a,-1,p))%p
    if model == "W216":
        left,right,weight,degree,denom=(p+2)//3,(p-1)//2,6,3,216
    else:
        assert model=="V2304"
        left,right,weight,degree,denom=(p+3)//4,(p-1)//2,8,4,2304
    invfac=[pow(x,-1,mod) for x in factorial]
    pw=pow(denom,-left,mod)
    pw3=pow(denom,-left,p**3)
    base_sum=harm_sum=direct=0
    for n in range(left,right+1):
        a=degree*n-p
        assert 0<=a<p and n<p
        base=(-(weight*n+1)*factorial[a]*
              (factorial[2*n] if model=="W216" else 1)*
              invfac[n]**(5 if model=="W216" else 4)*pw)%mod
        base_sum=(base_sum+base)%mod
        harm_sum=(harm_sum+base*harmonic[a])%p
        if model=="W216":
            numer=(weight*n+1)*comb(2*n,n)**2*comb(3*n,n)
        else:
            numer=(weight*n+1)*comb(4*n,2*n)*comb(2*n,n)**2
        residue=numer*pw3%(p**3)
        assert residue%p==0
        direct=(direct+residue//p)%mod
        pw=pw*pow(denom,-1,mod)%mod
        pw3=pw3*pow(denom,-1,p**3)%(p**3)
    wilson_corr=(-wilson*base_sum)%p
    predicted=(base_sum+p*(harm_sum+wilson_corr))%mod
    assert predicted==direct,(p,model,predicted,direct)
    return predicted,base_sum,harm_sum,wilson_corr,wilson

def two_digit(p):
    mod=p**3; invW=pow(216,-1,mod);invV=pow(2304,-1,mod)
    W=[0]*3;V=[0]*3;pw=pv=1
    for n in range(p):
        ew=2*n//p+3*n//p
        ev=4*n//p
        if ew<3:
            W[ew]=(W[ew]+(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pw)%mod
        if ev<3:
            V[ev]=(V[ev]+(8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2*pv)%mod
        pw=pw*invW%mod;pv=pv*invV%mod
    assert V[2]==0 and (W[0]-V[0])%p==0
    d0=(W[0]-V[0])%mod
    d1=(W[1]-V[1])%mod
    assert d0%p==d1%p==0 and W[2]%p**2==0
    c0=d0//p;c1=d1//p;tau=W[2]//p**2
    assert (c0+c1+p*tau)%(p*p)==((sum(W)-sum(V))%mod)//p
    return W,V,c0,c1,tau,(sum(W)-sum(V))%mod

if __name__=="__main__":
    bound=int(sys.argv[1]) if len(sys.argv)>1 else 2000
    primes=primes_upto(bound)
    for p in primes:
        grade_one(p,"W216")
        grade_one(p,"V2304")
    print("exact_first_grade_models",2*len(primes),"primes",len(primes))
    for p in (5,11,13,19,373):
        if p<=bound:
            result=two_digit(p)
            assert result[-1]==0
            print("two_digit",p,result,"first_grade",grade_one(p,"W216"),grade_one(p,"V2304"))
