#!/usr/bin/env python3
"""Exact finite-horizon two-law Markovization/occupancy regression, stdlib only.
External model: no native Heartbeat-X6 embedding asserted.
"""
from collections import defaultdict
from fractions import Fraction as F
from random import Random

ZERO = F(0)
ONE = F(1)
SIG = (F(1, 2), ONE, F(3, 2))
KQ = (F(1, 4), F(1, 2), F(1, 4))
ASSERTED_TRIALS = 240

def fracstr(x):
    return str(x)

def r_of(history):
    out = ONE
    for s in history[1:]:
        out *= s
    return out

def key(history):
    return (len(history), r_of(history))

def rational_actions(w):
    z = sum(w)
    assert z > 0
    return (F(w[0], z), F(w[1], z), F(w[2], z))

def example_full_policy(h):
    t, r = key(h)
    origin = h[0]
    if t == 1:
        return (ZERO, ZERO, ONE) if origin == 'A' else (ONE, ZERO, ZERO)
    if t == 2:
        return (ZERO, ONE, ZERO) if h[1] == ONE else (ZERO, ZERO, ONE)
    if t == 3:
        if r == F(3, 4):
            return (ZERO, ONE, ZERO) if h[1] == F(1, 2) else (ZERO, ZERO, ONE)
        return (ONE, ZERO, ZERO) if r >= ONE else (ZERO, ONE, ZERO)
    assert t == 4
    return (ONE, ZERO, ZERO) if r >= ONE else (ZERO, ONE, ZERO)

def random_full_policy(seed):
    rng = Random(seed)
    d = {}
    for o in ('A', 'B'):
        previous = [(o,)]
        for t in range(1, 5):
            new = []
            for h in previous:
                # Distinct random action kernels at full histories: no shared seed in play.
                a, b, c = (rng.randint(1, 7) for _ in range(3))
                if t == 4:
                    c = 0
                d[h] = rational_actions((a, b, c))
                for s in SIG:
                    new.append(h + (s,))
            previous = new
    return lambda h: d[h]

def run(policy):
    # Q flow along each complete observed history; P flow equals current LR times Q flow.
    level = [(('A',), F(1, 2)), (('B',), F(1, 2))]
    occupancy = defaultdict(lambda: ZERO)
    by_key_action = defaultdict(lambda: ZERO)
    terminal = defaultdict(lambda: ZERO)
    output = [ZERO, ZERO, ZERO, ZERO]
    for t in range(1, 5):
        next_level = []
        for h, q in level:
            k = key(h)
            r = k[1]
            occupancy[k] += q
            acts = policy(h)
            assert len(acts) == 3 and all(x >= 0 for x in acts) and sum(acts) == ONE
            if t == 4:
                assert acts[2] == ZERO
            for i, a in enumerate(('P','Q','C')):
                fq = q * acts[i]
                if fq == ZERO:
                    continue
                by_key_action[(k, a)] += fq
                if i == 2:
                    for s, qs in zip(SIG, KQ):
                        next_level.append((h + (s,), fq * qs))
                else:
                    terminal[(t, r, a)] += fq
                    # eP: true P but declared Q; eQ: true Q but declared P
                    output[0] += r*fq if a == 'Q' else ZERO
                    output[1] += fq if a == 'P' else ZERO
                    output[2] += t*r*fq
                    output[3] += t*fq
        level = next_level
    assert not level
    return occupancy, by_key_action, terminal, tuple(output)

def markovize(data):
    occupancy, by_key_action, _, _ = data
    d = {}
    for k, mass in occupancy.items():
        d[k] = tuple(by_key_action[(k, a)]/mass for a in ('P','Q','C')) if mass else (ONE,ZERO,ZERO)
    return lambda h: d.get(key(h), (ONE,ZERO,ZERO))

def compare(full):
    original = run(full)
    converted = run(markovize(original))
    assert original[0] == converted[0], 'Q occupancy mismatch'
    assert {k:v for k,v in original[1].items() if v} == {k:v for k,v in converted[1].items() if v}, 'Q state/action flow mismatch'
    assert original[2] == converted[2], 'terminal (t,LR,decl) flow mismatch'
    assert original[3] == converted[3], 'four-observer mismatch'
    # P flow is exactly current LR times the corresponding Q flow.
    for (k, action), q in original[1].items():
        assert k[1]*q == k[1]*converted[1][(k, action)]
    return original, converted

def check_kernels():
    assert sum(KQ) == ONE
    assert sum(s*q for s,q in zip(SIG,KQ)) == ONE
    assert all(q>0 and s*q>0 for s,q in zip(SIG,KQ))
    assert F(1,2)+F(1,2)==ONE
    # two source paths merge at t=1 ratio 1;
    # at t=3, (s=1/2, v=3/2) and (s=3/2, v=1/2) both have LR 3/4.
    assert SIG[0]*SIG[2] == SIG[2]*SIG[0] == F(3,4)

if __name__ == '__main__':
    check_kernels()
    original, converted = compare(example_full_policy)
    print('MODEL: two origins; repeated positive LR multiplier Q=(1/4,1/2,1/4), P=(1/8,1/2,3/8), t=1..4')
    print('FULL_OBSERVER:', *map(fracstr, original[3]))
    print('LR_OBSERVER:', *map(fracstr, converted[3]))
    key3 = (3,F(3,4))
    print('MERGER_T3_Q_OCCUPANCY:', original[0][key3])
    print('MERGER_T3_Q_ACT_P_Q_C:', *(original[1][(key3,a)] for a in ('P','Q','C')))
    print('MERGER_T3_LR_POLICY_P_Q_C:', *markovize(original)(('A',F(1,2),F(3,2))))
    assert original[0][key3] == F(1,16)
    assert markovize(original)(('A',F(1,2),F(3,2))) == (ZERO,F(1,2),F(1,2))
    for seed in range(ASSERTED_TRIALS):
        compare(random_full_policy(seed + 0xD25))
    print('VERIFIED_EXACT_RANDOMIZED_FULL_POLICY_CASES:', ASSERTED_TRIALS)
    print('PASS_EXACT_R5_SERIAL_INTERACTING_MERGER_LR_MARKOVIZATION')
