"""Exact V39 three-input observer checks. Run with Python 3. No dependencies."""
from collections import Counter
from itertools import permutations, product
import json
from pathlib import Path

IDENTITY = (0, 1, 2)
A = (0, 2, 1)
B = (1, 0, 2)


def after(later, earlier):
    return tuple(later[j] for j in earlier)


# R757 defines C as B^{-1} followed by A^{-1}. A and B are transpositions.
C = after(A, B)
BLOCK_FRAME = dict(A=A, B=B, C=C)
RING_EXPANSION = {"A": ["A+"], "B": ["B+"], "C": ["B-", "A-"]}
SOURCES = list(product(range(2), repeat=3))


def frame(word):
    now = IDENTITY
    for symbol in word:
        now = after(BLOCK_FRAME[symbol], now)
    return now


def ledger(word):
    return Counter(ring for symbol in word for ring in RING_EXPANSION[symbol])


WORDS = ["".join(p) for p in permutations("ABC")]
G = frame("ACB")
FRAMES = (IDENTITY, G, after(G, G))
EXPONENT = {w: FRAMES.index(frame(w)) for w in WORDS}
OPTS = list(product(WORDS, repeat=2))
BASELINE = ("ABC", "ACB")


def readout(pairs, bits):
    return sum(EXPONENT[pair[b]] for pair, b in zip(pairs, bits)) % 3


def evaluate_one(pairs):
    counts = [[0] * 3 for _ in range(2)]
    for bits in SOURCES:
        counts[sum(bits) % 2][readout(pairs, bits)] += 1
    return sum(max(column) for column in zip(*counts))


def run():
    assert tuple(EXPONENT[w] for w in WORDS) == (0, 1, 2, 0, 0, 2)
    assert len(set(FRAMES)) == 3 and after(G, FRAMES[2]) == IDENTITY
    assert all(ledger(w) == Counter({"A+": 1, "B+": 1, "B-": 1, "A-": 1}) for w in WORDS)
    histogram = Counter()
    exponents_histogram = Counter()
    for pairs in product(OPTS, repeat=3):
        score = evaluate_one(pairs)
        distinct = all(EXPONENT[w0] != EXPONENT[w1] for w0, w1 in pairs)
        assert score == (7 if distinct else 4)
        histogram[score] += 1
    for deltas in product(range(3), repeat=3):
        pairs = [(WORDS[0], ("ABC", "ACB", "BAC")[d]) for d in deltas]
        exponents_histogram[evaluate_one(pairs)] += 1
    assert histogram == {4: 36008, 7: 10648}
    assert exponents_histogram == {4: 19, 7: 8}

    one_pass, two_full, extra_replays = [], {}, 0
    for bits in SOURCES:
        words = [BASELINE[b] for b in bits]
        # Two group-valued queries on one live trace. No reset.
        q2 = frame("".join(words[:2]))
        q3 = frame("".join(words))
        i2, i3 = FRAMES.index(q2), FRAMES.index(q3)
        last_bit = (i3 - i2) % 3
        parity = sum(bits) % 2
        assert last_bit in (0, 1) and (i2 + last_bit) % 2 == parity
        assert ledger("".join(words)) == {x: 3 for x in ("A+", "A-", "B+", "B-")}
        # A full second pass independently initialized to identity, with x3 sign reversed.
        # BAC has frame g^2; every per-bit input pair has two distinct output frames.
        second_words = [words[0], words[1], ("ABC", "BAC")[bits[2]]]
        second = FRAMES.index(frame("".join(second_words)))
        assert ledger("".join(second_words)) == ledger("".join(words))
        recovered_last = (2 * (i3 - second)) % 3  # (r-r')/2 in Z/3
        assert recovered_last == bits[2]
        decoded = (((i3 - recovered_last) % 3) + recovered_last) % 2
        assert parity == decoded
        two_full.setdefault((i3, second), set()).add(parity)
        # Read final first, then re-encode just bit 1 if the final frame was identity.
        if i3 == 0:
            extra_replays += 1
            assisted = EXPONENT[words[0]]
        else:
            assisted = i3 % 2
        assert parity == assisted
        one_pass.append({"bits": "".join(map(str, bits)), "parity": parity,
                         "frame_after_two_exponent": i2, "frame_after_three_exponent": i3,
                         "independent_second_full_exponent": second})
    assert all(len(v) == 1 for v in two_full.values())
    assert extra_replays == 2

    # All fixed checkpoints up to length nine. A gap>=3 admits 000 versus 111.
    finite_check = {}
    for n in range(1, 10):
        smallest = n
        valid = 0
        for keep in product(range(2), repeat=n - 1):
            ends = [i for i, k in enumerate(keep, 1) if k] + [n]
            seen = {}
            works = True
            for bits in product(range(2), repeat=n):
                obs = tuple(sum(bits[:j]) % 3 for j in ends)
                parity = sum(bits) % 2
                if obs in seen and seen[obs] != parity:
                    works = False
                    break
                seen[obs] = parity
            gaps = [b - a for a, b in zip([0] + ends[:-1], ends)]
            assert works == (max(gaps) <= 2)
            if works:
                valid += 1
                smallest = min(smallest, len(ends))
        assert smallest == (n + 1) // 2
        finite_check[n] = {"minimum": smallest, "sufficient_checkpoint_sets": valid}
    return {
        "model": "three fair independent bits; predetermined source-separable choice of one ABC permutation per bit; last S3 V39 frame only for one-query theorem",
        "word_frame_exponents": EXPONENT, "frames_tuple": FRAMES,
        "universal_count_6_power_6": sum(histogram.values()),
        "one_observation_correct_out_of_8_histogram": dict(sorted(histogram.items())),
        "delta_classes_of_27": dict(sorted(exponents_histogram.items())),
        "one_pass_rows": one_pass,
        "separate_full_runs_distinct_signatures": len(two_full),
        "adaptive_final_then_one_bit_rereads_out_of_8": extra_replays,
        "same_ledger_each_3_block_run": {x: 3 for x in ("A+", "A-", "B+", "B-")},
        "checkpoint_bounds_finite_check": finite_check, "status": "PASS"
    }


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, ensure_ascii=False, indent=2))
