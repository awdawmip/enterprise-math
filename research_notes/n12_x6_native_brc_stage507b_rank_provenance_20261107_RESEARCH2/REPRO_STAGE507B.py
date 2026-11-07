#!/usr/bin/env python3
"""Stage507-B: exact rank-aware BRC piece proof checks (stdlib, no RNG)."""
from itertools import product
import json

Q = 12
DIRECTIONS = (0, 1, 2)  # subsets of signed native six-axis domain


def vector(a):
    v = [0] * 6
    v[a // 2] = 1 if a % 2 == 0 else -1
    return tuple(v)

V = [vector(a) for a in range(Q)]
ZERO = (0,) * 6
ZERO_E = (0,) * (Q * Q)


def fword(word):
    """Return exact (length, 6-displacement, 144 directed edges, first, last)."""
    ds = [0] * 6
    e = [0] * (Q * Q)
    for a in word:
        for j in range(6):
            ds[j] += V[a][j]
    for a, b in zip(word, word[1:]):
        e[a * Q + b] += 1
    return (len(word), tuple(ds), tuple(e), word[0] if word else None,
            word[-1] if word else None)


def append_f(x, y):
    if not x[0]:
        return y
    if not y[0]:
        return x
    e = [a + b for a, b in zip(x[2], y[2])]
    e[x[4] * Q + y[3]] += 1
    return (x[0] + y[0], tuple(a + b for a, b in zip(x[1], y[1])),
            tuple(e), x[3], y[4])


def fpieces(pieces):
    result = (0, ZERO, ZERO_E, None, None)
    for p in pieces:
        result = append_f(result, fword((p[1],)) if p[0] == 'E' else p[1])
    return result


def observe(word):
    return fword([a for a, _ in word])[:3]


def mask(length, h, R, S, word, budget=None):
    # The Stage506 conservative reachability halo + rightmost M public tokens.
    B = set(range(min(length, h + 3)))
    for r in R:
        B.update(q for q in range(r - h, r + h + 1) if 0 <= q < length)
    keep = {length - 1 - q for q in B}
    M = (max(S) + h - 1 if S and h else 0) if budget is None else budget
    seen = 0
    for i in range(length - 1, -1, -1):
        if word[i][1]:
            if seen < M:
                keep.add(i)
            seen += 1
    return keep


def compress(word, h, R, S, budget=None):
    keep = mask(len(word), h, R, S, word, budget)
    pieces, i = [], 0
    while i < len(word):
        if i in keep:
            pieces.append(('E', word[i][0], word[i][1]))
            i += 1
        else:
            j = i
            while j < len(word) and j not in keep:
                j += 1
            pieces.append(('G', fword([a for a, _ in word[i:j]])))
            i = j
    return tuple(pieces)


def offset_to_piece(pieces, q):
    """Locate exact token at end-offset q; must be explicit if accessed."""
    n = sum(1 if x[0] == 'E' else x[1][0] for x in pieces)
    i = n - 1 - q
    if i < 0 or i >= n:
        return None
    c = 0
    for j, p in enumerate(pieces):
        length = 1 if p[0] == 'E' else p[1][0]
        if c <= i < c + length:
            assert p[0] == 'E', ('opaque-position-access', n, q, pieces)
            return j
        c += length
    raise AssertionError('unlocated')


def piece_step(pieces, action):
    kind, arg = action
    n = sum(1 if x[0] == 'E' else x[1][0] for x in pieces)
    z = list(pieces)
    if kind == 'POP' and n >= 1:
        del z[offset_to_piece(z, 0)]
    elif kind == 'DELETE2' and n >= 3:
        del z[offset_to_piece(z, 2)]
    elif kind == 'SET' and n > arg[0]:
        j = offset_to_piece(z, arg[0])
        z[j] = ('E', arg[1], z[j][2])
    elif kind == 'INSERT2' and n >= 2:
        j = offset_to_piece(z, 1)
        z.insert(j, ('E', arg, True))
    elif kind == 'DELETE_PUBLIC':
        selected = [j for j in range(len(z) - 1, -1, -1) if z[j][0] == 'E' and z[j][2]]
        if len(selected) < arg:
            return None
        del z[selected[arg - 1]]
    else:
        return None
    return tuple(z)


def raw_step(word, action):
    kind, arg = action
    z = list(word)
    if kind == 'POP' and len(z) >= 1:
        z.pop()
    elif kind == 'DELETE2' and len(z) >= 3:
        z.pop(-3)
    elif kind == 'SET' and len(z) > arg[0]:
        i = len(z) - 1 - arg[0]
        z[i] = (arg[1], z[i][1])
    elif kind == 'INSERT2' and len(z) >= 2:
        z.insert(len(z) - 2, (arg, True))
    elif kind == 'DELETE_PUBLIC':
        inds = [i for i in range(len(z) - 1, -1, -1) if z[i][1]]
        if len(inds) < arg:
            return None
        z.pop(inds[arg - 1])
    else:
        return None
    return tuple(z)


def actions(R, S):
    a = [('POP', None), ('DELETE2', None)]
    a += [('INSERT2', d) for d in (0, 2)]
    a += [('SET', (r, d)) for r in R for d in (0, 2)]
    a += [('DELETE_PUBLIC', k) for k in S]
    return tuple(a)


ROOTS = NODES = TRANSITIONS = COLLISIONS = SHARPNESS = 0


def verify(word, h, R, S):
    global ROOTS, NODES, TRANSITIONS
    ROOTS += 1
    root = compress(word, h, R, S)
    assert observe(word) == fpieces(root)[:3]
    active = [(word, root)]
    A = actions(R, S)
    for d in range(h + 1):
        future = []
        for raw, pieces in active:
            NODES += 1
            assert observe(raw) == fpieces(pieces)[:3]
            if d == h:
                continue
            for a in A:
                TRANSITIONS += 1
                rr, pp = raw_step(raw, a), piece_step(pieces, a)
                assert (rr is None) == (pp is None), ('legal', raw, pieces, a)
                if rr is not None:
                    assert observe(rr) == fpieces(pp)[:3], ('observer', raw, pieces, a)
                    future.append((rr, pp))
        active = future


def collision_test():
    # Same directions; unrecorded older public provenance differs, but M=K+h-1
    # rightmost P tags identical. All future rank deletions within h are indistinguishable.
    global COLLISIONS
    h, R, S = 3, (2, 5), (1, 2)
    directions = (2, 0, 0, 2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0)
    p1 = {0, 12, 14, 15, 16, 17}
    p2 = {1, 12, 14, 15, 16, 17}
    x = tuple((d, i in p1) for i, d in enumerate(directions))
    y = tuple((d, i in p2) for i, d in enumerate(directions))
    assert x != y and compress(x, h, R, S) == compress(y, h, R, S)
    verify(x, h, R, S)
    verify(y, h, R, S)
    COLLISIONS += 1


def sharpness_test():
    """Rightmost M-1 P truncation fails exactly at operation h, K in S."""
    global SHARPNESS
    for K in range(1, 5):
        for h in range(1, 5):
            M = K + h - 1
            # Hidden B,A prefix and a distant group of M-1 trailing P tags.
            n = M + h + 12
            directions = (2,) + (0,) * (n - 1)
            late = set(range(n - M + 1, n))
            x = tuple((a, (i == 0 or i in late)) for i, a in enumerate(directions))
            y = tuple((a, (i == 1 or i in late)) for i, a in enumerate(directions))
            R, S = (2, 5), (K,)
            assert compress(x, h, R, S, budget=M-1) == compress(y, h, R, S, budget=M-1)
            assert compress(x, h, R, S) != compress(y, h, R, S)
            for j in range(h - 1):
                x = raw_step(x, ('POP', None))
                y = raw_step(y, ('POP', None))
                assert observe(x) == observe(y)
            rx, ry = raw_step(x, ('DELETE_PUBLIC', K)), raw_step(y, ('DELETE_PUBLIC', K))
            assert rx is not None and ry is not None and observe(rx) != observe(ry)
            SHARPNESS += 1


def main():
    Slist = ((1,), (1, 2), (1, 3))
    for h, max_len, R in ((1, 5, (2,)), (2, 4, (2, 4))):
        for S in Slist:
            for n in range(max_len + 1):
                for encoded in product(range(6), repeat=n):
                    word = tuple((DIRECTIONS[z // 2], bool(z % 2)) for z in encoded)
                    verify(word, h, R, S)
    # Declared deterministic full six-axis samples at h=3, lengths up to 18.
    for S in Slist:
        for n in range(1, 19):
            word = tuple(((7 * i + n + i * i) % 12, (i * i + 3 * n + 7 * i) % 5 == 0)
                         for i in range(n))
            verify(word, 3, (2, 5), S)
    collision_test()
    sharpness_test()
    print(json.dumps({'stage':'507-B','alphabet':'12 signed X6 directions',
        'observer':'length+six displacement+144 directed adjacency counts',
        'exhaustive': 'all 6^n tagged 3-direction words n<=5 for h1, n<=4 for h2, 3 S sets',
        'h3_deterministic': '54 tagged 12-direction inputs lengths 1..18, three S sets',
        'collision_pairs': COLLISIONS, 'sharpness_witnesses':SHARPNESS, 'roots':ROOTS, 'prefix_nodes':NODES,
        'tested_transitions':TRANSITIONS,'assertions':'PASS'}, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
