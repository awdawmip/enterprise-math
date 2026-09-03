"""Exact tetrahedral endpoint-sum residual analyzer for Enterprise Math.

This is a project subtool, not a new top-level toolbox family.  It packages the
finite K4 specialization shared by the operation-safe quotient (T6), finite
symmetry/equivariance (T7), and cocycle/gluing (T9) tool families.

Edge coordinates are ordered as ``(12, 13, 14, 23, 24, 34)``.  Vertex
coordinates are ordered as ``(1, 2, 3, 4)``.
"""
from __future__ import annotations

from dataclasses import dataclass
from numbers import Integral
from typing import Iterable

EdgeState = tuple[int, int, int, int, int, int]
VertexState = tuple[int, int, int, int]
PointF2 = tuple[int, int]

EDGE_NAMES = ("12", "13", "14", "23", "24", "34")
F2_POINTS: tuple[PointF2, ...] = ((0, 0), (1, 0), (0, 1), (1, 1))


def _integer_tuple(values: Iterable[int], length: int, name: str) -> tuple[int, ...]:
    result = tuple(values)
    if len(result) != length:
        raise ValueError(f"{name} must have exactly {length} coordinates")
    if any(isinstance(value, bool) or not isinstance(value, Integral) for value in result):
        raise TypeError(f"{name} coordinates must be integers")
    return tuple(int(value) for value in result)


def edge_state(values: Iterable[int]) -> EdgeState:
    return _integer_tuple(values, 6, "edge state")  # type: ignore[return-value]


def vertex_state(values: Iterable[int]) -> VertexState:
    return _integer_tuple(values, 4, "vertex state")  # type: ignore[return-value]


def edge_total(x: Iterable[int]) -> int:
    return sum(edge_state(x))


def vertex_total(v: Iterable[int]) -> int:
    return sum(vertex_state(v))


def endpoint_sum(v: Iterable[int]) -> EdgeState:
    """Apply the signless K4 incidence map ``delta(v)_ij = v_i + v_j``."""
    a, b, c, d = vertex_state(v)
    return (a + b, a + c, a + d, b + c, b + d, c + d)


def matching_sums(x: Iterable[int]) -> tuple[int, int, int]:
    """Return the three opposite-edge matching sums."""
    e12, e13, e14, e23, e24, e34 = edge_state(x)
    return (e12 + e34, e13 + e24, e14 + e23)


def star_parity(x: Iterable[int]) -> int:
    """Return the star-at-vertex-1 parity in ``{0,1}``."""
    e12, e13, e14, _, _, _ = edge_state(x)
    return (e12 + e13 + e14) & 1


@dataclass(frozen=True)
class ResidualCode:
    """Canonical ``A2 x C2`` code of a zero-total edge state."""

    p: int
    q: int
    parity: int

    def __post_init__(self) -> None:
        if self.parity not in (0, 1):
            raise ValueError("parity must be 0 or 1")

    @property
    def third_matching(self) -> int:
        return -self.p - self.q

    @property
    def matching(self) -> tuple[int, int, int]:
        return (self.p, self.q, self.third_matching)


def residual_code(x: Iterable[int]) -> ResidualCode:
    """Classify a zero-total K4 edge state modulo zero-total vertex potentials."""
    state = edge_state(x)
    if sum(state) != 0:
        raise ValueError("residual quotient is defined here only on zero-total edge states")
    m0, m1, m2 = matching_sums(state)
    if m0 + m1 + m2 != 0:
        raise AssertionError("matching total must equal the zero edge total")
    return ResidualCode(m0, m1, star_parity(state))


def normal_form(p: int, q: int, parity: int) -> EdgeState:
    """Return ``N(p,q,e)=(p,q,e-p-q,-e,0,0)`` with ``e`` reduced mod 2."""
    if isinstance(p, bool) or not isinstance(p, Integral):
        raise TypeError("p must be an integer")
    if isinstance(q, bool) or not isinstance(q, Integral):
        raise TypeError("q must be an integer")
    if isinstance(parity, bool):
        parity = int(parity)
    if not isinstance(parity, Integral):
        raise TypeError("parity must be an integer")
    e = int(parity) & 1
    p_i, q_i = int(p), int(q)
    return (p_i, q_i, e - p_i - q_i, -e, 0, 0)


