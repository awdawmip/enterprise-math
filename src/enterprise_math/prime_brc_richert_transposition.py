"""Exact Prime-BRC cofactor-prefix transposition identities.

Owner-local L3 research support. This module packages only finite identities:
P017/Campbell-compatible cofactor windows, Abel prefix recoalescence, and
aggregate interval-sieve remainders. It makes no P2 or prime-existence claim.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Mapping, Sequence

from .legendre import interior_hit_count
from .p017_cofactor_window import centered_cofactor_window


def _strictly_increasing(values: Sequence[int]) -> bool:
    return all(a < b for a, b in zip(values, values[1:]))


def campbell_hit_count(k: int, divisor: int) -> int:
    """Count multiples in Campbell's A(k^2)=Z intersect (k^2,k^2+2k).

    Campbell deliberately excludes the integer k^2+2k=k(k+2), whereas the
    full P017 square basin contains it. Keeping this distinction explicit
    prevents a one-endpoint mismatch in the Richert transposition.
    """
    if k < 1 or divisor <= 0:
        raise ValueError("require k>=1 and divisor>0")
    lower = k * k
    upper_inclusive = lower + 2 * k - 1
    return upper_inclusive // divisor - lower // divisor


def cofactor_window(k: int, prime: int, *, campbell: bool = False) -> tuple[int, int]:
    """Return a raw first-factor cofactor window.

    ``campbell=False`` returns canonical P017 W_p(k), including the final basin
    state k(k+2). ``campbell=True`` returns the strict-upper subwindow matching
    Campbell's analytic set A(k^2)=Z intersect (k^2,k^2+2k).
    """
    data = centered_cofactor_window(k, prime)
    lo = int(data["q_min"])
    if not campbell:
        return lo, int(data["q_max"])
    hi = (k * k + 2 * k - 1) // prime
    return lo, hi


def cofactor_windows_are_disjoint(
    k: int, primes: Sequence[int], *, campbell: bool = False
) -> bool:
    """Replay L054 disjointness; Campbell subwindows inherit it."""
    ps = tuple(primes)
    if not _strictly_increasing(ps):
        raise ValueError("primes must be strictly increasing")
    windows = [cofactor_window(k, p, campbell=campbell) for p in ps]
    return all(windows[i][1] < windows[i - 1][0] for i in range(1, len(windows)))


def cofactor_sift_count(
    k: int, prime: int, z_primes: Sequence[int], *, campbell: bool = False
) -> int:
    """Count values in the selected W_p window surviving supplied primes <z."""
    lo, hi = cofactor_window(k, prime, campbell=campbell)
    return sum(all(q % ell for ell in z_primes) for q in range(lo, hi + 1))


def shell_sift_count(
    k: int, prime: int, z_primes: Sequence[int], *, campbell: bool = False
) -> int:
    """Count n=pq in the selected p-shell window surviving primes <z.

    Every supplied sifting prime must be strictly smaller than ``prime``. Under
    that condition n=pq is z-rough iff q is z-rough.
    """
    if any(ell >= prime for ell in z_primes):
        raise ValueError("every sifting prime must be smaller than shell prime")
    lo, hi = cofactor_window(k, prime, campbell=campbell)
    return sum(
        all((prime * q) % ell for ell in z_primes)
        for q in range(lo, hi + 1)
    )


def abel_prefix_recoalescence(
    values: Sequence[Fraction], weights: Sequence[Fraction]
) -> dict[str, object]:
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


def shell_remainder(
    k: int, prime: int, divisor: int, *, campbell: bool = False
) -> Fraction:
    """Return r_p(d)=H_{pd}-H_p/d exactly for the selected interval."""
    if divisor <= 0:
        raise ValueError("divisor must be positive")
    counter = campbell_hit_count if campbell else lambda kk, dd: interior_hit_count(kk, dd, 2)
    hp = counter(k, prime)
    hpd = counter(k, prime * divisor)
    return Fraction(hpd * divisor - hp, divisor)


def prefix_remainder(
    k: int, primes: Sequence[int], divisor: int, *, campbell: bool = False
) -> Fraction:
    """Aggregate shell remainders before taking absolute value."""
    return sum(
        (shell_remainder(k, p, divisor, campbell=campbell) for p in primes),
        Fraction(0),
    )


def brc_before_absolute_value(
    rows: Sequence[Mapping[int, Fraction]],
    weights: Sequence[Fraction],
    moduli: Iterable[int],
) -> dict[str, Fraction]:
    """Verify the common-modulus Abel L1 inequality.

    ``rows[i][d]`` is a shell remainder r_i(d). Prefix rows are exact sums.
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
