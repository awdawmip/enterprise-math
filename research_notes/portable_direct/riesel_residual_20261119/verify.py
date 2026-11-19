"""Exact Riesel phase-cover evidence using the pinned Enterprise Math BRC core.

The affine register is internal arithmetic state attached to an unchanged X6
cell. Its dimension is not a spatial-axis count; n is an exponent index.
This script makes no physical-dynamics or global Riesel-minimum claim.
Run in a full project checkout:
  python research_notes/portable_direct/riesel_residual_20261119/verify.py
For the connector-materialized source, pass --source-dir /path/to/vendor_src.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import isqrt, lcm, prod
from pathlib import Path
import sys

SOURCE_COMMIT = "b1efc6c805661ed7b476e6e730107da6043176ee"
SOURCE_BLOBS = {
    "brc_transport.py": "be1debe367263931bd5e93fd750be3ed54624fe1",
    "brc_histogram.py": "9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1",
    "brc_rational_holonomy.py": "2591640fe348da9cd7f293a957bea9ae92c82943",
    "brc_weighted_recurrent.py": "4e6b3132580e3cd70a20a0d8bd4d28792b961afb",
}
PRIMES = (3, 5, 7, 13, 17, 241)
ORDERS = (2, 4, 3, 12, 8, 24)
GOOD_PHASES = (0, 1, 2, 7, 7, 3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parents[3] / "src")
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits
    from enterprise_math.brc_rational_holonomy import rational_prime_valuations

    # This is a singleton BRC branch with exact weight 1, count 1 and its
    # full affine effect. No invented stochastic branching or mass collapse.
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    double = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (0,)), 1)])

    def advance(packet, x):
        outputs = packet.evaluate((x,))
        if len(outputs) != 1:
            raise AssertionError("deterministic support changed")
        (point, weights), = outputs.items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    def rem(x, modulus):
        return euclidean_digits(x, (modulus,))[1][0]

    def row(k, n, value):
        residues = tuple(rem(value, p) for p in PRIMES)
        return {"n": n, "value": str(value), "residues": residues,
                "hit_primes": [p for p, r in zip(PRIMES, residues) if r == 0]}

    def orbit(k):
        value = k - 1
        rows = []
        for n in range(25):
            rows.append(row(k, n, value))
            value = advance(step, value)
        assert rows[0]["residues"] == rows[24]["residues"]
        composed = EffectHistogram.unit(1)
        for _ in range(24):
            composed = composed.then(step)
        assert advance(composed, k - 1) == int(rows[24]["value"])
        for current, later in zip(rows, rows[1:]):
            assert tuple(rem(advance(step, r), p) for p, r in zip(PRIMES, current["residues"])) == later["residues"]
        return rows

    assert all(rational_prime_valuations(p) == ((p, 1),) for p in PRIMES)
    actual_orders = []
    for p in PRIMES:
        power = 1
        for order in range(1, p):
            power = advance(double, power)
            if rem(power, p) == 1:
                actual_orders.append(order)
                break
    assert tuple(actual_orders) == ORDERS
    period = lcm(*ORDERS)
    good, contrast = orbit(509203), orbit(184333)
    assert all(r["hit_primes"] for r in good[:period])
    assert [r["n"] for r in contrast[:period] if not r["hit_primes"]] == [3]
    assert all(int(r["value"]) > max(PRIMES) for r in good[1:])

    histograms_equal = []
    for j in range(len(PRIMES)):
        a = Counter(r["residues"][j] for r in good[:period])
        b = Counter(r["residues"][j] for r in contrast[:period])
        histograms_equal.append(a == b)
    assert all(histograms_equal)
    prime_witness = int(contrast[3]["value"])
    assert prime_witness == 1474663
    trial_bound = isqrt(prime_witness)
    trial_divisors = [d for d in range(2, trial_bound + 1) if rem(prime_witness, d) == 0]
    assert not trial_divisors
    assert rational_prime_valuations(prime_witness) == ((prime_witness, 1),)

    # Exhaust every active zero-phase assignment. The mask uses only exponent
    # congruence observations. Each assignment is realizable by CRT on k.
    masks = [[sum(1 << n for n in range(period) if rem(n, m) == a)
              for a in range(m)] for m in ORDERS]
    full = (1 << period) - 1
    covering_phases = []
    for phases in product(*(range(m) for m in ORDERS)):
        union = 0
        for j, a in enumerate(phases):
            union |= masks[j][a]
        if union == full:
            covering_phases.append(phases)
    assert len(covering_phases) == 48

    # Normalize the 241-channel phase to zero; its period is the full period.
    normalized = sorted({tuple(rem(a - phases[-1], m) for a, m in zip(phases, ORDERS))
                         for phases in covering_phases})
    assert len(normalized) == 2

    # CRT is an explicit integer reconstruction from already checked phase
    # congruences, not a separate propagator. Small inverse search is exhaustive.
    def inverse_mod(a, m):
        return next(x for x in range(1, m) if rem(a * x, m) == 1)

    def odd_k(phases):
        residues = []
        for a, p in zip(phases, PRIMES):
            power = 1
            for _ in range(a):
                power = advance(double, power)
            residues.append(inverse_mod(rem(power, p), p))
        x, modulus = 1, 2
        for a, p in zip(residues, PRIMES):
            delta = rem((a - x) * inverse_mod(rem(modulus, p), p), p)
            x += modulus * delta
            modulus *= p
        assert x % 2 == 1 and all(rem(x, p) == a for p, a in zip(PRIMES, residues))
        return x

    representatives = sorted((odd_k(phases), phases) for phases in covering_phases)
    assert representatives[0] == (509203, GOOD_PHASES)
    deletions = {str(p): [r["n"] for r in good[:period] if r["hit_primes"] == [p]] for p in PRIMES}
    assert all(deletions.values())
    first_five_holes = [r["n"] for r in good[:period] if not set(r["hit_primes"]).intersection(PRIMES[:-1])]
    assert first_five_holes == [3]
    independent_miss = prod((1 - Fraction(1, m) for m in ORDERS), start=Fraction(1))

    result = {
        "schema": "RIESEL_RESIDUAL_PHASE_EVIDENCE_V1",
        "researcher_id": "EM-DIRECT-970E1C",
        "proof_status": "AUTHOR_PROOF_AND_EXACT_FINITE_CHECK; NOT_PROJECT_REVIEWED",
        "source_commit": SOURCE_COMMIT,
        "source_blobs": SOURCE_BLOBS,
        "brc_entrypoints": ["EffectHistogram.from_terms", "EffectHistogram.evaluate", "EffectHistogram.then", "euclidean_digits", "rational_prime_valuations"],
        "carrier": "deterministic positive singleton affine effect on one internal integer register; unchanged X6 anchor",
        "observer_scope": "the six labelled residues and divisor support under every nonnegative repetition of x -> 2*x+1",
        "exponent_index_is_physical_heartbeat_time": False,
        "spatial_axes_identified_with_prime_channels": False,
        "primes": PRIMES, "orders": ORDERS, "period": period,
        "k_residues": {str(k): [rem(k, p) for p in PRIMES] for k in (509203, 184333)},
        "good": {"k": 509203, "phases": GOOD_PHASES, "orbit": good,
                 "coverage_count_histogram": dict(Counter(len(r["hit_primes"]) for r in good[:period]))},
        "contrast": {"k": 184333, "phases": [0, 1, 2, 7, 7, 7], "orbit": contrast,
                     "uncovered_phases": [3], "coverage_count_histogram": dict(Counter(len(r["hit_primes"]) for r in contrast[:period]))},
        "full_marginal_residue_histograms_equal": histograms_equal,
        "prime_witness": {"value": str(prime_witness), "k": 184333, "n": 3,
                          "trial_bound": trial_bound, "tested_all_integers_from_2": True,
                          "proper_divisors_in_trial_range": trial_divisors,
                          "canonical_valuation_result": [[prime_witness, 1]]},
        "deletion_holes_mod24": deletions,
        "first_five_holes_mod24": first_five_holes,
        "same_cover_odd_progression": {"initial": 509203, "step": 2 * prod(PRIMES), "t_domain": "nonnegative integers"},
        "active_phase_classification": {"population": prod(ORDERS), "covered": 48,
            "fraction": "1/1152", "phase_tuples": covering_phases,
            "global_shift_orbits": 2, "normalized_phase_representatives": normalized,
            "odd_modulus": 2 * prod(PRIMES),
            "odd_k_representatives": [{"k": k, "phases": phases} for k, phases in representatives],
            "minimum_scope": "only coverings supported by exactly this fixed prime set; not all Riesel numbers"},
        "independent_marginal_model_uncovered_fraction": str(independent_miss),
        "classical_universal_finite_cover_claim": "NOT_PROVED_OR_ASSUMED",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"result": str(args.output), "period": period,
                      "good_covered": 24, "contrast_covered": 23,
                      "prime_witness": prime_witness, "trial_bound": trial_bound,
                      "phase_assignments": prod(ORDERS), "full_covers": len(covering_phases),
                      "shift_classes": normalized, "minimum_in_fixed_cover_family": representatives[0][0]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
