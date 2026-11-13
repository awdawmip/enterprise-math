"""Exact R762 S6/V29 signed-port overlap commutator verifier, Python stdlib."""
from collections import Counter, defaultdict
from itertools import combinations, product

N = 6
IDENTITY = tuple(range(N))


def compose(p, q):
    """p after q, on 0-based six native axis labels."""
    return tuple(p[q[i]] for i in range(N))


def inverse(p):
    return tuple(p.index(i) for i in range(N))


def permutation_cycle(indices):
    p = list(IDENTITY)
    for a, b in zip(indices, indices[1:] + indices[:1]):
        p[a] = b
    return tuple(p)


def cycle_type(p):
    seen = set()
    result = []
    for i in range(N):
        if i in seen:
            continue
        j, size = i, 0
        while j not in seen:
            seen.add(j)
            size += 1
            j = p[j]
        if size > 1:
            result.append(size)
    return tuple(sorted(result, reverse=True))


def make_event(axis_set, signs, backwards):
    axes = list(axis_set)
    if backwards:
        axes[1], axes[2] = axes[2], axes[1]
    signed = tuple((a, signs[axis_set.index(a)]) for a in axes)
    ledger = Counter((signed[k], signed[(k + 1) % 3]) for k in range(3))
    return axis_set, signed, permutation_cycle(axes), ledger


def main():
    events = [
        make_event(axis_set, signs, backwards)
        for axis_set in combinations(range(N), 3)
        for signs in product((-1, 1), repeat=3)
        for backwards in (False, True)
    ]
    assert len(events) == 320
    oriented = {frame for _, _, frame, _ in events}
    assert len(oriented) == 40
    assert all(sum(ledger.values()) == 3 for _, _, _, ledger in events)
    assert all(
        Counter(x for (x, _), count in ledger.items() for _ in range(count))
        == Counter(y for (_, y), count in ledger.items() for _ in range(count))
        for _, _, _, ledger in events
    )

    frame_counts = Counter()
    support_frame_counts = defaultdict(Counter)
    frame_values = defaultdict(set)
    for A, _, a, count_a in events:
        for B, _, b, count_b in events:
            k = len(set(A) & set(B))
            ab = compose(a, b)
            ba = compose(b, a)
            defect = compose(ab, inverse(ba))
            observed_type = cycle_type(defect)
            expected = () if k in (0, 3) else (3,) if k == 1 else (2, 2)
            assert observed_type == expected
            # The positive V29 count ledger is additive and schedule independent.
            assert count_a + count_b == count_b + count_a
            frame_counts[(k, observed_type)] += 1
            support_frame_counts[k][defect] += 1
            frame_values[k].add(defect)
    assert frame_counts == Counter({
        (0, ()): 5120, (1, (3,)): 46080,
        (2, (2, 2)): 46080, (3, ()): 5120,
    })
    assert [len(frame_values[k]) for k in range(4)] == [1, 40, 45, 1]
    assert set(support_frame_counts[1].values()) == {1152}
    assert set(support_frame_counts[2].values()) == {1024}
    assert support_frame_counts[0] == Counter({IDENTITY: 5120})
    assert support_frame_counts[3] == Counter({IDENTITY: 5120})

    # Strip signed-source multiplicity to independently verify all 40^2 frame pairs.
    bare = {p: frozenset(i for i in range(N) if p[i] != i) for p in oriented}
    unsigned_counts = Counter()
    for a, b in product(oriented, repeat=2):
        k = len(bare[a] & bare[b])
        defect = compose(compose(a, b), inverse(compose(b, a)))
        unsigned_counts[(k, cycle_type(defect))] += 1
    assert unsigned_counts == Counter({
        (0, ()): 80, (1, (3,)): 720,
        (2, (2, 2)): 720, (3, ()): 80,
    })
    assert sum(unsigned_counts.values()) == 1600
    print('PASS: 320 signed events, 40 orientation frames, 102400 ordered event pairs')
    print('support overlap 0,1,2,3 = 5120,46080,46080,5120')
    print('defect conjugacy: identity 10240, 3-cycle 46080, double transposition 46080')
    print('distinct defects = 86; multiplicities: each 3-cycle 1152; each double transposition 1024')
    print('unsigned orientation pairs = 1600; overlap 0,1,2,3 = 80,720,720,80')


if __name__ == '__main__':
    main()
