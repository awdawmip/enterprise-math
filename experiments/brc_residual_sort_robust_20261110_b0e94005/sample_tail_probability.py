#!/usr/bin/env python3
"""Exact finite-population rank-tail probabilities under an ideal uniform shuffle.

This is a model of which sample endpoints survive a fixed trim, not a prediction
of total running time or a correctness assumption. All actual inputs are checked.
"""
from decimal import Decimal, localcontext
import json
from math import comb
from pathlib import Path


def endpoint_survival_probability(n, sample, cut, low_tails, high_tails):
    """P(at least one sample tail population exceeds the per-side trim cut)."""
    ordinary = n - low_tails - high_tails
    denominator = comb(n, sample)
    both_removed = 0
    for low in range(min(cut, low_tails, sample) + 1):
        for high in range(min(cut, high_tails, sample - low) + 1):
            middle = sample - low - high
            if 0 <= middle <= ordinary:
                both_removed += comb(low_tails, low) * comb(high_tails, high) * comb(ordinary, middle)
    numerator = denominator - both_removed
    with localcontext() as context:
        context.prec = 60
        probability = str(Decimal(numerator) / Decimal(denominator))
    return probability


def main():
    n, sample, cut = 100_000, 1024, 16
    cases = [
        ("one_sided_0p01pct", 0, 10),
        ("two_sided_0p3pct", 150, 150),
        ("one_sided_1pct", 0, 1000),
        ("one_sided_2pct", 0, 2000),
        ("two_sided_5pct", 2500, 2500),
    ]
    rows = [dict(name=name, n=n, sample=sample, cut_each_side=cut,
                 low_tail_occurrences=low, high_tail_occurrences=high,
                 probability_a_trim_endpoint_remains_in_a_tail=
                    endpoint_survival_probability(n, sample, cut, low, high))
            for name, low, high in cases]
    result = {
        "model": "Ideal uniform permutation of a population with fixed tail multiplicities; a fixed set of distinct sample positions. Joint multivariate hypergeometric counts, with exact integer binomial coefficients.",
        "event": "A lower or upper selected rank remains in a tail because that sampled side has at least17 observations. This does not itself prove every layout rejects, or that removal guarantees counting success; the geometric conditions in THEORY.md remain necessary for the positive family.",
        "not_used_for_tuning": True,
        "cases": rows,
    }
    out = Path(__file__).with_name("sampling_probabilities.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
