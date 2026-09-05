"""Universal minimal X6 Cell-endpoint completion prototype.

Research status only: this module implements the endpoint group forced by the
four established three-axis slice relations, without promoting the universal
minimal completion to P000.

The computational normal form ``(u,v,epsilon) in Z^2 x Z/2`` is an endpoint
algebra representation.  It must NOT be read as a reduction of the P000 six
spatial dimensions, which are typed by six native axis relations.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Iterable

VERTEX_NAMES = ("A", "B", "C", "D")
EDGES = tuple(combinations(range(4), 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
EDGE_NAMES = ("AB", "AC", "AD", "BC", "BD", "CD")
EDGE_NAME_INDEX = {name: i for i, name in enumerate(EDGE_NAMES)}
STARS = tuple(tuple(i for i, e in enumerate(EDGES) if v in e) for v in range(4))
GROUP_S4 = tuple(permutations(range(4)))

# Endpoint generators in the exact normal form G6^cell ~= Z^2 x Z/2.
_AXIS = (
    (1, 0, 0),    # AB
    (0, 1, 0),    # AC
    (-1, -1, 0),  # AD
    (-1, -1, 1),  # BC
    (0, 1, 1),    # BD
    (1, 0, 1),    # CD
)
_T = (0, 0, 1)


def _add(x, y):
    return (x[0] + y[0], x[1] + y[1], (x[2] + y[2]) & 1)


def _scale(k: int, x):
    if type(k) is not int:
        raise TypeError("integer coefficient required")
    return (k * x[0], k * x[1], (k * x[2]) & 1)


def _canonical3(values: Iterable[int]) -> tuple[int, int, int]:
    values = tuple(values)
    if len(values) != 3 or any(type(x) is not int for x in values):
        raise ValueError("expected three integers")
    m = min(values)
    return tuple(x - m for x in values)


def _vertex(vertex: int | str) -> int:
    if isinstance(vertex, str):
        if vertex not in VERTEX_NAMES:
            raise ValueError("unknown slice vertex")
        return VERTEX_NAMES.index(vertex)
    if type(vertex) is not int or not 0 <= vertex < 4:
        raise ValueError("slice vertex must be A/B/C/D or 0..3")
    return vertex


def _axis_index(axis: int | str) -> int:
    if isinstance(axis, str):
        if axis not in EDGE_NAME_INDEX:
            raise ValueError("unknown native axis label")
        return EDGE_NAME_INDEX[axis]
    if type(axis) is not int or not 0 <= axis < 6:
        raise ValueError("axis must be one of six native labels")
    return axis


@dataclass(frozen=True)
class CellState:
    """Endpoint-state normal form, not a six-coordinate dimension claim."""

    u: int = 0
    v: int = 0
    sheet: int = 0

    def __post_init__(self):
        if type(self.u) is not int or type(self.v) is not int or type(self.sheet) is not int:
            raise TypeError("CellState entries must be integers")
        object.__setattr__(self, "sheet", self.sheet & 1)

    @property
    def tuple(self):
        return (self.u, self.v, self.sheet)

    def then_displacement(self, displacement: "CellState") -> "CellState":
        if not isinstance(displacement, CellState):
            raise TypeError("expected CellState displacement")
        return CellState(*_add(self.tuple, displacement.tuple))

    def inverse(self) -> "CellState":
        return CellState(-self.u, -self.v, self.sheet)


ORIGIN_CELL = CellState()
COMPANION = CellState(*_T)


def axis_generator(axis: int | str) -> CellState:
    return CellState(*_AXIS[_axis_index(axis)])


def step(state: CellState, axis: int | str, direction: int = 1) -> CellState:
    """One native-axis adjacency event; direction=-1 is path reversal, not a new axis."""
    if not isinstance(state, CellState):
        raise TypeError("state must be CellState")
    if direction not in (-1, 1):
        raise ValueError("direction must be +1 or -1")
    return state.then_displacement(CellState(*_scale(direction, axis_generator(axis).tuple)))


def endpoint_from_exponents(exponents: Iterable[int]) -> CellState:
    """Endpoint from six signed net axis exponents in AB,AC,AD,BC,BD,CD order."""
    exponents = tuple(exponents)
    if len(exponents) != 6 or any(type(k) is not int for k in exponents):
        raise ValueError("expected six integer net exponents")
    out = (0, 0, 0)
    for k, generator in zip(exponents, _AXIS):
        out = _add(out, _scale(k, generator))
    return CellState(*out)


def matching_sums(exponents: Iterable[int]) -> tuple[int, int, int]:
    z = tuple(exponents)
    if len(z) != 6:
        raise ValueError("expected six exponents")
    return (z[0] + z[5], z[1] + z[4], z[2] + z[3])


def return_certificate(exponents: Iterable[int]) -> bool:
    """Exact integer criterion for return to the starting Cell."""
    z = tuple(exponents)
    if len(z) != 6 or any(type(k) is not int for k in z):
        raise ValueError("expected six integer net exponents")
    m = matching_sums(z)
    return m[0] == m[1] == m[2] and ((z[0] + z[1] + z[3]) & 1) == 0


def star_return_coefficients(exponents: Iterable[int]) -> tuple[int, int, int, int]:
    """Recover exact integer coefficients of the four local star loops."""
    z = tuple(exponents)
    if not return_certificate(z):
        raise ValueError("endpoint is not the starting Cell")
    a, b, c, d, e, f = z
    k_a = (a + b - d) // 2
    k_b = a - k_a
    k_c = b - k_a
    k_d = c - k_a
    return (k_a, k_b, k_c, k_d)


def slice_sheet_bit(state: CellState, vertex: int | str) -> int:
    """Binary full-state sheet hidden by the ordinary selected-slice endpoint readout."""
    if not isinstance(state, CellState):
        raise TypeError("state must be CellState")
    vertex = _vertex(vertex)
    # Normal form uses AB,AC,T.  lambda_v(generator)=1 iff edge is not incident v.
    lambda_ab = int(vertex not in EDGES[0])
    lambda_ac = int(vertex not in EDGES[1])
    return (state.u * lambda_ab + state.v * lambda_ac + state.sheet) & 1


def visible_slice_state(state: CellState, vertex: int | str) -> CellState:
    """Project the full endpoint to the embedded local three-axis subgroup."""
    bit = slice_sheet_bit(state, vertex)
    return state.then_displacement(CellState(*_scale(bit, _T)))


def slice_address(state: CellState, vertex: int | str) -> tuple[int, int, int]:
    """Existing-style nonnegative min-zero address in one selected three-axis slice."""
    vertex = _vertex(vertex)
    h = visible_slice_state(state, vertex).tuple
    i, j, _ = STARS[vertex]
    a = _AXIS[i]
    b = _AXIS[j]
    det = a[0] * b[1] - b[0] * a[1]
    if abs(det) != 1:
        raise AssertionError("slice basis must be unimodular in the free endpoint coordinates")
    p = (h[0] * b[1] - b[0] * h[1]) // det
    q = (a[0] * h[1] - h[0] * a[1]) // det
    if _add(_scale(p, a), _scale(q, b)) != h:
        raise AssertionError("slice endpoint is not in the declared local subgroup")
    return _canonical3((p, q, 0))


def from_slice_chart(vertex: int | str, address: Iterable[int], sheet_bit: int) -> CellState:
    """Losslessly reconstruct a full universal state from one local address plus one bit."""
    vertex = _vertex(vertex)
    address = tuple(address)
    if len(address) != 3 or any(type(x) is not int or x < 0 for x in address) or min(address) != 0:
        raise ValueError("slice address must be a nonnegative min-zero triple")
    if sheet_bit not in (0, 1):
        raise ValueError("sheet bit must be 0 or 1")
    h = (0, 0, 0)
    for coefficient, edge_index in zip(address, STARS[vertex]):
        h = _add(h, _scale(coefficient, _AXIS[edge_index]))
    if slice_sheet_bit(CellState(*h), vertex) != 0:
        raise AssertionError("local slice address escaped its subgroup")
    return CellState(*_add(h, _scale(sheet_bit, _T)))


def change_slice_chart(
    source_vertex: int | str,
    address: Iterable[int],
    sheet_bit: int,
    target_vertex: int | str,
) -> tuple[tuple[int, int, int], int]:
    state = from_slice_chart(source_vertex, address, sheet_bit)
    return slice_address(state, target_vertex), slice_sheet_bit(state, target_vertex)


def _edge_action(permutation, edge_index):
    u, v = EDGES[edge_index]
    return EDGE_INDEX[tuple(sorted((permutation[u], permutation[v])))]


def rotate_state(state: CellState, permutation: Iterable[int]) -> CellState:
    """S4 atlas rotation acting exactly on the universal endpoint state."""
    permutation = tuple(permutation)
    if len(permutation) != 4 or set(permutation) != set(range(4)):
        raise ValueError("expected a permutation of four slice labels")
    image_ab = _AXIS[_edge_action(permutation, 0)]
    image_ac = _AXIS[_edge_action(permutation, 1)]
    out = _add(_scale(state.u, image_ab), _scale(state.v, image_ac))
    out = _add(out, _scale(state.sheet, _T))
    return CellState(*out)


__all__ = [
    "CellState",
    "ORIGIN_CELL",
    "COMPANION",
    "EDGE_NAMES",
    "VERTEX_NAMES",
    "axis_generator",
    "step",
    "endpoint_from_exponents",
    "matching_sums",
    "return_certificate",
    "star_return_coefficients",
    "slice_sheet_bit",
    "visible_slice_state",
    "slice_address",
    "from_slice_chart",
    "change_slice_chart",
    "rotate_state",
]
