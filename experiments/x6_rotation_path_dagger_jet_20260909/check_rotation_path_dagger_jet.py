#!/usr/bin/env python3
"""Exact checks for concrete rotation-path dagger typing and branch path jets."""
from collections import Counter
from itertools import combinations, product

ZERO = (0, 0, 0)
ORBIT = [
    (1, 0, 0),
    (0, -1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, 1, 0),
    (0, 0, -1),
]


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def edge_steps(a, b, outer):
    mid = add(a, b) if outer else ZERO
    return (sub(mid, a), sub(b, mid))


def path_steps(bits):
    out = []
    for r, bit in enumerate(bits):
        out.extend(edge_steps(ORBIT[r], ORBIT[(r + 1) % 6], bit))
    return tuple(out)


def reverse_steps(steps):
    return tuple(neg(s) for s in reversed(steps))


def step_letter(step):
    nz = [i for i, x in enumerate(step) if x]
    assert len(nz) == 1 and abs(step[nz[0]]) == 1
    i = nz[0]
    return i, step[i]


def jet(steps, k):
    if k == 0:
        return {(): 1}
    out = Counter()
    for inds in combinations(range(len(steps)), k):
        word = []
        coeff = 1
        for r in inds:
            i, sign = step_letter(steps[r])
            word.append(i)
            coeff *= sign
        out[tuple(word)] += coeff
    return {w: c for w, c in sorted(out.items()) if c}


def trunc_signature(steps, k):
    return tuple((d, tuple(jet(steps, d).items())) for d in range(1, k + 1))


def chen_rhs(gamma, delta, n):
    out = Counter()
    for p in range(n + 1):
        q = n - p
        for wl, cl in jet(gamma, p).items():
            for wr, cr in jet(delta, q).items():
                out[wl + wr] += cl * cr
    return {w: c for w, c in sorted(out.items()) if c}


def paircounts(bits):
    return tuple(bits[r] + bits[r + 3] for r in range(3))


def main():
    # Literal concrete-path concatenation keeps backtracking history.
    # Therefore reversal is a dagger/involution, not a categorical inverse.
    gamma = edge_steps(ORBIT[0], ORBIT[1], True)
    dagger = reverse_steps(gamma)
    loop = gamma + dagger
    assert len(gamma) == 2 and len(loop) == 4
    assert loop != ()
    displacement = ZERO
    for s in loop:
        displacement = add(displacement, s)
    assert displacement == ZERO

    # Exact finite Chen-type concatenation law through degree 3.
    all_words = list(product((0, 1), repeat=6))
    for bits in all_words:
        steps = path_steps(bits)
        gamma = steps[:6]
        delta = steps[6:]
        for n in range(4):
            assert jet(gamma + delta, n) == chen_rhs(gamma, delta, n)

    counts = {}
    sig2_to_pairs = {}
    for k in (1, 2, 3):
        sigs = set()
        for bits in all_words:
            steps = path_steps(bits)
            sig = trunc_signature(steps, k)
            sigs.add(sig)
            if k == 2:
                pc = paircounts(bits)
                old = sig2_to_pairs.setdefault(sig, pc)
                assert old == pc
        counts[k] = len(sigs)

    assert counts == {1: 1, 2: 27, 3: 64}
    assert len(set(sig2_to_pairs.values())) == 27

    # Degree 3 is the first lossless truncation among degrees 1,2,3
    # on the 64 concatenated-shortest branch words of one Q_S frame cycle.
    inverse = {}
    for bits in all_words:
        sig = trunc_signature(path_steps(bits), 3)
        assert sig not in inverse
        inverse[sig] = bits

    print("PASS_X6_ROTATION_PATH_DAGGER_BRANCH_JET")
    print("literal_path_reversal_is_dagger_not_inverse", True)
    print("jet_class_counts", counts)
    print("degree2_classes_equal_antipodal_paircounts", True)
    print("degree3_lossless_on_64_shortest_cycle_words", True)


if __name__ == "__main__":
    main()
