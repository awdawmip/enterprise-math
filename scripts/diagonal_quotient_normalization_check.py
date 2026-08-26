#!/usr/bin/env python3
"""Exact regression checker for the typed diagonal-quotient canonicalizer.

This checker validates only the accepted algebraic/representation laws.  It does
not grant semantic permission to quotient primitive Enterprise point addresses.
"""

from __future__ import annotations

import hashlib
import json
from itertools import product

from enterprise_math.diagonal_quotient import (
    canonical_min_zero,
    compose_canonical,
    diagonal_chart,
    diagonal_shift,
    identity_canonical,
    inverse_canonical,
    is_canonical_min_zero,
    same_diagonal_class,
)


def main() -> int:
    failures: list[dict[str, object]] = []
    counts = {
        "points": 0,
        "shift_cases": 0,
        "class_pairs": 0,
        "composition_cases": 0,
        "inverse_cases": 0,
    }

    points = list(product(range(-4, 5), repeat=3))
    canonical = sorted({canonical_min_zero(point) for point in points})

    for point in points:
        counts["points"] += 1
        can = canonical_min_zero(point)
        if not is_canonical_min_zero(can):
            failures.append({"law": "canonical_shape", "point": point, "can": can})
        if canonical_min_zero(can) != can:
            failures.append({"law": "idempotence", "point": point, "can": can})
        if diagonal_chart(can) != diagonal_chart(point):
            failures.append({"law": "chart_preservation", "point": point, "can": can})
        for k in range(-4, 5):
            counts["shift_cases"] += 1
            shifted = diagonal_shift(point, k)
            if canonical_min_zero(shifted) != can:
                failures.append({"law": "shift_invariance", "point": point, "k": k})

    for left in points:
        for right in points:
            counts["class_pairs"] += 1
            same = same_diagonal_class(left, right)
            expected = canonical_min_zero(left) == canonical_min_zero(right)
            if same != expected:
                failures.append({"law": "class_iff_canonical", "left": left, "right": right})

    sample = canonical[: min(64, len(canonical))]
    for left in sample:
        for right in sample:
            counts["composition_cases"] += 1
            composed = compose_canonical(left, right)
            chart_sum = tuple(a + b for a, b in zip(diagonal_chart(left), diagonal_chart(right)))
            if diagonal_chart(composed) != chart_sum:
                failures.append({"law": "transported_addition", "left": left, "right": right})
            if not is_canonical_min_zero(composed):
                failures.append({"law": "composition_canonical", "left": left, "right": right})

    identity = identity_canonical()
    for point in sample:
        counts["inverse_cases"] += 1
        inv = inverse_canonical(point)
        if compose_canonical(point, inv) != identity:
            failures.append({"law": "inverse", "point": point, "inverse": inv})
        if compose_canonical(point, identity) != point:
            failures.append({"law": "right_identity", "point": point})
        if compose_canonical(identity, point) != point:
            failures.append({"law": "left_identity", "point": point})

    payload = {
        "schema": "ENTERPRISE_MATH_DIAGONAL_QUOTIENT_NORMALIZATION_CHECK_V1",
        "status": "PASS" if not failures else "FAIL",
        "counts": counts,
        "failure_count": len(failures),
        "failures": failures[:20],
        "semantic_boundary": "REPRESENTATION_TOOL_ONLY_DOES_NOT_AUTHORIZE_PRIMITIVE_POINT_QUOTIENT",
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    payload["digest_sha256"] = hashlib.sha256(encoded).hexdigest()
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
