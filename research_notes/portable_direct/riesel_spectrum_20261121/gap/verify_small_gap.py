#!/usr/bin/env python3
"""Exact arithmetic evidence for the analytic sharp four-channel theorem.

The infinite-order claim is proved in proof.md. This verifier checks all finite
incidence, factorization, rational-bound, CRT and periodic-example inputs.
The arithmetic proof inputs use Python integers and Fraction, with complete
trial division for the few small factorizations and primality checks. The
numerical example also uses the four pinned native BRC modules. There is no
cutoff on arbitrary prime channels in the mathematical argument.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from fractions import Fraction
from hashlib import sha1
from math import gcd, lcm, prod
from pathlib import Path


A_STAR = 690786768637635218740714348513373826260012289
P = [7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281, 337,
     641, 673, 1321, 14449, 29191, 65537, 6700417]
H = [0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45, 48, 49,
     51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78, 79, 84, 85,
     90, 91, 93, 96, 99, 100]
M = prod(P)
G = [1, 3, 5, 7, 15, 21, 35, 105]
ROWS = [(5, 2, 1), (13, 6, 0), (11, 5, 0), (61, 30, 16), (331, 15, 4)]
NATIVE_COMMIT = "b1efc6c805661ed7b476e6e730107da6043176ee"
NATIVE_BLOBS = {
    "brc_transport.py": "be1debe367263931bd5e93fd750be3ed54624fe1",
    "brc_histogram.py": "9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1",
    "brc_rational_holonomy.py": "2591640fe348da9cd7f293a957bea9ae92c82943",
    "brc_weighted_recurrent.py": "4e6b3132580e3cd70a20a0d8bd4d28792b961afb",
}


def locate_native_source() -> Path:
    here = Path(__file__).resolve().parent
    for ancestor in (here, *here.parents):
        for directory in ("src", "vendor_src"):
            candidate = ancestor / directory
            if (candidate / "enterprise_math/brc_transport.py").is_file():
                return candidate
    raise FileNotFoundError("Supply --source-dir containing the four pinned enterprise_math modules")


def load_native(source_dir: Path):
    checks = {}
    for filename, expected in NATIVE_BLOBS.items():
        data = (source_dir / "enterprise_math" / filename).read_bytes()
        observed = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert observed == expected, (filename, expected, observed)
        checks[filename] = {"expected_git_blob": expected, "observed_git_blob": observed}
    sys.path.insert(0, str(source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    twice = step.then(step)
    assert twice.entries == ((Fraction(1), Affine(((4,),), (3,)), 1),)

    def advance(value: int) -> int:
        (point, weights), = step.evaluate((value,)).items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    return advance, euclidean_digits, checks


def factor_small(n: int) -> dict[int, int]:
    """Complete trial division, used only at this certificate's small inputs."""
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def order(b: int, q: int) -> int:
    assert gcd(b, q) == 1
    e, r = 1, b % q
    while r != 1:
        e += 1
        r = r * b % q
    return e


def crt(residues: list[int], moduli: list[int]) -> tuple[int, int]:
    x, current_modulus = 0, 1
    for residue, modulus in zip(residues, moduli, strict=True):
        assert gcd(current_modulus, modulus) == 1
        t = (residue - x) * pow(current_modulus, -1, modulus) % modulus
        x += current_modulus * t
        current_modulus *= modulus
    return x, current_modulus


def frac(x: Fraction | int) -> str:
    return str(Fraction(x))


