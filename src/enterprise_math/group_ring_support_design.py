"""Scoped support design and adversarial MARK erasures (research candidate).

Uses the preceding upper-band criterion unchanged: fixed S in [0,H] identifies
all abstract periods 1..H and above-H iff its differences cover floor(H/3)+1..H.
This is not arbitrary noisy residue corruption, channel erasure, or a new
sub-square-root order algorithm. An inclusion-minimal support is not necessarily
minimum-cardinality. Deleting marks changes collision masses; only bounded
period identifiability is retained. Protected marks are a caller assumption.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations
from math import isqrt
from typing import Iterable

from .group_ring_sparse_identifiability import (
    _nat, _support, labeled_collision_gcd, SparsePeriodInference,
)
from .group_ring_support_certificates import high_band_identifiable


@dataclass(frozen=True)
class TailRulerParameters:
    horizon: int
    compulsory_count: int
    width: int
    blocks: int
    mark_upper_bound: int


def tail_ruler_parameters(horizon: int) -> TailRulerParameters:
    """Constant-many exact integer operations; does NOT expand the support."""
    H = _nat('horizon', horizon, 1)
    W = H-H//3
    b = isqrt(W)
    q = (W+b-1)//b
    return TailRulerParameters(H, W, b, q, b+q)


def tail_ruler(horizon: int, *, max_marks: int = 1_000_000) -> tuple[int, ...]:
    """0..b-1 union {H-j*b:0<=j<q}, b=floor(sqrt(W)), q=ceil(W/b).

    Cross differences cover [H-q*b+1,H], containing the compulsory band.
    b+q=ceil(2*sqrt(W)) is an upper bound, not global optimality. The cap
    checks this conservative bound before allocation, not observation bit cost.
    """
    p = tail_ruler_parameters(horizon)
    _nat('max_marks', max_marks)
    if p.mark_upper_bound > max_marks:
        raise ValueError('support expansion exceeds max_marks')
    return tuple(sorted(set(range(p.width)) |
                        {p.horizon-j*p.width for j in range(p.blocks)}))


def tail_ruler_order(n: int, a: int, horizon: int, *,
                     max_marks: int = 1_000_000) -> SparsePeriodInference:
    """Use unchanged labeled_collision_gcd on the proved construction.

    Each retained mark is actually evaluated by the inherited implementation.
    No codebook/known order is an input. This costs k modular exponentiations,
    not the k modular products of a separately optimized block evaluator.
    """
    s = tail_ruler(horizon, max_marks=max_marks)
    ans = labeled_collision_gcd(n, a, s, horizon)
    r = ans.gcd_multiple
    return (SparsePeriodInference('ORDER_ABOVE_HORIZON', None, horizon+1)
            if r == 0 else SparsePeriodInference('EXACT_FROM_TAIL_RULER', r, r))


def _protected(values: Iterable[int], support: tuple[int, ...]) -> tuple[int, ...]:
    p = tuple(values)
    if any(type(x) is not int for x in p) or len(p) != len(set(p)):
        raise ValueError('distinct integer protected marks required')
    if not set(p).issubset(support):
        raise ValueError('protected marks must belong to support')
    return tuple(sorted(p))


def _pair_count(s):
    return len(s)*(len(s)-1)//2


def _counts(s, H):
    return Counter(y-x for i,x in enumerate(s) for y in s[i+1:]
                   if y-x > H//3)


@dataclass(frozen=True)
class SupportReduction:
    status: str
    horizon: int
    original: tuple[int, ...]
    protected: tuple[int, ...]
    support: tuple[int, ...]
    removed: tuple[int, ...]
    essential_lags: tuple[tuple[int, int], ...]
    required_pairs: int


def prune_identifying_support(exponents: Iterable[int], horizon: int, *,
                              protected: Iterable[int] = (),
                              order: Iterable[int] | None = None,
                              max_pairs: int = 2_000_000) -> SupportReduction:
    """One-pass, inclusion-minimal deletion with exact lag multiplicities.

    O(k^2) pair/incident visits, O(k^2) stored distinct lags in worst case.
    A mark once found essential cannot become removable after further deletions
    that keep coverage: all edges for its witness lag still meet that mark.
    This is not a minimum-cardinality or deletion-robustness guarantee.
    """
    s = _support(exponents, horizon); p = _protected(protected, s)
    _nat('max_pairs', max_pairs)
    scan = tuple(s if order is None else order)
    if (any(type(x) is not int for x in scan) or len(scan) != len(s)
            or set(scan) != set(s)):
        raise ValueError('order must be a permutation of the whole support')
    pairs = _pair_count(s)
    if pairs > max_pairs:
        return SupportReduction('BUDGET_EXHAUSTED', horizon, s, p, s, (), (), pairs)
    counts = _counts(s, horizon)
    if len(counts) != horizon-horizon//3:
        raise ValueError('initial support is not identifying')
    current = set(s); removed = []
    for x in scan:
        if x in p:
            continue
        incident = Counter(abs(x-y) for y in current if abs(x-y) > horizon//3)
        if all(counts[d] > amount for d,amount in incident.items()):
            current.remove(x); removed.append(x)
            counts.subtract(incident)
    final = tuple(sorted(current)); witnesses = []
    for x in final:
        if x in p:
            continue
        incident = Counter(abs(x-y) for y in final if abs(x-y) > horizon//3)
        blockers = [d for d, amount in incident.items() if counts[d] == amount]
        if not blockers:
            raise AssertionError('one-pass minimality invariant failed')
        witnesses.append((x, min(blockers)))
    return SupportReduction('COMPLETE', horizon, s, p, final, tuple(removed),
                            tuple(witnesses), pairs)


def verify_support_reduction(result: SupportReduction) -> bool:
    """Replay allowed deletion order and independently execute old band test."""
    if not isinstance(result, SupportReduction) or result.status != 'COMPLETE':
        raise ValueError('completed SupportReduction required')
    original = _support(result.original, result.horizon)
    p = _protected(result.protected, original)
    final = _support(result.support, result.horizon)
    if (len(result.removed) != len(set(result.removed))
            or any(type(x) is not int or x in p for x in result.removed)
            or set(original)-set(result.removed) != set(final)
            or not set(result.removed).issubset(original)
            or result.required_pairs != _pair_count(original)):
        raise ValueError('invalid deletion/domain binding')
    if not high_band_identifiable(final, result.horizon):
        raise ValueError('final support lost compulsory coverage')
    if tuple(x for x,d in result.essential_lags) != tuple(x for x in final if x not in p):
        raise ValueError('one essential witness per unprotected retained mark required')
    for x,d in result.essential_lags:
        if type(x) is not int:
            raise ValueError('witness mark must be an integer')
        if type(d) is not int or not result.horizon//3 < d <= result.horizon:
            raise ValueError('invalid compulsory-lag witness')
        remainder = set(final)-{x}
        if any(y+d in remainder for y in remainder):
            raise ValueError('purported essential lag survives deletion')
    return True


@dataclass(frozen=True)
class MarkErasureCertificate:
    horizon: int
    support: tuple[int, ...]
    protected: tuple[int, ...]
    minimum_deletions: int | None
    witness_lag: int | None
    erased_marks: tuple[int, ...]


@dataclass(frozen=True)
class MarkErasureAnalysis:
    status: str
    certificate: MarkErasureCertificate | None
    required_pairs: int
    evaluated_pairs: int


def _destroy_lag(edges, d, protected):
    """Minimum allowed vertex cover, via components of at most three marks.

    None means one fully protected edge makes this lag impossible to destroy.
    Exact integer distance d>H/3 forbids a four-vertex path inside [0,H].
    """
    if any(x in protected and y in protected for x,y in edges):
        return None
    lefts = {x for x,y in edges}
    erased = []
    for start in sorted(x for x in lefts if x-d not in lefts):
        vertices = [start]
        while vertices[-1] in lefts:
            vertices.append(vertices[-1]+d)
        if len(vertices) > 3:
            raise AssertionError('upper-band component exceeded three vertices')
        allowed = [x for x in vertices if x not in protected]
        winner = None
        for amount in range(len(allowed)+1):
            for choice in combinations(allowed, amount):
                chosen = set(choice)
                if all(x in chosen or y in chosen for x,y in zip(vertices, vertices[1:])):
                    winner = choice; break
            if winner is not None:
                break
        if winner is None:
            raise AssertionError('uncovered protected edge should have been detected')
        erased.extend(winner)
    return tuple(sorted(erased))


def certify_mark_erasures(exponents: Iterable[int], horizon: int, *,
                         protected: Iterable[int] = (),
                         max_pairs: int = 2_000_000) -> MarkErasureAnalysis:
    """Exact smallest adversarial MARK deletion that destroys identifiability.

    This is NOT the preceding channel-erasure/noise decoder. The remaining
    support may require redesigned weights. None minimum means immune because
    the protected core alone covers every mandatory lag; zero means already
    nonidentifying. Pair-cap refusal produces no robustness certificate.
    """
    s = _support(exponents, horizon); p = _protected(protected, s)
    _nat('max_pairs', max_pairs); pairs = _pair_count(s)
    if pairs > max_pairs:
        return MarkErasureAnalysis('BUDGET_EXHAUSTED', None, pairs, 0)
    edges = defaultdict(list)
    for i,x in enumerate(s):
        for y in s[i+1:]:
            if y-x > horizon//3:
                edges[y-x].append((x,y))
    if len(edges) != horizon-horizon//3:
        missing = next(d for d in range(horizon//3+1,horizon+1) if d not in edges)
        c = MarkErasureCertificate(horizon,s,p,0,missing,())
        return MarkErasureAnalysis('COMPLETE',c,pairs,pairs)
    best = None; best_lag = None; protected_set = set(p)
    for d in sorted(edges, reverse=True):
        deletion = _destroy_lag(edges[d],d,protected_set)
        if deletion is not None and (best is None or len(deletion) < len(best)):
            best,best_lag = deletion,d
            if len(best) == 1:
                break  # positive coverage makes 1 globally minimal
    c = MarkErasureCertificate(horizon,s,p,None if best is None else len(best),
                               best_lag,() if best is None else best)
    return MarkErasureAnalysis('COMPLETE',c,pairs,pairs)


def verify_mark_erasure_certificate(cert: MarkErasureCertificate, *,
                                    max_pairs: int = 2_000_000) -> bool:
    if not isinstance(cert, MarkErasureCertificate):
        raise TypeError('MarkErasureCertificate required')
    if cert.minimum_deletions is not None:
        _nat('minimum_deletions',cert.minimum_deletions)
    result = certify_mark_erasures(cert.support,cert.horizon,
                                   protected=cert.protected,max_pairs=max_pairs)
    if result.status != 'COMPLETE':
        raise ValueError('verification budget exhausted')
    if result.certificate != cert:
        raise ValueError('erasure certificate differs from exact graph computation')
    return True
