"""Narrowed T1 triaxial directional-defect subtool.

NO NEW MATHEMATICS integration adapter.  The executable operator core is the
independently verified implementation frozen at b1f79d2314de2d1ae1511a693cdf37e7c7812cf8.
This public surface keeps full-field adjoint semantics separate from compressed
native-hex Gram semantics and makes frame/domain/coefficient assumptions explicit.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Mapping, Sequence, Tuple

from . import _triaxial_directional_defect_core as _core

Point = _core.Point
Triple = _core.Triple
SparseField = _core.SparseField
Kernel = _core.Kernel

_VERIFIED_CHARACTERISTICS = (0, 2, 3, 5, 7)


@dataclass(frozen=True)
class CoefficientDomain:
    characteristic: int = 0

    def __post_init__(self) -> None:
        if self.characteristic not in _VERIFIED_CHARACTERISTICS:
            raise ValueError(
                "integration surface is frozen to verified characteristics 0,2,3,5,7"
            )


@dataclass(frozen=True)
class NativeHexDomain:
    radius: int

    def __post_init__(self) -> None:
        if self.radius < 0:
            raise ValueError("native-hex radius must be nonnegative")


@dataclass(frozen=True)
class DeclaredFrame:
    seed: Triple
    directions: Tuple[Point, Point, Point]
    width: int
    primitive: bool
    canonical: bool
    unoriented_rays: Tuple[Point, Point, Point]


@dataclass(frozen=True)
class UniquenessCertificate:
    domain: NativeHexDomain
    characteristic: int
    frame_count: int
    total_width: int
    row_count: int
    column_count: int
    rank: int
    nullity: int
    unique: bool


@dataclass(frozen=True)
class ExposedAugmentCertificate:
    domain: NativeHexDomain
    characteristic: int
    exposed_vertex: Point
    exposing_weight: Point
    dimension: int
    rank: int
    unimodular_full_rank: bool


@dataclass(frozen=True)
class FullAdjointResult:
    field: SparseField
    characteristic: int
    domain: str = "FULL_SPARSE_FIELD"
    codomain: str = "FULL_SPARSE_FIELD"


@dataclass(frozen=True)
class CompressedGramCertificate:
    domain: NativeHexDomain
    characteristic: int
    basis: Tuple[Point, ...]
    matrix: Tuple[Tuple[int, ...], ...]
    rank: int
    nonsingular: bool


@dataclass(frozen=True)
class GramFactorCertificate:
    gram_kernel: Kernel
    directional_laplacian_product_kernel: Kernel
    factorization_matches: bool


def _canonical_unoriented(direction: Point) -> Point:
    dx, dy = direction
    g = gcd(abs(dx), abs(dy))
    if g == 0:
        raise ValueError("zero direction")
    d = (dx // g, dy // g)
    rev = (-d[0], -d[1])
    return min(d, rev)


def DECLARE_FRAME(seed: Triple) -> DeclaredFrame:
    frame = _core.declare_frame(seed)
    if not _core.is_canonical_seed(seed):
        raise ValueError("frame seed must be canonical")
    if not frame.primitive:
        raise ValueError("T1 tomography/width interface requires a primitive frame")
    rays = tuple(sorted(_canonical_unoriented(d) for d in frame.directions))
    if len(set(rays)) != 3:
        raise ValueError("unoriented frame rays must be distinct")
    return DeclaredFrame(seed, frame.directions, frame.width, True, True, rays)


def _as_core(frame: DeclaredFrame) -> _core.Frame:
    return _core.declare_frame(frame.seed)


def _dedup_seeds(seeds: Sequence[Triple]) -> Tuple[Triple, ...]:
    out = []
    seen = set()
    for seed in seeds:
        frame = DECLARE_FRAME(seed)
        key = frame.unoriented_rays
        if key in seen:
            continue
        seen.add(key)
        out.append(seed)
    return tuple(out)


def _rank(matrix, coefficients: CoefficientDomain) -> int:
    if coefficients.characteristic == 0:
        return _core.rank_q(matrix)
    return _core.rank_mod(matrix, coefficients.characteristic)


def _reduce_field(field: Mapping[Point, int], coefficients: CoefficientDomain) -> SparseField:
    if coefficients.characteristic == 0:
        return dict(field)
    p = coefficients.characteristic
    return {x: v % p for x, v in field.items() if v % p}


def DIFF1(field: Mapping[Point, int], direction: Point) -> SparseField:
    return _core.diff1(field, direction)


def RHOMBUS2(field: Mapping[Point, int], direction_i: Point, direction_j: Point) -> SparseField:
    return _core.rhombus2(field, direction_i, direction_j)


def TRIPLE_DEFECT(field: Mapping[Point, int], frame: DeclaredFrame) -> SparseField:
    return _core.triple_defect(field, _as_core(frame))


def XRAY_KERNEL_CERT(seed_field: Mapping[Point, int], seeds: Sequence[Triple]) -> bool:
    return _core.xray_kernel_cert(seed_field, _dedup_seeds(seeds))


def FRAME_WIDTH(frame: DeclaredFrame) -> int:
    return frame.width


def MULTIFRAME_UNIQUENESS(
    seeds: Sequence[Triple],
    domain: NativeHexDomain,
    coefficients: CoefficientDomain = CoefficientDomain(),
) -> UniquenessCertificate:
    unique_seeds = _dedup_seeds(seeds)
    matrix, points = _core.xray_matrix(unique_seeds, domain.radius)
    rank = _rank(matrix, coefficients)
    columns = len(points)
    nullity = columns - rank
    return UniquenessCertificate(
        domain=domain,
        characteristic=coefficients.characteristic,
        frame_count=len(unique_seeds),
        total_width=_core.family_width(unique_seeds),
        row_count=len(matrix),
        column_count=columns,
        rank=rank,
        nullity=nullity,
        unique=(nullity == 0),
    )


def EXPOSED_AUGMENT(
    seeds: Sequence[Triple],
    domain: NativeHexDomain,
    coefficients: CoefficientDomain = CoefficientDomain(),
) -> ExposedAugmentCertificate:
    unique_seeds = _dedup_seeds(seeds)
    matrix, basis, exposed, weight = _core.exposed_vertex_sampling_matrix(
        unique_seeds, domain.radius
    )
    rank = _rank(matrix, coefficients)
    return ExposedAugmentCertificate(
        domain=domain,
        characteristic=coefficients.characteristic,
        exposed_vertex=exposed,
        exposing_weight=weight,
        dimension=len(basis),
        rank=rank,
        unimodular_full_rank=(rank == len(basis)),
    )


def FULL_ADJOINT(
    field: Mapping[Point, int],
    frame: DeclaredFrame,
    coefficients: CoefficientDomain = CoefficientDomain(),
) -> FullAdjointResult:
    g = _core.triple_defect_kernel(_as_core(frame))
    adj = _core.adjoint_kernel(g)
    result = _core.apply_kernel(field, adj)
    return FullAdjointResult(_reduce_field(result, coefficients), coefficients.characteristic)


CHIRALITY_ADJOINT = FULL_ADJOINT


def GRAM_FACTOR(frame: DeclaredFrame) -> GramFactorCertificate:
    core_frame = _as_core(frame)
    gram = _core.gram_factor_kernel(core_frame)
    lap = _core.laplacian_product_kernel(core_frame)
    return GramFactorCertificate(gram, lap, gram == lap)


def COMPRESSED_GRAM(
    seeds: Sequence[Triple],
    domain: NativeHexDomain,
    coefficients: CoefficientDomain = CoefficientDomain(),
) -> CompressedGramCertificate:
    unique_seeds = _dedup_seeds(seeds)
    matrix, basis = _core.gram_matrix(unique_seeds, domain.radius)
    rank = _rank(matrix, coefficients)
    frozen_matrix = tuple(tuple(v for v in row) for row in matrix)
    return CompressedGramCertificate(
        domain=domain,
        characteristic=coefficients.characteristic,
        basis=tuple(basis),
        matrix=frozen_matrix,
        rank=rank,
        nonsingular=(rank == len(basis)),
    )


def TRACE_CUBE_STATES(frame: DeclaredFrame):
    """Return eight typed trace states; endpoint coalescence is not trace identity."""
    return tuple(_core.eight_state_trace_cube(_as_core(frame)))


def ENDPOINT_STENCIL(frame: DeclaredFrame) -> Kernel:
    return _core.six_point_endpoint_stencil(_as_core(frame))


def HIVE_BRIDGE(field: Mapping[Point, int], frame: DeclaredFrame):
    return _core.hive_bridge_values(field, _as_core(frame))


def PRIMITIVE_FRAME_CENSUS(width: int, oriented: bool = False):
    return _core.primitive_frame_census(width, oriented)


def EULER_PHI(width: int) -> int:
    return _core.euler_phi(width)


def FINITE_SUPPORT_LEFT_INVERSE_POSSIBLE(frame: DeclaredFrame) -> bool:
    return _core.finite_support_left_inverse_possible(
        _core.triple_defect_kernel(_as_core(frame))
    )


__all__ = [
    "CoefficientDomain", "NativeHexDomain", "DeclaredFrame",
    "UniquenessCertificate", "ExposedAugmentCertificate", "FullAdjointResult",
    "CompressedGramCertificate", "GramFactorCertificate",
    "DECLARE_FRAME", "DIFF1", "RHOMBUS2", "TRIPLE_DEFECT",
    "XRAY_KERNEL_CERT", "FRAME_WIDTH", "MULTIFRAME_UNIQUENESS",
    "EXPOSED_AUGMENT", "FULL_ADJOINT", "CHIRALITY_ADJOINT",
    "COMPRESSED_GRAM", "GRAM_FACTOR", "TRACE_CUBE_STATES",
    "ENDPOINT_STENCIL", "HIVE_BRIDGE", "PRIMITIVE_FRAME_CENSUS",
    "EULER_PHI", "FINITE_SUPPORT_LEFT_INVERSE_POSSIBLE",
]
