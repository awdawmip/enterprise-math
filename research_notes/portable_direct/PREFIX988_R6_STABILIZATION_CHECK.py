"""PREFIX-988: exact source-alphabet stabilization and 19-bit lifting.
For the auxiliary signed-source bit-flip observer; Python 3 stdlib only.
"""
from collections import defaultdict
import json


def sources(p, c):
    return tuple((i, j, s) for i in range(p) for j in range(1, p)
                 for s in (-1, 1) if (1 << i) - s * (1 << j) == c)


def compact_graph(p, word):
    alphabet = [sources(p, c) for c in word]
    ports = sorted({j for row in alphabet for _, j, _ in row})
    offset = {j: k for k, j in enumerate(ports)}
    stride = 1 << len(ports)
    length = len(word)
    edges = [dict() for _ in range(length * stride)]
    for q, row in enumerate(alphabet):
        for i, j, s in row:
            mask = 1 << offset[j]
            for b in range(stride):
                if ((b & mask) != 0) == (s == -1):
                    edges[q * stride + b][(q, i, j, s)] = ((q+1) % length) * stride + (b ^ mask)
    return ports, alphabet, edges


def minimal_classes(edges):
    cls = [0] * len(edges)
    for _ in range(len(edges)+1):
        keys = [tuple(sorted((label, cls[v]) for label, v in row.items())) for row in edges]
        mapping = {}
        fresh = [mapping.setdefault(key, len(mapping)) for key in keys]
        if fresh == cls:
            return len(mapping)
        cls = fresh
    raise AssertionError('refinement failed')


def path_counts(edges, stride, max_len, weight):
    f = [1] * len(edges)
    ans = []
    for _ in range(max_len+1):
        ans.append(sum(f[:stride]))
        f = [sum(weight(label)*f[v] for label, v in row.items()) for row in edges]
    return ans


def direct_full_bits(p, word, horizon, weight):
    # Independent forward DP over every odd p-bit input; each state carries
    # its own path multiplicity. No active-port compression is used.
    states = {x: 1 for x in range(1, 1 << p, 2)}
    out = [sum(states.values())]
    for n in range(horizon):
        q = n % len(word)
        next_states = defaultdict(int)
        for x, multiplicity in states.items():
            for i, j, s in sources(p, word[q]):
                if ((x >> j) & 1) == (1 - s) // 2:
                    next_states[x ^ (1 << j)] += multiplicity * weight((q, i, j, s))
        states = next_states
        out.append(sum(states.values()))
    return out


def verify(word, low, high=19, horizon=20):
    m = max(abs(c) for c in word)
    assert m > 0 and all(c != 0 for c in word)
    p0 = 2 + (m.bit_length()-1)
    assert low >= p0
    ports0, alphabet0, edges0 = compact_graph(low, word)
    base = path_counts(edges0, 1 << len(ports0), horizon, lambda _: 1)
    weighted_base = path_counts(edges0, 1 << len(ports0), horizon,
                                lambda a: 2 if a[3] == 1 else 3)
    q0 = minimal_classes(edges0)
    for p in range(low, min(low+2, 8)+1):
        spectators = 1 << (p-1-len(ports0))
        assert direct_full_bits(p, word, 10, lambda _: 1) == [v * spectators for v in base[:11]]
        assert direct_full_bits(p, word, 10, lambda a: 2 if a[3] == 1 else 3) == [v * spectators for v in weighted_base[:11]]
    for p in range(low, high+1):
        ports, alph, edges = compact_graph(p, word)
        assert (ports, alph, edges) == (ports0, alphabet0, edges0)
        assert minimal_classes(edges) == q0
        assert path_counts(edges, 1 << len(ports), horizon, lambda _: 1) == base
    factor = 1 << (high-1-len(ports0))
    return {'word': list(word), 'minimum_complete_width_p0': p0,
            'verified_width_interval': [low, high],
            'active_ports': ports0, 'active_state_count': len(edges0),
            'minimal_named_language_classes': q0,
            'spectator_factor_at_p19': factor,
            'unit_path_counts_phase0_all_odd_p19': {'n8': base[8]*factor,
                                                     'n18': base[18]*factor,
                                                     'n19': base[19]*factor},
            'weight_plus2_minus3_all_odd_p19': {'n8': weighted_base[8]*factor,
                                                 'n19': weighted_base[19]*factor},
            'active_unit_n0_to_n10': base[:11]}


def main():
    examples = [((6,24,6,-3), 6), ((6,24,8,40), 7), ((4,-1,3,-7), 4)]
    results = [verify(word, low) for word, low in examples]
    # Sharpness of universal width threshold for powers of two (k >=1).
    for k in range(1, 14):
        c = 1 << k
        assert (k+1, k, 1) in sources(k+2, c)
        assert (k+1, k, 1) not in sources(k+1, c)
    # c = -1 makes p0=2 sharp for M=1.
    assert (0, 1, 1) in sources(2, -1) and not sources(1, -1)
    return {'research_id': 'PREFIX-988', 'model': 'AUXILIARY_SIGNED_SOURCE_BIT_FLIP',
            'method': 'exact_integer_active_state_graph_and_named_language_partition_refinement',
            'tested_powers_of_two_sharpness_k': [1, 13],
            'width_invariance_verified': True, 'independent_direct_full_input_check_n': [0,10], 'cases': results}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True, ensure_ascii=False))
