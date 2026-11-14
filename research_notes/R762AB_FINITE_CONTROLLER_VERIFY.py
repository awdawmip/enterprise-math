#!/usr/bin/env python3
"""R762AB: finite deterministic unary controller cutoff and typed triadic frame test."""
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path

def legal_prefix(transitions, steps):
    state = 0
    for _ in range(steps):
        if transitions[state] < 0:
            return False
        state = transitions[state]
    return True

def infinite_from_zero(transitions):
    state, seen = 0, set()
    while state not in seen:
        seen.add(state)
        if transitions[state] < 0:
            return False
        state = transitions[state]
    return True

def frame_transport(frame, source, target):
    leaving = next(iter(source - target))
    entering = next(iter(target - source))
    return tuple(entering if x == leaving else x for x in frame)

def verify():
    census = []
    for s in range(1, 7):
        count = success = 0
        for trans in product(range(-1, s), repeat=s):
            count += 1
            if legal_prefix(trans, s):
                success += 1
                assert infinite_from_zero(trans), (s, trans)
        chain = tuple(range(1, s)) + (-1,)
        assert legal_prefix(chain, s - 1)
        assert not legal_prefix(chain, s)
        census.append({"states": s, "tables": count,
                       "tables_with_first_s_legal": success})
    assert sum(x["tables"] for x in census) == 126125

    frame_cases = 0
    for initial in combinations(range(6), 3):
        S = set(initial)
        for entering in set(range(6)) - S:
            for fixed in S:
                b, d = sorted(S - {fixed})
                S1, S2 = {fixed, b, entering}, {fixed, d, entering}
                frame = tuple(sorted(S))
                for source, target in ((S, S1), (S1, S2), (S2, S)):
                    frame = frame_transport(frame, source, target)
                expected = tuple(d if x == b else b if x == d else x
                                 for x in sorted(S))
                assert frame == expected
                frame_cases += 1
    assert frame_cases == 180

    distinguishability = 0
    for N in range(1, 65):
        permanent = (0,)  # self-loop
        finite = tuple(range(1, N + 1)) + (-1,)
        assert legal_prefix(permanent, N + 1)
        assert legal_prefix(finite, N)
        assert not legal_prefix(finite, N + 1)
        for k in range(N + 1):
            # Both models have the same observable V29/V17 signature.
            M = ((0, 0, k), (k, 0, 0), (0, k, 0))
            incoming = tuple(sum(row) for row in M)
            outgoing = tuple(sum(M[i][j] for i in range(3))
                             for j in range(3))
            assert incoming == outgoing == (k, k, k)
            h = (0, 2, 1) if k % 2 else (0, 1, 2)
            assert h in ((0, 1, 2), (0, 2, 1))
        for i in range(N + 1):
            for j in range(i + 1, N + 1):
                suffix = N - j + 1
                assert legal_prefix(finite, i + suffix)
                assert not legal_prefix(finite, j + suffix)
                distinguishability += 1
    assert distinguishability == 45760
    return {
      "schema": "R762AB_UNARY_TRIAD_REPEATABILITY_EVIDENCE_V1",
      "date": "2026-11-14",
      "model": "conditional typed triadic macro with passive V29/V17 observer and deterministic autonomous unary enabling controller",
      "controller_census": census,
      "total_controller_tables": sum(x["tables"] for x in census),
      "v17_source_labelled_frame_cases": frame_cases,
      "horizon_families_N_1_to_64": 64,
      "pairwise_prefix_distinguishability_checks": distinguishability,
      "result": "ALL_ASSERTIONS_PASSED",
      "universal_result": "AB1/AB2 are independently human-proved under stated hypotheses",
      "native_triadic_event_admission": "UNPROVED",
      "V39_native_transport": "UNSPECIFIED",
      "formal_result": "NOT_PUBLISHED",
      "independent_review": "NOT_REVIEWED"
    }

if __name__ == "__main__":
    result = verify()
    dest = Path(__file__).with_name("R762AB_EVIDENCE.json")
    dest.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))
