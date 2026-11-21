#!/usr/bin/env python3
"""Exact finite six-axis Port-sign repair certificate; no floating arithmetic."""
from collections import Counter
from itertools import combinations, product

T = list(combinations(range(6), 3))
LABEL = [''.join(map(str, s)) for s in T]
INDEX = {name: k for k, name in enumerate(LABEL)}
FULL = (1 << len(T)) - 1
CORES = [
    ('024', '035', '125', '134'),
    ('012', '015', '025', '034', '123', '124'),
    ('012', '013', '014', '025', '035', '045', '125', '135', '145', '234'),
]
# 20-bit masks in T's lexicographic support order. Each is a proposed
# maximal nonsignable even-pair presence mask for the corresponding core.
BAD_MAX_HEX = [
    ('13301', '19122', '23222', '2a121', '42528', '43114',
     '5b525', '63339', '81524', '83038', '93336', 'ab52a'),
    ('6ccc9', '80cc8'),
    ('1d347',),
]
ZERO = (0,) * 6
VEC = [tuple(int(i in s) for i in range(6)) for s in T]


def members(mask):
    return [i for i in range(20) if mask & (1 << i)]


def minimal_masks(items):
    ordered = sorted(set(items), key=lambda q: (q.bit_count(), q))
    result = []
    for q in ordered:
        if not any((q & p) == p for p in result):
            result.append(q)
    return result


def minimal_hitting_sets(bad_max):
    """Duality: Q is good iff it hits every complement of a bad maximal Q."""
    out = [0]
    for b in bad_max:
        edge = FULL ^ b
        nxt = []
        for q in out:
            if q & edge:
                nxt.append(q)
            else:
                nxt.extend(q | (1 << j) for j in members(edge))
        out = minimal_masks(nxt)
    return out


def core_targets(core):
    out = {}
    for eps in product((-1, 1), repeat=len(core)):
        w = tuple(-sum(eps[j] * VEC[s][i] for j, s in enumerate(core)) // 2
                  for i in range(6))
        out.setdefault(w, eps)
    return out


def pair_reachable(q):
    """Return every sum of z_S*h_S with z_S in {-1,0,+1} and one witness."""
    got = {ZERO: ()}
    for j in members(q):
        nxt = {}
        for v, words in got.items():
            for z in (-1, 0, 1):
                w = tuple(v[i] + z * VEC[j][i] for i in range(6))
                if w not in nxt:
                    nxt[w] = words + (z,)
        got = nxt
    return got


def signing_witness(core, q):
    goals = core_targets(core)
    reached = pair_reachable(q)
    for target, eps in goals.items():
        if target in reached:
            return eps, reached[target]
    return None


PORTS = list(combinations(range(6), 2))
PORT_INDEX = {p: i for i, p in enumerate(PORTS)}
PORT_TRIANGLE = [tuple(PORT_INDEX[p] for p in combinations(s, 2)) for s in T]
EDGE_BOUNDARY = [tuple((1 << a) ^ (1 << b)
                       for a, b in combinations(ps, 2)) for ps in PORT_TRIANGLE]
SUPPORT_ADJ = [sum(1 << j for j, t in enumerate(T)
                   if len(set(s) & set(t)) == 2) for s in T]


def support_components(support_mask):
    remaining = support_mask
    components = []
    while remaining:
        reached = remaining & -remaining
        while True:
            grow = reached
            for j in members(reached):
                grow |= SUPPORT_ADJ[j] & support_mask
            if grow == reached:
                break
            reached = grow
        components.append(reached)
        remaining ^= reached
    return components


def even_port_degrees_possible(core, q):
    core_parities = {0}
    for j in core:
        core_parities = {v ^ edge for v in core_parities
                         for edge in EDGE_BOUNDARY[j]}
    basis = [0] * 15
    for j in members(q):
        for edge in EDGE_BOUNDARY[j]:
            v = edge
            for k in range(14, -1, -1):
                if v & (1 << k):
                    if basis[k]:
                        v ^= basis[k]
                    else:
                        basis[k] = v
                        break
    for p in core_parities:
        v = p
        for k in range(14, -1, -1):
            if v & (1 << k):
                v ^= basis[k]
        if v == 0:
            return True
    return False


def main():
    report = []
    for core_labels, hex_masks, expected in zip(CORES, BAD_MAX_HEX,
                                                 ((3824, 48, (4, 12, 24, 8)),
                                                  (1056, 14, (9, 5)),
                                                  (1024, 10, (10,)))):
        core = [INDEX[x] for x in core_labels]
        bad_max = [int(x, 16) for x in hex_masks]
        assert all(signing_witness(core, b) is None for b in bad_max)
        coremask = sum(1 << j for j in core)
        negative_port_obstructions = Counter()
        for b in bad_max:
            components = support_components(coremask | b)
            core_components = sum(bool(c & coremask) for c in components)
            if core_components > 1:
                negative_port_obstructions['core_disconnected'] += 1
            else:
                assert even_port_degrees_possible(core, b) is False
                negative_port_obstructions['even_degree_impossible'] += 1
        good_min = minimal_hitting_sets(bad_max)
        assert all(signing_witness(core, q) is not None for q in good_min)
        assert all(all(signing_witness(core, q ^ (1 << j)) is None
                       for j in members(q)) for q in good_min)
        # Independent Boolean coverage: every Q has exactly one classification.
        good = bytearray(1 << 20)
        for q in good_min:
            for sup in range(1 << 20):
                if (sup & q) == q:
                    good[sup] = 1
        count_bad = 0
        for q in range(1 << 20):
            bad = any((q & b) == q for b in bad_max)
            assert bad ^ bool(good[q])
            count_bad += bad
        hist = Counter(q.bit_count() for q in good_min)
        assert (count_bad, len(good_min), tuple(hist[k] for k in sorted(hist))) == expected
        report.append((len(core), count_bad, len(good_min), dict(sorted(hist.items())),
                       dict(negative_port_obstructions)))
        print('core', len(core), 'bad Q', count_bad, 'minimal repairs',
              len(good_min), 'repair sizes', dict(sorted(hist.items())),
              'Port obstructions', dict(negative_port_obstructions), flush=True)
        if len(core) == 4:
            q = max(good_min, key=int.bit_count)
            eps, z = signing_witness(core, q)
            print('four-pair template', [LABEL[j] for j in members(q)],
                  'core signs', eps, 'pair coefficients', z)
    print('PASS R762ID exact six-axis finite certificate', report)


if __name__ == '__main__':
    main()
