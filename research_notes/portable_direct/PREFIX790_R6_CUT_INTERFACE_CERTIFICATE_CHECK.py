#!/usr/bin/env python3
"""Exact nonnegative cut-interface and minimal residual-class regression.

External integer-path observer only. Parallel paths are distinct. No native X6
or physical dynamics execution is claimed. Standard-library Python integers.
"""
from collections import Counter, defaultdict
from random import Random
import json


def conv(a, b, modulus=None):
    result = Counter()
    for x, nx in a.items():
        for y, ny in b.items():
            z = x + y
            if modulus is not None:
                z %= modulus
            result[z] += nx * ny
    return +result


def hist(weights, modulus=None):
    ret = Counter()
    for w in weights:
        ret[w if modulus is None else w % modulus] += 1
    return +ret


def total(xs):
    ans = Counter()
    for x in xs:
        ans.update(x)
    return +ans


def markov_cut(left, right, modulus=None):
    return total(conv(hist(l, modulus), hist(r, modulus), modulus)
                 for l, r in zip(left, right))


def collapsed_cut(left, right, modulus=None):
    return conv(total(hist(l, modulus) for l in left),
                total(hist(r, modulus) for r in right), modulus)


def suffix_signature_quotient(left, right, modulus=None):
    groups = defaultdict(lambda: [Counter(), Counter()])
    for l, r in zip(left, right):
        signature = tuple(sorted(hist(r, modulus).items()))
        groups[signature][0].update(hist(l, modulus))
        groups[signature][1] = hist(r, modulus)
    return total(conv(a, b, modulus) for a, b in groups.values()), len(groups)


def compatible_paths(prefixes, suffixes, rows, modulus=None):
    out = Counter()
    for i, p in enumerate(prefixes):
        for j, r in enumerate(suffixes):
            if rows[i][j]:
                out[(p + r) if modulus is None else ((p + r) % modulus)] += 1
    return +out


def row_signature_quotient(prefixes, suffixes, rows, modulus=None):
    groups = defaultdict(list)
    for p, row in zip(prefixes, rows):
        groups[tuple(row)].append(p)
    out = total(conv(hist(left, modulus),
                     hist([s for s, permitted in zip(suffixes, row) if permitted], modulus),
                     modulus)
                for row, left in groups.items())
    return out, len(groups)


def weighted_suffix_quotient(prefixes, suffixes, rows, modulus=None):
    """Observer-specific exact count quotient by suffix weight histograms."""
    groups = defaultdict(lambda: [Counter(), Counter()])
    for p, row in zip(prefixes, rows):
        continuation = hist([s for s, allowed in zip(suffixes, row) if allowed], modulus)
        key = tuple(sorted(continuation.items()))
        groups[key][0].update(hist([p], modulus))
        groups[key][1] = continuation
    return total(conv(a, b, modulus) for a, b in groups.values()), len(groups)


