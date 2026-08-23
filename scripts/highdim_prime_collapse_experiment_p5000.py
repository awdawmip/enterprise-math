#!/usr/bin/env python3
"""High-dimensional prime-collapse experiment, quadratic carrier.

Research status: computational exploration / audit, not canonical foundation.

The native experimental carrier is N_0^d with readout
    kappa(x) = sum_i x_i^2.

For each n, A_s(n) counts ordered strictly-positive s-tuples with square-sum n.
The d-dimensional nonnegative shell count is
    C_d(n) = sum_s binom(d,s) A_s(n).

This script builds A_s and C_d for d<=19, checks the exact binomial/Newton
structure, scans prime support continuity, and tests two exact dimension-wall
filters discovered in the experiment.

Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def sieve(nmax: int) -> list[bool]:
    prime = [True] * (nmax + 1)
    if nmax >= 0:
        prime[0] = False
    if nmax >= 1:
        prime[1] = False
    q = 2
    while q * q <= nmax:
        if prime[q]:
            for m in range(q * q, nmax + 1, q):
                prime[m] = False
        q += 1
    return prime


def support_spectrum(nmax: int, dmax: int) -> list[list[int]]:
    """A[s][n] = ordered positive s-tuples whose squares sum to n."""
    squares = [a * a for a in range(1, math.isqrt(nmax) + 1)]
    A = [[0] * (nmax + 1) for _ in range(dmax + 1)]
    A[0][0] = 1
    for s in range(1, dmax + 1):
        prev = A[s - 1]
        cur = A[s]
        for q in squares:
            for n in range(q, nmax + 1):
                v = prev[n - q]
                if v:
                    cur[n] += v
    return A


def shell_count(A: list[list[int]], d: int, n: int) -> int:
    return sum(math.comb(d, s) * A[s][n] for s in range(1, d + 1))


def signed_completion(A: list[list[int]], d: int, n: int) -> int:
    """Classical audit multiplicity: each nonzero coordinate gets two signs."""
    return sum((2**s) * math.comb(d, s) * A[s][n] for s in range(1, d + 1))


def two_square_pair(p: int):
    for a in range(1, math.isqrt(p) + 1):
        b2 = p - a * a
        if b2 <= 0:
            continue
        b = math.isqrt(b2)
        if b > 0 and b * b == b2:
            return a, b
    return None


def contiguous_supports(A: list[list[int]], n: int, dmax: int):
    support = [s for s in range(1, dmax + 1) if A[s][n] > 0]
    if not support:
        return False, []
    return support == list(range(support[0], support[-1] + 1)), support


def run(nmax: int, dmax: int, out: Path) -> None:
    if dmax < 19:
        raise ValueError("this experiment requires dmax >= 19")
    out.mkdir(parents=True, exist_ok=True)

    is_prime = sieve(nmax)
    primes = [n for n in range(2, nmax + 1) if is_prime[n]]
    A = support_spectrum(nmax, dmax)

    # Cache C_d(n) for all dimensions needed by the filters.
    C = [[0] * (nmax + 1) for _ in range(dmax + 1)]
    for d in range(1, dmax + 1):
        for n in range(1, nmax + 1):
            C[d][n] = shell_count(A, d, n)

    # Exact binomial/Newton reconstruction check.
    for n in range(1, nmax + 1):
        values = [C[d][n] for d in range(dmax + 1)]
        for s in range(1, dmax + 1):
            diff = values[:]
            for _ in range(s):
                diff = [diff[i + 1] - diff[i] for i in range(len(diff) - 1)]
            if diff[0] != A[s][n]:
                raise AssertionError(("newton", n, s, diff[0], A[s][n]))

    # Prime birth registry and support continuity.
    birth_hist: dict[int, int] = {}
    support_gap_primes = []
    for p in primes:
        support = [s for s in range(1, dmax + 1) if A[s][p] > 0]
        birth = support[0]
        birth_hist[birth] = birth_hist.get(birth, 0) + 1
        contiguous, _ = contiguous_supports(A, p, dmax)
        if not contiguous:
            support_gap_primes.append(p)

    # Dimension-4 and dimension-8 exact prime walls on odd integers.
    wall4_mismatch = []
    wall8_mismatch = []
    for n in range(3, nmax + 1, 2):
        q4 = 2 * C[4][n] - 4 * C[3][n] + 3 * C[2][n]
        q8 = (
            16 * C[8][n]
            - 64 * C[7][n]
            + 112 * C[6][n]
            - 112 * C[5][n]
            + 70 * C[4][n]
            - 28 * C[3][n]
            + 7 * C[2][n]
        )
        if (q4 == n + 1) != is_prime[n]:
            wall4_mismatch.append((n, q4, is_prime[n]))
        if (q8 == n**3 + 1) != is_prime[n]:
            wall8_mismatch.append((n, q8, is_prime[n]))

    # 10D angular echo: for p == 3 mod 4 the signed shell is rigid;
    # for p == 1 mod 4 the residual recovers the unique two-square pair.
    angular_failures = []
    angular_recovered = 0
    rigid10_count = 0
    for p in primes:
        if p == 2:
            continue
        r10 = signed_completion(A, 10, p)
        if p % 4 == 3:
            rigid10_count += 1
            if r10 != 12 * (p**4 - 1):
                angular_failures.append((p, "rigid", r10))
        else:
            pair = two_square_pair(p)
            if pair is None:
                angular_failures.append((p, "missing_pair", r10))
                continue
            a, b = pair
            h4 = a**4 - 6 * a * a * b * b + b**4
            if 5 * r10 != 68 * (1 + p**4) + 64 * h4:
                angular_failures.append((p, "h4_identity", r10))
                continue
            u = (p * p - h4) // 8
            disc = p * p - 4 * u
            root = math.isqrt(disc)
            if root * root != disc:
                angular_failures.append((p, "disc", disc))
                continue
            aa = (p - root) // 2
            bb = (p + root) // 2
            if {aa, bb} != {a * a, b * b}:
                angular_failures.append((p, "recover", aa, bb, a, b))
                continue
            angular_recovered += 1

    if wall4_mismatch or wall8_mismatch or angular_failures:
        raise AssertionError(
            {
                "wall4": wall4_mismatch[:5],
                "wall8": wall8_mismatch[:5],
                "angular": angular_failures[:5],
            }
        )

    fields = [
        "prime", "p_mod8", "birth_dimension", "support_contiguous_to_d19",
        "C2", "C3", "C4", "C5", "C6", "C7", "C8",
        "wall4_value", "wall8_value", "R10", "two_square_a", "two_square_b",
        "H4_angular_echo",
    ]
    rows = []
    for p in primes:
        support = [s for s in range(1, dmax + 1) if A[s][p] > 0]
        pair = two_square_pair(p) if p != 2 and p % 4 == 1 else None
        h4 = None
        if pair:
            a, b = pair
            h4 = a**4 - 6 * a * a * b * b + b**4
        rows.append({
            "prime": p,
            "p_mod8": p % 8,
            "birth_dimension": support[0],
            "support_contiguous_to_d19": int(support == list(range(support[0], support[-1] + 1))),
            "C2": C[2][p], "C3": C[3][p], "C4": C[4][p],
            "C5": C[5][p], "C6": C[6][p], "C7": C[7][p], "C8": C[8][p],
            "wall4_value": 2 * C[4][p] - 4 * C[3][p] + 3 * C[2][p],
            "wall8_value": (
                16 * C[8][p] - 64 * C[7][p] + 112 * C[6][p]
                - 112 * C[5][p] + 70 * C[4][p] - 28 * C[3][p] + 7 * C[2][p]
            ),
            "R10": signed_completion(A, 10, p),
            "two_square_a": pair[0] if pair else "",
            "two_square_b": pair[1] if pair else "",
            "H4_angular_echo": h4 if h4 is not None else "",
        })

    csv_path = out / f"quadratic_prime_fingerprints_p{nmax}.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"NMAX={nmax}")
    print(f"PRIME_COUNT={len(primes)}")
    print(f"BIRTH_HISTOGRAM={dict(sorted(birth_hist.items()))}")
    print(f"SUPPORT_GAP_PRIMES={support_gap_primes}")
    print(f"WALL4_MISMATCHES={len(wall4_mismatch)}")
    print(f"WALL8_MISMATCHES={len(wall8_mismatch)}")
    print(f"R10_RIGID_P_3MOD4={rigid10_count}")
    print(f"R10_ANGULAR_RECOVERED_P_1MOD4={angular_recovered}")
    print(f"CSV={csv_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=5000)
    parser.add_argument("--d-max", type=int, default=19)
    parser.add_argument("--out", type=Path, default=Path("highdim_prime_experiment_out"))
    args = parser.parse_args()
    run(args.max_n, args.d_max, args.out)
