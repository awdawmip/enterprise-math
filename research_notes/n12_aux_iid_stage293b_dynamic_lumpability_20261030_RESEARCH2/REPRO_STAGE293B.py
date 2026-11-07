#!/usr/bin/env python3
"""Stage293-B exact finite-state partition and weighted-TV witness."""
from fractions import Fraction as F

STATES = ('a', 'b', 'c', 'd')
OUTPUT = {'a': 0, 'b': 0, 'c': 0, 'd': 1}
NEXT = {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'd'}
INITIAL = {'a': F(1, 3), 'b': F(2, 3), 'c': F(0), 'd': F(0)}

def reachable():
    todo = [s for s in STATES if INITIAL[s]]
    seen = set(todo)
    while todo:
        t = NEXT[todo.pop()]
        if t not in seen:
            seen.add(t)
            todo.append(t)
    return tuple(s for s in STATES if s in seen)

def traces(s, horizon):
    path = [OUTPUT[s]]
    for _ in range(horizon):
        s = NEXT[s]
        path.append(OUTPUT[s])
    return tuple(path)

def refine(blocks):
    result = []
    for block in blocks:
        bins = {}
        for s in block:
            sig = tuple(F(NEXT[s] in target) for target in blocks)
            bins.setdefault(sig, []).append(s)
        result.extend(tuple(v) for v in bins.values())
    return tuple(result)

def all_partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in all_partitions(tuple(rest)):
        for j in range(len(partition)):
            result = list(partition)
            result[j] = tuple((first,) + result[j])
            yield tuple(result)
        yield ((first,),) + partition

def output_factors(partition):
    return all(len({OUTPUT[s] for s in b}) == 1 for b in partition)

def transition_factors(partition):
    for block in partition:
        for s in block:
            for t in block:
                for target in partition:
                    mass_s = sum((F(NEXT[s] == x) for x in target), F(0))
                    mass_t = sum((F(NEXT[t] == x) for x in target), F(0))
                    if mass_s != mass_t:
                        return False
    return True

def main():
    R = reachable()
    assert R == STATES
    assert sum(INITIAL.values(), F(0)) == 1
    assert traces('a', 1) == traces('b', 1) == (0, 0)
    assert traces('a', 2) == (0, 0, 1)
    assert traces('b', 2) == (0, 0, 0)
    blocks = (('a', 'b', 'c'), ('d',))
    levels = [len(blocks)]
    while True:
        new = refine(blocks)
        levels.append(len(new))
        if new == blocks:
            break
        blocks = new
    assert levels == [2, 3, 4, 4], levels
    partitions = list(all_partitions(R))
    assert len(partitions) == 15
    acceptable = [p for p in partitions if output_factors(p) and transition_factors(p)]
    assert len(acceptable) == 1
    assert len(acceptable[0]) == 4
    for q in (F(0), F(1, 7), F(1, 3), F(1, 2), F(1)):
        error = INITIAL['a'] * (1 - q) + INITIAL['b'] * q
        assert error == F(1, 3) + q / 3
        assert error >= F(1, 3)
    optimum_q = F(0)
    optimum = INITIAL['a'] * (1 - optimum_q) + INITIAL['b'] * optimum_q
    assert optimum == F(1, 3)
    pooled_q = F(1, 3)
    assert abs(pooled_q - (INITIAL['a'] * 1 + INITIAL['b'] * 0)) == 0
    assert INITIAL['a'] * (1 - pooled_q) + INITIAL['b'] * pooled_q == F(4, 9)
    print('REACHABLE', ','.join(R))
    print('PARTITION_REFINEMENT_BLOCK_COUNTS', ','.join(map(str, levels)))
    print('ALL_PARTITIONS', len(partitions), 'EXACT_STRONG_LUMPABLE', len(acceptable))
    print('STAGE0_1_TRACES', traces('a', 1), traces('b', 1))
    print('STAGE2_TRACES', traces('a', 2), traces('b', 2))
    print('ONE_LABEL_WEIGHTED_CONDITIONAL_TV', optimum)
    print('POOLED_MATCH_Q', pooled_q, 'POOLED_TV', F(0), 'CONDITIONAL_TV', F(4, 9))
    print('STAGE293B_DYNAMIC_REACHABILITY_LUMPABILITY_EXACT_PASS')

if __name__ == '__main__':
    main()
