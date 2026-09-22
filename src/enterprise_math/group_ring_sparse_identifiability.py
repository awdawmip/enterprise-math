"""Finite sparse-support collision identifiability (research candidate).

All weights are POSITIVE INTEGER multiplicities on the declared sparse support;
missing exponents have weight zero. This is not a phase/noise/quantum model.
Structural period signatures characterize which periods any reweighting can
separate. A randomized search publishes only an exactly checked finite codebook.
Its O(H) decoder and O(H log H) preprocessing are charged, never free oracles.
Sparse rulers and polynomial grid separation are classical ingredients.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt
from random import Random
from types import MappingProxyType
from typing import Iterable, Mapping


def _nat(name, value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f'{name} must be an integer >= {minimum}')
    return value


def _support(exponents, horizon):
    _nat('horizon', horizon, 1)
    s = tuple(exponents)
    if not s or any(type(x) is not int or not 0 <= x <= horizon for x in s):
        raise ValueError('nonempty integer support inside [0,horizon] required')
    if any(x >= y for x, y in zip(s, s[1:])):
        raise ValueError('support must be strictly increasing; duplicates are not merged')
    return s


def _weights(values, size):
    w = tuple(values)
    if len(w) != size or any(type(x) is not int or x <= 0 for x in w):
        raise ValueError('one positive integer weight per support position required')
    return w


def sparse_ruler(horizon: int) -> tuple[int, ...]:
    """A simple complete ruler in [0,H] with at most 2*ceil(sqrt(H))+1 marks."""
    H = _nat('horizon', horizon, 1)
    b = isqrt(H)
    b += b*b < H
    return tuple(sorted(set(range(b)) | set(range(b, H+1, b)) | {H}))


def difference_set(exponents: Iterable[int], horizon: int) -> frozenset[int]:
    s = _support(exponents, horizon)
    return frozenset(y-x for i, x in enumerate(s) for y in s[i+1:])


def period_closures(exponents: Iterable[int], horizon: int) -> tuple[int, ...]:
    """c_D(r)=gcd{d in D : r divides d}; gcd(empty)=0, for r=1..H and r>H.

    The zero label represents the no-collision class. Positive labels are
    multiples of their candidate periods, NOT automatically the true periods.
    Equal labels are exactly equal complete collision partitions on the support.
    """
    differences = difference_set(exponents, horizon)
    out = []
    for r in range(1, horizon+1):
        value = 0
        for d in range(r, horizon+1, r):
            if d in differences:
                value = gcd(value, d)
        out.append(value)
    return tuple(out)+(0,)


def structural_alias(exponents: Iterable[int], horizon: int) -> tuple[int, int] | None:
    """First indistinguishable periods; H+1 represents every order above H.

    The gcd closure is an exact compression of the divisibility signature.
    Full bounded identifiability is equivalent to c_D(r)=r for every r<=H.
    Equality here is equality for EVERY positive weight assignment.
    """
    seen = {}
    for r, closure in enumerate(period_closures(exponents, horizon), 1):
        if closure in seen:
            return seen[closure], r
        seen[closure] = r
    return None


def collision_spectrum(exponents: Iterable[int], weights: Iterable[int],
                       horizon: int) -> tuple[int, ...]:
    """Conditional K_w(r) for r=1..H followed by the r>H baseline.

    Pair products cost k(k-1)/2; divisor-multiple visits sum_r floor(H/r).
    No ambient group, actual order or discrete logarithm is used offline.
    """
    s = _support(exponents, horizon)
    w = _weights(weights, len(s))
    lag = [0]*(horizon+1)
    for i, x in enumerate(s):
        for j in range(i+1, len(s)):
            lag[s[j]-x] += w[i]*w[j]
    baseline = sum(x*x for x in w)
    return tuple(baseline+2*sum(lag[d] for d in range(r, horizon+1, r))
                 for r in range(1, horizon+1)) + (baseline,)


def _group(n, a):
    _nat('n', n, 2)
    _nat('a', a, 1)
    if a >= n or gcd(a, n) != 1:
        raise ValueError('base must be a canonical unit modulo n')


def collision_readouts(n: int, a: int, exponents: Iterable[int],
                       profiles: Iterable[Iterable[int]], horizon: int) -> tuple[int, ...]:
    """Exact modular occupancy readouts; compute each residue only once.

    k modular exponentiations (not unit-cost multiplications), O(k*t) weight
    additions/squares across t channels. No supplied order or decoder access.
    """
    _group(n, a)
    s = _support(exponents, horizon)
    profiles = tuple(_weights(w, len(s)) for w in profiles)
    if not profiles:
        raise ValueError('at least one profile required')
    residues = tuple(pow(a, x, n) for x in s)
    out = []
    for weights in profiles:
        buckets = {}
        for u, weight in zip(residues, weights):
            buckets[u] = buckets.get(u, 0)+weight
        out.append(sum(value*value for value in buckets.values()))
    return tuple(out)


@dataclass(frozen=True)
class SparsePeriodInference:
    status: str
    order: int | None
    lower_bound: int


@dataclass(frozen=True)
class SparseCollisionCodebook:
    horizon: int
    support: tuple[int, ...]
    profiles: tuple[tuple[int, ...], ...]
    codes: tuple[tuple[int, ...], ...]
    _lookup: Mapping[tuple[int, ...], int]

    def decode(self, values: Iterable[int]) -> SparsePeriodInference:
        """A scalar/vector is trusted input, not an authenticated measurement."""
        key = tuple(values)
        if len(key) != len(self.profiles) or any(type(v) is not int or v < 0 for v in key):
            raise ValueError('one nonnegative exact integer readout per profile required')
        r = self._lookup.get(key)
        if r is None:
            raise ValueError('readout not in the certified finite codebook')
        if r == self.horizon+1:
            return SparsePeriodInference('ORDER_ABOVE_HORIZON', None, r)
        return SparsePeriodInference('EXACT_CONDITIONAL_ON_READOUT', r, r)

    def observe(self, n: int, a: int) -> tuple[int, ...]:
        return collision_readouts(n, a, self.support, self.profiles, self.horizon)


def verify_codebook(book: SparseCollisionCodebook) -> bool:
    """Recompute all masses and reject forged tables/mappings. Local, not signed."""
    if not isinstance(book, SparseCollisionCodebook):
        raise TypeError('SparseCollisionCodebook required')
    _support(book.support, book.horizon)
    if not book.profiles:
        raise ValueError('empty profile list')
    spectra = tuple(collision_spectrum(book.support, w, book.horizon) for w in book.profiles)
    codes = tuple(zip(*spectra))
    expected = {code: r for r, code in enumerate(codes, 1)}
    if len(expected) != book.horizon+1 or codes != book.codes or dict(book._lookup) != expected:
        raise ValueError('invalid or noninjective codebook')
    return True


@dataclass(frozen=True)
class SparseCompilation:
    status: str
    codebook: SparseCollisionCodebook | None
    alias: tuple[int, int] | None
    trials: int
    pair_products: int
    multiple_visits: int


def compile_sparse_codebook(horizon: int, exponents: Iterable[int] | None = None, *,
                            alphabet: str = 'large', seed: int = 20260922,
                            max_trials: int = 128, max_horizon: int = 100_000,
                            max_work: int = 20_000_000) -> SparseCompilation:
    """Search then EXACTLY certify. Failed search is not structural impossibility.

    Large alphabet: each independent trial uses weights 1..2*(H+1)*H;
    a uniform ideal draw separates all distinct signatures with probability >=1/2.
    Binary alphabet: weights 1,2, accumulating channels; each pair remains equal
    after t independent draws with probability <=(3/4)^t. Seeded PRNG is used
    for reproducibility, not as a proof of randomness. Acceptance is deterministic.
    """
    H = _nat('horizon', horizon, 1)
    _nat('max_horizon', max_horizon, 1)
    _nat('max_work', max_work)
    _nat('max_trials', max_trials)
    _nat('seed', seed)
    if alphabet not in ('large', 'binary'):
        raise ValueError('alphabet must be large or binary')
    if H > max_horizon:
        return SparseCompilation('BUDGET_EXHAUSTED', None, None, 0, 0, 0)
    s = _support(sparse_ruler(H) if exponents is None else exponents, H)
    pairs = len(s)*(len(s)-1)//2
    visits = sum(H//r for r in range(1, H+1))
    work = pairs+visits
    if work > max_work:
        return SparseCompilation('BUDGET_EXHAUSTED', None, None, 0, 0, 0)
    alias = structural_alias(s, H)
    if alias is not None:
        return SparseCompilation('UNIDENTIFIABLE_SUPPORT', None, alias, 0, 0, 0)
    rng = Random(seed)
    upper = 2*(H+1)*H if alphabet == 'large' else 2
    profiles, spectra = [], []
    for trial in range(1, max_trials+1):
        if (trial+1)*work > max_work:
            return SparseCompilation('BUDGET_EXHAUSTED', None, None, trial-1,
                                     (trial-1)*pairs, (trial-1)*visits)
        weights = tuple(rng.randrange(1, upper+1) for _ in s)
        spectrum = collision_spectrum(s, weights, H)
        if alphabet == 'large':
            profiles, spectra = [weights], [spectrum]
        else:
            profiles.append(weights)
            spectra.append(spectrum)
        codes = tuple(zip(*spectra))
        lookup = {code: r for r, code in enumerate(codes, 1)}
        if len(lookup) == H+1:
            book = SparseCollisionCodebook(H, s, tuple(profiles), codes, MappingProxyType(lookup))
            return SparseCompilation('COMPLETE', book, None, trial, trial*pairs, trial*visits)
    return SparseCompilation('SEARCH_EXHAUSTED', None, None, max_trials,
                             max_trials*pairs, max_trials*visits)


@dataclass(frozen=True)
class LabeledCollisionGCD:
    gcd_multiple: int
    observed_atoms: int
    residue_buckets: int
    repeated_residues: int


def labeled_collision_gcd(n: int, a: int, exponents: Iterable[int],
                          horizon: int) -> LabeledCollisionGCD:
    """Keep one exponent per residue and a gcd. For arbitrary support, ONLY a multiple.

    gcd=0 means no collision on this support, not a global lower bound on order.
    Differences to the representative generate the same gcd as all within-bucket pairs.
    """
    _group(n, a)
    s = _support(exponents, horizon)
    representatives, multiple, repeats = {}, 0, 0
    for x in s:
        u = pow(a, x, n)
        if u in representatives:
            multiple = gcd(multiple, x-representatives[u])
            repeats += 1
        else:
            representatives[u] = x
    return LabeledCollisionGCD(multiple, len(s), len(representatives), repeats)


def ruler_order(n: int, a: int, horizon: int) -> SparsePeriodInference:
    """Exact bounded order from a COMPLETE ruler, no offline mass decoder.

    All collision differences are multiples of r; if r<=H a pair has difference r.
    Differences to one representative per residue have the same gcd as all pairs.
    Generate the low block and block multiples using O(sqrt(H)) modular products,
    plus one O(log H) exponentiation for a possible final endpoint. Sorting and
    gcd/integer bit costs remain. This is NOT a generic sub-BSGS result.
    """
    _group(n, a)
    H = _nat('horizon', horizon, 1)
    b = isqrt(H)
    b += b*b < H
    residues = {}
    u = 1
    for x in range(b):
        residues[x] = u
        u = u*a % n
    step = u
    for x in range(b, H+1, b):
        residues[x] = u
        u = u*step % n
    if H % b:
        residues[H] = pow(a, H, n)
    representatives, multiple = {}, 0
    for x, u in sorted(residues.items()):
        if u in representatives:
            multiple = gcd(multiple, x-representatives[u])
        else:
            representatives[u] = x
    if multiple == 0:
        return SparsePeriodInference('ORDER_ABOVE_HORIZON', None, H+1)
    return SparsePeriodInference('EXACT_FROM_RULER_COLLISIONS', multiple, multiple)
