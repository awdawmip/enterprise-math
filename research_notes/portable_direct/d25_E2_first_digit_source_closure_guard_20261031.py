#!/usr/bin/env python3
"""Independent exact integer guard for the D25/E.2 first-digit dependency closure.

AUTHOR-SIDE, NOT_NATIVE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
No result here proves the all-prime second-digit bridge.
"""
from math import comb

PRIMES = (13, 19, 37, 43, 67, 373)


def term_series(p):
    modulus = p ** 3
    original = [1]
    e2 = [1]
    gauss = [1]
    for n in range(p - 1):
        original.append(original[-1] * (2*n+1) * (3*n+1) * (3*n+2)
                        * pow(36 * (n+1)**3, -1, modulus) % modulus)
        e2.append(-e2[-1] * (3*n+1)**3
                  * pow(27 * (n+1)**3, -1, modulus) % modulus)
        gauss.append(gauss[-1] * (6*n+1) * (3*n+1)
                     * pow(36 * (n+1)**2, -1, modulus) % modulus)
    return original, e2, gauss


def frozen_r(p, gauss):
    l = (p-1)//6
    c = [0, pow(10, -1, p)]
    for a in range(1, l):
        c.append(c[-1] * 36*a*a * pow((6*a+5)*(3*a+2), -1, p) % p)
    return sum(2 * gauss[i] * sum((1 + 6*(i-a)) * c[a]
                                        for a in range(1, i+1))
               for i in range(1, l+1)) % p


def check(p):
    l=(p-1)//6; m=2*l; h=3*l
    q=p**3
    a,b,g=term_series(p)
    A=sum((6*n+1)*a[n] for n in range(p)) % q
    B=sum((6*n+1)*b[n] for n in range(m+1)) % q
    D0=sum((6*n+1)*(a[n]-b[n]) for n in range(m+1)) % q
    D1=sum((6*n+1)*a[n] for n in range(m+1,h+1)) % q
    S2=sum((6*n+1)*a[n] for n in range(h+1,2*m+1)) % q
    assert sum((6*n+1)*a[n] for n in range(2*m+1,p)) % q == 0
    assert (A - B - D0 - D1 - S2) % q == 0
    assert A % (p*p) == p and B==p
    assert (D0+D1) % (p*p) == 0 and S2 % (p*p) == 0
    G=sum(g) % q
    H=sum((12*n+1)*g[n] for n in range(p)) % q
    assert G % p == 0
    prod=((G//p)*H) % (p*p)
    assert prod % p == 1
    delta=((prod-1)//p) % p
    R=frozen_r(p,g)
    carry=((D0 + D1) % q)//(p*p)
    inverse_moment=S2//(p*p)
    assert (carry+inverse_moment) % p == ((A-B) % q)//(p*p)
    assert ((A-p) % q)//(p*p) == (delta-R) % p
    assert (carry+inverse_moment) % p == (delta-R) % p
    A_bin=sum((6*n+1) * comb(2*n,n)**2 * comb(3*n,n)
              * pow(216,-n,q) for n in range(p)) % q
    assert A_bin==A
    return (p, D0% (p*p), D1%(p*p), carry, inverse_moment,
            delta, R, (delta-R)%p)


def main():
    print('p D0_mod_p2 D1_mod_p2 normalized_lowmid normalized_high delta frozen_R residual')
    for p in PRIMES:
        print(*check(p))
    print('PASS_D25_E2_FIRST_DIGIT_DEPENDENCY_AND_SIGNED_OBSERVER_GUARD')


if __name__=='__main__':
    main()
