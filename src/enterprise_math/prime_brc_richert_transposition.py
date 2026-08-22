"""Exact Prime-BRC cofactor-prefix transposition identities.

Owner-local L3 research support.  This module packages only finite identities:
P017 cofactor windows, Abel prefix recoalescence, and aggregate interval-sieve
remainders.  It makes no P2 or prime-existence claim.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Mapping, Sequence

from .legendre import interior_hit_count
from .p017_cofactor_window import centered_cofactor_window, is_p_rough


def _strictly_increasing(values: Sequence[int]) -> bool:
    return all(a < b for a, b in zip(values, values[1:]))


def cofactor_window(k: int, prime: int) -> tuple[int, int]:
    data = centered_cofactor_window(k, prime)
    return int(data["q_min"]), int(data["q_max"])


def cofactor_windows_are_disjoint(k: int, primes: Sequence[int]) -> bool:
    """Replay the L054 disjoint-window property on the supplied prime list."""
    ps = tuple(primes)
    if not _strictly_increasing(ps):
        raise ValueError("primes must be strictly increasing")
    windows = [cofactor_window(k, p) for p in ps]
    return all(windows[i][1] < windows[i - 1][0] for i in range(1, len(windows)))


def cofactor_sift_count(k: int, prime: int, z_primes: Sequence[int]) -> int:
    """Count values in W_p(k) surviving the supplied primes < z."""
    lo, hi = cofactor_window(k, prime)
    return sum(all(q % ell for ell in z_primes) for q in range(lo, hi + 1))


def shell_sift_count(k: int, prime: int, z_primes: Sequence[int]) -> int:
    """Count n=pq in the raw p-shell window surviving the supplied primes < z.

    This interface assumes every supplied sifting prime is strictly smaller than
    ``prime``.  Under that condition n=pq is z-rough iff q is z-rough.
    """
    if any(ell >= prime for ell in z_primes):
        raise ValueError("every sifting prime must be smaller than shell prime")
    lo, hi = cofactor_window(k, prime)
    return sum(
        all((prime * q) % ell for ell in z_primes)
        for q in range(lo, hi + 1)
    )


def abel_prefix_recoalescence(values: Sequence[Fraction], weights: Sequence[Fraction]) -> dict[str, object]:
    """Exact Abel-prefix identity for nonincreasing nonnegative weights."""
    if len(values) != len(weights):
        raise ValueError("values and weights must have equal length")
    ws = tuple(Fraction(w) for w in weights)
    if any(w < 0 for w in ws):
        raise ValueError("weights must be nonnegative")
    if any(a < b for a, b in zip(ws, ws[1:])):
        raise ValueError("weights must be nonincreasing")
    vals = tuple(Fraction(v) for v in values)
    prefix: list[Fraction] = []
    running = Fraction(0)
    for value in vals:
        running += value
        prefix.append(running)
    extended = ws + (Fraction(0),)
    increments = tuple(extended[j] - extended[j + 1] for j in range(len(ws)))
    shell_sum = sum((w * v for w, v in zip(ws, vals)), Fraction(0))
    prefix_sum = sum((dw * v for dw, v in zip(increments, prefix)), Fraction(0))
    if shell_sum != prefix_sum:
        raise AssertionError("Abel prefix recoalescence identity failed")
    return {
        "shell_sum": shell_sum,
        "prefix_sum": prefix_sum,
        "prefix_values": tuple(prefix),
        "weight_increments": increments,
    }


def shell_remainder(k: int, prime: int, divisor: int) -> Fraction:
    """Return r_p(d)=H_{pd}(k)-H_p(k)/d exactly."""
    if divisor <= 0:
        raise ValueError("divisor must be positive")
    hp = interior_hit_count(k, prime, 2)
    hpd = interior_hit_count(k, prime * divisor, 2)
    return Fraction(hpd * divisor - hp, divisor)


def prefix_remainder(k: int, primes: Sequence[int], divisor: int) -> Fraction:
    """Aggregate shell remainders before taking absolute value."""
    return sum((shell_remainder(k, p, divisor) for p in primes), Fraction(0))


def brc_before_absolute_value(
    rows: Sequence[Mapping[int, Fraction]],
    weights: Sequence[Fraction],
    moduli: Iterable[int],
) -> dict[str, Fraction]:
    """Verify the common-modulus Abel L1 inequality.

    ``rows[i][d]`` is a shell remainder r_i(d).  Prefix rows are exact sums.
    The theorem is purely algebraic and does not assume the rows come from a
    sieve; using actual sieve rows is a specialization.
    """
    if len(rows) != len(weights):
        raise ValueError("rows and weights must have equal length")
    ws = tuple(Fraction(w) for w in weights)
    if any(w < 0 for w in ws) or any(a < b for a, b in zip(ws, ws[1:])):
        raise ValueError("weights must be nonnegative and nonincreasing")
    ds = tuple(moduli)
    extended = ws + (Fraction(0),)
    increments = tuple(extended[j] - extended[j + 1] for j in range(len(ws)))

    shell_l1 = Fraction(0)
    for w, row in zip(ws, rows):
        shell_l1 += w * sum((abs(Fraction(row.get(d, 0))) for d in ds), Fraction(0))

    running = {d: Fraction(0) for d in ds}
    prefix_l1 = Fraction(0)
    for dw, row in zip(increments, rows):
        for d in ds:
            running[d] += Fraction(row.get(d, 0))
        prefix_l1 += dw * sum((abs(running[d]) for d in ds), Fraction(0))

    if prefix_l1 > shell_l1:
        raise AssertionError("BRC-before-absolute-value inequality failed")
    return {
        "prefix_l1": prefix_l1,
        "shell_l1": shell_l1,
        "saving": shell_l1 - prefix_l1,
    }
