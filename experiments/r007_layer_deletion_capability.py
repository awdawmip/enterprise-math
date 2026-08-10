"""Exact finite layer-deletion capability calculus for R007.

The visible state may forget scale-layer provenance, while future operations can
remove layers and then inspect a common scale (gcd).  This module implements the
resulting finite divisor-lattice objects:

* exact reachable gcd outputs R_h;
* their downward capability ideal C_h;
* the join envelope E_h;
* the supporter-gcd closure Gamma_S;
* provenance-fiber and one-shot gcd-repair counts over a uniform overlay.

The algorithms here are theorem oracles/regressions for small finite families.
Large closed-pattern enumeration should consume established FCA / frequent
closed-itemset machinery rather than treating this file as a new mining stack.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, lcm
from typing import Sequence


def _validate(scales: Sequence[int]) -> tuple[int, ...]:
    values = tuple(scales)
    if not values or any(d < 1 for d in values):
        raise ValueError("require a nonempty positive scale family")
    return values


def gcd_all(values: Sequence[int]) -> int:
    xs = _validate(values)
    out = 0
    for value in xs:
        out = gcd(out, value)
    return out


def lcm_all(values: Sequence[int]) -> int:
    xs = _validate(values)
    out = 1
    for value in xs:
        out = lcm(out, value)
    return out


def positive_divisors(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("n must be positive")
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def valuation(n: int, p: int) -> int:
    if n < 1 or p < 2:
        raise ValueError("require n>=1 and p>=2")
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def defect_indices(scales: Sequence[int], candidate: int) -> tuple[int, ...]:
    xs = _validate(scales)
    if candidate < 1:
        raise ValueError("candidate must be positive")
    return tuple(i for i, value in enumerate(xs) if value % candidate != 0)


def supporter_indices(scales: Sequence[int], candidate: int) -> tuple[int, ...]:
    xs = _validate(scales)
    if candidate < 1:
        raise ValueError("candidate must be positive")
    return tuple(i for i, value in enumerate(xs) if value % candidate == 0)


def supporter_gcd_closure(scales: Sequence[int], candidate: int) -> int | None:
    """Gamma_S(c): gcd of all layers divisible by c, or None if unsupported."""
    xs = _validate(scales)
    supporters = [xs[i] for i in supporter_indices(xs, candidate)]
    if not supporters:
        return None
    return gcd_all(supporters)


def capability_ideal(scales: Sequence[int], h: int) -> tuple[int, ...]:
    """All c that can divide a surviving gcd after at most h deletions.

    Exact criterion: c is feasible iff at most h layers fail divisibility by c.
    """
    xs = _validate(scales)
    if not (0 <= h < len(xs)):
        raise ValueError("require 0<=h<number of layers")
    ambient = lcm_all(xs)
    return tuple(
        c
        for c in positive_divisors(ambient)
        if len(defect_indices(xs, c)) <= h
    )


def exact_reachable_gcds_by_closure(scales: Sequence[int], h: int) -> tuple[int, ...]:
    """Exact reachable gcd outputs using Gamma fixed points plus support budget."""
    xs = _validate(scales)
    if not (0 <= h < len(xs)):
        raise ValueError("require 0<=h<number of layers")
    ambient = lcm_all(xs)
    out = []
    for c in positive_divisors(ambient):
        if len(defect_indices(xs, c)) > h:
            continue
        if supporter_gcd_closure(xs, c) == c:
            out.append(c)
    return tuple(out)


def exact_reachable_gcds_bruteforce(scales: Sequence[int], h: int) -> tuple[int, ...]:
    """Deletion-subset oracle used only to regression-check the closure theorem."""
    xs = _validate(scales)
    if not (0 <= h < len(xs)):
        raise ValueError("require 0<=h<number of layers")
    outputs: set[int] = set()
    indices = range(len(xs))
    for deleted_count in range(h + 1):
        for deleted in combinations(indices, deleted_count):
            deleted_set = set(deleted)
            survivors = [value for i, value in enumerate(xs) if i not in deleted_set]
            outputs.add(gcd_all(survivors))
    return tuple(sorted(outputs))


def deletion_envelope(scales: Sequence[int], h: int) -> int:
    """E_h: join/lcm of all exact gcd outputs reachable within deletion budget."""
    outputs = exact_reachable_gcds_by_closure(scales, h)
    return lcm_all(outputs)


def valuation_order_statistic(scales: Sequence[int], p: int, h: int) -> int:
    """The (h+1)-st smallest p-adic depth across labeled layers."""
    xs = _validate(scales)
    if not (0 <= h < len(xs)):
        raise ValueError("require 0<=h<number of layers")
    return sorted(valuation(value, p) for value in xs)[h]


def envelope_chain(scales: Sequence[int]) -> tuple[int, ...]:
    xs = _validate(scales)
    return tuple(deletion_envelope(xs, h) for h in range(len(xs)))


def capability_is_principal(scales: Sequence[int], h: int) -> bool:
    """Whether the capability ideal equals Div(E_h), i.e. envelope is jointly feasible."""
    xs = _validate(scales)
    envelope = deletion_envelope(xs, h)
    return len(defect_indices(xs, envelope)) <= h


def provenance_fiber_size(uniform_overlay_scale: int) -> int:
    """Number of hidden divisor-layer sets with unlabeled overlay exactly P_M."""
    divisors = positive_divisors(uniform_overlay_scale)
    return 1 << (len(divisors) - 1)


def _mobius(n: int) -> int:
    """Elementary integer Moebius function for the small provenance formula."""
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    x = n
    prime_count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            prime_count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def provenance_repair_class_count(uniform_overlay_scale: int, meet: int) -> int:
    """C_M(g): hidden P_M-layer families whose exact gcd repair value is g."""
    m = uniform_overlay_scale
    if m < 1 or meet < 1 or m % meet:
        raise ValueError("meet must divide the positive overlay scale")
    quotient = m // meet
    total = 0
    for h in positive_divisors(quotient):
        remaining = m // (meet * h)
        tau = len(positive_divisors(remaining))
        total += _mobius(h) * (1 << (tau - 1))
    return total


def provenance_repair_distribution(uniform_overlay_scale: int) -> dict[int, int]:
    return {
        g: provenance_repair_class_count(uniform_overlay_scale, g)
        for g in positive_divisors(uniform_overlay_scale)
    }
