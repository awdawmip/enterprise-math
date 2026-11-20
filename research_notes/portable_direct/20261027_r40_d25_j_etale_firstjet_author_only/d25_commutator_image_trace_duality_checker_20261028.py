#!/usr/bin/env python3
"""Exact finite-field commutator image/trace annihilator checker (auxiliary, non-native)."""
import itertools, json, random


def mat_mul(A, B, p):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) % p for j in range(n)] for i in range(n)]


def comm(B, A, p):
    X, Y = mat_mul(B, A, p), mat_mul(A, B, p)
    return [[(X[i][j] - Y[i][j]) % p for j in range(len(A))] for i in range(len(A))]


def trprod(C, K, p):
    n = len(C)
    return sum(C[i][j] * K[j][i] for i in range(n) for j in range(n)) % p


def unflat(x, n):
    return [list(x[i*n:(i+1)*n]) for i in range(n)]


def flat(A):
    return tuple(z for row in A for z in row)


def ad_columns(A, p):
    n = len(A)
    N = n*n
    cols = []
    for t in range(N):
        E = [[int(i*n+j == t) for j in range(n)] for i in range(n)]
        cols.append(flat(comm(E, A, p)))
    return cols


def rref_aug(M, p, ncols):
    B = [[v % p for v in row] for row in M]
    pivots = []
    r = 0
    for c in range(ncols):
        k = next((i for i in range(r, len(B)) if B[i][c]), None)
        if k is None:
            continue
        B[r], B[k] = B[k], B[r]
        inv = pow(B[r][c], -1, p)
        B[r] = [(x * inv) % p for x in B[r]]
        for i in range(len(B)):
            if i == r:
                continue
            q = B[i][c]
            if q:
                B[i] = [(a - q*b) % p for a, b in zip(B[i], B[r])]
        pivots.append(c)
        r += 1
        if r == len(B):
            break
    return B, pivots


def kernel(cols, p):
    N = len(cols)
    M = [[cols[j][i] for j in range(N)] for i in range(N)]
    R, pivots = rref_aug(M, p, N)
    free = [j for j in range(N) if j not in pivots]
    basis = []
    for q in free:
        x = [0] * N
        x[q] = 1
        for i, c in enumerate(pivots):
            x[c] = (-R[i][q]) % p
        basis.append(unflat(x, int(N**.5)))
    return basis, len(pivots)


def solve_ad(cols, target, p):
    N = len(cols)
    M = [[cols[j][i] for j in range(N)] + [target[i]] for i in range(N)]
    R, piv = rref_aug(M, p, N)
    if any(not any(row[:N]) and row[N] for row in R):
        return None
    B = [0] * N
    for i, c in enumerate(piv):
        B[c] = R[i][N]
    return unflat(B, int(N**.5))


def test_A(A, p, exhaustive=True):
    n = len(A)
    cols = ad_columns(A, p)
    Z, rank = kernel(cols, p)
    assert len(Z) + rank == n*n
    for C in Z:
        assert comm(C, A, p) == [[0]*n for _ in range(n)]
    all_k = {} if exhaustive else None
    if exhaustive:
        for digits in itertools.product(range(p), repeat=n*n):
            K = flat(comm(unflat(digits, n), A, p))
            all_k[K] = all_k.get(K, 0) + 1
        assert len(all_k) == p**rank
        assert set(all_k.values()) == {p**len(Z)}
        for digits in itertools.product(range(p), repeat=n*n):
            K = unflat(digits, n)
            allowed = all(trprod(C, K, p) == 0 for C in Z)
            assert allowed == (tuple(digits) in all_k)
    else:
        rng = random.Random(0xD250000 + p*10 + n + sum(flat(A)))
        for _ in range(50):
            raw = [rng.randrange(p) for _ in range(n*n)]
            B = unflat(raw, n)
            K = comm(B, A, p)
            assert all(trprod(C, K, p) == 0 for C in Z)
            Sol = solve_ad(cols, flat(K), p)
            assert Sol is not None and comm(Sol, A, p) == K
        for _ in range(80):
            K = unflat([rng.randrange(p) for _ in range(n*n)], n)
            allowed = all(trprod(C, K, p) == 0 for C in Z)
            Sol = solve_ad(cols, flat(K), p)
            assert allowed == (Sol is not None)
            if Sol is not None:
                assert comm(Sol, A, p) == K
    return dict(n=n, p=p, rank=rank, centralizer_dimension=len(Z), exhaustive=exhaustive, image_size=p**rank, fibers=p**len(Z))


