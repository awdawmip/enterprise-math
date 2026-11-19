#!/usr/bin/env python3
"""X6 Unit164 exact R061 relative-observer spectrum fiber checker.

Fixed positive chart a=max(coordinates)>0, 0<=b<=a; NOT a six-axis
native metric or physical rotation certificate.
"""
from collections import defaultdict
from math import comb
import json

def check(limit=128):
    fibers = defaultdict(list)
    for a in range(1, limit + 1):
        for b in range(a + 1):
            forward = a*a + b*b
            reverse = a*a + (a-b)*(a-b)
            key = tuple(sorted((forward, reverse)))
            fibers[key].append((a, b, comb(a+b, b)))
    singletons = doubletons = 0
    for key, records in fibers.items():
        s, t = key
        S, D = s + t, t - s
        candidates = [a for a in range(1, limit + 1)
                      if 5*a**4 - 2*S*a*a + D*D == 0]
        assert len(candidates) == 1, (key, candidates)
        a = candidates[0]
        assert D % a == 0
        u = D // a
        assert u <= a and (a-u) % 2 == 0
        candidates_b = {(a-u)//2, (a+u)//2}
        assert {(aa, b) for aa,b,_ in records} == {(a,b) for b in candidates_b}
        assert len(records) == len(candidates_b)
        if len(records) == 1:
            singletons += 1
        else:
            doubletons += 1
            assert records[0][2] != records[1][2], (key, records)
    return {
        "schema": "X6_UNIT164_R061_SPECTRUM_FIBER_CHECK_V1",
        "historical_source_commit": "fd2bcff10ca6e147348b6c1236027fc0d2877df3",
        "input_limit_a": limit,
        "canonical_chart_states": sum(a + 1 for a in range(1, limit+1)),
        "distinct_unordered_spectra": len(fibers),
        "singleton_fibers": singletons,
        "doubleton_fibers": doubletons,
        "checks": "PASS",
        "witness_1": {"input": [[1,0,0],[1,1,0]], "squared_spectrum": [1,2], "native_squared_lengths": [1,2], "native_n_brc": [1,2]},
        "witness_3": {"input": [[3,1,0],[3,2,0]], "squared_spectrum": [10,13], "native_squared_lengths": [10,13], "native_n_brc": [4,10]},
        "historical_python_tests_executed": False,
        "native_R063_benchmark_rerun": False
    }

if __name__ == "__main__":
    print(json.dumps(check(), indent=2, ensure_ascii=False, sort_keys=True))
