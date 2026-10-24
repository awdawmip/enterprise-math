"""R255: exact non-enumerative provenance rank/unrank for a formal native-X6 affine BRC.

Positive 1-weight branches with source-local selector alphabet {0,1}.
No asserted native heartbeat update law, R193 bridge, or result admission.
"""
from __future__ import annotations
from collections import defaultdict
from math import comb
import json

# q -> (next_state, holonomy_sign, first_native_axis_translation) by selector
EDGES = (
    ((2, -1, -1), (2, +1, -1)),
    ((0, -1, -1), (0, +1, -1)),
    ((1, +1, +1), (2, +1, -1)),
)


def effect_and_target(word: str, source: int = 0):
    q, sign, translation = source, 1, 0
    for symbol in word:
        q, eta, offset = EDGES[q][int(symbol)]
        sign, translation = eta * sign, eta * translation + offset
    return (q, sign, translation)


def suffix_tables(max_depth: int, target: int):
    """C[l][(q,eps,k)] = number of exactly-l word suffixes q -> target
    whose chronological composite affine effect is (eps,k).
    """
    tables = [{(target, 1, 0): 1}]
    for length in range(1, max_depth + 1):
        nxt = defaultdict(int)
        for q in range(3):
            for target_q, eta, b in EDGES[q]:
                for (q_after, eps_after, k_after), multiplicity in tables[-1].items():
                    if q_after == target_q:
                        nxt[(q, eps_after * eta, eps_after * b + k_after)] += multiplicity
        tables.append(dict(nxt))
    return tables


def count_fiber(tables, source: int, horizon: int, observed: tuple[int, int, int]):
    _q_t, eps_t, k_t = observed
    assert 0 <= horizon < len(tables)
    return tables[horizon].get((source, eps_t, k_t), 0)


def follow_prefix(prefix: str, source: int = 0):
    return effect_and_target(prefix, source)


def completions_after(prefix: str, horizon: int, observed, tables, source: int = 0):
    q, eps, k = follow_prefix(prefix, source)
    q_t, eps_t, k_t = observed
    rem = horizon - len(prefix)
    if rem < 0 or rem >= len(tables):
        raise ValueError('prefix length out of bounds')
    suffix_sign = eps_t * eps
    suffix_translation = k_t - suffix_sign * k
    # tables are for q_t fixed, checked by caller.
    return tables[rem].get((q, suffix_sign, suffix_translation), 0)


def count_remainder(q: int, eps: int, k: int, length: int, observed, tables):
    """Exact number of suffixes realizing the fixed target observation."""
    _q_t, eps_t, k_t = observed
    sigma = eps_t * eps
    c = k_t - sigma * k
    return tables[length].get((q, sigma, c), 0)


def rank(word: str, observed, tables, source: int = 0):
    horizon = len(word)
    if effect_and_target(word, source) != observed:
        raise ValueError('word not in specified observation fiber')
    r, q, eps, k = 0, source, 1, 0
    for pos, ch in enumerate(word):
        if ch == '1':
            q0, eta0, b0 = EDGES[q][0]
            r += count_remainder(q0, eta0*eps, eta0*k+b0,
                                 horizon-pos-1, observed, tables)
        q, eta, b = EDGES[q][int(ch)]
        eps, k = eta*eps, eta*k+b
    return r


def unrank(rank_value: int, horizon: int, observed, tables, source: int = 0):
    c = count_fiber(tables, source, horizon, observed)
    if rank_value < 0 or rank_value >= c:
        raise ValueError('tag outside observation fiber')
    q, eps, k = source, 1, 0
    word = []
    for pos in range(horizon):
        q0, eta0, b0 = EDGES[q][0]
        n0 = count_remainder(q0, eta0*eps, eta0*k+b0,
                             horizon-pos-1, observed, tables)
        chosen = 0 if rank_value < n0 else 1
        if chosen == 1:
            rank_value -= n0
        q, eta, b = EDGES[q][chosen]
        eps, k = eta*eps, eta*k+b
        word.append(str(chosen))
    path = ''.join(word)
    if effect_and_target(path, source) != observed or rank_value != 0:
        raise AssertionError('decoder invariant')
    return path


def all_fiber_sizes(tables_by_target, m: int, source: int = 0):
    hist = {}
    for q_t in range(3):
        for (q, sign, k), c in tables_by_target[q_t][m].items():
            if q == source:
                hist[(q_t, sign, k)] = c
    return hist


def check():
    max_m = 96
    tables_by_target = {target: suffix_tables(max_m, target) for target in range(3)}
    exact_cases = 0
    for source in range(3):
        for m in range(13):
            direct = defaultdict(list)
            for v in range(1 << m):
                word = format(v, '0%db' % m) if m else ''
                obs = effect_and_target(word, source)
                direct[obs].append(word)
            table_obs = all_fiber_sizes(tables_by_target, m, source)
            assert {o: len(words) for o, words in direct.items()} == table_obs
            for obs, words in direct.items():
                tab = tables_by_target[obs[0]]
                assert [unrank(i, m, obs, tab, source) for i in range(len(words))] == words
                for i, word in enumerate(words):
                    assert rank(word, obs, tab, source) == i
                    exact_cases += 1
    one_collision = effect_and_target('000'), effect_and_target('101')
    assert one_collision[0] == one_collision[1]
    obs3 = one_collision[0]
    tab3 = tables_by_target[obs3[0]]
    assert (rank('000', obs3, tab3), rank('101', obs3, tab3)) == (0, 1)
    chosen = {}
    for m in [3, 12, 24, 40, 48, 64, 96]:
        fiber = all_fiber_sizes(tables_by_target, m)
        assert sum(fiber.values()) == 2 ** m
        assert sum(v for (q, s, k), v in fiber.items() if -s*k == 0) == (comb(m, m//2) if m%2==0 else 0)
        obs, width = max(fiber.items(), key=lambda kv: (kv[1], kv[0]))
        tab = tables_by_target[obs[0]]
        ranks = sorted({0, width//2, width-1})
        for i in ranks:
            word = unrank(i, m, obs, tab)
            assert len(word)==m and rank(word, obs, tab) == i
        chosen[str(m)] = {'total_paths': str(2**m), 'max_fiber_size': str(width), 'max_fiber_obs': list(obs), 'min_tag_bits': (width-1).bit_length(), 'rank_checks': len(ranks)}
    print(json.dumps({'status':'PASS','model':'R253/R254 positive unit-weight three-control two-selector formal X6 affine carrier','precise_direct_rank_word_cases':exact_cases,'exhaustive_depths':'0..12, each of 3 initial controls','first_collision':{'word_a':'000','word_b':'101','joint_observation':list(obs3),'ranks':[0,1]},'selected_depths':chosen,'native_module_execution':False,'r193_observer_mapped':False},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    check()
