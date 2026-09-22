"""Research candidate: upper-band support certificates and exact noise margins.

Same sparse collision observer and abstract periods 1..H plus above-H as the
unchanged sparse-identifiability module. No order/factorization oracle, native
geometry claim, or universal runtime/noise advantage. Compact runs certify a
support description; they do NOT generate its modular observations for free.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Iterable

from .group_ring_sparse_identifiability import (
    SparseCollisionCodebook, SparsePeriodInference, _nat, _support,
    difference_set, labeled_collision_gcd, verify_codebook,
)

Run = tuple[int, int]


def _runs(intervals: Iterable[Run], horizon: int) -> tuple[Run, ...]:
    _nat('horizon', horizon, 1)
    rows = tuple(tuple(row) for row in intervals)
    if not rows:
        raise ValueError('nonempty support runs required')
    previous = -2
    for row in rows:
        if (len(row) != 2 or any(type(x) is not int for x in row)
                or not 0 <= row[0] <= row[1] <= horizon):
            raise ValueError('runs must be closed integer intervals inside [0,H]')
        if row[0] <= previous + 1:
            raise ValueError('runs must be sorted, disjoint and maximally merged')
        previous = row[1]
    return rows


def support_runs(exponents: Iterable[int], horizon: int) -> tuple[Run, ...]:
    """O(k) conversion; reading the explicit k marks remains charged."""
    support = _support(exponents, horizon)
    out = []
    start = end = support[0]
    for x in support[1:]:
        if x == end + 1:
            end = x
        else:
            out.append((start, end))
            start = end = x
    out.append((start, end))
    return tuple(out)



def high_band_identifiable(exponents: Iterable[int], horizon: int) -> bool:
    """O(k^2) finite-set test; no H-candidate or divisor-multiple sweep.

    Executes the prior difference_set unchanged. Equal cardinality suffices
    because every counted lag is inside the exact compulsory integer band.
    This returns a boolean, not the small reusable run-pair certificate.
    """
    differences = difference_set(exponents, horizon)
    return sum(d > horizon//3 for d in differences) == horizon-horizon//3



def _lag_interval(runs: tuple[Run, ...], i: int, j: int) -> Run:
    if type(i) is not int or type(j) is not int or not 0 <= i <= j < len(runs):
        raise ValueError('invalid run-pair witness')
    return (1, runs[i][1]-runs[i][0]) if i == j else (
        runs[j][0]-runs[i][1], runs[j][1]-runs[i][0])


def _has_difference(runs: tuple[Run, ...], d: int) -> bool:
    # Test S intersect (S+d) by two sorted interval cursors, O(number of runs).
    i = j = 0
    while i < len(runs) and j < len(runs):
        lo, hi = runs[i][0]+d, runs[i][1]+d
        a, b = runs[j]
        if max(lo, a) <= min(hi, b):
            return True
        if hi < b:
            i += 1
        else:
            j += 1
    return False


@dataclass(frozen=True)
class SupportCertificate:
    status: str
    horizon: int
    runs: tuple[Run, ...]
    cover: tuple[tuple[int, int], ...] = ()
    missing_lag: int | None = None
    alias: tuple[int, int] | None = None


@dataclass(frozen=True)
class SupportCertification:
    status: str
    certificate: SupportCertificate | None
    required_run_pairs: int
    evaluated_run_pairs: int


def certify_runs(intervals: Iterable[Run], horizon: int, *,
                 max_run_pairs: int = 2_000_000) -> SupportCertification:
    """Certify D covers floor(H/3)+1..H, equivalent to all c_D(r)=r.

    R maximal runs: O(R^2 log(R+1)) construction time, O(R^2) transient
    storage. Published positive witness has only its selected run pairs and
    is checked in O(R+witness length). No H-element array or divisor sweep.
    Negative certificates identify one missing compulsory lag and its alias.
    """
    runs = _runs(intervals, horizon)
    _nat('max_run_pairs', max_run_pairs)
    required = len(runs)*(len(runs)+1)//2
    if required > max_run_pairs:
        return SupportCertification('BUDGET_EXHAUSTED', None, required, 0)
    low = horizon//3+1
    intervals_with_witness = []
    for i in range(len(runs)):
        for j in range(i, len(runs)):
            left, right = _lag_interval(runs, i, j)
            if right >= low:
                intervals_with_witness.append((left, right, i, j))
    intervals_with_witness.sort()
    cursor = low
    cover = []
    for left, right, i, j in intervals_with_witness:
        if right < cursor:
            continue
        if left > cursor:
            break
        cover.append((i, j))
        cursor = right+1
        if cursor > horizon:
            cert = SupportCertificate('IDENTIFYING', horizon, runs, tuple(cover))
            return SupportCertification('COMPLETE', cert, required, required)
    # cursor is the first uncovered compulsory difference. The only possible
    # visible proper multiple is 2*cursor, giving an exact structural alias.
    other = 2*cursor if _has_difference(runs, 2*cursor) else horizon+1
    cert = SupportCertificate('ALIASED', horizon, runs, (), cursor, (cursor, other))
    return SupportCertification('COMPLETE', cert, required, required)


def certify_support(exponents: Iterable[int], horizon: int, *,
                    max_run_pairs: int = 2_000_000) -> SupportCertification:
    return certify_runs(support_runs(exponents, horizon), horizon,
                        max_run_pairs=max_run_pairs)


def verify_support_certificate(cert: SupportCertificate) -> bool:
    """Exact scoped verifier. Forged positives/aliases and incomplete rows raise."""
    if not isinstance(cert, SupportCertificate):
        raise TypeError('SupportCertificate required')
    runs = _runs(cert.runs, cert.horizon)
    low = cert.horizon//3+1
    if cert.status == 'IDENTIFYING':
        if cert.missing_lag is not None or cert.alias is not None:
            raise ValueError('positive certificate must not carry an alias')
        cursor = low
        for pair in cert.cover:
            if len(pair) != 2:
                raise ValueError('invalid run-pair witness')
            left, right = _lag_interval(runs, *pair)
            if not left <= cursor <= right:
                raise ValueError('cover has a gap or nonextending witness')
            cursor = right+1
        if cursor <= cert.horizon:
            raise ValueError('compulsory high band not fully covered')
    elif cert.status == 'ALIASED':
        d = cert.missing_lag
        if type(d) is not int or not low <= d <= cert.horizon or cert.cover:
            raise ValueError('alias requires one compulsory missing lag')
        if _has_difference(runs, d):
            raise ValueError('purported missing lag is actually present')
        other = 2*d if _has_difference(runs, 2*d) else cert.horizon+1
        if cert.alias != (d, other):
            raise ValueError('wrong structural alias')
    else:
        raise ValueError('not a completed support certificate')
    return True



def order_from_certified_support(n: int, a: int, exponents: Iterable[int],
                                 cert: SupportCertificate) -> SparsePeriodInference:
    """Use actual labeled modular collisions, not a supplied gcd/order value.

    Explicit support input and its k modular exponentiations are charged.
    Compact support certificates do not authorize implicit expansion of huge runs.
    """
    verify_support_certificate(cert)
    if cert.status != 'IDENTIFYING':
        raise ValueError('identifying support certificate required')
    support = _support(exponents, cert.horizon)
    if support_runs(support, cert.horizon) != cert.runs:
        raise ValueError('certificate does not bind the actual support')
    result = labeled_collision_gcd(n, a, support, cert.horizon)
    r = result.gcd_multiple
    if r == 0:
        return SparsePeriodInference('ORDER_ABOVE_HORIZON', None, cert.horizon+1)
    return SparsePeriodInference('EXACT_FROM_CERTIFIED_SUPPORT', r, r)



def support_mark_lower_bound(horizon: int) -> int:
    """Necessary, not sufficient or asserted optimal. Scope: fixed [0,H].

    Choose(k,2)>=H-floor(H/3). Also floor(k^2/4)>=ceil(H/2), since
    differences >H/2 cross the two halves of [0,H].
    """
    H = _nat('horizon', horizon, 1)
    need = H-H//3
    k = (1+isqrt(1+8*need))//2
    while k*(k-1)//2 < need:
        k += 1
    long_need = (H+1)//2
    ell = isqrt(4*long_need)
    if ell*ell < 4*long_need:
        ell += 1
    return max(k, ell)


def _exact(value, name: str) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ValueError(f'{name} requires an exact int or Fraction; no floats')
    return Fraction(value)


def _codes(book: SparseCollisionCodebook, normalized: bool) -> tuple:
    if type(normalized) is not bool:
        raise ValueError('normalized must be bool')
    verify_codebook(book)  # Execute the original full finite verifier unchanged.
    scales = tuple(sum(w)**2 for w in book.profiles)
    return tuple(tuple(Fraction(v, scales[j] if normalized else 1)
                       for j, v in enumerate(row)) for row in book.codes)


@dataclass(frozen=True)
class ReadoutMargin:
    status: str
    normalized: bool
    erased_channels: int
    minimum_gap: Fraction | None
    critical_pair: tuple[int, int] | None
    critical_erased: tuple[int, ...]
    required_pair_checks: int
    executed_pair_checks: int


def certify_readout_margin(book: SparseCollisionCodebook, *, normalized: bool = True,
                           erased_channels: int = 0,
                           max_pair_checks: int = 2_000_000) -> ReadoutMargin:
    """Exact worst-case L-infinity separation after <=e MARKED erasures.

    A pair's residual gap is its (e+1)-th largest coordinate difference.
    Additive error <=epsilon is universally unique iff 2*epsilon<gap.
    Equality has a midpoint ambiguity witness. Not an unmarked-corruption or
    stochastic-noise theorem. Full codebook verification is separately charged.
    Scalar minima use sorted neighbors; multiple channels use all pairs.
    """
    codes = _codes(book, normalized)
    _nat('erased_channels', erased_channels)
    _nat('max_pair_checks', max_pair_checks)
    channels = len(book.profiles)
    if erased_channels >= channels:
        raise ValueError('at least one retained channel required')
    size = len(codes)
    required = size-1 if channels == 1 else size*(size-1)//2
    if required > max_pair_checks:
        return ReadoutMargin('BUDGET_EXHAUSTED', normalized, erased_channels,
                             None, None, (), required, 0)
    if channels == 1:
        ordered = sorted(range(size), key=lambda i: codes[i][0])
        pairs = zip(ordered, ordered[1:])
    else:
        pairs = ((i, j) for i in range(size) for j in range(i+1, size))
    best = None
    critical = None
    erased = ()
    checks = 0
    for i, j in pairs:
        diffs = sorted(((abs(x-y), t) for t, (x, y) in
                        enumerate(zip(codes[i], codes[j]))),
                       key=lambda row: (-row[0], row[1]))
        gap = diffs[erased_channels][0]
        checks += 1
        if best is None or gap < best:
            best = gap
            critical = (i+1, j+1)
            erased = tuple(sorted(t for _, t in diffs[:erased_channels]))
    return ReadoutMargin('COMPLETE', normalized, erased_channels, best,
                         critical, erased, required, checks)


def verify_readout_margin(book: SparseCollisionCodebook, cert: ReadoutMargin, *,
                          max_pair_checks: int = 2_000_000) -> bool:
    if not isinstance(cert, ReadoutMargin) or cert.status != 'COMPLETE':
        raise ValueError('completed ReadoutMargin required')
    rebuilt = certify_readout_margin(book, normalized=cert.normalized,
        erased_channels=cert.erased_channels, max_pair_checks=max_pair_checks)
    if rebuilt.status != 'COMPLETE' or cert != rebuilt:
        raise ValueError('margin not reproduced from verified codebook')
    return True


@dataclass(frozen=True)
class BoundedNoiseInference:
    status: str
    candidates: tuple[int, ...]  # H+1 denotes the aggregate above-H hypothesis.
    order: int | None
    lower_bound: int | None


def decode_bounded_readout(book: SparseCollisionCodebook, values: Iterable,
                           epsilon: int | Fraction, *, normalized: bool = True,
                           erased: Iterable[int] = ()) -> BoundedNoiseInference:
    """Return ALL candidates consistent with the declared exact error box.

    No nearest-neighbor guess, measurement authentication, or probability claim.
    Erased coordinates are explicitly marked; they may contain None. Building
    and verifying the H+1-code decoder is NOT free, and is performed here too.
    """
    codes = _codes(book, normalized)
    epsilon = _exact(epsilon, 'epsilon')
    if epsilon < 0:
        raise ValueError('epsilon must be nonnegative')
    values = tuple(values)
    removed = tuple(erased)
    channels = len(book.profiles)
    if (len(values) != channels or any(type(t) is not int or not 0 <= t < channels
                                      for t in removed)
            or len(set(removed)) != len(removed) or len(removed) >= channels):
        raise ValueError('invalid channels/erasures')
    keep = tuple(t for t in range(channels) if t not in removed)
    observed = {t: _exact(values[t], 'readout') for t in keep}
    candidates = tuple(i+1 for i, code in enumerate(codes)
                       if all(abs(code[t]-observed[t]) <= epsilon for t in keep))
    if len(candidates) != 1:
        return BoundedNoiseInference('AMBIGUOUS' if candidates else 'INCONSISTENT',
                                     candidates, None, None)
    r = candidates[0]
    if r == book.horizon+1:
        return BoundedNoiseInference('ORDER_ABOVE_HORIZON_CONDITIONAL', candidates, None, r)
    return BoundedNoiseInference('UNIQUE_CONDITIONAL_ON_ERROR_BOUND', candidates, r, r)
