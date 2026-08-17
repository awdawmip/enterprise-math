"""Exact divisor-action calculus for the R007 multiscale component quotient.

This module is executable evidence for theorem targets, not a Lean proof.

Once a finite multiscale overlap family has component quotient ``R_G``, adding
another scale ``u`` updates the quotient by the fixed-mask action

    x |-> gcd(x, u).

On the divisor state lattice ``D(G)`` these actions compose by gcd, while the
collective state-separation power of a declared future probe family is governed
by the lcm of its normalized masks.  The functions below keep those two
semantics separate:

* execution closure: gcd / meet;
* observational envelope: lcm / join.

All arithmetic is exact integer arithmetic.
"""

from __future__ import annotations

from collections import Counter
from math import gcd, lcm
from typing import Iterable, Sequence


def factor_exponents(n: int) -> dict[int, int]:
    """Prime factorization ``p -> v_p(n)`` for positive integers."""
    if n < 1:
        raise ValueError("n must be positive")
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def p_adic_valuation(n: int, p: int) -> int:
    if n < 1 or p < 2:
        raise ValueError("require n>=1 and p>=2")
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def positive_divisors(n: int) -> tuple[int, ...]:
    """All positive divisors of ``n`` in increasing order."""
    factors = factor_exponents(n)
    values = [1]
    for p, exponent in factors.items():
        values = [
            value * p**power
            for value in values
            for power in range(exponent + 1)
        ]
    return tuple(sorted(values))


def divisor_count(n: int) -> int:
    """tau(n)."""
    result = 1
    for exponent in factor_exponents(n).values():
        result *= exponent + 1
    return result


def big_omega(n: int) -> int:
    """Omega(n): prime factors counted with multiplicity."""
    return sum(factor_exponents(n).values())


def little_omega(n: int) -> int:
    """omega(n): number of distinct prime factors."""
    return len(factor_exponents(n))


def normalized_probe_mask(G: int, u: int) -> int:
    """The action ``gcd(x,u)`` on ``x|G`` depends only on ``gcd(G,u)``."""
    if G < 1 or u < 1:
        raise ValueError("G and u must be positive")
    return gcd(G, u)


def future_probe_envelope(G: int, probes: Iterable[int]) -> int:
    """Least divisor ``C|G`` carrying the full one-step separation power.

    ``C = lcm(gcd(G,u) for u in probes)``.  For the empty language ``C=1``.
    """
    if G < 1:
        raise ValueError("G must be positive")
    C = 1
    for u in probes:
        C = lcm(C, normalized_probe_mask(G, u))
    return C


def future_signature(x: int, G: int, probes: Sequence[int]) -> tuple[int, ...]:
    """Exact one-step outputs of the declared probe family."""
    if x < 1 or G % x != 0:
        raise ValueError("state x must divide G")
    return tuple(gcd(x, u) for u in probes)


def future_projection(x: int, G: int, probes: Sequence[int]) -> int:
    """Canonical coarsest future-sufficient principal state ``gcd(x,C)``."""
    if x < 1 or G % x != 0:
        raise ValueError("state x must divide G")
    return gcd(x, future_probe_envelope(G, probes))


def fixed_mask_action_basis(G: int) -> tuple[int, ...]:
    """Unique least meet-generating basis for all fixed-mask actions on ``D(G)``.

    The basis consists of all meet-irreducibles

        G / p^j,  1 <= j <= v_p(G).

    Its cardinality is exactly ``Omega(G)``.
    """
    if G < 1:
        raise ValueError("G must be positive")
    return tuple(
        sorted(
            G // p**j
            for p, exponent in factor_exponents(G).items()
            for j in range(1, exponent + 1)
        )
    )


