#!/usr/bin/env python3
"""Independent direct trajectory verifier for PREFIX-859.
Usage: python3 PREFIX859_R6_INDEPENDENT_CROSSCHECK.py PREFIX859_R6_TWO_READ_ODD_PARETO_RESULTS.json
It deliberately does not call the forbidden-distance graph implementation.
"""
from json import load
from sys import argv

def direct(p, q1, q2):
    N = 1 << p
    observations = {}
    for terminal in range(N):
        for predecessor in [terminal] + [terminal ^ (1 << j) for j in range(p)]:
            key = (predecessor % q1, terminal % q2)
            prior = observations.get(key)
            if prior is not None and prior != terminal:
                return False
            observations[key] = terminal
    return True

def main():
    with open(argv[1], "r", encoding="utf-8") as f:
        data = load(f)
    assert data["schema"] == "PREFIX859_ODD_PARETO_V1"
    tested = 0
    for row in data["cases"]:
        p = row["p"]
        N = 1 << p
        for record in row["pareto_witnesses"] + row["best_total_witnesses"] + row["best_peak_witnesses"]:
            bw1, bw2, q1, q2 = record
            assert q1 % 2 and q2 % 2 and 3 <= q1 < N and 3 <= q2 < N
            assert (q1 - 1).bit_length() == bw1
            assert (q2 - 1).bit_length() == bw2
            assert direct(p, q1, q2), (p, q1, q2)
            tested += 1
        if p <= 7:
            exact_count = sum(direct(p, q1, q2)
                              for q1 in range(3, N, 2)
                              for q2 in range(3, N, 2))
            assert exact_count == row["successful_pairs"], (p, exact_count)
            tested += ((N - 2) // 2) ** 2
    # Arithmetic-orbit independent modulo-21 residue check.
    A = {0, 1, 2, 4, 8, 11, 16}
    AA = {(x + y) % 21 for x in A for y in A}
    assert set(range(21)) - AA == {7, 14}
    for p in (9, 15, 21, 27):
        assert (pow(2, p, 21) - 1) % 21 == 7
    print("INDEPENDENT_DIRECT_CROSSCHECK_PASS", tested)

if __name__ == "__main__":
    main()
