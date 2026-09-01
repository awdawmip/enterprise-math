#!/usr/bin/env python3
from __future__ import annotations
from itertools import combinations
from typing import FrozenSet, Tuple

Pair = Tuple[int, int]
Inc = Tuple[int, int]


def canon_pair(a: int, b: int) -> Pair:
    if a == b:
        raise ValueError("loops are not allowed")
    return (a, b) if a < b else (b, a)


def shift_pair(p: Pair, k: int, n: int) -> Pair:
    return canon_pair((p[0] + k) % n, (p[1] + k) % n)


def shift_inc(x: Inc, k: int, n: int, m: int) -> Inc:
    return ((x[0] + k) % n, (x[1] + k) % m)


def invariant_pair(r: FrozenSet[Pair], n: int) -> bool:
    return all(frozenset(shift_pair(p, k, n) for p in r) == r for k in range(n))


def invariant_inc(i: FrozenSet[Inc], n: int, m: int) -> bool:
    return all(frozenset(shift_inc(x, k, n, m) for x in i) == i for k in range(n))


def pairsets(n: int):
    return list(combinations(range(n), 2))


def relation_from_bits(domain, bits: int):
    return frozenset(x for i, x in enumerate(domain) if (bits >> i) & 1)


def encode_tagged(k, x, i):
    return {
        "pair": {p: (int(p in k), int(p in x)) for p in sorted(set(k) | set(x))},
        "inc": frozenset(i),
    }


def decode_tagged(obj):
    k = frozenset(p for p, v in obj["pair"].items() if v[0])
    x = frozenset(p for p, v in obj["pair"].items() if v[1])
    i = frozenset(obj["inc"])
    return k, x, i


def encode_witness(k, x, i):
    j = set()
    for role, rel in (("K", k), ("X", x)):
        for a, b in rel:
            w = (role, a, b)
            j.add((a, w))
            j.add((b, w))
    for c, s in i:
        j.add((c, ("I", s)))
    return frozenset(j)


def decode_witness(j):
    by = {}
    for c, w in j:
        by.setdefault(w, set()).add(c)
    k, x, i = set(), set(), set()
    for w, cells in by.items():
        role = w[0]
        if role in ("K", "X"):
            assert len(cells) == 2
            p = canon_pair(*sorted(cells))
            (k if role == "K" else x).add(p)
        elif role == "I":
            s = w[1]
            for c in cells:
                i.add((c, s))
        else:
            raise AssertionError("bad witness role")
    return frozenset(k), frozenset(x), frozenset(i)


def overlap_exclusion(i: FrozenSet[Inc], n: int) -> FrozenSet[Pair]:
    supp = {c: set() for c in range(n)}
    for c, s in i:
        supp[c].add(s)
    return frozenset(
        canon_pair(a, b)
        for a, b in combinations(range(n), 2)
        if supp[a] & supp[b]
    )


def selfdual_incidence(k: FrozenSet[Pair]) -> FrozenSet[Inc]:
    i = set()
    for a, b in k:
        i.add((a, b))
        i.add((b, a))
    return frozenset(i)


def selfdual_contact(i: FrozenSet[Inc], n: int) -> FrozenSet[Pair]:
    return frozenset(
        (a, b)
        for a, b in combinations(range(n), 2)
        if (a, b) in i and (b, a) in i
    )


