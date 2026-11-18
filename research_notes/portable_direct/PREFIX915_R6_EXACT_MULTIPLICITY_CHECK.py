#!/usr/bin/env python3
"""PREFIX-915: exact count of source-labeled bit-flip collision witnesses.

All arithmetic is integer exact; brute checks are exhaustive for 2 <= p <= 9.
No external dependencies or global research-state mutations.
"""
from itertools import product
import json


def count_bit_ones_below(z: int, bit: int) -> int:
    """Count n in [0,z) whose indicated binary bit equals one."""
    assert z >= 0 and bit >= 0
    h = 1 << bit
    period = h << 1
    return (z // period) * h + max(0, z % period - h)


def exact_witness_count(p: int, A: int, i: int, j: int,
                        eps: int, eta: int) -> int:
    """Count x with 0 <= x < 2**p-A, bit_i(x)=(eps==-1),
    and bit_j(x+A)=(eta==-1), for 0<=j<i<p and 0<=A<2**p.
    """
    N = 1 << p
    assert 0 <= j < i < p and 0 <= A < N
    assert eps in (-1, 1) and eta in (-1, 1)
    H, T = 1 << i, 1 << (i + 1)
    whole, rem = divmod(N - A, T)
    target_i = int(eps == -1)
    target_j = int(eta == -1)
    tail = max(0, min(H, rem - target_i * H))
    ones = count_bit_ones_below(A + tail, j) - count_bit_ones_below(A, j)
    return whole * (H // 2) + (ones if target_j else tail - ones)


def brute_count(p: int, A: int, i: int, j: int,
                eps: int, eta: int) -> int:
    """Independent exhaustive direct binary-bit test on a small p-bit state."""
    return sum(
        ((x >> i) & 1) == int(eps == -1)
        and (((x + A) >> j) & 1) == int(eta == -1)
        for x in range((1 << p) - A)
    )


def verify_modular_witness(a: int, b: int, k: int, ell: int,
                           i: int, j: int, eps: int, eta: int,
                           x: int, p: int = 32) -> None:
    N, A = 1 << p, k * a
    assert k * a - ell * b == eps * (1 << i) - eta * (1 << j)
    y = x + A
    assert 0 <= x < N and 0 <= y < N
    assert (x ^ (1 << i)) == x + eps * (1 << i)
    assert (y ^ (1 << j)) == y + eta * (1 << j)
    assert (y - x) % a == 0
    assert ((y ^ (1 << j)) - (x ^ (1 << i))) % b == 0


def main() -> None:
    cases = 0
    for p in range(2, 10):
        for A in range(1, 1 << p):
            for i in range(1, p):
                for j in range(i):
                    for eps, eta in product((-1, 1), repeat=2):
                        formula = exact_witness_count(p, A, i, j, eps, eta)
                        direct = brute_count(p, A, i, j, eps, eta)
                        assert formula == direct, (p, A, i, j, eps, eta, formula, direct)
                        cases += 1

    # PREFIX-914 new pair: beyond total-capacity collision threshold.
    a, b, k, ell, i, j, eps, eta = 321651, 440665, 3, 1, 20, 19, 1, 1
    A = k * a
    assert 3 * a - b == (1 << i) - (1 << j)
    assert a * b > 33 * (1 << 32)
    verify_modular_witness(a, b, k, ell, i, j, eps, eta, 83623)
    count914 = exact_witness_count(32, A, i, j, eps, eta)
    assert A <= (1 << i) and count914 == (1 << 30)

    # PREFIX-913 witness: exact terminal-truncation correction.
    a2, b2, k2, ell2, i2, j2, eps2, eta2 = (
        271999, 521085, 3, 1, 18, 15, 1, -1
    )
    verify_modular_witness(a2, b2, k2, ell2, i2, j2,
                           eps2, eta2, 3203)
    count913 = exact_witness_count(32, k2 * a2, i2, j2, eps2, eta2)
    assert count913 == 1073610752

    print(json.dumps({
        "schema": "PREFIX915_R6_EXACT_MULTIPLICITY_CERTIFICATE_V1",
        "arithmetic": "exact Python integers",
        "exhaustive_small_p": "2..9",
        "exhaustive_parameter_cases": cases,
        "small_p_mismatches": 0,
        "prefix914_pair": [321651, 440665],
        "prefix914_fixed_trajectory_pair_count": count914,
        "prefix913_pair": [271999, 521085],
        "prefix913_fixed_trajectory_pair_count": count913,
        "scientific_frozen_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d"
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
