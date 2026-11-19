"""Exact mixed Riesel certificates and a certified squaring counterexample.

The shared 20 divisors are proved prime by full trial division. Their exact
orders and both residual cycles use the pinned Enterprise Math BRC transport.
Each covering is exhaustively checked on its proved period 0 <= n < 6720.
Period representatives include n=0, while Riesel exponents are positive.
The even-exponent conclusion uses an algebraic identity and true-factor bounds.
The counterexample prime uses a complete-factorization Lucas certificate.

The native embedding keeps an arbitrary X6 anchor fixed and attaches internal
arithmetic registers. Prime channels are observations, not spatial axes; the
exponent counts arithmetic updates, not physical heartbeat time. The fixed
prime observer is exact for every repetition of x -> 2*x+1. Observing the
square structure or changing k by squaring it requires additional information.

This is author proof and exact computation, not independent project Review,
formal verification, global-minimum evidence or Foundation promotion.

Run in the repository:
  python research_notes/portable_direct/riesel_mixed_20261119/verify.py
For the materialized source:
  python research_notes/portable_direct/riesel_mixed_20261119/verify.py --source-dir vendor_src
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parents[3] / "src")
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("certificate.json"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits

    # Single deterministic branches with full affine effect, weight 1 and
    # multiplicity 1. Exact integers/Fractions only; no stochastic surrogate.
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    double = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (0,)), 1)])

    def advance(packet, x):
        outputs = packet.evaluate((x,))
        (point, weights), = outputs.items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    def rem(x, modulus):
        return euclidean_digits(x, (modulus,))[1][0]

    prime_evidence = {}

    def prove_small_prime(p):
        if p not in prime_evidence:
            assert p >= 2
            bound = isqrt(p)
            assert all(rem(p, q) for q in range(2, bound + 1))
            prime_evidence[p] = {"prime": p, "method": "full_integer_trial_division",
                                 "trial_division_bound": bound,
                                 "all_divisors_from_2_through_bound_checked": True}
        return prime_evidence[p]

    original_rows = data["original"]["rows"]
    optimized_rows = data["optimized"]["rows"]
    assert len(original_rows) == len(optimized_rows) == 20
    assert [(r["p"], r["order"]) for r in original_rows] == [
        (r["p"], r["order"]) for r in optimized_rows]
    primes = [row["p"] for row in original_rows]
    assert len(set(primes)) == 20
    period = lcm(*(row["order"] for row in original_rows))
    assert period == 6720

    # Shared mathematical obligations are checked once for both examples.
    shared_channels = []
    for row in original_rows:
        p, d = row["p"], row["order"]
        assert p > 2
        proof = prove_small_prime(p)
        power = 1
        for actual_order in range(1, d + 1):
            power = rem(advance(double, power), p)
            if power == 1:
                break
        assert actual_order == d and power == 1
        shared_channels.append({"p": p, "order": actual_order,
                                "order_method": "BRC doubling; first return to 1",
                                "primality": proof})

    shift = data["optimized"]["exponent_shift"]
    assert shift % 2 == 0
    for old, new in zip(original_rows, optimized_rows):
        assert new["exponent_phase"] == (old["exponent_phase"] + shift) % old["order"]

    def verify_root(example, expected_first_positive_hole):
        a = int(example["a"])
        k = a * a
        table = example["rows"]
        assert a > 1 and a % 2 == 1
        cycles = {}
        checked_rows = []
        for row in table:
            p, d, phase, root_residue = (row[name] for name in
                                        ("p", "order", "exponent_phase", "a_residue"))
            assert rem(a, p) == root_residue and 0 < root_residue < p
            current = rem(k - 1, p)
            cycle = []
            for _ in range(d):
                cycle.append(current)
                current = rem(advance(step, current), p)
            assert current == cycle[0]
            assert [n for n, value in enumerate(cycle) if value == 0] == [phase]
            cycles[p] = cycle
            checked_rows.append(dict(row, residual_cycle=cycle,
                                     cycle_closed=True, unique_zero_phase=phase))

        hits = [[row["p"] for row in table
                 if cycles[row["p"]][n % row["order"]] == 0]
                for n in range(period)]
        assert all(hits[n] for n in range(1, period, 2))
        holes = [n for n, hit in enumerate(hits) if not hit]
        assert len(holes) == 1152 and all(n % 2 == 0 for n in holes)
        assert sum(bool(hits[n]) for n in range(0, period, 2)) == 2208
        first_hole = min(n for n in holes if n > 0)
        assert first_hole == expected_first_positive_hole
        assert 2 * k - 1 > max(primes)

        witnesses = []
        for p in primes:
            unique = [n for n in range(1, period, 2) if hits[n] == [p]]
            assert unique
            witnesses.append({"p": p, "least_odd_exclusive_phase": min(unique),
                              "odd_exclusive_count": len(unique)})

        odd_order_rows = [row for row in table if row["order"] % 2]
        assert all(row["exponent_phase"] % 2 for row in table if row["order"] % 2 == 0)
        assert lcm(*(row["order"] for row in odd_order_rows)) == 105
        even_holes_mod210 = [n for n in range(0, 210, 2)
                             if not any(n % row["order"] == row["exponent_phase"]
                                        for row in odd_order_rows)]
        assert len(even_holes_mod210) == 36
        assert holes == [n for n in range(period) if n % 210 in even_holes_mod210]

        root, modulus = 1, 2
        for row in table:
            p, residue = row["p"], row["a_residue"]
            root += modulus * (((residue - root) * pow(modulus, -1, p)) % p)
            modulus *= p
        assert root == a and modulus == 2 * prod(primes)

        b = a
        for _ in range(first_hole // 2):
            b = advance(double, b)
        left, right = b - 1, b + 1
        value = k - 1
        for _ in range(first_hole):
            value = advance(step, value)
        assert value == left * right and 1 < left < right < value
        first_residues = {str(row["p"]): cycles[row["p"]][first_hole % row["order"]]
                          for row in table}
        assert all(first_residues.values())

        # The original phase conditions persist for a_t=a+modulus*t. At
        # t classes giving 3 nondividing a_t, 3 covers every even exponent.
        assert modulus % 3 != 0
        extension_classes = []
        for t in range(3):
            a_t = a + modulus * t
            residue0 = rem(a_t * a_t - 1, 3)
            residue1 = rem(advance(step, residue0), 3)
            residue2 = rem(advance(step, residue1), 3)
            assert residue2 == residue0
            extend_by_3 = a_t % 3 != 0
            assert (residue0 == 0) == extend_by_3
            if extend_by_3:
                assert all(hits[n] or n % 2 == 0 for n in range(period))
            extension_classes.append({"parameter_t_mod3": t, "a_t_mod3": a_t % 3,
                                      "N_even_mod3": residue0,
                                      "P_union_3_is_full_finite_cover": extend_by_3})
        assert sum(row["P_union_3_is_full_finite_cover"] for row in extension_classes) == 2

        return {
            "a": str(a), "k": str(k), "period": period,
            "source_url": example["source_url"], "source_table": example["source_table"],
            "checked_rows": checked_rows,
            "coverage": {"odd_total": 3360, "odd_covered": 3360,
                         "even_total": 3360, "even_covered": 2208,
                         "all_total": period, "all_covered": period - len(holes),
                         "uncovered": len(holes), "uncovered_density": "6/35",
                         "coverage_count_histogram": dict(Counter(map(len, hits))),
                         "odd_coverage_count_histogram": dict(Counter(len(hits[n]) for n in range(1, period, 2)))},
            "odd_cover_irredundancy": witnesses,
            "even_holes_mod210": even_holes_mod210,
            "uncovered_phases_mod6720": holes,
            "phase_zero_is_hole": 0 in holes,
            "phase_zero_semantics": "representative for positive exponents 6720, 13440, ...; n=0 is not a required Riesel exponent",
            "proper_fixed_factor_bound": {"minimum_n": 1, "minimum_value": str(2*k-1),
                                         "largest_fixed_prime": max(primes)},
            "first_positive_fixed_prime_hole": {
                "n": first_hole, "value": str(value),
                "left_factor": str(left), "right_factor": str(right),
                "residues_mod_fixed_primes": first_residues},
            "root_progression": {"initial": str(a), "step": str(modulus),
                                 "parameter_domain": "t>=0 integer",
                                 "initial_mod3": a % 3, "step_mod3": modulus % 3},
            "infinite_riesel_family": "k=(initial+step*t)^2 for every nonnegative integer t",
            "extension_by_prime_3": extension_classes,
        }

    original = verify_root(data["original"], 4)
    optimized = verify_root(data["optimized"], 2)

    counter = data["squaring_counterexample"]
    riesel_base = counter["riesel_base"]
    coefficient = int(counter["coefficient"])
    exponent = counter["exponent"]
    value = int(counter["prime_value"])
    assert coefficient == riesel_base * riesel_base
    computed = coefficient - 1
    for _ in range(exponent):
        computed = advance(step, computed)
    assert computed == value == coefficient * 2**exponent - 1
    factors = counter["prime_factors_of_value_minus_one"]
    assert len(factors) == len(set(factors)) and prod(factors) == value - 1
    factor_proofs = [prove_small_prime(q) for q in factors]
    base = counter["lucas_base"]
    assert gcd(base, value) == 1
    fermat_residue = pow(base, value - 1, value)
    assert fermat_residue == 1
    lucas_rows = []
    for q in factors:
        reduced_exponent = (value - 1) // q
        residue = pow(base, reduced_exponent, value)
        common_divisor = gcd(residue - 1, value)
        assert common_divisor == 1
        lucas_rows.append({"q": q, "exponent": str(reduced_exponent),
                           "power_residue": str(residue), "gcd_residue_minus_1_with_N": common_divisor})
    lucas_certificate = {
        "riesel_base": riesel_base, "coefficient": str(coefficient), "n": exponent,
        "N": str(value), "N_minus_one": str(value - 1),
        "complete_factorization": [{"prime": q, "exponent": 1} for q in factors],
        "factor_primality_proofs": factor_proofs,
        "base": base, "base_gcd_with_N": gcd(base, value),
        "base_power_N_minus_1_mod_N": fermat_residue,
        "lucas_checks": lucas_rows,
        "conclusion": "N is prime by the complete-factorization Lucas criterion",
        "proof_argument": "For each prime divisor r of N, the checks force ord_r(base)=N-1. Hence N-1 divides r-1 and r>=N, so r=N and N is prime.",
        "scope": "509203 is Riesel by the separately established 6-prime certificate; its square is not Riesel because n=29 gives this prime.",
    }

    result = {
        "schema": "RIESEL_MIXED_CERTIFICATE_RESULTS_V1",
        "researcher_id": data["researcher_id"],
        "research_activity_id": data["research_activity_id"],
        "status": "AUTHOR_PROOF_AND_EXACT_FINITE_CHECK; NOT_INDEPENDENT_PROJECT_REVIEW",
        "project_source_commit": data["project_source_commit"],
        "project_source_blobs": data["project_source_blobs"],
        "brc_entrypoints": ["EffectHistogram.from_terms", "EffectHistogram.evaluate", "euclidean_digits"],
        "arithmetic_semantics": "integer/Fraction exact arithmetic; no probabilistic primality, floating-point inference or approximate covering",
        "native_carrier": "fixed arbitrary X6 anchor with internal arithmetic registers; spatial axes are unchanged",
        "observer_and_horizon": {
            "fixed_prime_observer": "joint labelled residues mod the 20 specified primes",
            "future_family": "all nonnegative repetitions of x -> 2*x+1",
            "finite_check_domain": "0<=n<6720 with proved per-channel periodicity",
            "algebraic_observer": "retain k=a^2, a, exponent parity and factor-size lower bounds",
            "coefficient_squaring": "an additional operation, outside the fixed-k affine future family",
            "exponent_is_physical_heartbeat_time": False,
            "prime_channels_are_spatial_axes": False,
        },
        "shared_channel_proofs": shared_channels,
        "exponent_translation": {"shift": shift, "even": True, "all_phases_verified": True},
        "original": original,
        "optimized": optimized,
        "algebraic_rule": {
            "domain": "n=2u, integers u>=1; a>1 odd",
            "identity": "a^2*2^(2u)-1=(a*2^u-1)*(a*2^u+1)",
            "lower_factor_bound": "a*2^u-1>=2a-1>1",
            "universal_argument": "polynomial identity and positive factor bounds, not finite sampling",
        },
        "squaring_counterexample": lucas_certificate,
        "finite_cover_boundary": "Each given 20-prime list has 1152 even-phase holes; this does not prove absence of another finite prime covering.",
        "minimum_scope": "The minimization claim is verified separately by minimize.py; this verifier establishes both exact mixed certificates and the squaring counterexample.",
        "paper_boundary": "Theorem 4 proves the original Riesel property; the following paragraph treats absence of a finite prime cover as belief, not theorem.",
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output.resolve()), "period": period,
                      "original": {"odd_covered": 3360, "even_covered": 2208, "holes": 1152, "first_positive_hole": 4},
                      "optimized": {"odd_covered": 3360, "even_covered": 2208, "holes": 1152, "first_positive_hole": 2},
                      "irredundant_odd_channels_each": 20,
                      "counterexample_prime": str(value), "lucas_base": base,
                      "lucas_factor_checks": len(lucas_rows),
                      "all_shared_primes_and_lucas_factors_proved_by_trial_division": True}, ensure_ascii=False))


if __name__ == "__main__":
    main()