def test():
    rng = Random(79020261115)
    moduli = (2, 3, 5, 6, 7, 11, 13)
    assertions = 0
    cut_cases = 0
    modular_cut_cases = 0
    min_classes = 10**9
    max_classes = 0
    false_target_witnesses = 0
    for _ in range(4096):
        k = rng.randint(2, 5)
        left = [tuple(rng.randint(-7, 7) for _ in range(rng.randint(1, 4))) for _ in range(k)]
        right = [tuple(rng.randint(-7, 7) for _ in range(rng.randint(1, 4))) for _ in range(k)]
        if rng.random() < .4:
            right[-1] = right[0]
        exact = markov_cut(left, right)
        direct = hist([a+b for ls, rs in zip(left, right) for a in ls for b in rs])
        assert exact == direct
        quotient, classes = suffix_signature_quotient(left, right)
        assert quotient == exact
        allpairs = collapsed_cut(left, right)
        assert all(allpairs[s] >= c for s, c in exact.items())
        ghost = hist([a+b for i, ls in enumerate(left) for j, rs in enumerate(right)
                      if i != j for a in ls for b in rs])
        assert allpairs == exact + ghost
        assert sum(exact.values()) == sum(len(l)*len(r) for l,r in zip(left,right))
        assert sum(allpairs.values()) == sum(map(len,left))*sum(map(len,right))
        min_classes = min(min_classes, classes)
        max_classes = max(max_classes, classes)
        assertions += 6
        cut_cases += 1
        for m in moduli:
            q, qclasses = suffix_signature_quotient(left, right, m)
            actual = markov_cut(left, right, m)
            full = collapsed_cut(left, right, m)
            assert actual == q
            assert actual == hist([x for x, c in exact.items() for _ in range(c)], m)
            assert all(full[r] >= c for r, c in actual.items())
            assert full == actual + hist([x for x,c in ghost.items() for _ in range(c)],m)
            assert 1 <= qclasses <= classes
            false_target_witnesses += sum(1 for r,c in full.items() if c>0 and actual[r]==0)
            assertions += 5
            modular_cut_cases += 1

    # Hidden-memory interface with one visible vertex but a diagonal guard.
    prefixes = [0, 1]
    suffixes = [0, 1]
    rows = [(True, False), (False, True)]
    real = compatible_paths(prefixes, suffixes, rows)
    wrong = conv(hist(prefixes), hist(suffixes))
    repaired, cls = row_signature_quotient(prefixes, suffixes, rows)
    assert real == Counter({0:1, 2:1})
    assert wrong == Counter({0:1,1:2,2:1})
    assert repaired == real and cls == 2
    assertions += 3

    guarded_cases = 0
    guarded_modular_cases = 0
    weighted_reductions = 0
    modular_weighted_reductions = 0
    min_guard_classes, max_guard_classes = 10**9, 0
    for _ in range(4096):
        n = rng.randint(1,7)
        z = rng.randint(1,7)
        ps = [rng.randint(-9,9) for _ in range(n)]
        ss = [rng.randint(-9,9) for _ in range(z)]
        rows = [tuple(bool(rng.getrandbits(1)) for _ in range(z)) for _ in range(n)]
        actual = compatible_paths(ps, ss, rows)
        quotient, c = row_signature_quotient(ps,ss,rows)
        assert actual == quotient
        weighted, wc = weighted_suffix_quotient(ps,ss,rows)
        assert weighted == actual and wc <= c
        weighted_reductions += (wc < c)
        naive = conv(hist(ps),hist(ss))
        assert all(naive[s] >= cnt for s,cnt in actual.items())
        assert sum(actual.values()) == sum(sum(row) for row in rows)
        assert c == len(set(rows))
        for a in set(rows):
            for b in set(rows):
                if a != b:
                    assert any(x!=y for x,y in zip(a,b))
        assertions += 6
        min_guard_classes=min(min_guard_classes,c)
        max_guard_classes=max(max_guard_classes,c)
        guarded_cases+=1
        for m in moduli:
            exact_mod = compatible_paths(ps,ss,rows,m)
            quotient_mod,_ = row_signature_quotient(ps,ss,rows,m)
            assert exact_mod == quotient_mod
            weighted_mod, wmc = weighted_suffix_quotient(ps,ss,rows,m)
            assert weighted_mod == exact_mod and wmc <= c
            modular_weighted_reductions += (wmc < c)
            assert exact_mod == hist([s for s,cnt in actual.items() for _ in range(cnt)],m)
            assertions += 3
            guarded_modular_cases+=1

    # A suffix-support-only merge can preserve reachability but not counts.
    l=[[0],[0]]; r=[[0],[0,0]]
    h=markov_cut(l,r)
    count_bad=conv(hist([0,0]),hist([0]))
    assert h == Counter({0:3}) and count_bad == Counter({0:2})
    assert set(h) == set(count_bad)
    assertions += 2

    # Distinct typed suffix rows may share the same weighted continuation.
    pp=[0,1]; qq=[0,0]; rr=[(True,False),(False,True)]
    wr,wc=weighted_suffix_quotient(pp,qq,rr)
    sr,sc=row_signature_quotient(pp,qq,rr)
    assert wr == sr == Counter({0:1,1:1}) and wc == 1 and sc == 2
    assertions += 1

    out = {
        'schema': 'PREFIX790_CUT_INTERFACE_EXACT_REGRESSION_V1',
        'status': 'ALL_CHECKS_PASS PREFIX790 CUT_INTERFACE_MINIMAL_RESIDUAL',
        'seed': 79020261115,
        'scope': 'finite two-step parallel-edge cut graphs and finite Boolean prefix/suffix compatibility interfaces; exact integer and modular counts; external observer only',
        'cut_cases': cut_cases,
        'modular_cut_cases': modular_cut_cases,
        'compatibility_cases': guarded_cases,
        'modular_compatibility_cases': guarded_modular_cases,
        'moduli': list(moduli),
        'exact_assertions': assertions,
        'cut_signature_class_range': [min_classes,max_classes],
        'guard_row_class_range': [min_guard_classes,max_guard_classes],
        'exact_weighted_suffix_quotient_strict_reductions': weighted_reductions,
        'modular_weighted_suffix_quotient_strict_reductions': modular_weighted_reductions,
        'modular_false_positive_residues_observed': false_target_witnesses,
        'fixed_witness': {
          'cut_states': ['alpha','beta'],
          'left_weights': [0,1], 'right_weights':[0,1],
          'true_histogram':{'0':1,'2':1},
          'all_cross_pair_histogram':{'0':1,'1':2,'2':1},
          'target':1,
          'modulus':3,
          'cross_pair_ghost_count':2,
          'same_vertex_hidden_memory_requires_rows': [[1,0],[0,1]],
          'suffix_support_equal_but_counts_differ': {'true':3,'quotient_wrong':2},
          'typed_rows_differ_but_weighted_suffix_equal': {'typed_classes':2,'count_observer_classes':1}
        },
        'theorem_basis': 'combinatorial bijection, nonnegative-semiring expansion, residual row distinguishability; regression is not universal proof',
        'source_pin': 'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'predecessor': 'PREFIX-789'
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return out


if __name__ == '__main__':
    test()
