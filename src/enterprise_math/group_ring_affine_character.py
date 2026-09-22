"""Candidate nonuniform collision readout and certified Jacobi progression sieve.

Weights are w_x = intercept + slope*x on the FULL interval 0<=x<length,
intercept>0, slope>=0. These are nonnegative integer multiplicities, NOT
amplitudes or probabilities. Their autocorrelation is an exactly scaled cubic.

The existing bounded terminal index is executed unchanged; this module extends
its declared observer, not its generic BSGS algorithm. The Jacobi character can
certify a parity constraint without factoring n. It cannot certify arbitrary
residue-based pruning. Even moduli take the unchanged unfiltered path.

The Jacobi function below is ported verbatim (function text) from POWER
6d784d3990afae602a03745173c3f2a16a076b0c:src/power/modular/arithmetic.py,
source blob b17dd3a61e83677f571649790ebe3ace3699d773. No other POWER arithmetic
or primality routine is admitted by this port. Full comparison module blob:
82c87f779a07b84de601d54ebd04d3bfb1856f92 (group_ring_batch_response.py).
"""
from __future__ import annotations
from dataclasses import dataclass
from math import gcd
from types import MappingProxyType
from typing import Iterable

from .group_ring_batch_response import BoundedTerminalIndex, compile_terminal_index


