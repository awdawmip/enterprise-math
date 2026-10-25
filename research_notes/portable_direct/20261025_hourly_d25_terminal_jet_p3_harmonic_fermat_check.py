"""Exact author check of D25 p^3 terminal forcing, with source and observer routes.

Standard library; no remote compute or native Source experiment. This is author
validation of an algebraic theorem, not independent mathematical review.
"""
from fractions import Fraction
from math import factorial


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for d in range(2, int(n**0.5) + 1):
        if sieve[d]:
            sieve[d*d:n+1:d] = b"\x00" * ((n-d*d)//d+1)
    return [p for p in range(7, n+1) if sieve[p] and p % 6 == 1]


def local_mod(q, modulus):
    if isinstance(q, Fraction):
        return q.numerator * pow(q.denominator, -1, modulus) % modulus
    return q % modulus


def verify(p):
    assert p >= 7 and p % 6 == 1
    m = (p-1)//6
    modulus = p**3
    fac_mod = [1]*p
    for j in range(1, p):
        fac_mod[j] = fac_mod[j-1]*j % modulus
    f = lambda j: fac_mod[j]

    # Route 1: original source endpoint factorial, not the harmonic product.
    w = (2*(-1)**m*f(m)*f(2*m)*f(5*m-1)*f(4*m-1)
         * pow(f(6*m), -2, modulus)) % modulus
    K = (-40*m*m*w) % modulus

    # Route 2: p-local finite harmonic expansion of the complement product.
    h = Fraction(0)
    h2 = Fraction(0)
    for j in range(1, 2*m+2):
        h += Fraction(1, j)
        h2 += Fraction(1, j*j)
        if j <= m+1:
            h += Fraction(1, j)
            h2 += Fraction(1, j*j)
    A = h-Fraction(27, 10)
    B = (A*A+h2)/2-Fraction(171, 200)
    predicted_K = local_mod(-4*(1+p*A+p*p*B), modulus)
    assert K == predicted_K, (p, K, predicted_K)

    # Observer input uses Fermat quotient, not z^p -> z before differentiation.
    q2 = (pow(2, p-1, p**4)-1)//p  # sufficient exact residue of integer q_p(2)
    J = K*pow(pow(2, p, modulus), -1, modulus) % modulus
    predicted_J = local_mod(
        -2*(1+p*(A-q2)+p*p*(B+q2*q2-A*q2)), modulus)
    assert J == predicted_J, (p, J, predicted_J)
    assert K % p == -4 % p and J % p == -2 % p
    return p, K, J, local_mod(A, p), q2 % p


def rational_factorization_check(p):
    m = (p-1)//6
    w = Fraction(
        2*(-1)**m*factorial(m)*factorial(2*m)
        * factorial(5*m-1)*factorial(4*m-1),
        factorial(6*m)**2)
    product = Fraction(2, (m+1)*(2*m+1))
    for j in list(range(1, m+2)) + list(range(1, 2*m+2)):
        product /= (1-Fraction(p, j))
    assert w == product
    return w


if __name__ == "__main__":
    cases = primes_upto(373) + [1327, 19963]
    rows = [verify(p) for p in cases]
    assert len(rows) == 37
    for p in (7, 13, 19):
        rational_factorization_check(p)
    print("PASS:", len(rows), "eligible primes; mod p^3 full-source and 1/2-observer")
    print("PASS: exact rational complement for p=7,13,19")
    for row in rows:
        if row[0] in (7, 13, 19, 373, 1327, 19963):
            print(row)
