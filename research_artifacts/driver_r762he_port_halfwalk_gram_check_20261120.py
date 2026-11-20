#!/usr/bin/env python3
"""Finite arithmetic for the R762HD/HE candidate Port gate, not native admission."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations

PORTS = list(combinations(range(6), 2))
NEI = {p: [q for q in range(15) if len(set(PORTS[p]) & set(PORTS[q])) == 1]
       for p in range(15)}
SUPPORT = {(p, q): sum(1 << a for a in set(PORTS[p]) | set(PORTS[q]))
           for p in range(15) for q in NEI[p]}
ZERO = (0,) * 6


def signed_halfwalk_gram(kmax=6):
    # N_k(P,d) counts signed length-k paths from P0 to P with Cell delta d.
    N = {(0, ZERO): 1}
    out = []
    for k in range(kmax + 1):
        out.append((k, len(N), sum(n*n for n in N.values())))
        if k == kmax:
            break
        next_N = defaultdict(int)
        for (p, delta), n in N.items():
            for q in NEI[p]:
                supp = SUPPORT[p, q]
                v = tuple(int(bool(supp & (1 << a))) for a in range(6))
                for sign in (-1, +1):
                    d = tuple(delta[a] + sign*v[a] for a in range(6))
                    next_N[(q, d)] += n
        N = next_N
    return out


@lru_cache(None)
def reachable(remaining, port):
    # Achievable XOR supports along a path ending at Port0.
    if remaining == 0:
        return frozenset([0]) if port == 0 else frozenset()
    return frozenset(SUPPORT[port, q] ^ residual
                     for q in NEI[port]
                     for residual in reachable(remaining - 1, q))


@lru_cache(None)
def half_sign_sums(masks):
    counts = Counter()
    for bits in range(1 << len(masks)):
        delta = tuple(sum((1 if bits & (1 << j) else -1)
                          * int(bool(mask & (1 << a)))
                          for j, mask in enumerate(masks))
                      for a in range(6))
        counts[delta] += 1
    return counts


@lru_cache(None)
def sign_completions(support_masks):
    mid = len(support_masks) // 2
    left = half_sign_sums(support_masks[:mid])
    right = half_sign_sums(support_masks[mid:])
    return sum(n*right.get(tuple(-x for x in delta), 0)
               for delta, n in left.items())


def parity_pass_sign_histogram(m):
    # Exhaustive Port0-to-Port0 walks with XOR triple supports=0.
    histogram = Counter()

    def walk(port, remaining, parity, supports):
        if remaining == 0:
            assert port == 0 and parity == 0
            histogram[sign_completions(tuple(supports))] += 1
            return
        for q in NEI[port]:
            new_parity = parity ^ SUPPORT[port, q]
            if new_parity in reachable(remaining - 1, q):
                walk(q, remaining - 1, new_parity,
                     supports + [SUPPORT[port, q]])

    walk(0, m, 0, [])
    return histogram


if __name__ == '__main__':
    gram = signed_halfwalk_gram(6)
    expected = [1, 16, 624, 34688, 2413424, 200986368, 19705107552]
    assert [row[2] for row in gram] == expected
    print('even signed Cell+Port return counts (m, states at m/2, count):')
    for k, states, count in gram:
        print(2*k, states, count)

    hist = parity_pass_sign_histogram(8)
    assert hist == Counter({4:9600, 6:19200, 8:33120, 10:7200,
                            12:47808, 16:18936, 18:7632, 20:4224,
                            24:23136, 36:2112, 40:4224, 70:344})
    assert sum(hist.values()) == 177536
    assert sum(count*freq for count, freq in hist.items()) == expected[4]
    assert 0 not in hist
    print('m=8 parity-pass count:', sum(hist.values()))
    print('m=8 exact sign-completion histogram:', sorted(hist.items()))
    print('PASS: half-walk Gram transfer and independent exhaustive parity audit')
