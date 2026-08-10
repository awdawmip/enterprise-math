"""Exact multi-target structural-defect dependency and synergy decomposition."""

from __future__ import annotations

from typing import Sequence, Tuple

from .precision_structural_target_cut_compiler import row_module_elements

Matrix = Tuple[Tuple[int, ...], ...]


def _width(*matrices: Matrix) -> int:
    for M in matrices:
        if M:
            return len(M[0])
    raise ValueError("need at least one row")


def _sum(A, B, modulus: int):
    return frozenset(tuple((x + y) % modulus for x, y in zip(a, b)) for a in A for b in B)


def _zero(width: int):
    return frozenset({(0,) * width})


def _pexp(n: int, p: int) -> int:
    e = 0
    while n > 1:
        if n % p:
            raise ValueError("not a p-power")
        n //= p
        e += 1
    return e


def two_target_defect_synergy(U_rows: Matrix, W1_rows: Matrix, W2_rows: Matrix, p: int, K: int):
    width = _width(U_rows, W1_rows, W2_rows)
    modulus = p ** K
    U = row_module_elements(U_rows, p, K, width=width)
    W1 = row_module_elements(W1_rows, p, K, width=width)
    W2 = row_module_elements(W2_rows, p, K, width=width)
    Wsum = _sum(W1, W2, modulus)
    Wint = W1.intersection(W2)
    observed_components = _sum(U.intersection(W1), U.intersection(W2), modulus)
    observed_joint = U.intersection(Wsum)

    def delta(W):
        return _pexp(len(W) // len(U.intersection(W)), p)

    d1, d2, dint, djoint = delta(W1), delta(W2), delta(Wint), delta(Wsum)
    synergy = _pexp(len(observed_joint) // len(observed_components), p)
    if djoint != d1 + d2 - dint - synergy:
        raise AssertionError("two-target defect decomposition violated")
    return {
        "target1_mass": d1,
        "target2_mass": d2,
        "intersection_mass": dint,
        "joint_mass": djoint,
        "synergy_mass": synergy,
    }


def multi_target_defect_decomposition(U_rows: Matrix, targets: Sequence[Matrix], p: int, K: int):
    """Canonical m-target decomposition without Möbius/distributivity assumptions.

    joint = sum individual defects - dependency_rebate - synergy_rebate.
    """
    if not targets:
        return {
            "individual_masses": tuple(),
            "joint_mass": 0,
            "dependency_rebate_mass": 0,
            "synergy_rebate_mass": 0,
        }
    width = _width(U_rows, *(tuple(targets)))
    modulus = p ** K
    U = row_module_elements(U_rows, p, K, width=width)
    Ws = [row_module_elements(W, p, K, width=width) for W in targets]
    Wsum = _zero(width)
    for W in Ws:
        Wsum = _sum(Wsum, W, modulus)
    Uis = [U.intersection(W) for W in Ws]
    Uisum = _zero(width)
    for Ui in Uis:
        Uisum = _sum(Uisum, Ui, modulus)
    UcapWsum = U.intersection(Wsum)

    def mu(H):
        return _pexp(len(H), p)

    individual = tuple(mu(W) - mu(U.intersection(W)) for W in Ws)
    joint = mu(Wsum) - mu(UcapWsum)
    target_relation_mass = sum(mu(W) for W in Ws) - mu(Wsum)
    observed_relation_mass = sum(mu(Ui) for Ui in Uis) - mu(Uisum)
    dependency_rebate = target_relation_mass - observed_relation_mass
    synergy = mu(UcapWsum) - mu(Uisum)
    if dependency_rebate < 0 or synergy < 0:
        raise AssertionError("canonical rebate masses must be nonnegative")
    if joint != sum(individual) - dependency_rebate - synergy:
        raise AssertionError("multi-target defect decomposition violated")
    return {
        "individual_masses": individual,
        "joint_mass": joint,
        "dependency_rebate_mass": dependency_rebate,
        "synergy_rebate_mass": synergy,
    }
