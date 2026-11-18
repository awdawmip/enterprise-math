#!/usr/bin/env python3
"""R9 exact Boolean-BRC witness of 3n independent Port-history bits.

Input: X6 six-signed-integer Cell torsor, ordered 3-positive-token
triadic candidate, guarded one-shot (source_id,port_id) branch update.
This is conditional on declared triadic closure/admission: no native physics.
Branch identity, ordered event labels and whole occupied triad persist.

Run: python3 x6_triadic_port_multibit_brc_verify.py > x6_triadic_port_multibit_brc_results.json
"""
from itertools import permutations, product
from math import factorial, ceil, log2
import json

D = 6
FRAME = (0, 1, 2)


def e(axis):
    return tuple(int(i == axis) for i in range(D))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def choose_sources(n, frame):
    # Separation is a sixth-axis translation, not a new space dimension.
    unused = next(i for i in range(D) if i not in frame)
    sources = {}
    for g in range(n):
        o = tuple(10 * g * int(i == unused) for i in range(D))
        sources[('B', g)] = o
        for j in range(3):
            sources[('A', g, j)] = add(o, sub(e(frame[j]), e(frame[(j + 1) % 3])))
    assert len(set(sources.values())) == 4 * n
    return sources


def initialize(sources, frame):
    # Full source-bearing typed triad: no scalar-mass projection.
    tokens = {s: (s, tuple((frame[r], '+', r) for r in range(3))) for s in sources}
    occupancy = {cell: tokens[s] for s, cell in sources.items()}
    return occupancy, frozenset(), (), tokens


def step(state, source, port, sources, frame):
    """Actual guarded one-shot move, retaining source/port word."""
    occ, moved, word, tokens = state
    if source in moved or port not in (0, 1, 2):
        return None
    origin = sources[source]
    if occ.get(origin) != tokens[source]:
        return None
    dest = add(origin, e(frame[port]))
    if dest in occ:
        return None
    new_occ = dict(occ)
    del new_occ[origin]
    new_occ[dest] = tokens[source]
    return new_occ, frozenset((*moved, source)), word + ((source, port),), tokens


def observed_bitset(state, n, frame, sources):
    occ = state[0]
    return tuple(tuple(int(add(sources[('B', g)], e(frame[j])) in occ)
                       for j in range(3)) for g in range(n))


def allowed_ports(state, g, frame, sources):
    return tuple(j for j in range(3)
                 if step(state, ('B', g), j, sources, frame) is not None)


def prefix_count_formula(allowed, length):
    # Coefficients of product_g(1 + |S_g| z), multiplied by length!.
    co = [1]
    for slots in allowed:
        k = len(slots)
        nxt = [0] * (len(co) + 1)
        for i, v in enumerate(co):
            nxt[i] += v
            nxt[i + 1] += k * v
        co = nxt
    return factorial(length) * co[length]


def exact_labelled_future_levels(state, n, sources, frame):
    """Independently generate the full ordered B source/port BRC branch languages."""
    levels = [{()}]
    states = [(state, ())]
    for _ in range(n):
        nxt = []
        words = set()
        for st, word in states:
            for g in range(n):
                for port in range(3):
                    new_st = step(st, ('B', g), port, sources, frame)
                    if new_st is not None:
                        new_word = word + ((('B', g), port),)
                        nxt.append((new_st, new_word))
                        words.add(new_word)
        levels.append(words)
        states = nxt
    return levels


def check(n, frame, check_full):
    sources = choose_sources(n, frame)
    signatures = set()
    productive = 0
    full_word_counts_checked = 0
    quotient_steps_checked = 0
    checked = 0
    # Each bit chooses a distinct A_j shared B_j target (1) or safe target (0).
    for flags in product((0, 1), repeat=3*n):
        state = initialize(sources, frame)
        for g in range(n):
            for j in range(3):
                sj = ('A', g, j)
                port = (j + 1) % 3 if flags[3*g+j] else j
                state = step(state, sj, port, sources, frame)
                assert state is not None, (n, frame, g, j, flags)
        assert len(state[1]) == 3*n
        assert len(state[0]) == 4*n
        assert all(('A', g, j) in state[1] and ('B', g) not in state[1]
                   for g in range(n) for j in range(3))
        bitset = observed_bitset(state, n, frame, sources)
        assert bitset == tuple(tuple(flags[3*g+j] for j in range(3))
                               for g in range(n))
        enabled = tuple(allowed_ports(state, g, frame, sources) for g in range(n))
        assert enabled == tuple(tuple(j for j in range(3) if not flags[3*g+j])
                                for g in range(n))
        signatures.add(enabled)
        if all(enabled):
            productive += 1
        for g in range(n):
            for port in enabled[g]:
                successor = step(state, ('B', g), port, sources, frame)
                assert successor is not None
                assert all(allowed_ports(successor, h, frame, sources) == enabled[h]
                           for h in range(n) if h != g)
                quotient_steps_checked += 1
        if check_full:
            levels = exact_labelled_future_levels(state, n, sources, frame)
            assert len(levels) == n + 1
            assert all(len(words) == prefix_count_formula(enabled, k)
                       for k, words in enumerate(levels))
            assert all(len(w) == k for k, words in enumerate(levels) for w in words)
            full_word_counts_checked += 1
        checked += 1
    assert checked == 8**n
    assert len(signatures) == 8**n
    assert productive == 7**n
    return dict(n=n, frame=list(frame), cases=checked, future_classes=len(signatures),
                productive_full_quota_classes=productive,
                worst_case_bits=3*n,
                productive_worst_case_bits=(7**n-1).bit_length(),
                quotient_B_steps_checked=quotient_steps_checked,
                exact_future_language_cases=full_word_counts_checked)


def run():
    frames = list(permutations(range(D), 3))
    cases = 0
    exact_cases = 0
    quotient_steps = 0
    frame_family = {}
    for n in (1, 2):
        for frame in frames:
            r = check(n, frame, check_full=True)
            cases += r['cases']
            exact_cases += r['exact_future_language_cases']
            quotient_steps += r['quotient_B_steps_checked']
        frame_family[str(n)] = {'frames': len(frames), 'classes_per_frame': 8**n,
                                'productive_classes_per_frame': 7**n}
    larger = {}
    for n in (3, 4):
        r = check(n, FRAME, check_full=True)
        larger[str(n)] = r
        cases += r['cases']
        exact_cases += r['exact_future_language_cases']
        quotient_steps += r['quotient_B_steps_checked']
    return {'schema':'X6_TRIADIC_PORT_MULTIBIT_R9_V1', 'status':'PASS',
            'carrier':'source-port-labelled Boolean BRC, full six signed Cell coordinates and ordered triad-token occupancy',
            'model':'R8 conditional guarded one-shot triadic relocation; 4n sources in n independent separated gadgets',
            'frame_family':frame_family, 'larger_single_frame':larger,
            'witness_history_cases_checked':cases,
            'exhaustive_future_language_cases_checked':exact_cases,
            'future_quotient_B_transition_checks':quotient_steps,
            'exact_all_histories_classes':'8^n', 'all_histories_bits':'3n',
            'productive_history_classes':'7^n', 'productive_history_bits':'ceil(n*log2(7))',
            'limitation':'No native TRIADIC_CLOSURE_E admission or repeated relocation; not a physical or signed-amplitude certificate'}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2, ensure_ascii=False))
