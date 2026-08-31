#!/usr/bin/env python3
"""Exact equivalence, root-semantics, rank, and negative-control validation."""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path

from core import (
    GF2RelationMatrix,
    Relation,
    StageTimes,
    cfrac_reference_stream,
    factor_base_for,
    invalid_band_root_rejected,
    legendre,
    polynomial_roots_mod_prime,
    primes_up_to,
    perturb_recurrence_sign,
    run_collector,
    verify_paired_equivalence,
)
from corpus import CONFIG_PATH, DEFAULT_OUTPUT, canonical_digest, generate_rows


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research_output" / "VALLEY_BAND_VERIFICATION_SUMMARY_20260823.json"


def read_corpus() -> list[dict[str, str]]:
    with DEFAULT_OUTPUT.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def verify_corpus() -> dict[str, object]:
    generated = generate_rows()
    expected = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))["corpus"]["expected_canonical_digest"]
    digest = canonical_digest(generated)
    existing = read_corpus()
    normalized = [{key: str(value) for key, value in row.items()} for row in generated]
    assert existing == normalized
    assert digest == expected
    return {"rows": len(existing), "canonical_digest": digest, "exact_regeneration": True}


def verify_100k(rows: list[dict[str, str]]) -> dict[str, object]:
    selected = [row for row in rows if row["purpose"] == "state_equivalence"]
    assert len(selected) == 20
    combined = hashlib.sha256()
    per_instance = []
    for row in selected:
        digest = verify_paired_equivalence(int(row["N"]), 1, 5000)
        combined.update(f"{row['corpus_id']}|{digest}\n".encode("ascii"))
        per_instance.append({"corpus_id": row["corpus_id"], "steps": 5000, "digest": digest})
    return {
        "instances": 20,
        "steps_per_instance": 5000,
        "paired_steps": 100000,
        "combined_digest": combined.hexdigest(),
        "per_instance": per_instance,
    }


def verify_band_roots(n: int) -> dict[str, object]:
    total = n
    factor_base, factor = factor_base_for(n, 1, 200)
    assert factor is None
    state = (1, -total, 0)
    root = 1
    previous_root = 0
    checked_states = checked_prime_states = checked_roots = 0
    sqrt_total = math.isqrt(total)
    for step in range(250):
        A, B, C = state
        assert C * C - A * B == total
        a = (sqrt_total + abs(C)) // abs(A)
        for p in factor_base:
            roots = polynomial_roots_mod_prime(A, B, C, total, p)
            brute = tuple(t for t in range(p) if (A * t * t + 2 * C * t + B) % p == 0)
            assert tuple(sorted(roots)) == brute
            checked_prime_states += 1
            for t in roots:
                assert (A * t * t + 2 * C * t + B) % p == 0
                checked_roots += 1
        next_A = A * a * a + 2 * C * a + B
        next_state = (next_A, A, A * a + C)
        next_root = (a * root + previous_root) % n
        assert pow(next_root, 2, n) == next_A % n
        if math.gcd(root, n) == 1:
            for t in range(0, min(a, 8) + 1):
                value = A * t * t + 2 * C * t + B
                root_d = (A * t + C) * pow(root, -1, n) % n
                assert pow(root_d, 2, n) == value % n
        previous_root, root = root, next_root
        state = next_state
        checked_states += 1
    return {
        "states": checked_states,
        "factor_base_prime_states": checked_prime_states,
        "roots": checked_roots,
        "direct_bruteforce_agreement": True,
        "band_relation_identity": True,
    }


def verify_square_multiplier_classes(n: int) -> dict[str, object]:
    pairs = [(1, 4), (3, 12), (5, 45)]
    primes = [p for p in primes_up_to(997) if p > 2]
    checked = 0
    for base, square_multiple in pairs:
        ratio = square_multiple // base
        root = math.isqrt(ratio)
        assert root * root == ratio
        for p in primes:
            if n % p == 0 or root % p == 0:
                continue
            assert legendre(base * n, p) == legendre(square_multiple * n, p)
            checked += 1
    return {
        "pairs": pairs,
        "prime_checks": checked,
        "classification": "same quadratic-character class away from primes dividing the square multiplier; runtime state scaling not identified",
    }


