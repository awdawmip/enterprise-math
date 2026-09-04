"""Task-local checker for the branch-memory lattice behind the post-#1161 AGM RG.

For a two-element witness fiber D={A,B}, cumulative multiplicities (a,b) are
quotiented by common diagonal shifts.  The quotient coordinate z=a-b is a
rank-one integer lattice; witness swap sends z to -z.  The unlabeled first-return
observer sees only |z|.

This checker verifies the finite-horizon predictive class counts:
- branch-resolved deterministic language: 2*h+2 classes;
- swap-orbit / unlabeled first-return-mass language: h+2 classes.

No floating point, roots, or pi are used.
"""

from __future__ import annotations

from itertools import product
from math import comb


def memory_class(a: int, b: int) -> int:
    """Coordinate of Z^D / Z*1 after choosing proof labels A,B."""
    return a - b


def append_a(z: int) -> int:
    return z + 1


def append_b(z: int) -> int:
    return z - 1


def swap_witnesses(z: int) -> int:
    return -z


def terminal_step(z: int, letter: int) -> int:
    """Absorbing-zero verification dynamics for first-hit future language."""
    if z == 0:
        return 0
    return z + (1 if letter == 1 else -1)


def endpoint_zero_after_word(z: int, word: tuple[int, ...]) -> int:
    current = z
    for letter in word:
        current = terminal_step(current, letter)
    return int(current == 0)


def all_words(horizon: int) -> tuple[tuple[int, ...], ...]:
    words: list[tuple[int, ...]] = [()]
    for length in range(1, horizon + 1):
        words.extend(product((-1, 1), repeat=length))
    return tuple(words)


def resolved_signature(z: int, horizon: int) -> tuple[int, ...]:
    return tuple(endpoint_zero_after_word(z, word) for word in all_words(horizon))


def first_hit_count(distance: int, steps: int) -> int:
    if distance == 0:
        return int(steps == 0)
    if steps == 0 or steps < distance or (steps - distance) % 2:
        return 0
    numerator = distance * comb(steps, (steps - distance) // 2)
    if numerator % steps:
        raise AssertionError("ballot count lost integrality")
    return numerator // steps


def unlabeled_signature(z: int, horizon: int) -> tuple[int, ...]:
    d = abs(z)
    return tuple(first_hit_count(d, step) for step in range(horizon + 1))


def run() -> dict[str, object]:
    # Quotient and swap laws on a bounded exact census.
    quotient_cases = 0
    for a in range(0, 33):
        for b in range(0, 33):
            z = memory_class(a, b)
            for k in range(-32, 33):
                if a + k >= 0 and b + k >= 0:
                    if memory_class(a + k, b + k) != z:
                        raise AssertionError("common-shift quotient law failed")
            if memory_class(b, a) != swap_witnesses(z):
                raise AssertionError("witness swap did not invert memory coordinate")
            if memory_class(a + 1, b) != append_a(z):
                raise AssertionError("A append law failed")
            if memory_class(a, b + 1) != append_b(z):
                raise AssertionError("B append law failed")
            quotient_cases += 1

    resolved_counts: list[int] = []
    unlabeled_counts: list[int] = []
    for horizon in range(0, 11):
        radius = 2 * horizon + 5
        states = range(-radius, radius + 1)

        resolved = {z: resolved_signature(z, horizon) for z in states}
        resolved_count = len(set(resolved.values()))
        if resolved_count != 2 * horizon + 2:
            raise AssertionError(
                f"resolved horizon {horizon}: {resolved_count} != {2*horizon+2}"
            )
        far_resolved = resolved_signature(horizon + 1, horizon)
        for z in states:
            if abs(z) > horizon and resolved[z] != far_resolved:
                raise AssertionError("resolved far states failed to coalesce")

        unlabeled = {z: unlabeled_signature(z, horizon) for z in states}
        unlabeled_count = len(set(unlabeled.values()))
        if unlabeled_count != horizon + 2:
            raise AssertionError(
                f"unlabeled horizon {horizon}: {unlabeled_count} != {horizon+2}"
            )
        for z in states:
            if unlabeled[z] != unlabeled[-z]:
                raise AssertionError("unlabeled quotient failed swap invariance")

        resolved_counts.append(resolved_count)
        unlabeled_counts.append(unlabeled_count)

    return {
        "quotient_cases": quotient_cases,
        "horizons_checked": 11,
        "resolved_class_counts_h0_to_h10": resolved_counts,
        "unlabeled_class_counts_h0_to_h10": unlabeled_counts,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "quotient_cases": 1089,
        "horizons_checked": 11,
        "resolved_class_counts_h0_to_h10": [2,4,6,8,10,12,14,16,18,20,22],
        "unlabeled_class_counts_h0_to_h10": [2,3,4,5,6,7,8,9,10,11,12],
    }
    if result != expected:
        raise SystemExit(f"unexpected branch-memory lattice output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
