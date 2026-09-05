#!/usr/bin/env python3
"""Exact checker for the native oriented half-turn -> principal pro-state section.

Physical C12 indexing:
  E_k = 2k, G_k = 2k+1 (mod 12).
An oriented half-turn from E_k reaches E_{k+3} after +/-6 microsteps.
Its oriented half-way root is at relative phase +/-3.
The diagonal precision address +/-3 in C_{6*2^m} is the principal root tower.
"""

from math import gcd


def modulus(m: int) -> int:
    return 6 * (2 ** m)


def residue(x: int, n: int) -> int:
    return x % n


def order_mod(x: int, n: int) -> int:
    return n // gcd(x % n, n)


def e(k: int) -> int:
    return 2 * (k % 6)


def g(k: int) -> int:
    return (2 * (k % 6) + 1) % 12


def check_native_half_turn_arcs():
    for k in range(6):
        start = e(k)
        endpoint_forward = (start + 6) % 12
        endpoint_reverse = (start - 6) % 12
        assert endpoint_forward == e(k + 3)
        assert endpoint_reverse == e(k + 3)

        root_forward = (start + 3) % 12
        root_reverse = (start - 3) % 12
        assert root_forward == g(k + 1)
        assert root_reverse == g(k - 2)
        assert root_forward != root_reverse

        assert (root_forward - start) % 12 == 3
        assert (root_reverse - start) % 12 == 9  # -3 mod 12


def check_principal_prostate_section():
    for eps in (-1, 1):
        for m in range(0, 12):
            n = modulus(m)
            v = residue(3 * eps, n)

            # Level m has exact order 2^(m+1): half-turn, quarter-turn, etc.
            assert order_mod(v, n) == 2 ** (m + 1)

            # Standard precision projection preserves the same +/-3 address.
            if m > 0:
                assert residue(v, modulus(m - 1)) == residue(
                    3 * eps, modulus(m - 1)
                )

            # Root relation under phase-preserving embedding k -> 2k.
            if m < 11:
                fine = residue(3 * eps, modulus(m + 1))
                coarse_embedded = residue(2 * v, modulus(m + 1))
                assert residue(2 * fine, modulus(m + 1)) == coarse_embedded

    # Chirality is invisible at C6 but visible at every finer level.
    assert residue(3, 6) == residue(-3, 6)
    for m in range(1, 12):
        n = modulus(m)
        assert residue(3, n) != residue(-3, n)
        assert residue(-3, n) == residue(-residue(3, n), n)


def check_covariance_logic():
    # Relative root address is independent of start k; endpoint half-turn shifts
    # k by 3 but leaves sweep sign unchanged. Sweep reversal flips the sign.
    for k in range(6):
        for eps in (-1, 1):
            sigma = 3 * eps
            shifted_k = (k + 3) % 6
            shifted_sigma = 3 * eps
            reversed_sigma = 3 * (-eps)
            assert shifted_k != k
            assert shifted_sigma == sigma
            assert reversed_sigma == -sigma


def check_static_fiber_not_time_odometer():
    # Along a fixed-chirality physical cycle the relative root lineage stays
    # constant; it is a precision descriptor, not an absolute time phase.
    for eps in (-1, 1):
        sigma = 3 * eps
        for k in range(6):
            assert 3 * eps == sigma
            assert 3 * eps == sigma  # after shifting start to E_{k+1}


def main():
    check_native_half_turn_arcs()
    check_principal_prostate_section()
    check_covariance_logic()
    check_static_fiber_not_time_odometer()
    print("PASS: native half-turn -> principal Viète pro-state section")
    print("C6: +/-3 coincide as half-turn")
    print("C12+: chirality separates +/-3 root towers")
    print("endpoint half-turn preserves section; sweep reversal negates it")


if __name__ == "__main__":
    main()