def verify_rank_duplicate_control(n: int) -> dict[str, object]:
    matrix = GF2RelationMatrix(n, [2, 3, 5])
    stages = StageTimes()
    relation = Relation(1, {}, "duplicate-control", 0, 0)
    matrix.add(relation, stages)
    rank_after_one = matrix.rank
    matrix.add(relation, stages)
    assert matrix.rank == rank_after_one == 0
    assert len(matrix.relations) == 2 and matrix.dependencies == 2
    return {
        "raw_relations": 2,
        "rank": matrix.rank,
        "dependencies": matrix.dependencies,
        "demonstrates_raw_count_not_rank": True,
    }


def relation_rank_smoke(n: int) -> dict[str, object]:
    cfrac = run_collector(n, 1, 400, "cfrac_point", "none", 5000, 8)
    closed = run_collector(n, 1, 400, "closed_point", "none", 5000, 8)
    # Keep this correctness smoke comfortably below the deadline on the frozen
    # execution node. Performance measurements live only in the run CSV.
    band = run_collector(n, 1, 400, "closed_band", "slp", 1000, 8, 256)
    assert cfrac.status == closed.status == band.status == "MAX_STEPS"
    assert cfrac.mathematical_relation_digest == closed.mathematical_relation_digest
    assert (cfrac.full_relations, cfrac.rank) == (closed.full_relations, closed.rank)
    assert cfrac.rank > 0

    def deterministic(metrics) -> dict[str, object]:
        """Serialize semantics only; exclude timing, memory, and stage durations."""
        return {
            "status": metrics.status,
            "factor": metrics.factor,
            "orbit_steps": metrics.orbit_steps,
            "bands_considered": metrics.bands_considered,
            "bands_opened": metrics.bands_opened,
            "bands_skipped_resource": metrics.bands_skipped_resource,
            "total_band_width": metrics.total_band_width,
            "point_candidates": metrics.point_candidates,
            "band_candidates": metrics.band_candidates,
            "full_relations": metrics.full_relations,
            "partial_relations": metrics.partial_relations,
            "dlp_edges": metrics.dlp_edges,
            "completed_cycles": metrics.completed_cycles,
            "rank": metrics.rank,
            "dependencies": metrics.dependencies,
            "dependencies_tested": metrics.dependencies_tested,
            "rank_trajectory_digest": metrics.rank_trajectory_digest,
            "relation_stream_digest": metrics.relation_stream_digest,
            "mathematical_relation_digest": metrics.mathematical_relation_digest,
            "error": metrics.error,
        }
    return {
        "cfrac_point": deterministic(cfrac),
        "closed_point": deterministic(closed),
        "closed_band_256_slp": deterministic(band),
        "point_stream_exact_agreement": True,
    }


def main() -> int:
    corpus = verify_corpus()
    rows = read_corpus()
    n = int(next(row["N"] for row in rows if row["corpus_id"] == "E80-00"))
    result = {
        "schema": "valley-band-verification-v1",
        "corpus": corpus,
        "paired_equivalence": verify_100k(rows),
        "band_roots": verify_band_roots(n),
        "square_multiplier_classes": verify_square_multiplier_classes(n),
        "negative_controls": {
            "recurrence_sign_invariant_failure": perturb_recurrence_sign(n),
            "invalid_band_root_rejected": invalid_band_root_rejected(n, 1),
            "posthoc_threshold_selection": "INVALID_BY_FROZEN_CONFIG",
            "raw_count_without_rank": verify_rank_duplicate_control(n),
        },
        "relation_rank_smoke": relation_rank_smoke(n),
    }
    assert result["negative_controls"]["recurrence_sign_invariant_failure"]
    assert result["negative_controls"]["invalid_band_root_rejected"]
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode("utf-8")
    envelope = {"digest": hashlib.sha256(canonical).hexdigest(), "result": result}
    OUTPUT.write_text(json.dumps(envelope, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(OUTPUT),
        "digest": envelope["digest"],
        "paired_steps": result["paired_equivalence"]["paired_steps"],
        "band_root_checks": result["band_roots"]["roots"],
        "smoke_rank": result["relation_rank_smoke"]["cfrac_point"]["rank"],
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
