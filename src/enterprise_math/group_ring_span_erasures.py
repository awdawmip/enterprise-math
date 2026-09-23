"""Expanded-span collision identifiability and adversarial mark loss.

Research candidate. H bounds the order to identify; A bounds sampled exponents.
Above-H orders need not have the same observations when A>H. They are only one
OUTPUT class. No protected endpoints, noise, or known order is assumed by the
robust-tail construction. All arbitrary-support certificates are replayable local
data, not authenticated remote/physical measurements. Existing sparse arithmetic
and fixed-span certificates are not modified.
"""
from __future__ import annotations

from bisect import bisect_right
from collections import defaultdict
from dataclasses import dataclass
from math import gcd, isqrt
from typing import Iterable

from .group_ring_sparse_identifiability import (
    _nat, _support, difference_set, labeled_collision_gcd, SparsePeriodInference,
)
from .group_ring_support_design import _protected


def target_closures(exponents: Iterable[int], horizon: int, span: int) -> tuple[int, ...]:
    """Old difference-set law with separate target H and exponent span A.

    c_D(r)=r for all r<=H is necessary and sufficient against ALL other orders,
    including H<r<=A. This reference routine costs O(k^2+H*|D|) gcd/mod visits.
    """
    _nat('horizon', horizon, 1)
    ds = difference_set(exponents, span)
    result = []
    for r in range(1, horizon+1):
        c = 0
        for d in ds:
            if d % r == 0:
                c = gcd(c, d)
        result.append(c)
    return tuple(result)


def _primes(limit: int) -> tuple[int, ...]:
    """Bounded elementary sieve; caller checks allocation limit first."""
    bits = bytearray(b'\x01') * (limit+1)
    if limit >= 0:
        bits[0] = 0
    if limit >= 1:
        bits[1] = 0
    for p in range(2, isqrt(limit)+1):
        if bits[p]:
            count = (limit-p*p)//p+1
            bits[p*p:limit+1:p] = b'\x00'*count
    return tuple(i for i in range(2, limit+1) if bits[i])


def _coarsening_cut(s: tuple[int, ...], r: int, p: int,
                    protected: frozenset[int]) -> tuple[int, ...] | None:
    """Minimum allowed deletion making r and p*r equality partitions identical.

    Inside each residue mod r, all survivors must lie in ONE residue mod p*r.
    Distinct protected fine classes make this coarsening impossible (None).
    Otherwise keep the largest allowed fine class. This is a complete multipartite
    vertex-cover calculation, not an enumeration of deletion subsets.
    """
    groups = defaultdict(lambda: defaultdict(list))
    for x in s:
        groups[x % r][x % (p*r)].append(x)
    erased = []
    for fine in groups.values():
        forced = [key for key, xs in fine.items() if any(x in protected for x in xs)]
        if len(forced) > 1:
            return None
        keep = forced[0] if forced else min(fine, key=lambda key: (-len(fine[key]), key))
        for key, xs in fine.items():
            if key != keep:
                erased.extend(xs)
    return tuple(sorted(erased))


@dataclass(frozen=True)
class SpanErasureCertificate:
    horizon: int
    span: int
    support: tuple[int, ...]
    protected: tuple[int, ...]
    minimum_deletions: int | None
    witness_period: int | None
    alias_period: int | None
    erased_marks: tuple[int, ...]


@dataclass(frozen=True)
class SpanErasureAnalysis:
    status: str
    certificate: SpanErasureCertificate | None
    partition_count: int
    required_mark_visits: int
    evaluated_partitions: int


