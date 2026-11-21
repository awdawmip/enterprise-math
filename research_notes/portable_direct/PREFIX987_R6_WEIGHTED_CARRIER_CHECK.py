"""PREFIX-987: exact named-source quotient with positive edge weights.

Only the signed-source auxiliary bit-flip observer is tested here.
"""
from collections import defaultdict


def named_sources(p, c):
    return [(i, j, s) for i in range(p) for j in range(1, p)
            for s in (-1, 1) if (1 << i) - s * (1 << j) == c]


def automaton(p, word):
    assert len(word) == 4
    phase_sources = [named_sources(p, c) for c in word]
    ports = sorted({j for sources in phase_sources for _, j, _ in sources})
    port_index = {j: k for k, j in enumerate(ports)}
    stride = 1 << len(ports)
    edges = [dict() for _ in range(4 * stride)]
    for q, sources in enumerate(phase_sources):
        for i, j, sign in sources:
            k = port_index[j]
            label = (q, i, j, sign)
            for b in range(stride):
                if ((b >> k) & 1) == (1 - sign) // 2:
                    u = q * stride + b
                    v = ((q + 1) % 4) * stride + (b ^ (1 << k))
                    assert label not in edges[u]
                    edges[u][label] = v
    return ports, edges


def right_language_quotient(edges):
    # All live states accept the empty word; missing edges reject that letter.
    cls = [0] * len(edges)
    while True:
        keys = [tuple((letter, cls[dest]) for letter, dest in sorted(e.items()))
                for e in edges]
        numbers = {}
        updated = [numbers.setdefault(k, len(numbers)) for k in keys]
        if updated == cls:
            representatives = {}
            counts = defaultdict(int)
            for state, c in enumerate(cls):
                representatives.setdefault(c, state)
                counts[c] += 1
            quotient = [
                {letter: cls[dest] for letter, dest in edges[representatives[c]].items()}
                for c in range(len(representatives))]
            return cls, quotient, dict(counts)
        cls = updated


def weighted_counts(edges, initial, steps, weight):
    # Backward DP: F_n(state) = sum weights of legal n-step named words.
    future = [1] * len(edges)
    sequence = []
    for n in range(steps + 1):
        sequence.append(sum(initial[s] * future[s] for s in range(len(edges))))
        future = [sum(weight(label) * future[dest]
                      for label, dest in es.items()) for es in edges]
    return sequence


def check(p, word, steps=20):
    ports, edges = automaton(p, word)
    cls, quotient, counts = right_language_quotient(edges)
    stride = 1 << len(ports)
    # Exactly one representative of each active-bit pattern at phase zero.
    initial_full = [int(s < stride) for s in range(len(edges))]
    initial_quotient = [0] * len(quotient)
    for s, mult in enumerate(initial_full):
        initial_quotient[cls[s]] += mult
    unit = lambda label: 1
    positive = lambda label: 2 if label[3] == 1 else 3
    raw_unit = weighted_counts(edges, initial_full, steps, unit)
    q_unit = weighted_counts(quotient, initial_quotient, steps, unit)
    raw_weighted = weighted_counts(edges, initial_full, steps, positive)
    q_weighted = weighted_counts(quotient, initial_quotient, steps, positive)
    assert raw_unit == q_unit and raw_weighted == q_weighted
    return {
        "p": p, "word": list(word), "ports": ports,
        "states": len(edges), "minimal_named_language_classes": len(quotient),
        "raw_vs_quotient_verified_n": [0, steps],
        "phase_zero_unit_counts_n0_to_n10": raw_unit[:11],
        "phase_zero_unit_n18_n19": [raw_unit[18], raw_unit[19]],
        "phase_zero_weighted_n4_n8_n12": [raw_weighted[k] for k in (4, 8, 12)],
    }


if __name__ == "__main__":
    import json
    for p, word in [(6, (6, 24, 6, -3)),
                    (6, (6, 24, 8, 40)),
                    (4, (4, -1, 3, -7))]:
        print(json.dumps(check(p, word), ensure_ascii=False, sort_keys=True))
