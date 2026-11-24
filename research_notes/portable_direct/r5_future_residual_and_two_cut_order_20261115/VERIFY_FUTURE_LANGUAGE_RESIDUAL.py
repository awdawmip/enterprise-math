#!/usr/bin/env python3
"""Finite exact checks for a suffix-language observer of old optimal paths.
Pure finite path-language mathematics: no claim to have rerun frozen R5 data.
"""
from itertools import combinations
from random import Random
import json

NEG = -10**9

def subsets(items):
    return [frozenset(c) for r in range(len(items) + 1)
            for c in combinations(items, r)]

def response(langs, scores, new_suffix):
    return max((score + max(len(new_suffix & old) for old in lang)
                for lang, score in zip(langs, scores) if score != NEG), default=NEG)

def quotient(langs, scores):
    classes = {}
    for language, score in zip(langs, scores):
        key = frozenset(language)
        classes[key] = max(classes.get(key, NEG), score)
    return [list(k) for k in classes], list(classes.values())

def inclusion_certificate(langs, u, v):
    return all(any(score <= right_score and left_lang <= right_lang
                   for right_lang, right_score in zip(langs, v))
               for left_lang, score in zip(langs, u) if score != NEG)

def run():
    universe = tuple(range(4)); allsets = subsets(universe)
    rng = Random(20261115)
    quotient_checks = inclusion_checks = 0
    for _ in range(3000):
        n = rng.randrange(2, 7)
        languages = [frozenset(rng.sample(allsets, rng.randrange(1, 5))) for _ in range(n)]
        v = tuple(rng.choice([NEG, 0, 1, 2, 3]) for _ in range(n))
        qlang, qscore = quotient(languages, v)
        for S in allsets:
            assert response(languages, v, S) == response(qlang, qscore, S)
            quotient_checks += 1
        u = tuple(rng.choice([NEG, 0, 1, 2, 3]) for _ in range(n))
        if inclusion_certificate(languages, u, v):
            for S in allsets:
                assert response(languages, u, S) <= response(languages, v, S)
                inclusion_checks += 1

    L = (frozenset((frozenset((1,)), frozenset((2,)))),) * 2
    a, b = (1, 0), (0, 1)
    assert not all(x <= y for x, y in zip(a, b))
    assert not all(x <= y for x, y in zip(b, a))
    assert all(response(L, a, S) == response(L, b, S) for S in allsets)

    La = (frozenset((frozenset((1,)),)),
          frozenset((frozenset((1,)), frozenset((2,)))))
    u, v = (1, 0), (0, 1)
    assert inclusion_certificate(La, u, v)
    assert response(La, u, frozenset((2,))) == 1
    assert response(La, v, frozenset((2,))) == 2
    assert all(response(La, u, S) <= response(La, v, S) for S in allsets)

    print(json.dumps({'status': 'PASS_FUTURE_LANGUAGE_RESIDUAL_OBSERVER',
                      'random_language_and_vector_trials': 3000,
                      'suffix_masks_per_trial': len(allsets),
                      'exact_quotient_comparisons': quotient_checks,
                      'certified_inclusion_response_comparisons': inclusion_checks,
                      'strict_equivalence_witness': {'frontier_width': 2, 'future_classes': 1,
                                                     'vectors': [a, b]},
                      'strict_inclusion_witness': {'u': u, 'v': v,
                                                   'new_suffix': [2], 'response_u': 1,'response_v': 2},
                      'scope': 'all finite suffix-language systems in proof; toy audit exhaustive over 4-bit suffix masks',
                      'r5_full_instance_replayed': False}, indent=2))

if __name__ == '__main__':
    run()
