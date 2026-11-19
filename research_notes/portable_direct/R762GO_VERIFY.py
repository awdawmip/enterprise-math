#!/usr/bin/env python3
"""R762GO: certified finite-state absorption block and hitting-time interval.
Pure Python integer/rational arithmetic. Exact R762GM/GN moving-Port signed
K4-STAR candidate, not an adopted native TRIADIC_CLOSURE_E law.
"""
import json
from collections import deque
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations, permutations

VERTICES = range(4)
EDGES = tuple(combinations(VERTICES, 2))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}
STARS = tuple(tuple(EDGE_ID[tuple(sorted((v, w)))] for w in VERTICES if w != v)
              for v in VERTICES)
IDENTITY = tuple(range(6))
PORT0 = EDGE_ID[(0, 1)]
PORT_SINK = EDGE_ID[(2, 3)]

def even(p):
    return sum(p[i] > p[j] for i in range(6) for j in range(i+1, 6)) % 2 == 0

def compose(p, q):
    return tuple(p[q[i]] for i in range(6))

def inverse(p):
    return tuple(p.index(i) for i in range(6))

def triad_cycle(triple):
    p = list(IDENTITY)
    a, b, c = triple
    p[a], p[b], p[c] = b, c, a
    return tuple(p)

def graph():
    rotations = tuple(p for p in permutations(IDENTITY) if even(p))
    index = {p: i for i, p in enumerate(rotations)}
    cycles = tuple(triad_cycle(t) for t in STARS)
    inverses = tuple(inverse(p) for p in cycles)
    neighbors = []
    for p in rotations:
        targets = []
        for v in EDGES[p[PORT0]]:
            for g in (inverses[v], cycles[v]):
                targets.append(index[compose(p, g)])
        neighbors.append(tuple(targets))
    return rotations, neighbors

def forward_survival(neighbors, sink, length):
    """Positive BRC counts of length-m words from identity avoiding sink."""
    masses = [0] * len(neighbors)
    masses[0] = 1
    counts = []
    for m in range(length+1):
        counts.append(sum(masses))
        if m < length:
            next_masses = [0] * len(neighbors)
            for i, count in enumerate(masses):
                if count:
                    for j in neighbors[i]:
                        if j not in sink:
                            next_masses[j] += count
            masses = next_masses
    return counts

def backward_survival(neighbors, sink, length):
    """Exact survival words for each rotation."""
    f = [int(i not in sink) for i in range(len(neighbors))]
    for _ in range(length):
        f = [0 if i in sink else sum(f[j] for j in neighbors[i])
             for i in range(len(neighbors))]
    return f

def compute():
    rotations, neighbors = graph()
    assert len(rotations) == 360 and rotations[0] == IDENTITY
    assert all(len(js) == 4 for js in neighbors)
    sink = {i for i, p in enumerate(rotations) if p[PORT0] == PORT_SINK}
    assert len(sink) == 60
    assert all(set(neighbors[i]) <= sink for i in sink)
    reachable = {0}
    queue = deque([0])
    predecessor = {0: None}
    while queue:
        i = queue.popleft()
        for choice, j in enumerate(neighbors[i]):
            if j not in reachable:
                reachable.add(j)
                predecessor[j] = (i, choice)
                queue.append(j)
    transient = reachable - sink
    assert len(reachable) == 350 and len(transient) == 290

    f8 = backward_survival(neighbors, sink, 8)
    winner_count = max(f8[i] for i in transient)
    winners = [i for i in transient if f8[i] == winner_count]
    assert winner_count == 39652 and len(winners) == 1
    winner = winners[0]
    assert rotations[winner] == (0, 2, 1, 4, 3, 5)
    assert f8[0] == 38036
    witness = []
    i = winner
    while i != 0:
        prev, choice = predecessor[i]
        witness.append(choice)
        i = prev
    witness.reverse()
    p = 0
    for choice in witness:
        p = neighbors[p][choice]
        assert p not in sink
    assert p == winner
    q = Fraction(winner_count, 4**8)
    assert q == Fraction(9913, 16384)

    # Independent forward and backward counts agree for all horizons <=20.
    small = forward_survival(neighbors, sink, 20)
    for n, count in enumerate(small):
        assert backward_survival(neighbors, sink, n)[0] == count
    assert small[12] == 6534252 and small[16] == 1118196052

    # E[tau] = sum_{m>=0} Pr(tau>m).
    # U_N / 4**N = sum_{m=0}^{N-1} S_m / 4**m.
    # Tail <= (S_N/4**N) * 8/(1-q).
    N = 400
    surv = forward_survival(neighbors, sink, N)
    denominator = 4 ** N
    U = sum(surv[m] * 4 ** (N-m) for m in range(N))
    lower = Fraction(U, denominator)
    remainder = Fraction(surv[N], denominator) * 8 / (1-q)
    upper = lower + remainder
    with localcontext() as ctx:
        ctx.prec = 85
        decimal_lower = Decimal(lower.numerator)/Decimal(lower.denominator)
        decimal_upper = Decimal(upper.numerator)/Decimal(upper.denominator)
        width = Decimal(remainder.numerator)/Decimal(remainder.denominator)
        assert decimal_lower < decimal_upper
    return {
        "schema": "R762GO_MOVING_PORT_SHARP_EIGHT_BLOCK_AND_MEAN_CERTIFICATE_V1",
        "status": "PASS",
        "model": "R762GM/GN signed K4-STAR moving Port e=p(01), four equally weighted authorized branches",
        "arithmetic": "integer exact dynamic programming; rational certified tail",
        "rotations": len(rotations),
        "sink_rotations": len(sink),
        "reachable_rotations": len(reachable),
        "reachable_transient_rotations": len(transient),
        "block_events": 8,
        "uniform_reachable_transient_max_surviving_words": winner_count,
        "total_words_per_block": 4**8,
        "sharp_conditional_eight_step_survival_bound": str(q),
        "attaining_rotation": list(rotations[winner]),
        "attaining_rotation_path_choice_indices": witness,
        "identity_eight_step_survivors": f8[0],
        "survival_small": {str(i): small[i] for i in (0,3,6,8,12,16,20)},
        "coarse_expected_hit_upper": str(8/(1-q)),
        "expectation_truncation_N": N,
        "expectation_lower_numerator_U": str(U),
        "expectation_denominator": str(denominator),
        "S_N": str(surv[N]),
        "expectation_tail_upper_formula": "(S_N/4^N)*8/(1-9913/16384)",
        "expected_hit_lower_decimal": str(decimal_lower),
        "expected_hit_upper_decimal": str(decimal_upper),
        "interval_width_upper_decimal": str(width),
        "review": "NOT_REVIEWED",
        "native_permission": "CANDIDATE_NOT_ADOPTED"
    }

if __name__ == "__main__":
    print(json.dumps(compute(), indent=2, ensure_ascii=False, sort_keys=True))
