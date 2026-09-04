"""Task-local checker for the post-#1161 first-balance-return AGM RG.

The construction uses only finite two-letter words, exact integer counts, and
Fraction arithmetic.  It does not evaluate pi and does not use floating-point
square roots.

For an unlabeled two-element diamond branch fiber D, a word has a balanced
prefix when the two elements of D have equal multiplicity in that prefix.
A first-balance-return word of length 2n is balanced at 2n and has no earlier
nonempty balanced prefix.

The exact count is 2*Catalan(n-1), hence the normalized first-return mass is

    f_n = Catalan(n-1) / 2**(2*n-1).

For shape activity s define F_N(s)=sum_{n=1}^N f_n s**(2n).  The completed
formal series F satisfies F*(2-F)=s**2.  Consequently R=1-F is the positive
Pythagorean complement and the AGM geometric channel is

    b_plus = H*(1-F)/2.

The finite approximants b_N=H*(1-F_N)/2 decrease to b_plus.  On the standard
AGM orbit s<1/4 and H<2, the elementary first-return tail bound gives

    0 < b_N-b_plus < 2**(-4*N-4).
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb


def catalan(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return comb(2 * n, n) // (n + 1)


def first_balance_count_by_enumeration(n: int) -> int:
    """Enumerate first returns of a two-letter multiplicity imbalance."""
    if n < 1:
        raise ValueError("n must be positive")
    total = 0
    length = 2 * n
    for word in product((0, 1), repeat=length):
        left = 0
        right = 0
        first_return = True
        for index, letter in enumerate(word, start=1):
            if letter == 0:
                left += 1
            else:
                right += 1
            if index < length and left == right:
                first_return = False
                break
        if first_return and left == right:
            total += 1
    return total


def first_return_mass(n: int) -> Fraction:
    """Normalized first-balance-return mass f_n."""
    if n < 1:
        raise ValueError("n must be positive")
    return Fraction(catalan(n - 1), 2 ** (2 * n - 1))


def first_return_polynomial(s: Fraction, depth: int) -> Fraction:
    if s < 0 or s >= 1:
        raise ValueError("checker uses 0 <= s < 1")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return sum(
        (first_return_mass(n) * s ** (2 * n) for n in range(1, depth + 1)),
        Fraction(0),
    )


def finite_shape_update(s: Fraction, depth: int) -> Fraction:
    """Explicit finite first-return RG t_N=F_N/(2-F_N)."""
    f = first_return_polynomial(s, depth)
    return f / (2 - f)


def run() -> dict[str, object]:
    # Exact raw enumeration of the first eight first-return shells.
    enumerated = [first_balance_count_by_enumeration(n) for n in range(1, 9)]
    expected_counts = [2 * catalan(n - 1) for n in range(1, 9)]
    if enumerated != expected_counts:
        raise AssertionError((enumerated, expected_counts))

    # Coefficientwise renewal identity F(2-F)=s^2:
    # 2 f_1 = 1 and 2 f_n = sum_{i=1}^{n-1} f_i f_{n-i} for n>=2.
    if 2 * first_return_mass(1) != 1:
        raise AssertionError("first coefficient renewal identity failed")
    for n in range(2, 65):
        convolution = sum(
            (first_return_mass(i) * first_return_mass(n - i) for i in range(1, n)),
            Fraction(0),
        )
        if 2 * first_return_mass(n) != convolution:
            raise AssertionError(f"renewal recurrence failed at n={n}")

    # Rational finite-domain regression on the standard shape range s<=1/4.
    # R_N=1-F_N lies above sqrt(1-s^2), while R_N-s^(2N+2) lies below it.
    # These are checked without square roots by squaring exact rationals.
    rational_cases = 0
    inequalities_checked = 0
    for q in range(4, 41):
        for p in range(1, q // 4 + 1):
            s = Fraction(p, q)
            previous_t = Fraction(-1)
            for depth in range(1, 9):
                f_n = first_return_polynomial(s, depth)
                r_n = 1 - f_n
                target_square = 1 - s * s
                error = s ** (2 * depth + 2)
                if not r_n * r_n > target_square:
                    raise AssertionError("finite complement did not stay above exact complement")
                if not (r_n - error) * (r_n - error) <= target_square:
                    raise AssertionError("elementary first-return tail certificate failed")

                t_n = finite_shape_update(s, depth)
                if not t_n > previous_t:
                    raise AssertionError("finite shape update is not monotone in return depth")
                if not (0 <= t_n < 1):
                    raise AssertionError("finite shape update left admissible range")
                previous_t = t_n
                inequalities_checked += 3
            rational_cases += 1

    return {
        "enumerated_first_return_counts_n1_to_n8": enumerated,
        "renewal_coefficients_checked": 64,
        "rational_shape_cases": rational_cases,
        "finite_depths_per_case": 8,
        "exact_inequalities_checked": inequalities_checked,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "enumerated_first_return_counts_n1_to_n8": [2, 2, 4, 10, 28, 84, 264, 858],
        "renewal_coefficients_checked": 64,
        "rational_shape_cases": 190,
        "finite_depths_per_case": 8,
        "exact_inequalities_checked": 4560,
    }
    if result != expected:
        raise SystemExit(f"unexpected checker output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
