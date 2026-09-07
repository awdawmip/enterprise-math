"""Scaled cross-coordinate implementation of the exact BRC energy jet.

The existing square-increment difference jet retains

    M = (nabla q) * (nabla^2 J).

Its third-difference observer uses M only through

    K = M + (nabla^2 q) * (nabla q + nabla J).

This module retains the scaled coordinate

    C = 6*K

instead.  M and C are exactly interconvertible because the other finite-
difference coordinates are already retained.  The scaling removes the hot-loop
``6*K`` multiplication from the energy third-difference formula while keeping
all newly evaluated products bounded-coefficient big-integer products.

This is an information-equivalent execution variant of
``t0.brc_square_increment_difference_jet``.  It does not change the multiplier
search horizon or introduce a new factoring principle.
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


def scaled_cross_from_mixed(
    mixed_first_second: int,
    quotient_first: int,
    quotient_second: int,
    root_first: int,
) -> int:
    """Return ``C=6*(M+a*(s+t))`` from the older coordinate ``M=s*u``."""
    return 6 * (
        mixed_first_second
        + quotient_second * (quotient_first + root_first)
    )


def mixed_from_scaled_cross(
    scaled_cross: int,
    quotient_first: int,
    quotient_second: int,
    root_first: int,
) -> int:
    """Recover M exactly from C and already-retained finite differences."""
    quotient, remainder = divmod(scaled_cross, 6)
    if remainder:
        raise ValueError("scaled cross coordinate must be divisible by 6")
    return quotient - quotient_second * (quotient_first + root_first)


def square_increment_scaled_cross_third_difference(
    *,
    target_root: int,
    target_quotient: int,
    quotient_third: int,
    root_third: int,
    scaled_cross: int,
) -> int:
    """Exact compact third difference of ``E=q(2J+q)`` at the target point.

    With e=nabla^3 q_new, w=nabla^3 J_new and C=6K at the current orbit point,

      nabla^3 E_new
        = e*(2*(J_new+q_new)-e) + 2*w*(q_new-e) + C.
    """
    return (
        quotient_third
        * (2 * (target_root + target_quotient) - quotient_third)
        + 2 * root_third * (target_quotient - quotient_third)
        + scaled_cross
    )


def next_scaled_cross(
    *,
    scaled_cross: int,
    quotient_first: int,
    root_first: int,
    quotient_third: int,
    root_third: int,
    new_quotient_second: int,
    new_root_second: int,
) -> int:
    """Exact closed recurrence for ``C=6K`` at the next orbit point.

    If s=nabla q, t=nabla J, e=nabla^3 q_new, w=nabla^3 J_new,
    a'=nabla^2 q_new and u'=nabla^2 J_new, then

      C' = C + 6*s*w + 6*e*(s+t) + 6*a'*(2*u'+a').

    The multipliers ``6*w``, ``6*e`` and ``6*a'`` are uniformly bounded on the
    certified tail.
    """
    return (
        scaled_cross
        + (6 * root_third) * quotient_first
        + (6 * quotient_third) * (quotient_first + root_first)
        + (6 * new_quotient_second)
        * (2 * new_root_second + new_quotient_second)
    )


@dataclass(slots=True)
class ScaledCrossEnergyOrbit:
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
    scaled_cross: int
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
    ) -> "ScaledCrossEnergyOrbit":
        _pos("n", n)
        if step not in (1, 2):
            raise ValueError("step must be 1 or 2")
        m0, m1, m2 = (sample.multiplier for sample in samples)
        if (m1 - m0, m2 - m1) != (8, 8):
            raise ValueError("seed multipliers must be separated by 8")
        if any((sample.multiplier & 7) != (m0 & 7) for sample in samples):
            raise ValueError("seed multipliers must share one residue class")
        if any(outgoing_sparse_step(sample.multiplier) != step for sample in samples):
            raise ValueError("seed residue class has wrong outgoing step")
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
            scaled_cross=6 * (s * u + a * (s + t)),
            energy=e2,
            energy_first=e2 - e1,
            energy_second=e2 - 2 * e1 + e0,
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

        e3 = square_increment_scaled_cross_third_difference(
            target_root=target_root,
            target_quotient=quotient,
            quotient_third=q3,
            root_third=j3,
            scaled_cross=self.scaled_cross,
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
        scaled_cross = next_scaled_cross(
            scaled_cross=self.scaled_cross,
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
        self.scaled_cross = scaled_cross
        self.energy = energy
        self.energy_first = energy_first
        self.energy_second = energy_second
        return quotient, rho, energy, q3, j3, e3


class ScaledCrossEnergyTailScanner:
    """Unbounded exact tail scanner using the scaled cross coordinate C."""

    def __init__(self, n: int, start_multiplier: int | None = None) -> None:
        _pos("n", n)
        if n % 2 == 0:
            raise ValueError("scanner requires odd n")
        threshold = quotient_jet_tail_threshold(n)
        multiplier = threshold if start_multiplier is None else start_multiplier
        _pos("start_multiplier", multiplier)
        if multiplier < threshold or not odd_n_multiplier_is_representative(multiplier):
            raise ValueError("start multiplier is before/outside certified tail")
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
        self._orbits: list[ScaledCrossEnergyOrbit | None] = [None] * 5

    @property
    def active_orbit_count(self) -> int:
        return sum(orbit is not None for orbit in self._orbits)

    def advance_inplace(self) -> None:
        multiplier, root, remainder = self.multiplier, self.root, self.remainder
        index = _RESIDUE_INDEX[multiplier & 7]
        step = outgoing_sparse_step(multiplier)
        orbit = self._orbits[index]
        if orbit is None:
            quotient, rho = divmod(2 * step * root, 4 * multiplier + step)
            energy = quotient * (2 * root + quotient)
            self.seed_divisions += 1
            self.seed_square_increment_products += 1
            samples = self._samples[index]
            samples.append(EnergyJetSeedSample(multiplier, root, quotient, rho, energy))
            if len(samples) == 3:
                self._orbits[index] = ScaledCrossEnergyOrbit.seed(
                    self.n,
                    step,
                    (samples[0], samples[1], samples[2]),
                )
                samples.clear()
            quotient_mode, energy_mode = "SEED_DIVISION", "SEED_PRODUCT"
            q3 = j3 = e3 = 0
        else:
            quotient, rho, energy, q3, j3, e3 = orbit.advance(multiplier, root)
            quotient_mode = "JET_RECURRENCE"
            energy_mode = "SCALED_CROSS_RECURRENCE"
            self.jet_steps += 1

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
        self.multiplier = multiplier + step
        self.root = candidate
        self.remainder = gap


__all__ = [
    "ScaledCrossEnergyOrbit",
    "ScaledCrossEnergyTailScanner",
    "scaled_cross_from_mixed",
    "mixed_from_scaled_cross",
    "square_increment_scaled_cross_third_difference",
    "next_scaled_cross",
    "ENERGY_JET_TOTAL_SEED_DIVISIONS",
    "ENERGY_JET_TOTAL_SEED_PRODUCTS",
]
