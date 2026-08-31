import itertools
import json
import math
import platform
from fractions import Fraction

PRIMES = [3, 5, 7, 11]
DIMS = [(1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(3,3)]
ALPHABET = [-1,0,1]


def det_bareiss(M):
    n = len(M)
    if n == 0:
        return 1
    A = [list(map(int, row)) for row in M]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if swap is None:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
        for j in range(k + 1, n):
            A[k][j] = 0
    return sign * A[n - 1][n - 1]


def minors(A, k):
    m = len(A)
    n = len(A[0]) if m else 0
    for rs in itertools.combinations(range(m), k):
        for cs in itertools.combinations(range(n), k):
            yield det_bareiss([[A[i][j] for j in cs] for i in rs])


def Dk(A, k):
    g = 0
    for d in minors(A, k):
        g = math.gcd(g, abs(d))
    return g


def rank_mod(A, p):
    M = [[x % p for x in row] for row in A]
    m = len(M)
    n = len(M[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if M[i][c] % p), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        inv = pow(M[r][c], -1, p)
        M[r] = [(v * inv) % p for v in M[r]]
        for i in range(m):
            if i != r and M[i][c] % p:
                a = M[i][c] % p
                M[i] = [(M[i][j] - a * M[r][j]) % p for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def support_profile(A, N):
    upto = min(len(A), len(A[0]) if A else 0)
    out = []
    for k in range(1, upto + 1):
        d = Dk(A, k)
        out.append({"k": k, "D_k": d, "sigma_k": math.gcd(N, d)})
    return out


def all_matrices(m, n):
    for flat in itertools.product(ALPHABET, repeat=m*n):
        yield [list(flat[i*n:(i+1)*n]) for i in range(m)]


def main():
    rank_criterion_failures = 0
    equivalence_failures = 0
    matrices = 0
    semiprime_matrix_cases = 0
    k_checks = 0
    balanced_cases = 0
    rank_asymmetric_cases = 0
    proper_sigma_cases = 0

    semiprimes = [(p, q, p*q) for p, q in itertools.combinations(PRIMES, 2)]

    for m, n in DIMS:
        upto = min(m, n)
        for A in all_matrices(m, n):
            matrices += 1
            dvals = [Dk(A, k) for k in range(1, upto + 1)]
            for p, q, N in semiprimes:
                semiprime_matrix_cases += 1
                rp = rank_mod(A, p)
                rq = rank_mod(A, q)
                if rp == rq:
                    balanced_cases += 1
                else:
                    rank_asymmetric_cases += 1
                proper = False
                for k, d in enumerate(dvals, 1):
                    k_checks += 1
                    cp = (d % p == 0)
                    cq = (d % q == 0)
                    if cp != (rp < k) or cq != (rq < k):
                        rank_criterion_failures += 1
                    sigma = math.gcd(N, d)
                    if 1 < sigma < N:
                        proper = True
                if proper:
                    proper_sigma_cases += 1
                if proper != (rp != rq):
                    equivalence_failures += 1

    # Non-vacuity witness: balanced unimodular 3x3 seed, then a fixed
    # factor-blind row/column projection makes the p=3 channel singular.
    B0 = [[1,1,0],[1,4,1],[0,2,1]]
    A = [[B0[i][j] for j in (0,1)] for i in (0,1)]
    N, p, q = 15, 3, 5
    coord_gcds = [math.gcd(N, abs(x)) for row in B0 for x in row] + [math.gcd(N, abs(x)) for row in A for x in row]
    witness = {
        "N": N,
        "p": p,
        "q": q,
        "seed": B0,
        "projected": A,
        "coordinate_gcds": coord_gcds,
        "seed_rank_p": rank_mod(B0,p),
        "seed_rank_q": rank_mod(B0,q),
        "projected_rank_p": rank_mod(A,p),
        "projected_rank_q": rank_mod(A,q),
        "seed_support": support_profile(B0,N),
        "projected_support": support_profile(A,N),
    }
    assert witness["seed_rank_p"] == witness["seed_rank_q"] == 3
    assert witness["projected_rank_p"] == 1 and witness["projected_rank_q"] == 2
    assert [x["D_k"] for x in witness["seed_support"]] == [1,1,1]
    assert [x["D_k"] for x in witness["projected_support"]] == [1,3]
    assert all(g in (1,N) for g in coord_gcds)
    assert witness["projected_support"][-1]["sigma_k"] == 3

    cert = {
        "schema": "N_COUPLED_EXPLICIT_PRESENTATION_SCALARIZATION_CHECK_V1",
        "checker_execution": "PASS",
        "proof_role": "FINITE_REGRESSION_ONLY_NOT_GENERAL_PROOF",
        "python": platform.python_version(),
        "prime_set": PRIMES,
        "semiprimes": len(semiprimes),
        "dimensions": [list(x) for x in DIMS],
        "entry_alphabet": ALPHABET,
        "matrices": matrices,
        "semiprime_matrix_cases": semiprime_matrix_cases,
        "k_checks": k_checks,
        "balanced_cases": balanced_cases,
        "rank_asymmetric_cases": rank_asymmetric_cases,
        "proper_sigma_cases": proper_sigma_cases,
        "rank_criterion_failures": rank_criterion_failures,
        "equivalence_failures": equivalence_failures,
        "projection_witness": witness,
        "symbolic_laws_guarded": [
            "For every prime r, r divides D_k(A) iff rank_F_r(A mod r) < k.",
            "For N=pq with distinct primes, rank_F_p(A) != rank_F_q(A) iff some sigma_k(A)=gcd(N,D_k(A)) is a proper divisor of N.",
            "A balanced explicit presentation has only clean support scalars sigma_k in {1,N}; the first one-sided rank-support event creates a proper scalar gcd at the same explicit state.",
            "Arbitrary non-automorphic control/history does not evade this post-state scalarization when the resulting finite presentation matrix is explicit."
        ],
    }
    assert rank_criterion_failures == 0
    assert equivalence_failures == 0
    assert rank_asymmetric_cases == proper_sigma_cases
    print("PASS " + json.dumps(cert, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
