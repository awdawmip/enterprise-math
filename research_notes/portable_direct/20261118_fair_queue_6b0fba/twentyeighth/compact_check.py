"""Run with Python 3. Tests the declared compact comparison in dimension three."""
import json
import math
from collections import Counter
from fractions import Fraction
from itertools import combinations, product

ORIGIN = (0, 0, 0)
CORNERS = list(product(range(2), repeat=3))
EVEN = [v for v in CORNERS if sum(v) % 2 == 0]
CASES = {"point": [ORIGIN], "antipodes": [ORIGIN, (1, 1, 1)],
         "even_code": EVEN, "corners": CORNERS}
PI = math.pi


def cube(n):
    return product(range(-n, n + 1), repeat=3)


def parity_readout(points, mode):
    return Fraction(sum((-1) ** (sum(x * y for x, y in zip(p, mode)) % 2)
                        for p in points), len(points))


def shells(points, cutoff):
    result = Counter()
    for mode in cube(math.isqrt(cutoff)):
        m = sum(k * k for k in mode)
        if m <= cutoff:
            result[m] += parity_readout(points, mode) ** 2
    return result


def kernel(t):
    return (1 + t) * math.exp(-t)


def cube_tail(u, n):
    # Sum (24 j^2 + 2)(1 + u j)e^(-u j) over j >= n+1.
    q = math.exp(-u)
    d = -math.expm1(-u)
    a = n + 1
    powers = [1 / d, q / d ** 2, q * (1 + q) / d ** 3,
              q * (1 + 4 * q + q * q) / d ** 4]
    def moment(k):
        return math.exp(-a * u) * sum(math.comb(k, i) * a ** (k - i) * powers[i]
                                       for i in range(k + 1))
    return 2 * moment(0) + 2 * u * moment(1) + 24 * moment(2) + 24 * u * moment(3)


def direct(points, u, n):
    weights = {v: float(parity_readout(points, v) ** 2) for v in CORNERS}
    mult = Counter()
    for k in cube(n):
        mult[(sum(v * v for v in k), tuple(v % 2 for v in k))] += 1
    return math.fsum(count * weights[p] * kernel(u * math.sqrt(m))
                     for (m, p), count in mult.items())


def image_sum(points, u, n):
    # Aggregate differences modulo 2, with representative in {0,1}^3.
    differences = Counter(tuple((x - y) % 2 for x, y in zip(a, b))
                          for a in points for b in points)
    partial = math.fsum(
        count / len(points) ** 2 * 32 * PI * u ** 3
        / (u ** 2 + PI ** 2 * sum((2 * k + h) ** 2 for k, h in zip(lattice, diff))) ** 3
        for diff, count in differences.items() for lattice in cube(n))
    # 2j-1 >= 2j(1-1/(2(n+1))); sum j^-4, j^-6 bounded by integrals.
    scale = 2 * PI * (1 - 1 / (2 * (n + 1)))
    err = 32 * PI * u ** 3 / scale ** 6 * (8 / n ** 3 + 2 / (5 * n ** 5))
    return partial, err


def main():
    output = {"first_shells": {}, "uniform_subsets_of_binary_cube": {},
              "dual_sum_checks": []}
    for name, points in CASES.items():
        s = shells(points, 6)
        first = next(m for m in range(1, 7) if s[m])
        output["first_shells"][name] = [first, int(s[first])]
    assert list(output["first_shells"].values()) == [[1, 6], [2, 12], [3, 8], [4, 6]]
    # Quarter turns, for the sharp eight-point design outside the binary cube.
    sharp = [(0, 0, 0), (2, 2, 2), (0, 2, 1), (0, 2, 3),
             (1, 0, 2), (3, 0, 2), (2, 1, 0), (2, 3, 0)]
    assert all(any((a - b) % 4 == 2 for a, b in zip(x, y))
               for x, y in combinations(sharp, 2))
    exact = Counter()
    for k in cube(2):
        m = sum(v * v for v in k)
        if 1 <= m <= 4:
            counts = Counter(sum(a * b for a, b in zip(x, k)) % 4 for x in sharp)
            exact[m] += Fraction((counts[0] - counts[2]) ** 2
                                 + (counts[1] - counts[3]) ** 2, 64)
    assert [exact[m] for m in (1, 2, 3, 4)] == [0, 0, 0, Fraction(3, 2)]
    output["sharp_eight_point_weights"] = [str(exact[m]) for m in (1, 2, 3, 4)]
    low_modes = {m: [k for k in cube(1) if sum(v * v for v in k) == m] for m in (1, 2, 3)}
    for cutoff in (1, 2, 3):
        sizes = Counter()
        for size in range(1, 9):
            for subset in combinations(CORNERS, size):
                if all(parity_readout(subset, k) == 0 for m in range(1, cutoff + 1)
                       for k in low_modes[m]):
                    sizes[size] += 1
        output["uniform_subsets_of_binary_cube"][cutoff] = dict(sizes)
    assert [min(v) for v in output["uniform_subsets_of_binary_cube"].values()] == [2, 4, 8]
    # Each pair of partial sums has overlapping intervals with the stated analytic tails.
    for name, points in CASES.items():
        u = 2.75
        direct_value = direct(points, u, 13)
        direct_error = cube_tail(u, 13)
        img, img_error = image_sum(points, u, 18)
        assert max(direct_value, img) <= min(direct_value + direct_error, img + img_error) + 1e-13
        output["dual_sum_checks"].append({"probe": name, "u": u, "fourier_partial": direct_value,
                                        "fourier_tail_max": direct_error, "image_partial": img,
                                        "image_tail_max": img_error})
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
