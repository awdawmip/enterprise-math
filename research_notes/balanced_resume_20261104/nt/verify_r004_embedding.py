#!/usr/bin/env python3
"""Exact finite-set checks for the R004 local support draft; no external packages.

This is external finite module arithmetic, not a Heartbeat/BRC implementation.
All submodules are enumerated by adjoining vectors until closure stabilizes.
"""
import itertools
import json
import math
import time
from functools import lru_cache


class FiniteModule:
    def __init__(self, p, k, n):
        self.p, self.k, self.n = p, k, n
        self.m = p ** k
        self.zero = (0,) * n
        self.V = frozenset(itertools.product(range(self.m), repeat=n))

    def add(self, u, v):
        return tuple((a + b) % self.m for a, b in zip(u, v))

    def scale(self, a, v):
        return tuple((a * x) % self.m for x in v)

    @lru_cache(None)
    def plus(self, a, b):
        return frozenset(self.add(x, y) for x in a for y in b)

    @lru_cache(None)
    def cyclic(self, v):
        return frozenset(self.scale(a, v) for a in range(self.m))

    def span(self, *vectors):
        out = frozenset([self.zero])
        for v in vectors:
            out = self.plus(out, self.cyclic(v))
        return out

    def all_submodules(self):
        trivial = frozenset([self.zero])
        found, pending = {trivial}, [trivial]
        while pending:
            h = pending.pop()
            for v in self.V - h:
                new = self.plus(h, self.cyclic(v))
                if new not in found:
                    found.add(new)
                    pending.append(new)
        return sorted(found, key=lambda s: (len(s), sorted(s)))

    @lru_cache(None)
    def cosets(self, w, a):
        assert a <= w
        return frozenset(frozenset(self.add(v, x) for x in a) for v in w)

    @lru_cache(None)
    def profile(self, w, a):
        assert a <= w
        sizes = []
        for j in range(self.k + 1):
            scaled = frozenset(self.scale(self.p ** j, v) for v in w)
            sizes.append(len(self.plus(a, scaled)))
        out = []
        for x, y in zip(sizes, sizes[1:]):
            assert x % y == 0
            ratio, exp = x // y, 0
            while ratio > 1 and ratio % self.p == 0:
                ratio //= self.p
                exp += 1
            assert ratio == 1
            out.append(exp)
        return tuple(out)

    def defect(self, a, b):
        return self.profile(self.plus(a, b), a)


def gaussian(p, n, d):
    numerator = math.prod(p ** n - p ** i for i in range(d))
    denominator = math.prod(p ** d - p ** i for i in range(d))
    assert numerator % denominator == 0
    return numerator // denominator


def examples():
    z4 = FiniteModule(2, 2, 1)
    z, ideal, whole = z4.span(), z4.span((2,)), z4.V
    pairs = [(ideal, whole), (z, ideal)]
    pre = [z4.defect(a, b) for a, b in pairs]
    post = [z4.defect(z4.plus(a, ideal), b) for a, b in pairs]
    assert pre == [(1, 0), (1, 0)] and post == [(1, 0), (0, 0)]

    f2 = FiniteModule(2, 1, 2)
    z, d = f2.span(), f2.span((1, 0))
    u, v = f2.span((0, 1)), f2.span((1, 1))
    assert f2.defect(z, d) == f2.defect(z, u) == (1,)
    fixed_q_post = [f2.defect(d, b) for b in (d, u)]
    assert fixed_q_post == [(0,), (1,)]
    schedules = [(u, v), (u, u)]
    kernels = [[sorted(d & c) for c in schedule] for schedule in schedules]
    assert kernels[0] == kernels[1] == [[(0, 0)], [(0, 0)]]
    combined = [f2.defect(f2.plus(c1, c2), d) for c1, c2 in schedules]
    assert combined == [(0,), (1,)]
    return {"rank_one_z4": {"before": pre, "after": post},
            "fixed_ambient_f2_squared": {"after": fixed_q_post},
            "individual_kernel_collision": {"kernels": kernels, "after_joint": combined}}


