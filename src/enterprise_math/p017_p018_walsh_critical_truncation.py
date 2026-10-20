"""Critical d<=k truncation of the P017 orientation-Walsh divisor switch.

The full Walsh amplifier attached to one basin prime p is the number of
squarefree divisors of the transverse radical R of its opposite mirror state
n=2M-p:

    W_full(p)=2^omega(R).

For analytic work it is useful to discard large divisor-switch moduli.  This can
be done at the exact square-root scale without losing the prime observable.

If R>1, squarefree divisors pair under

    d <-> R/d.

Since R is squarefree, no pair is fixed.  In each pair at least one divisor is
<=sqrt(R).  Moreover R|n and n<(k+1)^2, so

    sqrt(R) <= sqrt(n) < k+1.

An integral divisor <=sqrt(R) is therefore <=k.  Hence

    #{d|R : d<=k} >= 2^(omega(R)-1).

For R=1 the truncated and full weights are both one.  Thus pointwise

    W_full/2 <= W_crit <= W_full

(with the obvious stronger equality when W_full=1), where W_crit keeps only
squarefree transverse divisors d<=k.

Summing over all basin primes gives

    (1/2) W_full(k) <= W_crit(k) <= W_full(k),

and because d=1 is always retained,

    W_crit(k)>0  iff the open square basin contains a prime.

Therefore the entire divisor-switched prime detector can be compiled to the
critical modulus range

    d<=k ~ sqrt(M),  M=k(k+1),

while preserving positivity exactly and at least half of the full Walsh signal.
This is an exact combinatorial reduction, not a short-interval distribution
theorem.
"""

from __future__ import annotations

from .legendre import is_prime
from .p017_p018_walsh_dual_titchmarsh import walsh_prime_divisor_weight


def critical_walsh_prime_weight(k: int, prime_state: int) -> dict[str, object]:
    """Return the d<=k divisor amplifier and certify the pointwise half bound."""
    row = walsh_prime_divisor_weight(k, prime_state)
    full_divisors = tuple(int(d) for d in row["squarefree_transverse_divisors"])
    truncated = tuple(d for d in full_divisors if d <= k)
    full_weight = int(row["walsh_divisor_weight"])
    truncated_weight = len(truncated)
    if 1 not in truncated:
        raise AssertionError("critical Walsh truncation lost the unit divisor")
    if truncated_weight > full_weight:
        raise AssertionError("critical Walsh truncation exceeded the full amplifier")
    if full_weight > 1 and 2 * truncated_weight < full_weight:
        raise AssertionError("critical Walsh truncation lost more than half the divisor amplifier")
    if full_weight == 1 and truncated_weight != 1:
        raise AssertionError("unit radical did not survive critical truncation exactly")
    return {
        **row,
        "critical_divisor_cutoff": k,
        "critical_squarefree_transverse_divisors": truncated,
        "critical_walsh_divisor_weight": truncated_weight,
        "full_walsh_divisor_weight": full_weight,
        "critical_to_full_ratio": truncated_weight / full_weight,
        "pointwise_half_retention": 2 * truncated_weight >= full_weight,
    }


def critical_walsh_profile(k: int) -> dict[str, object]:
    """Aggregate the exact critical divisor switch over all basin primes."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    primes = tuple(n for n in range(k * k + 1, (k + 1) ** 2) if is_prime(n))
    rows = tuple(critical_walsh_prime_weight(k, prime) for prime in primes)
    full = sum(int(row["full_walsh_divisor_weight"]) for row in rows)
    critical = sum(int(row["critical_walsh_divisor_weight"]) for row in rows)
    if critical > full:
        raise AssertionError("critical total exceeded full Walsh total")
    if full and 2 * critical < full:
        raise AssertionError("critical total lost more than half the full Walsh signal")
    prime_exists = bool(primes)
    if (critical > 0) != prime_exists:
        raise AssertionError("critical Walsh positivity is not equivalent to prime existence")

    by_divisor: dict[int, int] = {}
    triples: list[dict[str, int]] = []
    center = k * (k + 1)
    for row in rows:
        prime = int(row["prime_state"])
        opposite = int(row["opposite_state"])
        for divisor in row["critical_squarefree_transverse_divisors"]:
            d = int(divisor)
            quotient = opposite // d
            if d > k:
                raise AssertionError("critical divisor escaped d<=k")
            if prime + d * quotient != 2 * center:
                raise AssertionError("critical dual-Titchmarsh triple failed p+dq=2M")
            by_divisor[d] = by_divisor.get(d, 0) + 1
            triples.append({"prime": prime, "divisor": d, "quotient": quotient})
    switched = sum(by_divisor.values())
    if switched != critical:
        raise AssertionError("critical divisor-switched count disagrees with truncated prime weights")

    return {
        "k": k,
        "center": center,
        "prime_states": primes,
        "prime_rows": rows,
        "full_walsh_weighted_prime_count": full,
        "critical_walsh_weighted_prime_count": critical,
        "critical_to_full_ratio": (critical / full) if full else 1.0,
        "critical_divisor_counts": tuple(sorted(by_divisor.items())),
        "critical_dual_titchmarsh_triples": tuple(triples),
        "critical_modulus_ceiling": k,
        "half_retention_global": (not full) or 2 * critical >= full,
        "positivity_equivalent_to_prime_existence": (critical > 0) == prime_exists,
    }
