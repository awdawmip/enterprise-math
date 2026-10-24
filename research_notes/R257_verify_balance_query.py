#!/usr/bin/env python3
"""R257: exact author-side BRC selector-balance observer verification.
Formal affine model only; no native heartbeat or R193 provenance claim.
"""
import json
from collections import defaultdict
from itertools import product

# Each selector has unit positive mass, and the tuple is (next q, eta, b).
EDGES = (
    ((2, -1, -1), (2, 1, -1)),
    ((0, -1, -1), (0, 1, -1)),
    ((1, 1, 1), (2, 1, -1)),
)

def step(state, selector):
    q, eps, shift, diff = state
    target, eta, b = EDGES[q][int(selector)]
    return (target, eta * eps, eta * shift + b,
            diff + (1 if int(selector) == 0 else -1))

def run(word):
    state = (0, 1, 0, 0)
    for selector in word:
        state = step(state, selector)
    return state

def counts_until(depth):
    states = {(0, 1, 0, 0): 1}
    for m in range(depth + 1):
        yield m, states
        nxt = defaultdict(int)
        for state, count in states.items():
            for selector in (0, 1):
                nxt[step(state, selector)] += count
        states = dict(nxt)

def main():
    assert run('000') == (0, 1, -1, 3)
    assert run('101') == (0, 1, -1, -1)
    checked_words = 0
    layers = {}
    for m, states in counts_until(48):
        assert sum(states.values()) == 1 << m
        assert all(v > 0 and abs(s[2]) <= m and abs(s[3]) <= m
                   for s, v in states.items())
        if m <= 12:
            direct = defaultdict(int)
            for word in product('01', repeat=m):
                direct[run(word)] += 1
                checked_words += 1
            assert dict(direct) == states
        if m in (3, 6, 12, 24, 48):
            k, r = divmod(m, 3)
            witnesses = []
            for j in range(k + 1):
                word = '000' * j + '101' * (k - j) + '1' * r
                q, eps, shift, diff = run(word)
                assert (q, eps, shift, diff) == (0 if r == 0 else 2, 1, -k-r, 4*j-k-r)
                witnesses.append((word, diff))
            assert len({d for _, d in witnesses}) == k+1
            for i, (word, d) in enumerate(witnesses):
                suffix = ('1' * d) if d > 0 else ('0' * -d)
                done = run(word + suffix)
                assert done[3] == 0
                for idx, (other, d2) in enumerate(witnesses):
                    if i == idx:
                        continue
                    other_done = run(other + suffix)
                    assert other_done[:3] == done[:3]
                    assert other_done[3] == d2 - d != 0
            layers[str(m)] = {
                'total_paths': str(1 << m),
                'joint_atoms': len(states),
                'fiber': [q, eps, shift],
                'distinct_future_residuals_in_fiber': k+1,
                'provable_extra_bits_lower': k.bit_length(),
                'signed_counter_upper_bits': m.bit_length(),
                'distinct_d_values': [d for _, d in witnesses],
            }
    result = {
        'schema': 'EM_R257_BALANCE_QUERY_AUTHOR_EXACT_V1',
        'mode': 'AUTHOR_SIDE_FORMAL_BRC_NOT_NATIVE_HEARTBEAT',
        'validation': 'PASS',
        'all_layers_0_to_48': 'exact integer positive mass=2^m',
        'all_words_0_to_12_checked': checked_words,
        'fiber_witness_m6': ['101101', '000101', '000000'],
        'layers': layers,
        'bounds': 'ceil(log2(floor(m/3)+1)) <= b_m <= ceil(log2(m+1)), m>=3',
        'limitations': ['not a native ControlPacket execution', 'not matched to original R193',
                        'not a formal CLAIM/Result or independent Driver review'],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
