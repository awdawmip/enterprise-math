#!/usr/bin/env python3
"""Author-side exact finite prime checks for original 216 Picard--Fuchs cutoff.

No float or p-adic Gamma; modular recurrence and factorial/binomial cross-check.
Not a native H0/B0 computation, canonical Result or universal LIFT proof.
"""
from math import comb, factorial, isqrt

PRIMES = [5, 7, 11, 13, 17, 19, 23, 31, 37, 43, 61, 67, 73,
          79, 97, 103, 109, 127, 139, 151, 157, 163, 181, 193,
          199, 211, 373]


def terms(p):
    q = p**4
    t = 1
    out = []
    for n in range(p):
        out.append(t)
        if n+1 < p:
            t = (t * (2*n+1) * (3*n+1) * (3*n+2)
                 * pow(36*(n+1)**3, -1, q)) % q
    return out


def verify(p):
    assert p >= 5 and all(p % k for k in range(2, isqrt(p)+1))
    q = p**4
    inv = lambda a: pow(a % q, -1, q)
    a = terms(p)
    for n in range(p):
        coef = ((n**3*a[n]) - (0 if n == 0 else
                 inv(2) * (n-1+inv(2)) * (n-1+inv(3))
                 * (n-1+2*inv(3)) * a[n-1])) % q
        assert coef == 0, ('interior PF coefficient', p, n, coef)
    c = (-inv(2)*(p-1+inv(2))*(p-1+inv(3))
         *(p-1+2*inv(3))*a[p-1]) % q
    predicted = (-p**3*inv(18)) % q
    assert a[p-1] % p**3 == 0
    assert a[p-1]//p**3 == p-1
    assert c == predicted and c != 0
    assert ((6*p-5)*a[p-1]//p**3) % p == 5 % p
    for n in [0, 1, p//3, (p-1)//2, p-1]:
        independently = (comb(2*n,n)**2 * comb(3*n,n)
                         * inv(pow(216,n,q))) % q
        assert a[n] == independently, (p,n,'independent binomial')
    if p % 6 != 1:
        return {'p':p, 'pf':c, 'top':5}
    m=(p-1)//6
    w=[(6*n+1)*a[n] % q for n in range(p)]
    omega=0
    for r in range(2*m):
        n=4*m+1+r
        assert n == p-(2*m-r)
        assert w[n] % p**3 == 0 and w[n] % p**4 != 0
        digit = w[n]//p**3
        source = (-6*(2*r+1) * factorial(2*m+1+2*r)
                  * factorial(3*r+1)
                  * pow(216**n * factorial(n)**5,-1,p)) % p
        assert digit == source, (p,r,'upper factorial')
        low_n = p-n
        assert a[low_n] % p != 0
        reflected = ((a[n]//p**3)*(a[low_n]%p))%p
        assert reflected == -pow(18*low_n**3,-1,p)%p
        repaired = (-(1-6*low_n) * pow(18*low_n**3*(a[low_n]%p),-1,p))%p
        assert repaired == digit, (p,low_n,'low-to-upper inversion')
        omega=(omega+digit)%p
    bulk=sum(w[:4*m+1])%q
    full=sum(w)%q
    assert (bulk+p**3*omega)%q == full
    assert w[m]%p == 0 and w[m]//p%p == a[m]%p
    assert (w[p-m]//p**3)%p != 0
    return {'p':p, 'm':m, 'pf':c, 'omega':omega,
            'zero_weight_low_t':a[m]%p, 'zero_weight_low_w_over_p':w[m]//p%p,
            'mirror_upper':w[p-m]//p**3%p, 'bulk':bulk,'full':full}


def main():
    rows = [verify(p) for p in PRIMES]
    print('PASS_D25_EXACT_PF_CUTOFF_AND_ORIGINAL_P4_UPPER_PORT')
    print('primes_checked=',len(rows),'one_mod_six=',sum(p%6==1 for p in PRIMES))
    print('p13=',next(x for x in rows if x['p']==13))
    print('p19=',next(x for x in rows if x['p']==19))
    print('p373=',next(x for x in rows if x['p']==373))


if __name__=='__main__':
    main()
