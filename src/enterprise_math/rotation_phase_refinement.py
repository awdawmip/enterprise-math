"""Finite rotation-phase refinement for the Enterprise Math Euler line.

The module keeps three layers separate:

* carrier certificate: one triangular-lattice Cell star and its six triple gates;
* finite phase calculus: cyclic orientation levels and quotient/remainder refinement;
* Archimedean readout: dyadic half-traces and Viète-type finite slopes.

No function identifies carrier Euclidean distance with native Enterprise length, and no
function uses the numerical value of pi to construct the finite refinement.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from typing import Literal, NamedTuple


Axial = tuple[Fraction, Fraction]


def _axial(value: tuple[int | Fraction, int | Fraction]) -> Axial:
    return Fraction(value[0]), Fraction(value[1])


NEIGHBOR_AXIAL: tuple[Axial, ...] = tuple(
    _axial(value)
    for value in ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
)


def axial_add(left: Axial, right: Axial) -> Axial:
    return left[0] + right[0], left[1] + right[1]


def axial_sub(left: Axial, right: Axial) -> Axial:
    return left[0] - right[0], left[1] - right[1]


def axial_scale(scale: Fraction, value: Axial) -> Axial:
    return scale * value[0], scale * value[1]


def carrier_norm_sq(value: Axial) -> Fraction:
    """Squared Euclidean carrier norm in triangular axial coordinates.

    This is a carrier certificate only.  It is not the native Enterprise line gauge.
    """

    a, b = value
    return a * a + a * b + b * b


@dataclass(frozen=True)
class PivotGateCertificate:
    index: int
    left_neighbor: Axial
    right_neighbor: Axial
    gate: Axial
    pivot_distance_sq: Fraction
    left_distance_sq: Fraction
    right_distance_sq: Fraction

    @property
    def valid(self) -> bool:
        target = Fraction(1, 3)
        return (
            self.pivot_distance_sq == target
            and self.left_distance_sq == target
            and self.right_distance_sq == target
        )


def pivot_gate_certificate(index: int) -> PivotGateCertificate:
    """Return the unique elementary-triangle gate between two consecutive neighbors."""

    k = index % 6
    left = NEIGHBOR_AXIAL[k]
    right = NEIGHBOR_AXIAL[(k + 1) % 6]
    gate = axial_scale(Fraction(1, 3), axial_add(left, right))
    return PivotGateCertificate(
        index=k,
        left_neighbor=left,
        right_neighbor=right,
        gate=gate,
        pivot_distance_sq=carrier_norm_sq(gate),
        left_distance_sq=carrier_norm_sq(axial_sub(gate, left)),
        right_distance_sq=carrier_norm_sq(axial_sub(gate, right)),
    )


def pivot_gate_certificates() -> tuple[PivotGateCertificate, ...]:
    return tuple(pivot_gate_certificate(k) for k in range(6))


class GatePhaseState(NamedTuple):
    kind: Literal["cell", "gate"]
    index: int


def normalize_gate_phase_state(state: GatePhaseState) -> GatePhaseState:
    return GatePhaseState(state.kind, state.index % 6)


def gate_phase_index(state: GatePhaseState) -> int:
    """Encode the interleaved Cell/gate phase state as an index in C_12."""

    state = normalize_gate_phase_state(state)
    return 2 * state.index + (1 if state.kind == "gate" else 0)


def gate_phase_state(index: int) -> GatePhaseState:
    """Decode an index in C_12 into the alternating Cell/gate phase type."""

    value = index % 12
    return GatePhaseState("gate" if value % 2 else "cell", value // 2)


def gate_successor(state: GatePhaseState) -> GatePhaseState:
    """The oriented gate-refined successor Q.

    Q(cell_k)=gate_k and Q(gate_k)=cell_(k+1), hence Q^2 is the coarse C_6
    successor on Cell states.
    """

    state = normalize_gate_phase_state(state)
    if state.kind == "cell":
        return GatePhaseState("gate", state.index)
    return GatePhaseState("cell", (state.index + 1) % 6)


def gate_iterate(state: GatePhaseState, steps: int) -> GatePhaseState:
    current = normalize_gate_phase_state(state)
    for _ in range(steps % 12):
        current = gate_successor(current)
    return current


def gate_refinement_certificate() -> dict[str, object]:
    origin = GatePhaseState("cell", 0)
    return {
        "gate_geometry": all(item.valid for item in pivot_gate_certificates()),
        "q2_cell_0": gate_iterate(origin, 2),
        "q3_cell_0": gate_iterate(origin, 3),
        "q4_cell_0": gate_iterate(origin, 4),
        "q6_cell_0": gate_iterate(origin, 6),
        "q12_cell_0": gate_iterate(origin, 12),
        "quarter_square": gate_iterate(origin, 6)
        == gate_iterate(gate_iterate(origin, 3), 3),
    }


def crt_six_state(index: int) -> tuple[int, int]:
    """C_6 -> C_3 x C_2 with coarse successor mapped to (2,1).

    Under this map, two coarse steps give the positive C_3 sector turn and
    three coarse steps give the reversal bit.
    """

    k = index % 6
    return (2 * k) % 3, k % 2


def crt_six_generator_certificate() -> dict[str, tuple[int, int]]:
    generator = crt_six_state(1)
    square = ((2 * generator[0]) % 3, (2 * generator[1]) % 2)
    cube = ((3 * generator[0]) % 3, (3 * generator[1]) % 2)
    return {"generator": generator, "square": square, "cube": cube}


@dataclass(frozen=True)
class CyclicPhaseLevel:
    """One cyclic orientation level C_(6*2^depth)."""

    depth: int

    def __post_init__(self) -> None:
        if isinstance(self.depth, bool) or not isinstance(self.depth, int) or self.depth < 0:
            raise ValueError("depth must be a nonnegative integer")

    @property
    def order(self) -> int:
        return 6 * (2**self.depth)

    def normalize(self, state: int) -> int:
        return state % self.order

    @property
    def generator(self) -> int:
        return 1

    @property
    def native_sector_turn(self) -> int:
        """The embedded 120-degree three-ray turn, as a phase index."""

        return self.order // 3

    @property
    def half_turn(self) -> int:
        return self.order // 2

    @property
    def quarter_turn(self) -> int | None:
        return self.order // 4 if self.order % 4 == 0 else None

    def embed_to_next(self, state: int) -> int:
        """Embed an old phase as an even state in the next refinement."""

        return (2 * self.normalize(state)) % (2 * self.order)

    def normalized_phase(self, state: int) -> Fraction:
        return Fraction(self.normalize(state), self.order)

    def phase_distance(self, left: int, right: int) -> Fraction:
        gap = abs(self.normalize(left) - self.normalize(right))
        cyclic_gap = min(gap, self.order - gap)
        return Fraction(cyclic_gap, self.order)

    def embedding_isometric(self, left: int, right: int) -> bool:
        fine = CyclicPhaseLevel(self.depth + 1)
        return self.phase_distance(left, right) == fine.phase_distance(
            self.embed_to_next(left), self.embed_to_next(right)
        )

    def square_roots_in_next_of_embedded(self, state: int) -> tuple[int, int]:
        """The two roots x in C_(2N) of 2x = embed(state)."""

        k = self.normalize(state)
        return k, k + self.order

    def canonical_index_root_in_next_of_embedded(self, state: int) -> int:
        """Choose the root represented by the normalized coarse index.

        For the generator this is the positive refined successor.  For a general
        state this is an index-section choice, not an intrinsic shortest-arc claim.
        """

        return self.normalize(state)

    def split_fine_state(self, fine_state: int) -> tuple[int, int]:
        """Unique set-level quotient/remainder decomposition r=2k+epsilon."""

        value = fine_state % (2 * self.order)
        coarse, residual = divmod(value, 2)
        return coarse, residual

    def recompose_fine_state(self, coarse: int, residual: int) -> int:
        if residual not in (0, 1):
            raise ValueError("residual must be 0 or 1")
        return (2 * self.normalize(coarse) + residual) % (2 * self.order)

    def refined_successor_digits(self, coarse: int, residual: int) -> tuple[int, int]:
        """One fine successor: toggle the bit, carrying into the coarse phase."""

        state = self.recompose_fine_state(coarse, residual)
        return self.split_fine_state(state + 1)


def quarter_turn_roots(order: int) -> tuple[int, ...]:
    """Solutions q in C_order to 2q = order/2 (the half-turn)."""

    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    if order % 2:
        return ()
    target = order // 2
    return tuple(q for q in range(order) if (2 * q - target) % order == 0)


def minimal_cyclic_refinement_order(base_order: int = 6) -> int:
    """Smallest cyclic order divisible by the base order and admitting a quarter-turn."""

    if isinstance(base_order, bool) or not isinstance(base_order, int) or base_order < 1:
        raise ValueError("base_order must be a positive integer")
    candidate = base_order
    while candidate % 4:
        candidate += base_order
    return candidate


@dataclass(frozen=True)
class DyadicTraceDatum:
    level: int
    half_trace: Decimal
    skew_trace: Decimal
    finite_half_slope: Decimal
    product_readout: Decimal


def dyadic_trace_data(depth: int, *, precision: int = 80) -> tuple[DyadicTraceDatum, ...]:
    """Compute the finite half-trace/Viète tower without using a value of pi.

    Level 1 is the quarter-turn: c_1=0, s_1=1.  Recursively,
    c_(n+1)^2=(1+c_n)/2 and s_n^2=1-c_n^2.  The finite half-slope is
    2^n s_n and equals 2/prod_{j=2}^n c_j.
    """

    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")
    if isinstance(precision, bool) or not isinstance(precision, int) or precision < 20:
        raise ValueError("precision must be an integer at least 20")

    with localcontext() as context:
        context.prec = precision
        one = Decimal(1)
        two = Decimal(2)
        c = Decimal(0)
        product = Decimal(1)
        out: list[DyadicTraceDatum] = []
        for level in range(1, depth + 1):
            if level > 1:
                c = ((one + c) / two).sqrt()
                product *= c
            s = (one - c * c).sqrt()
            slope = (two**level) * s
            product_readout = two / product
            out.append(
                DyadicTraceDatum(
                    level=level,
                    half_trace=+c,
                    skew_trace=+s,
                    finite_half_slope=+slope,
                    product_readout=+product_readout,
                )
            )
        return tuple(out)


def verify_dyadic_trace_data(depth: int = 20, *, precision: int = 100) -> bool:
    data = dyadic_trace_data(depth, precision=precision)
    tolerance = Decimal(10) ** (-(precision // 2))
    previous_slope: Decimal | None = None
    for item in data:
        if abs(item.finite_half_slope - item.product_readout) > tolerance:
            return False
        if previous_slope is not None and not previous_slope < item.finite_half_slope:
            return False
        previous_slope = item.finite_half_slope
    return True


def certificate() -> dict[str, object]:
    levels = tuple(CyclicPhaseLevel(depth) for depth in range(4))
    trace = dyadic_trace_data(12, precision=80)
    return {
        "pivot_gate_geometry": [
            {
                "index": item.index,
                "gate": tuple(str(value) for value in item.gate),
                "squared_distances": (
                    str(item.pivot_distance_sq),
                    str(item.left_distance_sq),
                    str(item.right_distance_sq),
                ),
                "valid": item.valid,
            }
            for item in pivot_gate_certificates()
        ],
        "gate_refinement": gate_refinement_certificate(),
        "crt_c6": crt_six_generator_certificate(),
        "levels": [
            {
                "depth": level.depth,
                "order": level.order,
                "native_sector_turn": level.native_sector_turn,
                "half_turn": level.half_turn,
                "quarter_turn": level.quarter_turn,
                "quarter_roots": quarter_turn_roots(level.order),
            }
            for level in levels
        ],
        "minimal_order_from_c6_with_quarter_turn": minimal_cyclic_refinement_order(),
        "dyadic_trace_verified": verify_dyadic_trace_data(),
        "finite_half_slopes": [
            {
                "level": item.level,
                "value": str(item.finite_half_slope),
            }
            for item in trace
        ],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(certificate(), indent=2, ensure_ascii=False))
