"""Exact finite-difference transport of E=q(2J+q) on the BRC tail.

This extends ``t0.brc_quotient_jet_tail``.  Five mod-8 source orbits are
seeded three times each.  After those 15 divisions and 15 direct products,
quotient, quotient remainder, and E are transported exactly with no fresh
division and no multiplication of two N-growing operands.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .brc_linear_deep_tail import odd_n_multiplier_is_representative
from .brc_quotient_jet_tail import (
    QUOTIENT_JET_MAX_ABS_CORRECTION as Q3,
    QUOTIENT_JET_SECOND_DIFFERENCE_MAX as Q2_MAX,
    QUOTIENT_JET_SECOND_DIFFERENCE_MIN as Q2_MIN,
    outgoing_sparse_step,
    quotient_jet_bound_sufficient,
    quotient_jet_tail_threshold,
)

ROOT_JET_THIRD_DIFFERENCE_MIN = -3
ROOT_JET_THIRD_DIFFERENCE_MAX = 387
ENERGY_JET_ORBIT_STRIDE = 8
ENERGY_JET_ORBIT_COUNT = 5
ENERGY_JET_SEEDS_PER_ORBIT = 3
ENERGY_JET_TOTAL_SEED_DIVISIONS = 15
ENERGY_JET_TOTAL_SEED_PRODUCTS = 15
_RESIDUE_INDEX = (0, 1, -1, 2, -1, 3, -1, 4)


def _pos(name: str, x: int) -> None:
    if isinstance(x, bool) or not isinstance(x, int) or x <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _nonneg(name: str, x: int) -> None:
    if isinstance(x, bool) or not isinstance(x, int) or x < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def root_stride_third_difference(n: int, oldest_multiplier: int) -> int:
    _pos("n", n)
    _pos("oldest_multiplier", oldest_multiplier)
    j = [isqrt((oldest_multiplier + 8 * k) * n) for k in range(4)]
    return j[3] - 3 * j[2] + 3 * j[1] - j[0]


def root_third_difference_bound_sufficient(
    n: int, oldest_multiplier: int
) -> bool:
    """``4*m**5>=N`` implies ``-3<=Delta_8**3 floor(sqrt(mN))<=387``."""
    _pos("n", n)
    _pos("oldest_multiplier", oldest_multiplier)
    return 4 * oldest_multiplier**5 >= n


def square_increment_third_difference(
    *,
    root: int,
    quotient: int,
    quotient_first: int,
    quotient_second: int,
    root_first: int,
    root_second: int,
    quotient_third: int,
    root_third: int,
    mixed_first_second: int,
) -> int:
    """Exact third difference of ``E=q*(2*J+q)`` at the new orbit point."""
    return (
        quotient_third
        * (
            2
            * (
                root
                + quotient
                + quotient_first
                + quotient_second
                + root_first
                + root_second
                + root_third
            )
            + quotient_third
        )
        + 2 * root_third * (quotient + quotient_first + quotient_second)
        + 6
        * (
            mixed_first_second
            + quotient_second * (quotient_first + root_first)
        )
    )


@dataclass(frozen=True, slots=True)
class EnergyJetSeedSample:
    multiplier: int
    root: int
    quotient: int
    quotient_remainder: int
    square_increment: int


@dataclass(slots=True)
class EnergyDifferenceJetOrbit:
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
    mixed_q1_j2: int
    energy: int
    energy_first: int
    energy_second: int

    @classmethod
    def seed(
        cls,
        n: int,
        step: int,
        samples: tuple[EnergyJetSeedSample, EnergyJetSeedSample, EnergyJetSeedSample],
    ) -> "EnergyDifferenceJetOrbit":
        _pos("n", n)
        if step not in (1, 2):
            raise ValueError("step must be 1 or 2")
        m0, m1, m2 = (x.multiplier for x in samples)
        if (m1 - m0, m2 - m1) != (8, 8):
            raise ValueError("seed multipliers must be separated by 8")
        if any((x.multiplier & 7) != (m0 & 7) for x in samples):
            raise ValueError("seed multipliers must share a residue class")
        if any(outgoing_sparse_step(x.multiplier) != step for x in samples):
            raise ValueError("seed residue class has the wrong step")
        if not quotient_jet_bound_sufficient(n, m0, step):
            raise ValueError("oldest seed does not certify quotient jet")
        if not root_third_difference_bound_sufficient(n, m0):
            raise ValueError("oldest seed does not certify root jet")
        for x in samples:
            d = 4 * x.multiplier + step
            if not 0 <= x.quotient_remainder < d:
                raise ValueError("seed quotient remainder escaped denominator")
            if x.quotient * d + x.quotient_remainder != 2 * step * x.root:
                raise ValueError("seed quotient/remainder does not reconstruct")
            if x.square_increment != x.quotient * (2 * x.root + x.quotient):
                raise ValueError("seed square increment does not reconstruct")
        q0, q1, q2 = (x.quotient for x in samples)
        j0, j1, j2 = (x.root for x in samples)
        e0, e1, e2 = (x.square_increment for x in samples)
        qs = q2 - q1
        qa = q2 - 2 * q1 + q0
        if not Q2_MIN <= qa <= Q2_MAX:
            raise AssertionError("seed quotient second difference escaped bound")
        jt = j2 - j1
        ju = j2 - 2 * j1 + j0
        ef = e2 - e1
        es = e2 - 2 * e1 + e0
        d2 = 4 * m2 + step
        return cls(
            n,
            step,
            m2,
            j2,
            q2,
            samples[2].quotient_remainder,
            qs,
            qa,
            (qs + qa) * (d2 + 32),
            jt,
            ju,
            qs * ju,
            e2,
            ef,
            es,
        )

    def advance(self, target_multiplier: int, target_root: int) -> tuple[int, ...]:
        if target_multiplier != self.multiplier + 8:
            raise ValueError("target must be the next stride-8 visit")
        d = 4 * target_multiplier + self.step
        q = self.quotient + self.q_first + self.q_second
        rho = (
            self.quotient_remainder
            + 2 * self.step * (target_root - self.root)
            - 32 * self.quotient
            - self.predicted_delta_product
        )
        q3 = 0
        while rho < 0:
            q -= 1
            rho += d
            q3 -= 1
            if q3 < -Q3:
                raise AssertionError("quotient lower repair bound failed")
        while rho >= d:
            q += 1
            rho -= d
            q3 += 1
            if q3 > Q3:
                raise AssertionError("quotient upper repair bound failed")

        j1 = target_root - self.root
        j2 = j1 - self.j_first
        j3 = j2 - self.j_second
        if not ROOT_JET_THIRD_DIFFERENCE_MIN <= j3 <= ROOT_JET_THIRD_DIFFERENCE_MAX:
            raise AssertionError("root third difference escaped proved bound")
        e3 = square_increment_third_difference(
            root=self.root,
            quotient=self.quotient,
            quotient_first=self.q_first,
            quotient_second=self.q_second,
            root_first=self.j_first,
            root_second=self.j_second,
            quotient_third=q3,
            root_third=j3,
            mixed_first_second=self.mixed_q1_j2,
        )
        energy = self.energy + self.energy_first + self.energy_second + e3
        ef = self.energy_first + self.energy_second + e3
        es = self.energy_second + e3
        q1 = self.q_first + self.q_second + q3
        q2 = self.q_second + q3
        if not Q2_MIN <= q2 <= Q2_MAX:
            raise AssertionError("quotient second difference escaped proved bound")
        mixed = (
            self.mixed_q1_j2
            + self.q_first * j3
            + q2 * self.j_second
            + q2 * j3
        )
        pd = (
            self.predicted_delta_product
            + (2 * q2 - self.q_second) * d
            + 32 * (self.q_first + 2 * q2)
        )
        self.multiplier = target_multiplier
        self.root = target_root
        self.quotient = q
        self.quotient_remainder = rho
        self.q_first = q1
        self.q_second = q2
        self.predicted_delta_product = pd
        self.j_first = j1
        self.j_second = j2
        self.mixed_q1_j2 = mixed
        self.energy = energy
        self.energy_first = ef
        self.energy_second = es
        return q, rho, energy, q3, j3, e3


@dataclass(frozen=True, slots=True)
class EnergyDifferenceJetTailStep:
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
        return 0 if self.target_remainder == 0 else 2 * self.target_root + 1 - self.target_remainder


class EnergyDifferenceJetTailScanner:
    """Unbounded odd-N sparse tail; hot path is division/general-product free."""

    def __init__(self, n: int, start_multiplier: int | None = None) -> None:
        _pos("n", n)
        if n % 2 == 0:
            raise ValueError("scanner requires odd n")
        threshold = quotient_jet_tail_threshold(n)
        m = threshold if start_multiplier is None else start_multiplier
        _pos("start_multiplier", m)
        if m < threshold or not odd_n_multiplier_is_representative(m):
            raise ValueError("start_multiplier is before or outside the certified tail")
        target = m * n
        self.n, self.multiplier, self.root = n, m, isqrt(target)
        self.remainder = target - self.root * self.root
        self.seed_divisions = self.seed_square_increment_products = self.jet_steps = 0
        self.last_source_multiplier = m
        self.last_source_root = self.root
        self.last_predictor_quotient = self.last_predictor_quotient_remainder = 0
        self.last_square_increment = 0
        self.last_quotient_mode = self.last_energy_mode = "INITIAL"
        self.last_quotient_third_difference = 0
        self.last_root_third_difference = 0
        self.last_energy_third_difference = 0
        self.last_root_corrections = 0
        self._samples: list[list[EnergyJetSeedSample]] = [[] for _ in range(5)]
        self._orbits: list[EnergyDifferenceJetOrbit | None] = [None] * 5

    @property
    def active_orbit_count(self) -> int:
        return sum(x is not None for x in self._orbits)

    def advance_inplace(self) -> None:
        m, j, r = self.multiplier, self.root, self.remainder
        idx = _RESIDUE_INDEX[m & 7]
        h = outgoing_sparse_step(m)
        orbit = self._orbits[idx]
        if orbit is None:
            q, rho = divmod(2 * h * j, 4 * m + h)
            energy = q * (2 * j + q)
            self.seed_divisions += 1
            self.seed_square_increment_products += 1
            samples = self._samples[idx]
            samples.append(EnergyJetSeedSample(m, j, q, rho, energy))
            if len(samples) == 3:
                self._orbits[idx] = EnergyDifferenceJetOrbit.seed(
                    self.n, h, (samples[0], samples[1], samples[2])
                )
                samples.clear()
            qm, em, q3, j3, e3 = "SEED_DIVISION", "SEED_PRODUCT", 0, 0, 0
        else:
            q, rho, energy, q3, j3, e3 = orbit.advance(m, j)
            qm, em = "JET_RECURRENCE", "DIFFERENCE_JET_RECURRENCE"
            self.jet_steps += 1
        target_m = m + h
        candidate = j + q
        gap = r + h * self.n - energy
        corrections = 0
        while gap >= 2 * candidate + 1:
            gap -= 2 * candidate + 1
            candidate += 1
            corrections += 1
            if corrections > 2:
                raise AssertionError("linear-tail root correction bound failed")
        self.last_source_multiplier, self.last_source_root = m, j
        self.last_predictor_quotient = q
        self.last_predictor_quotient_remainder = rho
        self.last_square_increment = energy
        self.last_quotient_mode, self.last_energy_mode = qm, em
        self.last_quotient_third_difference = q3
        self.last_root_third_difference = j3
        self.last_energy_third_difference = e3
        self.last_root_corrections = corrections
        self.multiplier, self.root, self.remainder = target_m, candidate, gap

    def step(self) -> EnergyDifferenceJetTailStep:
        self.advance_inplace()
        return EnergyDifferenceJetTailStep(
            self.last_source_multiplier,
            self.multiplier,
            self.last_source_root,
            self.root,
            self.remainder,
            self.last_predictor_quotient,
            self.last_predictor_quotient_remainder,
            self.last_square_increment,
            self.last_quotient_mode,
            self.last_energy_mode,
            self.last_quotient_third_difference,
            self.last_root_third_difference,
            self.last_energy_third_difference,
            self.last_root_corrections,
        )

    def run(self, transition_count: int) -> tuple[EnergyDifferenceJetTailStep, ...]:
        _pos("transition_count", transition_count)
        return tuple(self.step() for _ in range(transition_count))


__all__ = [
    "ROOT_JET_THIRD_DIFFERENCE_MIN",
    "ROOT_JET_THIRD_DIFFERENCE_MAX",
    "ENERGY_JET_TOTAL_SEED_DIVISIONS",
    "ENERGY_JET_TOTAL_SEED_PRODUCTS",
    "EnergyJetSeedSample",
    "EnergyDifferenceJetOrbit",
    "EnergyDifferenceJetTailStep",
    "EnergyDifferenceJetTailScanner",
    "root_stride_third_difference",
    "root_third_difference_bound_sufficient",
    "square_increment_third_difference",
]
