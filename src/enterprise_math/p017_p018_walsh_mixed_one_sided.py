"""Even mixed Walsh roots collapse to a one-sided Mobius hyperbola.

Work in a centered/symmetric mirror interval, so exchanging the positive and
negative orientation products (a,b) is the physical reflection r -> -r and
therefore preserves the unoriented incidence count F(a,b)=F(b,a).

For an even-support conductor q=ab the Walsh coefficient of the split is
mu(b), and even support is equivalent to mu(a)=mu(b) for squarefree coprime
a,b.  The parity constraint may be eliminated algebraically:

    1_{mu(a)=mu(b)} mu(b) = (mu(a)+mu(b))/2.

Pairing (a,b) with (b,a) and using F(a,b)=F(b,a) gives

    sum_{even mixed} mu(b) F(a,b)
      = sum_{a,b>1, (a,b)=1, ab<=C} mu^2(a) mu(b) F(a,b).

Thus the dangerous mixed family has only one signed divisor variable.  In
radius space this becomes

    M_mix = sum_r sum_{a>1, a|M-r} mu^2(a)
                  sum_{1<b<=C/a, b|M+r} mu(b),

with the understood squarefree/transverse restrictions.  The inner bracket is
a truncated Mobius divisor sum of the target side; a is only the opposite-side
squarefree divisor amplifier.

This identity is the physical counterpart of the root-level Kloosterman/Farey
parametrization.  It isolates the exact parity-sensitive variable before any
analytic estimate.  It does not assert cancellation of the truncated Mobius
sum and does not prove Legendre's conjecture.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, prod


def squarefree_divisors_with_mu_from_primes(primes: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    normalized = tuple(sorted(int(p) for p in primes))
    if len(set(normalized)) != len(normalized):
        raise ValueError("primes must be distinct")
    rows: list[tuple[int, int]] = []
    for size in range(len(normalized) + 1):
        mu = -1 if size % 2 else 1
        for subset in combinations(normalized, size):
            rows.append((prod(subset, start=1), mu))
    return tuple(rows)


def even_mixed_parity_coefficient(mu_a: int, mu_b: int) -> int:
    """Return 1_{mu_a=mu_b} mu_b for squarefree Mobius signs +/-1."""
    if mu_a not in (-1, 1) or mu_b not in (-1, 1):
        raise ValueError("mu_a,mu_b must be squarefree Mobius signs")
    direct = mu_b if mu_a == mu_b else 0
    half_twice = mu_a + mu_b
    if half_twice % 2:
        raise AssertionError("parity projector produced a half-integer")
    transformed = half_twice // 2
    if direct != transformed:
        raise AssertionError("even-parity Mobius projector identity failed")
    return direct


def one_sided_mixed_sum_from_supports(
    lower_primes: tuple[int, ...],
    upper_primes: tuple[int, ...],
    cutoff: int,
) -> dict[str, object]:
    """Verify ordered even-mixed split sum equals one-sided mu^2(a)mu(b) hyperbola.

    This is a local support-lattice identity.  It does not count interval lifts;
    any symmetric physical incidence weight depending only on the unordered
    split may be inserted termwise.
    """
    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    lower = tuple(sorted(int(p) for p in lower_primes))
    upper = tuple(sorted(int(p) for p in upper_primes))
    if set(lower).intersection(upper):
        raise ValueError("orientation supports must be disjoint")
    lower_rows = squarefree_divisors_with_mu_from_primes(lower)
    upper_rows = squarefree_divisors_with_mu_from_primes(upper)

    direct = 0
    one_sided = 0
    rows: list[dict[str, int | bool]] = []
    for a, mu_a in lower_rows:
        for b, mu_b in upper_rows:
            if a == 1 or b == 1 or a * b > cutoff:
                continue
            if gcd(a, b) != 1:
                raise AssertionError("disjoint supports produced noncoprime divisors")
            direct_coefficient = even_mixed_parity_coefficient(mu_a, mu_b)
            one_sided_coefficient = mu_b  # mu^2(a)=1 for every squarefree a
            # A single ordered support orientation is not equal termwise to the
            # one-sided form.  Equality appears after adding its reflected split.
            reflected_direct = even_mixed_parity_coefficient(mu_b, mu_a)
            reflected_one_sided = mu_a
            if direct_coefficient + reflected_direct != one_sided_coefficient + reflected_one_sided:
                raise AssertionError("reflection failed to remove the parity constraint")
            direct += direct_coefficient + reflected_direct
            one_sided += one_sided_coefficient + reflected_one_sided
            rows.append(
                {
                    "a": a,
                    "b": b,
                    "mu_a": mu_a,
                    "mu_b": mu_b,
                    "direct_reflected_pair_coefficient": direct_coefficient + reflected_direct,
                    "one_sided_reflected_pair_coefficient": one_sided_coefficient + reflected_one_sided,
                    "product_within_cutoff": True,
                }
            )

    if direct != one_sided:
        raise AssertionError("one-sided mixed Mobius hyperbola identity failed")
    return {
        "lower_primes": lower,
        "upper_primes": upper,
        "cutoff": cutoff,
        "direct_even_mixed_reflection_sum": direct,
        "one_sided_mobius_reflection_sum": one_sided,
        "one_sided_mixed_identity": True,
        "rows": tuple(rows),
    }
