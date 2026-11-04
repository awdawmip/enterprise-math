#!/usr/bin/env python3
"""Check original-216 Picard-Fuchs band endpoints and universal terminal residue."""

def primes(n):
    t=[True]*(n+1);t[:2]=[False,False]
    for d in range(2,int(n**.5)+1):
        if t[d]:
            for v in range(d*d,n+1,d):t[v]=False
    return [p for p in range(5,n+1) if t[p]]

def factval(n,p):
    y=0
    while n:
        n//=p;y+=n
    return y

def factorial_unit(n,p,M):
    a=1
    for i in range(1,n+1):
        while i%p==0:i//=p
        a=a*i%M
    return a

def main():
    seen=0; band_seen=0
    for p in primes(2000):
        r=(p-1)//6; bound=p**4
        b=[1]
        for k in range(p-1):
            mult=(2*k+1)*(3*k+1)*(3*k+2)
            den=36*(k+1)**3
            b.append(b[-1]*mult*pow(den,-1,bound)%bound)
        # The hypergeometric recurrence is k^3 a_k = (1/2)*(k-1/2)(k-2/3)(k-1/3) a_(k-1).
        # The 216-normalized integer coefficient is (2k-1)(3k-2)(3k-1)/(36)*a_(k-1).
        def boundary(n):
            return n**3*b[n]%bound
        # Terminal at p from actual a_(p-1), whose p^3 unit may be tested against a_p mod p.
        terminal= ((2*p-1)*(3*p-2)*(3*p-1)*b[p-1]*pow(36,-1,bound))%bound
        a_p_unit = (factorial_unit(2*p,p,p)*factorial_unit(3*p,p,p)*
                    pow(factorial_unit(p,p,p),-5,p)*pow(216,-p,p))%p
        assert a_p_unit == pow(18,-1,p), (p,a_p_unit)
        assert terminal == (p**3*a_p_unit)%bound, (p,terminal)
        if p%6==1:
          band_seen+=1
          for n,v in [(2*r+1,1),(3*r+1,2),(4*r+1,3)]:
            val=factval(2*n,p)+factval(3*n,p)-5*factval(n,p)
            assert val==v,(p,n,val)
            assert b[n]%(p**(v+1))!=0 and b[n]%(p**v)==0
            # Exact terminal contribution L(sum_{k=0}^{n-1} a_k z^k) = -n^3 a_n z^n.
            # Interior terms cancel coefficientwise due to factorial recurrence.
            if n<p:
                assert boundary(n)==((2*n-1)*(3*n-2)*(3*n-1)*b[n-1]*pow(36,-1,bound))%bound
        # The entire original truncated solution is homogeneous mod p^3,
        # but carries a universal terminal source -p^3/18 modulo p^4.
        assert terminal//(p**3) == a_p_unit
        seen+=1
        if p in (5,7,13,19,37,373):
            print('p',p,'boundary valuations:',([factval(2*n,p)+factval(3*n,p)-5*factval(n,p) for n in (2*r+1,3*r+1,4*r+1)] if p%6==1 else 'n/a'),'a_p mod p',a_p_unit)
    print('PASS all_primes=',seen,'band_primes=',band_seen,'terminal=a_p mod p=18^-1; boundary valuations=1,2,3')
if __name__=='__main__':main()
