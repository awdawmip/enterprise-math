"""Execution-depth metrics for CRT-factorized precision representations.

A tuple of pairwise-coprime residue channels already carries the same arithmetic
information as one fused modulus.  If downstream semantics can consume that tuple
directly, no CRT reconstruction is required.

If downstream instead demands one scalar residue modulo the fused modulus, g
channels must be recombined.  With binary CRT merge primitives:

* sequential reconstruction depth is g-1;
* ideal balanced parallel reconstruction depth is ceil(log2 g).

Thus splitting one exact modulus into narrower channels trades peak arithmetic
word width against optional scalar-reconstruction depth.  The depth is an
**interface-conditional** cost, not an intrinsic property of the arithmetic
precision itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .sensor_factorization_pareto import (
    SensorFactorizationPoint,
    sensor_factorization_point,
)


def sequential_crt_reconstruction_depth(channel_count: int) -> int:
    if isinstance(channel_count, bool) or not isinstance(channel_count, int) or channel_count < 1:
        raise ValueError("channel_count must be a positive integer")
    return channel_count - 1


def parallel_crt_reconstruction_depth(channel_count: int) -> int:
    if isinstance(channel_count, bool) or not isinstance(channel_count, int) or channel_count < 1:
        raise ValueError("channel_count must be a positive integer")
    return (channel_count - 1).bit_length()


@dataclass(frozen=True)
class SensorExecutionPoint:
    factorization: SensorFactorizationPoint
    tuple_native_depth: int
    sequential_scalar_reconstruction_depth: int
    parallel_scalar_reconstruction_depth: int

    @property
    def channel_count(self) -> int:
        return self.factorization.channel_count

    @property
    def peak_bit_width(self) -> int:
        return self.factorization.peak_bit_width


def sensor_execution_point(
    prime_factors: Sequence[int],
    grouping: Sequence[Sequence[int]],
) -> SensorExecutionPoint:
    factorization = sensor_factorization_point(prime_factors, grouping)
    count = factorization.channel_count
    return SensorExecutionPoint(
        factorization=factorization,
        tuple_native_depth=0,
        sequential_scalar_reconstruction_depth=sequential_crt_reconstruction_depth(count),
        parallel_scalar_reconstruction_depth=parallel_crt_reconstruction_depth(count),
    )


def scalar_reconstruction_resource_pair(
    point: SensorExecutionPoint,
) -> tuple[int, int]:
    """Return (peak arithmetic bits, ideal parallel CRT reconstruction depth)."""
    return point.peak_bit_width, point.parallel_scalar_reconstruction_depth
