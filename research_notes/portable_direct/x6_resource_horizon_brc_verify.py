#!/usr/bin/env python3
"""Exact finite typed Boolean BRC reachability and source-future horizon certificates.

Carrier: provenance-preserving (source word, resource state) branches. Typed support
quotient: (A count, B count, resource state); guarded deterministic appends.
Scope: conditional finite two-source event model, NOT native TRIADIC_CLOSURE_E admission.
"""
import itertools
import json
from collections import defaultdict
from functools import lru_cache
from math import gcd

ALPHABET = ('A', 'B')


def model(a, b, transitions, root=0):
    def step(s, x):
        i, j, q = s
        if x == 'A':
            if i == a:
                return None
            i += 1
        else:
            if j == b:
                return None
            j += 1
        nq = transitions.get((q, x))
        return None if nq is None else (i, j, nq)

    levels = [{(0, 0, root)}]
    for _ in range(a + b):
        levels.append({t for s in levels[-1] for x in ALPHABET
                       if (t := step(s, x)) is not None})
    all_states = frozenset(s for lev in levels for s in lev)

    @lru_cache(None)
    def completions(s):
        if s[:2] == (a, b):
            return frozenset([''])
        out = set()
        for x in ALPHABET:
            t = step(s, x)
            if t is not None:
                out.update(x + word for word in completions(t))
        return frozenset(out)

    @lru_cache(None)
    def productive(s):
        if s[:2] == (a, b):
            return True
        return any((t := step(s, x)) is not None and productive(t)
                   for x in ALPHABET)

    # Canonical integer IDs for exact finite prefix-language tries. This
    # explicitly hash-conses the typed source-labelled Boolean BRC DAG.
    signature_ids = {}

    @lru_cache(None)
    def signature(s, horizon):
        if not productive(s):
            return None
        children = () if horizon == 0 else tuple(
            (x, signature(t, horizon - 1))
            for x in ALPHABET
            if (t := step(s, x)) is not None and productive(t))
        # The empty word is always admitted for a productive state. Canonical
        # child edges completely determine its bounded prefix language.
        if children not in signature_ids:
            signature_ids[children] = len(signature_ids) + 1
        return signature_ids[children]

    @lru_cache(None)
    def brute_prefixes(s, horizon):
        if not completions(s):
            return frozenset()
        return frozenset(w[:j] for w in completions(s)
                         for j in range(min(horizon, len(w)) + 1))

    def observed(s, pa, pb):
        i, j, _ = s
        return (i+j, i % pa, j % pb)

    def mh(k, h, pa, pb, key):
        classes = defaultdict(set)
        for s in levels[k]:
            if productive(s):
                classes[observed(s, pa, pb)].add(key(s, h))
        return max(map(len, classes.values()), default=0)

    def full_formula(k, pa, pb):
        per_count = defaultdict(set)
        for s in levels[k]:
            if productive(s):
                per_count[s[:2]].add(completions(s))
        period = pa * pb // gcd(pa, pb)
        return max((sum(len(classes) for (i, j), classes in per_count.items()
                        if i % period == residue)
                    for residue in range(period)), default=0)

    return locals()


def check_typed_branches(a, b, transitions):
    data = model(a, b, transitions)
    words = {('', 0)}
    for k, level in enumerate(data['levels']):
        reached = {(word.count('A'), word.count('B'), q) for word, q in words}
        assert reached == level, ('typed-support', a, b, transitions, k)
        upcoming = set()
        for word, q in words:
            s = (word.count('A'), word.count('B'), q)
            for x in ALPHABET:
                t = data['step'](s, x)
                if t is not None:
                    upcoming.add((word+x, t[2]))
        words = upcoming


