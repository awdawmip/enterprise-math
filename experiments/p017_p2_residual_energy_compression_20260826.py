#!/usr/bin/env python3
"""Exact regression certificate for P017 residual-energy compression.

This verifier checks the finite combinatorial identities behind
`docs/P017_P2_RESIDUAL_ENERGY_COMPRESSION_20260826.md`.

It deliberately does not certify a final Lemma-4 constant or an all-K P2
statement.  The logarithmic envelopes in the note are proved analytically;
here we check the exact pre-logarithmic inequalities and the a6 exponent
identities using integer / Fraction arithmetic.
"""

from fractions import Fraction as Q


K_SPLICE = 116_009_280_740_973_308


def floor_nth_root(n: int, k: int) -> int:
    """Largest r with r**k <= n, by exact integer arithmetic."""
    if n < 0 or k <= 0:
        raise ValueError("need n>=0 and k>=1")
    lo, hi = 0, 1
    while hi**k <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return lo


def five_ninth_level_in_k(k: int) -> int:
    # floor(k^(10/9)) exactly.
    return floor_nth_root(k**10, 9)


def hit_count(k: int, modulus: int) -> int:
    return (k * k + 2 * k) // modulus - (k * k) // modulus


def odd_carry(k: int, modulus: int) -> int:
    return hit_count(k, modulus) - hit_count(k, 2 * modulus)


def ordinary_remainder(k: int, modulus: int) -> Q:
    return Q(hit_count(k, modulus)) - Q(2 * k, modulus)


def centered_carry(k: int, modulus: int) -> Q:
    return Q(odd_carry(k, modulus)) - Q(k, modulus)


def exact_sharp_energy(k: int, level: int) -> Q:
    return sum(
        (
            centered_carry(k, m) ** 2
            for m in range(k + 1, level + 1)
            if m % 2 == 1
        ),
        Q(0),
    )


def exact_active_count(k: int, level: int) -> int:
    return sum(
        odd_carry(k, m)
        for m in range(k + 1, level + 1)
        if m % 2 == 1
    )


def root_mass_upper(k: int, level: int) -> Q:
    """Exact pre-log upper bound sum_{a>K^2/D, odd}(K/a+1)."""
    total = Q(0)
    for a in range(1, k + 1, 2):
        if a * level > k * k:
            total += Q(k, a) + 1
    return total


def odd_square_tail_upper(k: int) -> Q:
    # From spacing 2: sum_{odd m>K} 1/m^2 <= 1/K^2 + 1/(2K).
    return Q(1, k * k) + Q(1, 2 * k)


def interval_odd_carry(left: int, length: int, modulus: int) -> int:
    hm = (left + length) // modulus - left // modulus
    h2m = (left + length) // (2 * modulus) - left // (2 * modulus)
    return hm - h2m


def exact_short_support(k: int, level: int, left: int, length: int) -> int:
    return sum(
        1
        for m in range(k + 1, level + 1)
        if m % 2 == 1 and interval_odd_carry(left, length, m) != 0
    )


def quotient_support_upper(k: int, level: int, left: int, length: int) -> Q:
    """Exact pre-log envelope sum_q (L/q+1) over possible odd quotients."""
    total = Q(0)
    for q in range(1, k + 1, 2):
        if q * level > left:
            total += Q(length, q) + 1
    return total


def check_exponents() -> None:
    level_k = Q(10, 9)
    generic_energy_k = level_k
    pmin_k = Q(22, 27)
    z_k = Q(5, 27)
    qmax_k = 2 - 2 * pmin_k

    assert generic_energy_k - 1 == Q(1, 9)
    assert (generic_energy_k - 1) / 2 == Q(1, 18)  # convert K exponent to X
    assert pmin_k * 2 == Q(44, 27) > 1
    assert qmax_k == Q(10, 27)
    assert qmax_k == 2 * z_k


def check_sharp_regressions(k_max: int = 300) -> None:
    for k in range(2, k_max + 1):
        level = five_ninth_level_in_k(k)
        if level <= k:
            continue

        for m in range(k + 1, level + 1):
            if m % 2 == 0:
                continue
            # P2-R02 Boolean super-root carry.
            assert odd_carry(k, m) in (0, 1)
            # P2-R03 exact Chen bridge.
            assert centered_carry(k, m) == (
                ordinary_remainder(k, m) - ordinary_remainder(k, 2 * m)
            )

        energy = exact_sharp_energy(k, level)
        active = exact_active_count(k, level)

        # Boolean energy reduction before any harmonic relaxation.
        assert energy <= Q(active) + k * k * odd_square_tail_upper(k)

        # Reciprocal-window / root-mass carrier upper bound.
        assert Q(active) <= root_mass_upper(k, level)


def check_short_interval_support(k_max: int = 45) -> None:
    """Exhaust all integer subintervals of length <=K at small K."""
    for k in range(3, k_max + 1):
        level = five_ninth_level_in_k(k)
        if level <= k:
            continue
        basin_left = k * k
        basin_right = k * k + 2 * k

        for left in range(basin_left, basin_right):
            max_length = min(k, basin_right - left)
            for length in range(1, max_length + 1):
                for m in range(k + 1, level + 1):
                    if m % 2 == 1:
                        # Support length <=K<2m: at most one odd quotient hit.
                        assert interval_odd_carry(left, length, m) in (0, 1)

                support = exact_short_support(k, level, left, length)
                assert Q(support) <= quotient_support_upper(
                    k, level, left, length
                )


def splice_diagnostics() -> None:
    k = K_SPLICE
    level = five_ninth_level_in_k(k)

    # Exact level inequalities.
    assert level**9 <= k**10 < (level + 1) ** 9

    # The a6 collision small-core exponent is z^2 in K variables.
    # At the splice we only print integer-scale diagnostics; no theorem
    # depends on floating-point values here.
    print("K_splice =", k)
    print("floor(K^(10/9)) =", level)
    print("level / K ~=", level / k)
    print("K^(1/9) ~=", k ** (1 / 9))
    print("z = K^(5/27) ~=", k ** (5 / 27))
    print("z^2 = K^(10/27) ~=", k ** (10 / 27))


def main() -> None:
    check_exponents()
    check_sharp_regressions()
    check_short_interval_support()
    splice_diagnostics()
    print("P017 residual-energy compression certificate: PASS")


if __name__ == "__main__":
    main()
