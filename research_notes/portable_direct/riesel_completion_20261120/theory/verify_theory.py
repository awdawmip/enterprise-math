"""Deterministic certificates for finite-budget prime covers.

This implements exact gcd partitioning and the terminating bounded-depth
branch algorithm from proof.md. The demonstration instances are deliberately
small; the theorem gives an enormous computable bound, not an efficiency claim.
All cover claims initially mean divisibility. Properness for k=509203 is
checked separately. The native arithmetic register stays inside a fixed X6
anchor, with positive singleton BRC effects.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import sys


PRIME_PROOFS: dict[int, dict] = {}
PROJECT_SOURCE_BLOBS = {
    "brc_transport.py": "be1debe367263931bd5e93fd750be3ed54624fe1",
    "brc_histogram.py": "9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1",
    "brc_rational_holonomy.py": "2591640fe348da9cd7f293a957bea9ae92c82943",
    "brc_weighted_recurrent.py": "4e6b3132580e3cd70a20a0d8bd4d28792b961afb",
}


def prove_prime(p: int) -> None:
    if p not in PRIME_PROOFS:
        assert p >= 2
        bound = isqrt(p)
        assert all(p % d != 0 for d in range(2, bound + 1))
        PRIME_PROOFS[p] = {
            "prime": p,
            "trial_bound": bound,
            "every_integer_divisor_2_through_bound_tested": True,
        }


def factor_trial(n: int) -> list[list[int]]:
    """Complete exact factorization by finite deterministic trial division."""
    assert n > 1
    remaining, d = n, 2
    factors = []
    while d * d <= remaining:
        exponent = 0
        while remaining % d == 0:
            exponent += 1
            remaining //= d
        if exponent:
            factors.append([d, exponent])
        d = 3 if d == 2 else d + 2
    if remaining > 1:
        factors.append([remaining, 1])
    verify_factorization(n, factors)
    return factors


def verify_factorization(n: int, factors: list[list[int]]) -> None:
    assert len({p for p, _ in factors}) == len(factors)
    assert all(e > 0 for _, e in factors)
    for p, _ in factors:
        prove_prime(p)
    assert prod(p**e for p, e in factors) == n


def prime_cover_period(k: int, primes: list[int] | tuple[int, ...]) -> dict:
    """Whole positive orbit of x -> 2x+1 modulo product(primes).

    On an odd modulus this is a permutation, so the start has a first return
    in at most C steps. Includes n=h (same state as n=0), as positive exponents
    are the domain. Empty Q gives C=1, h=1 and correctly misses n=1.
    """
    assert k >= 3 and k % 2 == 1
    assert len(set(primes)) == len(primes)
    for p in primes:
        prove_prime(p)
        assert p % 2 == 1
    modulus = prod(primes)
    initial = (k - 1) % modulus
    x, n, first_missing = initial, 0, None
    orbit = []
    while True:
        n += 1
        x = (2 * x + 1) % modulus
        common = gcd(x, modulus)
        assert x == (k * pow(2, n, modulus) - 1) % modulus
        if common == 1 and first_missing is None:
            first_missing = n
        orbit.append({"n": n, "residue": x, "gcd_with_modulus": common})
        if x == initial:
            break
        assert n < modulus
    assert n <= modulus
    return {
        "modulus": modulus,
        "initial_state_n0": initial,
        "first_return_period": n,
        "first_missing_positive_exponent": first_missing,
        "is_full_divisibility_cover": first_missing is None,
        "orbit": orbit,
    }


def bounded_cover_search(k: int, budget: int, selected: tuple[int, ...] = ()) -> dict:
    """Unrestricted but finite-depth decision tree; may be impractical."""
    assert budget >= 0 and len(selected) <= budget
    status = prime_cover_period(k, selected)
    node = {"selected_primes": list(selected), "period_certificate": status}
    n = status["first_missing_positive_exponent"]
    if n is None:
        node.update(answer=True, children=[])
        return node
    value = k * (1 << n) - 1
    node["missing_value"] = value
    assert all(value % p for p in selected)
    if len(selected) == budget:
        node.update(answer=False, children=[])
        return node
    factors = factor_trial(value)
    node["complete_factorization_of_missing_value"] = factors
    children = []
    for p, _ in factors:
        assert p not in selected
        child = bounded_cover_search(k, budget, tuple(sorted((*selected, p))))
        children.append({"added_prime": p, "node": child})
        if child["answer"]:
            node.update(answer=True, children=children)
            return node
    node.update(answer=False, children=children)
    return node


def capped_U(k: int, steps: int, cap: int) -> int:
    """Compute min(U_steps, cap) without constructing enormous tower integers."""
    assert k >= 3 and cap >= 1
    u = 1
    for _ in range(steps):
        if u >= cap:
            return cap
        if u >= cap.bit_length():
            return cap
        u = min(cap, u * (k * (1 << u) - 1))
    return u


def verify_search_tree(k: int, budget: int, node: dict, expected: tuple[int, ...] = ()) -> bool:
    """Validate success or full failure, including completeness of branches."""
    selected = tuple(node["selected_primes"])
    assert selected == expected and selected == tuple(sorted(set(selected)))
    assert len(selected) <= budget
    status = prime_cover_period(k, selected)
    assert status == node["period_certificate"]
    assert capped_U(k, len(selected), status["modulus"]) == status["modulus"]
    missing = status["first_missing_positive_exponent"]
    if missing is None:
        assert node["answer"] is True and node["children"] == []
        return True
    value = k * (1 << missing) - 1
    assert node["missing_value"] == value
    assert missing <= status["modulus"]
    assert all(value % p for p in selected)
    if len(selected) == budget:
        assert node["answer"] is False and node["children"] == []
        return False
    factors = node["complete_factorization_of_missing_value"]
    verify_factorization(value, factors)
    primes = [p for p, _ in factors]
    children = node["children"]
    added = [child["added_prime"] for child in children]
    assert len(added) == len(set(added))
    assert all(p in primes for p in added)
    answers = []
    for child in children:
        p = child["added_prime"]
        assert p not in selected
        answers.append(verify_search_tree(k, budget, child["node"], tuple(sorted((*selected, p)))))
    if node["answer"]:
        assert any(answers)
        return True
    assert set(added) == set(primes) and not any(answers)
    return False


def search_stats(node: dict) -> dict:
    nodes = [node]
    all_nodes = []
    while nodes:
        here = nodes.pop()
        all_nodes.append(here)
        nodes.extend(child["node"] for child in here["children"])
    leaves = [r for r in all_nodes if not r["children"]]
    return {
        "node_count": len(all_nodes),
        "leaf_count": len(leaves),
        "maximum_selected_count": max(len(r["selected_primes"]) for r in all_nodes),
        "largest_missing_exponent": max((r["period_certificate"]["first_missing_positive_exponent"] or 0) for r in all_nodes),
        "successful_covers": [r["selected_primes"] for r in leaves if r["answer"]],
    }


def gcd_partition(values: list[int]) -> dict:
    """Exact minimum via all subset gcds and a partition DP, without factoring."""
    assert all(v > 1 for v in values)
    s = len(values)
    size = 1 << s
    subset_gcd = [0] * size
    dp = [s + 1] * size
    first_block = [0] * size
    dp[0] = 0
    for mask in range(1, size):
        bit = mask & -mask
        i = bit.bit_length() - 1
        subset_gcd[mask] = gcd(subset_gcd[mask ^ bit], values[i])
        sub = mask
        while sub:
            if sub & bit and subset_gcd[sub] > 1:
                score = 1 + dp[mask ^ sub]
                if score < dp[mask]:
                    dp[mask] = score
                    first_block[mask] = sub
            sub = (sub - 1) & mask
    partition = []
    mask = size - 1
    while mask:
        block = first_block[mask]
        assert block and block & mask == block and subset_gcd[block] > 1
        partition.append({
            "sample_positions_1_based": [i + 1 for i in range(s) if block >> i & 1],
            "common_gcd": subset_gcd[block],
        })
        mask ^= block
    assert len(partition) == dp[-1]
    return {
        "values": values,
        "minimum_prime_cover_cardinality": dp[-1],
        "optimal_gcd_partition": partition,
        "subset_gcds": subset_gcd,
        "dp_values": dp,
        "factorization_used": False,
    }


def maximum_coprime_subset(values: list[int]) -> list[int]:
    """Small exact branch search. Lower witnesses are separately checked."""
    adjacency = [sum(1 << j for j, b in enumerate(values) if i != j and gcd(a, b) == 1)
                 for i, a in enumerate(values)]
    best = []

    def visit(chosen: list[int], candidates: int) -> None:
        nonlocal best
        if len(chosen) + candidates.bit_count() <= len(best):
            return
        if not candidates:
            best = chosen
            return
        while candidates:
            if len(chosen) + candidates.bit_count() <= len(best):
                return
            bit = candidates & -candidates
            candidates ^= bit
            i = bit.bit_length() - 1
            visit([*chosen, i + 1], candidates & adjacency[i])

    visit([], (1 << len(values)) - 1)
    assert all(gcd(values[i - 1], values[j - 1]) == 1 for i, j in combinations(best, 2))
    return best


def sample_record(k: int, exponents: list[int]) -> dict:
    values = [k * (1 << n) - 1 for n in exponents]
    result = gcd_partition(values)
    result["exponents"] = exponents
    result["pairwise_gcds"] = [
        {"i": exponents[i], "j": exponents[j], "gcd": gcd(values[i], values[j])}
        for i, j in combinations(range(len(values)), 2)
    ]
    result["all_sample_gcd"] = gcd(*values)
    result["maximum_pairwise_coprime_count"] = len(maximum_coprime_subset(values))
    return result


def native_checks(source_dir: Path, k: int, primes: tuple[int, ...]) -> dict:
    actual_blobs = {}
    for name, expected_blob in PROJECT_SOURCE_BLOBS.items():
        content = (source_dir / "enterprise_math" / name).read_bytes()
        actual_blob = sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
        assert actual_blob == expected_blob, (name, expected_blob, actual_blob)
        actual_blobs[name] = actual_blob
    sys.path.insert(0, str(source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits

    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    double_step = step.then(step)
    composed = EffectHistogram.unit(1)

    def advance(packet, value):
        (point, weights), = packet.evaluate((value,)).items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    def rem(value, p):
        return euclidean_digits(value, (p,))[1][0]

    value = k - 1
    rows = []
    for n in range(1, 25):
        next_value = advance(step, value)
        assert next_value == 2 * value + 1 == k * (1 << n) - 1
        assert advance(double_step, value) == 4 * value + 3
        residues = []
        for p in primes:
            observed_next = rem(next_value, p)
            induced_next = rem(advance(step, rem(value, p)), p)
            assert observed_next == induced_next
            residues.append(observed_next)
        rows.append({"n": n, "value": next_value, "residues_in_prime_order": residues})
        composed = composed.then(step)
        assert advance(composed, k - 1) == next_value
        value = next_value
    source_file = source_dir / "enterprise_math" / "brc_transport.py"
    assert source_file.is_file()
    return {
        "source_commit": "b1efc6c805661ed7b476e6e730107da6043176ee",
        "source_file_sha256": sha256(source_file.read_bytes()).hexdigest(),
        "project_source_blobs": actual_blobs,
        "source_blob_pins_verified_before_import": True,
        "pin_provenance": "research_notes/portable_direct/riesel_mixed_20261119/results.json; same four pins in v4 phase verification.",
        "carrier_scope": "Fixed X6 anchor; internal integer register; exponent is not physical time or an added space axis.",
        "BRC_scope": "Exactly one output; positive weight 1 and multiplicity 1, checked each call.",
        "observation_identity": "O_Q(T(x)) = T_Q(O_Q(x)), checked on every native step and every prime channel.",
        "entrypoints": ["Affine", "EffectHistogram.from_terms", "EffectHistogram.unit", "EffectHistogram.then", "EffectHistogram.evaluate", "euclidean_digits"],
        "primes": list(primes),
        "full_24_step_records": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path("vendor_src"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()

    k = 509203
    primes = (3, 5, 7, 13, 17, 241)
    channels = []
    for p in primes:
        prove_prime(p)
        order, residue = 1, 2 % p
        while residue != 1:
            residue = residue * 2 % p
            order += 1
        phases = [n for n in range(order) if (k * pow(2, n, p) - 1) % p == 0]
        assert len(phases) == 1
        channels.append({"prime": p, "order_of_2": order, "unique_hit_phase": phases[0]})
    assert [(r["order_of_2"], r["unique_hit_phase"]) for r in channels] == [(2, 0), (4, 1), (3, 2), (12, 7), (8, 7), (24, 3)]
    assert lcm(*(r["order_of_2"] for r in channels)) == 24
    full_cover = prime_cover_period(k, primes)
    assert full_cover["is_full_divisibility_cover"] and full_cover["first_return_period"] == 24
    assert max(primes) < 2 * k - 1

    six_exponents = [1, 3, 4, 11, 15, 19]
    six = sample_record(k, six_exponents)
    assert six["minimum_prime_cover_cardinality"] == six["maximum_pairwise_coprime_count"] == 6
    assert len(six["pairwise_gcds"]) == 15 and all(r["gcd"] == 1 for r in six["pairwise_gcds"])

    prefix_records = []
    values24 = [k * (1 << n) - 1 for n in range(1, 25)]
    for length in range(1, 25):
        values = values24[:length]
        lower = maximum_coprime_subset(values)
        upper = next(subset for count in range(7) for subset in combinations(primes, count)
                     if all(any(value % p == 0 for p in subset) for value in values))
        assert len(lower) == len(upper)
        prefix_records.append({
            "prefix_length": length,
            "exact_minimum_cover_cardinality": len(lower),
            "lower_bound_coprime_exponents": lower,
            "upper_bound_cover": list(upper),
        })
    expected_prefix = [1, 2] + [3] * 4 + [4] * 4 + [5] * 8 + [6] * 6
    assert [row["exact_minimum_cover_cardinality"] for row in prefix_records] == expected_prefix

    triangle = sample_record(k, [2, 5, 13])
    common = sample_record(k, [2, 4, 6])
    assert [r["gcd"] for r in triangle["pairwise_gcds"]] == [7, 23, 5]
    assert [r["gcd"] for r in common["pairwise_gcds"]] == [3, 3, 3]
    assert triangle["all_sample_gcd"] == 1 and common["all_sample_gcd"] == 3
    assert triangle["minimum_prime_cover_cardinality"] == 2 and common["minimum_prime_cover_cardinality"] == 1
    assert triangle["maximum_pairwise_coprime_count"] == common["maximum_pairwise_coprime_count"] == 1
    assert all(any(value % p == 0 for p in (5, 7)) for value in triangle["values"])
    triangle["explicit_cover"] = [5, 7]
    common["explicit_cover"] = [3]

    five_primes = [3, 5, 7, 11, 13]
    supports = list(combinations(five_primes, 3))
    general_values = [prod(support) for support in supports]
    general = gcd_partition(general_values)
    assert general["minimum_prime_cover_cardinality"] == 3
    assert all(gcd(a, b) > 1 for a, b in combinations(general_values, 2))
    general["known_prime_supports"] = [list(support) for support in supports]
    general["maximum_pairwise_coprime_count"] = 1
    general["scope"] = "General integer-sequence example; not claimed to be an exponential Riesel orbit."

    searches = []
    for small_budget in range(4):
        tree = bounded_cover_search(3, small_budget)
        assert verify_search_tree(3, small_budget, tree) is False
        searches.append({"k": 3, "budget": small_budget, "answer": False, "tree": tree, "statistics": search_stats(tree)})
    success = bounded_cover_search(k, 6)
    assert verify_search_tree(k, 6, success) is True
    success_stats = search_stats(success)
    assert success_stats["successful_covers"] == [list(primes)]
    assert success_stats["node_count"] == 7
    searches.append({"k": k, "budget": 6, "answer": True, "tree": success, "statistics": success_stats})

    U = [1]
    for _ in range(3):
        U.append(U[-1] * (3 * (1 << U[-1]) - 1))
    assert U[:3] == [1, 5, 475]
    for budget, record in enumerate(searches[:4]):
        assert record["statistics"]["largest_missing_exponent"] <= U[budget]
    native = native_checks(args.source_dir, k, primes)

    output = {
        "schema": "riesel-v5-general-theory-v1",
        "researcher": "EM-DIRECT-970E1C",
        "research_activity": "RA-D2EC212845B63844081F9A14",
        "review_status": "Author proof and deterministic certificate checks; not an independent project Review.",
        "prior_science_commit": "a4d8c6a537a2f9c8c02beba4eae4b0c399fd7d52",
        "entry_snapshots": {"GK": "e1abd014a6f5afb166db32a7c6d7a5ace17dd14a", "EM": "5727d71f7a17b143b16ad7b93219ad6f2d4244a8"},
        "cover_definition": "Finite prime divisibility cover; properness is separate.",
        "theorems": {
            "finite_character": "tau = sup_L tau_L, including infinity; proof.md Theorem 2.",
            "gcd_partition": "Finite sample tau equals least number of blocks with common gcd > 1; proof.md Theorem 3.",
            "fixed_budget_bound": "U_0=1; U_(j+1)=U_j*(k*2^U_j-1); tau(k)<=t iff tau_(U_t)(k)<=t; proof.md Theorem 4.",
            "minimal_cover_product_bound": "Only inclusion-minimal size-s full covers satisfy product(Q)<=U_s.",
            "profinite_scope": "No finite cover iff a compatible formal exponent avoids every odd prime; existence for the fixed old square root remains unproved.",
        },
        "riesel_509203": {
            "k": k,
            "channels": channels,
            "whole_future_certificate": full_cover,
            "properness": {"smallest_term": 2 * k - 1, "largest_cover_prime": max(primes), "strict_for_all_positive_exponents": True},
            "six_coprime_terms": six,
            "exact_global_minimum_prime_cover_cardinality": 6,
            "prefix_certificates": prefix_records,
            "higher_order_gcd_counterexamples": [triangle, common],
        },
        "general_nu_1_tau_3_example": general,
        "bounded_search_demonstrations": searches,
        "illustrative_U_for_k_3_steps_0_through_3": [str(u) for u in U],
        "deterministic_prime_proofs": [PRIME_PROOFS[p] for p in sorted(PRIME_PROOFS)],
        "native_BRC_check": native,
        "limitations": [
            "Finite examples do not replace the universal proofs.",
            "Fixed-budget decidability does not settle unbounded existence of any finite cover.",
            "No non-cover theorem for the fixed old square root is claimed.",
            "Profinite formal exponents and formal roots are auxiliary observation completions, not actual integer BRC states.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "tau_509203": 6,
        "six_coprime_exponents": six_exponents,
        "boolean_triangle_cover_costs": [2, 1],
        "bounded_search_cases_checked": len(searches),
        "positive_search_nodes": success_stats["node_count"],
        "native_steps": 24,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
