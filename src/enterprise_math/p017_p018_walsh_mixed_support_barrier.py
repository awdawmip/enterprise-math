"""Four-support threshold for a positive one-sided mixed-Walsh Mobius boundary.

For a squarefree radical R and integer budget B define

    S_R(B)=sum_(d|R,d<=B) mu(d),
    I_R(B)=S_R(B)-1,

so I_R is the non-unit inner sum appearing in the one-sided mixed-Walsh
hyperbola.  If R has at most three distinct prime factors, then

    S_R(B)<=1,       I_R(B)<=0

for every B.

The proof is finite and structural.  The selected divisors d<=B form a downward
closed threshold complex on the prime vertices.

* With at most two vertices the claim is immediate.
* With three vertices, before the full triple enters, write v for the number of
  selected singleton vertices and e for the number of selected pair divisors.
  Every selected edge has both endpoints selected, and a simple graph on at most
  three selected vertices has e<=v.  Hence

      S=1-v+e<=1.

  Once the triple enters all divisors are present and S=0.

The threshold is sharp.  For

    R=3*5*7*11,  B=77,

the unit, all four singleton primes and all six pair products are selected, so

    S_R(B)=1-4+6=3,       I_R(B)=2>0.

Consequently a genuinely positive mixed inner requires at least four distinct
target primes.  If those primes divide one state n in the open k-th square
basin, their least prime p obeys

    p^4 <= n < (k+1)^2,

hence p^2<=k and

    p<=floor(sqrt(k)).

This gives an exact fourth-root continuation trigger for Euclidean boundary
descent: a mixed child with support depth at most three cannot propagate
positive mixed Mobius mass; every positive child must re-enter the square-root
least-prime shell.  The theorem is a sign/localization statement, not a bound on
negative mixed mass and not a Legendre proof.
"""

from __future__ import annotations

from itertools import combinations
from math import isqrt, prod


def squarefree_divisor_mobius_rows(primes: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    normalized = tuple(sorted(int(p) for p in primes))
    if len(set(normalized)) != len(normalized):
        raise ValueError("primes must be distinct")
    rows: list[tuple[int, int]] = []
    for size in range(len(normalized) + 1):
        mu = -1 if size % 2 else 1
        for subset in combinations(normalized, size):
            rows.append((prod(subset, start=1), mu))
    return tuple(sorted(rows))


def truncated_mixed_inner(primes: tuple[int, ...], budget: int) -> int:
    """Return I_R(B)=sum_(d|R,d<=B)mu(d)-1."""
    if isinstance(budget, bool) or not isinstance(budget, int) or budget < 0:
        raise ValueError("budget must be a nonnegative integer")
    return sum(mu for divisor, mu in squarefree_divisor_mobius_rows(primes) if divisor <= budget) - 1


def support_three_nonpositive(primes: tuple[int, ...], budget: int) -> dict[str, object]:
    """Certify I_R(B)<=0 for every declared support of size at most three."""
    normalized = tuple(sorted(int(p) for p in primes))
    if len(normalized) > 3:
        raise ValueError("support_three_nonpositive requires at most three primes")
    inner = truncated_mixed_inner(normalized, budget)
    if inner > 0:
        raise AssertionError("support depth <=3 produced a positive mixed Mobius inner")
    return {
        "support_primes": normalized,
        "support_size": len(normalized),
        "budget": budget,
        "truncated_mixed_inner": inner,
        "positive_mixed_inner_impossible": True,
    }


def four_support_sharpness_witness() -> dict[str, object]:
    primes = (3, 5, 7, 11)
    budget = 77
    inner = truncated_mixed_inner(primes, budget)
    if inner != 2:
        raise AssertionError("four-support sharpness witness changed")
    return {
        "support_primes": primes,
        "radical": prod(primes),
        "budget": budget,
        "truncated_mixed_inner": inner,
        "positive_mixed_inner": True,
        "four_support_threshold_sharp": True,
    }


def positive_mixed_square_root_trigger(k: int, state: int, primes: tuple[int, ...], budget: int) -> dict[str, object]:
    """If one basin state has positive mixed inner, force >=4 support and p_min<=sqrt(k)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(state, bool) or not isinstance(state, int) or not (k * k < state < (k + 1) ** 2):
        raise ValueError("state must lie in the open k-th square basin")
    normalized = tuple(sorted(int(p) for p in primes))
    if not normalized:
        raise ValueError("primes must be nonempty")
    if any(state % p for p in normalized):
        raise ValueError("every support prime must divide the declared state")
    inner = truncated_mixed_inner(normalized, budget)
    if inner <= 0:
        return {
            "k": k,
            "state": state,
            "support_primes": normalized,
            "budget": budget,
            "truncated_mixed_inner": inner,
            "positive_mixed_inner": False,
        }
    if len(normalized) < 4:
        raise AssertionError("positive mixed inner violated the four-support theorem")
    least = normalized[0]
    if least**4 > state:
        raise AssertionError("least support prime fourth power exceeded its state")
    if least > isqrt(k):
        raise AssertionError("positive mixed inner escaped the square-root least-prime shell")
    return {
        "k": k,
        "state": state,
        "support_primes": normalized,
        "support_size": len(normalized),
        "budget": budget,
        "truncated_mixed_inner": inner,
        "positive_mixed_inner": True,
        "least_support_prime": least,
        "least_prime_square_root_ceiling": isqrt(k),
        "positive_mixed_requires_four_support": True,
        "positive_mixed_reenters_square_root_shell": True,
    }
