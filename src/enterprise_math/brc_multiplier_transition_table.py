"""Dyadic predictor table for consecutive BRC multiplier roots.

For m=1..99 define gamma_m=sqrt((m+1)/m)-1. Five checked-in payload
shards store C_m=floor(2**2053*gamma_m), enough for the common static fast
path bit_length(N)<=4096, m<=100. Lower precisions are exact right shifts.

Larger N use the same proved transition with a cached exact runtime predictor
generator. The static bytes are derived classical integer-root data, not theorem
content.
"""

from __future__ import annotations

from functools import lru_cache
from math import isqrt

from .brc_multiplier_transition_table_shard0 import PAYLOAD as _S0
from .brc_multiplier_transition_table_shard1 import PAYLOAD as _S1
from .brc_multiplier_transition_table_shard2 import PAYLOAD as _S2
from .brc_multiplier_transition_table_shard3 import PAYLOAD as _S3
from .brc_multiplier_transition_table_shard4 import PAYLOAD as _S4

MAX_MULTIPLIER = 100
MAX_STATIC_N_BITS = 4096
MAX_STATIC_FRACTION_BITS = 2053
ENTRY_BYTES = 257
ENTRY_COUNT = 99
RAW_PAYLOAD_BYTES = 25443
TABLE_SHA256 = "b434d3be1f2c6a8f6a32276e7fa4660fd554969d5f32021e3e5c0504633c1003"

_TRANSITION_GAMMA_TABLE = _S0 + _S1 + _S2 + _S3 + _S4
if len(_TRANSITION_GAMMA_TABLE) != RAW_PAYLOAD_BYTES:
    raise AssertionError("BRC transition predictor table payload length mismatch")


def _require_n_bits(n_bits: int) -> None:
    if isinstance(n_bits, bool) or not isinstance(n_bits, int) or n_bits <= 0:
        raise ValueError("n_bits must be a positive integer")


def fraction_bits_for_n_bits(n_bits: int) -> int:
    """Return B such that every m<=100 root j satisfies j<2**(B-1)."""
    _require_n_bits(n_bits)
    return (n_bits + 8) // 2 + 1


@lru_cache(maxsize=1)
def high_precision_constants() -> tuple[int, ...]:
    return tuple(
        int.from_bytes(
            _TRANSITION_GAMMA_TABLE[i * ENTRY_BYTES : (i + 1) * ENTRY_BYTES],
            "big",
        )
        for i in range(ENTRY_COUNT)
    )


def _generate_constants(fraction_bits: int) -> tuple[int, ...]:
    scale = 1 << fraction_bits
    return tuple(
        isqrt((((m + 1) << (2 * fraction_bits)) // m)) - scale
        for m in range(1, MAX_MULTIPLIER)
    )


@lru_cache(maxsize=None)
def transition_constants_for_n_bits(
    n_bits: int,
) -> tuple[int, tuple[int, ...], str]:
    """Return ``(B, constants, mode)``.

    ``STATIC`` uses the checked-in <=4096-bit table. Above that, the same exact
    constants are built once and cached as ``DYNAMIC_CACHED``.
    """
    B = fraction_bits_for_n_bits(n_bits)
    if n_bits <= MAX_STATIC_N_BITS:
        shift = MAX_STATIC_FRACTION_BITS - B
        constants = tuple(value >> shift for value in high_precision_constants())
        return B, constants, "STATIC"
    return B, _generate_constants(B), "DYNAMIC_CACHED"


def regenerate_high_precision_constants() -> tuple[int, ...]:
    return _generate_constants(MAX_STATIC_FRACTION_BITS)


def regenerated_payload() -> bytes:
    return b"".join(
        value.to_bytes(ENTRY_BYTES, "big")
        for value in regenerate_high_precision_constants()
    )


__all__ = [
    "MAX_MULTIPLIER",
    "MAX_STATIC_N_BITS",
    "MAX_STATIC_FRACTION_BITS",
    "ENTRY_BYTES",
    "ENTRY_COUNT",
    "RAW_PAYLOAD_BYTES",
    "TABLE_SHA256",
    "fraction_bits_for_n_bits",
    "high_precision_constants",
    "transition_constants_for_n_bits",
    "regenerate_high_precision_constants",
    "regenerated_payload",
]