def compile_fixed_mask_action(G: int, target: int) -> tuple[int, ...]:
    """Shortest program for ``x |-> gcd(x,target)`` in the canonical basis."""
    if target < 1 or G % target != 0:
        raise ValueError("target must be a positive divisor of G")
    program: list[int] = []
    for p, top_exp in factor_exponents(G).items():
        target_exp = p_adic_valuation(target, p)
        if target_exp < top_exp:
            program.append(G // p ** (top_exp - target_exp))
    return tuple(program)


def action_depth(G: int, target: int) -> int:
    """Shortest canonical-basis depth, equal to ``omega(G/target)``."""
    return len(compile_fixed_mask_action(G, target))


def action_depth_spectrum(G: int) -> dict[int, int]:
    """Number of target actions at each shortest canonical-basis depth."""
    counts = Counter(action_depth(G, target) for target in positive_divisors(G))
    return dict(sorted(counts.items()))


def action_depth_spectrum_formula(G: int) -> tuple[int, ...]:
    """Coefficients of ``prod_p (1 + v_p(G) z)``.

    Coefficient k is the number of divisor actions requiring exactly k basis
    instructions.
    """
    coeff = [1]
    for exponent in factor_exponents(G).values():
        nxt = [0] * (len(coeff) + 1)
        for k, value in enumerate(coeff):
            nxt[k] += value
            nxt[k + 1] += exponent * value
        coeff = nxt
    return tuple(coeff)


def refinement_split_count(G: int, coarse: int, fine: int, observed: int) -> int:
    """How many ``fine`` classes split one ``coarse`` future class.

    Require ``observed | coarse | fine | G``.  A prime coordinate splits only
    when the coarse observation is saturated at the old ceiling.
    """
    if not (
        0 < observed
        and coarse % observed == 0
        and fine % coarse == 0
        and G % fine == 0
    ):
        raise ValueError("require observed | coarse | fine | G")
    result = 1
    for p in factor_exponents(G):
        beta = p_adic_valuation(coarse, p)
        gamma = p_adic_valuation(fine, p)
        seen = p_adic_valuation(observed, p)
        if seen == beta:
            result *= gamma - beta + 1
    return result


def _gcd_all(values: Sequence[int]) -> int:
    if not values:
        raise ValueError("values must be nonempty")
    result = values[0]
    for value in values[1:]:
        result = gcd(result, value)
    return result


def _lcm_all(values: Sequence[int]) -> int:
    if not values:
        raise ValueError("values must be nonempty")
    result = 1
    for value in values:
        result = lcm(result, value)
    return result


def extremal_witness_cover(
    values: Sequence[int], *, mode: str
) -> tuple[frozenset[int], tuple[frozenset[int], ...]]:
    """Set-cover encoding for preserving the full gcd or lcm of ``values``.

    Only prime coordinates whose exponent varies matter.  In ``gcd`` mode an
    item witnesses coordinates where it attains the global minimum exponent;
    in ``lcm`` mode it witnesses coordinates where it attains the maximum.
    A nonempty subfamily preserves the requested extremum iff its witness sets
    cover the returned universe.
    """
    if not values or any(value < 1 for value in values):
        raise ValueError("values must be nonempty positive integers")
    if mode not in {"gcd", "lcm"}:
        raise ValueError("mode must be 'gcd' or 'lcm'")

    lower = _gcd_all(values)
    upper = _lcm_all(values)
    primes = factor_exponents(upper)
    varying = frozenset(
        p
        for p in primes
        if p_adic_valuation(lower, p) < p_adic_valuation(upper, p)
    )
    extreme = {
        p: p_adic_valuation(lower if mode == "gcd" else upper, p)
        for p in varying
    }
    witnesses = tuple(
        frozenset(
            p for p in varying if p_adic_valuation(value, p) == extreme[p]
        )
        for value in values
    )
    return varying, witnesses


def witness_cover_preserves(
    values: Sequence[int], indices: Sequence[int], *, mode: str
) -> bool:
    """Check the witness-cover criterion for one nonempty chosen subfamily."""
    if not indices:
        raise ValueError("chosen subfamily must be nonempty")
    universe, witnesses = extremal_witness_cover(values, mode=mode)
    covered: set[int] = set()
    for index in indices:
        covered.update(witnesses[index])
    return covered == set(universe)


def full_action_table_size(G: int) -> int:
    """Nonidentity fixed-mask action table size."""
    return divisor_count(G) - 1


def balanced_squarefree_compiler_storage(prime_count: int, max_depth: int) -> int:
    """Balanced bounded-union construction for squarefree ``G``.

    Partition the prime directions as evenly as possible into ``max_depth``
    blocks and precompile every nonempty mask supported inside each block.
    Any target action then uses at most one instruction per block.
    """
    if prime_count < 0 or max_depth < 1:
        raise ValueError("invalid prime_count / max_depth")
    if prime_count == 0:
        return 0
    blocks = min(prime_count, max_depth)
    q, r = divmod(prime_count, blocks)
    return r * (2 ** (q + 1) - 1) + (blocks - r) * (2**q - 1)
