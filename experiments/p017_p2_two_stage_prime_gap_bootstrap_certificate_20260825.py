#!/usr/bin/env python3
"""Exact integer endpoint certificate for the two-stage uniform-gap P2 bootstrap.

This script verifies only the algebraic transfer interval for the declared
external Campbell/Sorenson-Webster computational inputs. It does not reproduce
or independently certify those prime-gap / Legendre computations.
"""

from math import isqrt


def admissible(K: int, B: int, G: int) -> bool:
    """Exact form of K^2/B + G <= 2K/G."""
    return G * K * K + B * G * G <= 2 * B * K


def main() -> None:
    B = 68_000_000_000_000_000_000
    G = 1724

    disc = B * B - B * G**3
    assert disc > 0
    root_floor = isqrt(disc)

    # Locate the integer endpoints around the exact quadratic roots.
    k_low_floor = (B - root_floor) // G
    k_high_floor = (B + root_floor) // G

    K_min = 1_486_089
    K_max = 78_886_310_903_386_301

    assert k_low_floor == K_min - 1
    assert k_high_floor == K_max

    assert not admissible(K_min - 1, B, G)
    assert admissible(K_min, B, G)
    assert admissible(K_max, B, G)
    assert not admissible(K_max + 1, B, G)

    assert K_max < B
    assert K_min < 70_500_000_000_000  # Sorenson-Webster overlap.

    K2 = K_max * K_max
    assert K2 == 6_223_050_047_945_724_396_985_428_834_462_601
    assert 10**31 < K2 < 10**34

    # A convenient scale comparison: the new finite X reach exceeds 10^31
    # by more than a factor 622.
    assert K2 > 622 * 10**31

    print("P017 two-stage prime-gap bootstrap endpoint certificate: PASS")
    print("B =", B)
    print("G =", G)
    print("K_min =", K_min)
    print("K_max =", K_max)
    print("K_max^2 =", K2)
    print("K_max^2 / 1e31 ~=", K2 / 10**31)


if __name__ == "__main__":
    main()
