"""Exact integer grade spectrum of close-packed stacking continuation words.

A stacking trajectory is a word of signs delta_i in {+1,-1}.  The local layer
context between consecutive transition signs is FCC-like when the signs agree
and HCP-like when they differ.  The integer domain-wall count

    H(delta)=#{i : delta_(i-1) != delta_i}

therefore counts HCP-like local layer contexts.  For an open word of L transition
signs, the number of words with exactly h domain walls is

    2 * C(L-1,h).

The two h=0 words are the two orientations of FCC-like ABC/CBA cycling; the two
h=L-1 words are alternating HCP-like trajectories.  Every HCP-like layer context
contributes six 422 primitive bonds in the exact contact model, so total local
422 count is 6H.

This is a finite combinatorial structural grade.  It is not a thermodynamic
energy or probability distribution unless an external physical bridge assigns
such semantics.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb


def _validate_sign_word(signs: tuple[int, ...]) -> None:
    if not isinstance(signs, tuple) or not signs:
        raise ValueError("stacking sign word must be a non-empty tuple")
    if any(sign not in (-1, 1) for sign in signs):
        raise ValueError("every stacking transition sign must be +/-1")


def hcp_like_layer_count(signs: tuple[int, ...]) -> int:
    _validate_sign_word(signs)
    return sum(left != right for left, right in zip(signs, signs[1:]))


def fcc_like_layer_count(signs: tuple[int, ...]) -> int:
    _validate_sign_word(signs)
    return max(0, len(signs) - 1) - hcp_like_layer_count(signs)


def local_422_bond_count(signs: tuple[int, ...]) -> int:
    return 6 * hcp_like_layer_count(signs)


def local_421_bond_count(signs: tuple[int, ...]) -> int:
    # Each interior layer center has twelve primitive bonds.  An HCP-like local
    # context converts exactly six in-layer bonds from 421 to 422.
    interior_layers = max(0, len(signs) - 1)
    return 12 * interior_layers - local_422_bond_count(signs)


def stacking_grade(
    signs: tuple[int, ...],
    fcc_like_grade: int = 0,
    hcp_like_grade: int = 1,
) -> int:
    _validate_sign_word(signs)
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in (fcc_like_grade, hcp_like_grade)
    ):
        raise ValueError("local grades must be integers")
    return (
        fcc_like_layer_count(signs) * fcc_like_grade
        + hcp_like_layer_count(signs) * hcp_like_grade
    )


def stacking_word_count(length: int) -> int:
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be a positive integer")
    return 1 << length


def stacking_domain_wall_multiplicity(length: int, walls: int) -> int:
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be a positive integer")
    if isinstance(walls, bool) or not isinstance(walls, int) or not (0 <= walls < length):
        raise ValueError("walls must lie in 0..length-1")
    return 2 * comb(length - 1, walls)


def stacking_domain_wall_spectrum(length: int) -> tuple[int, ...]:
    return tuple(
        stacking_domain_wall_multiplicity(length, walls)
        for walls in range(length)
    )


def enumerate_domain_wall_spectrum(length: int) -> tuple[int, ...]:
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be a positive integer")
    counts = Counter(
        hcp_like_layer_count(tuple(signs))
        for signs in product((-1, 1), repeat=length)
    )
    return tuple(counts[walls] for walls in range(length))


def stacking_grade_spectrum(
    length: int,
    fcc_like_grade: int = 0,
    hcp_like_grade: int = 1,
) -> dict[int, int]:
    """Exact multiplicity of every total local grade in the open-chain family."""
    result: Counter[int] = Counter()
    for walls in range(length):
        fcc = length - 1 - walls
        grade = fcc * fcc_like_grade + walls * hcp_like_grade
        result[grade] += stacking_domain_wall_multiplicity(length, walls)
    return dict(sorted(result.items()))


def stacking_pascal_recurrence(length: int, walls: int) -> bool:
    """Causal one-layer lift gives the binomial/Pascal counting shadow."""
    if length < 2 or not (0 <= walls < length):
        raise ValueError("need length>=2 and a valid wall count")
    current = stacking_domain_wall_multiplicity(length, walls)
    same_previous = (
        stacking_domain_wall_multiplicity(length - 1, walls)
        if walls <= length - 2
        else 0
    )
    changed_previous = (
        stacking_domain_wall_multiplicity(length - 1, walls - 1)
        if walls >= 1
        else 0
    )
    return current == same_previous + changed_previous
