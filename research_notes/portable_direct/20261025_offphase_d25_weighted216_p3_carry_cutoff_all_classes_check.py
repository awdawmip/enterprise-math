"""Exact author finite verification for weighted 216-series. Not an all-prime proof."""

from math import comb, isqrt


def primes_below(bound):
    s = bytearray(b"\x01") * bound
    s[:2] = b"\x00\x00"
    for q in range(2, isqrt(bound - 1) + 1):
        if s[q]:
            s[q * q:bound:q] = b"\x00" * ((bound - q * q - 1) // q + 1)
    return [p for p in range(5, bound) if s[p]]


def vport(k, p):
    """Exact v_p of the binomial integer numerator for 0<=k<p."""
    return (2*k)//p + (3*k)//p


def weighted216(p):
    mod = p**3
    inverse = [0]*p
    inverse[1] = 1
    for i in range(2, p):
        inverse[i] = -(mod//i)*inverse[mod%i] % mod
    inv36 = pow(36, -1, mod)
    cutoff_index = (2*p-1)//3
    d = 1
    total = 0
    cutoff = 0
    for k in range(p):
        v = vport(k, p)
        assert v == (3*k >= p) + (2*k >= p) + (3*k >= 2*p)
        if v < 3:
            assert d % p**v == 0 and d % p**(v+1) != 0, (p,k,v)
        else:
            assert d == 0, (p,k)
        term = ((6*k+1)*d) % mod
        total = (total+term) % mod
        if k <= cutoff_index:
            cutoff = (cutoff+term) % mod
        else:
            assert term == 0, (p,k)
        if k < p-1:
            t = k+1
            d = d*(2*k+1)*(3*k+1)*(3*k+2)*inv36*inverse[t]**3 % mod
    assert total == cutoff, p
    expected = p if p % 3 == 1 else mod-p
    assert total == expected, (p,total,expected)
    return total, cutoff_index


def check_direct(p):
    """Independent integer-binomial reconstruction, for p<200."""
    mod = p**3
    inv216 = pow(216,-1,mod)
    z = 1
    total = 0
    for k in range(p):
        ak = comb(2*k,k)**2 * comb(3*k,k)
        total = (total+(6*k+1)*ak*z) % mod
        z = z*inv216 % mod
    assert total == weighted216(p)[0], p


if __name__ == "__main__":
    count1 = count5 = count_direct = 0
    for prime in primes_below(5000):
        weighted216(prime)
        if prime < 200:
            check_direct(prime)
            count_direct += 1
        if prime % 6 == 1:
            count1 += 1
        else:
            count5 += 1
    assert (count1,count5,count_direct) == (330,337,44)
    print("PASS 667 primes <5000; 330 p=1 mod6; 337 p=5 mod6")
    print("PASS cutoff all 667; independent binomial all 44 primes <200")
    for prime in (5,7,11,13,19,31):
        residue, cap = weighted216(prime)
        print(prime, cap, residue)
