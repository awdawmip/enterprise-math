"""R116 exact finite verifier for online future-time signature refinement.

Auxiliary Boolean ranked model, not native Cell/Link/Port evolution.
Python 3, standard library only; fractions.Fraction throughout.
"""
from fractions import Fraction as Q
from random import Random
from collections import defaultdict
import json

I0, I1 = Q(0), Q(1)
X = Q(1, 4)


def eligible(t, theta):
    y = t * theta + X
    frac = y - y.numerator // y.denominator
    return Q(0) <= frac < Q(1, 2)


def cuts(t):
    if not t:
        return set()
    z0, z1 = X, t + X
    low, high = min(z0, z1), max(z0, z1)
    ans = set()
    for c in (Q(0), Q(1, 2)):
        for j in range(int(low) - 3, int(high) + 5):
            q = (Q(j) + c - X) / t
            if I0 < q < I1:
                ans.add(q)
    return ans


def atoms(times):
    cs = sorted({I0, I1}.union(*(cuts(t) for t in times)))
    xs = []
    for a, b in zip(cs, cs[1:]):
        xs.extend((a, (a + b) / 2))
    xs.append(cs[-1])
    return tuple(xs)


def signature(ts, x):
    return tuple(int(eligible(t, x)) for t in ts)


def top(h, x, k):
    return tuple(sorted((u for u in h if eligible(u[0], x)), reverse=True)[:k])


def capacity(F, G, x):
    c, d = F & G, F ^ G
    ds = [u for u in d if eligible(u[0], x)]
    if not ds:
        return None
    u = max(ds)
    return sum(v > u and eligible(v[0], x) for v in c)


def direct_equal_all_k(F, G, x, h):
    maxk = max(len(F), len(G)) + 1
    for k in range(1, maxk + 1):
        assert (top(F, x, k) == top(G, x, k)) == (h is None or k <= h)


def refine(old_times, new_t):
    old_times = tuple(sorted(old_times))
    assert new_t not in old_times
    new_times = tuple(sorted((*old_times, new_t)))
    old_xs, new_xs = atoms(old_times), atoms(new_times)
    old_sig = {signature(old_times, x) for x in old_xs}
    new_sig = {signature(new_times, x) for x in new_xs}
    fibers = defaultdict(set)
    for x in new_xs:
        fibers[signature(old_times, x)].add(int(eligible(new_t, x)))
    assert set(fibers) == old_sig
    assert len(new_sig) == len(old_sig) + sum(len(bits) == 2 for bits in fibers.values())
    assert len(old_sig) <= len(new_sig) <= 2 * len(old_sig)
    return old_xs, new_xs, old_sig, new_sig, fibers


def run():
    rng = Random(1162026)
    time_chain = [-3, 1, 7, -9, 13, 23]
    checks = 0
    inherited = 0
    witnesses = 0
    split_fibers = 0
    zero_inheritance = 0
    max_raw = 0
    max_sig = 0
    old_times = ()
    histories = [frozenset()]
    for t in time_chain:
        ox, nx, os, ns, fibers = refine(old_times, t)
        split_fibers += sum(len(v) == 2 for v in fibers.values())
        max_raw = max(max_raw, len(nx))
        max_sig = max(max_sig, len(ns))
        u = (t, 0)
        previous_histories = tuple(histories)
        next_histories = []
        for _ in range(36):
            base = rng.choice(previous_histories)
            F = set(base)
            G = set(rng.choice(previous_histories))
            # New potential time is not in either version before the actual edit.
            old_caps = {s: capacity(F, G, next(x for x in ox if signature(old_times, x) == s)) for s in os}
            for x in nx:
                assert capacity(F, G, x) == old_caps[signature(old_times, x)], (t, F, G, x, signature(old_times, x), capacity(F, G, x), old_caps[signature(old_times, x)], ox)
                inherited += 1
            # One-sided insertion; every false-eligibility child reuses old capacity exactly.
            F.add(u)
            for x in nx:
                h = capacity(F, G, x)
                direct_equal_all_k(F, G, x, h)
                checks += 1
                if not eligible(t, x):
                    assert h == old_caps[signature(old_times, x)]
                    zero_inheritance += 1
                if h is not None:
                    assert top(F, x, h + 1) != top(G, x, h + 1)
                    witnesses += 1
            next_histories.append(frozenset(F))
        histories = (list(previous_histories) + next_histories)[-24:]
        old_times = tuple(sorted((*old_times, t)))
    # Small complete enumeration over every pair of subsets and all exact atoms.
    U = ((-3, 0), (1, 0), (7, 0), (7, 1))
    xs = atoms({u[0] for u in U})
    subsets = [frozenset(U[i] for i in range(len(U)) if mask & (1 << i)) for mask in range(1 << len(U))]
    exhaustive = 0
    for F in subsets:
        for G in subsets:
            for x in xs:
                h = capacity(F, G, x)
                direct_equal_all_k(F, G, x, h)
                exhaustive += 1
    # A high-frequency new time creates many connected cut atoms, but at most doubles signatures.
    ox, nx, os, ns, fib = refine((), 101)
    assert len(os) == 1 and len(ns) == 2 and len(nx) >= 200
    return {"status":"R116_PASS","seed":1162026,"new_times":time_chain,
            "randomized_comparisons":checks,"unmodified_history_inheritance_checks":inherited,
            "zero_eligibility_capacity_inheritance_checks":zero_inheritance,
            "difference_witnesses":witnesses,"split_fibers":split_fibers,
            "exhaustive_pair_atom_checks":exhaustive,"max_raw_atoms":max_raw,
            "max_distinct_signatures":max_sig,"high_frequency_raw_atoms":len(nx),
            "high_frequency_distinct_signatures":len(ns),
            "arithmetic":"exact Fraction", "model":"half-open fractional threshold auxiliary ranked Boolean"}


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, ensure_ascii=False))
