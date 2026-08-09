"""Cross-shell root-target packing for the P017 lower least-factor band.

The high band p^2 >= 2k is controlled by the existing finite resource bounds.
This module studies the complementary least-prime band p^2 < 2k using the
canonical P018 quotient-basin transport.

For each lower-band prime p, let

    j_p = R_2(floor(k^2 / p)).

P018-T110 says the cofactor root can lie only in {j_p, j_p+1}.  The result here
is cross-shell: every target root index belongs to at most two such candidate
pairs.  No prime-distribution estimate is used.
"""

from __future__ import annotations

from .core import integer_nth_root
from .legendre import is_prime, primes_up_to


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def lower_band_primes(k: int) -> list[int]:
    """Return least-prime candidates p<=k with p^2 < 2k."""
    _require_positive("k", k)
    return [p for p in primes_up_to(k) if p * p < 2 * k]


def lower_band_base_root(k: int, prime: int) -> int:
    """Return j_p = R_2(floor(k^2/p)) for a lower-band prime p."""
    _require_positive("k", k)
    _require_positive("prime", prime)
    if prime > k or not is_prime(prime) or prime * prime >= 2 * k:
        raise ValueError("prime must be a lower-band prime with p^2 < 2k")
    return integer_nth_root((k * k) // prime, 2)


def lower_band_candidate_roots(k: int, prime: int) -> tuple[int, int]:
    """Return the two T110 candidate cofactor-root indices for one shell."""
    base = lower_band_base_root(k, prime)
    return base, base + 1


def lower_band_root_channels(k: int) -> dict[int, tuple[int, ...]]:
    """Reindex lower-band shells by their two possible T110 target roots.

    L051 proves that every target root has at most two prime-shell channels.
    The assertion below is executable validation of that theorem, not its proof.
    """
    _require_positive("k", k)
    channels: dict[int, list[int]] = {}
    for prime in lower_band_primes(k):
        base = lower_band_base_root(k, prime)
        channels.setdefault(base, []).append(prime)
        channels.setdefault(base + 1, []).append(prime)

    frozen = {target: tuple(primes) for target, primes in channels.items()}
    if any(len(primes) > 2 for primes in frozen.values()):
        raise AssertionError("lower-band root target received more than two shells")
    return frozen


def lower_band_root_overlap_bound(k: int) -> dict[str, object]:
    """Return the L051 cross-shell root packing data.

    If p<q<r are three distinct lower-band primes and u=j_r, then u>=r.  Except
    for the special prime triple (2,3,5), prime spacing gives r-p>=4; in both the
    general and special cases one obtains

        p*(u+2)^2 < r*u^2 <= k^2.

    Therefore j_p>=u+2=j_r+2.  Three candidate pairs {j_p,j_p+1},
    {j_q,j_q+1}, {j_r,j_r+1} cannot have a common integer.  Consequently every
    target root index has channel multiplicity at most two.
    """
    _require_positive("k", k)
    primes = lower_band_primes(k)
    base_roots = {prime: lower_band_base_root(k, prime) for prime in primes}

    # Stronger three-shell endpoint separation used in the paper proof.
    for left_index in range(len(primes) - 2):
        p = primes[left_index]
        for right_index in range(left_index + 2, len(primes)):
            r = primes[right_index]
            if base_roots[p] < base_roots[r] + 2:
                raise AssertionError("three-shell endpoint separation failed")

    channels: dict[int, list[int]] = {}
    for prime in primes:
        base = base_roots[prime]
        channels.setdefault(base, []).append(prime)
        channels.setdefault(base + 1, []).append(prime)
    frozen = {target: tuple(shells) for target, shells in channels.items()}
    max_multiplicity = max((len(v) for v in frozen.values()), default=0)
    if max_multiplicity > 2:
        raise AssertionError("L051 root-target overlap bound failed")

    return {
        "k": k,
        "lower_band_primes": primes,
        "base_roots": base_roots,
        "root_channels": frozen,
        "max_multiplicity": max_multiplicity,
    }
