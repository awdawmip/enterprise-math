#!/usr/bin/env python3
"""Exact finite checker for the Viète 2-adic root-gauge classification.

This checker extends the existing Euler/Viète rotation-refinement tool family; it
uses only integer/Fraction arithmetic and imports no pi or trigonometric function.
"""
from fractions import Fraction
from math import gcd

from enterprise_math import euler_rotation_refinement as err


def least_signed_residue(alpha: int, modulus: int) -> int:
    r = alpha % modulus
    if r > modulus // 2:
        r -= modulus
    return r


def alpha_residue(alpha: int, depth: int) -> int:
    return alpha % (1 << (depth + 1))


def root_state(alpha: int, depth: int) -> int:
    return (3 * alpha_residue(alpha, depth)) % err.phase_order(depth)


def phase_distance(alpha: int, depth: int) -> Fraction:
    if depth < 1:
        raise ValueError("depth must be at least 1")
    modulus = 1 << (depth + 1)
    r = least_signed_residue(alpha, modulus)
    return Fraction(abs(r), modulus)


def strictly_refining(alpha: int, max_depth: int) -> bool:
    distances = [phase_distance(alpha, m) for m in range(1, max_depth + 1)]
    return all(b < a for a, b in zip(distances, distances[1:]))


def main() -> None:
    checks = 0

    # Through finite depth M there are exactly 2^M primitive pure-2 gauges,
    # represented by odd alpha modulo 2^(M+1).
    for max_depth in range(1, 13):
        modulus = 1 << (max_depth + 1)
        alphas = list(range(1, modulus, 2))
        assert len(alphas) == 1 << max_depth
        checks += 1

        monotone = []
        forward = []
        for alpha in alphas:
            # Every finite projection is pure 2-primary primitive.
            for depth in range(max_depth + 1):
                state = root_state(alpha, depth)
                order = err.phase_order(depth)
                assert state % 3 == 0
                assert gcd(state // 3, 2) == 1
                assert err.element_order(state, depth) == 1 << (depth + 1)
                checks += 3

            # Projective compatibility and square-root compatibility.
            for depth in range(max_depth):
                coarse = root_state(alpha, depth)
                fine = root_state(alpha, depth + 1)
                assert fine % err.phase_order(depth) == coarse
                assert (2 * fine) % err.phase_order(depth + 1) == err.coarse_embed(
                    coarse, depth
                )
                checks += 2

            if strictly_refining(alpha, max_depth):
                monotone.append(alpha)
                if alpha % 4 == 1:
                    forward.append(alpha)

        # The only all-level strictly improving truncations are ±1.
        assert monotone == [1, modulus - 1]
        assert forward == [1]
        checks += 2

    # Exact high-bit-jump lower bound: any changed least representative creates
    # a next-level normalized phase distance >= 1/4.
    for depth in range(1, 12):
        coarse_modulus = 1 << (depth + 1)
        fine_modulus = coarse_modulus << 1
        for alpha in range(1, fine_modulus, 2):
            r0 = least_signed_residue(alpha, coarse_modulus)
            r1 = least_signed_residue(alpha, fine_modulus)
            assert r1 == r0 or abs(r1 - r0) == coarse_modulus
            if r1 != r0:
                assert Fraction(abs(r1), fine_modulus) >= Fraction(1, 4)
            checks += 2

    # Principal and inverse towers have exact distance halving.
    for alpha in (1, -1):
        for depth in range(1, 16):
            assert phase_distance(alpha, depth + 1) == phase_distance(alpha, depth) / 2
            checks += 1

    print(
        "PASS VIETE_2ADIC_ROOT_GAUGE; "
        f"checks={checks}; "
        "finite_tower_count_at_depth_M=2^M; "
        "strict_refinement_survivors=2; "
        "forward_chirality_survivors=1; "
        "high_bit_jump_distance_lower_bound=1/4; "
        "principal_alpha=1; inverse_alpha=-1"
    )


if __name__ == "__main__":
    main()
