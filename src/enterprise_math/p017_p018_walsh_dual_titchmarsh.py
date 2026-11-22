"""Exact divisor-switching interface for the P017 orientation-Walsh prime weight.

Let M=k(k+1).  Summing both orientation-Walsh endpoints over surviving mirror
radii gives the nonnegative prime-side observable

    W(k)=sum_r [2^c_-(r) 1_{M+r prime} + 2^c_+(r) 1_{M-r prime}].

Every prime p in the open square basin corresponds to exactly one mirror radius;
its opposite state is n=2M-p.  Because a prime-side radius automatically
survives the anchor sieve, every small odd prime <=k dividing n is transverse.
Therefore

    2^{omega_{<=k}(n)}
      = sum_{d|n, d squarefree, p|d => p<=k and p does not divide M} 1.

Switching the divisor and prime sums gives the exact identity

    W(k)
      = sum_d #{p prime: k^2<p<(k+1)^2, p = 2M (mod d)},

with d ranging over squarefree transverse products that can occur below the
opposite-state ceiling.  Equivalently each contribution is a solution of

    p + d q = 2M,
    |p-M|<k.

Thus the parity-balanced Walsh weight is a localized **dual Titchmarsh / Goldbach
 divisor correlation**.  The logarithmic density loss of primes can be offset by
the divisor family because the formal AP main coefficient is

    sum_d 1/phi(d),

which grows logarithmically as the cutoff grows.  The unresolved analytic input
is not the exact divisor switch; it is a short-window mean-value theorem for
these correlated residue classes at physical length H~k~sqrt(M).

For a cutoff D define the log-weighted truncated observable

    Theta_D(k)
      = sum_{d<=D} sum_{p in square basin, p=2M mod d} log p.

The divisor d=1 is always present and all terms are nonnegative, hence
Theta_D(k)>0 iff the square basin contains a prime.  Its formal length-times-
local-density comparison is

    2(k-1) * sum_{d<=D} 1/phi(d).

This comparison is returned only as a diagnostic target; no error bound or
Bombieri-Vinogradov theorem at the square-root interval scale is asserted.
"""

from __future__ import annotations

from math import gcd, log

from .legendre import is_prime, primes_up_to


def _transverse_primes(k: int) -> tuple[int, ...]:
    M = k * (k + 1)
    return tuple(p for p in primes_up_to(k) if p % 2 == 1 and M % p != 0)


def _small_transverse_support(value: int, k: int) -> tuple[int, ...]:
    return tuple(p for p in _transverse_primes(k) if value % p == 0)


def _squarefree_products(primes: tuple[int, ...], cutoff: int) -> tuple[int, ...]:
    values = [1]
    for prime in primes:
        additions = []
        for value in values:
            if value <= cutoff // prime:
                additions.append(value * prime)
        values.extend(additions)
    return tuple(sorted(set(values)))


def _phi_squarefree(value: int, primes: tuple[int, ...]) -> int:
    result = value
    remaining = value
    for prime in primes:
        if remaining % prime == 0:
            result = result // prime * (prime - 1)
            remaining //= prime
    if remaining != 1:
        raise AssertionError("squarefree phi factorization missed a prime")
    return result


