#!/usr/bin/env python3
"""Exact finite checker for typed two-chain event counts + historyful port-state automata.

The model is conditional; it does not admit native X6 Cell/Link/Port events.
No floating-point arithmetic, external packages or Monte Carlo steps.
"""
import json
from collections import defaultdict
from functools import lru_cache
from itertools import product

ALPHABET = ('A', 'B')


def check_model(a, b, p_a, p_b, delta, q0=0, inspect=False):
    """Compute exact future-language classes by recursive signatures and by full words."""
    def step(s, label):
        i, j, q = s
        if label == 'A':
            if i == a: return None
            ii, jj = i + 1, j
        else:
            if j == b: return None
            ii, jj = i, j + 1
        qq = delta.get((q, label))
        return None if qq is None else (ii, jj, qq)

    ranks = [set() for _ in range(a + b + 1)]
    ranks[0].add((0, 0, q0))
    for k in range(a + b):
        for state in ranks[k]:
            for label in ALPHABET:
                target = step(state, label)
                if target is not None:
                    ranks[k + 1].add(target)

    @lru_cache(None)
    def sig(s):
        i, j, _ = s
        if (i, j) == (a, b):
            return ('END',)
        child = tuple((label, sig(step(s, label)))
                      for label in ALPHABET
                      if step(s, label) is not None and sig(step(s, label)) is not None)
        return ('NODE', child) if child else None

    @lru_cache(None)
    def full_suffixes(s):
        i, j, _ = s
        if (i, j) == (a, b):
            return frozenset(('',))
        words = set()
        for label in ALPHABET:
            target = step(s, label)
            if target is not None:
                words.update(label + word for word in full_suffixes(target))
        return frozenset(words)

    observation = defaultdict(set)
    count_observation = defaultdict(lambda: defaultdict(set))
    result_by_rank = [0] * (a + b + 1)
    count_by_rank = [0] * (a + b + 1)
    resource_splits = 0
    productive = 0
    for k, level in enumerate(ranks):
        for s in level:
            v = sig(s)
            f = full_suffixes(s)
            assert (v is None) == (len(f) == 0)
            if v is None:
                continue
            productive += 1
            assert all(len(w) == a+b-k for w in f)
            o = (k, s[0] % p_a, s[1] % p_b)
            observation[o].add(v)
            count_observation[o][s[:2]].add(v)
        for o in (key for key in observation if key[0] == k):
            count_classes = count_observation[o]
            # Different completed count vectors yield disjoint complete source words.
            expected = sum(len(v) for v in count_classes.values())
            assert len(observation[o]) == expected, (a, b, p_a, p_b, delta, o)
            result_by_rank[k] = max(result_by_rank[k], expected)
            count_by_rank[k] = max(count_by_rank[k], len(count_classes))
            if any(len(c) > 1 for c in count_classes.values()):
                resource_splits += 1

    # At a fixed rank, language-signature equality is exactly equality of full
    # completion-word sets. This is an independent exhaustive oracle.
    for level in ranks:
        ss = [s for s in level if sig(s) is not None]
        for s in ss:
            for t in ss:
                assert (sig(s) == sig(t)) == (full_suffixes(s) == full_suffixes(t))

    out = {
        'productive_states': productive,
        'complete_words': len(full_suffixes((0, 0, q0))),
        'max_language_classes_by_rank': result_by_rank,
        'max_distinct_count_vectors_by_rank': count_by_rank,
        'resource_distinguished_observation_fibers': resource_splits,
        'minimum_extra_bits_by_rank': [(m-1).bit_length() for m in result_by_rank],
        'uniform_extra_bits': (max(result_by_rank)-1).bit_length(),
        'equivalence_oracle': 'all completed source-label suffix words',
    }
    if inspect:
        k = 2
        ss = sorted(s for s in ranks[k] if sig(s) is not None)
        out['k2_states'] = [{'state': list(s), 'future_words': sorted(full_suffixes(s))}
                            for s in ss]
        out['complete_source_words'] = sorted(full_suffixes((0, 0, q0)))
    return out


