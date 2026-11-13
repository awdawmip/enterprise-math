#!/usr/bin/env python3
"""Exact R758P3 exhaustive verifier. Candidate S3 connection; not native V39 admission."""
import itertools
import json
from collections import Counter, defaultdict

E = (0, 1, 2)
S = (1, 0, 2)
R = (1, 2, 0)
T = ((1, 0, 2), (0, 2, 1), (2, 1, 0))
R2 = (2, 0, 1)
FRAMES = {E: "e", R: "r", R2: "r2"}


def mul(p, q):
    return tuple(p[q[i]] for i in range(3))


def frame(word):
    out = E
    for axis in word:
        out = mul(T[axis], out)
    return out


def qword(word):
    return sum((1 if i % 2 == 0 else -1) * a for i, a in enumerate(word)) % 3


def predicted(word):
    rpower = (E, R, R2)[qword(word)]
    return mul(S, rpower) if len(word) % 2 else rpower


def signed_area(word):
    pos, areas = [0, 0, 0], [0, 0, 0]
    for axis, sign in word:
        if axis == 1:
            areas[0] += pos[0] * sign
        elif axis == 2:
            areas[1] += pos[0] * sign
            areas[2] += pos[1] * sign
        pos[axis] += sign
    assert pos == [0, 0, 0]
    return tuple(areas)


def repair_q(word, areas):
    edges = ((0, 1), (0, 2), (1, 2))
    degree = [0, 0, 0]
    for v, (a, b) in zip(areas, edges):
        if v:
            degree[a] += 1
            degree[b] += 1
    nonzero = sum(v != 0 for v in areas)
    if nonzero in (0, 3):
        return 0, None
    assert nonzero in (1, 2)
    a, c = [i for i, deg in enumerate(degree) if deg % 2]
    axis_word = [axis for axis, _ in word]
    positions = [i for i, v in enumerate(axis_word) if v == a]
    assert len(positions) == 2 and positions[0] % 2 == positions[1] % 2
    beta = int(positions[0] % 2 == 0)
    return (2 * (a - c) if beta else 2 * (c - a)) % 3, beta


def main():
    assert mul(S, R) == T[1] and mul(S, R2) == T[2]
    words = itertools.permutations([(axis, sign) for axis in range(3) for sign in (+1, -1)])
    fibers = defaultdict(Counter)
    nnz_counter = Counter()
    checked = 0
    repaired = 0
    for w in words:
        checked += 1
        a = signed_area(w)
        labels = [axis for axis, _ in w]
        h = frame(labels)
        assert h == predicted(labels)
        q, beta = repair_q(w, a)
        assert h == (E, R, R2)[q]
        if beta is not None:
            repaired += 1
        fibers[a][FRAMES[h]] += 1
        nnz_counter[sum(x != 0 for x in a)] += 1
    assert checked == 720
    assert len(fibers) == 27
    expected = {
        0: (1, 240, {"e": 240}),
        1: (6, 48, {"r": 24, "r2": 24}),
        2: (12, 12, {"r": 6, "r2": 6}),
        3: (8, 6, {"e": 6}),
    }
    by_nnz = {}
    for n, (nvec, fiber_size, fiber_frame) in expected.items():
        matching = [counts for area, counts in fibers.items() if sum(v != 0 for v in area) == n]
        assert len(matching) == nvec
        assert all(sum(ct.values()) == fiber_size and ct == fiber_frame for ct in matching)
        assert nnz_counter[n] == nvec * fiber_size
        by_nnz[str(n)] = {
            "signed_vectors": nvec,
            "words_per_vector": fiber_size,
            "frame_per_vector": fiber_frame,
            "total_words": nnz_counter[n],
        }
    assert repaired == 432

    all_prefixes = 0
    all_splits = 0
    for length in range(7):
        for labels in itertools.product(range(3), repeat=length):
            all_prefixes += 1
            assert predicted(labels) == frame(labels)
            for j in range(len(labels) + 1):
                u, v = labels[:j], labels[j:]
                q_comp = (qword(u) + ((-1) ** len(u)) * qword(v)) % 3
                assert q_comp == qword(labels)
                all_splits += 1
    assert all_prefixes == 1093

    evidence = {
        "schema": "R758P3_EXACT_FULL_AREA_FRAME_V1",
        "validation": "PASS",
        "model": "three selected X6 axes; all 720 words of six signed steps; candidate S3 axis-link transport",
        "frozen_science_commit": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "signed_words_checked": checked,
        "signed_area_vectors": len(fibers),
        "by_area_nonzero_count": by_nnz,
        "frame_distribution": {
            h: sum(f[h] for f in fibers.values()) for h in ("e", "r", "r2")
        },
        "words_requiring_binary_repair": repaired,
        "uniform_conditional_entropy_bits": "3/5",
        "all_axis_words_length_0_to_6_checked": all_prefixes,
        "split_compositions_checked": all_splits,
        "native_triadic_admission": "PENDING",
    }
    assert evidence["frame_distribution"] == {"e": 288, "r": 216, "r2": 216}
    print(json.dumps(evidence, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
