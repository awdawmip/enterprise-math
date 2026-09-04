#!/usr/bin/env python3
"""Finite checks for the V16 one/two-history parity block coupling.

The coupling and second-iterate identities are checked exactly with
``fractions.Fraction``.  The prime-power logarithmic laws are displayed only
as numerical diagnostics and are not promoted to theorem status by this
script.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import exp, log
from typing import Callable, Dict, Hashable, Iterable, Mapping, Sequence, TypeVar


X = TypeVar("X", bound=Hashable)


def expectation(probability: Mapping[X, Fraction], value: Mapping[X, Fraction]) -> Fraction:
    return sum((probability[x] * value[x] for x in probability), Fraction(0))


def variance(probability: Mapping[X, Fraction], value: Mapping[X, Fraction]) -> Fraction:
    mean = expectation(probability, value)
    return sum(
        (probability[x] * (value[x] - mean) ** 2 for x in probability),
        Fraction(0),
    )


def normalize(weight: Mapping[X, Fraction]) -> Dict[X, Fraction]:
    total = sum(weight.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive mass required")
    return {x: w / total for x, w in weight.items() if w}


def matvec(
    kernel: Mapping[X, Mapping[X, Fraction]],
    value: Mapping[X, Fraction],
) -> Dict[X, Fraction]:
    return {
        x: sum((p * value[y] for y, p in row.items()), Fraction(0))
        for x, row in kernel.items()
    }


def check_second_iterate_identity() -> None:
    states = (0, 1, 2, 3)
    kernel: Dict[int, Dict[int, Fraction]] = {
        0: {0: Fraction(1)},
        1: {0: Fraction(1, 3), 1: Fraction(2, 3)},
        2: {0: Fraction(1, 5), 1: Fraction(2, 5), 2: Fraction(2, 5)},
        3: {0: Fraction(1, 7), 1: Fraction(2, 7), 2: Fraction(1, 7), 3: Fraction(3, 7)},
    }
    r = {x: Fraction((7 * x * x + 3 * x - 5) % 19 - 9, 11) for x in states}
    pr = matvec(kernel, r)
    e = {x: r[x] + pr[x] for x in states}
    p2r = matvec(kernel, pr)
    pe = matvec(kernel, e)
    for x in states:
        assert 2 * r[x] == p2r[x] - pr[x] + 2 * e[x] - pe[x]


def block_coupling_energy(
    mu: Mapping[X, Fraction],
    nu: Mapping[X, Fraction],
    value: Mapping[X, Fraction],
    block: Callable[[X], int],
) -> tuple[Fraction, Fraction]:
    """Return block overlap L and the pooled matched variance V."""
    mu_blocks: Dict[int, Dict[X, Fraction]] = defaultdict(dict)
    nu_blocks: Dict[int, Dict[X, Fraction]] = defaultdict(dict)
    for x, p in mu.items():
        mu_blocks[block(x)][x] = p
    for x, p in nu.items():
        nu_blocks[block(x)][x] = p

    overlap = Fraction(0)
    pooled_variance = Fraction(0)
    for key in set(mu_blocks) | set(nu_blocks):
        mu_part = mu_blocks.get(key, {})
        nu_part = nu_blocks.get(key, {})
        mu_mass = sum(mu_part.values(), Fraction(0))
        nu_mass = sum(nu_part.values(), Fraction(0))
        lam = min(mu_mass, nu_mass)
        if lam == 0:
            continue
        overlap += lam

        # Matched submeasures have common mass lam.  Their equally weighted
        # mixture, divided by 2*lam, is the pooled probability pi_j.
        pooled: Dict[X, Fraction] = defaultdict(Fraction)
        for x, p in mu_part.items():
            pooled[x] += (lam / mu_mass) * p / (2 * lam)
        for x, p in nu_part.items():
            pooled[x] += (lam / nu_mass) * p / (2 * lam)
        assert sum(pooled.values(), Fraction(0)) == 1
        pooled_variance += lam * variance(pooled, value)

    return overlap, pooled_variance


def check_exact_block_coupling() -> None:
    points = tuple(range(9))
    mu = normalize({x: Fraction((3 * x + 2) % 11 + 1, 13) for x in points})
    nu = normalize({x: Fraction((5 * x * x + 1) % 17 + 1, 19) for x in points})
    value = {x: Fraction((7 * x * x - 2 * x + 4) % 23 - 11, 9) for x in points}
    block = lambda x: x // 3

    overlap, block_variance = block_coupling_energy(mu, nu, value, block)
    difference = abs(expectation(nu, value) - expectation(mu, value))
    sup_norm = max(abs(v) for v in value.values())

    # The exact square-root-free form of
    #   difference/2 <= (1-L) sup + sqrt(L V).
    remainder = max(Fraction(0), difference / 2 - (1 - overlap) * sup_norm)
    assert remainder**2 <= overlap * block_variance
    assert 0 <= overlap <= 1
    assert block_variance >= 0

    # Verify the between-component mean bound in every nonempty block.
    for key in range(3):
        mu_part = {x: p for x, p in mu.items() if block(x) == key}
        nu_part = {x: p for x, p in nu.items() if block(x) == key}
        mu_mass = sum(mu_part.values(), Fraction(0))
        nu_mass = sum(nu_part.values(), Fraction(0))
        lam = min(mu_mass, nu_mass)
        if lam == 0:
            continue
        mu_prob = normalize(mu_part)
        nu_prob = normalize(nu_part)
        mean_difference = expectation(mu_prob, value) - expectation(nu_prob, value)
        pooled: Dict[int, Fraction] = defaultdict(Fraction)
        for x, p in mu_prob.items():
            pooled[x] += p / 2
        for x, p in nu_prob.items():
            pooled[x] += p / 2
        assert mean_difference**2 <= 4 * variance(pooled, value)


def ideal_block_overlap(blocks: int) -> float:
    if blocks < 2:
        raise ValueError("at least two blocks required")

    def primitive(z: float) -> float:
        return 0.0 if z == 0.0 else z * (1.0 - log(z))

    total = 0.0
    for j in range(blocks):
        lo = j / blocks
        hi = (j + 1) / blocks
        one = hi - lo
        two = primitive(hi) - primitive(lo)
        total += min(one, two)
    return total


def check_ideal_overlap() -> None:
    target = 1.0 - exp(-1.0)
    for blocks in (4, 8, 16, 32, 64, 128):
        overlap = ideal_block_overlap(blocks)
        assert abs(overlap - target) <= 1.0 / blocks + 1e-14
    q_star = exp(-1.0) + (1.0 / 3.0) * (1.0 - exp(-1.0)) ** 0.5
    assert q_star < 0.634


def prime_power_weights(limit: int) -> tuple[list[int], Dict[int, float]]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    p = 2
    while p * p <= limit:
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
        p += 1

    weights: Dict[int, float] = {}
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        power = p
        lp = log(p)
        while power <= limit:
            weights[power] = lp / power
            if power > limit // p:
                break
            power *= p
    return sorted(weights), weights


def logarithmic_block_diagnostic(n: int, blocks: int) -> tuple[float, float]:
    actions, weights = prime_power_weights(n)
    prefix = [0.0]
    for q in actions:
        prefix.append(prefix[-1] + weights[q])
    total = prefix[-1]

    def available(cutoff: int) -> list[int]:
        # Inputs are small enough that this transparent implementation is
        # preferable to importing a numerical dependency.
        return [q for q in actions if q <= cutoff]

    one = [0.0] * blocks
    two = [0.0] * blocks
    logn = log(n)

    def bin_of(state: int) -> int:
        if state <= 1:
            return 0
        index = int((log(state) / logn) * blocks)
        return min(blocks - 1, max(0, index))

    for q in actions:
        pq = weights[q] / total
        child = n // q
        one[bin_of(child)] += pq
        child_actions = available(child)
        child_mass = sum(weights[s] for s in child_actions)
        if not child_actions or child_mass == 0.0:
            two[0] += pq
            continue
        for s in child_actions:
            two[bin_of(child // s)] += pq * weights[s] / child_mass

    assert abs(sum(one) - 1.0) < 1e-10
    assert abs(sum(two) - 1.0) < 1e-10
    overlap = sum(min(x, y) for x, y in zip(one, two))
    return overlap, ideal_block_overlap(blocks)


def main() -> None:
    check_second_iterate_identity()
    check_exact_block_coupling()
    check_ideal_overlap()
    print("exact parity/block coupling checks: passed")
    print("N       discrete overlap   ideal block overlap   continuum target")
    target = 1.0 - exp(-1.0)
    for n in (500, 1_000, 2_000, 5_000):
        discrete, ideal = logarithmic_block_diagnostic(n, 16)
        print(f"{n:<7d} {discrete:<18.10f} {ideal:<21.10f} {target:.10f}")


if __name__ == "__main__":
    main()