def check_small_models():
    checks = 0
    nonempty = 0
    indistinct_h1_later_split = 0
    # Every deterministic partial two-state controller: each state/source
    # transitions to absent, state 0 or state 1 (3^4 possibilities).
    for targets in itertools.product((None, 0, 1), repeat=4):
        delta = dict(zip(itertools.product((0, 1), ALPHABET), targets))
        for a in (1, 2, 3):
            for b in (1, 2, 3):
                check_typed_branches(a, b, delta)
                data = model(a, b, delta)
                if data['completions']((0, 0, 0)):
                    nonempty += 1
                for k in range(a+b+1):
                    horizon = a+b-k
                    states = [s for s in data['levels'][k] if data['productive'](s)]
                    for h in range(horizon+1):
                        # Hash-consed typed BRC future signatures exactly match
                        # independently materialized completed-word prefixes.
                        for s in states:
                            for t in states:
                                assert ((data['signature'](s, h) == data['signature'](t, h))
                                        == (data['brute_prefixes'](s, h)
                                            == data['brute_prefixes'](t, h)))
                        for pa, pb in ((2, 2), (2, 3)):
                            assert data['mh'](k, h, pa, pb, data['signature']) == data['mh'](
                                k, h, pa, pb, data['brute_prefixes'])
                    for pa, pb in ((2, 2), (2, 3)):
                        profile = [data['mh'](k, h, pa, pb, data['signature'])
                                   for h in range(horizon+1)]
                        assert profile == sorted(profile), ('monotonicity', k, profile)
                        assert profile[-1] == data['full_formula'](k, pa, pb)
                        if horizon >= 1:
                            # P=lcm(pa,pb)>=2: the final required label is
                            # determined once a productive H-1 prefix is known.
                            assert profile[-2] == profile[-1], ('H-1', k, profile)
                        if profile and profile[0] < profile[-1]:
                            indistinct_h1_later_split += 1
                checks += 1
    return {'controller_structures': 3**4, 'capacity_pairs': 9,
            'model_cases': checks, 'models_with_full_completion': nonempty,
            'rank_phase_profiles_with_late_distinction': indistinct_h1_later_split,
            'exact_comparison': 'all reachable productive state pairs, all ranks, every horizon, two local phase pairs',
            'result': 'PASS'}


def late_controller(d):
    # After the same-count AB/BA prefixes: remember first source A or B, allow
    # arbitrary d labels, then distinguish the (d+1)st future event.
    delta = {(0, 'A'): ('FIRST_A',), (0, 'B'): ('FIRST_B',),
             (('FIRST_A',), 'B'): ('A', 0),
             (('FIRST_B',), 'A'): ('B', 0)}
    for mode in ALPHABET:
        for t in range(d):
            for x in ALPHABET:
                delta[((mode, t), x)] = (mode, t+1)
        delta[((mode, d), mode)] = ('RELEASED',)
    for x in ALPHABET:
        delta[(('RELEASED',), x)] = ('RELEASED',)
    return delta


def check_delayed_family(max_d=10):
    results = []
    for d in range(max_d+1):
        a = b = d+3
        data = model(a, b, late_controller(d))
        x = (1, 1, ('A', 0))
        y = (1, 1, ('B', 0))
        assert x in data['levels'][2] and y in data['levels'][2]
        assert data['productive'](x) and data['productive'](y)
        horizon = d+1
        equality_profile = [data['signature'](x, h) == data['signature'](y, h)
                            for h in range(horizon+1)]
        assert equality_profile == [True]*(d+1) + [False]
        assert data['mh'](2, d, a+1, b+1, data['signature']) == 1
        assert data['mh'](2, d+1, a+1, b+1, data['signature']) == 2
        # One exact shortest labelled future witness is A^(d+1).
        w = 'A'*(d+1)
        def accepts_prefix(s, word):
            for letter in word:
                s = data['step'](s, letter)
                if s is None:
                    return False
            return data['productive'](s)
        assert accepts_prefix(x, w) and not accepts_prefix(y, w)
        results.append({'d': d, 'capacity_each': a,
                        'indistinguishable_through': d,
                        'first_distinguishing_horizon': d+1,
                        'extra_bits_at_k2_before_after': [0, 1]})
    return results


