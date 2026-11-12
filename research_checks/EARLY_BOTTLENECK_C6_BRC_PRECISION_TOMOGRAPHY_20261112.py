"""Exact rational checks for the 2026-11-12 bounded-height C6 BRC tomography note.

No numerical/physical X6 dynamical claims are made by these tests.
Source note: research_notes/early_bottleneck_revisit_20261112_c6_rational_precision.md
"""
from fractions import Fraction as Q
from random import Random

IDENTITY = ((Q(1), Q(0)), (Q(0), Q(1)))


def multiply(a, b):
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(2)), Q(0))
              for j in range(2))
        for i in range(2)
    )


def transfer(t):
    return ((Q(1), t), (Q(1), Q(0)))


def product(weights):
    matrix = IDENTITY
    for weight in weights:
        matrix = multiply(matrix, transfer(weight))
    return matrix


def inverse(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    assert det != 0
    return (
        (a[1][1] / det, -a[0][1] / det),
        (-a[1][0] / det, a[0][0] / det),
    )


def four_origins(weights):
    assert len(weights) == 6
    return [product(weights[j:] + weights[:j]) for j in range(4)]


def round_binary(x, bits):
    """Exact nearest-grid rounding, with deterministic upper tie break."""
    scaled = x * (1 << bits)
    quotient, rem = divmod(scaled.numerator, scaled.denominator)
    if 2 * rem >= scaled.denominator:
        quotient += 1
    return Q(quotient, 1 << bits)


def decode(rounded_origins, height):
    limit = height ** 6
    matrices = [
        tuple(tuple(entry.limit_denominator(limit) for entry in row)
              for row in matrix)
        for matrix in rounded_origins
    ]
    prefix = [
        matrices[j + 1][0][1] / matrices[j][1][0]
        for j in range(3)
    ]
    residual = multiply(matrices[3], inverse(product(prefix)))
    assert residual[1][1] > 0
    return prefix + [
        residual[0][1] / residual[1][1] - 1,
        residual[1][0] - 1,
        residual[1][1],
    ]


def test_main():
    rng = Random(20261112)
    for height in range(2, 7):
        bits = 12 * (height - 1).bit_length() + 3
        for _ in range(100):
            weights = [
                Q(rng.randint(1, height), rng.randint(1, height))
                for _ in range(6)
            ]
            originals = four_origins(weights)
            observed = [
                tuple(tuple(round_binary(entry, bits) for entry in row)
                      for row in matrix)
                for matrix in originals
            ]
            reconstructed = [
                tuple(tuple(entry.limit_denominator(height ** 6)
                            for entry in row)
                      for row in matrix)
                for matrix in observed
            ]
            assert reconstructed == originals
            assert decode(observed, height) == weights

    u = [Q(1, 2), Q(1, 2), Q(1, 2), Q(1, 2), Q(2), Q(2)]
    v = [Q(1, 2), Q(1, 2), Q(1), Q(2), Q(1, 2), Q(1)]
    assert u != v
    assert four_origins(u)[:3] == four_origins(v)[:3]
    assert four_origins(u)[3] != four_origins(v)[3]
    print("PASS 500/500 bounded-height exact reconstructions; 3-origin collision")


if __name__ == "__main__":
    test_main()
