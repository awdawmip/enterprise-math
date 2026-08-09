"""Cross-shell root-target packing for the P017 lower least-factor band.

The high band p^2 >= 2k is controlled by the existing finite resource bounds.
This module studies the complementary least-prime band p^2 < 2k using the
canonical P018 quotient-basin transport.

For each lower-band prime p, let

    j_p = R_2(floor(k^2 / p)).

P018-T110 says the cofactor root can lie only in {j_p, j_p+1}. L051 gives a
uniform multiplicity-two packing bound. L052 sharpens the stable range k>=15:
distinct lower-band prime shells have disjoint candidate-root pairs.
"""

from __future__ import annotations

from math import isqrt

from .core import integer_nth_root
from .legendre import is_prime, primes_up_to


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def lower_band_primes(k: int) -> list[int]:
    """Return least-prime candidates p with p^2 < 2k.

    The exact cutoff is floor(sqrt(2k-1)), so there is no reason to construct a
    prime table up to k. Keeping the implementation aligned with the theorem's
    integer-root horizon also keeps large-root regression tests inexpensive.
    """
    _require_positive("k", k)
    cutoff = isqrt(2 * k - 1)
    return primes_up_to(cutoff)


def lower_band_base_root(k: int, prime: int) -> int:
    """Return j_p = R_2(floor(k^2/p)) for a lower-band prime p."""
    _require_positive("k", k)
    _require_positive("prime", prime)
    if not is_prime(prime) or prime * prime >= 2 * k:
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

    If p<q<r are three distinct lower-band primes and u=j_r, then u>=r. Except
    for the special prime triple (2,3,5), prime spacing gives r-p>=4; in both the
    general and special cases one obtains

        p*(u+2)^2 < r*u^2 <= k^2.

    Therefore j_p>=u+2=j_r+2. Three candidate pairs {j_p,j_p+1},
    {j_q,j_q+1}, {j_r,j_r+1} cannot have a common integer. Consequently every
    target root index has channel multiplicity at most two.
    """
    _require_positive("k", k)
    primes = lower_band_primes(k)
    base_roots = {prime: lower_band_base_root(k, prime) for prime in primes}

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


def lower_band_root_disjoint_bound(k: int) -> dict[str, object]:
    """Return the L052 stable-range disjoint-root packing data.

    For k>=15 and any distinct lower-band primes p<q,

        j_p >= j_q + 2.

    Hence their candidate pairs {j_p,j_p+1} and {j_q,j_q+1} are disjoint, so
    every target root index receives at most one lower-band prime-shell channel.
    The threshold k>=15 is sharp for the uniform statement: at k=14 the shells
    p=2 and p=3 both contain target root 9 in their candidate pairs.
    """
    _require_positive("k", k)
    if k < 15:
        raise ValueError("L052 stable-range disjointness requires k >= 15")

    primes = lower_band_primes(k)
    base_roots = {prime: lower_band_base_root(k, prime) for prime in primes}
    for left_index, p in enumerate(primes):
        for q in primes[left_index + 1 :]:
            if base_roots[p] < base_roots[q] + 2:
                raise AssertionError("L052 pairwise lower-band root separation failed")

    channels: dict[int, list[int]] = {}
    for prime in primes:
        base = base_roots[prime]
        channels.setdefault(base, []).append(prime)
        channels.setdefault(base + 1, []).append(prime)
    frozen = {target: tuple(shells) for target, shells in channels.items()}
    max_multiplicity = max((len(v) for v in frozen.values()), default=0)
    if max_multiplicity > 1:
        raise AssertionError("L052 lower-band target pairs are not disjoint")

    return {
        "k": k,
        "lower_band_primes": primes,
        "base_roots": base_roots,
        "root_channels": frozen,
        "max_multiplicity": max_multiplicity,
    }