def verify(source_dir: Path | None = None) -> dict:
    assert M == 1397394912916194098609132326092145093313722687204526281
    assert len(H) == len(set(H)) == 36
    assert sorted(g for g in range(1, 106) if 105 % g == 0) == G
    h_set = set(H)
    maxima = {g: max(Counter(h % g for h in H).values()) for g in G}
    assert list(maxima.values()) == [36, 23, 11, 7, 6, 4, 2, 1]

    small_factors = {j: factor_small(4**j - 1) for j in range(1, 7)}
    all_small = set().union(*(set(f) for f in small_factors.values()))
    assert all_small == {3, 5, 7, 11, 13, 17, 31}
    assert all_small <= set(P) | {3, 5, 11, 13}
    factor_24 = factor_small(2**24 - 1)
    assert factor_24 == {3: 2, 5: 1, 7: 1, 13: 1, 17: 1, 241: 1}
    assert prod(q**e for q, e in factor_24.items()) == 16**6 - 1 == 4**12 - 1
    assert set(factor_24) <= set(P) | {3, 5, 13}

    # A larger period with the same gcd only decreases the bound in formula (1).
    # The finite scans verify each claimed smallest admissible period, not a
    # cutoff for the infinite-order theorem.
    min_all = [8, 9, 10, 7, 15, 21, 35, 105]
    min_parity = [4, 9, 5, 7, 15, 21, 35, 105]
    table_all, table_parity = [], []
    for g, d, e in zip(G, min_all, min_parity, strict=True):
        assert gcd(d, 105) == gcd(e, 105) == g
        assert not any(gcd(x, 105) == g for x in range(7, d))
        assert not any(gcd(x, 105) == g and x not in {1, 2, 3, 6}
                       for x in range(1, e))
        table_all.append(Fraction(maxima[g], 36 * (d // g)))
        table_parity.append(Fraction(maxima[g], 36 * (e // g)))
    assert max(table_all) == Fraction(23, 108)
    assert max(table_parity) == Fraction(11, 36)
    first_case_coverage = Fraction(11, 36) + 3 * max(table_all)
    assert first_case_coverage == Fraction(17, 18)

    subrows = []
    subset_bound = {}
    for r, expected_size, expected_m5, expected_m7 in [(0, 23, 6, 4), (1, 13, 5, 3)]:
        sub = [h for h in H if h % 3 == r]
        size = len(sub)
        m5 = max(Counter(h % 5 for h in sub).values())
        m7 = max(Counter(h % 7 for h in sub).values())
        assert (size, m5, m7) == (expected_size, expected_m5, expected_m7)
        values = [Fraction(1, 3), Fraction(m5, size), Fraction(m7, size), Fraction(1, size)]
        subset_bound[r] = max(values)
        # The affine parameterization removes the fixed mod-3 and parity
        # coordinates without changing either incidence maximum.
        for epsilon in [0, 1]:
            u0 = next(u for u in range(6) if u % 2 == epsilon and u % 3 == r)
            image = [v for v in range(35) if (u0 + 6*v) % 105 in h_set]
            assert len(image) == size
            assert max(Counter(v % 5 for v in image).values()) == m5
            assert max(Counter(v % 7 for v in image).values()) == m7
        subrows.append({"mod3": r, "size": size, "max_mod5": m5, "max_mod7": m7,
                        "gcd_order": [1, 5, 7, 35], "bounds": list(map(frac, values)),
                        "max_channel_fraction": frac(max(values))})
    assert subset_bound == {0: Fraction(1, 3), 1: Fraction(5, 13)}
    for epsilon in [0, 1]:
        image = [v for v in range(105) if (epsilon + 2*v) % 105 in h_set]
        assert {g: max(Counter(v % g for v in image).values()) for g in G} == maxima

    gaps = {
        "neither_5_nor_13_active": 1 - first_case_coverage,
        "exactly_one_active": Fraction(1, 2) * (1 - 3 * max(table_parity)),
        "both_same_parity": Fraction(1, 2) * (1 - 2 * max(table_parity)),
        "different_parities_13_phase_2_mod3": Fraction(1, 2) * (1 - 2 * max(table_parity)),
        "different_parities_13_phase_0_mod3": Fraction(13, 72) * (1 - 2 * subset_bound[1]),
        "different_parities_13_phase_1_mod3": Fraction(23, 72) * (1 - 2 * subset_bound[0]),
    }
    assert min(gaps.values()) == Fraction(1, 24)
    full_index_gap = Fraction(len(H), 210) * min(gaps.values())
    assert full_index_gap == Fraction(1, 140)

    old_orders = {q: order(2, q) for q in P}
    full_period = lcm(*old_orders.values())
    assert full_period == 6720
    for n in range(1, full_period + 1):
        old_hole = all((A_STAR*A_STAR * pow(2, n, q) - 1) % q for q in P)
        assert old_hole == (n % 2 == 0 and n//2 % 105 in h_set)

    root_residues = [A_STAR, 0] + [pow(pow(2, c, q), -1, q) for q, _, c in ROWS]
    root_moduli = [2*M, 3] + [q for q, _, _ in ROWS]
    a, progression_modulus = crt(root_residues, root_moduli)
    assert a == 8681796600341899699165924755002845830837950628236344137765453
    assert progression_modulus == 121041494945903853943122890515382691774327737794816871699188590
    assert a % (2*M) == A_STAR and a % 3 == 0
    assert len(str(a)) == 61
    assert 2*a*a - 1 > max(P + [q for q, _, _ in ROWS])
    rows_certificate = []
    for q, d, c in ROWS:
        assert factor_small(q) == {q: 1}
        assert order(4, q) == d and order(2, q) == 2*d
        assert a % q == pow(pow(2, c, q), -1, q)
        assert full_period % (2*d) == 0
        private = [u for u in range(1, 211)
                   if u % 105 in h_set and u % d == c
                   and all(u % dd != cc for qq, dd, cc in ROWS if qq != q)]
        assert private
        rows_certificate.append({"q": q, "order_2": 2*d, "order_4": d, "phase_u": c,
                                 "root_residue": a % q, "private_u": private[0],
                                 "all_private_u_in_1_210": private})

    sharp_missing_u = [u for u in range(210) if u % 105 in h_set
                       and not any(u % d == c for q, d, c in ROWS[:4])]
    assert sharp_missing_u == [64, 154, 184]
    advance, euclidean_digits, native_checks = load_native(source_dir or locate_native_source())
    missing_n = []
    native_private_indices = {}
    native_old_private_odd_indices = {}
    all_channels = P + [q for q, _, _ in ROWS]
    x = a*a - 1
    for n in range(1, full_period + 1):
        x = advance(x)
        assert x == (a*a << n) - 1
        readout = {q: euclidean_digits(x, (q,))[1][0] for q in all_channels}
        assert all(readout[q] == (a*a * pow(2, n, q) - 1) % q for q in all_channels)
        hits = [q for q in all_channels if readout[q] == 0]
        if len(hits) == 1:
            native_private_indices.setdefault(hits[0], n)
            if n % 2 and hits[0] in P:
                native_old_private_odd_indices.setdefault(hits[0], n)
        old_hit = any(readout[q] == 0 for q in P)
        q4_hit = any(readout[q] == 0 for q, _, _ in ROWS[:4])
        missing = not old_hit and not q4_hit
        assert missing == (n % 420 in {128, 308, 368})
        if missing:
            missing_n.append(n)
        q5_hit = any(readout[q] == 0 for q, _, _ in ROWS)
        assert old_hit or q5_hit
    assert len(missing_n) == 48
    assert Fraction(len(missing_n), full_period) == full_index_gap
    assert [row["private_u"] for row in rows_certificate] == [1, 6, 10, 16, 64]
    assert set(native_private_indices) == set(all_channels)
    assert set(native_old_private_odd_indices) == set(P)

    delta1_root = next(A_STAR + 2*M*t for t in range(3) if (A_STAR + 2*M*t) % 3)
    assert gcd(2*M, 3) == 1
    assert sum((A_STAR + 2*M*t) % 3 != 0 for t in range(3)) == 2
    assert all((delta1_root*delta1_root * pow(2, n, 3) - 1) % 3 == 0
               for n in range(2, 2*full_period + 1, 2))

    return {
        "schema": "enterprise-math.riesel-sharp-small-cost-gap.v1",
        "status": "Author analytic proof and exact finite evidence; not independent project Review.",
        "researcher_id": "EM-DIRECT-970E1C",
        "activity_id": "RA-D2EC212845B63844081F9A14",
        "dependency": {
            "repository": "awdawmip/enterprise-math",
            "old_certificate_commit": "e61a43115cf9dcbd0b3d8a746a5ac8086b8ca8fe",
            "old_certificate_path": "research_notes/portable_direct/riesel_mixed_20261119/certificate.json",
            "sixth_continuation_commit": "2feef401388e6e81a35dd8b0e66383f43561ad12",
            "sixth_continuation_proof": "research_notes/portable_direct/riesel_budget_20261120/cost/proof.md",
        },
        "a_star": str(A_STAR), "M": str(M), "P": P, "H": H,
        "incidence": {"gcds": G, "maxima": list(maxima.values()), "subsets": subrows},
        "small_factorizations": {
            "four_to_j_minus_one": {str(j): {str(q): e for q, e in f.items()} for j, f in small_factors.items()},
            "two_to_24_minus_one": {str(q): e for q, e in factor_24.items()},
        },
        "all_order_bounds": {
            "all_holes_minimum_period_by_gcd": min_all,
            "all_holes_bounds_by_gcd": list(map(frac, table_all)),
            "parity_minimum_effective_period_by_gcd": min_parity,
            "parity_bounds_by_gcd": list(map(frac, table_parity)),
            "excluded_parity_effective_orders": [1, 2, 3, 6],
            "excluded_parity_mod3_effective_orders": [1, 2],
            "proof_of_uniformity": "Formula (1) decreases with period at fixed gcd; every gcd divides 105 or 35.",
        },
        "case_gaps_relative_to_old_holes": {k: frac(v) for k, v in gaps.items()},
        "sharp_uncovered_density_among_all_exponents": frac(full_index_gap),
        "sharp_example": {
            "a": str(a), "a_decimal_digits": len(str(a)), "k_a_squared": str(a*a),
            "progression_modulus": str(progression_modulus),
            "crt_residues": list(map(str, root_residues)), "crt_moduli": list(map(str, root_moduli)),
            "rows": rows_certificate, "sharp_four_are_first_rows": 4,
            "missing_u_mod_210": sharp_missing_u,
            "missing_n_mod_420": [128, 308, 368],
            "full_checked_exponent_period": full_period,
            "missing_n_count_in_full_period": len(missing_n),
            "properness_lower_bound_first_term": str(2*a*a - 1),
            "exact_delta_after_fifth_row": 5,
            "total_cost_upper_bound_only": 25,
            "old_order_and_phase_source_reused": True,
        },
        "native_verification": {
            "source_commit": NATIVE_COMMIT,
            "source_blob_checks": native_checks,
            "positive_packet": {"affine_multiplier": 2, "affine_offset": 1,
                                "weight": "1", "multiplicity": 1},
            "actual_native_updates": full_period,
            "actual_euclidean_digits_calls": full_period * len(all_channels),
            "integer_formula_equalities": full_period,
            "native_readout_and_independent_modular_equalities": full_period * len(all_channels),
            "first_native_private_exponent_per_channel": native_private_indices,
            "first_native_private_odd_exponent_per_old_channel": native_old_private_odd_indices,
            "even_packet_composition_checked": True,
            "x6_anchor": "Unchanged; the integer register and prime projections retain their existing types.",
        },
        "cost_classification": {
            "delta1_iff": "3 does not divide a",
            "delta1_relative_density_in_old_root_progression": "2/3",
            "delta1_example_root": str(delta1_root),
            "excluded_finite_costs": [0, 2, 3, 4],
            "root_divisible_by_3": "delta is at least 5 or infinity",
            "attainability_all_costs_at_least_5": "Uses companion refinement theorem, not this finite verification.",
            "infinity_attainability": "Unresolved in this research.",
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path)
    args = parser.parse_args()
    result = verify(args.source_dir)
    target = Path(__file__).with_name("small_gap_certificate.json")
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "certificate": str(target),
                      "universal_lower_density": result["sharp_uncovered_density_among_all_exponents"],
                      "root_digits": result["sharp_example"]["a_decimal_digits"],
                      "checked_period": result["sharp_example"]["full_checked_exponent_period"],
                      "missing_count": result["sharp_example"]["missing_n_count_in_full_period"]}))