def check_quotient_law():
    m = FiniteModule(2, 2, 2)
    subs = m.all_submodules()
    triples = 0
    for a, b, c in itertools.product(subs, repeat=3):
        w, ac = m.plus(a, b), m.plus(a, c)
        kernel_preimage = w & ac
        numerator = m.plus(w, c)
        # Count actual cosets; additionally compare every p-adic layer.
        lhs, rhs = m.cosets(numerator, ac), m.cosets(w, kernel_preimage)
        assert len(lhs) == len(rhs)
        assert m.profile(numerator, ac) == m.profile(w, kernel_preimage)
        # Explicit quotient map from W to V/(A+C) is onto the updated defect.
        image = frozenset(frozenset(m.add(v, x) for x in ac) for v in w)
        assert image == lhs
        triples += 1
    quadruples = 0
    for a, b, c1, c2 in itertools.product(subs, repeat=4):
        w, ac1 = m.plus(a, b), m.plus(a, c1)
        ac12 = m.plus(ac1, c2)
        # At step 1 keep the *ambient* coset representation and map it onward.
        first_defect = m.cosets(m.plus(w, c1), ac1)
        transported = frozenset(
            frozenset(m.add(next(iter(coset)), x) for x in ac12)
            for coset in first_defect
        )
        direct = m.cosets(m.plus(w, m.plus(c1, c2)), ac12)
        assert transported == direct
        quadruples += 1
    # Coordinate deletion f(x,y)=x is a surjective coordinate map.
    target = FiniteModule(2, 2, 1)
    n = m.span((0, 1))
    maps = 0
    for a, b in itertools.product(subs, repeat=2):
        fa = frozenset((v[0],) for v in a)
        fb = frozenset((v[0],) for v in b)
        assert target.defect(fa, fb) == m.defect(m.plus(a, n), b)
        maps += 1
    return {"p": 2, "k": 2, "n": 2, "ambient_elements": len(m.V),
            "all_submodules": len(subs), "all_triples": triples,
            "all_two_update_quadruples": quadruples,
            "coordinate_deletion_pairs": maps}


def check_behavior_and_capacity():
    rows = []
    for p, n in [(2, 2), (2, 3), (3, 2), (3, 3), (5, 2)]:
        m = FiniteModule(p, 1, n)
        subs = m.all_submodules()
        lines = [s for s in subs if len(s) == p]
        by_dim = {}
        for d in range(n + 1):
            states = [s for s in subs if len(s) == p ** d]
            signatures = {tuple(len(s) // len(s & c) for c in lines) for s in states}
            assert len(signatures) == len(states) == gaussian(p, n, d)
            # Zero/nonzero observations after arbitrary finite cyclic schedules:
            # every subspace C is the span of such a schedule.
            zero_signatures = {tuple(s <= c for c in subs) for s in states}
            assert len(zero_signatures) == len(states)
            by_dim[str(d)] = {"states": len(states),
                              "one_step_size_signatures": len(signatures),
                              "all_finite_zero_query_signatures": len(zero_signatures),
                              "fixed_length_bits": (len(states) - 1).bit_length()}
        rows.append({"p": p, "n": n, "all_subspaces": len(subs),
                     "cyclic_nonzero_controls": len(lines), "dimensions": by_dim})
    return rows


def rank_one_minimality():
    checked = 0
    for p in (2, 3, 5):
        m = FiniteModule(p, 1, 1)
        subs = m.all_submodules()
        groups = {}
        for a, b in itertools.product(subs, repeat=2):
            groups.setdefault(m.defect(a, b), []).append((a, b))
        for pairs in groups.values():
            signatures = {tuple(m.defect(m.plus(a, c), b) for c in subs) for a, b in pairs}
            assert len(signatures) == 1
            checked += len(pairs)
    return {"primes": [2, 3, 5], "rank_one_field_state_pairs": checked,
            "scope": "Finite confirmation only; paper proves this for every prime."}


if __name__ == "__main__":
    started = time.perf_counter()
    result = {"status": "PASS", "arithmetic": "exact finite sets over Z/(p^k)",
              "examples": examples(), "quotient_law": check_quotient_law(),
              "behavior_and_capacity": check_behavior_and_capacity(),
              "rank_one_minimality": rank_one_minimality()}
    result["elapsed_seconds"] = round(time.perf_counter() - started, 6)
    print(json.dumps(result, indent=2, sort_keys=True))
