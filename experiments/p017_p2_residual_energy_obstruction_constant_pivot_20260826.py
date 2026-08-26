#!/usr/bin/env python3
"""Exact/integer certificate for the P017 residual-energy obstruction and constant pivot.

This checker certifies the exact rational exponent identities, the dyadic rho=2
reciprocal-block constant bookkeeping, and the finite T4 x T4 packet ledger at
the conservative Tier-A splice.  It intentionally uses only Python integers and
fractions.Fraction.
"""

from fractions import Fraction as Q


THETA = Q(4999, 10000)
D_EXP = Q(5, 9)
A = Q(6)
B = Q(22, 5)
C = Q(27, 5)
MU = Q(31, 72)
NU = Q(1, 8)

K_SPLICE = 116_009_280_740_973_308
X_SPLICE = K_SPLICE * K_SPLICE


def ceil_power_ratio(k: int, num: int, den: int) -> int:
    """Return ceil(k**(num/den)) by exact integer comparisons."""
    if k < 1 or num < 0 or den <= 0:
        raise ValueError
    lo, hi = 0, k + 1
    target = k**num
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**den >= target:
            hi = mid
        else:
            lo = mid
    return hi


def omega_table(n: int) -> list[int]:
    """Return omega(m), the number of distinct prime divisors, for 0<=m<=n."""
    omega = [0] * (n + 1)
    is_prime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        is_prime[0] = 0
    if n >= 1:
        is_prime[1] = 0
    limit = int(n**0.5)
    for p in range(2, limit + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            for m in range(p, n + 1, p):
                omega[m] += 1
    return omega


def count_odd_inclusive(lo: int, hi: int) -> int:
    if hi < lo:
        return 0
    first = lo if lo & 1 else lo + 1
    last = hi if hi & 1 else hi - 1
    if last < first:
        return 0
    return (last - first) // 2 + 1


def odd_packet_count(k: int, q: int) -> int:
    """Count odd P with k^2 < P*q < (k+1)^2."""
    low = k * k // q + 1
    high = ((k + 1) * (k + 1) - 1) // q
    return count_odd_inclusive(low, high)


def main() -> None:
    # Root-edge source identities and scalar envelopes.
    delta = 2 * C - B - 1
    assert delta == C == Q(27, 5)
    assert D_EXP * C / A == Q(1, 2)
    assert D_EXP * B / A == Q(11, 27)

    t1 = (C - B) / delta
    t2 = (A / delta) * ((B + 1) / (2 * A) - 1 / A)
    t3 = (B + 1 - 2) / delta
    t4 = (C - B) / delta
    assert (t1, t2, t3, t4) == (Q(5, 27), Q(17, 54), Q(17, 27), Q(5, 27))
    assert 1 - Q(22, 27) == Q(5, 27)
    assert 1 - 2 * THETA == Q(1, 5000)

    # Dyadic rho=2 reciprocal block.
    lower_margin = 1 - 2 * NU - Q(5, 3) * MU
    assert lower_margin == Q(7, 216)
    assert 2**720 < 10**217  # therefore 2^(720/7) < 10^31
    assert 48 * 48 < 28 * 28 * 3  # 48/sqrt(3) < 28
    assert 49 < 50  # 1/sqrt(2) < 5/7
    assert Q(28) + Q(48, 7) < 35

    # Explicit a6 B-spline companion: p=6, eta=13/900.
    eta = Q(13, 900)
    c6_crude = Q(2 * 6**6, 3**6 * 5)
    assert c6_crude == Q(128, 5)

    diag_square_exp = MU - THETA + eta
    off_square_exp = (
        2 * (D_EXP - THETA)
        + (1 - THETA) / 2
        + Q(5, 2) * eta
        - MU
    )
    tail_saving = 5 * eta - (D_EXP - THETA)
    upper_margin = 3 * MU - (D_EXP + 1 + eta - THETA - NU)

    assert diag_square_exp == -Q(549, 10000)
    assert -diag_square_exp / 2 == Q(549, 20000)
    assert off_square_exp == -Q(397, 12000)
    assert -off_square_exp / 2 == Q(397, 24000)
    assert tail_saving == Q(497, 30000)
    assert upper_margin == Q(10397, 30000) > Q(1, 3)

    # Conservative Tier-A finite splice and T4 x T4 small-core range.
    assert X_SPLICE == 13_458_153_218_037_960_469_637_923_168_462_864
    p_min = ceil_power_ratio(K_SPLICE, 22, 27)
    assert p_min == 80_241_952_393_051
    q_max = (((K_SPLICE + 1) ** 2 - 1) // (p_min * p_min))
    assert q_max == 2_090_174
    assert q_max < 2**21
    assert K_SPLICE**3 > 2**170

    # Coefficient-uniform all-odd-P packet ledger.  This deliberately ignores
    # the semiprime P restriction and uses the worst internal 2*4^omega(Q).
    omega = omega_table(q_max)
    unweighted = 0
    weighted_num = 0
    weighted_den = 4 * 170 * 170

    for q in range(1, q_max + 1, 2):
        count_p = odd_packet_count(K_SPLICE, q)
        if count_p == 0:
            continue
        multiplicity = 2 * (4 ** omega[q])
        contribution = count_p * multiplicity
        unweighted += contribution

        j = q.bit_length() - 1  # 2^j <= q < 2^(j+1)
        # log(q)/log(K) < 3(j+1)/170, so paired T4 weight is
        # < 9(j+1)^2 / (4*170^2).
        weighted_num += contribution * 9 * (j + 1) ** 2

    weighted = Q(weighted_num, weighted_den)
    assert unweighted < 427 * K_SPLICE
    assert weighted < Q(883, 100) * K_SPLICE

    print("P017 residual-energy obstruction / constant-pivot certificate: PASS")
    print("W1 scalar envelopes:", t1, t2, t3, t4)
    print("rho=2 reciprocal constant <= 35")
    print(
        "a6 p=6 eta=13/900 deltas:",
        -diag_square_exp / 2,
        -off_square_exp / 2,
        tail_saving,
    )
    print("finite T4 pmin =", p_min)
    print("finite T4 qmax =", q_max)
    print("unweighted crude packet ledger / K =", float(Q(unweighted, K_SPLICE)))
    print("weighted dyadic packet ledger upper / K =", float(weighted / K_SPLICE))
    print("weighted dyadic packet ledger < 8.83 K")


if __name__ == "__main__":
    main()
