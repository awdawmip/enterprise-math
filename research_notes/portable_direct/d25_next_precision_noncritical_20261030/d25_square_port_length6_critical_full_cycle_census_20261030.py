#!/usr/bin/env python3
"""Author-only exact finite critical fiber census (p=3/5, e=2, L=6).

Enumerates every integer source and every actual time in its verified state cycle;
uses exact pairwise label refinement, not a lossy hash as a proof of equivalence.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

CONFIGS = [(3, 2), (3, 4), (3, 10), (5, 2), (5, 6), (5, 26)]
E = 2
L = 2 * E + 2
OUT = Path(__file__).with_name(
    "d25_square_port_length6_critical_full_cycle_census_author_check_20261030.json"
)


def full_permutation_cycles(transition, sources):
    unseen = set(sources)
    spectrum = Counter()
    while unseen:
        initial = min(unseen)
        x = initial
        length = 0
        while x in unseen:
            unseen.remove(x)
            length += 1
            x = transition[x]
        assert x == initial, (initial, x)
        spectrum[length] += 1
    return dict(sorted(spectrum.items()))


def class_histogram(labels):
    source_count = Counter(labels)
    return dict(sorted(Counter(source_count.values()).items()))


def census(p, d):
    modulus = p**L
    h = p**E
    critical = [x for x in range(1, modulus) if x % p in (1, p - 1)]
    transition = {x: (x + h * pow(x, d, modulus)) % modulus for x in critical}
    assert len(set(transition.values())) == len(critical)
    assert set(transition.values()) == set(critical)
    cycles = full_permutation_cycles(transition, critical)
    complete_period = max(cycles)
    assert complete_period == p ** (L - E)
    assert all(complete_period % cycle_length == 0 for cycle_length in cycles)
    # Precompute actual two-factor observer, never quotient away labels.
    observation = {
        x: ((x + 1) * (pow(x, -1, modulus) + 1)) % modulus for x in critical
    }
    positions = list(critical)
    labels = [None] * len(critical)
    checkpoints = {}
    for t in range(complete_period):
        new_class = {}
        new_labels = []
        for old_label, source_state in zip(labels, positions):
            key = (old_label, observation[source_state])
            if key not in new_class:
                new_class[key] = len(new_class)
            new_labels.append(new_class[key])
        labels = new_labels
        if t in (0, 1, 2, complete_period - 1):
            checkpoints[str(t)] = {
                "class_count": len(set(labels)),
                "fiber_histogram": {str(k): v for k, v in class_histogram(labels).items()},
            }
        if t < complete_period - 1:
            positions = [transition[x] for x in positions]
    expected = {
        p**v: 2 * (p - 1) * p ** (2 * E + 1 - 2 * v)
        for v in range(1, E)
    }
    expected[p**E] = 2 * p * p
    histogram = class_histogram(labels)
    assert histogram == expected, (p, d, histogram, expected)
    assert class_histogram_at(checkpoints, "1") == expected
    assert class_histogram_at(checkpoints, "2") == expected
    examples = defaultdict(list)
    for source, label in zip(critical, labels):
        if len(examples[label]) < 3:
            examples[label].append(source)
    multi_sample = next((values for values in examples.values() if len(values) > 1), [])
    return {
        "p": p,
        "e": E,
        "L": L,
        "degree": d,
        "lambda": 1,
        "modulus": modulus,
        "critical_labeled_sources": len(critical),
        "permutation_cycle_length_spectrum": {str(k): v for k, v in cycles.items()},
        "all_time_period": complete_period,
        "checkpoints": checkpoints,
        "complete_future_fiber_histogram": {str(k): v for k, v in histogram.items()},
        "persistent_sample_labeled_sources": multi_sample,
        "observer_product_evaluations": len(critical) * complete_period,
        "state_updates": len(critical) * (complete_period - 1),
        "status": "PASS",
    }


def class_histogram_at(checkpoints, time):
    return {int(k): v for k, v in checkpoints[time]["fiber_histogram"].items()}


def main():
    records = [census(p, d) for p, d in CONFIGS]
    doc = {
        "scope": "exact complete critical-unit domain p=3 or 5, e=2, L=6, even degrees",
        "general_prime_theorem_proved_in_companion_markdown": True,
        "general_prime_theorem_formally_verified": False,
        "native_X6_experiment": False,
        "method": "exhaustive exact labeled state-cycle enumeration and all-time output partition; no hash equivalence shortcuts",
        "configurations": records,
        "totals": {
            "critical_labeled_sources": sum(x["critical_labeled_sources"] for x in records),
            "observer_product_evaluations": sum(x["observer_product_evaluations"] for x in records),
            "state_updates": sum(x["state_updates"] for x in records),
        },
        "result": "PASS",
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "result": doc["result"],
        "histograms": {f"p={x['p']},d={x['degree']}": x["complete_future_fiber_histogram"] for x in records},
        "totals": doc["totals"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
