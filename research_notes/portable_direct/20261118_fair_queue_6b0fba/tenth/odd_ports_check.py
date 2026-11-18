"""Exact certificate for the p=32 fixed odd two-port observer. Python 3 + NumPy."""
import hashlib
import json
import math
from collections import Counter
import numpy as np

N = 1 << 32
LO = (1 << 18) + 1
HI = (1 << 19) - 1
THRESHOLD = 63 * N + 2
TOTAL = ((HI - LO) // 2 + 1) ** 2


def odd_multiples(g):
    # Count the odd multiples of odd g in [LO,HI].
    return (HI // g + 1) // 2 - ((LO - 1) // g + 1) // 2


def exact_gcd_counts():
    counts = {}
    for g in range(HI, 0, -2):
        both = odd_multiples(g) ** 2
        counts[g] = both - sum(counts[h] for h in range(3*g, HI+1, 2*g))
    assert sum(counts.values()) == TOTAL and min(counts.values()) == 0
    return counts


def labels(p):
    # (lower endpoint to old coordinate, lower endpoint to new coordinate)
    return [(0, 0)] + [s for i in range(p) for s in [(0, 1 << i), (1 << i, 0)]]


def fiber_weights(g, p):
    n = 1 << p
    weight = Counter()
    for old, new in labels(p):
        weight[(new - old) % g] += n - max(old, new)
    return weight


def check_small():
    # Test the implication against literal hashing of all named trajectories.
    # No circle contact calculation is used by the hashing oracle.
    tested = forced = 0
    for p in range(1, 7):
        n = 1 << p
        events = [(x, x) for x in range(n)]
        events.extend((x, x ^ (1 << i)) for x in range(n) for i in range(p))
        for a in range(3, 2*n, 2):
            for b in range(a, 2*n, 2):
                g = math.gcd(a, b)
                ell = a*b // g
                tested += 1
                if ell < n or ell < max(fiber_weights(g, p).values()):
                    observations = {(x % a, y % b) for x, y in events}
                    assert len(observations) < len(events)
                    forced += 1
    return {"unordered_tested": tested, "forced_and_brute_confirmed": forced}


def corner():
    offsets = np.array(labels(32), dtype=np.int64)
    weights = offsets.max(axis=1)
    witness_hash = hashlib.sha256()
    max_bit_counts = np.zeros(32, dtype=np.int64)
    kind_counts = Counter()
    candidates = whole_corner = first_moduli = 0
    examples = []
    # Ordered pair (a,b) is represented by a<=b. Reversing both trajectories
    # supplies the certificate for (b,a), including named flip directions.
    for a in range(((THRESHOLD + HI - 1) // HI) | 1, HI+1, 2):
        low_b = max(a, ((THRESHOLD + a - 1) // a) | 1)
        b = np.arange(low_b, HI+1, 2, dtype=np.int64)
        whole_corner += len(b)
        b = b[np.gcd(a, b) == 1]
        if not len(b):
            continue
        first_moduli += 1
        candidates += len(b)
        ell = a * b
        row = np.arange(len(b))
        alpha = a * np.fromiter((pow(a, -1, int(v)) for v in b),
                                 dtype=np.int64, count=len(b))
        centers = np.zeros((len(b), 65), dtype=np.int64)
        for i in range(32):
            centers[:, 2*i+1] = alpha
            centers[:, 2*i+2] = ((1 << i) - alpha) % ell
            alpha = (2*alpha) % ell
        order = np.argsort(centers, axis=1, kind="stable")
        sorted_centers = np.take_along_axis(centers, order, axis=1)
        gaps = np.roll(sorted_centers, -1, axis=1) - sorted_centers
        gaps[:, -1] += ell
        following = np.roll(order, -1, axis=1)
        # We need only coinciding paths from different bit names (zero allowed).
        # Every accepted witness is decoded and verified on the original ports.
        use = (gaps < N-weights[order]) & (weights[order] != weights[following])
        if not use.any(axis=1).all():
            missed = b[~use.any(axis=1)]
            raise ValueError(f"uncovered corner pair(s) with a={a}: {missed!r}")
        col = np.argmax(use, axis=1)
        left, right = order[row, col], following[row, col]
        gap = gaps[row, col]
        tr = weights[right]
        tl = weights[left]
        w = np.where((gap & tl) == 0, 0, tl)
        x, y = gap+w+offsets[left, 0], gap+w+offsets[left, 1]
        u, v = w+offsets[right, 0], w+offsets[right, 1]
        assert ((x >= 0) & (y >= 0) & (u >= 0) & (v >= 0)).all()
        assert ((x < N) & (y < N) & (u < N) & (v < N)).all()
        assert ((x ^ y) == tl).all() and ((u ^ v) == tr).all()
        assert (((x != u) | (y != v)) & ((x-u) % a == 0) & ((y-v) % b == 0)).all()
        kind_counts["zero_flip"] += int(((tl == 0) | (tr == 0)).sum())
        kind_counts["distinct_named_flips"] += int(((tl != 0) & (tr != 0)).sum())
        highest = np.searchsorted(1 << np.arange(32, dtype=np.int64), np.maximum(tl,tr))
        max_bit_counts += np.bincount(highest, minlength=32)
        # In this stream each record is (a,b,x,y,u,v), 6 little-endian int64.
        stream = np.column_stack((np.full_like(b,a), b, x, y, u, v)).astype("<i8")
        witness_hash.update(stream.tobytes(order="C"))
        if not examples:
            examples.append(stream[0].tolist())
        last = stream[-1].tolist()
    examples.append(last)
    return {
        "range_unordered_including_noncoprime": whole_corner,
        "coprime_unordered": candidates, "coprime_ordered": 2*candidates,
        "nonempty_first_modulus_rows": first_moduli, "uncovered": 0,
        "witness_kinds_unordered": dict(kind_counts),
        "max_used_bit_unordered_histogram_0_to_31": max_bit_counts.tolist(),
        "examples_a_b_x_y_u_v": examples,
        "sha256_little_endian_six_int64_witness_stream": witness_hash.hexdigest(),
    }


def main():
    gcd_count = exact_gcd_counts()
    rows = []
    for g in range(3, 64, 2):
        w = fiber_weights(g, 32)[1]
        assert g*w > HI*HI
        rows.append([g, w, g*w - HI*HI, gcd_count[g]])
    assert HI*HI < 65*N
    small = check_small()
    finite = corner()
    by_case = {
        "gcd_ge_65_nochange": sum(v for g,v in gcd_count.items() if g >= 65),
        "gcd_3_through_63_residue_one": sum(r[3] for r in rows),
        "coprime_below_threshold": gcd_count[1] - finite["coprime_ordered"],
        "coprime_corner": finite["coprime_ordered"],
    }
    assert sum(by_case.values()) == TOTAL
    assert sum(fiber_weights(1, 32).values()) == THRESHOLD
    # Independent existing upper witness: all 65 signed increments are distinct mod 67.
    a20, b20 = 536469, 536603
    g20 = math.gcd(a20, b20)
    assert len({(end-start) % g20 for start,end in labels(32)}) == 65
    assert math.lcm(a20,b20) >= N and max(a20,b20).bit_length() == 20
    print(json.dumps({
        "model": "32 named bits, directed nochange or a single named XOR, two fixed odd ports",
        "Q": [LO,HI], "N": N, "coprime_product_threshold": THRESHOLD,
        "ordered_partition": by_case, "ordered_total": TOTAL, "unresolved": 0,
        "g_weight_margin_ordered_count": rows, "small_hash_oracle": small,
        "corner": finite, "prefix907_union": 7778425088,
        "increase_vs_prefix907": TOTAL-7778425088,
        "upper_20": [a20,b20,g20,math.lcm(a20,b20)],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
