#!/usr/bin/env python3
"""Independent exact R063 512-row SHA256 reconciliation. Author-side, not native replay."""
import json
from hashlib import sha256
from collections import Counter
from math import gcd, isqrt

EXPECTED = "51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae"

def digest(x):
    b = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(b).hexdigest()

def factor(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def direct(N):
    return {(a, b) for a in range(isqrt(N) + 1)
            if (v := N - a * a) >= 0 and (b := isqrt(v)) ** 2 == v}

def c2(r):
    out = set()
    for m, n in direct(r):
        if m >= n:
            a, b = m * m - n * n, 2 * m * n
            out.update(((a, b), (b, a)))
    return out

def c3(r):
    out = {(0, r), (r, 0)}
    for m in range(2, isqrt(r) + 1):
        for n in range(1, m):
            h = m * m + n * n
            if h > r:
                break
            if r % h == 0 and gcd(m, n) == 1 and (m - n) % 2:
                k = r // h
                a, b = k * (m * m - n * n), k * (2 * m * n)
                out.update(((a, b), (b, a)))
    return out

def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

def power(z, k):
    a = (1, 0)
    for _ in range(k):
        a = mul(a, z)
    return a

def split_prime(p):
    for a in range(1, isqrt(p) + 1):
        v = p - a * a
        if v > 0 and (b := isqrt(v)) ** 2 == v:
            return (a, b)
    raise AssertionError(("split prime not represented", p))

def c4(N):
    """Gaussian split/inert/ramified allocation; no full norm-fibre lookup."""
    zlist = {(1, 0)}
    for p, e in factor(N).items():
        if p == 2:
            choices = {power((1, 1), e)}
        elif p % 4 == 3:
            assert e % 2 == 0
            choices = {(p ** (e // 2), 0)}
        else:
            pi = split_prime(p)
            cj = (pi[0], -pi[1])
            choices = {mul(power(pi, k), power(cj, e - k)) for k in range(e + 1)}
        zlist = {mul(u, v) for u in zlist for v in choices}
    units = ((1, 0), (0, 1), (-1, 0), (0, -1))
    roots = {z for a in zlist for u in units
             if (z := mul(a, u))[0] >= 0 and z[1] >= 0}
    assert all(a*a + b*b == N for a, b in roots)
    return roots

def main():
    rows, errors_c2, hist = [], [], Counter()
    for r in range(1, 513):
        N = r * r
        brute, v2, v3, v4 = direct(N), c2(r), c3(r), c4(N)
        assert v3 == brute, ("C3", r, sorted(brute-v3), sorted(v3-brute))
        assert v4 == brute, ("C4", r, sorted(brute-v4), sorted(v4-brute))
        if v2 != brute:
            errors_c2.append({"r":r, "N":N,
                              "missing":[list(v) for v in sorted(brute-v2)],
                              "extra":[list(v) for v in sorted(v2-brute)]})
        hist[len(brute)] += 1
        rows.append({"r":r, "N":N, "brute_branch_count":len(brute),
                     "C2_exact":v2==brute, "C3_exact":v3==brute,
                     "C4_exact":v4==brute,
                     "fiber_sha256":digest([list(v) for v in sorted(brute)])})
    h = digest(rows)
    assert h == EXPECTED, (h, EXPECTED)
    assert len(rows) == 512 and len(errors_c2) == 484
    assert errors_c2[0] == {"r":3,"N":9,"missing":[[0,3],[3,0]],"extra":[]}
    assert sum(n * c for n, c in hist.items()) == 1820
    result = {"status":"PASS_AUTHOR_EXACT_512_ROWS_NOT_NATIVE_REPLAY",
              "regression_r_range":[1,512],"rows_sha256":h,
              "C2_failure_count":len(errors_c2),
              "C2_first_failure":errors_c2[0],
              "C3_mismatch_count":0,"C4_mismatch_count":0,
              "root_count_histogram":dict(sorted(hist.items())),
              "root_occurrences":sum(n*c for n,c in hist.items()),
              "original_native_loader_executed":False,
              "original_17_gates_executed":False,
              "review_status":"UNREVIEWED_NOT_ADMITTED"}
    print("PASS_X6_R063_512_ORIGINAL_ROW_DIGEST_INDEPENDENT_C2_C3_C4")
    print(json.dumps(result, sort_keys=True, ensure_ascii=False))
    return result

if __name__ == "__main__":
    main()
