"""R762CK: exact author-side reproduction, Python standard library only."""
from itertools import permutations, product
from collections import defaultdict
from math import gcd

def area(word, n=6):
    """word contains (0-based axis, signed unit); P_ij is ordered, A antisymmetric."""
    z = [0] * n
    p = [[0] * n for _ in range(n)]
    for axis, sign in word:
        for i in range(n):
            p[i][axis] += z[i] * sign
        z[axis] += sign
    return tuple(z), p

def block(i, j, turn):
    if turn:
        return [(i, 1), (j, 1), (i, -1), (j, -1)]
    return [(i, 1), (i, -1), (j, 1), (j, -1)]

def main():
    count = 0
    perms = list(permutations(range(6)))
    for signs in product((-1, 1), repeat=6):
        for order in perms:
            z, p = area([(i, signs[i]) for i in order])
            assert z == signs
            rank = {i: k for k, i in enumerate(order)}
            for i in range(6):
                for j in range(i+1, 6):
                    t = signs[i] * signs[j]
                    a = p[i][j] - p[j][i]
                    expected_before = rank[i] < rank[j]
                    assert p[i][j] == (t if expected_before else 0)
                    assert a == (t if expected_before else -t)
                    assert a == 2 * p[i][j] - z[i] * z[j]
                    assert a % 2 == 1
                    count += 1
    assert count == 691200
    table = []
    for q in range(2, 13):
        fibers = defaultdict(set)
        for c in product(range(q), repeat=3):
            fibers[tuple(2*x % q for x in c)].add(c)
        g = gcd(q, 2)
        assert len(fibers) == (q // g)**3
        assert set(map(len, fibers.values())) == {g**3}
        table.append((q, len(fibers), g**3))
    witnesses = []
    for q in (2, 4, 6, 8, 10):
        k = q // 2
        zb, pb = area(block(0, 1, False)*k)
        zl, pl = area(block(0, 1, True)*k)
        assert zb == zl == (0,)*6
        cb, cl = pb[0][1], pl[0][1]
        ab, al = pb[0][1]-pb[1][0], pl[0][1]-pl[1][0]
        assert (cb,cl) == (0,k)
        assert ab % q == al % q
        assert cb % q != cl % q
        witnesses.append((q, k))
    print({"signed_words":46080, "pair_checks":count,
           "fibers_d3_q2_to_12":table,
           "even_q_witnesses":witnesses, "result":"PASS"})

if __name__ == "__main__":
    main()