def walsh_prime_divisor_weight(k: int, prime_state: int) -> dict[str, object]:
    """Return the squarefree-small-divisor amplifier attached to one basin prime."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if not (k * k < prime_state < (k + 1) ** 2) or not is_prime(prime_state):
        raise ValueError("prime_state must be prime in the open square basin")
    M = k * (k + 1)
    opposite = 2 * M - prime_state
    radius = abs(prime_state - M)
    if not (1 <= radius < k):
        raise AssertionError("basin prime did not belong to a mirror radius")
    if gcd(radius, M) != 1:
        raise AssertionError("prime-side mirror radius did not survive the anchor sieve")
    support = _small_transverse_support(opposite, k)
    divisors = _squarefree_products(support, opposite)
    expected = 2 ** len(support)
    if len(divisors) != expected:
        raise AssertionError("squarefree divisor amplifier has wrong cardinality")
    if any(opposite % divisor for divisor in divisors):
        raise AssertionError("generated divisor does not divide the opposite state")
    return {
        "k": k,
        "center": M,
        "prime_state": prime_state,
        "opposite_state": opposite,
        "radius": radius,
        "opposite_small_transverse_support": support,
        "squarefree_transverse_divisors": divisors,
        "walsh_divisor_weight": expected,
    }


def walsh_dual_titchmarsh_profile(k: int) -> dict[str, object]:
    """Verify W(k) by both prime-weight and divisor-switched enumerations."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    M = k * (k + 1)
    primes = tuple(n for n in range(k * k + 1, (k + 1) ** 2) if is_prime(n))
    prime_rows = tuple(walsh_prime_divisor_weight(k, prime) for prime in primes)
    direct = sum(int(row["walsh_divisor_weight"]) for row in prime_rows)

    by_divisor: dict[int, int] = {}
    triple_rows: list[dict[str, int]] = []
    for row in prime_rows:
        prime = int(row["prime_state"])
        opposite = int(row["opposite_state"])
        for divisor in row["squarefree_transverse_divisors"]:
            d = int(divisor)
            quotient = opposite // d
            if prime + d * quotient != 2 * M:
                raise AssertionError("dual-Titchmarsh triple failed p+dq=2M")
            by_divisor[d] = by_divisor.get(d, 0) + 1
            triple_rows.append({"prime": prime, "divisor": d, "quotient": quotient})

    switched = sum(by_divisor.values())
    if direct != switched:
        raise AssertionError("Walsh prime weight and divisor-switched count disagree")
    for divisor, count in by_divisor.items():
        direct_ap = sum(1 for prime in primes if (prime - 2 * M) % divisor == 0)
        if count != direct_ap:
            raise AssertionError("divisor-switched residue class count is incorrect")

    return {
        "k": k,
        "center": M,
        "prime_states": primes,
        "prime_rows": prime_rows,
        "walsh_weighted_prime_count": direct,
        "divisor_switched_count": switched,
        "divisor_counts": tuple(sorted(by_divisor.items())),
        "dual_titchmarsh_triples": tuple(triple_rows),
        "dual_titchmarsh_identity": True,
    }


def truncated_log_walsh_ap_profile(k: int, cutoff: int) -> dict[str, object]:
    """Return Theta_D and its formal AP-main coefficient for bounded diagnostics."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 1:
        raise ValueError("cutoff must be a positive integer")
    M = k * (k + 1)
    trans = _transverse_primes(k)
    divisors = _squarefree_products(trans, cutoff)
    primes = tuple(n for n in range(k * k + 1, (k + 1) ** 2) if is_prime(n))

    theta = 0.0
    rows: list[dict[str, object]] = []
    phi_reciprocal_sum = 0.0
    for divisor in divisors:
        phi = _phi_squarefree(divisor, trans)
        phi_reciprocal_sum += 1.0 / phi
        hits = tuple(prime for prime in primes if (prime - 2 * M) % divisor == 0)
        contribution = sum(log(prime) for prime in hits)
        theta += contribution
        rows.append(
            {
                "divisor": divisor,
                "phi": phi,
                "prime_hits": hits,
                "log_prime_contribution": contribution,
            }
        )

    formal_main = 2 * (k - 1) * phi_reciprocal_sum
    return {
        "k": k,
        "center": M,
        "cutoff": cutoff,
        "squarefree_transverse_divisors": divisors,
        "theta_D": theta,
        "contains_prime": bool(primes),
        "theta_positive_iff_prime_exists": (theta > 0.0) == bool(primes),
        "phi_reciprocal_sum": phi_reciprocal_sum,
        "formal_interval_length_times_local_density": formal_main,
        "diagnostic_discrepancy_from_formal_main": theta - formal_main,
        "rows": tuple(rows),
        "status": "EXACT_OBSERVABLE_PLUS_FORMAL_MAIN_TARGET_NO_ERROR_THEOREM",
    }
