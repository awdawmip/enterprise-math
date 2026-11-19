#!/usr/bin/env python3
"""Exact Boolean-BRC provenance-language checker for R30 conditional labelled X6 carrier.

Carrier: boolean set of full signed-Port / named-gate words. This checks the
specified conditional transition system, not native TRIADIC_CLOSURE_E admission.
"""
from functools import lru_cache
from itertools import product
import json

@lru_cache(None)
def lang(m, covers, theta, phase, done, fired, h):
    # The empty word is included. The returned tuple is a sorted, deterministic
    # set of successful fully labelled paths, with no collapsed source identity.
    if h == 0:
        return frozenset({()})
    out = {()}
    union = 0
    for j, mask in enumerate(covers):
        if fired & (1 << j):
            union |= mask
    for i in range(m):
        p = phase[i]
        if p < 2:
            newphase = phase[:i] + (p+1,) + phase[i+1:]
            lab = f"T{i}{'+' if p == 0 else '-'}"
            for w in lang(m, covers, theta, newphase, done, fired, h-1):
                out.add((lab,) + w)
        elif not (done & (1 << i)) and ((theta | union) & (1 << i)):
            for w in lang(m, covers, theta, phase, done | (1 << i), fired, h-1):
                out.add((f"Q{i}",) + w)
    for j in range(len(covers)):
        if not (fired & (1 << j)):
            for w in lang(m, covers, theta, phase, done, fired | (1 << j), h-1):
                out.add((f"B{j}",) + w)
    return frozenset(out)


def run():
    checks = 0
    configurations = 0
    full_erasure_witnesses = 0
    maximum_language_size = 0
    by_m = []
    for m in range(1, 4):
        ck = 0
        cf = 0
        # zero to two named broadcast gates, each with arbitrary coverage.
        for q in range(3):
            for covers in product(range(1 << m), repeat=q):
                for fired in range(1 << q):
                    union = 0
                    for j, mask in enumerate(covers):
                        if fired & (1 << j):
                            union |= mask
                    signatures = {}
                    for theta in range(1 << m):
                        for h in range(4):
                            v = lang(m, covers, theta, (0,) * m, 0, fired, h)
                            signatures[theta, h] = v
                            maximum_language_size = max(maximum_language_size, len(v))
                    for a in range(1 << m):
                        for b in range(1 << m):
                            for h in range(4):
                                actual = signatures[a, h] == signatures[b, h]
                                predicted = (h <= 2 or ((a ^ b) & ~union) == 0)
                                assert actual == predicted, (m, covers, fired, a, b, h)
                                checks += 1
                                ck += 1
                    if union == (1 << m) - 1:
                        # Once the public broadcasts cover all indices, the
                        # hidden assignments are language equivalent at all h.
                        assert len({signatures[theta, 3] for theta in range(1 << m)}) == 1
                        full_erasure_witnesses += 1
                    cf += 1
                    configurations += 1
        by_m.append({"m": m, "configurations": cf, "pair_horizon_checks": ck})
    return {
        "schema": "EM_X6_R30_BOOLEAN_BRC_CHECK_V1",
        "model": "conditional labelled signed-Port, one-shot probe, monotone Link broadcast carrier",
        "scope": "all m=1..3, 0..2 broadcasts, all coverage masks, all fired subsets, all theta pairs, h=0..3",
        "result": "PASS",
        "configurations": configurations,
        "pair_horizon_checks": checks,
        "all_bit_erasure_configurations": full_erasure_witnesses,
        "largest_exact_language_cardinality": maximum_language_size,
        "by_m": by_m,
        "math_inference": "Exact finite model coverage only; unbounded m and h follow from written proof.",
        "native_event_admission": "NOT_ESTABLISHED",
        "independent_review": "NOT_REVIEWED"
    }

if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