def run():
    # Explicit last-used-source exclusive port/cooldown model: A, B alternate.
    # 0=unallocated, 1=last A, 2=last B. Finite port memory is not an X6 primitive.
    alternating = {(0,'A'):1,(0,'B'):2,(1,'B'):2,(2,'A'):1}
    examples = {}
    for m in (2,3,4,5):
        r = check_model(m,m,m+1,m+1,alternating,inspect=(m==2))
        assert r['complete_words'] == 2
        expected = [0] * (2*m+1)
        for k in range(2,2*m,2):
            expected[k] = 1
        assert r['minimum_extra_bits_by_rank'] == expected, (m,r)
        examples[str(m)] = r

    assert examples['2']['complete_source_words'] == ['ABAB','BABA']
    assert {tuple(x['state']):tuple(x['future_words'])
            for x in examples['2']['k2_states']} == {
                (1,1,1):('BA',), (1,1,2):('AB',)
            }

    # Completely enumerate each deterministic partial port automaton Q={0,1}
    # over A/B. Every one of its four transitions is absent or targets 0 or 1:
    # 3^4=81 controllers; 9 chain-length pairs; 4 phase-period pairs.
    period_pairs = ((2,2),(2,3),(3,3),(3,4))
    controllers = models = productive_models = 0
    nontrivial_fiber_models = 0
    models_with_resource_split = 0
    models_with_more_bits_than_count_only = 0
    sample_resource_split = None
    for choices in product((-1,0,1),repeat=4):
        controllers += 1
        d = {(q, lab):choices[2*q+i]
             for q in (0,1) for i,lab in enumerate(ALPHABET)
             if choices[2*q+i] != -1}
        for a in (1,2,3):
            for b in (1,2,3):
                for pa,pb in period_pairs:
                    result = check_model(a,b,pa,pb,d)
                    models += 1
                    if result['complete_words'] > 0:
                        productive_models += 1
                        # A phase observer can require more memory than the
                        # distinct count-supports in that phase whenever distinct
                        # historyful port states yield different complete languages.
                        if max(result['max_language_classes_by_rank']) >= 2:
                            nontrivial_fiber_models += 1
                        if result['resource_distinguished_observation_fibers'] > 0:
                            models_with_resource_split += 1
                            if sample_resource_split is None:
                                sample_resource_split = {'transitions': [[q,lab,qq] for (q,lab),qq in sorted(d.items())],
                                    'a': a, 'b': b, 'periods': [pa,pb],
                                    'bits': result['minimum_extra_bits_by_rank'],
                                    'counts_by_rank': result['max_distinct_count_vectors_by_rank']}

                        if any(result['max_language_classes_by_rank'][k] > result['max_distinct_count_vectors_by_rank'][k]
                               for k in range(a+b+1)):
                            models_with_more_bits_than_count_only += 1

    assert controllers == 81 and models == 81 * 9 * 4
    return {
      'schema': 'X6_CONDITIONAL_RESOURCE_FUTURE_LANGUAGE_CHECK_V1',
      'result': 'PASS',
      'scope': 'deterministic partial 2-state resource automata and the 3-state alternating family; not native Cell permission',
      'signature_matches_full_word_languages': True,
      'two_state_controllers_exhaustively_checked': controllers,
      'two_state_length_pairs': 9,
      'two_state_period_pairs': [list(x) for x in period_pairs],
      'two_state_models_checked': models,
      'two_state_models_with_complete_trajectory': productive_models,
      'two_state_models_with_nontrivial_observation_fiber': nontrivial_fiber_models,
      'two_state_models_with_same_count_resource_split': models_with_resource_split,
      'two_state_models_with_larger_class_count_than_count_only': models_with_more_bits_than_count_only,
      'sample_two_state_same_count_resource_split': sample_resource_split,
      'alternating_port_family': examples,
    }

if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False))
