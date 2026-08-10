"""Exact repetition-phase spectrum for contact critical-group precision.

One contact body-delta class of finite critical order ``s`` needs potential/cycle
representation denominator ``s``.  Repeating the same physical delta ``m``
times multiplies that critical-group element by ``m``.  Its exact new order is

    s_m = s / gcd(s,m).

Hence the precision pattern is periodic modulo ``s``.  The possible denominator
values over one complete period are exactly the divisors ``q|s`` and the number
of phases with denominator ``q`` is exactly Euler's totient

    #{m mod s : s/gcd(s,m)=q} = phi(q).

So a finite torsion class carries an exact precision phase distribution, not
merely a worst-case denominator.  The mean denominator over one period is

    (1/s) * sum_{q|s} q*phi(q).

For a connected contact graph, primitive edge body-delta classes generate the
critical group ``K(G)=im(B)/im(L)``.  Therefore the lcm of their class orders is
exactly the critical-group exponent ``E`` and is the least common denominator
sufficient for every integer contact history in the potential/cycle
representation.  If every history is multiplied by a common repetition factor
``m``, the new uniform denominator is

    E_m = E / gcd(E,m),

with the same totient phase spectrum over one period ``E``.

This separates three graph-topological resources:

* ``beta=rank H_1(G;Z)``: free hidden-history dimension;
* ``exp K(G)``: uniform representation denominator;
* ``|K(G)|``: number of finite torsion classes / spanning-tree count.

Finite abelian groups, Euler totient identities and critical groups are standard
prior mathematics.  This module is the E001/P024 precision interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Sequence

from .contact_critical_precision import contact_critical_precision_report
from .contact_cycle_witness_repair import fundamental_cycle_lattice


Matrix = tuple[tuple[int, ...], ...]


def _require_positive_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _lcm(left: int, right: int) -> int:
    _require_positive_int("left", left)
    _require_positive_int("right", right)
    return abs(left * right) // gcd(left, right)


def positive_divisors(value: int) -> tuple[int, ...]:
    _require_positive_int("value", value)
    lower = []
    upper = []
    divisor = 1
    while divisor * divisor <= value:
        if value % divisor == 0:
            lower.append(divisor)
            partner = value // divisor
            if partner != divisor:
                upper.append(partner)
        divisor += 1
    return tuple(lower + list(reversed(upper)))


def euler_totient(value: int) -> int:
    _require_positive_int("value", value)
    result = value
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            while remaining % prime == 0:
                remaining //= prime
            result -= result // prime
        prime += 1
    if remaining > 1:
        result -= result // remaining
    return result


def repeated_critical_denominator(
    critical_class_order: int,
    repetitions: int,
) -> int:
    """Exact order/denominator of ``m*x`` when ``ord(x)=s``."""
    _require_positive_int("critical_class_order", critical_class_order)
    _require_int("repetitions", repetitions)
    return critical_class_order // gcd(
        critical_class_order,
        abs(repetitions),
    )


@dataclass(frozen=True)
class CriticalPrecisionPhase:
    denominator: int
    phase_count: int


def critical_precision_phase_spectrum(
    critical_class_order: int,
) -> tuple[CriticalPrecisionPhase, ...]:
    """Exact denominator distribution over one repetition period modulo ``s``."""
    _require_positive_int("critical_class_order", critical_class_order)
    phases = tuple(
        CriticalPrecisionPhase(
            denominator=denominator,
            phase_count=euler_totient(denominator),
        )
        for denominator in positive_divisors(critical_class_order)
    )
    if sum(phase.phase_count for phase in phases) != critical_class_order:
        raise AssertionError("totient phase counts failed to partition one period")
    return phases


def critical_precision_average_denominator(
    critical_class_order: int,
) -> Fraction:
    """Exact mean denominator over one full repetition period."""
    phases = critical_precision_phase_spectrum(critical_class_order)
    return Fraction(
        sum(
            phase.denominator * phase.phase_count
            for phase in phases
        ),
        critical_class_order,
    )


def critical_precision_phase_histogram_direct(
    critical_class_order: int,
) -> tuple[tuple[int, int], ...]:
    """Direct residue enumeration used as an independent executable oracle."""
    _require_positive_int("critical_class_order", critical_class_order)
    counts: dict[int, int] = {}
    for repetitions in range(critical_class_order):
        denominator = repeated_critical_denominator(
            critical_class_order,
            repetitions,
        )
        counts[denominator] = counts.get(denominator, 0) + 1
    return tuple(sorted(counts.items()))


def repetition_refinement_respects_divisibility(
    critical_class_order: int,
    coarse_repetitions: int,
    fine_repetitions: int,
) -> bool:
    """Verify ``m|m'`` implies the refined denominator divides the coarse one."""
    _require_positive_int("critical_class_order", critical_class_order)
    _require_positive_int("coarse_repetitions", coarse_repetitions)
    _require_positive_int("fine_repetitions", fine_repetitions)
    if fine_repetitions % coarse_repetitions != 0:
        raise ValueError("coarse_repetitions must divide fine_repetitions")
    coarse = repeated_critical_denominator(
        critical_class_order,
        coarse_repetitions,
    )
    fine = repeated_critical_denominator(
        critical_class_order,
        fine_repetitions,
    )
    if coarse % fine != 0:
        raise AssertionError("divisibility refinement increased critical denominator")
    return True


