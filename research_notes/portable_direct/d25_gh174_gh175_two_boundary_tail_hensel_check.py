"""Exact portable check of GH-174/GH-175; no native D25 runtime is used."""
from math import comb


def primes_under(n):
    sieve = bytearray(b"\x01") * n
    sieve[:2] = b"\x00\x00"
    for k in range(2, int(n**0.5) + 1):
        if sieve[k]:
            sieve[k*k:n:k] = b"\x00" * ((n - 1 - k*k) // k + 1)
    return [p for p in range(7, n) if sieve[p] and p % 6 == 1]


def tail_mod_p(p, full_operator=False):
    m, N = (p - 1) // 6, 4 * ((p - 1) // 6) + 1
    factorial = 1
    for k in range(1, N + 1):
        factorial = factorial * k % p
    nf = factorial
    for k in range(N + 1, p):
        factorial = factorial * k % p
    # For (2m+1)!, recompute just the smaller unit factorial.
    rfact = 1
    for k in range(1, 2*m + 2):
        rfact = rfact * k % p
    u = (-2 * rfact * pow(pow(nf, 5, p) * pow(216, N, p) % p, -1, p)) % p
    c = u
    scalar = derivative = 0
    previous = 0
    for n in range(N, p):
        scalar = (scalar + (6*n + 1) * c) % p
        derivative = (derivative + n * (6*n + 1) * c) % p
        if full_operator:
            coeff = (pow(n, 3, p) * c -
                     (2*n-1)*(3*n-2)*(3*n-1)*previous * pow(36, -1, p)) % p
            assert coeff == (pow(N, 3, p) * u % p if n == N else 0), (p, n, coeff)
        previous = c
        if n < p - 1:
            ratio = ((2*n+1)*(3*n+1)*(3*n+2) *
                     pow(36 * pow(n+1, 3, p), -1, p)) % p
            c = c * ratio % p
    assert c == p - 1, (p, c)
    assert (-(2*p-1)*(3*p-2)*(3*p-1)*c*pow(36, -1, p)) % p == (-pow(18, -1, p)) % p
    assert ((6*(p-1)+1)*c) % p == 5 % p
    return N, u, scalar, derivative


def hensel_1327():
    p = 1327
    N = 4 * ((p - 1) // 6) + 1
    modulus = p**5
    a = 1
    value = derivative = 0
    check_indices = {N, N+1, N+37, p-2, p-1}
    for n in range(p):
        if n >= N:
            assert a % p**3 == 0
            residue = a // p**3
            value = (value + (6*n+1)*residue) % p**2
            derivative = (derivative + n*(6*n+1)*residue) % p
            if n in check_indices:
                direct = comb(2*n, n)**2 * comb(3*n, n)
                direct = direct * pow(pow(216, n, modulus), -1, modulus) % modulus
                assert direct == a, (n, direct, a)
        if n < p-1:
            a = a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3, -1, modulus) % modulus
    assert value == 1646807 and derivative == 480
    assert value % p == 0
    t = (-value//p * pow(derivative, -1, p)) % p
    assert t == 61
    root = 1 + p*t
    # Taylor modulo p² is exact for the integral polynomial D_p.
    assert (value + p*t*derivative) % p**2 == 0
    return value, derivative, t, root


def main():
    tested = primes_under(12000)
    zeroes = []
    for p in tested:
        _, _, q, _ = tail_mod_p(p, full_operator=(p < 5000))
        if q == 0:
            zeroes.append(p)
    assert zeroes == [1327], zeroes
    assert tail_mod_p(373) == (249, 277, 278, 279)
    assert tail_mod_p(1327) == (885, 788, 0, 480)
    print("primes", len(tested), "full_operator_primes", sum(p < 5000 for p in tested))
    print("p373 N,u,Q,Qprime", *tail_mod_p(373))
    print("p1327 N,u,Q,Qprime", *tail_mod_p(1327))
    print("p1327 D(1)modp2,Dprime,t,lift", *hensel_1327())
    print("bounded_Q_zeroes", zeroes)
    print("PASS_GH174_GH175_TWO_BOUNDARY_TAIL_AND_HENSEL_EXACT")


if __name__ == "__main__":
    main()
