#!/usr/bin/env python3
"""R730 exact labeled-source BRC port-edge count verifier; Python stdlib only."""
from functools import lru_cache
from itertools import combinations
from math import factorial
import json

AX = range(6)
ALL = set(combinations(AX, 3))
BASE = frozenset(t for t in ALL if not (0 in t and 1 in t))
assert len(BASE) == 16

@lru_cache(None)
def count(a, added):
    """Pivot one distinguishable source ID; choose its two distinct partners."""
    E = BASE if added == -1 else BASE | {(0, 1, added)}
    if not any(a):
        return 1
    if sum(a) % 3:
        return 0
    i = next(i for i, x in enumerate(a) if x)
    out = 0
    for t in E:
        if i not in t:
            continue
        j, k = (v for v in t if v != i)
        if a[j] and a[k]:
            b = list(a)
            b[i] -= 1; b[j] -= 1; b[k] -= 1
            out += a[j] * a[k] * count(tuple(b), added)
    return out

def support(a, k):
    m = sum(a) // 3
    lo = max(0, a[0] + a[1] - m)
    hi = min(a[0], a[1], a[k], m,
             *(m-a[j] for j in (2,3,4,5) if j != k))
    if a[k] > m or lo > hi:
        return ()
    return tuple(range(lo, hi+1))

def coefficient(a, k, s):
    b = list(a)
    f = 1
    for i in (0, 1, k):
        f *= factorial(a[i]) // factorial(a[i] - s)
        b[i] -= s
    assert f % factorial(s) == 0
    return f // factorial(s) * count(tuple(b), -1)

def vectors(total, n=6):
    if n == 1:
        yield (total,)
    else:
        for x in range(total+1):
            for tail in vectors(total-x, n-1):
                yield (x,) + tail

def verify():
    summary = {}
    for m in range(1, 5):
        st = dict(vectors=0, k_slices=0, feasible_slices=0,
                  no_feasible_slices=0, only_new_cases=0,
                  s_support_hist={}, max_positive_coeff=0, max_s=0)
        for a in vectors(3*m):
            st["vectors"] += 1
            old = count(a, -1)
            for k in (2,3,4,5):
                st["k_slices"] += 1
                iv = support(a,k)
                observed = tuple(s for s in range(min(m,a[0],a[1],a[k])+1)
                                 if coefficient(a,k,s) > 0)
                assert iv == observed, (m,a,k,iv,observed)
                opened = count(a,k)
                assert opened == sum(coefficient(a,k,s) for s in iv)
                if iv:
                    st["feasible_slices"] += 1
                    if 0 not in iv:
                        assert old == 0
                        st["only_new_cases"] += 1
                    label = str(iv[0]) + ":" + str(iv[-1])
                    st["s_support_hist"][label] = st["s_support_hist"].get(label,0)+1
                    st["max_positive_coeff"] = max(st["max_positive_coeff"],
                                                   max(coefficient(a,k,s) for s in iv))
                    st["max_s"] = max(st["max_s"], iv[-1])
                else:
                    st["no_feasible_slices"] += 1
                    assert opened == 0
        summary[str(m)] = st
    for m in range(1, 9):
        for r in range(1, m+1):
            a = (m, r, m, m-r, 0, 0)
            assert support(a, 2) == (r,)
            assert coefficient(a, 2, r) == factorial(m)**2
            assert count(a, 2) == factorial(m)**2
    summary["family"] = dict(m_checked=list(range(1,9)),
                             r_all_between_1_and_m=True,
                             count_m8=factorial(8)**2)
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("R730_EXACT_SUPPORT_AND_HIDDEN_ORDER_PASS")

if __name__ == "__main__":
    verify()
