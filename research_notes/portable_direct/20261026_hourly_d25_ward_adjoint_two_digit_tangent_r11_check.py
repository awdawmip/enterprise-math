#!/usr/bin/env python3
"""Exact finite-ring check of the fixed-m second-digit Ward-adjoint expansion.
Author-only auxiliary corrected-Clausen observer; not native CM, proof acceptance or CLAIM.
"""
from fractions import Fraction


def target_primes(bound=997):
    for p in range(7,bound + 1):
        if (p - 1) % 6:
            continue
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            yield p


def inv(x, modulus):
    return pow(x % modulus, -1, modulus)


def direct_adjoint(p, modulus):
    m = (p - 1) // 6
    N = 2 * m - 1
    b = 0
    out = [0]
    for t in range(1, N + 1):
        # Actual source recurrence, independently of the binomial/tangent path.
        b = ((p + 2 * t - 2) * b
             - inv(pow(2, t - 1, modulus), modulus)) \
            * inv(p + 2 * t - 1, modulus) % modulus
        out.append(b)
    delta = (inv(pow(2, N, modulus), modulus) - (p + 2 * N) * b) % modulus
    return out, delta


def expansion(p, modulus):
    m = (p - 1) // 6
    N = 2 * m - 1
    A = 1
    v = 1
    h = 0
    S = 0
    T = 0
    bs = [0]
    diagnostics = []
    for t in range(1, N + 1):
        if t >= 2:
            A = A * (2 * (t - 1)) * inv(2 * t - 1, modulus) % modulus
            v = v * (2 * t - 3) * inv(4 * (t - 1), modulus) % modulus
            h = (h + inv(2 * t - 2, modulus)
                   - inv(2 * t - 1, modulus)) % modulus
        S = (S + v) % modulus
        T = (T + v * (h + inv(2 * t - 1, modulus))) % modulus
        W = (h * S - T) % modulus
        b = (-A * (S + p * W)) % modulus
        bs.append(b)
        diagnostics.append((A, S, W))
    aN, SN, WN = diagnostics[-1]
    d0 = (inv(pow(2, N, modulus), modulus) + 2 * N * aN * SN) % modulus
    d1 = (aN * SN + 2 * N * aN * WN) % modulus
    delta = (d0 + p * d1) % modulus
    return bs, delta, d0, d1, diagnostics


def exact_fraction_spot_check(m):
    p = 6 * m + 1
    N = 2 * m - 1
    A = Fraction(1)
    v = Fraction(1)
    h = Fraction(0)
    S = Fraction(0)
    T = Fraction(0)
    b = Fraction(0)
    for t in range(1, N + 1):
        if t > 1:
            A *= Fraction(2 * (t - 1), 2 * t - 1)
            v *= Fraction(2 * t - 3, 4 * (t - 1))
            h += Fraction(1, 2 * t - 2) - Fraction(1, 2 * t - 1)
        S += v
        T += v * (h + Fraction(1, 2 * t - 1))
        W = h * S - T
        b = (p + 2 * t - 2) * b / (p + 2 * t - 1) \
            - Fraction(1, 2**(t - 1) * (p + 2 * t - 1))
        assert (b + A * (S + p * W)).numerator % p**2 == 0, (m, t, b)
    delta = Fraction(1, 2**N) - (p + 2 * N) * b
    d0 = Fraction(1, 2**N) + 2 * N * A * S
    d1 = A * S + 2 * N * A * W
    assert (delta - d0 - p * d1).numerator % p**2 == 0


def main():
    cases = 0
    stages = 0
    vanishing = []
    for p in target_primes():
        modulus = p * p
        direct, delta = direct_adjoint(p, modulus)
        approx, delta2, d0, d1, _ = expansion(p, modulus)
        assert direct == approx, (
            'adjoint', p,
            [(i, a, b) for i, (a, b) in enumerate(zip(direct, approx)) if a != b][:3]
        )
        assert delta == delta2, ('delta', p, delta, delta2)
        stages += len(direct)  # N individual b_t checks plus terminal delta
        cases += 1
        if delta % p == 0:
            vanishing.append((p, delta, delta // p, d0, d1))
    for m in range(1, 9):
        p = 6 * m + 1
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            exact_fraction_spot_check(m)
    assert cases == 80, (cases, vanishing)
    assert [item[0] for item in vanishing] == [733], vanishing

    p = 733
    modulus = p * p
    _, delta, d0, d1, _ = expansion(p, modulus)
    assert delta == 176653 and delta // p == 241
    assert (delta // p * 610) % p == 410
    print('PASS:', cases, 'target primes 7..997; exact Fraction spot checks for six primes')
    print('PASS:', stages, 'adjoint/terminal congruences mod p^2')
    print('p=733:', {
        'd0_mod_p2': d0, 'd0_div_p_mod_p': d0 // p,
        'd1_mod_p': d1 % p, 'delta_mod_p2': delta,
        'delta_div_p_mod_p': delta // p, 'normalized_adj_face': 410
    })
    print('First-digit zeroes in tested finite range:', vanishing)


if __name__ == '__main__':
    main()
