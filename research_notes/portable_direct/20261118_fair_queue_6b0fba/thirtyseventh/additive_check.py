"""Exact certificates for homogeneous Fermat addition defects. Python 3.8+, stdlib."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb
import json


def valuation(number, p):
    if number == 0:
        raise ValueError("valuation(0) is infinite")
    n = 0
    while number % p == 0:
        number //= p
        n += 1
    return n


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def order(a, p):
    return next(d for d in divisors(p - 1) if pow(a, d, p) == 1)


def defect(x, y, p, n):
    """Evaluate the original numerator before integer division by p."""
    modulus = p ** (n + 1)
    numerator = (pow(x + y, p, modulus) - pow(x, p, modulus) - pow(y, p, modulus)) % modulus
    assert numerator % p == 0
    return numerator // p


@lru_cache(None)
def critical_data(p, a, n):
    modulus = p ** (n + 1)
    w0 = a * pow(1 + a, -1, p) % p
    w = pow(w0, p**n, modulus)
    assert pow(w, p - 1, modulus) == 1
    value = (pow(1 - w, 1 - p, modulus) - 1) % modulus
    assert value % p == 0
    tau = w * pow(1 - w, -1, modulus) % modulus
    assert defect(1, tau, p, n) == value // p
    b = pow(2 * a * (a + 1), -1, p)
    return value // p, b


def branch_count(p, a, n, target=0):
    value, b = critical_data(p, a, n)
    transported = (target - value) % (p**n)
    if transported == 0:
        return p ** (n // 2)
    j = valuation(transported, p)
    if j < 2 or j % 2:
        return 0
    residue = transported // (p**j) * pow(b, -1, p) % p
    return 2 * p ** (j // 2) if pow(residue, (p - 1) // 2, p) == 1 else 0


def projected_branches(p, n):
    return sum(branch_count(p, a, n) for a in range(1, p - 1))


def histograms():
    total = 0
    for p, depth in [(3, 4), (5, 4), (7, 4), (13, 3), (59, 2)]:
        for n in range(1, depth + 1):
            if p == 59 and n == 2:
                # Full branch zero counts only. The other primes also cover all nonzero targets.
                counts = Counter(t % p for t in range(p**n) if defect(1, t, p, n) == 0)
                assert counts[0] == counts[p - 1] == 1
                assert all(counts[a] == branch_count(p, a, n) for a in range(1, p - 1))
                continue
            actual = Counter((t % p, defect(1, t, p, n)) for t in range(p**n))
            for a in range(1, p - 1):
                for target in range(p**n):
                    assert actual[a, target] == branch_count(p, a, n, target)
                    total += 1
    return total


def global_counts():
    cases = {}
    for p, max_n in [(3, 5), (5, 4), (7, 3), (11, 2)]:
        counts = [1]
        for n in range(1, max_n + 1):
            modulus = p**n
            primitive = (modulus - modulus // p) * (3 + projected_branches(p, n))
            inner = p ** (2 * (n - 1)) if n <= p else p ** (2 * (p - 1)) * counts[n - p]
            predicted = primitive + inner
            numerators = [pow(t, p, modulus * p) for t in range(2 * modulus)]
            actual = sum((numerators[x + y] - numerators[x] - numerators[y]) % (modulus * p) == 0
                         for x in range(modulus) for y in range(modulus))
            assert actual == predicted
            counts.append(actual)
        cases[str(p)] = counts[1:]
    for n in range(1, 8):
        modulus = 2**n
        zeros = sum(x * y % modulus == 0 for x in range(modulus) for y in range(modulus))
        assert Fraction(zeros, modulus**2) == Fraction(2 + n, 2 ** (n + 1))
    return cases


def slope_examples(p):
    profile = defaultdict(list)
    for a in range(1, p - 1):
        v, _ = critical_data(p, a, 2)
        if (a * a + a + 1) % p == 0 and p % 3 == 1:
            assert v == 0
            profile["permanent"].append(a)
        elif v % p == 0:
            assert v != 0
            profile["finite_depth_one"].append(a)
    return {
        "exceptional_nontrivial_slopes": dict(profile),
        "unit_counts_at_n_1_2_3_4": [
            1 + len(profile["permanent"]) + len(profile["finite_depth_one"]),
            *[1 + len(profile["permanent"]) * p ** (n // 2) for n in (2, 3, 4)],
        ],
    }


def monic_division(poly, monic):
    top = poly[:]
    degree = len(monic) - 1
    quotient = [0] * max(0, len(poly) - degree)
    while len(top) > degree:
        q = top[-1]
        shift = len(top) - len(monic)
        quotient[shift] = q
        for i in range(degree):
            top[shift + i] -= q * monic[i]
        top.pop()
    return quotient, top


@lru_cache(None)
def cyclotomic(d):
    poly = [-1] + [0] * (d - 1) + [1]
    for e in divisors(d)[:-1]:
        poly, remainder = monic_division(poly, cyclotomic(e))
        assert not any(remainder)
    return poly


def integer_det(matrix):
    """Bareiss elimination; every division is exact."""
    n = len(matrix)
    old = 1
    sign = 1
    for k in range(n - 1):
        if not matrix[k][k]:
            later = next((i for i in range(k + 1, n) if matrix[i][k]), None)
            if later is None:
                return 0
            matrix[k], matrix[later] = matrix[later], matrix[k]
            sign = -sign
        pivot = matrix[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = matrix[i][j] * pivot - matrix[i][k] * matrix[k][j]
                assert value % old == 0
                matrix[i][j] = value // old
        old = pivot
    return sign * matrix[-1][-1]


def resultant(p, d):
    phi = cyclotomic(d)
    degree = len(phi) - 1
    f = [0] + [(-1)**j * comb(p - 1, j) for j in range(1, p)]
    column = monic_division(f, phi)[1]
    cols = []
    for _ in range(degree):
        cols.append(column)
        column = monic_division([0] + column, phi)[1]
    return integer_det([list(row) for row in zip(*cols)])


def resultant_checks():
    cases = {}
    for p in (3, 5, 7, 11, 13, 17, 19, 31, 59):
        values = {}
        for d in divisors(p - 1)[1:]:
            W = resultant(p, d)
            if d == 6:
                assert W == 0
                values[str(d)] = "permanent"
                continue
            degree = len(cyclotomic(d)) - 1
            valuations = []
            for a in range(1, p - 1):
                if order(a * pow(1 + a, -1, p) % p, p) == d:
                    value, _ = critical_data(p, a, 4)
                    assert value
                    valuations.append(valuation(value, p))
            assert len(valuations) == degree and valuation(W, p) == degree + sum(valuations)
            values[str(d)] = {"degree": degree, "v_p_resultant": valuation(W, p)}
        cases[str(p)] = values
    return cases


def shifted_witnesses():
    original = Counter(defect(1, t, 7, 4) for t in range(2, 7**4, 7))
    targets = [0, 147, 441, 343]
    counts = [original[w] for w in targets]
    assert counts == [49, 14, 0, 0] == [branch_count(7, 2, 4, w) for w in targets]
    return {"p": 7, "a": 2, "n": 4, "targets": targets, "counts": counts}


if __name__ == "__main__":
    print(json.dumps({
        "all_targets_branch_comparisons": histograms(),
        "same_disc_four_targets": shifted_witnesses(),
        "integer_pair_zero_counts": global_counts(),
        "critical_value_examples": {str(p): slope_examples(p) for p in (3, 7, 13, 59, 1093)},
        "independent_cyclotomic_resultants": resultant_checks(),
    }, indent=2))
