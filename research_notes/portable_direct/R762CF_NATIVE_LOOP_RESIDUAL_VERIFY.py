#!/usr/bin/env python3
"""Exact finite witness checks for R762CF; universal q>=2 proof is in the accompanying theorem."""
from collections import Counter
from itertools import permutations, product
from json import dumps

AXES = (1, 2, 3)
SIGNS = (1, -1, 1)

def loop_word(kind, j, axes=AXES, signs=SIGNS):
    a = axes[j] * signs[j]
    b = axes[(j + 1) % 3] * signs[(j + 1) % 3]
    if kind == "B":
        return (a, -a, b, -b)
    if kind == "L":
        return (a, b, -a, -b)
    raise ValueError(kind)

def endpoint(word):
    d = [0] * 6
    for v in word:
        d[abs(v) - 1] += 1 if v > 0 else -1
    return tuple(d)

def coarse(word):
    return (endpoint(word), len(word), tuple(sorted(Counter(word).items())))

def evolve(q, r, word):
    for event in word:
        if event == "L":
            r = (r + 1) % q
        elif event == "B":
            pass
        elif event == "T":
            if r != 0:
                return False, r
        else:
            raise AssertionError(event)
    return True, r

def main():
    samples = []
    for q in range(2, 17):
        paths = []
        for r in range(q):
            path = loop_word("B", 0) * (q-r) + loop_word("L", 0) * r
            assert len(path) == 4*q
            assert endpoint(path) == (0,0,0,0,0,0)
            assert evolve(q, 0, "B"*(q-r)+"L"*r) == (True, r)
            paths.append(path)
        assert len({coarse(p) for p in paths}) == 1
        for r, s in product(range(q), repeat=2):
            if r == s:
                continue
            probe = "L"*((-r) % q) + "T"
            assert evolve(q, r, probe)[0]
            assert not evolve(q, s, probe)[0]
        for h in range(q+4):
            signatures = {
                tuple(evolve(q,r,"L"*k+"T")[0] for k in range(h+1))
                for r in range(q)
            }
            assert len(signatures) == min(q,h+2), (q,h)
        for perm in permutations((1,2,3,4,5,6)):
            axes = perm[:3]
            for signs in product((-1,1), repeat=3):
                for j in range(3):
                    assert coarse(loop_word("B", j, axes, signs)) == coarse(loop_word("L", j, axes, signs))
        samples.append({
            "q":q,
            "same_observation_states":q,
            "fixed_repair_bits":(q-1).bit_length(),
            "witness_primitive_steps":4*q,
            "pairwise_future_distinctions":q*(q-1),
            "finite_horizon_checked_through":q+3
        })
    result = {
        "schema":"R762CF_CONDITIONAL_LOOP_RESIDUAL_EVIDENCE_V1",
        "scope":"Exact finite q=2..16; full S6(720) x 8 signs x 3 rooted pairs; the theorem proves arbitrary q>=2",
        "samples":samples,
        "all_assertions_passed":True
    }
    print(dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