def main():
    results = []
    # Complete list of all A and all K over F3 for 2x2 matrices.
    for digits in itertools.product(range(3), repeat=4):
        results.append(test_A(unflat(digits, 2), 3, True))
    # F5 checks every 2x2 A with both distinct-Jordan and irreducible representatives.
    cases_5 = [
        [[0,0],[0,0]], [[0,0],[0,1]], [[1,1],[0,1]],
        [[0,1],[4,0]], [[0,1],[1,0]], [[0,1],[1,1]],
    ]
    for A in cases_5:
        results.append(test_A(A, 5, True))
    # F3 rank-three: exact whole-domain B and K image count on selected A.
    cases_3 = [
        [[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,0],[0,1,0],[0,0,2]],
        [[0,1,0],[0,0,1],[0,0,0]],
    ]
    for A in cases_3:
        results.append(test_A(A, 3, True))
    # Larger primes and rank three via independent RREF satisfiability check.
    for p in (13, 19, 373):
        for n in (2,3):
            A = [[(i+1)**2 + j*7 + (i*j+3)**3 for j in range(n)] for i in range(n)]
            A = [[x % p for x in row] for row in A]
            results.append(test_A(A, p, False))
    p = 373
    A = [[0,0],[0,1]]
    B = [[0,1],[0,0]]
    K = comm(B, A, p)
    assert K == [[0,1],[0,0]]
    assert trprod([[1,0],[0,1]], K, p) == 0 and trprod(A, K, p) == 0
    impossible_I = [[1,0],[0,1]]
    impossible_trace_A = [[1,0],[0,p-1]]
    assert trprod([[1,0],[0,1]], impossible_I, p) == 2
    assert trprod(A, impossible_trace_A, p) == p-1
    out = {
        'schema':'AUTHOR_EXACT_CHECK_V1',
        'project':'Enterprise Math / D25 auxiliary matrix lift',
        'verification':'PASS',
        'classification':'AUTHOR_ONLY_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE',
        'statement':'Im(B -> BA-AB) equals trace-orthogonal complement of Z(A); each attainable K has p^dimZ(A) preimages',
        'source_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
        'algorithm':'F_p row reduction of ad_A and kernel + complete brute enumeration for all F3 2x2 A, six F5 2x2 A and three F3 3x3 A; sampled exact crosschecks for p=13,19,373',
        'cases':len(results),
        'case_breakdown':{
            'all_F3_rank2_matrices_A':81,
            'F5_rank2_representative_A':6,
            'F3_rank3_representative_A':3,
            'larger_prime_cases':6,
        },
        'prime_373_witness':{
            'A':A,'B':B,'K':K,
            'trace_K':0,'trace_AK':0,
            'contrast':'K=0 and K=E12 both meet trace existence tests; K=I and K=diag(1,-1) fail different tests',
        },
        'fingerprints':{'min_center_dim':min(x['centralizer_dimension'] for x in results),
                        'max_center_dim':max(x['centralizer_dimension'] for x in results),
                        'count_by_prime_rank':{str((p,n)):sum(x['p']==p and x['n']==n for x in results) for p,n in {(x['p'],x['n']) for x in results}}},
    }
    return out

if __name__ == '__main__':
    print(json.dumps(main(),sort_keys=True,ensure_ascii=False,indent=2))
