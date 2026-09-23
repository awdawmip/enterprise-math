#!/usr/bin/env python3
"""Regression for BRC absorbing-dirty quotient / clean-cone repair budget.

Finite computation is falsification/regression only. The symbolic theorem is in
research_notes/brc_clean_subcone_dirty_capacity_20260924.md.
"""
from collections import Counter

BOUND = 5000

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def primes_upto(n):
    return [p for p in range(2, n+1) if is_prime(p)]

def vp(n, p):
    c = 0
    while n and n % p == 0:
        n //= p
        c += 1
    return c

def factor(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d,e))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n,1))
    return out

def order_mod(a, p):
    o = p-1
    for r,_ in factor(p-1):
        while o % r == 0 and pow(a, o//r, p) == 1:
            o //= r
    return o

TARGETS = [p for p in primes_upto(BOUND) if p % 24 in (13,19)]
C13 = [p for p in TARGETS if p % 24 == 13]
C19 = [p for p in TARGETS if p % 24 == 19]

def s13(p):
    o = order_mod(4,p)
    assert p % 24 == 13 and o % 2 == 0
    return o // 2

def c13(p):
    s = s13(p)
    return vp(pow(4,s)+1, p)

S = {p:s13(p) for p in C13}
C = {p:c13(p) for p in C13}

def cancel13(p, j):
    s = S[p]
    return j % s == 0 and (j//s) % 2 == 1

def delta_single(r, j):
    h = (r-1)//2
    endpoint = int(j % h == 0)
    denom = vp(j, r)
    if r % 24 == 13:
        if cancel13(r,j):
            return endpoint + denom - (denom + C[r])
        return endpoint + denom
    return endpoint + denom

def debt19(q, r):
    sq = S[q]
    hr = (r-1)//2
    return int(sq % hr == 0) + vp(sq, r)

def dirty(q):
    return any(r < q and debt19(q,r) > 0 for r in C19)

HIGHER13 = [q for q in C13 if q > 13]
CLEAN = [q for q in HIGHER13 if not dirty(q)]
DIRTY = [q for q in HIGHER13 if dirty(q)]

# The intrinsic clean->dirty capacity coefficient.
def alpha_dirty(d, q):
    # d is dirty, q is clean.
    return int(S[q] % ((d-1)//2) == 0) + vp(S[q], d)

# 1. Exact matrix structural checks.
matrix_fail = []
positive_dirty_edges = []
for q in CLEAN:
    # own diagonal
    if delta_single(q, S[q]) != -C[q]:
        matrix_fail.append(("diag", q, delta_single(q,S[q]), -C[q]))
    # larger class-13 rows are never increased
    for r in HIGHER13:
        if r > q and delta_single(r, S[q]) > 0:
            matrix_fail.append(("upper-positive", r, q, delta_single(r,S[q])))
    # dirty rows cannot receive negative clean-column mass; exact intrinsic formula
    for d in DIRTY:
        if d >= q:
            continue
        a = delta_single(d, S[q])
        alpha = alpha_dirty(d,q)
        if a != alpha or a < 0:
            matrix_fail.append(("dirty-alpha", d, q, a, alpha))
        if a > 0:
            positive_dirty_edges.append((d,q,a))
assert not matrix_fail, matrix_fail[:10]

# 2. Divisibility/absorption witness: a clean step cannot contain a dirty
# cancellation step as an odd multiple.
nested_dirty_fail = []
for q in CLEAN:
    for d in DIRTY:
        if d >= q:
            continue
        if S[q] % S[d] == 0 and (S[q]//S[d]) % 2 == 1:
            nested_dirty_fail.append((d,q,S[d],S[q]))
assert not nested_dirty_fail, nested_dirty_fail[:10]

# 3. Exact causal repair on the canonical clean-atom cone for primitive endpoint
# initial carriers e_{h_p}. The recurrence processes clean q from largest down.
def causal_closure(p):
    hp = (p-1)//2
    earlier13 = [q for q in HIGHER13 if q < p]
    clean = [q for q in earlier13 if not dirty(q)]
    dirty_rows = [q for q in earlier13 if dirty(q)]
    b = {r:delta_single(r,hp) for r in earlier13}
    b19 = {r:delta_single(r,hp) for r in C19 if r < p}
    n = {}
    processed_fail = []
    for q in sorted(clean, reverse=True):
        x = b[q] + sum(delta_single(q,S[qq])*n[qq] for qq in n)
        nq = 0 if x <= 0 else (x + C[q] - 1)//C[q]
        n[q] = nq
        now = b[q] + sum(delta_single(q,S[qq])*n[qq] for qq in n)
        if now > 0:
            processed_fail.append((p,q,"not-closed",x,nq,now))
        # Later (smaller) clean columns must not be able to reawaken q.
        for later in clean:
            if later < q and delta_single(q,S[later]) > 0:
                processed_fail.append((p,q,"future-positive",later,delta_single(q,S[later])))
    final = {r:b[r] + sum(delta_single(r,S[q])*n[q] for q in clean) for r in earlier13}
    dirty_spend = {
        d:sum(delta_single(d,S[q])*n[q] for q in clean)
        for d in dirty_rows
    }
    dirty_slack = {d:-b[d] for d in dirty_rows}
    # exact ledger identity
    for d in dirty_rows:
        assert final[d] == b[d] + dirty_spend[d]
        assert dirty_spend[d] >= 0
    assert not processed_fail, processed_fail[:5]
    assert all(final[q] <= 0 for q in clean)
    return {
        "p":p, "clean":clean, "dirty":dirty_rows, "b":b, "b19":b19, "n":n,
        "final":final, "dirty_spend":dirty_spend, "dirty_slack":dirty_slack,
        "class19_ok":all(v <= 0 for v in b19.values()),
        "dirty_capacity_ok":all(b[d] <= 0 and dirty_spend[d] <= dirty_slack[d] for d in dirty_rows),
        "base13_out":delta_single(13,hp) + sum(delta_single(13,S[q])*n[q] for q in clean),
    }

runs = [causal_closure(p) for p in HIGHER13]
class19_clean = [r for r in runs if r["class19_ok"]]
capacity_pass = [r for r in class19_clean if r["dirty_capacity_ok"]]
capacity_fail = [r for r in class19_clean if not r["dirty_capacity_ok"]]

# This recovers the two previously structural class-13-only obstructions, now as
# dirty-capacity exhaustion in the quotient.
assert [r["p"] for r in capacity_fail] == [2221,2749], [r["p"] for r in capacity_fail]
assert capacity_fail[0]["final"][37] == 1
assert capacity_fail[1]["final"][229] == 1

# Active clean-repair primitive cases: eight use at least one clean atom;
# seven stay within dirty capacities, while p=2221 exhausts d=37.
active = [r for r in class19_clean if any(r["n"].values())]
assert [r["p"] for r in active] == [733,1021,1741,1861,2029,2221,3181,3541]
assert [r["p"] for r in active if r["dirty_capacity_ok"]] == [733,1021,1741,1861,2029,3181,3541]

# 4. The dirty-capacity edges are sparse but real; this is a census, not a theorem.
assert positive_dirty_edges == [(37,2221,1),(229,2749,1),(37,3109,1)], positive_dirty_edges

print({
    "target_primes_below_5000": len(TARGETS),
    "higher_class13": len(HIGHER13),
    "clean_class13": len(CLEAN),
    "dirty_class13": len(DIRTY),
    "clean_to_dirty_pairs_checked": sum(1 for q in CLEAN for d in DIRTY if d < q),
    "positive_intrinsic_dirty_capacity_edges": positive_dirty_edges,
    "matrix_structural_failures": 0,
    "nested_dirty_cancellation_failures": 0,
    "primitive_endpoint_targets_class19_clean": len(class19_clean),
    "primitive_endpoint_dirty_capacity_pass": len(capacity_pass),
    "primitive_endpoint_dirty_capacity_fail": [r["p"] for r in capacity_fail],
    "active_clean_repair_targets": [r["p"] for r in active],
    "active_clean_repair_capacity_pass": [r["p"] for r in active if r["dirty_capacity_ok"]],
    "failures": 0,
})
