"""A deliberately falsifiable minimum-precision lattice-selection hypothesis.

This module does *not* define physical isotropy or packing optimality.  It records
a low-dimensional causal-coherence heuristic that happened to select the classic
root-lattice sequence A2,A3,D4,D5,E6,E7,E8 before being falsified as a packing
selection rule by the laminated Lambda9 primitive shell.

The heuristic is lexicographic and mechanism-preserving rather than scalar:

1. hard gate: connected regular first link + one rooted edge-context type;
2. prefer fewer connected components inside that common edge context;
3. among ties, prefer later first compatible-flag continuation split.

The Lambda9 shell fails the hard regularity gate despite having higher primitive
relation capacity than D9.  Hence density/capacity and causal homogeneity must be
kept as separate objectives beyond the low-dimensional root-lattice regime.
"""

from __future__ import annotations

from dataclasses import dataclass

from .causal_primitive_link_profile import PrimitiveLinkProfile


@dataclass(frozen=True)
class CoherenceAssessment:
    hard_gate: bool
    edge_context_component_count: int | None
    flag_homogeneity_depth: int
    maximal_flag_size: int
    primitive_count: int
    link_degree: int | None
    pair_context_type_count: int


def causal_coherence_assessment(profile: PrimitiveLinkProfile) -> CoherenceAssessment:
    regular = len(profile.link_degree_histogram) == 1
    connected = len(profile.link_component_sizes) == 1
    edge_uniform = len(profile.edge_context_histogram) == 1
    hard_gate = regular and connected and edge_uniform

    edge_components = None
    if edge_uniform:
        signature, _ = profile.edge_context_histogram[0]
        edge_components = len(signature[3])

    maximal_flag_size = len(profile.flag_extension_histograms)
    split = profile.first_flag_split_order
    # No split through the maximal compatible flag is one step stronger than a
    # split exactly at that maximal flag size.
    homogeneity_depth = split if split is not None else maximal_flag_size + 1

    link_degree = None
    if regular:
        link_degree = profile.link_degree_histogram[0][0]

    return CoherenceAssessment(
        hard_gate=hard_gate,
        edge_context_component_count=edge_components,
        flag_homogeneity_depth=homogeneity_depth,
        maximal_flag_size=maximal_flag_size,
        primitive_count=profile.primitive_count,
        link_degree=link_degree,
        pair_context_type_count=len(profile.pair_context_histogram),
    )


def coherence_preference_key(profile: PrimitiveLinkProfile) -> tuple[int, int, int]:
    """Low-dimensional hypothesis key; lower tuple is preferred.

    The key intentionally ignores primitive count/density.  It is retained only
    as a falsifiable research hypothesis and must not be promoted to a universal
    geometry selection law.
    """
    assessment = causal_coherence_assessment(profile)
    if not assessment.hard_gate:
        return (1, 10**9, 10**9)
    assert assessment.edge_context_component_count is not None
    return (
        0,
        assessment.edge_context_component_count,
        -assessment.flag_homogeneity_depth,
    )


def pareto_coordinates(profile: PrimitiveLinkProfile) -> tuple[int, int, int, int]:
    """Typed coordinates, not a scalar score.

    Returns `(primitive_capacity, local_fragmentation, -homogeneity_depth,
    pair_context_types)`.  No universal ordering is imposed on these axes.
    """
    assessment = causal_coherence_assessment(profile)
    fragmentation = (
        assessment.edge_context_component_count
        if assessment.edge_context_component_count is not None
        else 10**9
    )
    return (
        assessment.primitive_count,
        fragmentation,
        -assessment.flag_homogeneity_depth,
        assessment.pair_context_type_count,
    )
