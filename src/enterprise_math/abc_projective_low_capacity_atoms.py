"""Cutoff-five prime-power atom atlas for P025 projective activation.

Stage 71 plus Stage 51 shows that if a threshold-active orientation has both
complement capacities below five, then those complements are prime powers
``p^e,q^f`` with e,f in {1,2,3,4}.  The active component is their sum (for the
c-oriented term) or positive difference (for a side-oriented term), and the
projective denominator is exactly

    e*q + f*p.

The prime-prime shell (e,f)=(1,1) can never activate at threshold one.  Every
other unordered exponent pair in {1,2,3,4}^2 is populated by an explicit
primitive threshold-one example.  Thus exponent data alone cannot further
prune the low-capacity hard slice beyond excluding prime-prime complements.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_projective_capacity_stratified import low_capacity_active_slices
from .abc_support import multiplicity_residual, radical


@dataclass(frozen=True)
class PrimePowerAtom:
    abc: tuple[int, int, int]
    active_component_index: int
    mode: str
    complement_prime_powers: tuple[tuple[int, int], tuple[int, int]]
    exponent_shell: tuple[int, int]
    cross_capacity: int
    active_residual: int
    active_radical: int


def cutoff_five_atom(a: int, b: int, c: int, threshold: int = 1) -> PrimePowerAtom | None:
    """Return the cutoff-five prime-power atom for the first low-capacity active term."""
    slices = low_capacity_active_slices(a, b, c, threshold, 5)
    if not slices:
        return None
    item = slices[0]
    bound = item.active_bound
    classes = item.complement_classifications
    if not all(data.prime_power for data in classes):
        raise AssertionError("cutoff-five atom lost prime-power complements")
    pp = tuple(
        (int(data.prime_power_base), int(data.prime_power_exponent))
        for data in classes
    )
    (p, e), (q, f) = pp
    cross_capacity = e * q + f * p
    active = bound.active_component_index
    values = (a, b, c)
    active_value = values[active]
    if active == 2:
        mode = "sum"
        if active_value != values[bound.complement_indices[0]] + values[bound.complement_indices[1]]:
            raise AssertionError("c-oriented atom lost sum relation")
    else:
        mode = "difference"
        x, y = (values[index] for index in bound.complement_indices)
        if active_value != abs(x - y):
            raise AssertionError("side-oriented atom lost difference relation")
    residual = multiplicity_residual(active_value)
    if residual < threshold * cross_capacity:
        raise AssertionError("cutoff-five atom lost projective threshold")
    return PrimePowerAtom(
        abc=(a, b, c),
        active_component_index=active,
        mode=mode,
        complement_prime_powers=(pp[0], pp[1]),
        exponent_shell=tuple(sorted((e, f))),
        cross_capacity=cross_capacity,
        active_residual=residual,
        active_radical=radical(active_value),
    )


def prime_prime_complements_cannot_activate(p: int, q: int) -> bool:
    """Prove the exponent shell (1,1) is impossible at threshold one.

    For sum orientation the denominator is p+q and m(p+q)<p+q.  For a
    difference orientation |p-q|<p+q while m(|p-q|)<=|p-q|.  Distinct primes
    are required by primitive block coprimality.
    """
    if p <= 1 or q <= 1 or p == q:
        raise ValueError("require distinct primes")
    from .abc_support import prime_factorization
    if prime_factorization(p) != ((p, 1),) or prime_factorization(q) != ((q, 1),):
        raise ValueError("require prime inputs")
    denominator = p + q
    sum_value = p + q
    diff_value = abs(p - q)
    if multiplicity_residual(sum_value) >= denominator:
        raise AssertionError("prime-prime sum unexpectedly activated")
    if diff_value and multiplicity_residual(diff_value) >= denominator:
        raise AssertionError("prime-prime difference unexpectedly activated")
    return True


def populated_nontrivial_cutoff_five_shells() -> dict[tuple[int, int], tuple[int, int, int]]:
    """Return one exact activated primitive triple for every shell except (1,1)."""
    fixtures = {
        (1, 2): (2, 25, 27),
        (1, 3): (3, 125, 128),
        (1, 4): (23, 625, 648),
        (2, 2): (9, 6241, 6250),
        (2, 3): (125, 361, 486),
        (2, 4): (49, 576, 625),
        (3, 3): (8, 1323, 1331),
        (3, 4): (81, 1250, 1331),
        (4, 4): (16, 14625, 14641),
    }
    for shell, triple in fixtures.items():
        atom = cutoff_five_atom(*triple, threshold=1)
        if atom is None or atom.exponent_shell != shell:
            raise AssertionError(f"cutoff-five shell fixture failed for {shell}")
    return fixtures
