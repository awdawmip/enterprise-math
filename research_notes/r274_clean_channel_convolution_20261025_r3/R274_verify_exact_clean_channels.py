#!/usr/bin/env python3
"""R274 author-side: exact positive ordered affine BRC clean-channel identities.

This is the fixed R268--R273 auxiliary six-channel automaton, not P000 dynamics.
Requires only Python standard library. The mathematical proof is the suffix
partition; finite checks here inspect that proof's implementation and data.
"""
from collections import defaultdict
from pathlib import Path
import json

STEPS = {0: ((2, -1, -1), (2, +1, -1)),
         1: ((0, -1, -1), (0, +1, -1)),
         2: ((1, +1, +1), (2, +1, -1))}
CHANNELS = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1))
MAX_DEPTH = 400


def step(state, letter):
    q, r, eps, k = state
    q2, eta, b = STEPS[q][letter]
    r2 = 2 if r == 2 or (r == 1 and letter == 0) else (1 if letter == 0 else 0)
    return q2, r2, eta * eps, eta * k + b


def push(hist, suffix):
    """Right-compose one fixed affine effect (eta,b), preserving integer counts."""
    eta, b = suffix
    out = defaultdict(int)
    for (eps, k), multiplicity in hist.items():
        out[(eta * eps, eta * k + b)] += multiplicity
    return out


def clean_histograms(full):
    h = [defaultdict(int) for _ in range(3)]
    for (q, r, eps, k), count in full.items():
        if r != 2:
            h[q][(eps, k)] += count
    return h


def all_equal(actual, predicted):
    keys = set(actual) | set(predicted)
    return all(actual.get(k, 0) == predicted.get(k, 0) for k in keys)


def raw_enumeration(depth):
    hist = defaultdict(int)
    for x in range(1 << depth):
        state = (0, 0, 1, 0)
        for shift in range(depth - 1, -1, -1):
            state = step(state, (x >> shift) & 1)
        hist[state] += 1
    return hist


def main():
    full = {(0, 0, 1, 0): 1}
    previous_resets = []
    previous_q2 = {}
    bruteforce_count = 0
    identities_checked = 0
    q1_pointwise_checked = 0
    q2_recursions_checked = 0
    q2_pointwise_observations = []
    exact_peaks = {}
    for n in range(MAX_DEPTH + 1):
        assert sum(full.values()) == (1 << n)
        if n <= 12:
            assert dict(full) == dict(raw_enumeration(n))
            bruteforce_count += 1 << n
        p, q1, q2 = clean_histograms(full)
        previous_resets.append(p)
        if n >= 1:
            prediction = defaultdict(int, p)
            if n >= 2:
                for g, c in previous_resets[n - 2].items():
                    prediction[g] += c
            if n >= 3:
                for g, c in push(previous_resets[n - 3], (-1, -1)).items():
                    prediction[g] += c
            assert all_equal(q1, prediction), ('q1 decomposition', n)
            identities_checked += 1
            for g, c in p.items():
                assert q1.get(g, 0) >= c, ('q1 domination', n, g)
                q1_pointwise_checked += 1
            q2_prediction = push(previous_q2, (+1, -1))
            for suffix in ((-1, -1), (+1, -1)):
                for g, c in push(previous_resets[n - 1], suffix).items():
                    q2_prediction[g] += c
            assert all_equal(q2, q2_prediction), ('q2 recurrence', n)
            q2_recursions_checked += 1
        failures = [(g, c, q2.get(g, 0)) for g, c in p.items() if c > q2.get(g, 0)]
        if failures:
            q2_pointwise_observations.append((n, len(failures)))
        if n in (7, 11, 12, 50, 150, 300, 400):
            lam = max(p.values(), default=0)
            by_g = defaultdict(lambda: [0] * 6)
            for (q, r, eps, k), c in full.items():
                by_g[(eps, k)][CHANNELS.index((q, int(r == 2)))] += c
            bval = max((min(v) for v in by_g.values()), default=0)
            exact_peaks[str(n)] = {'Lambda': str(lam), 'B': str(bval)}
        previous_q2 = q2
        if n != MAX_DEPTH:
            nxt = defaultdict(int)
            for state, c in full.items():
                for a in (0, 1):
                    nxt[step(state, a)] += c
            full = nxt
    evidence = {
        'schema': 'EM_R274_CLEAN_CHANNEL_CONVOLUTION_EVIDENCE_V1',
        'status': 'PASS',
        'model': 'R268_R273_POSITIVE_ORDERED_AFFINE_BRC_AUXILIARY',
        'depth_max': MAX_DEPTH,
        'lengths_checked': MAX_DEPTH + 1,
        'independent_raw_words_checked': bruteforce_count,
        'exact_q1_fibre_identities_checked': identities_checked,
        'exact_q2_fibre_recursions_checked': q2_recursions_checked,
        'q1_pointwise_comparisons_checked': q1_pointwise_checked,
        'q2_domination_counterexample_depths_up_to_400': q2_pointwise_observations,
        'peak_anchors': exact_peaks,
        'universal_proof_basis': 'disjoint exhaustive suffix classes preserving full affine effect and positive path multiplicities',
        'finite_computation_is_universal_proof': False,
        'native_P000_dynamics_executed': False,
        'formal_research_claim_obtained': False,
        'independent_driver_reviewed': False
    }
    outfile = Path(__file__).with_name('EXACT_EVIDENCE.json')
    outfile.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: evidence[k] for k in ('status', 'depth_max', 'independent_raw_words_checked', 'exact_q1_fibre_identities_checked', 'exact_q2_fibre_recursions_checked', 'q1_pointwise_comparisons_checked', 'q2_domination_counterexample_depths_up_to_400', 'peak_anchors')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