def jacobi_symbol(a: int, n: int) -> int:
    """Computes the Jacobi symbol (a / n) for positive odd integer n."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0


def _nat(name, value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f'{name} must be an integer >= {minimum}')
    return value


def _weights(length, intercept, slope):
    _nat('length', length, 1)
    _nat('intercept', intercept, 1)
    _nat('slope', slope)


def affine_correlation_coefficients(length: int, intercept: int = 1,
                                    slope: int = 0) -> tuple[int, int, int]:
    """Return (c0,c1,c3) with 6*A(d)=c0+c1*d+c3*d^3 for 0<=d<=L.

    A(d) = sum(x=0..L-1-d) w_x*w_(x+d). Outside 0<=d<L the
    autocorrelation is zero; the cubic must not be extrapolated there.
    Signed coefficients here are algebraic readouts, never BRC branch masses.
    """
    _weights(length, intercept, slope)
    L, a, b = length, intercept, slope
    c0 = 6*a*a*L + 6*a*b*L*(L-1) + b*b*L*(L-1)*(2*L-1)
    c1 = -6*a*a - 6*a*b*(L-1) - b*b*(3*L*L-3*L+1)
    return c0, c1, b*b


def affine_correlation(length: int, difference: int, intercept: int = 1,
                       slope: int = 0) -> int:
    c0, c1, c3 = affine_correlation_coefficients(length, intercept, slope)
    if type(difference) is not int:
        raise ValueError('difference must be an integer')
    d = abs(difference)
    if d >= length:
        return 0
    numerator = c0+c1*d+c3*d*d*d
    if numerator < 0 or numerator % 6:
        raise ArithmeticError('invalid exact autocorrelation')
    return numerator//6


def _progression_sum(coeff, length, first, period):
    if first is None or first >= length:
        return 0
    count = 1 if period is None else (length-1-first)//period+1
    r = 0 if period is None else period
    s1 = count*(count-1)//2
    s2 = count*(count-1)*(2*count-1)//6
    s3 = s1*s1
    p1 = count*first+r*s1
    p3 = count*first**3+3*first*first*r*s1+3*first*r*r*s2+r**3*s3
    out = coeff[0]*count+coeff[1]*p1+coeff[2]*p3
    if out < 0 or out % 6:
        raise ArithmeticError('invalid progression autocorrelation sum')
    return out//6


def affine_collision_from_order(length: int, order: int, intercept: int = 1,
                                slope: int = 0) -> int:
    """Conditional arithmetic model; does NOT authenticate a supplied order."""
    coeff = affine_correlation_coefficients(length, intercept, slope)
    _nat('order', order, 1)
    return coeff[0]//6+2*_progression_sum(coeff, length, order, order)


@dataclass(frozen=True)
class AffineOrderInference:
    status: str
    order: int | None
    lower_bound: int


def invert_affine_collision(mass: int, length: int, intercept: int = 1,
                            slope: int = 0) -> AffineOrderInference:
    """Invert an exact affine-weight collision mass, conditional on its origin.

    A supplied scalar is not an authenticated group computation. Inconsistent
    masses raise. The no-collision baseline gives only r>=length, never equality.
    Monotone positive weights prove strict injectivity below that horizon.
    """
    _weights(length, intercept, slope)
    _nat('mass', mass)
    diagonal = affine_correlation(length, 0, intercept, slope)
    if mass == diagonal:
        return AffineOrderInference('NO_COLLISION_WITHIN_WINDOW', None, length)
    if mass < diagonal or length == 1:
        raise ValueError('mass is inconsistent with the declared weight profile')
    low, high = 1, length-1
    while low <= high:
        mid = (low+high)//2
        actual = affine_collision_from_order(length, mid, intercept, slope)
        if actual == mass:
            return AffineOrderInference('EXACT_CONDITIONAL_ON_MASS', mid, mid)
        if actual > mass:
            low = mid+1
        else:
            high = mid-1
    raise ValueError('mass is inconsistent with any order for this profile')


def affine_index_responses(index: BoundedTerminalIndex, length: int,
                           states: Iterable[int], intercept: int = 1,
                           slope: int = 0) -> tuple[int, ...]:
    """Exact affine-weight autocorrelation from a locally compiled index.

    Uses the pinned index's internal first-hit/period evidence explicitly.
    Inputs are trusted local typed data, not externally signed certificates.
    It neither regenerates exponent histograms nor loops over the window.
    """
    if not isinstance(index, BoundedTerminalIndex):
        raise TypeError('a compiled BoundedTerminalIndex is required')
    coeff = affine_correlation_coefficients(length, intercept, slope)
    states = tuple(states)
    if length > index.span or any(type(u) is not int or u not in index._domain for u in states):
        raise ValueError('query outside compiled horizon/state domain')
    out = []
    for u in states:
        if u not in index._inverses:
            out.append(0)
            continue
        positive = _progression_sum(coeff, length, index._logs.get(u), index.order)
        negative = _progression_sum(coeff, length, index._logs.get(index._inverses[u]), index.order)
        out.append(positive+negative-(coeff[0]//6)*int(u == 1))
    return tuple(out)


@dataclass(frozen=True)
class CharacterCompilation:
    status: str
    index: BoundedTerminalIndex | None
    mode: str
    input_span: int
    search_span: int
    rejected_states: tuple[int, ...]
    character_evaluations: int
    baby_width: int
    table_entries: int
    required_scans: int
    executed_scans: int


def compile_character_index(n: int, a: int, span: int, states: Iterable[int], *,
                            use_character: bool = True,
                            max_baby_steps: int = 100_000,
                            max_scan_steps: int = 1_000_000) -> CharacterCompilation:
    """Use an exact Jacobi character before the UNCHANGED bounded compiler.

    If chi(a)=-1, a^d=t requires d=epsilon(t) mod2. Compile with base a^2
    and target t*a^(-epsilon). Negative exponents are handled by registering
    both signed targets; extra transformed inverses are counted by the inherited
    compiler, not silently free. A witnessed order s of a^2 certifies r=2*s.

    If chi(a)=1, chi(t)=-1 proves whole-subgroup nonmembership. Retain identity
    in the compiled domain when unit targets exist so the order bound is real.
    Equal positive characters are NECESSARY, not sufficient, for membership.

    This is at most a constant-factor pruning mechanism, not an RSA or
    sub-BSGS speedup. Chi(a^2)=1, so repeatedly squaring cannot repeat the parity
    information gain. Even n uses the unfiltered backend. No factoring oracle.
    """
    _nat('n', n, 3); _nat('a', a, 1); _nat('span', span, 1)
    _nat('max_baby_steps', max_baby_steps, 1); _nat('max_scan_steps', max_scan_steps)
    if type(use_character) is not bool:
        raise ValueError('use_character must be bool')
    if a >= n or gcd(a,n) != 1:
        raise ValueError('base must be a canonical unit')
    states = tuple(states)
    if any(type(u) is not int or not 0 <= u < n for u in states):
        raise ValueError('states must be canonical integer residues')
    domain = frozenset(states)
    inverses = {u:pow(u,-1,n) for u in domain if gcd(u,n) == 1}
    limits = dict(max_baby_steps=max_baby_steps, max_scan_steps=max_scan_steps)
    mode, reduced_span, calls, rejected = 'DISABLED', span, 0, ()
    if not use_character or n%2 == 0 or not inverses:
        if use_character:
            mode = 'EVEN_MODULUS' if n%2 == 0 else 'NO_UNIT_TARGETS'
        compiled = compile_terminal_index(n,a,span,states,**limits)
        return CharacterCompilation(compiled.status,compiled.index,mode,span,span,(),0,
                                    compiled.baby_width,compiled.table_entries,
                                    compiled.required_scans,compiled.executed_scans)
    chi_a = jacobi_symbol(a,n)
    signs = {u:jacobi_symbol(u,n) for u in inverses}
    calls = 1+len(signs)
    if chi_a == 1:
        mode = 'CHARACTER_ZERO_EXCLUSION'
        rejected = tuple(sorted(u for u in signs if signs[u] == -1))
        registered = tuple(sorted({1} | {u for u in signs if signs[u] == 1}))
        compiled = compile_terminal_index(n,a,span,registered,**limits)
        if compiled.index is not None:
            idx = compiled.index
            result = BoundedTerminalIndex(n,a,span,idx.order,idx._logs,
                                          MappingProxyType(inverses),domain)
        else:
            result = None
    else:
        mode = 'PARITY_PROGRESSION'
        reduced_span = (span+1)//2
        inv_a = pow(a,-1,n)
        signed = set(inverses) | set(inverses.values()) | {1}
        # Inverse characters agree, so no second Jacobi evaluation is needed.
        epsilon = {1:0}
        for u in inverses:
            epsilon[u] = epsilon[inverses[u]] = int(signs[u] == -1)
        transformed = {u:(u*inv_a % n if epsilon[u] else u) for u in signed}
        compiled = compile_terminal_index(n,a*a % n,reduced_span,
                                          tuple(sorted(set(transformed.values()))),**limits)
        if compiled.index is not None:
            inner = compiled.index
            logs = {}
            for u,t in transformed.items():
                k = inner._logs.get(t)
                if k is not None and (e := epsilon[u]+2*k) < span:
                    logs[u] = e
            order = None if inner.order is None else 2*inner.order
            if order is not None:
                # A period learned through a^2 may exceed the original span by
                # one. Complete inverse logs from that actual period, including
                # canonical exponents outside the searched positive window.
                # The inherited cuts API needs this evidence for both signs.
                for u in signed:
                    inverse = pow(u,-1,n)
                    if u not in logs and inverse in logs:
                        logs[u] = (-logs[inverse]) % order
            result = BoundedTerminalIndex(n,a,span,order,MappingProxyType(logs),
                                          MappingProxyType(inverses),domain)
        else:
            result = None
    return CharacterCompilation(compiled.status,result,mode,span,reduced_span,rejected,calls,
                                compiled.baby_width,compiled.table_entries,
                                compiled.required_scans,compiled.executed_scans)
