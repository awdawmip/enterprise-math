#!/usr/bin/env python3
"""R749SUQ: exact segmented closest-divisor optimizer certificate (stdlib only)."""
import json
from math import isqrt


def near_product(M):
    t = isqrt(M + 1)
    k = M + 1 - t*t
    j = 1 if k <= t else 2
    z = 0
    while z*(z+j) < j*t-k:
        z += 1
    r, s = t-z, t+z+j
    p = r*s - 1
    assert 0 <= M-p <= 2*isqrt(t)+3
    return p


def segmented_optimizer(M):
    assert M >= 9999
    p = near_product(M)
    L, U = p+1, M+1
    dmax = isqrt(U)
    closest = [0]*(U-L+1)
    marks = 0
    for d in range(2, dmax+1):
        first = max(d*d, ((L+d-1)//d)*d)
        for n in range(first, U+1, d):
            closest[n-L] = d
            marks += 1
    score = -1
    opt = []
    total_labeled = 0
    for n in range(L, U+1):
        x = closest[n-L]
        if x < 2:
            continue
        y = n//x
        if n-x-y < 1:
            continue
        val = (n-1)*(n-x-1)*(n-y-1)
        multiplicity = 2 if x == y else 4
        if val > score:
            score, opt, total_labeled = val, [(n,x,y)], multiplicity
        elif val == score:
            opt.append((n,x,y))
            total_labeled += multiplicity
    assert score >= 0 and opt
    return score, total_labeled, opt, {"p":p, "width":U-L+1,
        "divisor_tests":max(0,dmax-1), "mark_updates":marks}


def independent_full_prefix(N):
    d = [0]*(N+2)
    for x in range(2, isqrt(N+1)+1):
        for n in range(x*x, N+2, x):
            d[n] = x
    out = {}
    best, count = -1, 0
    for M in range(2, N+1):
        n = M+1
        x = d[n]
        if x >= 2 and n-x-n//x >= 1:
            y = n//x
            val = (n-1)*(n-x-1)*(n-y-1)
            mul = 2 if x==y else 4
            if val > best:
                best, count = val, mul
            elif val == best:
                count += mul
        out[M] = (best,count)
    return out


def independent_window_trial(M):
    p = near_product(M)
    best, count = -1, 0
    for n in range(p+1, M+2):
        x = 0
        for d in range(2,isqrt(n)+1):
            if n%d == 0:
                x = d
        if x < 2 or n-x-n//x < 1:
            continue
        y = n//x
        val = (n-1)*(n-x-1)*(n-y-1)
        mul = 2 if x==y else 4
        if val > best:
            best, count = val, mul
        elif val == best:
            count += mul
    return best,count


def verify():
    oracle = independent_full_prefix(25000)
    for M in range(9999,25001):
        ans = segmented_optimizer(M)
        assert ans[:2] == oracle[M], (M,ans,oracle[M])
    examples = {}
    for M in (9999, 10000, 25000, 100000, 1000000, 100000000):
        score, labels, pairs, cost = segmented_optimizer(M)
        assert (score,labels) == independent_window_trial(M)
        examples[str(M)] = {"score":str(score),"labeled_ties":labels,
            "optimizing_factor_pairs":[list(z) for z in pairs],**cost}
    return {"status":"PASS", "version":"R749SUQ_V1",
      "exact_integer_tests":{"all_M_9999_to_25000":15002,
        "independent_large_window_trials":6},
      "method":"full independent prefix sieve; separately trial every divisor for 6 scales",
      "examples":examples,
      "scope":"finite tests; universal O(sqrt(M)) theorem is proven separately"}


if __name__ == '__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
