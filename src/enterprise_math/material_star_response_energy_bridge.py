"""Kinetic-energy spectrum of the minimum-total symmetric-star response relation.

The star-response precision owner classifies every minimum-total impulse numerator
vector at denominator ``s``.  For ``k`` equal-mass leaves and closing quantum
``q``, write

    Q = q*s = (k+1)t + r,      0 <= r <= k,

and let the minimum-total relation be

    a_i = t + x_i,
    x_i >= 0,
    sum_i x_i = r.

The scaled initial body-momentum numerator state is one center with momentum
``Q`` and ``k`` leaves at zero.  If ``S=sum a_i``, contact incidence gives the
after-state

    center: Q-S,
    leaf i: a_i.

On the common denominator, the equal-mass kinetic coordinate is proportional to
sum of squared body-momentum numerators.  Its exact change is

    Delta E = (Q-S)^2 + sum_i a_i^2 - Q^2
            = S^2 - 2QS + sum_i a_i^2.

Across the entire minimum-total relation, ``S`` is fixed.  Therefore physical
energy ambiguity is exactly the variation of ``sum x_i^2``.  Since ``0<=r<=k``:

* the most balanced weak composition has ``sum x_i^2=r``;
* the most concentrated one has ``sum x_i^2=r^2``.

Hence

    Delta E_least_dissipative = -k*t*((k+1)t + 2r) <= 0,
    Delta E_most_dissipative  = Delta E_least_dissipative - r(r-1),
    energy-spectrum width     = r(r-1).

Consequences:

* every minimum-total star response is passive in this kinetic coordinate;
* energy is identical across the minimum relation exactly for residue r=0 or 1;
* for r>=2, minimum total impulse does not determine kinetic after-state energy;
* at the symmetric residue gate r=k, the permutation-fixed minimum ``x_i=1``
a  attains the most-dissipative endpoint, while concentrated minima dissipate less.

The energy metric and star impulse algebra are standard mechanics/linear algebra.
This module is an E001 cross-owner diagnostic showing that response-relation
ambiguity can remain physically visible even after total impulse is minimized.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .material_star_response_precision_phase import (
    star_minimum_response_relation_at_precision,
    star_minimum_total_numerator_at_precision,
    star_scaled_closing_phase,
    star_symmetric_minimum_numerators,
)


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _leaf_count(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        raise ValueError("leaf_count must be an integer at least two")


def star_equal_mass_kinetic_change_numerator(
    impulse_numerators: tuple[int, ...] | list[int],
    closing_quantum: int,
    denominator: int,
) -> int:
    """Return exact squared-momentum numerator change for one star response."""
    values = tuple(impulse_numerators)
    if len(values) < 2:
        raise ValueError("star response requires at least two leaves")
    _positive("closing_quantum", closing_quantum)
    _positive("denominator", denominator)
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in values):
        raise ValueError("impulse numerators must be non-negative integers")
    demand = closing_quantum * denominator
    total = sum(values)
    return (demand - total) ** 2 + sum(value * value for value in values) - demand**2


@dataclass(frozen=True, order=True)
class StarMinimumEnergyBin:
    kinetic_change_numerator: int
    response_count: int


@dataclass(frozen=True)
class StarMinimumEnergySpectrum:
    leaf_count: int
    closing_quantum: int
    denominator: int
    quotient_baseline: int
    residue: int
    minimum_total_impulse_numerator: int
    response_relation_cardinality: int
    energy_bins: tuple[StarMinimumEnergyBin, ...]
    most_dissipative_change_numerator: int
    least_dissipative_change_numerator: int
    energy_spectrum_width: int
    energy_unique_across_minimum_relation: bool
    all_minimum_responses_passive: bool
    symmetric_minimum_energy_change_numerator: int | None
    symmetric_minimum_is_most_dissipative: bool | None


def star_minimum_energy_spectrum(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> StarMinimumEnergySpectrum:
    """Return exact kinetic-energy bins across one minimum-total response relation."""
    _leaf_count(leaf_count)
    _positive("closing_quantum", closing_quantum)
    _positive("denominator", denominator)
    baseline, residue = star_scaled_closing_phase(
        leaf_count, closing_quantum, denominator
    )
    minimum_total = star_minimum_total_numerator_at_precision(
        leaf_count, closing_quantum, denominator
    )
    relation = star_minimum_response_relation_at_precision(
        leaf_count, closing_quantum, denominator
    )
    if any(sum(vector) != minimum_total for vector in relation):
        raise AssertionError("star minimum relation lost fixed total impulse")

    counts: Counter[int] = Counter(
        star_equal_mass_kinetic_change_numerator(
            vector, closing_quantum, denominator
        )
        for vector in relation
    )
    bins = tuple(
        StarMinimumEnergyBin(change, count)
        for change, count in sorted(counts.items())
    )
    most_dissipative = -leaf_count * baseline * (
        (leaf_count + 1) * baseline + 2 * residue
    ) - residue * (residue - 1)
    least_dissipative = -leaf_count * baseline * (
        (leaf_count + 1) * baseline + 2 * residue
    )
    width = residue * (residue - 1)
    observed_min = min(counts)
    observed_max = max(counts)
    if (observed_min, observed_max) != (most_dissipative, least_dissipative):
        raise AssertionError("star energy enumeration disagrees with residue endpoint formulas")
    if observed_max - observed_min != width:
        raise AssertionError("star energy spectrum width lost residue formula")
    passive = observed_max <= 0
    if not passive:
        raise AssertionError("minimum-total star relation unexpectedly injected kinetic energy")

    symmetric = star_symmetric_minimum_numerators(
        leaf_count, closing_quantum, denominator
    )
    if symmetric is None:
        symmetric_energy = None
        symmetric_is_most = None
    else:
        symmetric_energy = star_equal_mass_kinetic_change_numerator(
            symmetric, closing_quantum, denominator
        )
        symmetric_is_most = symmetric_energy == most_dissipative

    return StarMinimumEnergySpectrum(
        leaf_count=leaf_count,
        closing_quantum=closing_quantum,
        denominator=denominator,
        quotient_baseline=baseline,
        residue=residue,
        minimum_total_impulse_numerator=minimum_total,
        response_relation_cardinality=len(relation),
        energy_bins=bins,
        most_dissipative_change_numerator=most_dissipative,
        least_dissipative_change_numerator=least_dissipative,
        energy_spectrum_width=width,
        energy_unique_across_minimum_relation=len(bins) == 1,
        all_minimum_responses_passive=passive,
        symmetric_minimum_energy_change_numerator=symmetric_energy,
        symmetric_minimum_is_most_dissipative=symmetric_is_most,
    )
