"""Pinned same-language single-polynomial QS context baseline.

This is deliberately a small, auditable context implementation, not a claim to
match an optimized native quadratic-sieve package.  It reuses the exact
relation verifier and GF(2) dependency extractor used by the valley runs.
"""

from __future__ import annotations

import math
import time
import tracemalloc

from core import RelationEngine, RunMetrics


def run_python_spqs_context(
    target_n: int,
    factor_base_bound: int,
    max_candidates: int,
    timeout_seconds: float,
) -> RunMetrics:
    """Collect Q(x)=x^2-N point relations with a fixed factor base.

    No known factor is accepted by this function.  The polynomial, candidate
    order, stopping condition, matrix, and dependency extraction depend only on
    N and the frozen run specification.
    """

    tracemalloc.start()
    started = time.perf_counter()
    engine = RelationEngine(target_n, 1, factor_base_bound, "none")
    status = "MAX_CANDIDATES"
    candidates = 0
    error = ""
    if engine.immediate_factor is not None:
        engine.matrix.factor = engine.immediate_factor
        status = "FACTOR_BASE_GCD"
    else:
        try:
            x0 = math.isqrt(target_n)
            if x0 * x0 < target_n:
                x0 += 1
            for offset in range(max_candidates):
                if time.perf_counter() - started >= timeout_seconds:
                    status = "TIMEOUT"
                    break
                x = x0 + offset
                value = x * x - target_n
                engine._classify_exact(value, x % target_n, f"spqs-point:{offset}", offset, offset)
                candidates = offset + 1
                if engine.matrix.factor is not None:
                    status = "FACTOR_FOUND"
                    break
        except Exception as exc:  # retained in the result table
            status = "ERROR"
            error = f"{type(exc).__name__}: {exc}"
    wall = time.perf_counter() - started
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return RunMetrics(
        status=status,
        factor=engine.matrix.factor,
        orbit_steps=candidates,
        bands_considered=0,
        bands_opened=0,
        bands_skipped_resource=0,
        total_band_width=0,
        point_candidates=candidates,
        band_candidates=0,
        full_relations=engine.full_relations,
        partial_relations=engine.recombiner.partial_relations,
        dlp_edges=0,
        completed_cycles=0,
        rank=engine.matrix.rank,
        dependencies=engine.matrix.dependencies,
        dependencies_tested=engine.matrix.dependencies_tested,
        wall_seconds=wall,
        peak_memory_bytes=peak,
        stages=engine.stages.as_dict(),
        rank_trajectory_digest=engine.matrix.trajectory_digest(),
        relation_stream_digest=engine.relation_digest.hexdigest(),
        mathematical_relation_digest=engine.math_relation_digest.hexdigest(),
        error=error,
    )
