#!/usr/bin/env python3
"""PREFIX-982: signed-port branching and sharp finite triple (exact integers).

Original source identity (i,j,s) is reconstructed from each residual, port,
and current input bit. Auxiliary XOR observer, not a native X6 embedding.
"""
from collections import defaultdict
from itertools import product
from functools import lru_cache
import json
import random

def residual_ports(p):
    d = defaultdict(lambda: defaultdict(set))
    for i in range(p):
        for j in range(1, p):
            for s in (1, -1):
                d[(1 << i) - s * (1 << j)][j].add(int(s == -1))
    return {a: {j: frozenset(bits) for j, bits in ports.items()}
            for a, ports in d.items()}

def exact_fiber_mass(p, word, n, dictionary):
    """Formula 982.1, sum over named port skeletons, factor by initial bit."""
    choices = [tuple(dictionary[word[t % len(word)]]) for t in range(n)]
    total = 0
    for ports in product(*choices):
        parity = [0] * p
        possible = [3] * p
        possible[0] = 2  # odd input bit zero fixed to 1
        for t, j in enumerate(ports):
            allowed = dictionary[word[t % len(word)]][j]
            shifted = 0
            for b in allowed:
                shifted |= 1 << (b ^ parity[j])
            possible[j] &= shifted
            parity[j] ^= 1
            if not possible[j]:
                break
        else:
            count = 1
            for mask in possible[1:]:
                count *= mask.bit_count()
            total += count
    return total

def direct_mass(p, word, n, dictionary):
    """Independent original XOR-state enumeration with named branch counts."""
    amounts = {x: 1 for x in range(1, 1 << p, 2)}
    for t in range(n):
        ports = dictionary[word[t % len(word)]]
        nxt = defaultdict(int)
        for x, mass in amounts.items():
            for j, bits in ports.items():
                if ((x >> j) & 1) in bits:
                    nxt[x ^ (1 << j)] += mass
        amounts = nxt
    return sum(amounts.values())

def active_mass_19(word, steps):
    """Four active ports, sixteen odd 5-bit states, and 2**14 free coordinates."""
    d = residual_ports(5)
    assert all(set(d[a]) <= {1,2,3,4} for a in word)
    amounts = {x: 1 for x in range(1, 32, 2)}
    totals = [sum(amounts.values())]
    for t in range(steps):
        nxt = defaultdict(int)
        for x, mass in amounts.items():
            for j, bits in d[word[t % 3]].items():
                if ((x >> j) & 1) in bits:
                    nxt[x ^ (1 << j)] += mass
        amounts = nxt
        totals.append(sum(amounts.values()))
    return [v * (1 << 14) for v in totals]

def maximal_fixture(p, word, dictionary):
    @lru_cache(None)
    def best(phase, x):
        choices = []
        for j, bits in dictionary[word[phase]].items():
            if ((x >> j) & 1) in bits:
                n, ports, states = best((phase + 1) % 3, x ^ (1 << j))
                choices.append((n + 1, (j,) + ports, (x,) + states))
        return max(choices, key=lambda z: z[0]) if choices else (0, (), (x,))
    by_state = {x: best(0, x) for x in range(1, 1 << p, 2)}
    return max(by_state.values(), key=lambda z: z[0]), [v[0] for v in by_state.values()]

def verify():
    comparisons = 0
    for p in (3, 4):
        d = residual_ports(p)
        for word in product(d, repeat=3):
            for n in range(7):
                a = exact_fiber_mass(p, word, n, d)
                b = direct_mass(p, word, n, d)
                assert a == b, (p, word, n, a, b)
                comparisons += 1
    rng = random.Random(982)
    for p, samples in ((5, 400), (6, 80)):
        d = residual_ports(p)
        keys = list(d)
        for _ in range(samples):
            word = tuple(rng.choice(keys) for _ in range(3))
            n = rng.randrange(9)
            assert exact_fiber_mass(p, word, n, d) == direct_mass(p, word, n, d)
            comparisons += 1
    word = (12, 4, 20)
    d5 = residual_ports(5)
    d19 = residual_ports(19)
    assert all(d5[a] == d19[a] for a in word)
    counts19 = active_mass_19(word, 14)
    assert counts19[13] == 98304 and counts19[14] == 0
    assert all(counts19[h] == direct_mass(5, word, h, d5) * (1 << 14)
               for h in range(15))
    best, max_lengths = maximal_fixture(5, word, d5)
    assert best[0] == 13
    assert tuple(max_lengths) == (1,4,4,7,4,7,7,10,1,7,7,10,7,10,10,13)
    assert comparisons == 41871
    return {
        "schema": "PREFIX982_R6_EXACT_INTEGER_RESULTS_V1",
        "formula_test_aggregates": comparisons,
        "finite_fixture": {
            "p_invariance": "all p>=5; active ports {1,2,3,4}",
            "residual_word": [12,4,20],
            "maximal_path_length": 13,
            "all_odd_19bit_named_path_counts_by_h": counts19,
            "sample_maximal_ports": list(best[1]),
            "sample_maximal_states": list(best[2]),
            "maximal_by_initial_odd_5bit": max_lengths
        },
        "status": "AUTHOR_PROOF_EXACT_INTEGER_CHECKED_NOT_REVIEWED",
        "native_x6_embedding": "NOT_ESTABLISHED"
    }

if __name__ == "__main__":
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