def canonical_representative(x: Iterable[int]) -> EdgeState:
    code = residual_code(x)
    return normal_form(code.p, code.q, code.parity)


def delta_equivalent(x: Iterable[int], y: Iterable[int]) -> bool:
    """Exact quotient equality on ``E0``."""
    return residual_code(x) == residual_code(y)


def lift_difference(x: Iterable[int], y: Iterable[int]) -> VertexState | None:
    """Return the unique zero-total vertex lift of ``x-y``, or ``None``.

    For equal matching coordinates the difference has kernel shape
    ``(a,b,c,-c,-b,-a)``.  It lifts integrally iff ``a+b+c`` is even, with
    explicit lift ``(t,a-t,b-t,c-t)`` for ``t=(a+b+c)/2``.
    """
    x_state, y_state = edge_state(x), edge_state(y)
    if sum(x_state) != 0 or sum(y_state) != 0:
        raise ValueError("lift classification requires zero-total edge states")
    if matching_sums(x_state) != matching_sums(y_state):
        return None
    diff: EdgeState = tuple(a - b for a, b in zip(x_state, y_state))  # type: ignore[assignment]
    a, b, c = diff[:3]
    if (a + b + c) & 1:
        return None
    t = (a + b + c) // 2
    lift: VertexState = (t, a - t, b - t, c - t)
    if sum(lift) != 0 or endpoint_sum(lift) != diff:
        raise AssertionError("explicit endpoint-sum lift certificate failed")
    return lift


@dataclass(frozen=True)
class CanonicalDecomposition:
    code: ResidualCode
    representative: EdgeState
    lift: VertexState


def canonical_decomposition(x: Iterable[int]) -> CanonicalDecomposition:
    """Decompose ``x`` as its canonical residual representative plus ``delta(lift)``."""
    state = edge_state(x)
    code = residual_code(state)
    representative = normal_form(code.p, code.q, code.parity)
    lift = lift_difference(state, representative)
    if lift is None:
        raise AssertionError("canonical representative must lie in the same quotient class")
    reconstructed = tuple(a + b for a, b in zip(representative, endpoint_sum(lift)))
    if reconstructed != state:
        raise AssertionError("canonical decomposition failed reconstruction")
    return CanonicalDecomposition(code, representative, lift)


TORSION_WITNESS: EdgeState = (1, 0, 0, 0, 0, -1)
TORSION_DOUBLE_LIFT: VertexState = (1, 1, -1, -1)


def verify_torsion_certificate() -> bool:
    """Check ``tau`` is the odd class while ``2*tau`` has the displayed lift."""
    zero: EdgeState = (0, 0, 0, 0, 0, 0)
    if lift_difference(TORSION_WITNESS, zero) is not None:
        return False
    doubled = tuple(2 * value for value in TORSION_WITNESS)
    return endpoint_sum(TORSION_DOUBLE_LIFT) == doubled and sum(TORSION_DOUBLE_LIFT) == 0


def affine_value(code: ResidualCode, point: PointF2) -> int:
    """Evaluate ``e + p*x + q*y`` over F2."""
    x, y = point
    if x not in (0, 1) or y not in (0, 1):
        raise ValueError("affine point coordinates must lie in F2={0,1}")
    return (code.parity + (code.p & 1) * x + (code.q & 1) * y) & 1


def affine_support(code: ResidualCode) -> tuple[PointF2, ...]:
    return tuple(point for point in F2_POINTS if affine_value(code, point) == 1)


def opposite_support(code: ResidualCode) -> tuple[PointF2, ...]:
    """Add the nonzero constant class, hence complement the affine support."""
    toggled = ResidualCode(code.p, code.q, code.parity ^ 1)
    return affine_support(toggled)


def hidden_translation_phase(code: ResidualCode, translation: PointF2) -> int:
    """Return the V4/F2^2 translation phase ``p*a+q*b`` mod 2."""
    a, b = translation
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError("translation coordinates must lie in F2={0,1}")
    return ((code.p & 1) * a + (code.q & 1) * b) & 1