def _incidence_matrix(
    incidence: Sequence[Sequence[int]],
) -> Matrix:
    rows = tuple(tuple(row) for row in incidence)
    lattice = fundamental_cycle_lattice(rows)
    if lattice.component_count != 1:
        raise ValueError("critical phase signature requires a connected graph")
    return rows


@dataclass(frozen=True)
class ContactGraphCriticalPhaseSignature:
    cycle_rank: int
    critical_group_order: int
    critical_group_exponent: int
    edge_class_orders: tuple[int, ...]

    @property
    def uniform_potential_denominator(self) -> int:
        return self.critical_group_exponent

    def repeated_uniform_denominator(self, repetitions: int) -> int:
        return repeated_critical_denominator(
            self.critical_group_exponent,
            repetitions,
        )

    @property
    def phase_spectrum(self) -> tuple[CriticalPrecisionPhase, ...]:
        return critical_precision_phase_spectrum(
            self.critical_group_exponent
        )


def contact_graph_critical_phase_signature(
    incidence: Sequence[Sequence[int]],
    *,
    root: int | None = None,
) -> ContactGraphCriticalPhaseSignature:
    """Return ``(beta, |K(G)|, exp K(G))`` plus primitive-edge class orders."""
    matrix = _incidence_matrix(incidence)
    body_count = len(matrix)
    edge_count = len(matrix[0])
    if edge_count <= 0:
        raise ValueError("critical phase signature requires at least one edge")
    if root is None:
        root = body_count - 1
    _require_int("root", root)
    if not 0 <= root < body_count:
        raise ValueError("root is outside the vertex set")

    edge_orders = []
    group_order: int | None = None
    exponent = 1
    for edge in range(edge_count):
        history = tuple(
            1 if index == edge else 0
            for index in range(edge_count)
        )
        report = contact_critical_precision_report(
            matrix,
            history,
            root=root,
        )
        if group_order is None:
            group_order = report.spanning_tree_count
        elif group_order != report.spanning_tree_count:
            raise AssertionError("critical group order changed between edge generators")
        edge_orders.append(report.critical_class_order)
        exponent = _lcm(exponent, report.critical_class_order)

    if group_order is None or group_order <= 0:
        raise AssertionError("connected graph lost its critical group order")
    if group_order % exponent != 0:
        raise AssertionError("critical group exponent must divide group order")

    cycle_rank = fundamental_cycle_lattice(matrix).cycle_rank
    return ContactGraphCriticalPhaseSignature(
        cycle_rank=cycle_rank,
        critical_group_order=group_order,
        critical_group_exponent=exponent,
        edge_class_orders=tuple(edge_orders),
    )


def graph_uniform_repetition_denominator_from_edges(
    signature: ContactGraphCriticalPhaseSignature,
    repetitions: int,
) -> int:
    """Independent lcm-of-scaled-generators check of the exponent formula."""
    if not isinstance(signature, ContactGraphCriticalPhaseSignature):
        raise TypeError("signature must be ContactGraphCriticalPhaseSignature")
    _require_int("repetitions", repetitions)
    result = 1
    for order in signature.edge_class_orders:
        result = _lcm(
            result,
            repeated_critical_denominator(order, repetitions),
        )
    expected = signature.repeated_uniform_denominator(repetitions)
    if result != expected:
        raise AssertionError("scaled edge generators disagreed with exponent phase")
    return result
