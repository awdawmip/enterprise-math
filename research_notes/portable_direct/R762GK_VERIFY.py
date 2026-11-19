#!/usr/bin/env python3
"""R762GK — exact integer verification for the Klein-four BRC word-bijection theorem.
Pure Python 3 standard library. No floating point arithmetic and no external inputs.
"""
import itertools
import json
from collections import Counter

EDGES = tuple(itertools.combinations(range(4), 2))
EDGE_ID = {edge: i for i, edge in enumerate(EDGES)}
STARS = tuple(tuple(EDGE_ID[tuple(sorted((v, w)))] for w in range(4) if w != v)
              for v in range(4))
V4 = ((0, 1, 2, 3), (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0))
IDENTITY = tuple(range(6))
D = (1,) * 6


def compose(p, q):
    return tuple(p[q[i]] for i in range(6))


def apply(p, x):
    out = [0] * 6
    for i in range(6):
        out[p[i]] = x[i]
    return tuple(out)


def product(a, b):
    x, p = a
    y, q = b
    py = apply(p, y)
    return (tuple(x[i] + py[i] for i in range(6)), compose(p, q))


def cyc(star):
    p = list(range(6))
    a, b, c = star
    p[a], p[b], p[c] = b, c, a
    return tuple(p)


def perm_inv(p):
    a = [0] * 6
    for i in range(6):
        a[p[i]] = i
    return tuple(a)


def event(v, sign):
    x = tuple(sign if i in STARS[v] else 0 for i in range(6))
    p = cyc(STARS[v])
    if sign == -1:
        p = perm_inv(p)
    return x, p


def edge_perm(q):
    return tuple(EDGE_ID[tuple(sorted((q[a], q[b])))] for a, b in EDGES)


def parity(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))


def local_signs(q):
    P = edge_perm(q)
    return tuple(parity(tuple(STARS[q[v]].index(P[i]) for i in STARS[v])) for v in range(4))


def phi(state, q, eta):
    x, p = state
    P = edge_perm(q)
    Pinv = perm_inv(P)
    return tuple(eta*t for t in apply(P, x)), compose(compose(P, p), Pinv)


def evaluate(word):
    val = (0, 0, 0, 0, 0, 0), IDENTITY
    for v, sign in word:
        val = product(val, event(v, sign))
    return val


def diagonal_return(state):
    x, p = state
    if p == IDENTITY and len(set(x)) == 1:
        return x[0]
    return None


def main():
    table=[]
    for q in V4:
        signs = local_signs(q)
        assert len(set(signs)) == 1, (q, signs)
        eta = signs[0]
        P = edge_perm(q)
        for v in range(4):
            for s in (-1, 1):
                assert phi(event(v, s), q, eta) == event(q[v], eta*s)
        table.append({"vertex_permutation": list(q), "edge_permutation": list(P),
                      "local_orientation_parities": list(signs), "global_sign": eta})
    for q in V4:
        P = edge_perm(q)
        eta = local_signs(q)[0]
        for v in range(4):
            for s in (-1,1):
                a=event(v,s)
                b=event(v,-s)
                assert product(a,b) == ((0,)*6, IDENTITY)
    # Exhaustively verify the full word-level transport on 4 subsets, lengths 0..5.
    word_tests=0
    for missing in range(4):
        J=tuple(v for v in range(4) if v != missing)
        alphabet=tuple((v,s) for v in J for s in (-1,1))
        for m in range(6):
            for word in itertools.product(alphabet, repeat=m):
                outcome=evaluate(word)
                for q in V4:
                    eta=local_signs(q)[0]
                    image_word=tuple((q[v], eta*s) for v,s in word)
                    assert evaluate(image_word) == phi(outcome, q, eta)
                    word_tests += 1
    # Independent direct exact counts at small even lengths for all four 3-STAR subsets.
    counts={}
    for missing in range(4):
        J=tuple(v for v in range(4) if v != missing)
        alphabet=tuple((v,s) for v in J for s in (-1,1))
        counts[str(missing)]={}
        for m in (2,4,6):
            c=Counter()
            for word in itertools.product(alphabet,repeat=m):
                k=diagonal_return(evaluate(word))
                if k is not None: c[k]+=1
            counts[str(missing)][str(m)]=dict(sorted((str(k),v) for k,v in c.items()))
            assert counts[str(missing)][str(m)]=={'0':{2:6,4:66,6:876}[m]}
    assert len({json.dumps(c,sort_keys=True) for c in counts.values()})==1
    output={"schema":"R762GK_V4_ALL_HORIZON_EQUIVARIANCE_CHECK_V1",
            "status":"PASS", "arithmetic":"exact integers", "indexing":"vertices 0..3; edges [01,02,03,12,13,23]",
            "v4_table":table, "letter_checks":32,
            "word_length_range_tested":"0..5", "evaluated_word_automorphism_comparisons":word_tests,
            "full_diagonal_return_counts_lengths_2_4_6":counts,
            "proof_scope":"All m >= 0 and all k in Z by explicit involutive group automorphisms and inverse-word bijections; finite checks not used to extrapolate.",
            "original_input":"R762GJ@eeadd34ce522fb7b446c26400dd4a2b63d07a764; P000 pin a72226e2430ffa4786321ac86e7f0c599d5f0389",
            "review":"NOT_REVIEWED"}
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__': main()
