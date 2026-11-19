"""Clean proper minors, local determinant law, and conditional last rows. Python 3.10+."""
import argparse
from collections import Counter
from fractions import Fraction
from functools import reduce
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import gcd
from pathlib import Path
from runpy import run_path


FROZEN = Path("research_checks/N_COUPLED_SCALAR_CLEAN_NONAUTOMORPHIC_FITTING_SUPPORT_CHANGE_CHECK_20260831.py")
FROZEN_SHA = "ef7c11a753aff2794e0dae55b973ef58ca319348fe7ad76fbbe2fe0b9118b851"


def det(matrix):
    if not matrix:
        return 1
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1) ** j * x * det([row[:j] + row[j + 1:] for row in matrix[1:]])
               for j, x in enumerate(matrix[0]))


def minors(rows, k):
    for chosen in combinations(rows, k):
        for cols in combinations(range(len(rows[0])), k):
            yield det([tuple(row[c] for c in cols) for row in chosen])


def normal(vector, p):
    if p:
        first = next(v % p for v in vector if v % p)
        return tuple(v * pow(first, -1, p) % p for v in vector)
    divisor = reduce(gcd, vector)
    if next(v for v in vector if v) < 0:
        divisor = -divisor
    return tuple(v // divisor for v in vector)


def pair(form, vector):
    return sum(a * b for a, b in zip(form, vector))


def forbidden(rows, p):
    """Distinct central hyperplanes from proper minors involving a new last row."""
    n = len(rows[0])
    forms = set()
    for k in range(1, min(len(rows) + 1, n - 1) + 1):
        for old in combinations(rows, k - 1):
            for cols in combinations(range(n), k):
                row = [0] * n
                for j, col in enumerate(cols):
                    rest = cols[:j] + cols[j + 1:]
                    minor = det([tuple(v[i] for i in rest) for v in old])
                    row[col] = (-1) ** j * minor
                forms.add(normal(row, p))
    return forms


def counts_for_prefix(rows, p):
    assert all(v % p if p else v for k in range(1, len(rows) + 1) for v in minors(rows, k))
    forms = forbidden(rows, p)
    restricted = {normal(tuple(pair(f, row) for row in rows), p) for f in forms}
    output = {"ambient_planes": len(forms), "restricted_planes": len(restricted)}
    if p:
        valid = singular = 0
        for tail in product(range(p), repeat=len(rows[0]) - 1):
            last = (1,) + tail
            if all(pair(f, last) % p for f in forms):
                valid += 1
                singular += det(rows + [last]) % p == 0
        output.update(normalized_valid=valid, normalized_singular=singular)
    return output


def census(n, p):
    """Gauge fixed by all first-row/first-column entries equal to one."""
    first = (1,) * n
    candidates = [(1,) + v for v in permutations(range(2, p), n - 1)]
    prefixes = [0] * (n + 1)
    prefixes[1] = 1
    total = Counter()

    def extend(rows):
        if len(rows) == n:
            total[det(rows) % p == 0] += 1
            return
        forms = forbidden(rows, p)
        for row in candidates:
            if all(pair(f, row) % p for f in forms):
                prefixes[len(rows) + 1] += 1
                extend(rows + [row])

    extend([first])
    return {"normalized_prefixes": prefixes[1:], "normalized_total": sum(total.values()),
            "normalized_singular": total[True], "denormalization_factor": (p - 1) ** (2 * n - 1)}


def gf4_product(a, b):
    result = (a if b & 1 else 0) ^ ((a << 1) if b & 2 else 0)
    return result ^ 7 if result & 4 else result


def finite_field_four():
    def determinant(rows):
        values = (prod_in_field(rows[i][j] for i, j in enumerate(sigma))
                  for sigma in permutations(range(len(rows))))
        return reduce(lambda a, b: a ^ b, values, 0)

    def prod_in_field(values):
        return reduce(gf4_product, values, 1)

    total = singular = 0
    for a, b, c, d in product(range(1, 4), repeat=4):
        m = [(1, 1, 1), (1, a, b), (1, c, d)]
        if all(determinant([tuple(row[j] for j in jj) for row in rr])
               for rr in combinations(m, 2) for jj in combinations(range(3), 2)):
            total += 1
            singular += determinant(m) == 0
    assert (total, singular) == (2, 0)
    return [total, singular]


def four_coefficients():
    original = [(1, 2, 4, -7), (3, 5, 9, -17), (7, 11, 13, -31)]
    exchanged = [(1, -1, 2, -2), (3, 5, -3, -5), (7, 11, -11, -7)]
    report = []
    for j in range(4):
        rows = exchanged[:j] + original[j:]
        assert all(sum(row) == 0 for row in rows)
        for p in (0, 23):
            assert all(v % p if p else v for k in (1, 2, 3) for v in minors(rows, k))
            forms = forbidden(rows, p)
            on_plane = {normal(tuple(pair(f, row) for row in rows), p) for f in forms}
            assert (len(forms), len(on_plane)) == (34, 25 - j)
        report.append({"rows": rows, "field_23_and_Q": [34, 25 - j], "second_coefficient": 9 + j})
    return report


def composite_35():
    units = [z for z in range(35) if gcd(z, 35) == 1]
    distribution = Counter()
    for a, b, c, d in product(units, repeat=4):
        second = (a-1, b-1, b-a, c-1, d-1, d-c, c-a, d-b, a*d-b*c)
        if all(gcd(z, 35) == 1 for z in second):
            delta = (a-1)*(d-1) - (b-1)*(c-1)
            distribution[gcd(delta, 35)] += 1
    assert distribution == {1: 840, 5: 840, 7: 360, 35: 360}
    return dict(sorted(distribution.items()))


def solved_lifts(p, e):
    """Normalized two-by-two census over the complete local ring."""
    mod = p ** e
    # The normalized matrix is [[1,1],[1,d]]. Keep all unit d.
    hist = Counter((d - 1) % mod for d in range(mod) if d % p)
    units = (p - 1) * p ** (e - 1)
    rho = Fraction(1, p - 1)
    for z in range(mod):
        # Gauge fixing changes the determinant by a uniformly random unit.
        cnt = sum(hist[z * u % mod] for u in range(mod) if u % p)
        wanted = (1 - rho) / units if z % p else rho / p ** (e - 1)
        assert Fraction(cnt, units * units) == wanted
    return [p, e, units, mod]


def source_check(repo):
    source = repo / FROZEN
    assert sha256(source.read_bytes()).hexdigest() == FROZEN_SHA
    native = run_path(str(source))
    matrix = [[1, 1, 1], [1, 2, 3], [1, 4, 2]]
    proper = [abs(v) for k in (1, 2) for v in minors(matrix, k)]
    assert all(gcd(v, 35) == 1 for v in proper)
    assert det(matrix) == native["det_bareiss"](matrix) == -5
    signature = native["support_signature"](matrix, 35)
    assert [x["sigma_k"] for x in signature] == [1, 1, 5]
    ranks = [[native["rank_mod_prime"](matrix[:rows], p) for p in (5, 7)] for rows in (2, 3)]
    assert ranks == [[2, 2], [2, 3]]
    return {"sha256": FROZEN_SHA, "matrix": matrix, "signature": signature,
            "ranks_before_then_after": ranks, "absolute_proper_minor_values": sorted(set(proper))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=(Path(".") if FROZEN.is_file()
                                                      else Path("/workspace/enterprise-math")))
    original = source_check(parser.parse_args().repo)
    n3 = {}
    for p in (2, 3, 5, 7, 11, 13, 17):
        report = census(3, p)
        if p <= 3:
            assert report["normalized_total"] == 0
        else:
            prefixes = (p - 2) * (p - 3)
            assert report["normalized_total"] == prefixes * ((p - 4) ** 2 + 1)
            assert report["normalized_singular"] == prefixes * (p - 4)
        n3[p] = report
    n4 = {p: census(4, p) for p in (3, 5, 7)}
    assert n4[7]["normalized_prefixes"] == [1, 60, 120, 120]
    assert all(v["normalized_singular"] == 0 for v in n4.values())
    prefix_examples = []
    for rows, primes, expected in [
        ([(1, 1, 1, 1), (1, 2, 3, 4), (1, 3, 2, 5)], [11], [(34, 23, 4, 13)]),
        ([(1, 1, 1, 1), (1, 2, 3, 4), (1, 3, 6, 10)], [11], [(34, 24, 1, 9)]),
        ([(1, 1, 1, 1), (1, 5, 6, 4), (1, 7, 8, 5)], [0, 19], [(34, 24), (34, 24)]),
        ([(1, 1, 1, 1), (1, 2, 4, 9), (1, 4, 16, 81)], [0, 19], [(34, 25), (34, 25)]),
    ]:
        cases = []
        for p, target in zip(primes, expected):
            result = counts_for_prefix(rows, p)
            observed = [result["ambient_planes"], result["restricted_planes"]]
            if len(target) == 4:
                observed += [result["normalized_singular"], result["normalized_valid"]]
            assert tuple(observed) == target
            cases.append({"field": str(p) if p else "Q", **result})
        prefix_examples.append({"rows": rows, "cases": cases})
    n3_lifts = []
    # A fixed singular residue matrix at p=5; vary the final entry by multiples of 5.
    for e in (2, 3, 4):
        mod = 5 ** e
        residues = [det([(1, 1, 1), (1, 2, 3), (1, 4, 2 + 5 * v)]) % mod
                    for v in range(mod // 5)]
        assert sorted(residues) == list(range(0, mod, 5))
        n3_lifts.append([e, len(residues)])
    print(json.dumps({"frozen_integer_signature": original, "dimension_three": n3,
                      "dimension_four": n4, "gf4_normalized_total_and_singular": finite_field_four(),
                      "two_by_two_uniform_lifts": [solved_lifts(p, e) for p in (2, 3, 5, 7)
                                                   for e in (1, 2, 3)],
                      "three_by_three_simple_lifts_at_5": n3_lifts,
                      "fixed_prefixes": prefix_examples, "classified_dimension_four": four_coefficients(),
                      "composite_35_full_normalized": composite_35()}, indent=2))


if __name__ == "__main__":
    main()