def terminal_sharp_controller(m):
    # From equal-count AB/BA histories at k=2, both modes must append exactly
    # (AB)^(m-2), leaving (1 A,1 B) of the total quotas; the penultimate
    # future label is then chosen according to the first-event memory.
    word = 'AB'*(m-2)
    delta = {(0,'A'):('FIRST_A',), (0,'B'):('FIRST_B',),
             (('FIRST_A',),'B'):('A',0), (('FIRST_B',),'A'):('B',0)}
    for mode in ALPHABET:
        for t, label in enumerate(word):
            delta[((mode,t),label)] = (mode,t+1)
        delta[((mode,len(word)),mode)] = ('RELEASED',)
    for x in ALPHABET:
        delta[(('RELEASED',),x)] = ('RELEASED',)
    return delta


def check_sharp_terminal(max_m=9):
    witness = []
    for m in range(2,max_m+1):
        data = model(m,m,terminal_sharp_controller(m))
        x,y = (1,1,('A',0)),(1,1,('B',0))
        H = 2*m-2
        assert x in data['levels'][2] and y in data['levels'][2]
        assert data['productive'](x) and data['productive'](y)
        equal = [data['signature'](x,h)==data['signature'](y,h)
                 for h in range(H+1)]
        assert equal == [True]*(H-1)+[False,False]
        assert data['mh'](2,H-2,m+1,m+1,data['signature']) == 1
        assert data['mh'](2,H-1,m+1,m+1,data['signature']) == 2
        witness.append({'m':m,'total_remaining_from_k2':H,
                        'shared_future_prefix_through':H-2,
                        'first_difference_at':H-1,
                        'selector_bits_before_after':[0,1]})
    return witness


def check_period_one_boundary():
    data = model(1,1,{(0,'A'):0,(0,'B'):0})
    x,y = (1,0,0),(0,1,0)
    assert data['mh'](1,0,1,1,data['signature']) == 1
    assert data['mh'](1,1,1,1,data['signature']) == 2
    assert data['signature'](x,0) == data['signature'](y,0)
    assert data['signature'](x,1) != data['signature'](y,1)
    return {'capacities':[1,1],'periods':[1,1],'k':1,
            'remaining_horizon':1,'M_h0':1,'M_h1':2,'result':'PASS'}


def check_no_port_count_alias():
    # A different-count pair can have indistinguishable short productive futures,
    # so the full-language count-wise sum is invalid before full horizon.
    data = model(3, 3, {(0, 'A'):0, (0, 'B'):0})
    x, y = (0, 2, 0), (2, 0, 0)
    assert data['signature'](x, 1) == data['signature'](y, 1)
    assert data['signature'](x, 2) != data['signature'](y, 2)
    assert data['mh'](2, 1, 2, 2, data['signature']) == 1
    assert data['mh'](2, 2, 2, 2, data['signature']) == 2
    return {'a':3, 'b':3, 'periods':[2,2], 'k':2,
            'phase_alias_count_pairs':[[0,2],[2,0]],
            'M_h1':1,'M_h2':2,'first_distinguishing_horizon':2,
            'result':'PASS'}


def run():
    small = check_small_models()
    delay = check_delayed_family(10)
    terminal = check_sharp_terminal(9)
    period_one = check_period_one_boundary()
    count_alias = check_no_port_count_alias()
    return {'schema':'X6_CONDITIONAL_TYPED_BRC_HORIZON_CERTIFICATE_V1',
            'scope':'finite source-labelled boolean BRC support under conditional deterministic partial port guard',
            'small_exhaustive':small,
            'unbounded_delay_samples':delay,
            'sharp_H_minus_1_samples':terminal,
            'period_one_H_bound_witness':period_one,
            'different_count_short_horizon_alias':count_alias,
            'all_assertions':'PASS',
            'not_claimed':'native Cell/Link/Port TRIADIC_CLOSURE_E admission or physical time'}

if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
