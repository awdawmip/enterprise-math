"""Exact derivative-gain reduction on the two-nonsquarefree activation slice.

Suppose a primitive non-unit triple has exactly two nonsquarefree components.
Stage 69 forces them to be c and exactly one side y; let s be the unique
squarefree side.  Since s is squarefree, its block capacity is the standard
arithmetic derivative s'.

If sigma_proj >= an integer threshold T, then regardless of whether the active
cyclic term is y- or c-oriented, the repeated pair satisfies

    rad(y) * rad(c) <= max(y,c) / (T*s') <= c/(T*s').

Thus the Stage-64 pair-radical compiler gains an exact factor equal to the
arithmetic derivative of the squarefree side.  For composite squarefree s,
classical arithmetic-derivative bounds give s'>=2*sqrt(s); prime s has s'=1
and is the lowest-capacity branch.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_projective_orientation import raw_derivative_mass
from .abc_projective_squarefree_basin import is_squarefree_integer
from .abc_support import abc_support_state, radical


@dataclass(frozen=True)
class TwoNonsquarefreeProjectiveState:
    abc: tuple[int, int, int]
    threshold: int
    squarefree_side_index: int
    squarefree_side_value: int
    squarefree_side_derivative: int
    repeated_side_index: int
    repeated_pair: tuple[int, int]
    repeated_pair_radical: int
    active_cyclic_indices: tuple[int, ...]


def two_nonsquarefree_projective_state(
    a: int, b: int, c: int, threshold: int
) -> TwoNonsquarefreeProjectiveState | None:
    """Return the derivative-gain pair state when the threshold is crossed.

    ``None`` means the triple has the required exactly-two-nonsquarefree shape
    but ``sigma_proj<threshold``.
    """
    abc_support_state(a, b, c)
    if a <= 1 or b <= 1:
        raise ValueError("require a non-unit primitive triple")
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be an integer >=1")
    values = (a, b, c)
    flags = tuple(is_squarefree_integer(n) for n in values)
    if sum(not flag for flag in flags) != 2:
        raise ValueError("require exactly two nonsquarefree components")
    if flags[2]:
        raise ValueError("Stage-69 necessity requires nonsquarefree c")
    squarefree_side_index = 0 if flags[0] else 1
    repeated_side_index = 1 - squarefree_side_index
    s = values[squarefree_side_index]
    y = values[repeated_side_index]
    s_derivative = raw_derivative_mass(s)
    if s_derivative <= 0:
        raise AssertionError("non-unit squarefree side must have positive derivative")

    state = projective_capacity_condition_state(a, b, c)
    if state.sigma_projective < threshold:
        return None

    # Stored cyclic order is c,b,a.  The squarefree-side oriented term cannot
    # activate because its residual is one, so every active term is c or y.
    active = tuple(
        i
        for i, ratio in enumerate(state.cyclic_weighted_defects)
        if ratio >= threshold
    )
    squarefree_cyclic_index = 2 if squarefree_side_index == 0 else 1
    if squarefree_cyclic_index in active:
        raise AssertionError("squarefree-side projective term unexpectedly activated")

    pair_radical = radical(y) * radical(c)
    # Exact derivative-gain envelope: T*s'*rad(y)rad(c) <= c (for c-oriented)
    # or <= y (for y-oriented); the common safe envelope is <=c.
    if threshold * s_derivative * pair_radical > c:
        raise AssertionError("two-nonsquarefree pair radical exceeded derivative-gain envelope")

    return TwoNonsquarefreeProjectiveState(
        abc=(a, b, c),
        threshold=threshold,
        squarefree_side_index=squarefree_side_index,
        squarefree_side_value=s,
        squarefree_side_derivative=s_derivative,
        repeated_side_index=repeated_side_index,
        repeated_pair=(y, c),
        repeated_pair_radical=pair_radical,
        active_cyclic_indices=active,
    )


def composite_squarefree_derivative_gap(n: int) -> bool:
    """Verify the classical ``n'>=2*sqrt(n)`` gap without floating point.

    For a composite squarefree n, Omega(n)>=2; the standard lower bound
    ``n'>=r*n^((r-1)/r)`` implies in particular ``n'^2>=4n``.
    """
    if n <= 1 or not is_squarefree_integer(n):
        raise ValueError("require a squarefree integer >1")
    # Prime squarefree numbers are the low-capacity equality branch n'=1.
    if raw_derivative_mass(n) == 1:
        raise ValueError("require composite squarefree n")
    derivative = raw_derivative_mass(n)
    if derivative * derivative < 4 * n:
        raise AssertionError("composite squarefree derivative lost 2*sqrt(n) lower bound")
    return True
