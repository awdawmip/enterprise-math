#!/usr/bin/env python3
"""Exact finite audit for R284EL's explicit four-label temporal memory code.

No floating point, no external packages. The sharp lower bound is proved
algebraically in the accompanying mathematical note.
"""
from itertools import combinations
import json


def encode(a: int, b: int, k: int) -> int:
    # Blocks: (k+1) copies of a, (k+1) copies of b, k copies of (a XOR b).
    bits = [a] * (k + 1) + [b] * (k + 1) + [a ^ b] * k
    return sum(bit << pos for pos, bit in enumerate(bits))


def audit(k: int) -> dict:
    n = 3 * k + 2
    codewords = [encode(a, b, k) for b in (0, 1) for a in (0, 1)]
    distances = [(codewords[i] ^ codewords[j]).bit_count()
                 for i in range(4) for j in range(i + 1, 4)]
    assert min(distances) == 2 * k + 1
    assert n == (3 * (2 * k + 1) + 1) // 2
    seen: dict[int, int] = {}
    tested = 0
    for label, codeword in enumerate(codewords):
        for t in range(k + 1):
            for positions in combinations(range(n), t):
                mask = sum(1 << p for p in positions)
                received = codeword ^ mask
                previous = seen.setdefault(received, label)
                assert previous == label, (k, label, previous, received)
                tested += 1
    return {
        "fault_budget": k,
        "minimum_storage_bits": n,
        "codewords_msb_first": [format(x, f"0{n}b") for x in codewords],
        "pairwise_hamming_distances": distances,
        "minimum_distance": min(distances),
        "tested_received_words_counting_error_patterns": tested,
        "distinct_receivable_words": len(seen),
        "no_cross_label_collision": True,
    }


def main() -> None:
    results = [audit(k) for k in range(6)]
    print(json.dumps({
        "schema": "R284EL_SHARP_TEMPORAL_TAG_MEMORY_CERTIFICATE_V1",
        "scope": "4 logical labels, up to k adversarial Hamming flips between perfect refreshes",
        "conditional_port_evidence": "R284EK four-label confusion graph K4 at numeric E=8656; R284EJ same-tag min L_infinity distance 17313",
        "cases": results,
        "proof_obligation_not_dispatched_to_computation": "For any 4 binary words of length n and distance at least 2k+1, sum of six distances >=6(2k+1); each coordinate contributes <=4, hence n>=ceil(3(2k+1)/2)=3k+2. The explicit 3-block code achieves this."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
