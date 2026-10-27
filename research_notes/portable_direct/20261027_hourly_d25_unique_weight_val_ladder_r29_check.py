"""R29 author-side exact certificate: the unique S weight-zero and W/S p^3 census.

Uses integer binomial coefficients independently of the Wilson-block formula;
no floating point, native CM/Frobenius implementation, or claimed proof by census.
"""
from math import comb, factorial, isqrt


def primes_1_mod_6(limit):
    return [p for p in range(7, limit) if p % 6 == 1
            and all(p % d for d in range(2, isqrt(p) + 1))]


def special_source(p):
    a = p % 8                           # odd residue in {1, 3, 5, 7}
    k = (a * p - 1) // 8                # unique k<p with p | (8k+1)
    q2, q3 = (2 * k) // p, (3 * k) // p
    q = (a - 1) // 2
    exceptional = int(a == p)           # only p=7 within this prime class
    assert 8 * k + 1 == a * p
    assert (4 * k) // p == q == q2 + q3
    assert 0 <= k < p and 6 * k + 1 != 0
    assert (6 * k + 1) % p != 0
    mod = p ** (q + 3 + exceptional)

    # Independent original integer factorial-ratio via binomial coefficients.
    w = (6 * k + 1) * comb(2*k, k)**2 * comb(3*k, k)
    s = (8 * k + 1) * comb(4*k, k) * comb(3*k, k) * comb(2*k, k)
    w = w * pow(216, -k, mod) % mod
    s = s * pow(2304, -k, mod) % mod
    assert w % p**q == 0 and w % p**(q+1) != 0
    assert s % p**(q+1+exceptional) == 0
    assert s % p**(q+2+exceptional) != 0
    w_unit, s_unit = w // p**q % p, s // p**(q+1+exceptional) % p

    # Independently predicted Wilson-block factorial units.
    fw = (6*k+1) * (-1)**q * factorial(q2) * factorial(q3)
    fw *= factorial(2*k-q2*p) * factorial(3*k-q3*p)
    fw *= pow((factorial(k)**5 * 216**k) % p, -1, p)
    fs = (a // p if exceptional else a) * (-1)**q * factorial(q)
    fs *= factorial((p-1)//2)
    fs *= pow((factorial(k)**4 * 2304**k) % p, -1, p)
    assert w_unit == fw % p and s_unit == fs % p
    assert (w-s) % p**(q+1) != 0       # intrinsic termwise mismatch
    return (p, a, k, q, q+1+exceptional, w_unit, s_unit)


def full_original_sums(p):
    """Independent p^3 factorial-ratio recurrences, no division by weights."""
    m, modulus = (p-1)//6, p**3
    wbase = sbase = 1
    low = high = W = S = 0
    for k in range(p):
        wk = (6*k+1) * wbase % modulus
        sk = (8*k+1) * sbase % modulus
        W = (W+wk) % modulus
        S = (S+sk) % modulus
        if k <= 3*m:
            low = (low+wk-sk) % modulus
        if 3*m < k <= 4*m:
            high = (high+wk) % modulus
        if k+1 < p:
            d = k+1
            wbase = (wbase * (2*k+1)*(2*k+2)*(3*k+1)*(3*k+2)*(3*k+3)
                     * pow(216*d**5, -1, modulus)) % modulus
            sbase = (sbase * (4*k+1)*(4*k+2)*(4*k+3)*(4*k+4)
                     * pow(2304*d**4, -1, modulus)) % modulus
    assert low % p**2 == high % p**2 == 0
    assert (low+high) % modulus == 0
    assert W == S == p % modulus
    return low//p**2, high//p**2


def main():
    primes = primes_1_mod_6(2000)
    assert len(primes) == 148
    certs = [special_source(p) for p in primes]
    bridges = {p: full_original_sums(p) for p in primes}
    assert sum(p%24 == 13 for p in primes) == 40
    assert sum(p%24 == 19 for p in primes) == 37
    print("PASS: 148 primes 7<=p<2000, p=1(mod6): exact binomial/Wilson weight units")
    print("PASS: original full W=S=p mod p^3 and independent low+high source balance")
    print("p a k v_w v_s w_unit s_unit low/p^2 high/p^2")
    for p,a,k,q,vs,wu,su in certs:
        if p in {7,13,19,37,43,61,181,373,733,997}:
            print(p,a,k,q,vs,wu,su,*bridges[p])


if __name__ == '__main__':
    main()
