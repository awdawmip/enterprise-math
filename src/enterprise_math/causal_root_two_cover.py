"""Two-cover loop-return invariants for ADE primitive edge contexts.

Fix a primitive root direction ``alpha`` in a simply-laced root system.  Its
common-neighbor roots come in complementary pairs ``{beta, alpha-beta}``.  The
edge-context graph is therefore a two-fold cover of a complete graph with
``h-2`` base vertices, where ``h`` is the Coxeter number.

For a triple of complementary fibers, the lifted base triangle is either two
separate 3-cycles (return-preserving) or one 6-cycle (return-flipping).  This
triangle parity is invariant under swapping the two labels inside any fiber,
so it is an intrinsic local continuation invariant rather than a coordinate
choice.

The closed forms below are a compact executable profile for the ADE
pressure-test family.  They are not claimed as original root-system results.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb

from enterprise_math.causal_root_system_profile import (
    RootSystemProfile,
    a_profile,
    d_profile,
    e_profile,
)


@dataclass(frozen=True)
class TwoCoverProfile:
    family: str
    base_vertices: int
    base_triangles: int
    return_preserving_triangles: int
    return_flipping_triangles: int

    @property
    def has_nontrivial_loop_return(self) -> bool:
        return self.return_flipping_triangles > 0

    @property
    def flipping_fraction(self) -> Fraction:
        if self.base_triangles == 0:
            return Fraction(0, 1)
        return Fraction(self.return_flipping_triangles, self.base_triangles)


def _profile(
    root: RootSystemProfile,
    flipping: int,
) -> TwoCoverProfile:
    base_vertices = root.coxeter_number - 2
    total = comb(base_vertices, 3) if base_vertices >= 3 else 0
    if flipping < 0 or flipping > total:
        raise ValueError("invalid flipping-triangle count")
    return TwoCoverProfile(
        family=root.family,
        base_vertices=base_vertices,
        base_triangles=total,
        return_preserving_triangles=total - flipping,
        return_flipping_triangles=flipping,
    )


def a_two_cover_profile(rank: int) -> TwoCoverProfile:
    root = a_profile(rank)
    return _profile(root, 0)


def d_two_cover_profile(rank: int) -> TwoCoverProfile:
    root = d_profile(rank)
    flipping = 4 * comb(rank - 2, 2)
    return _profile(root, flipping)


def e_two_cover_profile(rank: int) -> TwoCoverProfile:
    root = e_profile(rank)
    h = root.coxeter_number
    # For E6,E7,E8 the exact integer counts are respectively 60,240,1260;
    # the following single expression reproduces all three.
    flipping = (h - 2) * comb(h // 3, 2)
    return _profile(root, flipping)


def two_cover_profile(family: str, rank: int) -> TwoCoverProfile:
    normalized = family.upper()
    if normalized == "A":
        return a_two_cover_profile(rank)
    if normalized == "D":
        return d_two_cover_profile(rank)
    if normalized == "E":
        return e_two_cover_profile(rank)
    raise ValueError("family must be one of A, D, E")
