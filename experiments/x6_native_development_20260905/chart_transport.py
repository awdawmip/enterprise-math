"""Gauge-compatible chart transport, not a physical Cell-identification rule.

Shared K4 edge labels stay fixed along their own chart transition. The entire
coordinate frame rotates. Flatness is an explicitly stated selector; it is
not inferred from the packet unit axiom.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
import x6_development as x


def transition(u: int, v: int, *, kind: str = "flat") -> tuple[int, ...]:
    """The two S4-natural shared-edge swaps; flat selects double transpositions."""
    x.atlas.vertex(u); x.atlas.vertex(v)
    if kind not in ("flat", "single"):
        raise ValueError("kind must be flat or single")
    p = list(range(4))
    if u == v:
        return tuple(p)
    p[u], p[v] = v, u
    if kind == "flat":
        a, b = (w for w in range(4) if w not in (u, v))
        p[a], p[b] = b, a
    return tuple(p)


def transport_word(walk: Iterable[int], *, kind: str = "flat") -> tuple[int, ...]:
    walk = tuple(x.atlas.vertex(v) for v in walk)
    if not walk:
        raise ValueError("nonempty chart walk required")
    p = x.brc.IDENTITY
    for u, v in zip(walk, walk[1:]):
        p = x.brc.compose(transition(u, v, kind=kind), p)
    return p


@dataclass(frozen=True)
class FramedCell:
    """Same candidate packet described in a selected passive chart frame.

    Equivalence here is a proven CHANGE OF DESCRIPTION of X_dev; it does not
    identify any additional pair of distinct X_dev endpoints.
    """
    chart: int
    coordinates: x.Cell

    def __post_init__(self):
        x.atlas.vertex(self.chart)
        if not isinstance(self.coordinates, x.Cell):
            raise TypeError("coordinates must be a development Cell")

    def reframe(self, v: int) -> "FramedCell":
        return FramedCell(v, self.coordinates.rotate(transition(self.chart, v)))

    def decode(self, *, reference: int = 0) -> x.Cell:
        x.atlas.vertex(reference)
        return self.coordinates.rotate(transition(self.chart, reference))

    @classmethod
    def encode(cls, cell: x.Cell, chart: int, *, reference: int = 0) -> "FramedCell":
        if not isinstance(cell, x.Cell):
            raise TypeError("a candidate packet is required")
        return cls(chart, cell.rotate(transition(reference, chart)))

    def relabel_chart_and_coordinates(self, g: Iterable[int]) -> "FramedCell":
        """Simultaneous atlas relabeling, NOT fixed-reference active rotation.

        After decode this action factors through S4/V4. Confusing it with
        active rotation silently deletes the Klein-four rotation component.
        """
        g = x.brc.permutation(g)
        return FramedCell(g[self.chart], self.coordinates.rotate(g))

    def active_rotate(self, g: Iterable[int], *, reference: int = 0) -> "FramedCell":
        """Physical candidate-state action, conjugated into the selected chart.

        Does not quotient any candidate endpoints or discard the actual frame.
        """
        g = x.brc.permutation(g)
        actual = self.decode(reference=reference).rotate(g)
        return FramedCell.encode(actual, self.chart, reference=reference)

    def observer(self, *, reference: int = 0) -> tuple[int, int, int]:
        return self.decode(reference=reference).carrier_readout()
