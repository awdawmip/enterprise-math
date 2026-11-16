"""Exact checks for positive shortest BRC words and their auxiliary character.

Run beside the project's signed_brc.py, or in its existing checkout.  All
enclosures below use integer and Fraction arithmetic, with no floating point.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha1
from itertools import combinations
from math import comb, isqrt
from pathlib import Path
import sys

KERNEL_PATH = Path("experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py")
KERNEL_BLOB = "300a96e3dc24bf6fff73743037a0347a8bc83176"
here = Path(__file__).resolve().parent
candidates = [here / "signed_brc.py", *(base / KERNEL_PATH for base in (here, *here.parents))]
kernel = next((path for path in candidates if path.is_file()), None)
if kernel is None:
    raise FileNotFoundError(f"Place the source {KERNEL_PATH} beside this checker")
raw = kernel.read_bytes()
assert sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == KERNEL_BLOB
sys.path.insert(0, str(kernel.parent))
from signed_brc import shortest_path_multiplicity


def histogram(m):
    previous = []
    for x in range(m + 1):
        row = []
        for y in range(m + 1):
            bins = Counter({0: 1}) if x == y == 0 else Counter()
            if x:
                bins.update(previous[y])
            if y:
                for old, count in row[y - 1].items():
                    bins[old + x] += count
            row.append(bins)
        previous = row
    return previous[-1]


def check_histograms():
    checked_bins = represented_words = 0
    for m in range(1, 33):
        M = m * m
        hist = histogram(m)
        total = shortest_path_multiplicity((m, m, 0, 0, 0, 0))
        assert sum(hist.values()) == total == comb(2 * m, m)
        assert set(hist) == set(range(M + 1))
        assert all(hist[k] == hist[M - k] for k in hist)
        assert hist[0] == hist[M] == hist[1] == hist[M - 1] == 1
        # Independent exact enumeration using positions of vertical moves.
        if m <= 8:
            explicit = Counter(sum(slot - j for j, slot in enumerate(slots))
                               for slots in combinations(range(2 * m), m))
            assert explicit == hist
        variance = Fraction(sum((2 * k - M)**2 * v for k, v in hist.items()), total)
        fourth = Fraction(sum((2 * k - M)**4 * v for k, v in hist.items()), total)
        assert variance == Fraction(m*m*(2*m+1), 3)
        assert fourth == 3*variance**2 - Fraction(2*m**3*(2*m+1)*(3*m+2), 15)
        assert 0 < fourth <= 3*variance**2
        if m >= 2:
            # Certify feasible optimizers at both mass endpoints and midpoint.
            # Remainder support is at the two end and two nearest-end words.
            for lower_share in (Fraction(0), Fraction(1,3), Fraction(1)):
                floor_internal = lower_share * Fraction(total - 2, total)
                top_internal = 1 - 2*lower_share / total
                for p in (floor_internal, (floor_internal+top_internal)/2, top_internal):
                    probabilities = {k: lower_share*c/total for k, c in hist.items()}
                    extra_internal = p - floor_internal
                    extra_end = 1 - lower_share - extra_internal
                    for k in (1, M-1):
                        probabilities[k] += extra_internal / 2
                    for k in (0, M):
                        probabilities[k] += extra_end / 2
                    assert sum(probabilities.values()) == 1
                    assert sum(probabilities[k] for k in range(1,M)) == p
                    assert all(probabilities[k] >= lower_share*c/total for k,c in hist.items())
                    assert all(probabilities[k] == probabilities[M-k] for k in hist)
        checked_bins += len(hist)
        represented_words += total
    return checked_bins, represented_words


# Positive roots in dyadic orders allow certified enclosures by square roots.
# Each bound is rounded outwards on the denominator GRID.
GRID = 1 << 100


def round_out(lo, hi):
    def lower(x):
        return Fraction((x * GRID).__floor__(), GRID)
    return lower(lo), -lower(-hi)


def sqrt_enclosure(x):
    assert x >= 0
    n = isqrt((x.numerator * GRID**2) // x.denominator)
    low = Fraction(n, GRID)
    high = low if low * low == x else Fraction(n + 1, GRID)
    return low, high


def positive_root_coordinates(order):
    assert order >= 4 and order & (order - 1) == 0
    real = (Fraction(0), Fraction(0))
    n = 4
    while n < order:
        real = (sqrt_enclosure((1 + real[0]) / 2)[0],
                sqrt_enclosure((1 + real[1]) / 2)[1])
        n *= 2
    imag = (sqrt_enclosure(1 - real[1]**2)[0], sqrt_enclosure(1 - real[0]**2)[1])
    return real, imag


def multiply_and_round(x, y):
    endpoints = [a * b for a in x for b in y]
    return round_out(min(endpoints), max(endpoints))


def real_parts(root_real, max_power):
    values = [(Fraction(1), Fraction(1)), root_real]
    for n in range(2, max_power + 1):
        p = multiply_and_round(root_real, values[-1])
        prev = values[-2]
        values.append(round_out(2*p[0] - prev[1], 2*p[1] - prev[0]))
    return values


def check_dyadic_characters():
    sqrt2 = sqrt_enclosure(Fraction(2))
    for m in (1, 2, 4, 8):
        M = m*m
        a, unused_imag = positive_root_coordinates(8*M)
        real = real_parts(a, M)
        h = histogram(m)
        B = sum(h.values())
        def mean(which):
            return sum((real[abs(2*k-M)][which] * count for k, count in h.items()), Fraction()) / B
        delta = (1 - mean(1), 1 - mean(0))
        c = (2*M*M*(1-a[1]), 2*M*M*(1-a[0]))
        assert Fraction(1,2) <= c[0] <= c[1] <= 1
        assert Fraction(2*m+1,24*m*m) <= delta[0] <= delta[1] <= Fraction(2*m+1,6*m*m)
        v = Fraction(m*m*(2*m+1),3)
        fourth = 3*v*v - Fraction(2*m**3*(2*m+1)*(3*m+2),15)
        # Polynomial equality makes the leading inequality exact at m=1.
        if m > 1:
            lead = Fraction(2*m+1,6*m*m)
            assert 0 < c[0]*lead-delta[1]
            assert c[1]*lead-delta[0] <= (fourth-v)/(24*M**4)
            b, d = positive_root_coordinates(4*M)
            gap = ((b[0]+d[0]-1)/sqrt2[1], (b[1]+d[1]-1)/sqrt2[0])
            assert Fraction(1,4*M) < gap[0] <= gap[1] < Fraction(2,M)
        print(f"m={m}: delta in [{(delta[0]*10**9).__floor__()}, "
              f"{(delta[1]*10**9).__ceil__()}] / 10^9")


if __name__ == "__main__":
    print("histogram bins and represented words", *check_histograms())
    check_dyadic_characters()
    print("PASS")
