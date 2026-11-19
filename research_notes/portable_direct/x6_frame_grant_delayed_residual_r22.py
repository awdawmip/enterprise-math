#!/usr/bin/env python3
"""R22: source-labelled Boolean-BRC verifier, exact integers, no dependencies."""
import itertools
import json

FRAME_ZERO = (0, 1, 2)
FRAME_ONE = (0, 1, 3)

def enabled(state, theta, k):
    m = len(theta)
    moves = []
    for i in range(m):
        j, d, r = state[3*i:3*i+3]
        if j < k:
            nxt = list(state)
            nxt[3*i] += 1
            if j+1 == k:
                nxt[3*i+2] = min(1, r+theta[i])
            moves.append((('B', i), tuple(nxt)))
        if j >= 1 and d == 0 and r >= 1:
            nxt = list(state)
            nxt[3*i+1] = 1
            nxt[3*i+2] -= 1
            moves.append((('A', i), tuple(nxt)))
    return moves

def language(theta, k, horizon):
    m = len(theta)
    frontier = {((0, 0, 0)*m, ())}
    support = {()}
    for _ in range(horizon):
        next_frontier = set()
        for state, prefix in frontier:
            for label, successor in enabled(state, theta, k):
                word = prefix+(label,)
                next_frontier.add((successor, word))
                support.add(word)
        frontier = next_frontier
    return frozenset(support)

def independent_oracle(word, theta, k):
    n = len(theta)
    b = [0]*n
    a = [0]*n
    for who, i in word:
        if who == 'B':
            if b[i] >= k:
                return False
            b[i] += 1
        elif who == 'A':
            if a[i] or b[i] != k or theta[i] != 1:
                return False
            a[i] = 1
        else:
            raise ValueError(who)
    return True

def verify():
    assert FRAME_ZERO != FRAME_ONE
    assert len(set(FRAME_ZERO)) == len(set(FRAME_ONE)) == 3
    assert 0 in FRAME_ZERO and 0 in FRAME_ONE
    counts = {'models': 0, 'language_checks': 0,
              'pair_checks': 0, 'oracle_checks': 0}
    cases = []
    for m in (1, 2, 3):
        for k in (1, 2, 3, 4):
            bits = list(itertools.product((0, 1), repeat=m))
            alphabet = [(who, i) for who in ('A', 'B') for i in range(m)]
            memo = {}
            for theta in bits:
                counts['models'] += 1
                for h in range(k+2):
                    words = language(theta, k, h)
                    memo[(theta, h)] = words
                    counts['language_checks'] += 1
                    for length in range(h+1):
                        for w in itertools.product(alphabet, repeat=length):
                            assert (w in words) == independent_oracle(w, theta, k)
                            counts['oracle_checks'] += 1
            for h in range(k+1):
                assert len({memo[(theta, h)] for theta in bits}) == 1
            assert len({memo[(theta, k+1)] for theta in bits}) == 2**m
            for x in range(len(bits)):
                for y in range(x+1, len(bits)):
                    a, b = bits[x], bits[y]
                    counts['pair_checks'] += 1
                    assert all(memo[(a,h)] == memo[(b,h)] for h in range(k+1))
                    assert memo[(a,k+1)] != memo[(b,k+1)]
                    i = next(i for i in range(m) if a[i] != b[i])
                    witness = (('B',i),)*k + (('A',i),)
                    assert (witness in memo[(a,k+1)]) != (witness in memo[(b,k+1)])
            cases.append({'lanes':m, 'delay_parameter':k,
                'first_distinction_depth':k+1,
                'hidden_frame_assignments':2**m,
                'classes_h_le_k':1, 'classes_h_k_plus_one':2**m,
                'fixed_length_residual_bits':m,
                'max_word_count_h_k_plus_one':max(len(memo[(theta,k+1)]) for theta in bits)})
    return {'schema':'X6_FRAME_GRANT_DELAYED_RESIDUAL_R22_EXACT_V1',
        'status':'PASS', 'observer':'Boolean support of successful ordered (source,signed Port) words',
        'frame_zero':list(FRAME_ZERO), 'frame_one':list(FRAME_ONE),
        'counts':counts, 'cases':cases}

if __name__ == '__main__':
    print(json.dumps(verify(), ensure_ascii=False, indent=2, sort_keys=True))
