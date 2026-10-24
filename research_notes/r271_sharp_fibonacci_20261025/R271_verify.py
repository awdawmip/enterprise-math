#!/usr/bin/env python3
"""R271 author-side exact checks for a formal positive affine BRC; no native X6 claims."""
import json
from collections import defaultdict
from itertools import product

TRANSITIONS = {
    0: {0: (2, -1, -1), 1: (2, 1, -1)},
    1: {0: (0, -1, -1), 1: (0, 1, -1)},
    2: {0: (1, 1, 1), 1: (2, 1, -1)},
}
CHANNELS = tuple((q, h) for q in range(3) for h in range(2))


def advance(q, r, e, k, a):
    q1, eta, b = TRANSITIONS[q][a]
    r1 = 2 if r == 2 or (r == 1 and a == 0) else (1 if a == 0 else 0)
    return q1, r1, eta * e, eta * k + b


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def exact_dp(max_n, forbid_00=False):
    state = {(0, 0, 1, 0): 1}
    yield 0, state
    for n in range(1, max_n + 1):
        out = defaultdict(int)
        for (q, r, e, k), count in state.items():
            for a in (0, 1):
                if forbid_00 and r == 1 and a == 0:
                    continue
                out[advance(q, r, e, k, a)] += count
        state = out
        assert sum(state.values()) == (fib(n + 2) if forbid_00 else 2 ** n)
        assert all(abs(k) <= n and (k - n) % 2 == 0 for q, r, e, k in state)
        yield n, state


def brute_state(word):
    q, r, e, k = 0, 0, 1, 0
    for a in word:
        q, r, e, k = advance(q, r, e, k, int(a))
    return q, r, e, k


def channel_vector(state, effect):
    return tuple(sum(count for (q0, r, e, k), count in state.items()
                     if q0 == q and int(r == 2) == h and (e, k) == effect)
                 for q, h in CHANNELS)


def common_effect_min_mass(state):
    effects = {(e, k) for q, r, e, k in state}
    return max((min(channel_vector(state, e)) for e in effects), default=0)


def main():
    for initial_q in (0, 1, 2):
        q, r, e, k = initial_q, 0, 1, 0
        for a in '1101':
            q, r, e, k = advance(q, r, e, k, int(a))
        assert (q, r) == (0, 0), (initial_q, q, r)
    assert brute_state('101')[:2] == (0, 0)
    assert brute_state('101')[2:] == (1, -1)

    all_dp = list(exact_dp(38))
    for n in range(0, 12):
        counts = defaultdict(int)
        for word in product('01', repeat=n):
            counts[brute_state(word)] += 1
        assert dict(counts) == dict(all_dp[n][1]), n

    bases = {
        7: ((1, -3), (2, 2, 3, 1, 1, 9)),
        8: ((1, 0), (1, 6, 1, 9, 2, 16)),
        9: ((-1, -1), (1, 19, 2, 20, 4, 28)),
    }
    for n, (effect, expected) in bases.items():
        got = channel_vector(all_dp[n][1], effect)
        assert got == expected, (n, got, expected)

    support = [common_effect_min_mass(all_dp[n][1]) for n in range(0, 16)]
    assert all(x == 0 for x in support[:7])
    assert all(x > 0 for x in support[7:])

    # Verify all 6-channel common effect lower bounds for the 30-reset coefficient.
    checks = 0
    for n in range(7, 39):
        K = (n - 7) // 30
        rem = n - 30 * K
        j = 7 + ((rem - 7) % 3)
        h = (rem - j) // 3
        eb, kb = bases[j][0]
        effect = (eb, kb - eb * (4 * K + h))
        vec = channel_vector(all_dp[n][1], effect)
        assert all(vec[i] >= 16482 ** K * bases[j][1][i] for i in range(6)), (n, vec)
        checks += 1

    no00_metrics = {}
    for N, state in exact_dp(160, forbid_00=True):
        if N in (20, 30, 40, 60, 80, 100, 120, 160):
            masses = [(v, e, k) for (q, r, e, k), v in state.items() if (q, r) == (0, 0)]
            m, e, k = max(masses)
            assert m <= fib(N + 1)
            assert m * (2 * (N + 1)) >= fib(N - 3) if N >= 5 else True
            no00_metrics[str(N)] = dict(max_reset_mass=str(m), effect=[e, k],
                                         reset_total=str(sum(x[0] for x in masses)),
                                         root_approx=round(m ** (1.0/N), 9))
        if N == 30:
            assert state[(0, 0, 1, -4)] == 16482
    for n in range(1, 12):
        good = [''.join(w) for w in product('01', repeat=n)
                if '00' not in ''.join(w) and w[-1] == '1']
        assert len(good) == fib(n + 1)
        outputs = [brute_state(w + '1101') for w in good]
        assert all((q, r) == (0, 0) for q, r, e, k in outputs)
        assert len(set(w + '1101' for w in good)) == len(good)
        assert len({(e, k) for q, r, e, k in outputs}) <= 2 * (n + 5)

    result = {
        'schema': 'EM_R271_EXACT_AUTHOR_VERIFICATION_V1',
        'status': 'PASS',
        'scope': 'FORMAL_AFFINE_POSITIVE_BRC_NOT_NATIVE_P000_X6',
        'proof_status': 'HAND_PROVED_NOT_FORMALIZED_NOT_DRIVER_REVIEWED',
        'brute_enumeration_depths': '0..11',
        'brute_enumerated_words': str(sum(2 ** n for n in range(12))),
        'full_brc_dp_depths': '0..38',
        'n00_reset_dp_depths': '0..160',
        'common_effect_base_vectors': {str(n): {'effect': list(e), 'vector': list(v)} for n, (e, v) in bases.items()},
        'common_min_mass_depth_0_to_15': support,
        'r270_reference_coefficient': 'P_30(0,0,+1,-4)=16482',
        'reset_maxima': no00_metrics,
        'thirty_step_amplification_verified_depths': f'7..38 ({checks} depths)',
        'theorem': 'lim_N M_N^(1/N)=phi; lim_n B_n^(1/n)=phi',
        'remaining': 'D(6) existence/no-go; actual R193 provenance ports and source-native modules; independent reviewer/admission',
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
