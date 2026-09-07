"""Staged quadratic-residue tables for BRC square-gap filtering.

The existing checked-in mod-4032 bit table is an excellent first gate, but a
single larger modulus forces every candidate to pay the larger modular
reduction.  This module keeps 4032 as stage one and compiles two small,
pairwise-coprime secondary bit tables once per process:

    12155 = 5*11*13*17
    12673 = 19*23*29

A square must be a quadratic residue at every stage, so the cascade has zero
false negatives.  Because the stage moduli are pairwise coprime, CRT makes the
uniform survival density the exact product of the per-stage densities.

The BALANCED profile uses only 3,609 raw table bytes in total (including the
existing 504-byte 4032 table) while its exact uniform survivor density is
19440/30808063 ~= 0.0006310036, i.e. about 0.0631%.

This is a classical modular square filter composed with the BRC multiplier
pipeline.  It does not change factor-search complexity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt

from .brc_square_gap_tables import SQUARE_RESIDUE_TABLE_4032

CASCADE_STAGE_MODULI = (4032, 12155, 12673)
CASCADE_PROFILES = {
    "BASE": (4032,),
    "COMPACT": (4032, 12155),
    "BALANCED": (4032, 12155, 12673),
}


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _compile_square_residue_bitset(modulus: int) -> bytes:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 0:
        raise ValueError("modulus must be a positive integer")
    table = bytearray((modulus + 7) // 8)
    # x and modulus-x have the same square, so half the representatives suffice.
    for x in range(modulus // 2 + 1):
        residue = (x * x) % modulus
        table[residue >> 3] |= 1 << (residue & 7)
    return bytes(table)


@lru_cache(maxsize=None)
def cascade_table(modulus: int) -> bytes:
    """Return the bit table for one registered cascade stage."""
    if modulus == 4032:
        return SQUARE_RESIDUE_TABLE_4032
    if modulus not in CASCADE_STAGE_MODULI:
        raise ValueError(f"unsupported cascade modulus {modulus}")
    return _compile_square_residue_bitset(modulus)


def _profile_moduli(profile: str) -> tuple[int, ...]:
    try:
        return CASCADE_PROFILES[profile.upper()]
    except (AttributeError, KeyError) as exc:
        raise ValueError(f"unknown cascade profile {profile!r}") from exc


def _passes_table(value: int, modulus: int, table: bytes) -> bool:
    residue = value % modulus
    return bool(table[residue >> 3] & (1 << (residue & 7)))


def passes_square_residue_cascade(value: int, profile: str = "BALANCED") -> bool:
    """Necessary square test with zero false negatives.

    Stages are evaluated in order and stop at the first rejection, so later
    modular reductions are paid only by earlier survivors.
    """
    _require_nonnegative("value", value)
    for modulus in _profile_moduli(profile):
        if not _passes_table(value, modulus, cascade_table(modulus)):
            return False
    return True


def filtered_square_root_cascade(
    value: int, profile: str = "BALANCED"
) -> int | None:
    """Return sqrt(value) only when value is an exact square, otherwise None."""
    if not passes_square_residue_cascade(value, profile):
        return None
    root = isqrt(value)
    return root if root * root == value else None


@lru_cache(maxsize=None)
def square_residue_count_for_stage(modulus: int) -> int:
    return sum(byte.bit_count() for byte in cascade_table(modulus))


def cascade_survival_density(profile: str = "BALANCED") -> Fraction:
    """Exact uniform CRT survival density for a registered profile."""
    density = Fraction(1, 1)
    for modulus in _profile_moduli(profile):
        density *= Fraction(square_residue_count_for_stage(modulus), modulus)
    return density


def cascade_raw_table_bytes(profile: str = "BALANCED") -> int:
    return sum(len(cascade_table(modulus)) for modulus in _profile_moduli(profile))


@dataclass(frozen=True)
class CascadeProfileStats:
    profile: str
    moduli: tuple[int, ...]
    raw_table_bytes: int
    survival_density: Fraction

    @property
    def rejection_density(self) -> Fraction:
        return 1 - self.survival_density


def cascade_profile_stats(profile: str = "BALANCED") -> CascadeProfileStats:
    name = profile.upper()
    return CascadeProfileStats(
        profile=name,
        moduli=_profile_moduli(name),
        raw_table_bytes=cascade_raw_table_bytes(name),
        survival_density=cascade_survival_density(name),
    )


__all__ = [
    "CASCADE_STAGE_MODULI",
    "CASCADE_PROFILES",
    "CascadeProfileStats",
    "cascade_table",
    "passes_square_residue_cascade",
    "filtered_square_root_cascade",
    "square_residue_count_for_stage",
    "cascade_survival_density",
    "cascade_raw_table_bytes",
    "cascade_profile_stats",
]
