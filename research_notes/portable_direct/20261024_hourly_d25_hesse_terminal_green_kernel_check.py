"""Author check of the D25 Hesse second-digit Green kernel (portable, exact integers).

Scope: p ≡ 13 or 19 mod 24, p < 10000; not a native CM experiment.
"""
from math import comb, isqrt


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, 1 + isqrt(n)))


def terminal_kernel(p):
    assert p >= 13 and p % 6 == 1 and is_prime(p)
    m, n = (p - 1) // 6, (p - 1) // 3
    fac = 1
    for k in range(1, n + 1):
        fac = (fac * k) % p
    c_n = -pow(pow(27, n, p) * pow(fac, 3, p) % p, -1, p) % p
    C = c_n * pow(9, -1, p) % p
    inv9, inv8 = pow(9, -1, p), pow(8, -1, p)
    beta = [0] * (m + 1)
    for j in range(m - 1, -1, -1):
        f_j = (-1 if j % 2 else 1) * comb(2 * m - 1 - j, j)
        lam = ((6 * j + 4) * (6 * j + 5) * inv9) % p
        beta[j] = ((j + 1)**2 * beta[j + 1] - f_j) * pow(lam, -1, p) % p
    Q = sum((2 * j - 1) * beta[j] * pow(inv8, j, p)
            for j in range(m)) % p
    return C * Q % p, C, Q


def harmonic_trace(p):
    n = (p - 1) // 3
    W = [2, 1]
    for _ in range(2, n):
        W.append((W[-1] - pow(8, -1, p) * W[-2]) % p)
    ck, Lk, total = 1, 0, 0
    for k in range(1, n + 1):
        j = k - 1
        ck = ck * (3*j+1) * (3*j+2) * (3*j+3) * pow(27*k**3, -1, p) % p
        Lk = (Lk + pow(3*j+1, -1, p) - pow(3*j+2, -1, p)) % p
        total = (total + k * ck * Lk * W[k-1]) % p
    return total * pow(2, -1, p) % p


def mul(a, b, modulus):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % modulus,
            (a[0]*b[1] + a[1]*b[0]) % modulus)


def direct_derivative(p):
    """A_p'(u) mod p^2 as a+bT, T^2=2 and u=(2-T)/4."""
    q, n = p*p, (p - 1)//3
    inv4 = pow(4, -1, q)
    u, upow, ck, derivative = (2*inv4 % q, -inv4 % q), (1, 0), 1, (0, 0)
    for k in range(1, n + 1):
        j = k - 1
        ck = ck*(3*j+1)*(3*j+2)*(3*j+3)*pow(27*k**3, -1, q) % q
        term = mul((k*ck % q, 0), upow, q)
        derivative = ((derivative[0]+term[0]) % q,
                      (derivative[1]+term[1]) % q)
        upow = mul(upow, u, q)
    return derivative


if __name__ == "__main__":
    targets = [p for p in range(13, 10000)
               if p % 24 in (13, 19) and is_prime(p)]
    mismatches = [(p, terminal_kernel(p)[0], harmonic_trace(p))
                  for p in targets if terminal_kernel(p)[0] != harmonic_trace(p)]
    zeros = [p for p in targets if terminal_kernel(p)[0] == 0]
    assert not mismatches
    assert zeros == [373]
    E, C, Q = terminal_kernel(373)
    assert (E, C, Q) == (0, 40, 0)
    assert direct_derivative(373) == (0, 130607)
    assert 3 * (130607 % 373) % 373 == 171
    print("target_primes_below_10000", len(targets))
    print("kernel_trace_mismatches", len(mismatches))
    print("bounded_E_zero_primes", zeros)
    print("p373_C_Q_E", C, Q, E)
    print("p373_direct_Aprime_u_mod_p2", direct_derivative(373))
    print("p373_first_digit_h", 171)
