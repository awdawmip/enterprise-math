#!/usr/bin/env python3
"""R762AH: exact typed source-count BRC, no physical/native claim.

Input: named source tokens 0..m-1, one ingress per token and one egress
per destination, central hub capacity B, forbidden home return. The
record erases outgoing source names but preserves all I/O ports and order.
All arithmetic is exact integer counting of label-preserving branches.
"""
import json
from collections import Counter, defaultdict
from functools import lru_cache


def sliding_word(m, B):
    assert 2 <= B <= m
    w = [('I', i) for i in range(B)]
    for j in range(m - B + 1):
        w.append(('O', j))
        if B + j < m:
            w.append(('I', B + j))
    w.extend(('O', j) for j in range(m - B + 1, m))
    assert len(w) == 2 * m
    return w


def direct_permanent_sliding(m, B):
    """Independent subset DP over actual distinct ingressed source labels."""
    assert 2 <= B <= m
    dp = {0: 1}
    for j in range(m):
        new = defaultdict(int)
        for mask, ways in dp.items():
            for i in range(min(m, j + B)):
                if i != j and not (mask >> i & 1):
                    new[mask | (1 << i)] += ways
        dp = new
    return dp.get((1 << m) - 1, 0)


def next_states(B, bits):
    """Old unused sources are distinct but future-diagonal equivalent."""
    high = 1 << (B - 2)
    old = B - 1 - bits.bit_count()
    out = defaultdict(int)
    if old:
        out[(bits >> 1) | high] += old
    for r in range(1, B - 1):
        if bits >> r & 1:
            out[((bits ^ (1 << r)) >> 1) | high] += 1
    out[bits >> 1] += 1
    return dict(out)


@lru_cache(None)
def terminal(B, bits):
    """Exact tail perfect matching after the final ingress."""
    old = B - 1 - bits.bit_count()
    sources = tuple(-(a + 1) for a in range(old)) + tuple(
        r for r in range(B - 1) if bits >> r & 1
    )
    assert len(sources) == B - 1

    @lru_cache(None)
    def f(j, used):
        if j == B - 1:
            return 1
        return sum(f(j + 1, used | (1 << k))
                   for k, src in enumerate(sources)
                   if not (used >> k & 1) and src != j)
    return f(0, 0)


def transfer_count(m, B):
    assert 2 <= B <= m
    states = {(1 << (B - 1)) - 1: 1}
    for _ in range(m - B + 1):
        nxt = defaultdict(int)
        for bits, ways in states.items():
            for newbits, multiplicity in next_states(B, bits).items():
                nxt[newbits] += ways * multiplicity
        states = nxt
    return sum(ways * terminal(B, bits) for bits, ways in states.items())


def physical_transcript_count(word, B):
    """Direct named-token transition DP, separate from transfer matrix."""
    states = {0: 1}
    entered = exited = 0
    for kind, j in word:
        nxt = defaultdict(int)
        if kind == 'I':
            if entered >> j & 1 or (entered.bit_count() - exited.bit_count()) >= B:
                return 0
            entered |= (1 << j)
            for mask, val in states.items():
                nxt[mask | (1 << j)] += val
        else:
            if not (entered >> j & 1) or exited >> j & 1:
                return 0
            exited |= (1 << j)
            for mask, val in states.items():
                candidates = mask & ~(1 << j)
                while candidates:
                    bit = candidates & -candidates
                    candidates -= bit
                    nxt[mask ^ bit] += val
        states = nxt
    return states.get(0, 0)


def complete_census(m, B):
    """All physical logs modulo relabeling by first-ingress order."""
    histogram = Counter()
    exemplars = []
    maximum = 0
    words = 0

    def walk(ingressed, exits, states, word):
        nonlocal words, maximum, exemplars
        occupancy = ingressed - exits.bit_count()
        if exits == (1 << m) - 1:
            k = states.get(0, 0)
            assert k
            words += 1
            if words % 997 == 0:
                assert k == physical_transcript_count(word, B)
            histogram[k] += 1
            if k > maximum:
                maximum, exemplars = k, [''.join(x + str(i) for x, i in word)]
            elif k == maximum and len(exemplars) < 2:
                exemplars.append(''.join(x + str(i) for x, i in word))
            return

        if ingressed < m and occupancy < B:
            new = {mask | (1 << ingressed): val for mask, val in states.items()}
            walk(ingressed + 1, exits, new, word + [('I', ingressed)])
        if occupancy:
            for j in range(ingressed):
                if exits >> j & 1:
                    continue
                new = defaultdict(int)
                for mask, val in states.items():
                    candidates = mask & ~(1 << j)
                    while candidates:
                        bit = candidates & -candidates
                        candidates -= bit
                        new[mask ^ bit] += val
                if new:
                    walk(ingressed, exits | (1 << j), new, word + [('O', j)])

    walk(0, 0, {0: 1}, [])
    return dict(m=m, capacity=B, normalized_realizable_words=words,
                largest_fiber=maximum,
                sliding_fiber=transfer_count(m, min(m, B)),
                maximizing_examples=exemplars,
                fiber_histogram={str(k): v for k, v in sorted(histogram.items())})


def main():
    canonical = []
    for B in (2, 3, 4):
        for m in range(B, 19):
            a = direct_permanent_sliding(m, B)
            b = transfer_count(m, B)
            c = physical_transcript_count(sliding_word(m, B), B)
            assert a == b == c, (m, B, a, b, c)
            canonical.append(dict(m=m, B=B, count=a))

    B3 = [transfer_count(m, 3) for m in range(3, 19)]
    for j in range(4, len(B3)):
        assert B3[j] == 2 * B3[j - 1] + B3[j - 2] + B3[j - 3] + B3[j - 4]
    assert [transfer_count(m, 3) for m in range(3, 11)] == \
           [2, 6, 15, 39, 101, 262, 679, 1760]
    matrix = [[next_states(3, s).get(t, 0) for t in range(4)] for s in range(4)]
    tail = [terminal(3, s) for s in range(4)]
    assert matrix == [[1, 0, 2, 0], [1, 0, 1, 0],
                      [0, 1, 1, 1], [0, 1, 1, 0]]
    assert tail == [2, 1, 1, 1]

    census = [complete_census(m, 3) for m in range(2, 11)]
    assert all(row['largest_fiber'] == row['sliding_fiber'] for row in census)
    assert [row['normalized_realizable_words'] for row in census] == \
           [2, 10, 54, 290, 1558, 8370, 44966, 241570, 1297782]
    return dict(
        schema='R762AH_THREE_SLOT_SLIDING_SOURCE_FIBER_V1',
        scientific_input='awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        model='conditional named-token shortest-transfer star; source-blind ordered port log',
        proof_scope='all m>=3 for B=3 canonical sliding log; fixed B matrix formula for all m>=B',
        finite_scope='B=2,3,4 sliding identities m=B..18; all normalized physically realizable B=3 logs m=2..10',
        matrix_B3=matrix, tail_B3=tail,
        characteristic_polynomial='lambda^4 - 2 lambda^3 - lambda^2 - lambda - 1',
        generating_function='(1+x^2)/(1-2x-x^2-x^3-x^4)',
        recurrence='f_m=2f_(m-1)+f_(m-2)+f_(m-3)+f_(m-4), m>=7',
        canonical_matches=canonical,
        complete_census=census,
        native_admission=False,
        claim_authorization=False,
        conjecture='Does B=3 sliding maximize fiber over all m? Checked only m<=10.'
    )


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, ensure_ascii=False))
