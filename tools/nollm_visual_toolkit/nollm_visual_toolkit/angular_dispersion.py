"""Exact angular-histogram dispersion, not a native-geometry state.

For B bins, population T and squared-count sum Q, CV squared is the
unreduced integer ratio (B*Q - T*T, T*T). A one-bin histogram with positive
population has exact CV squared zero. Keeping CV squared avoids a root
when comparing non-negative dispersions. Ordered counts remain the source;
equal ratios do not authorize identifying histograms or native paths.

The standalone toolkit can construct, compare and serialize this symbolic
ratio without Enterprise Math. Explicit finite-scale quotient/remainder
readouts require the existing BRC facade; there is no approximate fallback.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enterprise_math.exact_arithmetic import BRCScaledReadout


def _natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _positive(name: str, value: int) -> None:
    _natural(name, value)
    if value == 0:
        raise ValueError(f"{name} must be positive")


@dataclass(frozen=True)
class AngularDispersion:
    """An immutable, source-preserving exact CV-squared observation."""

    counts: tuple[int, ...]
    bins: int = field(init=False)
    population: int = field(init=False)
    sum_squares: int = field(init=False)
    numerator: int = field(init=False)
    denominator: int = field(init=False)

    def __post_init__(self) -> None:
        if not isinstance(self.counts, tuple) or len(self.counts) < 1:
            raise ValueError("counts must be an ordered tuple with at least one bin")
        for count in self.counts:
            _natural("bin count", count)
        population = sum(self.counts)
        if population == 0:
            raise ValueError("CV squared is undefined for a zero population")
        bins = len(self.counts)
        sum_squares = sum(count * count for count in self.counts)
        denominator = population * population
        numerator = bins * sum_squares - denominator
        if numerator < 0:
            raise AssertionError("non-negative histogram gave negative dispersion")
        for name, value in (
            ("bins", bins), ("population", population),
            ("sum_squares", sum_squares), ("numerator", numerator),
            ("denominator", denominator),
        ):
            object.__setattr__(self, name, value)

    @classmethod
    def from_counts(cls, counts: list[int] | tuple[int, ...]) -> AngularDispersion:
        """Snapshot ordered bins; never coerce approximate input to integers."""
        if not isinstance(counts, (list, tuple)):
            raise ValueError("counts must be an ordered list or tuple")
        return cls(tuple(counts))

    def compare_value(self, other: AngularDispersion) -> int:
        """Compare the scalar statistic, without equating its source states."""
        if not isinstance(other, AngularDispersion):
            raise TypeError("other must be an AngularDispersion")
        return self.compare_ratio(other.numerator, other.denominator)

    def compare_ratio(self, numerator: int, denominator: int) -> int:
        """Compare CV squared with an exact non-negative rational threshold."""
        _natural("threshold numerator", numerator)
        _positive("threshold denominator", denominator)
        left = self.numerator * denominator
        right = numerator * self.denominator
        return (left > right) - (left < right)

    def readout(self, scale: int) -> BRCScaledReadout:
        """Materialize S*N = D*q+r through the existing BRC implementation."""
        _positive("scale", scale)
        try:
            from enterprise_math.exact_arithmetic import DivisionExpr, brc_scaled_evaluate
        except ModuleNotFoundError as exc:
            if exc.name not in {"enterprise_math", "enterprise_math.exact_arithmetic"}:
                raise
            raise RuntimeError(
                "Exact residual readout requires enterprise_math.exact_arithmetic; "
                "install Enterprise Math or expose the repository src directory. "
                "No approximate fallback is available."
            ) from exc
        return brc_scaled_evaluate(DivisionExpr(self.numerator, self.denominator), scale)

    def as_record(self, *, scale: int | None = None) -> dict[str, object]:
        """Return lossless JSON data; every integer is encoded as decimal text.

        This observation is exact for the supplied histogram. It is not a
        certificate for polar-cell assignment, native geometry or hidden paths.
        A missing readout is explicit, never substituted with floating digits.
        """
        record: dict[str, object] = {
            "schema": "NOLLM_ANGULAR_CV_SQUARED_V1",
            "scope": "ORDERED_HISTOGRAM_OBSERVER_NOT_NATIVE_GEOMETRY",
            "integer_encoding": "DECIMAL_STRING",
            "counts": [str(count) for count in self.counts],
            "bins": str(self.bins),
            "population": str(self.population),
            "sum_squares": str(self.sum_squares),
            "numerator": str(self.numerator),
            "denominator": str(self.denominator),
            "definition": "(bins*sum_squares-population*population)/(population*population)",
            "readout": None,
        }
        if scale is not None:
            observed = self.readout(scale)
            trace = observed.trace
            record["readout"] = {
                "kind": "INTEGER_PLUS_RATIONAL_RESIDUAL_OF_CV_SQUARED",
                "scale": str(observed.scale),
                "integer": str(observed.scaled_value),
                "residual_numerator": str(observed.residual_numerator),
                "residual_denominator": str(observed.residual_denominator),
                "trace": {
                    "evaluation_kind": trace.evaluation_kind,
                    "numerator": str(trace.numerator),
                    "denominator": str(trace.denominator),
                    "quotient": str(trace.quotient),
                    "remainder": str(trace.remainder),
                    "collapsed_numerator": str(trace.collapsed_numerator),
                },
            }
        return record