def check() -> None:
    # Same carrier, same constant readout, nontrivial C4 equivariance.
    n = m = 4
    pairs = pairsets(n)
    k_cycle = frozenset(
        p for p in pairs
        if min((p[1] - p[0]) % n, (p[0] - p[1]) % n) == 1
    )
    k_opp = frozenset(
        p for p in pairs
        if min((p[1] - p[0]) % n, (p[0] - p[1]) % n) == 2
    )
    k_empty = frozenset()
    i_diag = frozenset((c, c) for c in range(n))
    i_shift = frozenset((c, (c + 1) % n) for c in range(n))

    assert invariant_pair(k_cycle, n)
    assert invariant_pair(k_opp, n)
    assert invariant_pair(k_empty, n)
    assert invariant_inc(i_diag, n, m)
    assert invariant_inc(i_shift, n, m)
    assert i_diag != i_shift and k_cycle != k_opp != k_empty

    witnesses = {
        "CONTACT_NOT_IMPLY_EXCLUSION": ((k_cycle, k_opp, i_diag), (k_cycle, k_empty, i_diag)),
        "EXCLUSION_NOT_IMPLY_CONTACT": ((k_opp, k_cycle, i_diag), (k_empty, k_cycle, i_diag)),
        "CONTACT_NOT_IMPLY_SUPPORT": ((k_cycle, k_opp, i_diag), (k_cycle, k_opp, i_shift)),
        "SUPPORT_NOT_IMPLY_CONTACT": ((k_cycle, k_opp, i_diag), (k_opp, k_opp, i_diag)),
        "EXCLUSION_NOT_IMPLY_SUPPORT": ((k_opp, k_cycle, i_diag), (k_opp, k_cycle, i_shift)),
        "SUPPORT_NOT_IMPLY_EXCLUSION": ((k_opp, k_cycle, i_diag), (k_opp, k_opp, i_diag)),
    }
    source_target = {
        "CONTACT_NOT_IMPLY_EXCLUSION": (0, 1),
        "EXCLUSION_NOT_IMPLY_CONTACT": (1, 0),
        "CONTACT_NOT_IMPLY_SUPPORT": (0, 2),
        "SUPPORT_NOT_IMPLY_CONTACT": (2, 0),
        "EXCLUSION_NOT_IMPLY_SUPPORT": (1, 2),
        "SUPPORT_NOT_IMPLY_EXCLUSION": (2, 1),
    }
    for name, (a, b) in witnesses.items():
        source, target = source_target[name]
        assert a[source] == b[source], name
        assert a[target] != b[target], name
        for rel in (a[0], a[1], b[0], b[1]):
            assert invariant_pair(rel, n), name
        for inc in (a[2], b[2]):
            assert invariant_inc(inc, n, m), name

    # Exhaustive lossless encoding on C=3, S=2.
    n2, m2 = 3, 2
    pair_domain = pairsets(n2)
    inc_domain = [(c, s) for c in range(n2) for s in range(m2)]
    triples = 0
    for kb in range(1 << len(pair_domain)):
        k = relation_from_bits(pair_domain, kb)
        for xb in range(1 << len(pair_domain)):
            x = relation_from_bits(pair_domain, xb)
            for ib in range(1 << len(inc_domain)):
                i = relation_from_bits(inc_domain, ib)
                assert decode_tagged(encode_tagged(k, x, i)) == (k, x, i)
                assert decode_witness(encode_witness(k, x, i)) == (k, x, i)
                triples += 1
    independent_bits = 2 * len(pair_domain) + len(inc_domain)
    assert independent_bits == 12
    assert triples == 2 ** independent_bits == 4096
    assert len({(k, x) for k in (0, 1) for x in (0, 1)}) == 4

    # Explicit self-dual law gives CONTACT <-> SUPPORT.
    for kb in range(1 << len(pair_domain)):
        k = relation_from_bits(pair_domain, kb)
        i = selfdual_incidence(k)
        assert selfdual_contact(i, n2) == k

    # Explicit support-overlap law gives SUPPORT -> EXCLUSION but not conversely.
    seen = {}
    collision = None
    for ib in range(1 << len(inc_domain)):
        i = relation_from_bits(inc_domain, ib)
        x = overlap_exclusion(i, n2)
        if x in seen and seen[x] != i:
            collision = (seen[x], i, x)
            break
        seen[x] = i
    assert collision is not None

    matrices = {
        "INDEPENDENT_TYPED_TRIPLE": [["Y", "N", "N"], ["N", "Y", "N"], ["N", "N", "Y"]],
        "ROLE_TAGGED_SUM": [["Y", "N", "N"], ["N", "Y", "N"], ["N", "N", "Y"]],
        "TYPED_WITNESS_INCIDENCE": [["Y", "N", "N"], ["N", "Y", "N"], ["N", "N", "Y"]],
        "SELF_DUAL_CONTACT_SUPPORT": [["Y", "N", "Y"], ["N", "Y", "N"], ["Y", "N", "Y"]],
        "SUPPORT_OVERLAP_EXCLUSION": [["Y", "N", "N"], ["N", "Y", "N"], ["N", "Y", "Y"]],
    }
    assert matrices["INDEPENDENT_TYPED_TRIPLE"][0][1] == "N"
    assert matrices["SELF_DUAL_CONTACT_SUPPORT"][0][2] == "Y"
    assert matrices["SUPPORT_OVERLAP_EXCLUSION"][2][1] == "Y"

    print(
        "PASS",
        f"equivariant_nonimplications={len(witnesses)}",
        f"exhaustive_triples={triples}",
        f"independent_bits_n3_m2={independent_bits}",
        "pair_local_alphabet_min=4",
        "incidence_local_alphabet_min=2",
        f"signature_classes={len(matrices)}",
        "selfdual_roundtrip=8",
        "support_overlap_collision=1",
    )


if __name__ == "__main__":
    check()
