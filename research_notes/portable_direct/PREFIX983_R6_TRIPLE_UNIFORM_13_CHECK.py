#!/usr/bin/env python3
"""PREFIX-983: complete isomorphism-class certificate for 3-stage nonzero
signed-source XOR-port words; exact finite graph, no floating arithmetic.

Bit requirements: 1 = current bit 0, 2 = current bit 1, 3 = either.
This is an auxiliary port observer, NOT a native X6/triadic embedding.
"""
from collections import Counter, defaultdict, deque
from itertools import product
import json

LOCAL_TYPES = ((1,), (2,), (1, 2), (2, 2), (2, 3))


def canonical_port_assignments(length):
    """All set partitions via restricted-growth strings, with labels by first use."""
    def extend(prefix, maximum):
        if len(prefix) == length:
            yield tuple(prefix)
            return
        for label in range(maximum + 2):
            prefix.append(label)
            yield from extend(prefix, max(maximum, label))
            prefix.pop()
    yield from extend([0], 0)


def nonzero_residual_dictionary(p):
    d = defaultdict(lambda: defaultdict(set))
    for i in range(p):
        for j in range(1, p):
            for s in (-1, 1):
                c = (1 << i) - s * (1 << j)
                if c:
                    d[c][j].add(int(s == -1))
    return {c: tuple(sorted((j, sum(1 << b for b in bits))
                             for j, bits in ports.items()))
            for c, ports in d.items()}


def graph_result(word):
    """Full 3-phase graph over every bit assignment to active ports."""
    m = max(j for phase in word for j, _ in phase) + 1
    q = 1 << m
    total = 3 * q
    edge = [[] for _ in range(total)]
    indegree = [0] * total
    for phase in range(3):
        for x in range(q):
            src = phase*q + x
            for j, mask in word[phase]:
                if mask & (1 << ((x >> j) & 1)):
                    dest = ((phase+1) % 3)*q + (x ^ (1 << j))
                    edge[src].append(dest)
                    indegree[dest] += 1
    queue = deque(i for i in range(total) if not indegree[i])
    length = [0] * total
    examined = 0
    while queue:
        src = queue.popleft()
        examined += 1
        for dest in edge[src]:
            length[dest] = max(length[dest], length[src]+1)
            indegree[dest] -= 1
            if not indegree[dest]:
                queue.append(dest)
    if examined == total:
        return {'kind': 'FINITE', 'max_steps': max(length)}
    # A genuinely phase-aligned 6-step loop, not just an unspecified cycle.
    for x0 in range(q):
        reachable = {x0}
        for t in range(6):
            reachable = {x ^ (1 << j)
                         for x in reachable for j, mask in word[t%3]
                         if mask & (1 << ((x >> j) & 1))}
        if x0 in reachable:
            return {'kind': 'SIX_STEP_CYCLE', 'initial_bits': x0}
    return {'kind': 'CYCLE_WITHOUT_SIX', 'initial_bits': None}


def structurally_admissible(word):
    """Each mask-3 port has a unique mask-2 successor among (2,3) stages.

    The identity follows from real signed-source arithmetic: such stages
    represent c=3*2**j, with mask-3 at j and mask-2 at j+1.
    """
    pairings = {}
    for phase in word:
        if sorted(mask for _, mask in phase) != [2, 3]:
            continue
        both = next(j for j, mask in phase if mask == 3)
        one = next(j for j, mask in phase if mask == 2)
        if both in pairings and pairings[both] != one:
            return False
        pairings[both] = one
    return True


def count_classes():
    stats = Counter()
    maximum = 0
    extremizers = []
    rejected_extremizers = []
    phase_cycle_counterexample = []
    for kinds in product(LOCAL_TYPES, repeat=3):
        sizes = tuple(map(len, kinds))
        for labels in canonical_port_assignments(sum(sizes)):
            pos = 0
            word = []
            for kind in kinds:
                selected = labels[pos:pos+len(kind)]
                pos += len(kind)
                if len(set(selected)) != len(selected):
                    break
                word.append(tuple(zip(selected, kind)))
            if len(word) != 3:
                continue
            word = tuple(word)
            answer = graph_result(word)
            admissible = structurally_admissible(word)
            stats['all_classes'] += 1
            stats['admissible_classes' if admissible else 'excluded_classes'] += 1
            if answer['kind'] == 'CYCLE_WITHOUT_SIX':
                phase_cycle_counterexample.append(word)
            if answer['kind'] == 'FINITE':
                stats['finite_classes'] += 1
                d = answer['max_steps']
                if d > 13:
                    rejected_extremizers.append({'word': word, 'steps': d,
                                                  'admissible': admissible})
                if admissible and d > maximum:
                    maximum = d
                    extremizers = [word]
                elif admissible and d == maximum:
                    extremizers.append(word)
            else:
                stats['cycle_classes'] += 1
    assert stats['all_classes'] == 4207
    assert not phase_cycle_counterexample
    assert maximum == 13
    assert len(rejected_extremizers) == 12
    assert all(e['steps'] == 14 and not e['admissible']
               for e in rejected_extremizers)
    return stats, maximum, extremizers, rejected_extremizers


def direct_fixture():
    word = (12, 4, 20)
    d = nonzero_residual_dictionary(5)
    graph = graph_result([d[c] for c in word])
    assert graph == {'kind': 'FINITE', 'max_steps': 13}
    # The phase-zero initial state 31 has the 13-step path recorded in PREFIX-982.
    xs = (31, 27, 31, 15, 11, 15, 11, 3, 7, 3, 7, 5, 1, 5)
    ports = (2, 2, 4, 2, 2, 2, 3, 2, 2, 2, 1, 2, 2)
    for t, j in enumerate(ports):
        assert xs[t] ^ (1 << j) == xs[t+1]
        assert any(k == j and mask & (1 << ((xs[t] >> j) & 1))
                   for k, mask in d[word[t%3]])
    return {'residual_word': word, 'path_ports': ports,
            'initial_state': xs[0], 'final_state_after_13_steps': xs[-1]}


def check_residual_type_family():
    counts = {}
    for p in range(3, 20):
        d = nonzero_residual_dictionary(p)
        for c, ports in d.items():
            assert tuple(sorted(mask for _,mask in ports)) in LOCAL_TYPES, (p,c,ports)
        counts[str(p)] = len(d)
    return counts


def main():
    stats, maximum, witnesses, excluded = count_classes()
    dsize = check_residual_type_family()
    witness = direct_fixture()
    result = {
        'schema': 'PREFIX983_R6_UNIFORM_THREE_RESIDUAL_DICHOTOMY_V1',
        'model': 'auxiliary signed-source bit-flip observer; nonzero residuals only',
        'parameters': {'word_length': 3, 'all_p': 'p>=3',
                       'local_port_mask_types': LOCAL_TYPES},
        'abstract_graph_census': dict(stats),
        'max_finite_steps_admissible': maximum,
        'cycle_without_phase_aligned_6_step_loop_count': 0,
        'all_14_step_abstract_exceptions': len(excluded),
        'exceptions_all_violate_same_both_port_unique_successor': True,
        'admissible_13_step_extremizer_count': len(witnesses),
        'sharp_real_residual_fixture': witness,
        'type_family_checked_real_p_3_to_19': dsize,
        'evidence_status': 'AUTHOR_FINITE_EXHAUSTIVE_CERTIFICATE_NOT_INDEPENDENTLY_REVIEWED',
        'native_x6_embedding': 'NOT_ESTABLISHED',
        'frozen_science_pin': 'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json'
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
