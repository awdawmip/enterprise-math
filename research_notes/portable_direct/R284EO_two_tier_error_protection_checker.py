#!/usr/bin/env python3
"""Exact graph/checker for R284EO, using pinned R284EM integer minima.
This does not recompute the 65,536 original Port states.
"""
import itertools
import json
from pathlib import Path

MINIMA = {
    'two_port': {'0-1': 60, '0-2': 9394, '0-3': 9526,
                 '1-2': 9289, '1-3': 9421, '2-3': 60},
    'four_port': {'0-1': 60, '0-2': 9432, '0-3': 9564,
                  '1-2': 9327, '1-3': 9459, '2-3': 60},
}
THRESHOLDS = {'two_port': 4696, 'four_port': 4715}


def edges(port, E):
    return {pair for pair, dist in MINIMA[port].items() if dist <= 2 * E}


def n_opt(port, E, k, t, e):
    assert 0 <= E <= 8656 and k >= 0 and t >= 0 and e >= 0
    if t > 2 * e:
        return 0 if E <= THRESHOLDS[port] else 2 * k + 1
    if E <= 29:
        return 0
    if E <= THRESHOLDS[port]:
        return 2 * k + 1
    return 3 * k + 2


def data_code(a, b, port, E, k, old_reliable):
    if old_reliable:
        return () if E <= THRESHOLDS[port] else (b,) * (2 * k + 1)
    if E <= 29:
        return ()
    if E <= THRESHOLDS[port]:
        return (a,) * (2 * k + 1)
    return (a,) * (k + 1) + (b,) * (k + 1) + ((a ^ b),) * k


def ham(x, y):
    return sum(v != w for v, w in zip(x, y))


def check_code(port, E, k, t, e):
    old_reliable = t > 2 * e
    codes = {a + 2 * b: data_code(a, b, port, E, k, old_reliable)
             for a, b in itertools.product((0, 1), repeat=2)}
    assert {len(c) for c in codes.values()} == {n_opt(port, E, k, t, e)}
    for pair in edges(port, E):
        u, v = map(int, pair.split('-'))
        au, av = u & 1, v & 1
        # Product-ball intersection iff both channel distances <= 2*budgets.
        assert not (ham((au,) * t, (av,) * t) <= 2 * e
                    and ham(codes[u], codes[v]) <= 2 * k), (port, E, k, t, e, pair)


def main():
    critical = [0, 29, 30, 4644, 4645, 4663, 4664, 4696, 4697,
                4715, 4716, 8656]
    checks = 0
    for port in MINIMA:
        for E in range(8657):
            for k, t, e in ((0, 0, 0), (1, 0, 0), (2, 0, 0),
                            (0, 1, 0), (1, 1, 0), (2, 1, 0),
                            (1, 1, 1), (2, 2, 1), (1, 3, 1),
                            (2, 4, 2), (3, 5, 2)):
                check_code(port, E, k, t, e)
                checks += 1
    for port in MINIMA:
        for E in critical:
            for k, t, e in itertools.product(range(6), range(8), range(4)):
                check_code(port, E, k, t, e)
                checks += 1
    atlas = {}
    for port in MINIMA:
        T = THRESHOLDS[port]
        assert edges(port, 29) == set()
        assert edges(port, T) == {'0-1', '1-2', '2-3'}
        assert {'0-1', '0-2', '1-2'}.issubset(edges(port, T+1))
        atlas[port] = {
            'old_a_reliable_threshold': 't >= 2e+1',
            'zero_storage_without_old': 'E <= 29',
            'bipartite_phase': [30, T],
            'triangle_onset': T + 1,
            'opt_new_storage_when_old_unreliable': ['0', '2k+1', '3k+2'],
            'opt_new_storage_when_old_reliable': ['0', '0', '2k+1'],
            'opt_total_if_t_is_chosen_freely': [
                '0', 'min(2k+1,2e+1)', 'min(3k+2,2e+2k+2)'],
            'critical_edges_at_threshold': sorted(edges(port, T)),
            'critical_edges_next': sorted(edges(port, T+1)),
        }
    cert = {
        'schema': 'R284EO_TWO_TIER_ERROR_PROTECTION_GRAPH_CHECK_V1',
        'source_frozen_commit': 'acba2d8667903434aaa2a10720f43637fcc2421b',
        'source_certificate': 'research_notes/portable_direct/R284EM_history_aware_tag_certificate.json',
        'frozen_residue_sha256': 'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4',
        'nature': 'Exact graph-derived finite checker, not a new Port exhaustive enumeration',
        'scope': {'port_types': list(MINIMA), 'E_range': [0,8656],
                  'tested_k': '0..5 on selected E; 0..3 on all E',
                  'tested_old_t': '0..7 on selected E',
                  'tested_old_e': '0..3 on selected E'},
        'tested_five_tuples': checks,
        'results': atlas,
        'proof': 'General unbounded t,e,k follows from product-ball intersection, P4/K3 graph lower bounds, and explicit codes; finite tests do not establish the universal step.',
        'review': 'NOT_REVIEWED',
    }
    output = Path(__file__).with_name('R284EO_two_tier_error_protection_certificate.json')
    output.write_text(json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
    print('PASS', checks, 'parameter checks; saved', output)


if __name__ == '__main__':
    main()
