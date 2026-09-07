"""Exact quotient/remainder jet for the order-1 linear BRC multiplier tail.

For a fixed odd N and one source residue class r modulo 8, the outgoing sparse
step h is fixed and the exact order-1 predictor quotient is

    q(m) = floor(2*h*J(m) / (4*m+h)),  J(m)=floor(sqrt(m*N)).

Successive occurrences of the same residue class are eight multipliers apart.
After three exact seed divisions, retain q together with its first and second
stride-8 differences and the exact division remainder.  Quadratic extrapolation

    q_hat(m+8) = 3*q(m) - 3*q(m-8) + q(m-16)

is then corrected by a bounded signed epsilon.  On the certified linear tail,
|epsilon| <= 4.  An exact residual transport identity obtains epsilon using
only a handful of additions/subtractions of the new linear denominator; no
new full numerator/denominator division is needed.

This is an extension of t0.brc_linear_deep_tail.  It preserves the exact
quotient remainder as a repair/provenance coordinate and composes with the
existing square-gap residue cascade.  It does not shorten a factor-search
horizon or introduce a new factoring principle.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .brc_linear_deep_tail import (
    common_mod8_linear_tail_sufficient,
    common_mod8_linear_tail_threshold,
    odd_n_multiplier_is_representative,
)

QUOTIENT_ORBIT_STRIDE = 8
QUOTIENT_JET_PHASE_FACTOR = 962
QUOTIENT_JET_UNIFORM_MIN_MULTIPLIER = 2 * QUOTIENT_JET_PHASE_FACTOR
QUOTIENT_JET_MAX_ABS_CORRECTION = 4
QUOTIENT_JET_SECOND_DIFFERENCE_MIN = -2
QUOTIENT_JET_SECOND_DIFFERENCE_MAX = 98

_RESIDUE_INDEX = (0, 1, -1, 2, -1, 3, -1, 4)
_OUTGOING_STEP = (1, 2, 2, 2, 1)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def outgoing_sparse_step(multiplier: int) -> int:
    """Return the exact odd-N representative step h in {1,2} from multiplier."""
    _require_positive("multiplier", multiplier)
    if not odd_n_multiplier_is_representative(multiplier):
        raise ValueError("multiplier must be an odd-N mod-8 representative")
    return _OUTGOING_STEP[_RESIDUE_INDEX[multiplier & 7]]


def quotient_jet_bound_sufficient(
    n: int,
    oldest_multiplier: int,
    step: int,
) -> bool:
    """Root-free certificate for the stride-8 quotient-jet correction bound.

    The proof combines the existing common linear-tail condition 4*m^5>=N
    with m>=962*h.  For

        F_h(m)=2*h*sqrt(m*N)/(4*m+h),

    these conditions imply -1 < Delta_8^3 F_h < 0.  Since the exact integer
    quotient differs from F_h by a phase in [0, 1+2h/(4m+h)), the resulting
    integer third difference lies in [-4,4].
    """
    _require_positive("n", n)
    _require_positive("oldest_multiplier", oldest_multiplier)
    _require_positive("step", step)
    if step not in (1, 2):
        return False
    return (
        common_mod8_linear_tail_sufficient(n, oldest_multiplier)
        and oldest_multiplier >= QUOTIENT_JET_PHASE_FACTOR * step
    )


def quotient_jet_tail_threshold(n: int) -> int:
    """First representative multiplier supporting every quotient-jet orbit.

    The common linear tail controls the root predictor.  The fixed 1924 guard
    simultaneously certifies the worst h=2 quotient orbit.  Starting here,
    the first three visits to every residue class seed five exact quotient
    orbits; every later visit is division-free.
    """
    _require_positive("n", n)
    m = max(
        common_mod8_linear_tail_threshold(n),
        QUOTIENT_JET_UNIFORM_MIN_MULTIPLIER,
    )
    while not odd_n_multiplier_is_representative(m):
        m += 1
    return m


@dataclass(slots=True)
class QuotientJetOrbit:
    """Exact quotient/remainder jet for one fixed mod-8 source class."""

    n: int
    step: int
    multiplier: int
    root: int
    quotient: int
    quotient_remainder: int
    first_difference: int
    second_difference: int
    predicted_delta_times_next_denominator: int
    max_abs_correction_seen: int = 0

    @classmethod
    def seed(
        cls,
        n: int,
        step: int,
        samples: tuple[tuple[int, int], tuple[int, int], tuple[int, int]],
    ) -> "QuotientJetOrbit":
        """Seed one orbit from three exact roots at m,m+8,m+16."""
        _require_positive("n", n)
        _require_positive("step", step)
        if step not in (1, 2):
            raise ValueError("step must be 1 or 2")
        multipliers = tuple(sample[0] for sample in samples)
        roots = tuple(sample[1] for sample in samples)
        if multipliers[1] - multipliers[0] != QUOTIENT_ORBIT_STRIDE:
            raise ValueError("seed multipliers must be separated by 8")
        if multipliers[2] - multipliers[1] != QUOTIENT_ORBIT_STRIDE:
            raise ValueError("seed multipliers must be separated by 8")
        residue = multipliers[0] & 7
        if any((m & 7) != residue for m in multipliers):
            raise ValueError("seed multipliers must share one residue class")
        if any(outgoing_sparse_step(m) != step for m in multipliers):
            raise ValueError("seed residue class does not have the declared step")
        if not quotient_jet_bound_sufficient(n, multipliers[0], step):
            raise ValueError("oldest seed multiplier does not certify the jet bound")

        quotient_data: list[tuple[int, int]] = []
        for m, root in samples:
            if isinstance(root, bool) or not isinstance(root, int) or root < 0:
                raise ValueError("seed roots must be non-negative integers")
            target = m * n
            if root * root > target or (root + 1) * (root + 1) <= target:
                raise ValueError("seed root is not floor(sqrt(m*n))")
            quotient_data.append(divmod(2 * step * root, 4 * m + step))

        q0 = quotient_data[0][0]
        q1 = quotient_data[1][0]
        q2, rho2 = quotient_data[2]
        first = q2 - q1
        second = q2 - 2 * q1 + q0
        if not (
            QUOTIENT_JET_SECOND_DIFFERENCE_MIN
            <= second
            <= QUOTIENT_JET_SECOND_DIFFERENCE_MAX
        ):
            raise AssertionError("seed second difference escaped the proved tail bound")
        last_m = multipliers[2]
        last_denominator = 4 * last_m + step
        next_delta = first + second
        return cls(
            n=n,
            step=step,
            multiplier=last_m,
            root=roots[2],
            quotient=q2,
            quotient_remainder=rho2,
            first_difference=first,
            second_difference=second,
            predicted_delta_times_next_denominator=(
                next_delta * (last_denominator + 32)
            ),
        )

    def advance(self, target_multiplier: int, target_root: int) -> int:
        """Advance in place by one stride-8 visit and return signed epsilon.

        The stored product is

            (first_difference + second_difference) * D_next.

        This lets the provisional division residual be transported without a
        full-width quotient*denominator multiplication.  The exact epsilon is
        found by at most four additions/subtractions of D_next.
        """
        _require_positive("target_multiplier", target_multiplier)
        if target_multiplier != self.multiplier + QUOTIENT_ORBIT_STRIDE:
            raise ValueError("target multiplier must be the next same-residue visit")
        if (
            isinstance(target_root, bool)
            or not isinstance(target_root, int)
            or target_root < 0
        ):
            raise ValueError("target_root must be a non-negative integer")

        denominator = 4 * target_multiplier + self.step
        predicted_delta = self.first_difference + self.second_difference
        q = self.quotient + predicted_delta

        # Let D'=D+32.  From 2hJ=qD+rho and q_hat=q+v+a:
        #
        # 2hJ' - q_hat D'
        #   = rho + 2h(J'-J) - 32q - (v+a)D'.
        #
        # The last product is carried from the previous orbit state.
        residual = (
            self.quotient_remainder
            + 2 * self.step * (target_root - self.root)
            - 32 * self.quotient
            - self.predicted_delta_times_next_denominator
        )

        epsilon = 0
        while residual < 0:
            q -= 1
            residual += denominator
            epsilon -= 1
            if epsilon < -QUOTIENT_JET_MAX_ABS_CORRECTION:
                raise AssertionError("quotient-jet lower correction bound failed")
        while residual >= denominator:
            q += 1
            residual -= denominator
            epsilon += 1
            if epsilon > QUOTIENT_JET_MAX_ABS_CORRECTION:
                raise AssertionError("quotient-jet upper correction bound failed")

        new_first = self.first_difference + self.second_difference + epsilon
        new_second = self.second_difference + epsilon
        if not (
            QUOTIENT_JET_SECOND_DIFFERENCE_MIN
            <= new_second
            <= QUOTIENT_JET_SECOND_DIFFERENCE_MAX
        ):
            raise AssertionError("second difference escaped the proved tail bound")

        # P'=(v'+a')*(D'+32), from P=(v+a)D':
        #
        # P' = P + (2a'-a)D' + 32(v+2a').
        new_product = (
            self.predicted_delta_times_next_denominator
            + (2 * new_second - self.second_difference) * denominator
            + 32 * (self.first_difference + 2 * new_second)
        )

        self.multiplier = target_multiplier
        self.root = target_root
        self.quotient = q
        self.quotient_remainder = residual
        self.first_difference = new_first
        self.second_difference = new_second
        self.predicted_delta_times_next_denominator = new_product
        if abs(epsilon) > self.max_abs_correction_seen:
            self.max_abs_correction_seen = abs(epsilon)
        return epsilon


@dataclass(frozen=True, slots=True)
class QuotientJetTailStep:
    n: int
    source_multiplier: int
    target_multiplier: int
    source_root: int
    target_root: int
    target_remainder: int
    predictor_quotient: int
    predictor_quotient_remainder: int
    quotient_mode: str
    quotient_correction: int
    root_corrections: int

    @property
    def ceiling_completion_gap(self) -> int:
        if self.target_remainder == 0:
            return 0
        return 2 * self.target_root + 1 - self.target_remainder


class QuotientJetTailScanner:
    """Unbounded odd-N linear-tail scanner with only 15 seed divisions."""

    __slots__ = (
        "n",
        "multiplier",
        "root",
        "remainder",
        "seed_divisions",
        "jet_steps",
        "max_abs_quotient_correction",
        "last_source_multiplier",
        "last_source_root",
        "last_predictor_quotient",
        "last_predictor_quotient_remainder",
        "last_quotient_mode",
        "last_quotient_correction",
        "last_root_corrections",
        "_samples",
        "_orbits",
    )

    def __init__(self, n: int, start_multiplier: int | None = None) -> None:
        _require_positive("n", n)
        if n % 2 == 0:
            raise ValueError("quotient-jet sparse tail requires odd n")
        threshold = quotient_jet_tail_threshold(n)
        if start_multiplier is None:
            start_multiplier = threshold
        _require_positive("start_multiplier", start_multiplier)
        if start_multiplier < threshold:
            raise ValueError("start_multiplier is before the certified jet tail")
        if not odd_n_multiplier_is_representative(start_multiplier):
            raise ValueError("start_multiplier must be a mod-8 representative")

        target = start_multiplier * n
        root = isqrt(target)
        self.n = n
        self.multiplier = start_multiplier
        self.root = root
        self.remainder = target - root * root
        self.seed_divisions = 0
        self.jet_steps = 0
        self.max_abs_quotient_correction = 0
        self.last_source_multiplier = start_multiplier
        self.last_source_root = root
        self.last_predictor_quotient = 0
        self.last_predictor_quotient_remainder = 0
        self.last_quotient_mode = "INITIAL"
        self.last_quotient_correction = 0
        self.last_root_corrections = 0
        self._samples: list[list[tuple[int, int]]] = [[] for _ in range(5)]
        self._orbits: list[QuotientJetOrbit | None] = [None] * 5

    @property
    def active_orbit_count(self) -> int:
        """Number of residue-class jets already seeded (0 through 5)."""
        return sum(orbit is not None for orbit in self._orbits)

    @property
    def quotient_second_differences(self) -> tuple[int, ...]:
        """Current exact stride-8 second differences for active jets."""
        return tuple(
            orbit.second_difference
            for orbit in self._orbits
            if orbit is not None
        )

    def advance_inplace(self) -> None:
        """Advance one sparse transition without allocating a result object.

        The exact result is written to ``multiplier/root/remainder`` and the
        diagnostic fields prefixed by ``last_``.  This is the hot-path API for
        long scans; :meth:`step` wraps it with a frozen result record.
        """
        source_m = self.multiplier
        source_root = self.root
        source_remainder = self.remainder
        index = _RESIDUE_INDEX[source_m & 7]
        step = _OUTGOING_STEP[index]
        denominator = 4 * source_m + step
        orbit = self._orbits[index]

        if orbit is None:
            quotient, quotient_remainder = divmod(
                2 * step * source_root, denominator
            )
            samples = self._samples[index]
            samples.append((source_m, source_root))
            self.seed_divisions += 1
            if len(samples) == 3:
                self._orbits[index] = QuotientJetOrbit.seed(
                    self.n,
                    step,
                    (samples[0], samples[1], samples[2]),
                )
                samples.clear()
            mode = "SEED_DIVISION"
            epsilon = 0
        else:
            epsilon = orbit.advance(source_m, source_root)
            quotient = orbit.quotient
            quotient_remainder = orbit.quotient_remainder
            mode = "JET_RECURRENCE"
            self.jet_steps += 1
            abs_epsilon = abs(epsilon)
            if abs_epsilon > self.max_abs_quotient_correction:
                self.max_abs_quotient_correction = abs_epsilon

        target_m = source_m + step
        candidate = source_root + quotient
        gap = (
            source_remainder
            + step * self.n
            - quotient * (2 * source_root + quotient)
        )
        corrections = 0
        odd_width = 2 * candidate + 1
        while gap >= odd_width:
            gap -= odd_width
            candidate += 1
            corrections += 1
            if corrections > 2:
                raise AssertionError(
                    "order-1 linear-tail correction bound failed"
                )
            odd_width += 2

        self.last_source_multiplier = source_m
        self.last_source_root = source_root
        self.last_predictor_quotient = quotient
        self.last_predictor_quotient_remainder = quotient_remainder
        self.last_quotient_mode = mode
        self.last_quotient_correction = epsilon
        self.last_root_corrections = corrections
        self.multiplier = target_m
        self.root = candidate
        self.remainder = gap

    def step(self) -> QuotientJetTailStep:
        self.advance_inplace()
        return QuotientJetTailStep(
            n=self.n,
            source_multiplier=self.last_source_multiplier,
            target_multiplier=self.multiplier,
            source_root=self.last_source_root,
            target_root=self.root,
            target_remainder=self.remainder,
            predictor_quotient=self.last_predictor_quotient,
            predictor_quotient_remainder=(
                self.last_predictor_quotient_remainder
            ),
            quotient_mode=self.last_quotient_mode,
            quotient_correction=self.last_quotient_correction,
            root_corrections=self.last_root_corrections,
        )

    def run(self, transition_count: int) -> tuple[QuotientJetTailStep, ...]:
        _require_positive("transition_count", transition_count)
        return tuple(self.step() for _ in range(transition_count))


__all__ = [
    "QUOTIENT_ORBIT_STRIDE",
    "QUOTIENT_JET_PHASE_FACTOR",
    "QUOTIENT_JET_UNIFORM_MIN_MULTIPLIER",
    "QUOTIENT_JET_MAX_ABS_CORRECTION",
    "QUOTIENT_JET_SECOND_DIFFERENCE_MIN",
    "QUOTIENT_JET_SECOND_DIFFERENCE_MAX",
    "QuotientJetOrbit",
    "QuotientJetTailStep",
    "QuotientJetTailScanner",
    "outgoing_sparse_step",
    "quotient_jet_bound_sufficient",
    "quotient_jet_tail_threshold",
]
