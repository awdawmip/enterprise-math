#!/usr/bin/env python3
"""Finite enumeration of the R284EU monotone marker transition criterion."""
from itertools import combinations
import json

def ball(center, bits, errors):
    for radius in range(errors + 1):
        for mask_positions in combinations(range(bits), radius):
            word = center
            for bit in mask_positions:
                word ^= 1 << bit
            yield word

def analysis(u, n):
    """C0=0^n, C1=1^n, monotone writer fixes bits in increasing index order."""
    mask = (1 << n) - 1
    possible = []
    for step in range(n + 1):
        physical = (1 << step) - 1
        outputs = set()
        for observed in ball(physical, n, u):
            if observed.bit_count() <= u:
                outputs.add(0)  # must accept at settled C0
            if ((observed ^ mask).bit_count() <= u):
                outputs.add(1)  # must accept at settled C1
        possible.append(sorted(outputs))
    bad = [step for step, outputs in enumerate(possible) if outputs == [0, 1]]
    backward = [(a, b) for a in range(n+1) for b in range(a,n+1)
                if 1 in possible[a] and 0 in possible[b]]
    return {"u": u, "n": n, "ambiguous_prefixes": bad,
            "backward_possible": bool(backward),
            "quiescent_correctable": n >= 2 * u + 1}

def main():
    cases = []
    for u in range(4):
        for n in range(max(1, 2*u+1), 4*u+3):
            result = analysis(u, n)
            assert result["backward_possible"] == (n <= 4*u)
            assert bool(result["ambiguous_prefixes"]) == (n <= 4*u)
            cases.append(result)
    print(json.dumps({"theorem":"n_min=4u+1",
                      "all_tests_passed":True,
                      "tested_u":[0,1,2,3],
                      "case_count":len(cases),
                      "cases":cases}, indent=2, ensure_ascii=False))
if __name__ == "__main__":
    main()
