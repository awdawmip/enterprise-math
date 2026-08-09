"""Separate causal LEGO factorization profiles from ADE geometry shadows.

The same current root-lattice geometry can have different causal constructions.
This module records several classical ADE constructions in a typed way.  A
factorization profile stores not only local cell rank/count, but also any
independent conservation constraint rank removed from the naive product.  This
prevents a product-of-cells representation from being mistaken for the final
relation rank.

Examples:
* A_r: r+1 one-dimensional integer slots with one exact-total constraint;
* D_r: r one-dimensional integer cells with a binary parity residue code;
* E6: three rank-two hex/A2 cells with ternary repetition code;
* E7: seven rank-one integer cells with binary simplex code;
* E8 has both eight rank-one binary cells and four rank-two ternary-hex cells.

The two E8 grammars have different factorization profiles but the same global
rank, primitive-event count, and Coxeter root-count shadow.  All ADE/code
correspondences are classical prior mathematics; this module organizes them under
the project's causal ordering.
"""

from __future__ import annotations

from dataclasses import dataclass

from .causal_code_lattice import even_parity_code, extended_hamming_8_code
from .causal_code_root_shadow import simplex_7_code
from .causal_local_alphabet_code import (
    binary_integer_alphabet,
    e6_primitive_shadow,
    primitive_grade_and_multiplicity,
    primitive_grade_regime,
    ternary_e8_primitive_shadow,
    ternary_hamming_4_code,
    ternary_hexagonal_alphabet,
    ternary_repetition_3_code,
)


@dataclass(frozen=True)
class CausalFactorizationProfile:
    name: str
    local_cell_rank: int
    cell_count: int
    independent_constraint_rank_loss: int
    residue_alphabet_size: int
    code_name: str
    primitive_grade_channel: str
    primitive_grade: int
    primitive_grade_regime: str

    @property
    def global_relation_rank(self) -> int:
        rank = self.local_cell_rank * self.cell_count - self.independent_constraint_rank_loss
        if rank < 0:
            raise ValueError("constraint rank loss exceeds product relation rank")
        return rank


@dataclass(frozen=True)
class GeometryShadowProfile:
    name: str
    rank: int
    primitive_event_count: int
    coxeter_root_count_shadow: int


def _coxeter_shadow(rank: int, primitive_count: int) -> int:
    if rank <= 0 or primitive_count % rank != 0:
        raise ValueError("primitive count must be divisible by positive rank")
    return primitive_count // rank


def _checked_pair(
    factor: CausalFactorizationProfile,
    shadow: GeometryShadowProfile,
) -> tuple[CausalFactorizationProfile, GeometryShadowProfile]:
    if factor.global_relation_rank != shadow.rank:
        raise AssertionError("causal factorization rank must match geometry-shadow rank")
    return factor, shadow


def a_grammar(rank: int) -> tuple[CausalFactorizationProfile, GeometryShadowProfile]:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 1:
        raise ValueError("A rank must be positive")
    cells = rank + 1
    primitive_count = cells * (cells - 1)
    factor = CausalFactorizationProfile(
        name=f"A{rank}:exact-transfer",
        local_cell_rank=1,
        cell_count=cells,
        independent_constraint_rank_loss=1,
        residue_alphabet_size=1,
        code_name="exact-total conservation",
        primitive_grade_channel="support",
        primitive_grade=2,
        primitive_grade_regime="conservation_forced",
    )
    shadow = GeometryShadowProfile(
        name=f"A{rank}",
        rank=rank,
        primitive_event_count=primitive_count,
        coxeter_root_count_shadow=_coxeter_shadow(rank, primitive_count),
    )
    return _checked_pair(factor, shadow)


def d_grammar(rank: int) -> tuple[CausalFactorizationProfile, GeometryShadowProfile]:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("D research grammar requires rank at least three")
    code = even_parity_code(rank)
    alphabet = binary_integer_alphabet()
    grade, primitive_count = primitive_grade_and_multiplicity(code, alphabet)
    factor = CausalFactorizationProfile(
        name=f"D{rank}:binary-parity",
        local_cell_rank=1,
        cell_count=rank,
        independent_constraint_rank_loss=0,
        residue_alphabet_size=2,
        code_name="binary even-parity code",
        primitive_grade_channel="binary-integer-square",
        primitive_grade=grade,
        primitive_grade_regime=primitive_grade_regime(code, alphabet),
    )
    shadow = GeometryShadowProfile(
        name=f"D{rank}",
        rank=rank,
        primitive_event_count=primitive_count,
        coxeter_root_count_shadow=_coxeter_shadow(rank, primitive_count),
    )
    return _checked_pair(factor, shadow)


