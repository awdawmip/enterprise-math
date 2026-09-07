"""Exact residue transport for the BRC completion-gap table cascade.

The square-increment difference jet already transports exact root/remainder
states without fresh roots, divisions, or products of two N-growing operands.
The remaining BALANCED square-gap filter traditionally evaluates

    F_m = 0                              if R_m == 0
          (J_m + 1)^2 - m*N             otherwise

with three full big-integer modulo operations.

On each fixed source class modulo eight, J_m is sampled with stride eight and
its exact third difference is emitted by the parent energy jet. Reduction
modulo a fixed product commutes with that difference recurrence. After three
root-residue seeds on each of the five source classes, J_m modulo the selected
cascade-stage product is transported using only word-size arithmetic.

The default COMPACT profile transports the first two stages (4032, 12155) in
one modulus 49,008,960. Only their exact CRT survivors materialize F_m and pay
the final big-integer reduction modulo 12673. The filter remains a necessary
square condition and therefore has zero false negatives.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt, prod

from .brc_energy_difference_jet_tail import EnergyDifferenceJetTailScanner
from .brc_quotient_jet_tail import outgoing_sparse_step
from .brc_square_gap_cascade import CASCADE_STAGE_MODULI, cascade_table

ROOT_RESIDUE_ORBIT_STRIDE = 8
ROOT_RESIDUE_ORBIT_COUNT = 5
ROOT_RESIDUE_SEEDS_PER_ORBIT = 3
ROOT_RESIDUE_TOTAL_SEED_REDUCTIONS = 15
INITIAL_FULL_WIDTH_REDUCTIONS = 2

TRANSPORTED_CASCADE_PROFILES: dict[str, tuple[int, ...]] = {
    "PRIMARY": (4032,),
    "COMPACT": (4032, 12155),
    "FULL": (4032, 12155, 12673),
}

_RESIDUE_INDEX = (0, 1, -1, 2, -1, 3, -1, 4)


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _profile_moduli(profile: str) -> tuple[int, ...]:
    try:
        return TRANSPORTED_CASCADE_PROFILES[profile.upper()]
    except (AttributeError, KeyError) as exc:
        raise ValueError(
            f"unknown transported cascade profile {profile!r}"
        ) from exc


def transported_cascade_modulus(profile: str = "COMPACT") -> int:
    """Return the product modulus transported by one registered profile."""
    return prod(_profile_moduli(profile))


def _passes_residue(residue: int, modulus: int) -> bool:
    table = cascade_table(modulus)
    residue %= modulus
    return bool(table[residue >> 3] & (1 << (residue & 7)))


@dataclass(slots=True)
class RootResidueDifferenceOrbit:
    """Exact stride-eight root-residue jet modulo one fixed product."""

    modulus: int
    multiplier: int
    root_residue: int
    first_difference: int
    second_difference: int

    @classmethod
    def seed(
        cls,
        modulus: int,
        samples: tuple[
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
        ],
    ) -> "RootResidueDifferenceOrbit":
        _positive("modulus", modulus)
        m0, m1, m2 = (sample[0] for sample in samples)
        if (m1 - m0, m2 - m1) != (
            ROOT_RESIDUE_ORBIT_STRIDE,
            ROOT_RESIDUE_ORBIT_STRIDE,
        ):
            raise ValueError("root-residue seeds must be separated by eight")
        if not ((m0 & 7) == (m1 & 7) == (m2 & 7)):
            raise ValueError(
                "root-residue seeds must share one source residue class"
            )

        r0, r1, r2 = (sample[1] % modulus for sample in samples)
        return cls(
            modulus=modulus,
            multiplier=m2,
            root_residue=r2,
            first_difference=(r2 - r1) % modulus,
            second_difference=(r2 - 2 * r1 + r0) % modulus,
        )

    def advance(
        self,
        target_multiplier: int,
        root_third_difference: int,
    ) -> int:
        """Advance one source-orbit visit by its exact third difference."""
        if target_multiplier != self.multiplier + ROOT_RESIDUE_ORBIT_STRIDE:
            raise ValueError(
                "target multiplier must be the next stride-eight source visit"
            )

        modulus = self.modulus
        third = root_third_difference % modulus
        new_residue = (
            self.root_residue
            + self.first_difference
            + self.second_difference
            + third
        ) % modulus
        new_first = (
            self.first_difference + self.second_difference + third
        ) % modulus
        new_second = (self.second_difference + third) % modulus

        self.multiplier = target_multiplier
        self.root_residue = new_residue
        self.first_difference = new_first
        self.second_difference = new_second
        return new_residue


@dataclass(frozen=True, slots=True)
class GapResidueJetTailStep:
    source_multiplier: int
    target_multiplier: int
    source_root: int
    source_remainder: int
    transported_profile: str
    transported_modulus: int
    root_residue: int
    completion_gap_residue: int
    root_residue_mode: str
    root_third_difference: int
    transported_stages_passed: bool
    cascade_passed: bool
    exact_gap: int | None
    exact_square: bool | None

    @property
    def exact_gap_was_materialized(self) -> bool:
        return self.exact_gap is not None


class GapResidueJetTailScanner:
    """Energy-jet tail plus transported square-gap table residues.

    ``advance_filter_inplace`` is the hot path. It advances the parent root
    state once and stores the table verdict for the consumed source state in
    ``last_*`` fields. ``step`` allocates a frozen result only when requested.

    Reporting is delayed by one root transition because the parent energy jet
    emits the exact stride-eight third difference for the source it just used.
    This changes only the endpoint convention of a finite scan.
    """

    __slots__ = (
        "energy",
        "n",
        "transported_profile",
        "transported_moduli",
        "remaining_moduli",
        "modulus",
        "n_residue",
        "target_residue",
        "initial_full_width_reductions",
        "root_seed_mod_reductions",
        "root_residue_jet_steps",
        "exact_gap_materializations",
        "native_big_mod_reductions",
        "exact_square_tests",
        "cascade_survivors",
        "_samples",
        "_orbits",
        "_table_4032",
        "_table_12155",
        "_table_12673",
        "last_source_multiplier",
        "last_source_root",
        "last_source_remainder",
        "last_root_residue",
        "last_completion_gap_residue",
        "last_root_residue_mode",
        "last_root_third_difference",
        "last_transported_stages_passed",
        "last_cascade_passed",
        "last_exact_gap",
        "last_exact_square",
    )

    def __init__(
        self,
        n: int,
        start_multiplier: int | None = None,
        *,
        transported_profile: str = "COMPACT",
    ) -> None:
        _positive("n", n)
        profile = transported_profile.upper()
        moduli = _profile_moduli(profile)

        self.energy = EnergyDifferenceJetTailScanner(n, start_multiplier)
        self.n = n
        self.transported_profile = profile
        self.transported_moduli = moduli
        self.remaining_moduli = tuple(
            modulus
            for modulus in CASCADE_STAGE_MODULI
            if modulus not in moduli
        )
        self.modulus = prod(moduli)

        # Two one-time full-width reductions seed m*N modulo the product.
        self.n_residue = n % self.modulus
        start_residue = self.energy.multiplier % self.modulus
        self.target_residue = (start_residue * self.n_residue) % self.modulus
        self.initial_full_width_reductions = INITIAL_FULL_WIDTH_REDUCTIONS

        self.root_seed_mod_reductions = 0
        self.root_residue_jet_steps = 0
        self.exact_gap_materializations = 0
        self.native_big_mod_reductions = 0
        self.exact_square_tests = 0
        self.cascade_survivors = 0

        self._samples: list[list[tuple[int, int]]] = [
            [] for _ in range(ROOT_RESIDUE_ORBIT_COUNT)
        ]
        self._orbits: list[RootResidueDifferenceOrbit | None] = [
            None for _ in range(ROOT_RESIDUE_ORBIT_COUNT)
        ]
        self._table_4032 = cascade_table(4032)
        self._table_12155 = cascade_table(12155)
        self._table_12673 = cascade_table(12673)

        self.last_source_multiplier = self.energy.multiplier
        self.last_source_root = self.energy.root
        self.last_source_remainder = self.energy.remainder
        self.last_root_residue = 0
        self.last_completion_gap_residue = 0
        self.last_root_residue_mode = "INITIAL"
        self.last_root_third_difference = 0
        self.last_transported_stages_passed = False
        self.last_cascade_passed = False
        self.last_exact_gap: int | None = None
        self.last_exact_square: bool | None = None

    @property
    def multiplier(self) -> int:
        return self.energy.multiplier

    @property
    def root(self) -> int:
        return self.energy.root

    @property
    def remainder(self) -> int:
        return self.energy.remainder

    @property
    def active_root_residue_orbit_count(self) -> int:
        return sum(orbit is not None for orbit in self._orbits)

    def _source_root_residue(
        self,
        source_multiplier: int,
        source_root: int,
        root_third_difference: int,
    ) -> tuple[int, str]:
        index = _RESIDUE_INDEX[source_multiplier & 7]
        if index < 0:
            raise AssertionError(
                "source multiplier left the mod-eight representative set"
            )

        orbit = self._orbits[index]
        if orbit is None:
            residue = source_root % self.modulus
            self.root_seed_mod_reductions += 1
            samples = self._samples[index]
            samples.append((source_multiplier, residue))
            if len(samples) == ROOT_RESIDUE_SEEDS_PER_ORBIT:
                self._orbits[index] = RootResidueDifferenceOrbit.seed(
                    self.modulus,
                    (samples[0], samples[1], samples[2]),
                )
                samples.clear()
            return residue, "SEED_ROOT_MOD"

        self.root_residue_jet_steps += 1
        return (
            orbit.advance(source_multiplier, root_third_difference),
            "ROOT_RESIDUE_JET",
        )

    @staticmethod
    def _bit(table: bytes, residue: int) -> bool:
        return bool(table[residue >> 3] & (1 << (residue & 7)))

    @staticmethod
    def _exact_completion_gap(root: int, remainder: int) -> int:
        return 0 if remainder == 0 else 2 * root + 1 - remainder

    def _transported_stages_pass(self, gap_residue: int) -> bool:
        profile = self.transported_profile
        passed = self._bit(self._table_4032, gap_residue % 4032)
        if not passed or profile == "PRIMARY":
            return passed

        passed = self._bit(self._table_12155, gap_residue % 12155)
        if not passed or profile == "COMPACT":
            return passed

        return self._bit(self._table_12673, gap_residue % 12673)

    def advance_filter_inplace(
        self,
        *,
        check_exact_square: bool = True,
    ) -> bool:
        """Advance once, filter the consumed source, and return its verdict."""
        source_multiplier = self.energy.multiplier
        source_root = self.energy.root
        source_remainder = self.energy.remainder
        source_target_residue = self.target_residue
        step = outgoing_sparse_step(source_multiplier)

        self.energy.advance_inplace()
        if (
            self.energy.last_source_multiplier != source_multiplier
            or self.energy.last_source_root != source_root
        ):
            raise AssertionError("parent energy-jet source bookkeeping drifted")

        root_residue, mode = self._source_root_residue(
            source_multiplier,
            source_root,
            self.energy.last_root_third_difference,
        )
        if source_remainder == 0:
            gap_residue = 0
        else:
            next_root_residue = root_residue + 1
            gap_residue = (
                next_root_residue * next_root_residue
                - source_target_residue
            ) % self.modulus

        transported_passed = self._transported_stages_pass(gap_residue)
        exact_gap: int | None = None
        cascade_passed = transported_passed

        if transported_passed and self.remaining_moduli:
            exact_gap = self._exact_completion_gap(
                source_root,
                source_remainder,
            )
            self.exact_gap_materializations += 1
            for modulus in self.remaining_moduli:
                self.native_big_mod_reductions += 1
                residue = exact_gap % modulus
                table = (
                    self._table_12155
                    if modulus == 12155
                    else self._table_12673
                )
                if not self._bit(table, residue):
                    cascade_passed = False
                    break

        exact_square: bool | None = None
        if cascade_passed:
            self.cascade_survivors += 1
            if check_exact_square:
                if exact_gap is None:
                    exact_gap = self._exact_completion_gap(
                        source_root,
                        source_remainder,
                    )
                    self.exact_gap_materializations += 1
                gap_root = isqrt(exact_gap)
                self.exact_square_tests += 1
                exact_square = gap_root * gap_root == exact_gap

        self.target_residue = (
            source_target_residue + step * self.n_residue
        ) % self.modulus
        if self.energy.multiplier != source_multiplier + step:
            raise AssertionError("parent energy-jet multiplier drifted")

        self.last_source_multiplier = source_multiplier
        self.last_source_root = source_root
        self.last_source_remainder = source_remainder
        self.last_root_residue = root_residue
        self.last_completion_gap_residue = gap_residue
        self.last_root_residue_mode = mode
        self.last_root_third_difference = (
            self.energy.last_root_third_difference
        )
        self.last_transported_stages_passed = transported_passed
        self.last_cascade_passed = cascade_passed
        self.last_exact_gap = exact_gap
        self.last_exact_square = exact_square
        return cascade_passed

    def step(
        self,
        *,
        check_exact_square: bool = True,
    ) -> GapResidueJetTailStep:
        self.advance_filter_inplace(check_exact_square=check_exact_square)
        return GapResidueJetTailStep(
            source_multiplier=self.last_source_multiplier,
            target_multiplier=self.energy.multiplier,
            source_root=self.last_source_root,
            source_remainder=self.last_source_remainder,
            transported_profile=self.transported_profile,
            transported_modulus=self.modulus,
            root_residue=self.last_root_residue,
            completion_gap_residue=self.last_completion_gap_residue,
            root_residue_mode=self.last_root_residue_mode,
            root_third_difference=self.last_root_third_difference,
            transported_stages_passed=(
                self.last_transported_stages_passed
            ),
            cascade_passed=self.last_cascade_passed,
            exact_gap=self.last_exact_gap,
            exact_square=self.last_exact_square,
        )

    def advance_and_filter_source(
        self,
        *,
        check_exact_square: bool = True,
    ) -> GapResidueJetTailStep:
        """Allocated alias for :meth:`step` with explicit source semantics."""
        return self.step(check_exact_square=check_exact_square)

    def run(
        self,
        transition_count: int,
        *,
        check_exact_square: bool = True,
    ) -> tuple[GapResidueJetTailStep, ...]:
        _positive("transition_count", transition_count)
        return tuple(
            self.step(check_exact_square=check_exact_square)
            for _ in range(transition_count)
        )


__all__ = [
    "ROOT_RESIDUE_ORBIT_STRIDE",
    "ROOT_RESIDUE_ORBIT_COUNT",
    "ROOT_RESIDUE_SEEDS_PER_ORBIT",
    "ROOT_RESIDUE_TOTAL_SEED_REDUCTIONS",
    "INITIAL_FULL_WIDTH_REDUCTIONS",
    "TRANSPORTED_CASCADE_PROFILES",
    "RootResidueDifferenceOrbit",
    "GapResidueJetTailStep",
    "GapResidueJetTailScanner",
    "transported_cascade_modulus",
]
