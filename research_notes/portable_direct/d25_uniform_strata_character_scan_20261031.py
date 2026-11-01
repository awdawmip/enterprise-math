"""Original 216 weighted sum: exact all-prime valuation and bounded signed scan."""
from math import comb

LIMIT = 12000


def primes_below(limit):
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p*p:limit:p] = b"\x00" * (((limit-1-p*p)//p)+1)
    return [p for p in range(5, limit) if sieve[p]]


def weighted_sum_mod(p, cutoff=True):
    mod = p**3
    q = 2*p//3 if cutoff else p-1
    inv36 = pow(36, -1, mod)
    inv = [0] * (q+1)
    inv[1] = 1
    for k in range(2, q+1):
        inv[k] = -(mod//k)*inv[mod%k] % mod
    a = 1
    total = 1
    for n in range(q):
        k = n+1
        a = a*(2*n+1)*(3*n+1)*(3*n+2)*inv36*pow(inv[k],3,mod) % mod
        total = (total+(6*k+1)*a) % mod
    return total


def exact_weighted_valuation(n,p):
    value = 2*n//p + 3*n//p
    w = 6*n+1
    while w % p == 0:
        value += 1
        w //= p
    return value


def check():
    counts = {r:0 for r in (1,5,7,11,13,17,19,23)}
    exceptions = []
    anchors = [5,7,11,13,17,19,23,31,37,43,67,73,97,157,373]
    primes = primes_below(LIMIT)
    for p in primes:
        q = 2*p//3
        assert 2*q//p + 3*q//p == 2
        assert 2*(q+1)//p + 3*(q+1)//p == 3
        counts[p%24] += 1
        got = weighted_sum_mod(p)
        expected = (p if p%3==1 else -p) % (p**3)
        if got != expected:
            exceptions.append((p,got,expected))
        if p in anchors:
            assert got == weighted_sum_mod(p,False)
            direct = sum(
                (6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,p**3)
                for n in range(p)
            ) % (p**3)
            assert got == direct
            for n in range(p):
                coeff = comb(2*n,n)**2*comb(3*n,n)
                val = 0
                while coeff % p == 0:
                    val += 1
                    coeff //= p
                assert val == 2*n//p+3*n//p
                w = 6*n+1
                wv = 0
                while w%p==0:
                    wv+=1
                    w//=p
                assert exact_weighted_valuation(n,p) == val+wv
    assert not exceptions
    print("PASS_WEIGHTED_216_UNIFORM_STRATA_AND_CHARACTER_SCAN_EXACT")
    print("range 5<=p<",LIMIT,"total",len(primes))
    print("mod24_counts",counts)
    print("positive",sum(counts[k] for k in (1,7,13,19)))
    print("negative",sum(counts[k] for k in (5,11,17,23)))
    print("character_exceptions",exceptions)
    print("integer_binomial_and_full_recurrence_anchors",anchors)
    print("p373",weighted_sum_mod(373),"mod",373**3,"prefix_q",2*373//3)


if __name__ == "__main__":
    check()
