"""Exact fixed-depth ancestor densities for triangular multiples by 6.

Run with Python 3.8+ and the standard library. Output is the complete JSON certificate.
"""

import json
from fractions import Fraction
from math import isqrt


SEEDS = ((7, 3), (17, 7))
MAX_DEPTH = 9


def next_pell(y, z):
    return 5 * y + 12 * z, 2 * y + 5 * z


def sign_in_quadratic(a, b, radicand=6):
    """Sign of a+b sqrt(radicand), including zero, for nonsquare radicands."""
    if a == 0:
        return (b > 0) - (b < 0)
    sign_a = (a > 0) - (a < 0)
    if b == 0 or (a > 0) == (b > 0):
        return sign_a
    norm = a * a - radicand * b * b
    return sign_a * ((norm > 0) - (norm < 0))


def limiting_depth(y, z, depth_bound):
    """Periodic gate at large height, evaluated on residues of the Pell pair."""
    previous = 0
    for j in range(1, depth_bound + 1):
        scale = 6 ** ((j + 1) // 2)
        base, multiplier = (y, 6) if j % 2 else (z, 1)
        residue = (scale - base) % (2 * scale)
        admissible = []
        for shift in (residue - 2 * scale, residue):
            above_lower = sign_in_quadratic(2 * scale - multiplier * previous, shift)
            below_upper = sign_in_quadratic(2 * scale + multiplier * previous, -shift)
            if above_lower > 0 and below_upper > 0:
                assert abs(shift) < 2 * scale
                admissible.append(shift)
        if not admissible:
            return j - 1
        assert len(admissible) == 1
        previous = admissible[0]
    return depth_bound


def positive_predecessor(z):
    """Read the original squared bracketing gate on positive odd coordinates."""
    lower = (z - 2) ** 2 + 5
    upper = (z + 2) ** 2 + 5
    x = max(3, isqrt(lower // 6) + 1)
    if not x % 2:
        x += 1
    if 6 * x * x >= upper:
        return None
    assert lower < 6 * x * x and 6 * (x + 2) ** 2 >= upper
    return x


def actual_chain(z, depth_bound):
    chain = [z]
    for _ in range(depth_bound):
        parent = positive_predecessor(chain[-1])
        if parent is None:
            break
        chain.append(parent)
    return chain


def gate_word(seed, depth):
    modulus = 2 * 6 ** ((depth + 1) // 2)
    start = tuple(coordinate % modulus for coordinate in seed)
    y, z = start
    word = []
    while True:
        word.append(limiting_depth(y, z, depth) == depth)
        y, z = (coordinate % modulus for coordinate in next_pell(y, z))
        if (y, z) == start:
            return word


def minimal_period(word):
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and all(v == word[j % period] for j, v in enumerate(word)):
            return period
    raise AssertionError("finite word must have a period")


def individual_checks(seed, rank_bound=667):
    y, z = seed
    early_exceptions = [[] for _ in range(MAX_DEPTH)]
    stability_ranks = [None] * MAX_DEPTH
    for n in range(rank_bound + 1):
        assert y * y - 6 * z * z == -5
        true_depth = len(actual_chain(z, MAX_DEPTH)) - 1
        predicted_depth = limiting_depth(y, z, MAX_DEPTH)
        for j in range(1, MAX_DEPTH + 1):
            scale = 6 ** ((j + 1) // 2)
            above_threshold = z >= 200 * scale**3
            if above_threshold and stability_ranks[j - 1] is None:
                stability_ranks[j - 1] = n
            if (true_depth >= j) != (predicted_depth >= j):
                assert not above_threshold and true_depth < j
                early_exceptions[j - 1].append(n)
        assert (true_depth >= 1) == (n % 2 == 0 and (seed != (7, 3) or n != 0))
        y, z = next_pell(y, z)
    assert None not in stability_ranks
    return {
        "seed_Y_Z": seed,
        "max_rank_checked_from_zero": rank_bound,
        "first_rank_above_proved_height_by_depth": stability_ranks,
        "ranks_to_remove_from_periodic_word_by_depth": early_exceptions,
    }


def triangular(k):
    return k * (k + 1) // 2


def forward_crosscheck(index_bound):
    """Calculate all one-step children using triangular numbers instead of Pell data."""
    image = {}
    for k in range(1, index_bound + 1):
        value = 6 * triangular(k)
        m = (isqrt(8 * value + 1) - 1) // 2
        children = (m,) if triangular(m) == value else (m, m + 1)
        for child in children:
            assert child not in image
            image[child] = k
    for j in range(1, index_bound + 1):
        x = positive_predecessor(2 * j + 1)
        assert image.get(j) == (None if x is None else (x - 1) // 2)


def modular_orbit_order_checks():
    def multiply(left, right, modulus):
        a, b = left
        c, d = right
        return (a * c + 6 * b * d) % modulus, (a * d + b * c) % modulus

    def transform(seed, exponent, modulus):
        unit = (5, 2)
        out = seed
        while exponent:
            if exponent % 2:
                out = multiply(out, unit, modulus)
            exponent //= 2
            unit = multiply(unit, unit, modulus)
        return out

    tested = list(range(1, 41)) + [64, 128, 256]
    for e in tested:
        modulus = 2 * 6**e
        predicted = 6 if e == 1 else 2**e * 3 ** (e - 1)
        for seed in SEEDS:
            start = tuple(component % modulus for component in seed)
            assert transform(start, predicted, modulus) == start
            for prime in (2, 3):
                assert transform(start, predicted // prime, modulus) != start
    return {"exponents_e_checked": tested, "seeds": len(SEEDS), "proper_prime_divisors_tested": [2, 3]}


def geometry_checks():
    def switching_allowed(fraction):
        return sign_in_quadratic(21 - 2 * fraction, -9 + 2 * fraction) >= 0

    unresolved = []
    for a in range(1, 501):
        fraction = Fraction(5, a) % 1
        if a != 2 and switching_allowed(fraction) and switching_allowed(1 - fraction):
            unresolved.append(a + 2)
    assert unresolved == list(range(10, 16))
    assert not switching_allowed(Fraction(1, 100))  # beyond a=500, f<1/100
    assert sign_in_quadratic(-23, 9, 7) > 0
    assert sign_in_quadratic(6, -2, 8) > 0

    def forward_endpoints(s, r, k):
        a, c = s - 2, s - 4
        z = 2 * a * k - c
        value = r * z * z - (r - 1) * c * c
        t = isqrt(value)
        lower = (c + t) // (2 * a)
        exact = t * t == value and (c + t) % (2 * a) == 0
        return lower, lower if exact else lower + 1

    checked = 0
    for s in range(3, 19):
        if s == 4:
            continue
        for r in (5, 6, 7, 8, 10, 11, 12, 13, 14, 15):
            for k in range(1, 151):
                lower, upper = forward_endpoints(s, r, k)
                first_right, _ = forward_endpoints(s, r, k + 1)
                assert upper > k and first_right > upper
                assert (lower == k) == (k == 1 and s > r)
                checked += 1
    return {
        "r6_open_cells_after_switch_test": unresolved,
        "ordered_adjacent_transitions_checked": checked,
    }


def certificate():
    small = []
    for z in range(3, 30, 2):
        y = isqrt(6 * z * z - 5)
        if y * y == 6 * z * z - 5:
            small.append((y, z))
    assert small == [SEEDS[0], SEEDS[1], next_pell(*SEEDS[0])]
    forward_crosscheck(20000)
    density_table = []
    for depth in range(1, MAX_DEPTH + 1):
        words = [gate_word(seed, depth) for seed in SEEDS]
        periods = [minimal_period(word) for word in words]
        densities = [Fraction(sum(word), len(word)) for word in words]
        density_table.append({
            "H": depth,
            "modulus": 2 * 6 ** ((depth + 1) // 2),
            "orbit_lengths": [len(word) for word in words],
            "accepted_ranks_per_orbit": [sum(word) for word in words],
            "minimal_indicator_periods": periods,
            "densities_by_seed": [str(density) for density in densities],
            "density_by_equal_hit_index": str(sum(densities) / 2),
        })
    examples = {}
    for z in [3, 7, 29, 69, 287]:
        chain = actual_chain(z, MAX_DEPTH)
        examples[str((z - 1) // 2)] = [(x - 1) // 2 for x in chain]
    return {
        "cell_s_r": [3, 6],
        "small_positive_shell_pairs_Z_below_30": small,
        "forward_triangular_oracle_through_index": 20000,
        "fixed_depths": density_table,
        "exact_original_gate_checks": [individual_checks(seed) for seed in SEEDS],
        "backward_chains_by_target_index": examples,
        "normalized_limit_coding": geometry_checks(),
        "full_matrix_period_certificate": modular_orbit_order_checks(),
    }


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))