def e6_grammar() -> tuple[CausalFactorizationProfile, GeometryShadowProfile]:
    code = ternary_repetition_3_code()
    alphabet = ternary_hexagonal_alphabet()
    grade, primitive_count = e6_primitive_shadow()
    factor = CausalFactorizationProfile(
        name="E6:ternary-hex-repetition",
        local_cell_rank=2,
        cell_count=3,
        independent_constraint_rank_loss=0,
        residue_alphabet_size=3,
        code_name="[3,1,3]_3 repetition",
        primitive_grade_channel="hex-normalized-quadratic",
        primitive_grade=grade,
        primitive_grade_regime=primitive_grade_regime(code, alphabet),
    )
    shadow = GeometryShadowProfile("E6", 6, primitive_count, _coxeter_shadow(6, primitive_count))
    return _checked_pair(factor, shadow)


def e7_grammar() -> tuple[CausalFactorizationProfile, GeometryShadowProfile]:
    code = simplex_7_code()
    alphabet = binary_integer_alphabet()
    grade, primitive_count = primitive_grade_and_multiplicity(code, alphabet)
    factor = CausalFactorizationProfile(
        name="E7:binary-simplex",
        local_cell_rank=1,
        cell_count=7,
        independent_constraint_rank_loss=0,
        residue_alphabet_size=2,
        code_name="[7,3,4]_2 simplex",
        primitive_grade_channel="binary-integer-square",
        primitive_grade=grade,
        primitive_grade_regime=primitive_grade_regime(code, alphabet),
    )
    shadow = GeometryShadowProfile("E7", 7, primitive_count, _coxeter_shadow(7, primitive_count))
    return _checked_pair(factor, shadow)


def e8_binary_grammar() -> tuple[CausalFactorizationProfile, GeometryShadowProfile]:
    code = extended_hamming_8_code()
    alphabet = binary_integer_alphabet()
    grade, primitive_count = primitive_grade_and_multiplicity(code, alphabet)
    factor = CausalFactorizationProfile(
        name="E8:binary-extended-hamming",
        local_cell_rank=1,
        cell_count=8,
        independent_constraint_rank_loss=0,
        residue_alphabet_size=2,
        code_name="[8,4,4]_2 extended Hamming",
        primitive_grade_channel="binary-integer-square",
        primitive_grade=grade,
        primitive_grade_regime=primitive_grade_regime(code, alphabet),
    )
    shadow = GeometryShadowProfile("E8", 8, primitive_count, _coxeter_shadow(8, primitive_count))
    return _checked_pair(factor, shadow)


def e8_ternary_grammar() -> tuple[CausalFactorizationProfile, GeometryShadowProfile]:
    code = ternary_hamming_4_code()
    alphabet = ternary_hexagonal_alphabet()
    grade, primitive_count = ternary_e8_primitive_shadow()
    factor = CausalFactorizationProfile(
        name="E8:ternary-hex-hamming",
        local_cell_rank=2,
        cell_count=4,
        independent_constraint_rank_loss=0,
        residue_alphabet_size=3,
        code_name="[4,2,3]_3 Hamming",
        primitive_grade_channel="hex-normalized-quadratic",
        primitive_grade=grade,
        primitive_grade_regime=primitive_grade_regime(code, alphabet),
    )
    shadow = GeometryShadowProfile("E8", 8, primitive_count, _coxeter_shadow(8, primitive_count))
    return _checked_pair(factor, shadow)


def e8_factorizations_share_geometry_shadow() -> bool:
    binary_factor, binary_shadow = e8_binary_grammar()
    ternary_factor, ternary_shadow = e8_ternary_grammar()
    return binary_shadow == ternary_shadow and binary_factor != ternary_factor
