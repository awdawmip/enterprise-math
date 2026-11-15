#!/usr/bin/env python3
"""Exact DFA one-flip residual counter and independent finite word checks."""
from collections import defaultdict
import itertools
import json
from pathlib import Path
import random

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"


def accepts(delta, start, F, bits):
    q = start
    for bit in bits:
        q = delta[q][bit]
    return q in F


def residual_count(delta, start, F, ell):
    """Return (number accepted, number isolated in induced Hamming-1 graph, state count)."""
    state_count = {(start, frozenset()): 1}
    for _ in range(ell):
        nxt = defaultdict(int)
        for (q, R), weight in state_count.items():
            for b in (0, 1):
                q2 = delta[q][b]
                R2 = frozenset([delta[q][1 - b]] +
                               [delta[r][b] for r in R])
                nxt[(q2, R2)] += weight
        state_count = nxt
    N = sum(w for (q, R), w in state_count.items() if q in F)
    I = sum(w for (q, R), w in state_count.items()
            if q in F and R.isdisjoint(F))
    return N, I, len(state_count)


def direct_count(delta, start, F, ell):
    words = {b for b in itertools.product((0, 1), repeat=ell)
             if accepts(delta, start, F, b)}
    isolated = sum(not any(tuple((1-v if k == j else v)
                                 for k, v in enumerate(b)) in words
                           for j in range(ell))
                   for b in words)
    return len(words), isolated


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    no11 = ((0, 1), (0, 2), (2, 2))
    fibonacci = []
    for ell in range(1, 23):
        N, I, states = residual_count(no11, 0, frozenset((0, 1)), ell)
        assert N == fib(ell + 2) and I == 0
        if ell <= 10:
            assert (N, I) == direct_count(no11, 0, frozenset((0, 1)), ell)
        fibonacci.append({"ell": ell, "N": N, "I": I, "residual_states": states})

    uniform = ((1, 2), (1, 3), (3, 2), (3, 3))
    constant_bits = []
    for ell in range(1, 20):
        N, I, states = residual_count(uniform, 0, frozenset((1, 2)), ell)
        assert (N, I) == (2, 0 if ell == 1 else 2)
        if ell <= 10:
            assert (N, I) == direct_count(uniform, 0, frozenset((1, 2)), ell)
        constant_bits.append({"ell": ell, "N": N, "I": I, "residual_states": states})

    exhaustive_two = 0
    for trans in itertools.product((0, 1), repeat=4):
        delta = ((trans[0], trans[1]), (trans[2], trans[3]))
        for start in (0, 1):
            for fmask in range(4):
                F = frozenset(q for q in range(2) if (fmask >> q) & 1)
                for ell in range(8):
                    N, I, _ = residual_count(delta, start, F, ell)
                    assert (N, I) == direct_count(delta, start, F, ell)
                    exhaustive_two += 1

    rng = random.Random(20261115)
    sampled_three = 0
    for _ in range(300):
        delta = tuple(tuple(rng.randrange(3) for _ in range(2))
                      for _ in range(3))
        start = rng.randrange(3)
        F = frozenset(q for q in range(3) if rng.randrange(2))
        for ell in range(7):
            N, I, _ = residual_count(delta, start, F, ell)
            assert (N, I) == direct_count(delta, start, F, ell)
            sampled_three += 1

    result = {
        "status": "PASS_R5_DFA_ONE_FLIP_OBSERVER",
        "frozen_science_pin": PIN,
        "claim": "exact accepted counts and isolated accepted word counts via DFA residual (q,R)",
        "two_state_dfa_exhaustive_checks": exhaustive_two,
        "three_state_dfa_seeded_sample_checks": sampled_three,
        "fibonacci": fibonacci,
        "constant_bits": constant_bits,
    }
    path = Path(__file__).with_name("EXACT_DFA_ONE_FLIP_EVIDENCE.json")
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")
    print(result["status"], "two-state", exhaustive_two,
          "sampled-three-state", sampled_three)
    print("output:", path)


if __name__ == "__main__":
    main()
