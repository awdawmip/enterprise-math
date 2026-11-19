"""Exact CRT families with unbounded necessary finite-cover resources.

New author derivation for the fourth Riesel research continuation. This script
does not decide whether the constructed hard examples admit finite covers.
It checks finite obligations in the accompanying general proof, without
factorization of the large lcm integers or of the Riesel sequence values.

Native embedding: fixed X6 anchor, internal arithmetic registers, singleton
positive-weight BRC branch. Exponent is an arithmetic index, not physical time.

Run: python v4_family_work/verify_family.py --source-dir vendor_src
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import sys


def primes_through(bound: int) -> list[int]:
    """Exact finite sieve; no probabilistic primality tests."""
    if bound < 2:
        return []
    flags = bytearray(b"\x01") * (bound + 1)
    flags[0:2] = b"\x00\x00"
    for q in range(2, isqrt(bound) + 1):
        if flags[q]:
            flags[q*q:bound+1:q] = b"\x00" * ((bound-q*q)//q + 1)
    return [q for q in range(2, bound+1) if flags[q]]


def strip_known_primes(value: int, primes: list[int]):
    valuations = {}
    for p in primes:
        v = 0
        while value % p == 0:
            value //= p
            v += 1
        valuations[str(p)] = v
    return value, valuations


def digits(value: int) -> int:
    return len(str(value))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=Path("vendor_src"))
    parser.add_argument("--input", type=Path, default=Path(
        "research_notes/portable_direct/riesel_mixed_20261119/certificate.json"))
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("family_results.json"))
    parser.add_argument("--B", type=int, default=1000)
    parser.add_argument("--m", type=int, default=20)
    args = parser.parse_args()
    assert args.B >= 2 and args.m >= 1
    sys.set_int_max_str_digits(0)
    source_bytes = args.input.read_bytes()
    old = json.loads(source_bytes)["optimized"]
    a0 = int(old["a"])
    rows = old["rows"]
    P = [r["p"] for r in rows]
    assert len(P) == len(set(P)) == 20
    M = prod(P)
    modulus = 2*M
    assert 0 < a0 < modulus and a0 % 2 == 1 and a0 % 3 == 0
    assert gcd(a0, M) == 1 and modulus % 3 == 2
    assert all(all(p % d for d in range(2, isqrt(p)+1)) for p in P)
    period = lcm(*(r["order"] for r in rows))
    assert period == 6720

    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    double = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (0,)), 1)])

    def advance(packet, x):
        (point, weights), = packet.evaluate((x,)).items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    assert advance(step, -1) == -1
    sampled = EffectHistogram.unit(1)
    for _ in range(210):
        sampled = sampled.then(step)
    R = 2**210
    assert sampled.entries == ((Fraction(1), Affine(((R,),), (R-1,)), 1),)
    assert advance(sampled, -1) == -1

    # Exact prime orders and the complete old residual cycles.
    residual_cycles = {}
    for row in rows:
        p, d, phase = row["p"], row["order"], row["exponent_phase"]
        assert a0 % p == row["a_residue"]
        power = 1
        for order in range(1, d+1):
            power = advance(double, power) % p
            if power == 1:
                break
        assert power == 1 and order == d
        start = (a0*a0-1) % p
        cycle, x = [], start
        for _ in range(d):
            cycle.append(x)
            x = advance(step, x) % p
        assert x == start
        assert [i for i, x in enumerate(cycle) if x == 0] == [phase]
        residual_cycles[p] = cycle
    hits = [[p for p in P if residual_cycles[p][n % len(residual_cycles[p])] == 0]
            for n in range(period)]
    assert all(hits[n] for n in range(1, period, 2))
    H = [n for n in range(210) if not hits[n]]
    assert len(H) == 36 and all(n % 2 == 0 for n in H)
    # Riesel indices are positive. Residue zero denotes n=210, not n=0;
    # in particular N_a(0) is even whereas every positive-index N_a(n) is odd.
    positive_H_representatives = [n if n else 210 for n in H]
    assert 2 in H and all(bool(hits[n]) == (n % 210 not in H)
                          for n in range(period))
    # Proves the whole n=2+210v fibre is outside P by finite periodicity.
    fibre_period = lcm(*(r["order"] // gcd(r["order"], 210) for r in rows))
    assert all(not hits[(2+210*v) % period] for v in range(fibre_period))

    # No unknown factors are computed: strip only the twenty supplied primes.
    D = 1
    for j in range(1, args.m+1):
        D = lcm(D, pow(R, j)-1)
    T_order, removed = strip_known_primes(D, P)
    assert D == T_order * prod(p**removed[str(p)] for p in P)
    assert gcd(T_order, modulus) == 1
    small_primes = primes_through(args.B)
    extra_small = [q for q in small_primes if q != 2 and q not in P]
    U = prod(extra_small)
    assert gcd(U, modulus) == 1
    T = lcm(U, T_order)
    assert gcd(T, modulus) == 1
    t = (a0 * pow(T, -1, modulus)) % modulus
    assert 0 < t < modulus
    a = T*t
    assert a >= 3 and a % modulus == a0 and a % T == 0
    assert a % 2 == 1 and a % 3 == 0
    j_parameter = (a-a0)//modulus
    assert j_parameter >= 0 and a == a0+modulus*j_parameter

    order_exclusion_witnesses = []
    for j in range(1, args.m+1):
        stripped, valuations = strip_known_primes(pow(R, j)-1, P)
        assert T_order % stripped == 0 and a % stripped == 0
        order_exclusion_witnesses.append({
            "j": j, "R_to_j_minus_1_bit_length": (pow(R, j)-1).bit_length(),
            "P_stripped_part_bit_length": stripped.bit_length(),
            "P_stripped_part_divides_T_order_and_a": True,
            "removed_P_valuations": valuations})

    # Root congruence proves all P observations, not just hit flags, agree.
    for p in P:
        assert a % p == a0 % p
        assert (a*a-1) % p == residual_cycles[p][0]
    for q in extra_small:
        assert a % q == 0
        x0 = (a*a-1) % q
        assert x0 == q-1 and advance(step, x0) % q == q-1
        assert advance(sampled, x0) % q == q-1
    assert all((a*a*pow(2, n, q)-1) % q != 0
               for n in positive_H_representatives for q in small_primes)
    # n=2 is a certified composite surviving every prime <= B.
    N2 = 4*a*a-1
    left, right = 2*a-1, 2*a+1
    assert 1 < left < right < N2 and left*right == N2
    assert all(N2 % q for q in small_primes)

    # A finite witness for the cover-cardinality bound: m+1 consecutive
    # fibre terms are pairwise coprime. Shared-context mathematical check by
    # riesel_v4_phase_geometry supplied this direct proof in addition to density.
    window = [N2]
    for _ in range(args.m):
        window.append(advance(sampled, window[-1]))
    window_checks = []
    for v, value in enumerate(window):
        n = 2+210*v
        assert value == (a*a << n)-1
        factor = a << (n//2)
        assert (factor-1)*(factor+1) == value and 1 < factor-1 < value
        decimal = str(value)
        window_checks.append({"v": v, "n": n, "decimal_digits": len(decimal),
                              "decimal_sha256": sha256(decimal.encode()).hexdigest()})
    pair_count = 0
    for i in range(len(window)):
        for j in range(i+1, len(window)):
            assert gcd(window[i], window[j]) == 1
            pair_count += 1
    assert pair_count == args.m*(args.m+1)//2

    # A positive and a negative coverage certificate under the same old P state.
    # Include 3 explicitly so this contrast also holds for the allowed B=2.
    # For the main B=1000 example this equals P union {primes <= B}.
    Q = sorted(set(P) | set(small_primes) | {3})
    easy_a = a0+modulus
    assert easy_a % modulus == a % modulus and easy_a % 3 != 0
    assert 2*easy_a*easy_a-1 > max(P+[3])
    assert all(hits[n] or (easy_a*easy_a*pow(2, n, 3)-1) % 3 == 0
               for n in range(period))
    assert all((a*a*pow(2, n, q)-1) % q
               for n in positive_H_representatives for q in Q)
    comparison = []
    for residue in range(3):
        root = a0+modulus*residue
        mod3 = root % 3
        comparison.append({"root_parameter_j_mod3": residue, "a_mod3": mod3,
                           "P_union_3_fullcover": mod3 != 0})
    assert sum(c["P_union_3_fullcover"] for c in comparison) == 2

    # Small-to-large deterministic examples show constructive scale, not search.
    scale = []
    for m in [1, 2, 5, 10, 20]:
        Dm = 1
        for j in range(1, m+1):
            Dm = lcm(Dm, pow(R, j)-1)
        Tm, _ = strip_known_primes(Dm, P)
        combined = lcm(U, Tm)
        root = combined*((a0*pow(combined, -1, modulus)) % modulus)
        assert root % modulus == a0 and root % combined == 0
        scale.append({"B": args.B, "m": m, "a_decimal_digits": digits(root),
                      "k_decimal_digits": digits(root*root),
                      "T_decimal_digits": digits(combined),
                      "minimum_P_outside_primes_if_fullcover": m+1})

    result = {
        "schema": "enterprise-math.riesel-crt-family.v1",
        "researcher_id": "EM-DIRECT-970E1C",
        "research_activity_id": "RA-D2EC212845B63844081F9A14",
        "session_id": "LOCAL-RIESEL-a047cf12d55443c395589f6024246b16",
        "derivation_status": "new_this_round_author_proof_and_exact_computation",
        "not_claimed": ["literature novelty", "independent project Review",
                        "absence of every finite cover for any constructed root",
                        "one fixed root meeting all B and m"],
        "base_certificate_sha256": sha256(source_bytes).hexdigest(),
        "brc_module": "enterprise_math.brc_transport",
        "brc_source_commit": "b1efc6c805661ed7b476e6e730107da6043176ee",
        "B": args.B, "m": args.m,
        "a_star": str(a0), "P": P, "M": str(M), "two_M": str(modulus),
        "P_residual_period": period, "P_hole_period": 210,
        "P_holes_mod210": H, "P_hole_density": "6/35",
        "hole_fibre": {"n0": 2, "step": 210, "v_minimum": 0,
                       "finite_P_check_period_in_v": fibre_period},
        "R": str(R), "D_m": str(D), "D_m_removed_P_valuations": removed,
        "T_order": str(T_order), "U_B": str(U), "T_B_m": str(T),
        "crt_t": str(t), "a": str(a),
        "root_progression_step": str(modulus*T),
        "base_class_parameter_j": str(j_parameter),
        "a_decimal_digits": digits(a), "k_decimal_digits": digits(a*a),
        "D_m_decimal_digits": digits(D), "T_B_m_decimal_digits": digits(T),
        "primes_through_B_count": len(small_primes),
        "extra_small_primes_forced_to_minus_one": extra_small,
        "order_exclusion_witnesses": order_exclusion_witnesses,
        "finite_pairwise_coprime_witness": {
            "number_of_composite_terms": len(window),
            "all_pair_gcd_checks": pair_count, "all_pair_gcd_values": 1,
            "terms": window_checks,
            "general_proof_also_applies_to_every_sliding_window": True},
        "claims": {
            "same_all_future_P_residues_as_a_star": True,
            "all_positive_odd_n_covered_by_P": True,
            "all_positive_even_n_have_proper_square_difference_factors": True,
            "every_n_in_H_has_least_prime_factor_strictly_above_B": True,
            "B_at_least_max_P_so_survival_set_exactly_H": args.B >= max(P),
            "minimum_P_outside_primes_in_any_full_finite_cover": args.m+1,
            "minimum_total_if_P_is_retained": len(P)+args.m+1,
            "every_full_finite_cover_has_a_prime_strictly_above_B": True,
            "at_most_m_extra_primes_leave_fibre_density_at_least": f"1/{args.m+1}",
            "at_most_m_extra_primes_leave_density_relative_to_H_at_least": f"1/{args.m+1}",
            "at_most_m_extra_primes_leave_one_fibre_in_all_n_density_at_least": f"1/{210*(args.m+1)}",
            "at_most_m_extra_primes_leave_all_n_density_at_least": str(Fraction(len(H),210*(args.m+1))),
            "large_integer_factorization_used": False,
            "main_root_finite_cover_existence_decided": False},
        "BRC": {"arithmetic_step": "x -> 2x+1", "fixed_point": -1,
                "sampled_step": "x -> R*x+(R-1)",
                "branch_weight": "1", "branch_multiplicity": 1,
                "X6_anchor": "fixed; arithmetic registers internal",
                "exponent_is_physical_time": False},
        "same_observer_contrast": {
            "Q": Q, "Q_size": len(Q), "easy_a": str(easy_a),
            "easy_full_Q_cover": True, "hard_full_Q_cover": False,
            "hard_Q_holes_include_all_H": True,
            "root_parameter_mod3_table": comparison,
            "P_union_3_fullcover_relative_density": "2/3"},
        "scale_table": scale,
        "all_assertions_passed": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "B": args.B, "m": args.m,
                      "a_digits": digits(a), "k_digits": digits(a*a),
                      "T_digits": digits(T), "Q_size": len(Q),
                      "minimum_outside_P": args.m+1,
                      "all_assertions_passed": True,
                      "scale_table": scale}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
