"""Arithmetic certificates for central intervals in F_p. Python 3.8+ standard library."""
import json
from fractions import Fraction
from itertools import combinations
from math import isqrt, prod


def primes_through(bound):
    sieve = bytearray([1]) * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(bound) + 1):
        if sieve[p]:
            count = (bound - p * p) // p + 1
            sieve[p * p : bound + 1 : p] = bytes(count)
    return [p for p, prime in enumerate(sieve) if prime]


def squarefree_primes(value):
    result = []
    p = 2
    while p * p <= value:
        multiplicity = 0
        while value % p == 0:
            value //= p
            multiplicity += 1
        if multiplicity % 2:
            result.append(p)
        p = 3 if p == 2 else p + 2
    if value > 1:
        result.append(value)
    return result


def quadratic_rows(h):
    prime_columns = {}
    pivots = {}
    witness = None
    for j, x in enumerate(range(1, h, 2)):
        mask = 0
        for prime in squarefree_primes(x * x + 8 * h):
            if prime not in prime_columns:
                prime_columns[prime] = len(prime_columns)
            mask |= 1 << prime_columns[prime]
        combination = 1 << j
        while mask:
            pivot = mask.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = mask, combination
                break
            other, indices = pivots[pivot]
            mask ^= other
            combination ^= indices
        if mask == 0 and bin(combination).count("1") % 2:
            support = [2 * i + 1 for i in range(j + 1) if combination & (1 << i)]
            if witness is None or len(support) < len(witness):
                witness = support
    # Every dependency arising from elimination has a distinct last touched input.
    # They therefore span the relation space. Checking their parity suffices.
    rank = len(pivots)
    data = {"h": h, "rows": h // 2, "rank": rank}
    if witness is None:
        data["density_fraction"] = str(Fraction(1, 2**rank))
    else:
        factors = [x * x + 8 * h for x in witness]
        value = prod(factors)
        root = isqrt(value)
        assert len(witness) % 2 and root * root == value
        data.update(density_fraction="0", odd_witness_x=witness, factors=factors, product_sqrt=root)
    return data


def centered(t, q):
    return (t + q // 2) % q - q // 2


def original_image(s, q):
    return {centered(-s * a - pow(2 * a, -1, q), q) for a in range(1, q)}


def passes_character_test(h, q):
    return all(pow(x * x + 8 * h, (q - 1) // 2, q) == q - 1 for x in range(1, h, 2))


FINITE_ZERO_WITNESSES = {
    6: (1, 37, 59),
    7: (9, 43, 51, 69, 109),
    8: (17, 99, 245),
    9: (67, 83, 135),
    10: (61, 193, 261),
    11: (83, 121, 171),
    12: (483, 527, 1019),
    13: (183, 283, 701),
    14: (361, 985, 1593),
    15: (409, 10059, 24155),
    16: (139, 205, 557),
    17: (3571, 12343, 56139),
    18: (2879, 4287, 9379),
    19: (4123, 7439, 493197),
    20: (385, 4537, 64861),
    21: (8411, 625035, 1622761),
    22: (419, 28661, 817123),
    23: (769, 30669, 635531),
    24: (13147, 15215, 221769),
    25: (295, 35013, 22333811),
    26: (47255, 54025, 58043),
    27: (5377, 144401, 8159001),
    28: (16431, 20243, 138457),
    29: (69415, 179127, 23709289),
    30: (61229, 74399, 478637),
    31: (920077, 1558467, 3701279),
    32: (601765, 1312675, 7113831),
    33: (382825, 18452083, 290589141),
    34: (82561, 317315, 30525273),
    35: (1591691, 3258409, 7101459),
    36: (291023, 3351797, 8273899),
    37: (561157, 1337847051, 31036329943),
    38: (1887835, 2007393, 3306421),
    39: (3707827, 6700861, 282924225),
    40: (2984701, 4098803, 5476247),
    41: (4976989, 15123303, 36575203),
    42: (185855, 19445209, 52800087),
    43: (7903387, 8402524931, 61095593295),
    44: (6609965, 17696197, 780062501),
    45: (16060171, 16276775, 41792763),
    46: (49371491, 183691939, 1140279323),
    47: (890091551, 78040116107, 171212960349),
    48: (14910337, 15465937, 307897329),
    49: (105621865, 136146669, 310053317052427),
    50: (57342643, 89224405, 391830005),
    51: (20206933, 13090056629, 109431422508207),
    52: (269773147, 371449671, 576991955),
    53: (708100579, 69706373720125, 3767331415283817),
    54: (274815649, 633169559, 5801115637),
    55: (118359809, 6690858459, 13691990197277),
    56: (384258277, 2728939225, 85530935871),
    57: (9657608375, 13764133789, 1135752312957),
    58: (695585069, 3789070535, 42589542273),
    59: (252211443, 10753439761, 83057245411),
    60: (3682046065, 11371017059, 25701961123),
    61: (3800804135, 5742779086179, 330041492553059),
    62: (207086793, 822028789, 2479277185),
    63: (21188718493, 54657215169269, 1205140329569254305),
    64: (20482385783, 42377766341, 45784469237),
    65: (3677503579, 954706739413, 1215778699759737),
    66: (38401410139, 45006581569, 636494842287),
    67: (1017351499, 132562420499, 1226270339985),
    68: (10618040315, 73001745815, 5860196764689),
    69: (19670782973, 952900998423, 4051800450923),
    70: (105700044071, 382747076569, 1590078607123),
    71: (314215652603, 927858233855371, 3783157540107135),
    72: (70467696173, 410392048089, 529460938513),
}


def verify_finite_obstructions():
    assert set(FINITE_ZERO_WITNESSES) == set(range(6, 73))
    rows = []
    for k, indices in FINITE_ZERO_WITNESSES.items():
        assert len(indices) == (5 if k == 7 else 3) and len(set(indices)) == len(indices)
        assert all(0 < x < 2**k and x % 2 == 1 for x in indices)
        value = prod(x * x + 2 ** (k + 3) for x in indices)
        root = isqrt(value)
        assert root * root == value
        rows.append({"k": k, "x": indices, "square_root_of_product": root})
    return rows


NORM_DATA = (
    # squarefree D, numerator coefficients of pi, integer coefficients of epsilon
    (41, 7, 1, 32, 5),
    (97, 69, 7, 5604, 569),
    (3977, 63, 1, 30392000596, 481927261),
)


def balanced_witness(exponent, parameters):
    """Construct x,y in x^2+2^(k+3)=D y^2, using the basis (1, (1+sqrt(D))/2)."""
    field, a, b, u, v = parameters
    theta_constant = (field - 1) // 4

    def multiply(left, right):
        m, n = left
        p, q = right
        return m * p + theta_constant * n * q, m * q + n * p + n * q

    def power(base, n):
        ans = (1, 0)
        while n:
            if n % 2:
                ans = multiply(ans, base)
            n //= 2
            base = multiply(base, base)
        return ans

    def trace(element):
        return 2 * element[0] + element[1]

    assert field % 8 == 1 and prod(squarefree_primes(field)) == field
    assert abs(a * a - field * b * b) == 8 and a % 2 == b % 2 == 1
    assert u * u - field * v * v == -1 and 2 * u + 1 < 2**36
    n = exponent + 1
    seed = ((a - b) // 2, b)
    unit = (u - v, 2 * v)
    element = power(seed, n)
    positive_norm = a * a - field * b * b > 0 or n % 2 == 0
    if positive_norm:
        element = multiply(element, unit)

    # Trace increases with the positive real embedding when the norm is negative.
    unit_squared = multiply(unit, unit)
    m, t = unit_squared
    inverse_squared = (m + t, -t)
    if trace(element) > 0:
        lo, hi = multiply(element, inverse_squared), element
        while trace(lo) > 0:
            lo, hi = multiply(lo, inverse_squared), lo
    else:
        lo, hi = element, multiply(element, unit_squared)
        while trace(hi) < 0:
            lo, hi = hi, multiply(hi, unit_squared)
    nearest = min((lo, hi), key=lambda entry: abs(trace(entry)))
    x, y = abs(trace(nearest)), abs(nearest[1])
    assert x % 2 == y % 2 == 1 and x * x + (1 << (exponent + 3)) == field * y * y
    return x, y


def infinite_tail_checks():
    exponents = [73, 74, 75, 100, 127, 128, 256, 1024]
    for k in exponents:
        pairs = [balanced_witness(k, entry) for entry in NORM_DATA]
        assert len(set(x for x, _ in pairs)) == 3
        assert all(0 < x < 2**k for x, _ in pairs)
        root = 3977 * prod(y for _, y in pairs)
        assert prod(x * x + 2 ** (k + 3) for x, _ in pairs) == root * root
    return {
        "proved_from_exponent": 73,
        "archimedean_unit_upper_bound": 2**36,
        "norm_input_rows_D_a_b_u_v": NORM_DATA,
        "independent_exact_sample_exponents": exponents,
        "at_first_uniform_exponent_x_y": [balanced_witness(73, row) for row in NORM_DATA],
    }


def checks():
    small_primes = primes_through(257)
    power_rows = [quadratic_rows(2**k) for k in range(1, 13)]
    assert [row["rank"] for row in power_rows[:5]] == [1, 2, 4, 8, 16]
    assert power_rows[5]["odd_witness_x"] == [1, 37, 59]
    assert power_rows[5]["product_sqrt"] == 62073
    triples_checked = 0
    for xs in combinations(range(1, 128, 2), 3):
        value = prod(x * x + 1024 for x in xs)
        assert isqrt(value) ** 2 != value
        triples_checked += 1
    assert triples_checked == 41664
    direct_comparisons = 0
    zero_branch_comparisons = 0
    for q in small_primes:
        for h in range(2, min(q - 4, 129), 2):
            s = q - h
            if q - 2 * h in (-1, 1, 3):
                continue  # previously archived near-extremal families
            image = original_image(s, q)
            outside = [x for x in image if abs(x) > (s - 1) // 2]
            assert (not outside) == passes_character_test(h, q)
            odd_part = h
            while odd_part % 2 == 0:
                odd_part //= 2
            if odd_part > 1:
                v = 2 * h // odd_part
                x = abs(v - odd_part)
                assert 0 < x < h and x % 2 == 1 and x * x + 8 * h == (v + odd_part) ** 2
                assert (q - x) // 2 in outside
            for x in range(1, h, 2):
                if (x * x + 8 * h) % q == 0:
                    assert (q - x) // 2 in outside
                    zero_branch_comparisons += 1
            direct_comparisons += 1

    examples = {2: 11, 4: 13, 8: 43, 16: 2791, 32: 63179}
    for h, q in examples.items():
        assert all(q % p for p in range(2, isqrt(q) + 1))
        assert passes_character_test(h, q)
        assert max(map(abs, original_image(q - h, q))) <= (q - h - 1) // 2

    d5_claims = {}
    for q in (5, 13, 17, 29, 37):
        s = (q + 5) // 2
        image = original_image(s, q)
        values = [centered(-k * pow(3, -1, q), q) for k in (23, 7)]
        assert set(values) <= image
        status = max(map(abs, image)) <= (s - 1) // 2
        assert status == all(abs(t) <= (s - 1) // 2 for t in values)
        d5_claims[str(q)] = {"s": s, "radius": (s - 1) // 2, "a3_and_a_third": values, "saturation": status}
    assert sorted(original_image(9, 13)) == [-3, -2, -1, 1, 2, 3]

    moving_witnesses = 0
    for q in small_primes:
        for d in range(5, q, 2):
            if (q + d) % 4 != 2:
                continue
            radius = (q + d - 2) // 4
            s = (q + d) // 2
            for a, threshold in ((3, 21 * d - 4), (pow(3, -1, q), 5 * d + 12)):
                if a != 3 and d % 3 == 0:
                    continue
                if q > threshold:
                    assert abs(centered(-s * a - pow(2 * a, -1, q), q)) > radius
                    moving_witnesses += 1
    return {
        "fixed_gap_power_rows": power_rows,
        "finite_power_gap_obstructions": verify_finite_obstructions(),
        "h128_triples_exhaustively_excluded": triples_checked,
        "uniform_quadratic_norm_tail": infinite_tail_checks(),
        "direct_field_comparisons": direct_comparisons,
        "ramified_zero_discriminant_checks": zero_branch_comparisons,
        "verified_saturated_examples_by_h": examples,
        "d5_small_prime_control": d5_claims,
        "moving_family_outside_witnesses_checked": moving_witnesses,
    }


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
