"""Structural target-defect diamond and premature-collapse interaction module."""

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


def _pexp(n: int, p: int) -> int:
    e = 0
    while n > 1:
        if n % p:
            raise ValueError("not a p-power")
        n //= p
        e += 1
    return e


def structural_defect_diamond(
    U_fine_rows: Matrix,
    U_coarse_rows: Matrix,
    W_strong_rows: Matrix,
    W_weak_rows: Matrix,
    p: int,
    K: int,
):
    """Exact exponent-mass data for U'<=U and W'<=W.

    U_fine=U, U_coarse=U', W_strong=W, W_weak=W'.
    """
    width = _width(U_fine_rows, U_coarse_rows, W_strong_rows, W_weak_rows)
    modulus = p ** K
    U = row_module_elements(U_fine_rows, p, K, width=width)
    Up = row_module_elements(U_coarse_rows, p, K, width=width)
    W = row_module_elements(W_strong_rows, p, K, width=width)
    Wp = row_module_elements(W_weak_rows, p, K, width=width)
    if not Up.issubset(U):
        raise ValueError("coarse observation row module must be contained in fine observation")
    if not Wp.issubset(W):
        raise ValueError("weak target row module must be contained in strong target")

    UcapW = U.intersection(W)
    UpcapW = Up.intersection(W)
    UcapWp = U.intersection(Wp)
    UpcapWp = Up.intersection(Wp)
    interaction_den = _sum(UpcapW, UcapWp, modulus)

    j_strong = len(UcapW) // len(UpcapW)
    j_weak = len(UcapWp) // len(UpcapWp)
    interaction = len(UcapW) // len(interaction_den)

    UpW = _sum(Up, W, modulus)
    UpWp = _sum(Up, Wp, modulus)
    UW = _sum(U, W, modulus)
    UWp = _sum(U, Wp, modulus)
    l_coarse = len(UpW) // len(UpWp)
    l_fine = len(UW) // len(UWp)

    if j_strong != j_weak * interaction:
        raise AssertionError("observation-loss exact sequence violated")
    if l_coarse != interaction * l_fine:
        raise AssertionError("target-retirement exact sequence violated")

    def delta(A, B):
        return _pexp(len(_sum(A, B, modulus)) // len(A), p)

    d_UW = delta(U, W)
    d_UpW = delta(Up, W)
    d_UWp = delta(U, Wp)
    d_UpWp = delta(Up, Wp)
    interaction_mass = _pexp(interaction, p)
    cross = d_UpW + d_UWp - d_UW - d_UpWp
    if cross != interaction_mass:
        raise AssertionError("four-point interaction identity violated")

    return {
        "strong_observation_loss_mass": _pexp(j_strong, p),
        "weak_observation_loss_mass": _pexp(j_weak, p),
        "interaction_mass": interaction_mass,
        "coarse_target_retirement_mass": _pexp(l_coarse, p),
        "fine_target_retirement_mass": _pexp(l_fine, p),
        "delta_fine_strong": d_UW,
        "delta_coarse_strong": d_UpW,
        "delta_fine_weak": d_UWp,
        "delta_coarse_weak": d_UpWp,
    }
