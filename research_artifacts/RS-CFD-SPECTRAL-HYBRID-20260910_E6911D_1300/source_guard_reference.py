"""Reference Source-support guard for the spectralDNS static-carrier research route.

This is a bounded, host-independent reference contract. It does not replace
spectralDNS. It formalizes when a previously certified sparse carrier may be
used in the presence of the host ``Source`` term and when the current RK stage
must be replayed through the unchanged dense RHS.

Key invariants
--------------
* Exact mode defines support by coefficient != 0. No thresholding is allowed.
* A static Source contract declares a support set, not frozen coefficients.
  Values may change arbitrarily inside the declared support.
* A dynamic support escape is detected before the stage result is committed.
  The sparse result is discarded, that same stage is replayed densely from the
  same stage input, and dense mode is sticky thereafter.
* Full complex coefficients are passed through unchanged.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Mapping, TypeVar

Vec = tuple[int, int, int]
CoeffMap = Mapping[Vec, complex]
StateT = TypeVar("StateT")
RhsT = TypeVar("RhsT")


def _vec(v: Iterable[int]) -> Vec:
    x = tuple(int(a) for a in v)
    if len(x) != 3:
        raise ValueError("wavevector must have exactly three integer coordinates")
    return x  # type: ignore[return-value]


def exact_support(coefficients: CoeffMap) -> frozenset[Vec]:
    """Return exact nonzero support; every nonzero complex coefficient counts."""
    return frozenset(_vec(k) for k, value in coefficients.items() if complex(value) != 0j)


def approximate_support(coefficients: CoeffMap, tolerance: float) -> frozenset[Vec]:
    """Explicit opt-in approximate support; never an exact-equivalence certificate."""
    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative")
    return frozenset(_vec(k) for k, value in coefficients.items() if abs(complex(value)) > tolerance)


@dataclass(frozen=True)
class SourceInspection:
    support: frozenset[Vec]
    escape: frozenset[Vec]
    exact: bool
    tolerance: float | None

    @property
    def safe(self) -> bool:
        return not self.escape


def inspect_source(source: CoeffMap, carrier: Iterable[Vec], *, tolerance: float | None = None) -> SourceInspection:
    """Compare current Source support with a certified carrier.

    ``tolerance=None`` is the only exact mode. Supplying a tolerance explicitly
    changes the semantics to an approximation and is reported in the result.
    """
    C = frozenset(_vec(v) for v in carrier)
    if tolerance is None:
        S = exact_support(source)
        exact = True
    else:
        S = approximate_support(source, tolerance)
        exact = False
    return SourceInspection(S, frozenset(S - C), exact, tolerance)


@dataclass(frozen=True)
class StaticSourceSupportContract:
    """Declared support envelope for a time/stage-varying Source."""

    declared_support: frozenset[Vec]

    @classmethod
    def from_labels(cls, labels: Iterable[Vec]) -> "StaticSourceSupportContract":
        return cls(frozenset(_vec(v) for v in labels))

    def validate(self, source: CoeffMap) -> SourceInspection:
        S = exact_support(source)
        escape = frozenset(S - self.declared_support)
        return SourceInspection(S, escape, True, None)

    def seed(self, initial_state_support: Iterable[Vec]) -> frozenset[Vec]:
        """Carrier closure must be seeded by initial state support union this envelope."""
        return frozenset(_vec(v) for v in initial_state_support) | self.declared_support


@dataclass
class StickyDenseSourceGuard:
    """Dynamic exact guard implementing atomic pre-commit dense replay.

    Once a Source label escapes the certified carrier, ``dense_sticky`` becomes
    true. The caller must discard any sparse RHS already computed for that stage
    and evaluate the same stage input using the unchanged dense RHS. All later
    stages are dense. This deliberately avoids trying to re-close/restart the
    carrier mid-step.
    """

    carrier: frozenset[Vec]
    dense_sticky: bool = False
    first_escape_stage: int | None = None
    first_escape: frozenset[Vec] = frozenset()

    @classmethod
    def from_carrier(cls, carrier: Iterable[Vec]) -> "StickyDenseSourceGuard":
        return cls(frozenset(_vec(v) for v in carrier))

    def inspect_before_commit(self, source: CoeffMap, *, stage: int) -> SourceInspection:
        inspection = inspect_source(source, self.carrier)
        if inspection.escape and not self.dense_sticky:
            self.dense_sticky = True
            self.first_escape_stage = int(stage)
            self.first_escape = inspection.escape
        return inspection


def guarded_stage_rhs(*, stage: int, stage_state: StateT, source: CoeffMap,
                      sparse_rhs: Callable[[StateT, CoeffMap], RhsT],
                      dense_rhs: Callable[[StateT, CoeffMap], RhsT],
                      guard: StickyDenseSourceGuard) -> tuple[RhsT, str, SourceInspection]:
    """Evaluate one stage under the atomic fallback contract.

    If the route was sparse before this call, an implementation may have already
    computed a speculative sparse RHS. The Source inspection occurs before that
    stage is committed. An escape makes the sparse result unusable and forces a
    dense replay from ``stage_state``. This reference checks first, which is
    equivalent but avoids doing disposable work.
    """
    inspection = guard.inspect_before_commit(source, stage=stage)
    if guard.dense_sticky:
        return dense_rhs(stage_state, source), "DENSE", inspection
    return sparse_rhs(stage_state, source), "SPARSE", inspection


def _add_scaled_state(y: CoeffMap, k: CoeffMap, a: float) -> dict[Vec, complex]:
    out: dict[Vec, complex] = {p: complex(v) for p, v in y.items()}
    for p, v in k.items():
        out[p] = out.get(p, 0j) + a * complex(v)
        if out[p] == 0j:
            del out[p]
    return out


def _rk4_combine(y: CoeffMap, h: float, ks: list[CoeffMap]) -> dict[Vec, complex]:
    weights = (1.0, 2.0, 2.0, 1.0)
    out: dict[Vec, complex] = {p: complex(v) for p, v in y.items()}
    acc: dict[Vec, complex] = {}
    for w, k in zip(weights, ks):
        for p, v in k.items():
            acc[p] = acc.get(p, 0j) + w * complex(v)
    for p, v in acc.items():
        out[p] = out.get(p, 0j) + h * v / 6.0
        if out[p] == 0j:
            del out[p]
    return out


def guarded_rk4_step(y0: CoeffMap, h: float, *,
                     source_for_stage: Callable[[int, CoeffMap], CoeffMap],
                     sparse_rhs: Callable[[CoeffMap, CoeffMap], CoeffMap],
                     dense_rhs: Callable[[CoeffMap, CoeffMap], CoeffMap],
                     guard: StickyDenseSourceGuard) -> tuple[dict[Vec, complex], tuple[str, str, str, str]]:
    """Classical RK4 with Source guard at every stage before commit."""
    ks: list[CoeffMap] = []
    routes: list[str] = []
    s1 = dict(y0)
    src1 = source_for_stage(1, s1)
    k1, r1, _ = guarded_stage_rhs(stage=1, stage_state=s1, source=src1, sparse_rhs=sparse_rhs, dense_rhs=dense_rhs, guard=guard)
    ks.append(k1); routes.append(r1)
    s2 = _add_scaled_state(y0, k1, 0.5 * h)
    src2 = source_for_stage(2, s2)
    k2, r2, _ = guarded_stage_rhs(stage=2, stage_state=s2, source=src2, sparse_rhs=sparse_rhs, dense_rhs=dense_rhs, guard=guard)
    ks.append(k2); routes.append(r2)
    s3 = _add_scaled_state(y0, k2, 0.5 * h)
    src3 = source_for_stage(3, s3)
    k3, r3, _ = guarded_stage_rhs(stage=3, stage_state=s3, source=src3, sparse_rhs=sparse_rhs, dense_rhs=dense_rhs, guard=guard)
    ks.append(k3); routes.append(r3)
    s4 = _add_scaled_state(y0, k3, h)
    src4 = source_for_stage(4, s4)
    k4, r4, _ = guarded_stage_rhs(stage=4, stage_state=s4, source=src4, sparse_rhs=sparse_rhs, dense_rhs=dense_rhs, guard=guard)
    ks.append(k4); routes.append(r4)
    return _rk4_combine(y0, h, ks), tuple(routes)  # type: ignore[return-value]


def dense_rk4_step(y0: CoeffMap, h: float, *,
                   source_for_stage: Callable[[int, CoeffMap], CoeffMap],
                   dense_rhs: Callable[[CoeffMap, CoeffMap], CoeffMap]) -> dict[Vec, complex]:
    """All-dense comparison path for the witness harness."""
    ks: list[CoeffMap] = []
    s1 = dict(y0); k1 = dense_rhs(s1, source_for_stage(1, s1)); ks.append(k1)
    s2 = _add_scaled_state(y0, k1, 0.5*h); k2 = dense_rhs(s2, source_for_stage(2, s2)); ks.append(k2)
    s3 = _add_scaled_state(y0, k2, 0.5*h); k3 = dense_rhs(s3, source_for_stage(3, s3)); ks.append(k3)
    s4 = _add_scaled_state(y0, k3, h); k4 = dense_rhs(s4, source_for_stage(4, s4)); ks.append(k4)
    return _rk4_combine(y0, h, ks)
