#!/usr/bin/env python3
from itertools import combinations, product
from math import gcd
import json
import platform
import sys

SCHEMA = "N_COUPLED_EXPLICIT_PRESENTATION_SCALARIZATION_CHECK_V1"

def det_bareiss(M):
    n = len(M)
    if n == 0:
        return 1
    if n == 1:
        return int(M[0][0])
    A = [list(map(int, row)) for row in M]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot_row = None
            for i in range(k + 1, n):
                if A[i][k] != 0:
                    pivot_row = i
                    break
            if pivot_row is None:
                return 0
            A[k], A[pivot_row] = A[pivot_row], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
    return sign * A[n - 1][n - 1]

def determinantal_divisor(M, k):
    m = len(M)
    n = len(M[0]) if m else 0
    if k == 0:
        return 1
    if k > min(m, n):
        return 0
    g = 0
    for rows in combinations(range(m), k):
        for cols in combinations(range(n), k):
            sub = [[M[i][j] for j in cols] for i in rows]
            g = gcd(g, abs(det_bareiss(sub)))
            if g == 1:
                return 1
    return g

def rank_mod_prime(M, p):
    A = [[int(x) % p for x in row] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    row = 0
    for col in range(n):
        pivot = None
        for i in range(row, m):
            if A[i][col] % p:
                pivot = i
                break
        if pivot is None:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        inv = pow(A[row][col], -1, p)
        A[row] = [(x * inv) % p for x in A[row]]
        for i in range(m):
            if i != row and A[i][col] % p:
                factor = A[i][col] % p
                A[i] = [(A[i][j] - factor * A[row][j]) % p for j in range(n)]
        row += 1
        if row == m:
            break
    return row

def support_signature(M, N):
    out = []
    for k in range(1, min(len(M), len(M[0])) + 1):
        d = determinantal_divisor(M, k)
        out.append({"k": k, "D_k": d, "sigma_k": gcd(N, d)})
    return out

def main():
    primes = [3, 5, 7, 11]
    semiprimes = [(p, q, p * q) for p, q in combinations(primes, 2)]
    dims = [(1,1), (1,2), (2,1), (2,2), (2,3), (3,2), (3,3)]
    alphabet = (-1, 0, 1)

    counts = {
        "matrices": 0,
        "semiprime_matrix_cases": 0,
        "k_checks": 0,
        "rank_asymmetric_cases": 0,
        "proper_sigma_cases": 0,
        "balanced_cases": 0,
        "equivalence_failures": 0,
        "rank_criterion_failures": 0,
    }

    for m, n in dims:
        for vals in product(alphabet, repeat=m*n):
            M = [list(vals[i*n:(i+1)*n]) for i in range(m)]
            counts["matrices"] += 1
            divisors = [determinantal_divisor(M, k) for k in range(1, min(m,n)+1)]
            for p, q, N in semiprimes:
                counts["semiprime_matrix_cases"] += 1
                rp = rank_mod_prime(M, p)
                rq = rank_mod_prime(M, q)
                if rp == rq:
                    counts["balanced_cases"] += 1
                else:
                    counts["rank_asymmetric_cases"] += 1

                proper = False
                for k, d in enumerate(divisors, start=1):
                    counts["k_checks"] += 1
                    if ((d % p == 0) != (rp < k)):
                        counts["rank_criterion_failures"] += 1
                    if ((d % q == 0) != (rq < k)):
                        counts["rank_criterion_failures"] += 1
                    sigma = gcd(N, d)
                    if sigma not in (1, N):
                        proper = True

                if proper:
                    counts["proper_sigma_cases"] += 1
                if proper != (rp != rq):
                    counts["equivalence_failures"] += 1

    # Non-vacuity witness: a fixed, factor-blind, non-invertible projection
    # changes full-carrier determinantal support from clean to one-sided, but
    # the new support is immediately scalarized by D_2.
    N = 15
    p, q = 3, 5
    B0 = [[1,1,0],[1,4,1],[0,2,1]]
    A = [[1,1],[1,4]]  # fixed top-left row/column restriction
    witness = {
        "N": N,
        "p": p,
        "q": q,
        "seed": B0,
        "projected": A,
        "seed_rank_p": rank_mod_prime(B0, p),
        "seed_rank_q": rank_mod_prime(B0, q),
        "projected_rank_p": rank_mod_prime(A, p),
        "projected_rank_q": rank_mod_prime(A, q),
        "seed_support": support_signature(B0, N),
        "projected_support": support_signature(A, N),
        "coordinate_gcds": [gcd(N, abs(x)) for row in B0 for x in row] +
                           [gcd(N, abs(x)) for row in A for x in row],
    }

    expected_witness = (
        witness["seed_rank_p"] == 3 and
        witness["seed_rank_q"] == 3 and
        witness["projected_rank_p"] == 1 and
        witness["projected_rank_q"] == 2 and
        [x["D_k"] for x in witness["seed_support"]] == [1,1,1] and
        [x["D_k"] for x in witness["projected_support"]] == [1,3] and
        witness["projected_support"][1]["sigma_k"] == 3 and
        all(g in (1, N) for g in witness["coordinate_gcds"])
    )

    if counts["rank_criterion_failures"] != 0:
        raise AssertionError(counts)
    if counts["equivalence_failures"] != 0:
        raise AssertionError(counts)
    if counts["rank_asymmetric_cases"] != counts["proper_sigma_cases"]:
        raise AssertionError(counts)
    if not expected_witness:
        raise AssertionError(witness)

    certificate = {
        "schema": SCHEMA,
        "checker_execution": "PASS",
        "python": platform.python_version(),
        "prime_set": primes,
        "semiprimes": len(semiprimes),
        "dimensions": [list(x) for x in dims],
        "entry_alphabet": list(alphabet),
        **counts,
        "projection_witness": witness,
        "symbolic_laws_guarded": [
            "For every prime r, r divides D_k(A) iff rank_F_r(A mod r) < k.",
            "For N=pq with distinct primes, rank_F_p(A) != rank_F_q(A) iff some sigma_k(A)=gcd(N,D_k(A)) is a proper divisor of N.",
            "A balanced explicit presentation has only clean support scalars sigma_k in {1,N}; the first one-sided rank-support event creates a proper scalar gcd at the same explicit state.",
            "Arbitrary non-automorphic control/history does not evade this post-state scalarization when the resulting finite presentation matrix is explicit."
        ],
        "proof_role": "FINITE_REGRESSION_ONLY_NOT_GENERAL_PROOF"
    }
    print("PASS " + json.dumps(certificate, sort_keys=True, separators=(",", ":")))

if __name__ == "__main__":
    main()
