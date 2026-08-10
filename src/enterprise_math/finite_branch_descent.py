"""Finite labelled-branch coherence across modular precision.

Let a fixed exact world law be a finite labelled disjunction

    P = OR_(lambda in Lambda) P_lambda.

For one modulus M define the branch-support set

    S_M = {lambda : P_lambda has a solution modulo M}.

Because a solution modulo N reduces modulo M whenever M|N,

    M|N  =>  S_N subseteq S_M.

If the local/unlabelled law is **branch-reflecting** at every modulus, then local
solvability implies ``S_M`` is nonempty.  Finiteness of Lambda and lcm-directed
precision then force one label to survive every modulus.

Contrapositive blocker form: suppose every label lambda has one blocker modulus
``b_lambda`` at which that branch has no solution.  Let

    L = lcm_lambda b_lambda.

Then every labelled branch is blocked modulo L.  Hence any unlabelled solution
modulo L is an explicit finite-precision certificate that branch reflection has
failed.

This module implements the finite set/lcm part of that theorem.  It does not
attempt to decide arbitrary Diophantine branch solvability by itself; callers
supply a branch-solver predicate.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Callable, Hashable, Mapping, Sequence


Label = Hashable
BranchSolver = Callable[[Label, int], bool]


def _modulus(value: int, *, name: str = "modulus") -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def branch_support_at_modulus(
    labels: Sequence[Label],
    modulus: int,
    branch_solver: BranchSolver,
) -> frozenset[Label]:
    values = tuple(labels)
    if not values:
        raise ValueError("label family must be nonempty")
    if len(set(values)) != len(values):
        raise ValueError("branch labels must be distinct")
    M = _modulus(modulus)
    if not callable(branch_solver):
        raise TypeError("branch_solver must be callable")
    return frozenset(
        label for label in values if branch_solver(label, M)
    )


def branch_support_descends_under_divisibility(
    labels: Sequence[Label],
    coarser_modulus: int,
    finer_modulus: int,
    branch_solver: BranchSolver,
) -> bool:
    coarse = _modulus(coarser_modulus, name="coarser_modulus")
    fine = _modulus(finer_modulus, name="finer_modulus")
    if fine % coarse != 0:
        raise ValueError("finer_modulus must be divisible by coarser_modulus")
    coarse_support = branch_support_at_modulus(labels, coarse, branch_solver)
    fine_support = branch_support_at_modulus(labels, fine, branch_solver)
    if not fine_support.issubset(coarse_support):
        raise AssertionError("branch support failed reduction monotonicity")
    return True


def blocker_lcm(blockers: Mapping[Label, int]) -> int:
    if not blockers:
        raise ValueError("blocker map must be nonempty")
    result = 1
    for modulus in blockers.values():
        result = lcm(result, _modulus(modulus, name="blocker modulus"))
    return result


@dataclass(frozen=True)
class FiniteBranchBlockerReport:
    labels: tuple[Label, ...]
    blockers: tuple[tuple[Label, int], ...]
    joint_modulus: int
    joint_branch_support: frozenset[Label]
    every_label_blocked: bool
    unlabelled_locally_solvable: bool | None

    @property
    def branch_reflection_failure(self) -> bool:
        return (
            self.every_label_blocked
            and self.unlabelled_locally_solvable is True
        )


def finite_branch_blocker_report(
    blockers: Mapping[Label, int],
    branch_solver: BranchSolver,
    *,
    unlabelled_solver: Callable[[int], bool] | None = None,
) -> FiniteBranchBlockerReport:
    """Combine one blocker per label into one joint precision.

    The supplied blocker for each label is verified directly.  The joint lcm is
    then checked directly as well, avoiding any hidden assumption about the
    branch solver beyond its declared modular semantics.
    """
    if not blockers:
        raise ValueError("blocker map must be nonempty")
    labels = tuple(blockers)
    if len(set(labels)) != len(labels):
        raise ValueError("branch labels must be distinct")
    normalized = tuple(
        (label, _modulus(modulus, name="blocker modulus"))
        for label, modulus in blockers.items()
    )
    if not callable(branch_solver):
        raise TypeError("branch_solver must be callable")

    for label, modulus in normalized:
        if branch_solver(label, modulus):
            raise ValueError("declared blocker still admits its branch")

    joint = blocker_lcm(dict(normalized))
    support = branch_support_at_modulus(labels, joint, branch_solver)
    if support:
        # A true blocker at a divisor should remain a blocker at every multiple
        # for ordinary reduction semantics.  Treat a violation as a malformed
        # branch solver / precision system rather than silently accepting it.
        raise AssertionError("blocked branch resurrected at a finer joint modulus")

    unlabelled = None
    if unlabelled_solver is not None:
        if not callable(unlabelled_solver):
            raise TypeError("unlabelled_solver must be callable")
        unlabelled = bool(unlabelled_solver(joint))

    return FiniteBranchBlockerReport(
        labels=labels,
        blockers=normalized,
        joint_modulus=joint,
        joint_branch_support=support,
        every_label_blocked=not support,
        unlabelled_locally_solvable=unlabelled,
    )


def finite_branch_survival_theorem_statement() -> str:
    """Machine-visible statement of the finite-label lcm argument."""
    return (
        "If a fixed finite labelled branch family is branch-reflecting at every "
        "positive modulus and the unlabelled law is locally solvable at every "
        "modulus, then at least one fixed label is locally solvable at every "
        "modulus."
    )
