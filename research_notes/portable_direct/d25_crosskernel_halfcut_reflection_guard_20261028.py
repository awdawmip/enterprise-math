#!/usr/bin/env python3
"""Exact p-adic half-cut reflection for original A_216 and established B_2304.

No native H0/B0 operator is evaluated. The B high-tail theorem is imported
from Guo--Zudilin (Adv. Math. 346, 2019); its reciprocal form is derived here.
"""
from math import isqrt, comb


def primes(bound):
    for p in range(5, bound):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def terms(p, base, precision=3):
    modulus = p**precision
    term = 1
    result = []
    for n in range(p):
        result.append(term)
        if n == p - 1:
            break
        if base == 216:
            num = (2*n+1)*(3*n+1)*(3*n+2)
            den = 36*(n+1)**3
        elif base == 2304:
            num = (2*n+1)*(4*n+1)*(4*n+3)
            den = 288*(n+1)**3
        else:
            raise ValueError(base)
        term = (term * num * pow(den, -1, modulus)) % modulus
    return result


def grouped(p, base, values):
    modulus = p**3
    cutoff = (p-1)//2
    weight = 6 if base == 216 else 8
    shorter = sum((weight*n+1)*values[n] for n in range(cutoff+1)) % modulus
    high = sum((weight*n+1)*values[n] for n in range(cutoff+1,p)) % modulus
    return shorter, high


def inspect(p):
    a = terms(p,216)
    b = terms(p,2304)
    half = (p-1)//2
    Bmirror = 0
    for j in range((p+3)//4,half+1):
        k = p-j
        assert b[j] % p == 0 and b[j] % (p*p) != 0
        assert b[k] % (p*p) == 0
        v = (b[j]//p)%p
        w = (b[k]//(p*p))%p
        assert (v*w*288*j**3)%p == 1, (p,j,"B reflection")
        Bmirror += (1-8*j)*pow(288*j**3*v,-1,p)
    Bmirror %= p

    Amirror = 0
    if p%6 == 1:
        m = (p-1)//6
        for j in range(2*m+1,3*m+1):
            k = p-j
            assert a[j]%p == 0 and a[j]%(p*p) != 0
            assert a[k]%(p*p) == 0
            u = (a[j]//p)%p
            w = (a[k]//(p*p))%p
            assert (u*w*36*j**3)%p == 1, (p,j,"A reflection")
            Amirror += (1-6*j)*pow(36*j**3*u,-1,p)
        Amirror %= p
    alow, ahigh = grouped(p,216,a)
    blow, bhigh = grouped(p,2304,b)
    assert bhigh == (p*p*Bmirror)%(p**3)
    assert Bmirror == 0, (p,"GZ half/full benchmark",Bmirror)
    if p%6 == 1:
        assert ahigh == p*p*Amirror, (p,"original A high")
    assert (blow+bhigh)%(p**3) == (p if p%3 == 1 else -p)%(p**3)
    return {"p":p,"Ashort":alow,"Bshort":blow,
            "Ahigh_digit":ahigh//(p*p),"Bhigh_digit":bhigh//(p*p),
            "A_mirror":Amirror,"B_mirror":Bmirror,
            "full_diff_digit": ((alow+ahigh-blow-bhigh)%(p**3))//(p*p)}


def main():
    rows = [inspect(p) for p in primes(1000)]
    # All-prime high-tail vanishing is a COROLLARY of the cited established B theorem.
    # A_full=B_full mod p^3 remains a conjecture: we merely observe examples.
    for p in (7,13,19,373):
        # Independent integer-binomial implementation for representative primes.
        for base in (216,2304):
            m = p**3
            original = terms(p,base)
            inverse = pow(base,-1,m)
            assert all(original[n] == ((comb(2*n,n)**2 *
                    (comb(3*n,n) if base==216 else comb(4*n,2*n)) *
                    pow(inverse,n,m))%m) for n in range(p))
    target = inspect(373)
    assert target == {"p":373,"Ashort":14887176,"Bshort":373,
                      "Ahigh_digit":266,"Bhigh_digit":0,
                      "A_mirror":266,"B_mirror":0,"full_diff_digit":0}
    b = terms(373,2304)
    part = lambda lo,hi:sum((1-8*j)*pow(288*j**3*((b[j]//373)%373),-1,373)
                             for j in range(lo,hi+1))%373
    assert (part(94,140),part(141,186)) == (289,84)
    print("PASS_D25_B2304_HALF_CUT_REFLECTION",len(rows),"primes <1000")
    print("PASS_D25_A216_PAIR_RECIPROCITY",sum(r['p']%6==1 for r in rows),"primes <1000")
    print("B373_UNIT_SUM_SPLIT",289,84,"total",(289+84)%373)
    print("P373",target)


if __name__ == "__main__":
    main()
