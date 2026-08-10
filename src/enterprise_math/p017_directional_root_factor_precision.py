"""Directional precision geometry between P017 least-prime shells and cofactor roots.

For a square-basin composite state n=p*q with p=spf(n), compare two retained
coordinates:

* P: the least-prime shell label p;
* R: the integer square-root index isqrt(q) of the stripped cofactor.

P018's two-basin quotient theorem implies that, once p is known, R has at most
two possible values.  The reverse direction can be far more expensive: one root
fiber may contain many distinct least-prime shells.
"""

from __future__ import annotations

from math import isqrt

from .legendre import primes_up_to
from .p017_cofactor_window import centered_cofactor_window, is_p_rough
from .precision_incidence_geometry import (
    directed_repair_depth,
    directed_repair_factor,
)

TaggedState = tuple[int, int]


def root_factor_tagged_states(k: int) -> tuple[TaggedState, ...]:
    """Return actual `(least_prime, cofactor)` states in the open square basin.

    The implementation uses the proved exact cofactor envelope followed by the
    p-rough realizability predicate.  It intentionally does not call the slower
    legacy shell enumerator, whose equality is already a separate regression.
    """

    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    states: list[TaggedState] = []
    for prime in primes_up_to(k):
        window = centered_cofactor_window(k, prime)
        for q in range(int(window["q_min"]), int(window["q_max"]) + 1):
            if is_p_rough(q, prime):
                states.append((prime, q))
    if not states:
        raise ValueError("square basin contains no composite shell states")
    return tuple(states)


def factor_partition(states: tuple[TaggedState, ...]) -> dict[TaggedState, int]:
    return {state: state[0] for state in states}


def root_partition(states: tuple[TaggedState, ...]) -> dict[TaggedState, int]:
    return {state: isqrt(state[1]) for state in states}


def root_given_factor_repair_factor(k: int) -> int:
    """Minimum alphabet for adding cofactor root when least-prime label is known."""

    states = root_factor_tagged_states(k)
    return directed_repair_factor(
        states,
        factor_partition(states),
        root_partition(states),
    )


def factor_given_root_repair_factor(k: int) -> int:
    """Minimum alphabet for adding least-prime label when cofactor root is known."""

    states = root_factor_tagged_states(k)
    return directed_repair_factor(
        states,
        root_partition(states),
        factor_partition(states),
    )


def root_factor_directed_depths(k: int, base: int = 2) -> dict[str, int]:
    """Return the two directed S12 repair depths between factor and root precision."""

    states = root_factor_tagged_states(k)
    factor = factor_partition(states)
    root = root_partition(states)
    return {
        "factor_to_root_factor": directed_repair_factor(states, factor, root),
        "root_to_factor_factor": directed_repair_factor(states, root, factor),
        "factor_to_root_depth": directed_repair_depth(states, factor, root, base),
        "root_to_factor_depth": directed_repair_depth(states, root, factor, base),
    }


def factor_root_images(k: int) -> dict[int, frozenset[int]]:
    """Actual cofactor-root values realized inside each least-prime shell."""

    states = root_factor_tagged_states(k)
    images: dict[int, set[int]] = {}
    for prime, q in states:
        images.setdefault(prime, set()).add(isqrt(q))
    return {prime: frozenset(values) for prime, values in images.items()}


def root_factor_labels(k: int) -> dict[int, frozenset[int]]:
    """Actual least-prime labels realized inside each cofactor-root fiber."""

    states = root_factor_tagged_states(k)
    labels: dict[int, set[int]] = {}
    for prime, q in states:
        labels.setdefault(isqrt(q), set()).add(prime)
    return {root: frozenset(values) for root, values in labels.items()}
