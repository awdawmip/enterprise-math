"""Independent exact finite checks of the owner's raw-marginal stability bound.

The mathematical audit supplies the general induction; finite checks here are
regressions and boundary witnesses, never a substitute for that induction.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import json
from math import comb
import random


@lru_cache(None)
def constant(n, k):
    if k in (0, n):
        return Fraction(1)
    return ((n - k) * constant(n - 1, k) + 2 * k * constant(n - 1, k - 1)) / n


def marginal_norm_sum(array, n, k, *, min_zero=False):
    result = Fraction(0)
    for axes in combinations(range(n), k):
        projected = defaultdict(Fraction)
        for point, weight in array.items():
            address = tuple(point[axis] for axis in axes)
            if min_zero and address:
                offset = min(address)
                address = tuple(value - offset for value in address)
            projected[address] += weight
        result += sum(abs(value) for value in projected.values())
    return result


def check(array, n, k):
    assert sum(value > 0 for value in array.values()) < 2 ** k
    norm = sum(abs(value) for value in array.values())
    defect = marginal_norm_sum(array, n, k)
    assert norm <= constant(n, k) * defect, (array, n, k, norm, defect)


def run():
    exhaustive_count = 0
    cube3 = tuple(product((0, 1), repeat=3))
    for coefficients in product((-1, 0, 1), repeat=8):
        array = {point: Fraction(value) for point, value in zip(cube3, coefficients) if value}
        for k in range(4):
            if sum(value > 0 for value in coefficients) < 2 ** k:
                check(array, 3, k)
                exhaustive_count += 1
    rng = random.Random(202609071203)
    cube6 = tuple(product((-4, 3), repeat=6))
    for trial in range(160):
        positives = rng.sample(cube6, rng.randrange(8))
        negatives = rng.sample([point for point in cube6 if point not in positives], rng.randrange(1, 28))
        array = {point: Fraction(rng.randrange(1, 20), rng.randrange(1, 11)) for point in positives}
        array.update({point: -Fraction(rng.randrange(1, 20), rng.randrange(1, 11)) for point in negatives})
        check(array, 6, 3)
    # At eight positive cells, four active axes give a zero three-axis defect.
    parity = {point + (0, 0): Fraction((-1) ** sum(point)) for point in product((0, 1), repeat=4)}
    assert sum(value > 0 for value in parity.values()) == 8
    assert marginal_norm_sum(parity, 6, 3) == 0
    assert sum(abs(value) for value in parity.values()) == 16
    # A diagonal raw translation is invisible to every local min-zero chart.
    diagonal = {(0,) * 6: Fraction(1), (1,) * 6: Fraction(-1)}
    assert marginal_norm_sum(diagonal, 6, 3, min_zero=True) == 0
    assert marginal_norm_sum(diagonal, 6, 3) == 40
    # n=4,k=3 is sharp for the stated recurrence: parity minus one positive cell.
    punctured = {point: Fraction((-1) ** sum(point)) for point in product((0, 1), repeat=4)
                 if point != (0,) * 4}
    assert sum(abs(value) for value in punctured.values()) == 15
    assert marginal_norm_sum(punctured, 4, 3) == 4
    check(punctured, 4, 3)
    for n in range(13):
        for k in range(n + 1):
            numerator = sum((-1) ** (k - j) * 2 ** j * comb(n, j) for j in range(k + 1))
            assert constant(n, k) == Fraction(numerator, comb(n, k))
    return {
        "status": "PASS",
        "arithmetic": "Fraction only",
        "exhaustive_n3_array_k_cases": exhaustive_count,
        "random_n6_k3_cases": 160,
        "C_6_3": str(constant(6, 3)),
        "two_candidate_total_noise_constant": str(2 * constant(6, 3)),
        "each_table_noise_constant": str(2 * comb(6, 3) * constant(6, 3)),
        "boundary_witnesses": ["eight-positive parity", "min-zero diagonal collapse", "n4_k3_sharpness"],
        "scope": "finite checks plus explicit boundary witnesses; general proof is in the independent audit",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
