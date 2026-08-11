"""Rounded storage overhead for CRT-factorized residue precision.

For pairwise-coprime channel moduli M_i with product L, ideal information content
is invariant:

    sum log2(M_i) = log2(L).

If each residue channel is stored in the minimum whole number of bits

    b_i = ceil(log2 M_i),

and the fused residue needs

    B = ceil(log2 L),

then pure per-channel rounding overhead obeys

    0 <= sum b_i - B <= g-1.

So CRT splitting can greatly reduce *peak* arithmetic word width while adding at
most one bit of rounded storage overhead per additional channel.  Other costs
(channel metadata, routing, synchronization, reconstruction) are separate and
must not be hidden inside this information-width theorem.
"""

from __future__ import annotations

from .sensor_factorization_pareto import (
    SensorFactorizationPoint,
    residue_bit_width,
)


def fused_residue_bit_width(point: SensorFactorizationPoint) -> int:
    return residue_bit_width(point.fused_modulus)


def rounded_storage_overhead(point: SensorFactorizationPoint) -> int:
    return point.total_rounded_bit_width - fused_residue_bit_width(point)


def rounded_storage_overhead_bound(point: SensorFactorizationPoint) -> int:
    return point.channel_count - 1


def verify_rounded_storage_law(point: SensorFactorizationPoint) -> bool:
    overhead = rounded_storage_overhead(point)
    bound = rounded_storage_overhead_bound(point)
    if not 0 <= overhead <= bound:
        raise AssertionError("CRT rounded storage overhead exceeded g-1 theorem")
    return True
