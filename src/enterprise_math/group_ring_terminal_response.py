"""Exact fixed-terminal dyadic response via multiplicity-aware block moments.

The suffix with generators b,b^2,...,b^(2^(t-1)) equals
sum_{d=-(L-1)}^{L-1} (L-|d|)[b^d], L=2^t.  The weighted
matcher below also works for any positive integer L.  It needs no supplied
order or discrete logarithm and never builds the full response distribution.

This is a BRC/T4/T6 terminal-observer specialization of classical baby-step
 giant-step, not a new order-finding complexity bound or a stepwise quotient.
Count AND first offset moment are required when baby residues repeat.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import gcd, isqrt
from typing import Iterable


def _nat(name: str, x: int, minimum: int = 0) -> int:
    if type(x) is not int or x < minimum:
        raise ValueError(f'{name} must be an integer >= {minimum}')
    return x


@dataclass(frozen=True)
class TerminalResponse:
    status: str
    values: tuple[int, ...] | None
    baby_width: int
    blocks_per_target: int
    table_entries: int
    required_scan_steps: int
    executed_scan_steps: int


def terminal_responses(n: int, b: int, length: int, states: Iterable[int] = (1,),
                       *, baby_width: int | None = None,
                       max_baby_steps: int = 100_000,
                       max_scan_steps: int = 1_000_000) -> TerminalResponse:
    """Return h(u)=[1]([u] sum_d (L-|d|)[b^d]) for each given state.

    Fixed window only: a zero is an exact zero for THIS terminal program, not
    absence of later collisions. Nonunit states have response zero. Budget
    refusal returns values=None, never a partial/empty result. Scan budgets
    count baby iterations + giant-block/target visits, not wall time or bytes.
    Tables hold (count,sum_offsets) for full blocks and the final partial block.
    Inputs must be canonical residues; repetitions in states are permitted.
    """
    _nat('n', n, 3); _nat('b', b, 1); _nat('length', length, 1)
    _nat('max_baby_steps', max_baby_steps, 1)
    _nat('max_scan_steps', max_scan_steps, 0)
    if b >= n or gcd(b, n) != 1:
        raise ValueError('b must be a canonical unit modulo n')
    states = tuple(states)
    if any(type(u) is not int or not 0 <= u < n for u in states):
        raise ValueError('states must be canonical integer residues modulo n')
    if baby_width is not None:
        _nat('baby_width', baby_width, 1)
        if baby_width > length:
            raise ValueError('baby_width cannot exceed length')
    # These exact degenerate cases need neither a table nor a subgroup oracle.
    if not states or b == 1 or length == 1:
        values = tuple(length*length if u == 1 else 0 for u in states)
        return TerminalResponse('COMPLETE', values, 0, 0, 0, 0, 0)
    inverses = {u: pow(u, -1, n) for u in set(states) if gcd(u, n) == 1}
    targets = tuple(sorted(set(inverses) | set(inverses.values())))
    if not targets:
        return TerminalResponse('COMPLETE', (0,)*len(states), 0, 0, 0, 0, 0)
    # Balance actual number of distinct signed targets against table work.
    width = min(length, isqrt(len(targets)*length-1)+1, max_baby_steps)
    if baby_width is not None:
        width = baby_width
    full, tail = divmod(length, width)
    blocks = full + int(tail != 0)
    required = width + blocks*len(targets)
    if width > max_baby_steps or required > max_scan_steps:
        return TerminalResponse('BUDGET_EXHAUSTED', None, width, blocks, 0, required, 0)
    table: dict[int, tuple[int, int]] = {}
    partial: dict[int, tuple[int, int]] = {}
    power = 1
    for j in range(width):
        c, s = table.get(power, (0, 0)); table[power] = (c+1, s+j)
        if j < tail:
            c, s = partial.get(power, (0, 0)); partial[power] = (c+1, s+j)
        power = power*b % n
    giant_inverse = pow(power, -1, n)  # power == b**width (mod n)
    sums = {}
    for target in targets:
        v, total = target, 0
        for i in range(full):
            c, s = table.get(v, (0, 0))
            total += (length-i*width)*c-s
            v = v*giant_inverse % n
        if tail:
            c, s = partial.get(v, (0, 0)); total += tail*c-s
        sums[target] = total
    values = tuple(sums[u]+sums[inverses[u]]-length*int(u == 1)
                   if u in inverses else 0 for u in states)
    if any(v < 0 or v > length*length for v in values):
        raise ArithmeticError('terminal mass outside the exact positive envelope')
    return TerminalResponse('COMPLETE', values, width, blocks,
                            len(table)+len(partial), required, required)


def suffix_responses(n: int, a: int, total_bits: int, cut: int,
                     states: Iterable[int] = (1,), **limits) -> TerminalResponse:
    """Fixed dyadic suffix beginning at cut; no supplied order or log.

    Prefix histogram construction and later summation are caller costs.
    The 1,000,000-bit admission cap bounds exponent/window allocation, not
    mathematical validity. Even admitted large windows may exceed scan budgets.
    """
    _nat('n', n, 3); _nat('a', a, 1)
    _nat('total_bits', total_bits); _nat('cut', cut)
    if a >= n or gcd(a, n) != 1 or cut > total_bits:
        raise ValueError('canonical unit and 0 <= cut <= total_bits required')
    if total_bits > 1_000_000:
        raise ValueError('bit allocation cap exceeded')
    b = pow(a, 1 << cut, n)
    return terminal_responses(n, b, 1 << (total_bits-cut), states, **limits)


def cyclic_terminal_value(order: int, length: int, exponent: int) -> int:
    """Conditional closed form; order/log supplied HERE, never to online matcher.

    Caller must establish exact order and membership/exponent before using this
    formula for modular residues. It is not an order-certificate validator.
    """
    _nat('order', order, 1); _nat('length', length, 1)
    if type(exponent) is not int:
        raise ValueError('exponent must be an integer')
    q, t = divmod(length, order); k = exponent % order
    return order*q*q+2*q*t+max(0, t-k)+max(0, t-order+k)


def terminal_class_count(order: int, length: int) -> int:
    """Number of distinct terminal responses on the cyclic subgroup, not ambient G."""
    _nat('order', order, 1); _nat('length', length, 1)
    t = length % order
    return min(t, order-t)+1


def invert_collision_mass(length: int, mass: int) -> int | None:
    """Invert an EXACT identity collision mass of a uniform exponent interval.

    K_L(r)=L+2*sum_{j>=1} max(L-j*r,0) strictly decreases for 1<=r<L.
    K==L means only r>=L. K>L uniquely specifies r<L. This arithmetic helper
    does not authenticate externally supplied mass as a group computation.
    """
    _nat('length', length, 1); _nat('mass', mass)
    if not length <= mass <= length*length:
        raise ValueError('mass outside collision envelope')
    if mass == length:
        return None
    low, high = 1, length-1
    while low < high:
        mid = (low+high)//2
        if cyclic_terminal_value(mid, length, 0) > mass:
            low = mid+1
        else:
            high = mid
    if cyclic_terminal_value(low, length, 0) != mass:
        raise ValueError('mass not realizable by a uniform cyclic interval')
    return low


@dataclass(frozen=True)
class CollisionOrderResult:
    status: str
    order: int | None
    order_lower_bound: int
    scans: int
    # Exact completed queries: (window, mass, baby_width, table_entries, scans).
    history: tuple[tuple[int, int, int, int, int], ...]


def collision_order_search(n: int, a: int, *, max_bits: int | None = None,
                           max_baby_steps: int = 100_000,
                           max_scan_steps: int = 1_000_000) -> CollisionOrderResult:
    """Adaptive first-collision mass inversion; classical sqrt-order complexity.

    This specialization computes interval masses by block matching, NOT by
    forwarding just the current K. Every new interval is computed from its
    explicit program. No order oracle and no factorization of n or its totient.
    Budgets are cumulative scans as defined by terminal_responses, not bit cost.
    """
    _nat('n', n, 3); _nat('a', a, 1)
    _nat('max_baby_steps', max_baby_steps, 1)
    _nat('max_scan_steps', max_scan_steps)
    if a >= n or gcd(a, n) != 1:
        raise ValueError('a must be a canonical unit')
    bits = n.bit_length() if max_bits is None else _nat('max_bits', max_bits)
    if bits > 1_000_000:
        raise ValueError('bit allocation cap exceeded')
    history = []; scans = 0; lower = 1
    for m in range(bits+1):
        length = 1 << m
        res = terminal_responses(n, a, length, max_baby_steps=max_baby_steps,
                                 max_scan_steps=max_scan_steps-scans)
        if res.status != 'COMPLETE':
            return CollisionOrderResult('BUDGET_EXHAUSTED', None, lower, scans, tuple(history))
        mass = res.values[0]
        scans += res.executed_scan_steps
        history.append((length, mass, res.baby_width, res.table_entries,
                        res.executed_scan_steps))
        order = invert_collision_mass(length, mass)
        if order is not None:
            if pow(a, order, n) != 1:
                raise ArithmeticError('exact inferred order failed roundtrip')
            return CollisionOrderResult('COMPLETE', order, order, scans, tuple(history))
        lower = length
    return CollisionOrderResult('WINDOW_LIMIT', None, lower, scans, tuple(history))
