"""Finite original-coefficient checks for D25 dual PF forcing and terminal carry.
All calculations are integer modular; these tests do not prove the all-prime theorem.
"""
from math import isqrt

def primes(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes([0, 0])
    for d in range(2, isqrt(limit) + 1):
        if sieve[d]:
            sieve[d*d::d] = bytes([0]) * ((limit-d*d)//d+1)
    return [p for p in range(5, limit+1) if sieve[p]]

def p_unit_facts(p, N, modulus):
    facts = [1] * (N + 1)
    for k in range(1, N+1):
        x = k
        while x % p == 0:
            x //= p
        facts[k] = facts[k-1] * x % modulus
    return facts

def a216(k, p, f, m):
    v = 2*k//p + 3*k//p - 5*(k//p)
    if v >= 4: return 0
    den = f[k]**5 * pow(216, k, m)
    return pow(p, v, m)*f[2*k]*f[3*k]*pow(den, -1, m)%m

def b2304(k, p, f, m):
    v = 4*k//p - 4*(k//p)
    if v >= 4: return 0
    den = f[k]**4 * pow(2304, k, m)
    return pow(p, v, m)*f[4*k]*pow(den, -1, m)%m

def run(limit=2000):
    examples, count, coefs = {}, 0, 0
    for p in primes(limit):
        m, n3 = p**4, p**3
        f = p_unit_facts(p, 4*p, m)
        aa = [a216(k,p,f,m) for k in range(p+1)]
        bb = [b2304(k,p,f,m) for k in range(p+1)]
        inv144, inv576, inv36 = pow(144,-1,m), pow(576,-1,m), pow(36,-1,m)
        for n in range(1,p+1):
            ca = ((2*n-1)*(3*n-2)*(3*n-1)*inv36)%m
            cb = ((4*n-3)*(4*n-2)*(4*n-1)*inv576)%m
            rr = ((2*n-1)*(56*(n-1)*n+13)*inv144*pow(2,-1,m))%m
            assert (n**3*aa[n]-ca*aa[n-1])%m==0,(p,n,"A recurrence")
            assert (n**3*bb[n]-cb*bb[n-1])%m==0,(p,n,"B recurrence")
            delta_prev=(aa[n-1]-bb[n-1])%m
            if n<p:
                dl=(n**3*(aa[n]-bb[n])-cb*delta_prev)%m
                dr=(rr*aa[n-1])%m
                el=(n**3*(aa[n]-bb[n])-ca*delta_prev)%m
                er=(rr*bb[n-1])%m
            else:
                dl=(-cb*delta_prev)%m
                dr=(rr*aa[n-1]-p**3*(aa[n]-bb[n]))%m
                el=(-ca*delta_prev)%m
                er=(rr*bb[n-1]-p**3*(aa[n]-bb[n]))%m
            assert dl==dr,(p,n,"L_B delta",dl,dr)
            assert el==er,(p,n,"L_A delta",el,er)
            coefs+=1
        qa=(pow(216,p-1,n3)-1)//p
        qb=(pow(2304,p-1,n3)-1)//p
        aform=pow(18,-1,n3)*(1-p*qa+p*p*qa*qa)%n3
        bform=pow(96,-1,n3)*(1-p*qb+p*p*qb*qb)%n3
        assert aa[p]%n3==aform,(p,"terminal A")
        assert bb[p]%n3==bform,(p,"terminal B")
        assert (aa[p]-bb[p]-13*pow(288,-1,p))%p==0,(p,"terminal delta")
        if p in (5,7,13,19,37,373,1999):
            examples[p]=(aa[p]%n3,bb[p]%n3,(aa[p]-bb[p])%n3)
        count+=1
    print("PASS primes=",count,"PF_dual_coefficients=",coefs,"terminal_mod_p3=",count)
    for p,vals in examples.items(): print("EXAMPLE",p,vals)

if __name__=="__main__": run()
