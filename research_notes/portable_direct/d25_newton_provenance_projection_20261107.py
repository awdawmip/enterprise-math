"""D25: Newton spectral block projection of normal/carry source bands.

Pure Python integer/prime-field regression for an author-side proof, not an
Enterprise Math native task/run/experiment. Full theorem is established in
its accompanying algebraic note; these checks cover only declared primes.
"""
from math import isqrt


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def test_prime(p):
    assert p > 3 and p % 6 == 1 and isprime(p)
    m = (p - 1) // 6
    a, b, c, n = 2 * m, 3 * m, 4 * m, 2 * m
    fact = [1] * p
    for i in range(1, p):
        fact[i] = fact[i - 1] * i % p
    invfact = [pow(x, -1, p) for x in fact]

    def bc(x, j):
        """Binomial polynomial (x choose j) in F_p, j<p, any integer x."""
        x %= p
        return fact[x] * invfact[j] * invfact[x - j] % p if 0 <= j <= x else 0

    weights = [((6 * j + 1) * pow(-2, -j, p) * bc(b, j)) % p
               for j in range(b + 1)]
    # Recover the scalar endpoint samples from their labelled source terms.
    full, normal, carry = ([0] * p for _ in range(3))
    for t in range(p):
        bound = min(t, (t - a) % p, b)
        for j in range(bound + 1):
            term = weights[j] * bc(t, j) * bc(t - a, j) % p
            full[t] = (full[t] + term) % p
            if j <= a:
                normal[t] = (normal[t] + term) % p
            else:
                carry[t] = (carry[t] + term) % p
        assert full[t] == (normal[t] + carry[t]) % p

    # Carry terms have an exact consecutive-zero interval t=0,...,4m.
    assert all(carry[t] == 0 for t in range(c + 1))
    differences = full[:c + 1]
    d = []
    while differences:
        d.append(differences[0])
        differences = [(differences[k + 1] - differences[k]) % p
                       for k in range(len(differences) - 1)]

    # Newton projection of all p samples recovers the normal labelled band.
    N = [sum(d[j] * bc(t, j) for j in range(min(t, c) + 1)) % p
         for t in range(p)]
    assert N == normal

    # At t=c+1,...,p-1, q(t)=(t)_{c+1} is a unit. Divide the
    # complementary data by q, then extrapolate degree<=2m-1 back to t=c.
    C_samples = []
    for u in range(n):
        t = c + 1 + u
        q_t = fact[t] * invfact[t - c - 1] % p
        assert q_t != 0
        C_samples.append((full[t] - N[t]) * pow(q_t, -1, p) % p)
    C_at_c = sum((-1 if u % 2 else 1) * bc(n, u + 1) * C_samples[u]
                 for u in range(n)) % p
    carry_derivative = fact[c] * C_at_c % p

    Hc = sum(pow(k, -1, p) for k in range(1, c + 1)) % p
    normal_derivative = (full[c] * Hc + sum(
        (-1 if (c - t) % 2 else 1) * bc(c, t) * full[t] *
        pow(c - t, -1, p)
        for t in range(c)
    )) % p

    # Independent derivative of the two source-labelled polynomial bands.
    direct_normal = 0
    for j in range(a + 1):
        logarithmic = sum(pow(c - r, -1, p) + pow(a - r, -1, p)
                          for r in range(j)) % p
        direct_normal += weights[j] * bc(c, j) * bc(a, j) * logarithmic
    direct_normal %= p
    direct_carry = 0
    for j in range(a + 1, b + 1):
        # derivative of binom(t-a,j) at t=c, a simple root
        derivative_binomial = (fact[a] * fact[j - a - 1] * invfact[j]
                               * (-1 if (j - a - 1) % 2 else 1)) % p
        direct_carry += weights[j] * bc(c, j) * derivative_binomial
    direct_carry %= p
    assert normal_derivative == direct_normal
    assert carry_derivative == direct_carry

    # The open all-prime tangent congruence remains only a finite check.
    total = (normal_derivative + carry_derivative) % p
    assert total == 0, (p, total)
    if p <= 73:
        # Separately reconstruct the entire endpoint sequence E_t(+1).
        inv3 = pow(3, -1, p)
        central = [(6*j+1)*bc(2*j,j)*pow(8,-j,p) % p
                   for j in range(b+1)]
        for t in range(p):
            other = (t + inv3) % p
            E_t = sum(central[j]*bc(t,j)*bc(other,j)
                      for j in range(min(t,other,b)+1)) % p
            assert E_t == full[t], (p,t)
    return (p, normal_derivative, carry_derivative, C_at_c, total)


def main():
    ps = [p for p in range(7, 1001) if p % 6 == 1 and isprime(p)]
    witnesses = {7,13,19,31,109,211,229,373}
    for p in ps:
        row = test_prime(p)
        if p in witnesses:
            print("NORMAL_CARRY_NEWTON_PROJECTION", row)
    print("EXACT_FINITE_REGRESSION_PASS", len(ps), "primes p=1(mod6), p<=1000")
    print("MATHEMATICAL_STATUS algebraic theorem; tangent zero only finite-tested")


if __name__ == "__main__":
    main()
