"""Exact compact cross-coordinate transport for the BRC square-increment jet.

This module is an information-equivalent execution variant of
``t0.brc_square_increment_difference_jet``.  The current energy jet retains

    M = (nabla q) * (nabla^2 J).

The third-difference formula never observes M in isolation; it observes

    K = M + (nabla^2 q) * (nabla q + nabla J).

Because the existing jet already retains all three added finite-difference
coordinates, M and K determine each other exactly.  Retaining K directly
therefore loses no observer/provenance information while shortening the hot
third-difference and mixed-coordinate updates.

The result remains an exact multiplier-state execution optimization.  It does
not change the factor-search horizon or introduce a new factoring principle.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .brc_energy_difference_jet_tail import (
    ENERGY_JET_TOTAL_SEED_DIVISIONS,
    ENERGY_JET_TOTAL_SEED_PRODUCTS,
    EnergyJetSeedSample,
    ROOT_JET_THIRD_DIFFERENCE_MAX,
    ROOT_JET_THIRD_DIFFERENCE_MIN,
    root_third_difference_bound_sufficient,
)
from .brc_linear_deep_tail import odd_n_multiplier_is_representative
from .brc_quotient_jet_tail import (
    QUOTIENT_JET_MAX_ABS_CORRECTION as Q3,
    QUOTIENT_JET_SECOND_DIFFERENCE_MAX as Q2_MAX,
    QUOTIENT_JET_SECOND_DIFFERENCE_MIN as Q2_MIN,
    outgoing_sparse_step,
    quotient_jet_bound_sufficient,
    quotient_jet_tail_threshold,
)

_RESIDUE_INDEX = (0, 1, -1, 2, -1, 3, -1, 4)


def _pos(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def cross_coordinate_from_mixed(
    mixed_first_second: int,
    quotient_first: int,
    quotient_second: int,
    root_first: int,
) -> int:
    """Return ``K=M+a(s+t)`` from the older mixed coordinate ``M=s*u``."""
    return mixed_first_second + quotient_second * (
        quotient_first + root_first
    )


def mixed_coordinate_from_cross(
    cross_coordinate: int,
    quotient_first: int,
    quotient_second: int,
    root_first: int,
) -> int:
    """Recover ``M`` exactly from K and already-retained jet coordinates."""
    return cross_coordinate - quotient_second * (
        quotient_first + root_first
    )


def square_increment_cross_third_difference(
    *,
    target_root: int,
    target_quotient: int,
    quotient_third: int,
    root_third: int,
    cross_coordinate: int,
) -> int:
    """Exact compact third difference of ``E=q(2J+q)`` at the target point.

    If e=nabla^3 q_new, w=nabla^3 J_new and K is the current cross
    coordinate, then

      nabla^3 E_new
        = e * (2*(J_new+q_new)-e)
          + 2*w*(q_new-e)
          + 6*K.
    """
    return (
        quotient_third
        * (2 * (target_root + target_quotient) - quotient_third)
        + 2 * root_third * (target_quotient - quotient_third)
        + 6 * cross_coordinate
    )


def next_cross_coordinate(
    *,
    cross_coordinate: int,
    quotient_first: int,
    root_first: int,
    quotient_third: int,
    root_third: int,
    new_quotient_second: int,
    new_root_second: int,
) -> int:
    """Exact closed recurrence for K at the next stride-8 orbit point.

    With s=nabla q, t=nabla J, e=nabla^3 q_new, w=nabla^3 J_new,
    a'=nabla^2 q_new and u'=nabla^2 J_new,

      K' = K + s*w + e*(s+t) + a'*(2*u'+a').

    The newly evaluated products all have a bounded coefficient on the common
    certified tail: e in [-4,4], w in [-3,387], a' in [-2,98].
    """
    return (
        cross_coordinate
        + quotient_first * root_third
        + quotient_third * (quotient_first + root_first)
        + new_quotient_second * (
            2 * new_root_second + new_quotient_second
        )
    )


@dataclass(slots=True)
class CrossEnergyDifferenceJetOrbit:
    """One exact fixed-residue energy jet retaining K instead of M."""

    n: int
    step: int
    multiplier: int
    root: int
    quotient: int
    quotient_remainder: int
    q_first: int
    q_second: int
    predicted_delta_product: int
    j_first: int
    j_second: int
    cross_coordinate: int
    energy: int
    energy_first: int
    energy_second: int

    @classmethod
    def seed(
        cls,
        n: int,
        step: int,
        samples: tuple[
            EnergyJetSeedSample,
            EnergyJetSeedSample,
            EnergyJetSeedSample,
        ],
    ) -> "CrossEnergyDifferenceJetOrbit":
        _pos("n", n)
        if step not in (1, 2):
            raise ValueError("step must be 1 or 2")
        m0, m1, m2 = (sample.multiplier for sample in samples)
        if (m1 - m0, m2 - m1) != (8, 8):
            raise ValueError("seed multipliers must be separated by 8")
        if any((sample.multiplier & 7) != (m0 & 7) for sample in samples):
            raise ValueError("seed multipliers must share a residue class")
        if any(outgoing_sparse_step(sample.multiplier) != step for sample in samples):
            raise ValueError("seed residue class has the wrong step")
        if not quotient_jet_bound_sufficient(n, m0, step):
            raise ValueError("oldest seed does not certify quotient jet")
        if not root_third_difference_bound_sufficient(n, m0):
            raise ValueError("oldest seed does not certify root jet")

        for sample in samples:
            denominator = 4 * sample.multiplier + step
            if not 0 <= sample.quotient_remainder < denominator:
                raise ValueError("seed quotient remainder escaped denominator")
            if (
                sample.quotient * denominator + sample.quotient_remainder
                != 2 * step * sample.root
            ):
                raise ValueError("seed quotient/remainder does not reconstruct")
            if sample.square_increment != sample.quotient * (
                2 * sample.root + sample.quotient
            ):
                raise ValueError("seed square increment does not reconstruct")

        q0, q1, q2 = (sample.quotient for sample in samples)
        j0, j1, j2 = (sample.root for sample in samples)
        e0, e1, e2 = (sample.square_increment for sample in samples)
        s = q2 - q1
        a = q2 - 2 * q1 + q0
        if not Q2_MIN <= a <= Q2_MAX:
            raise AssertionError("seed quotient second difference escaped bound")
        t = j2 - j1
        u = j2 - 2 * j1 + j0
        energy_first = e2 - e1
        energy_second = e2 - 2 * e1 + e0
        denominator = 4 * m2 + step
        return cls(
            n=n,
            step=step,
            multiplier=m2,
            root=j2,
            quotient=q2,
            quotient_remainder=samples[2].quotient_remainder,
            q_first=s,
            q_second=a,
            predicted_delta_product=(s + a) * (denominator + 32),
            j_first=t,
            j_second=u,
            cross_coordinate=s * u + a * (s + t),
            energy=e2,
            energy_first=energy_first,
            energy_second=energy_second,
        )

    def advance(self, target_multiplier: int, target_root: int) -> tuple[int, ...]:
        if target_multiplier != self.multiplier + 8:
            raise ValueError("target must be the next stride-8 visit")
        denominator = 4 * target_multiplier + self.step
        quotient = self.quotient + self.q_first + self.q_second
        rho = (
            self.quotient_remainder
            + 2 * self.step * (target_root - self.root)
            - 32 * self.quotient
            - self.predicted_delta_product
        )
        q3 = 0
        while rho < 0:
            quotient -= 1
            rho += denominator
            q3 -= 1
            if q3 < -Q3:
                raise AssertionError("quotient lower repair bound failed")
        while rho >= denominator:
            quotient += 1
            rho -= denominator
            q3 += 1
            if q3 > Q3:
                raise AssertionError("quotient upper repair bound failed")

        j1 = target_root - self.root
        j2 = j1 - self.j_first
        j3 = j2 - self.j_second
        if not ROOT_JET_THIRD_DIFFERENCE_MIN <= j3 <= ROOT_JET_THIRD_DIFFERENCE_MAX:
            raise AssertionError("root third difference escaped proved bound")

        e3 = square_increment_cross_third_difference(
            target_root=target_root,
            target_quotient=quotient,
            quotient_third=q3,
            root_third=j3,
            cross_coordinate=self.cross_coordinate,
        )
        energy = self.energy + self.energy_first + self.energy_second + e3
        energy_first = self.energy_first + self.energy_second + e3
        energy_second = self.energy_second + e3

        old_q_first = self.q_first
        old_j_first = self.j_first
        q1 = self.q_first + self.q_second + q3
        q2 = self.q_second + q3
        if not Q2_MIN <= q2 <= Q2_MAX:
            raise AssertionError("quotient second difference escaped proved bound")

        cross_coordinate = next_cross_coordinate(
            cross_coordinate=self.cross_coordinate,
            quotient_first=old_q_first,
            root_first=old_j_first,
            quotient_third=q3,
            root_third=j3,
            new_quotient_second=q2,
            new_root_second=j2,
        )
        predicted_delta_product = (
            self.predicted_delta_product
            + (2 * q2 - self.q_second) * denominator
            + 32 * (self.q_first + 2 * q2)
        )

        self.multiplier = target_multiplier
        self.root = target_root
        self.quotient = quotient
        self.quotient_remainder = rho
        self.q_first = q1
        self.q_second = q2
        self.predicted_delta_product = predicted_delta_product
        self.j_first = j1
        self.j_second = j2
        self.cross_coordinate = cross_coordinate
        self.energy = energy
        self.energy_first = energy_first
        self.energy_second = energy_second
        return quotient, rho, energy, q3, j3, e3


@dataclass(frozen=True, slots=True)
class CrossEnergyDifferenceJetTailStep:
    source_multiplier: int
    target_multiplier: int
    source_root: int
    target_root: int
    target_remainder: int
    predictor_quotient: int
    predictor_quotient_remainder: int
    square_increment: int
    quotient_mode: str
    energy_mode: str
    quotient_third_difference: int
    root_third_difference: int
    energy_third_difference: int
    root_corrections: int

    @property
    def ceiling_completion_gap(self) -> int:
        if self.target_remainder == 0:
            return 0
        return 2 * self.target_root + 1 - self.target_remainder


class CrossEnergyDifferenceJetTailScanner:
    """Unbounded exact tail scanner using the compact K coordinate."""

    def __init__(self, n: int, start_multiplier: int | None = None) -> None:
        _pos("n", n)
        if n % 2 == 0:
            raise ValueError("scanner requires odd n")
        threshold = quotient_jet_tail_threshold(n)
        multiplier = threshold if start_multiplier is None else start_multiplier
        _pos("start_multiplier", multiplier)
        if multiplier < threshold or not odd_n_multiplier_is_representative(multiplier):
            raise ValueError("start_multiplier is before or outside certified tail")

        target = multiplier * n
        self.n = n
        self.multiplier = multiplier
        self.root = isqrt(target)
        self.remainder = target - self.root * self.root
        self.seed_divisions = 0
        self.seed_square_increment_products = 0
        self.jet_steps = 0
        self.last_source_multiplier = multiplier
        self.last_source_root = self.root
        self.last_predictor_quotient = 0
        self.last_predictor_quotient_remainder = 0
        self.last_square_increment = 0
        self.last_quotient_mode = "INITIAL"
        self.last_energy_mode = "INITIAL"
        self.last_quotient_third_difference = 0
        self.last_root_third_difference = 0
        self.last_energy_third_difference = 0
        self.last_root_corrections = 0
        self._samples: list[list[EnergyJetSeedSample]] = [[] for _ in range(5)]
        self._orbits: list[CrossEnergyDifferenceJetOrbit | None] = [None] * 5

    @property
    def active_orbit_count(self) -> int:
        return sum(orbit is not None for orbit in self._orbits)

    def advance_inplace(self) -> None:
        multiplier = self.multiplier
        root = self.root
        remainder = self.remainder
        index = _RESIDUE_INDEX[multiplier & 7]
        step = outgoing_sparse_step(multiplier)
        orbit = self._orbits[index]

        if orbit is None:
            quotient, rho = divmod(2 * step * root, 4 * multiplier + step)
            energy = quotient * (2 * root + quotient)
            self.seed_divisions += 1
            self.seed_square_increment_products += 1
            samples = self._samples[index]
            samples.append(
                EnergyJetSeedSample(
                    multiplier,
                    root,
                    quotient,
                    rho,
                    energy,
                )
            )
            if len(samples) == 3:
                self._orbits[index] = CrossEnergyDifferenceJetOrbit.seed(
                    self.n,
                    step,
                    (samples[0], samples[1], samples[2]),
                )
                samples.clear()
            quotient_mode = "SEED_DIVISION"
            energy_mode = "SEED_PRODUCT"
            q3 = j3 = e3 = 0
        else:
            quotient, rho, energy, q3, j3, e3 = orbit.advance(
                multiplier,
                root,
            )
            quotient_mode = "JET_RECURRENCE"
            energy_mode = "CROSS_COORDINATE_RECURRENCE"
            self.jet_steps += 1

        target_multiplier = multiplier + step
        candidate = root + quotient
        gap = remainder + step * self.n - energy
        corrections = 0
        while gap >= 2 * candidate + 1:
            gap -= 2 * candidate + 1
            candidate += 1
            corrections += 1
            if corrections > 2:
                raise AssertionError("linear-tail root correction bound failed")

        self.last_source_multiplier = multiplier
        self.last_source_root = root
        self.last_predictor_quotient = quotient
        self.last_predictor_quotient_remainder = rho
        self.last_square_increment = energy
        self.last_quotient_mode = quotient_mode
        self.last_energy_mode = energy_mode
        self.last_quotient_third_difference = q3
        self.last_root_third_difference = j3
        self.last_energy_third_difference = e3
        self.last_root_corrections = corrections
        self.multiplier = target_multiplier
        self.root = candidate
        self.remainder = gap

    def step(self) -> CrossEnergyDifferenceJetTailStep:
        self.advance_inplace()
        return CrossEnergyDifferenceJetTailStep(
            source_multiplier=self.last_source_multiplier,
            target_multiplier=self.multiplier,
            source_root=self.last_source_root,
            target_root=self.root,
            target_remainder=self.remainder,
            predictor_quotient=self.last_predictor_quotient,
            predictor_quotient_remainder=self.last_predictor_quotient_remainder,
            square_increment=self.last_square_increment,
            quotient_mode=self.last_quotient_mode,
            energy_mode=self.last_energy_mode,
            quotient_third_difference=self.last_quotient_third_difference,
            root_third_difference=self.last_root_third_difference,
            energy_third_difference=self.last_energy_third_difference,
            root_corrections=self.last_root_corrections,
        )


__all__ = [
    "CrossEnergyDifferenceJetOrbit",
    "CrossEnergyDifferenceJetTailScanner",
    "CrossEnergyDifferenceJetTailStep",
    "cross_coordinate_from_mixed",
    "mixed_coordinate_from_cross",
    "next_cross_coordinate",
    "square_increment_cross_third_difference",
    "ENERGY_JET_TOTAL_SEED_DIVISIONS",
    "ENERGY_JET_TOTAL_SEED_PRODUCTS",
]