def certify_span_erasures(exponents: Iterable[int], horizon: int, span: int, *,
                         protected: Iterable[int] = (),
                         max_sieve_span: int = 1_000_000,
                         max_mark_visits: int = 5_000_000) -> SpanErasureAnalysis:
    """Exact least MARK erasures destroying identification of some r<=H.

    Test r versus p*r for primes p<=A/r and p=2 always. A nonzero false closure
    c>r has a prime factor of c/r; zero closure is also caught by p=2. This covers
    failure against an above-H order, not just pairs of small orders.

    No exponential erasure sweep. Sieve O(A) memory; V=k*sum_r max(1,pi(A/r))
    mark insertions plus dictionary/protection/sorting costs. Preflight counts
    the full worst-case scan; a cap refusal provides NO robustness certificate.
    """
    H = _nat('horizon', horizon, 1)
    s = _support(exponents, span)
    protected_tuple = _protected(protected, s)
    _nat('max_sieve_span', max_sieve_span)
    _nat('max_mark_visits', max_mark_visits)
    if H > span:
        cert = SpanErasureCertificate(H, span, s, protected_tuple, 0,
                                      span+1, 2*(span+1), ())
        return SpanErasureAnalysis('COMPLETE', cert, 0, 0, 0)
    if span > max_sieve_span:
        return SpanErasureAnalysis('BUDGET_EXHAUSTED', None, 0, 0, 0)
    primes = _primes(span)
    counts = tuple(max(1, bisect_right(primes, span//r)) for r in range(1, H+1))
    partitions = sum(counts)
    required = len(s)*partitions
    if required > max_mark_visits:
        return SpanErasureAnalysis('BUDGET_EXHAUSTED', None, partitions, required, 0)
    P = frozenset(protected_tuple)
    best = None
    winner = (None, None)
    evaluated = 0
    for r, count in enumerate(counts, 1):
        ps = primes[:count] if span//r >= 2 else (2,)
        for p in ps:
            erased = _coarsening_cut(s, r, p, P)
            evaluated += 1
            if erased is not None and (best is None or len(erased) < len(best)):
                best, winner = erased, (r, p*r)
                if not best:
                    break
        if best == ():
            break
    cert = SpanErasureCertificate(H, span, s, protected_tuple,
                                 None if best is None else len(best),
                                 *winner, () if best is None else best)
    return SpanErasureAnalysis('COMPLETE', cert, partitions, required, evaluated)


def verify_span_erasure_certificate(cert: SpanErasureCertificate, **budgets) -> bool:
    """Replay actual certificate content; do not trust a caller's minimum flag."""
    if not isinstance(cert, SpanErasureCertificate):
        raise TypeError('SpanErasureCertificate required')
    if cert.minimum_deletions is not None:
        _nat('minimum_deletions', cert.minimum_deletions)
        _nat('witness_period', cert.witness_period, 1)
        _nat('alias_period', cert.alias_period, 1)
    replay = certify_span_erasures(cert.support, cert.horizon, cert.span,
                                  protected=cert.protected, **budgets)
    if replay.status != 'COMPLETE' or replay.certificate != cert:
        raise ValueError('unverified, forged or over-budget erasure certificate')
    return True


def interval_period_threshold(span: int, period: int) -> int:
    """For full 0..A, min deletions losing the fixed-point evidence c_D(r)=r.

    r versus 2r attains the minimum: sum over residue classes floor(size/2).
    Periods larger than A have zero threshold. No marks are allocated here.
    """
    _nat('span', span)
    _nat('period', period, 1)
    q, t = divmod(span+1, 2*period)
    return q*period + max(0, t-period)


def full_interval_threshold(span: int, horizon: int, *, max_periods: int = 1_000_000) -> int:
    """Exact destructive threshold, not the number of safely lost marks."""
    _nat('span', span)
    _nat('horizon', horizon, 1)
    _nat('max_periods', max_periods)
    if horizon > span:
        return 0
    if horizon > max_periods:
        raise ValueError('period evaluation budget exhausted')
    return min(interval_period_threshold(span, r) for r in range(1, horizon+1))


@dataclass(frozen=True)
class MinimumSpanResult:
    status: str
    horizon: int
    losses: int
    minimum_span: int | None
    limiting_period: int | None
    evaluated_blocks: int


def minimum_erasure_span(horizon: int, losses: int, *,
                         max_blocks: int = 1_000_000) -> MinimumSpanResult:
    """Least possible A for ANY support surviving all <=e unprotected losses.

    Dense support attains it; this does not minimize mark count. With E=e+1,
    A_min=E-1+max_{1<=r<=H} r*ceil(E/r). For e<H this equals e+max(H,2e).
    General evaluation groups equal floor((E-1)/r), O(min(H,sqrt(E))) blocks.
    Returns BUDGET_EXHAUSTED without an asserted span if the block cap binds.
    """
    H = _nat('horizon', horizon, 1)
    e = _nat('losses', losses)
    _nat('max_blocks', max_blocks)
    if e < H:
        r = H if H >= 2*e else e
        return MinimumSpanResult('COMPLETE', H, e, e+max(H, 2*e), r, 0)
    E = e+1
    r = 1
    best = -1
    witness = None
    blocks = 0
    while r <= H:
        if blocks == max_blocks:
            return MinimumSpanResult('BUDGET_EXHAUSTED', H, e, None, None, blocks)
        q = (E-1)//r
        end = H if q == 0 else min(H, (E-1)//q)
        value = end*(q+1)
        if value > best:
            best, witness = value, end
        blocks += 1
        r = end+1
    return MinimumSpanResult('COMPLETE', H, e, E+best-1, witness, blocks)


@dataclass(frozen=True)
class RobustTailParameters:
    horizon: int
    losses: int
    span: int
    width: int
    blocks: int
    mark_upper_bound: int


def robust_tail_parameters(horizon: int, losses: int, *,
                           width: int | None = None) -> RobustTailParameters:
    """Span-optimal sparse construction for 0<=e<=floor(H/3).

    Thicken both parts of a tail ruler by offsets 0..e. For each mandatory
    d>H/3>=e, its e+1 translated witnessing pairs are vertex-disjoint.
    No endpoint is protected. This parameter function does not expand marks.
    """
    H = _nat('horizon', horizon, 1)
    e = _nat('losses', losses)
    if e > H//3:
        raise ValueError('this sparse construction requires losses<=floor(H/3)')
    W = H-H//3
    b = isqrt((e+1)*W) if width is None else _nat('width', width, 1)
    if b > W:
        raise ValueError('width exceeds required band size')
    q = (W+b-1)//b
    return RobustTailParameters(H, e, H+e, b, q, b+e+(e+1)*q)


def robust_mark_lower_bound(horizon: int, losses: int) -> int:
    """Necessary mark count at the minimum span H+e, for 0<=e<=H/2.

    Every target lag r>(H+e)/2 needs e+1 disjoint pairs. Such pairs cross the
    span midpoint. Mandatory endpoint strips also force 2(e+1) marks.
    This bound is not claimed sufficient or globally tight.
    """
    H = _nat('horizon', horizon, 1)
    e = _nat('losses', losses)
    if 2*e > H:
        raise ValueError('this bound assumes losses<=H/2 and span=H+losses')
    pairs = (e+1)*(H-(H+e)//2)
    root = isqrt(4*pairs)
    root += root*root < 4*pairs
    return max(2*(e+1), root)


def robust_tail_support(horizon: int, losses: int, *, width: int | None = None,
                        max_marks: int = 1_000_000) -> tuple[int, ...]:
    p = robust_tail_parameters(horizon, losses, width=width)
    _nat('max_marks', max_marks)
    if p.mark_upper_bound > max_marks:
        raise ValueError('support expansion exceeds max_marks')
    marks = set(range(p.width+p.losses))
    marks.update(p.horizon-j*p.width+t for j in range(p.blocks)
                 for t in range(p.losses+1))
    return tuple(sorted(marks))


def translated_lag_witness(params: RobustTailParameters, lag: int) -> tuple[tuple[int, int], ...]:
    """e+1 disjoint pairs for ONE mandatory lag; not a materialized H-wide table."""
    if not isinstance(params, RobustTailParameters):
        raise TypeError('RobustTailParameters required')
    if params != robust_tail_parameters(params.horizon, params.losses, width=params.width):
        raise ValueError('forged robust-tail parameters')
    _nat('lag', lag, 1)
    if not params.horizon//3 < lag <= params.horizon:
        raise ValueError('lag outside mandatory target band')
    j, i = divmod(params.horizon-lag, params.width)
    return tuple((i+t, params.horizon-j*params.width+t) for t in range(params.losses+1))


def robust_tail_order(n: int, a: int, horizon: int, losses: int, *,
                      erased: Iterable[int] = (), width: int | None = None,
                      max_marks: int = 1_000_000) -> SparsePeriodInference:
    """Evaluate actual surviving powers using inherited labeled_collision_gcd.

    Losses are MARKED erasures supplied by the caller, not corrupted residues.
    Gcd zero OR greater than H means above-H, even when above-H orders collide
    inside the expanded span. Each survivor costs an actual modular pow.
    """
    p = robust_tail_parameters(horizon, losses, width=width)
    s = robust_tail_support(horizon, losses, width=width, max_marks=max_marks)
    missing = _protected(erased, s)  # same strict subset/type check, no protection implied
    if len(missing) > losses:
        raise ValueError('erasure count exceeds certified budget')
    absent = set(missing)
    kept = tuple(x for x in s if x not in absent)
    observed = labeled_collision_gcd(n, a, kept, p.span)
    r = observed.gcd_multiple
    if r == 0 or r > horizon:
        return SparsePeriodInference('ORDER_ABOVE_HORIZON', None, horizon+1)
    return SparsePeriodInference('EXACT_FROM_ROBUST_TAIL', r, r)
