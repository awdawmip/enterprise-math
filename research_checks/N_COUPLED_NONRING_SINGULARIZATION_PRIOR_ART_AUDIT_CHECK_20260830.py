#!/usr/bin/env python3
"""Exact structural/regression checker for the N-coupled non-ring prior-art audit.

The literature classifications are evidence judgments and are not proved by this script.
The checker verifies:
  * required audit classes and fields are present in source_ledger.json;
  * classification vocabulary is respected;
  * every required mechanism class is covered;
  * the negative-match novelty guard is explicit;
  * elementary scalar firewall lemmas on pq are exhaustively true for a finite regression set.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts" / "N_COUPLED_NONRING_SINGULARIZATION_PRIOR_ART_AUDIT"
LEDGER = ART / "source_ledger.json"
CLAIMS = ART / "claim_map.json"

ALLOWED = {
    "EXACT_DUPLICATE",
    "STRICT_OR_PARTIAL_ANTECEDENT",
    "ADJACENT_METHOD",
    "NO_MATERIAL_MATCH",
}
REQUIRED_CLASSES = {
    "EUCLIDEAN_CONTINUED_FRACTION_STATE",
    "CANONICAL_REPRESENTATIVE_QUOTIENT_REMAINDER_CARRY",
    "PADIC_HENSEL_VALUATION_STATE",
    "POLLARD_WILLIAMS_ORDER_SMOOTHNESS",
    "RHO_COLLISION_CYCLE",
    "CONGRUENCE_OF_SQUARES_FERMAT_LEHMAN_HART",
    "LATTICE_RELATION_MODULAR_LINEAR_ALGEBRA",
    "CRT_IDEMPOTENT_ZERO_DIVISOR_NONUNIT_DISCOVERY",
}
SOURCE_FIELDS = {
    "source_id",
    "class",
    "citation",
    "public_inputs",
    "hidden_information_assumptions",
    "evolving_state",
    "stopping_predicate",
    "selective_collapse_event",
    "final_factor_extraction",
    "classification",
    "guard_relation",
    "exact_duplicate",
}


def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def check_structure() -> tuple[int, int]:
    ledger = load(LEDGER)
    claims = load(CLAIMS)

    got = set(ledger["minimum_search_classes"])
    missing = REQUIRED_CLASSES - got
    assert not missing, f"missing minimum search classes: {sorted(missing)}"

    source_ids = set()
    for source in ledger["sources"]:
        miss = SOURCE_FIELDS - set(source)
        assert not miss, (source.get("source_id"), sorted(miss))
        assert source["classification"] in ALLOWED
        assert source["source_id"] not in source_ids
        source_ids.add(source["source_id"])
        assert source["exact_duplicate"] is False

    assert ledger["exact_match_test"]["result"] == "NO_EXACT_DUPLICATE_FOUND_IN_AUDITED_SURFACES"
    assert "NOVELTY" in ledger["exact_match_test"]["novelty_guard"]

    for row in claims["rows"]:
        assert row["classification"] in ALLOWED
        unknown = set(row["sources"]) - source_ids
        assert not unknown, (row["claim_id"], sorted(unknown))

    assert claims["terminal_boundary"]["exact_duplicate"] is False
    assert "NOVELTY" in claims["terminal_boundary"]["novelty_guard"]
    return len(source_ids), len(claims["rows"])


def check_scalar_firewall() -> dict:
    primes = [3, 5, 7, 11, 13]
    semiprimes = 0
    scalar_checks = 0
    idempotent_checks = 0
    sqrt_unity_checks = 0

    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            N = p * q
            semiprimes += 1

            # Proper scalar nonunit iff exactly one CRT channel is zero.
            for s in range(N):
                g = math.gcd(s, N)
                proper = 1 < g < N
                one_sided_zero = ((s % p == 0) ^ (s % q == 0))
                assert proper == one_sided_zero, (p, q, s, g)
                if proper:
                    assert g in (p, q)
                scalar_checks += 1

            # Nontrivial idempotents are exactly (0,1)/(1,0), and each gives both factors.
            for e in range(N):
                if (e * e - e) % N == 0 and e not in (0, 1):
                    gp = math.gcd(e, N)
                    gm = math.gcd(e - 1, N)
                    assert {gp, gm} == {p, q}, (p, q, e, gp, gm)
                    idempotent_checks += 1

            # Nontrivial square roots of unity yield complementary factors.
            for x in range(N):
                if (x * x - 1) % N == 0 and x not in (1, N - 1):
                    g1 = math.gcd(x - 1, N)
                    g2 = math.gcd(x + 1, N)
                    assert {g1, g2} == {p, q}, (p, q, x, g1, g2)
                    sqrt_unity_checks += 1

    return {
        "semiprimes": semiprimes,
        "scalar_checks": scalar_checks,
        "nontrivial_idempotent_checks": idempotent_checks,
        "nontrivial_sqrt_unity_checks": sqrt_unity_checks,
    }


def main() -> None:
    sources, claims = check_structure()
    stats = check_scalar_firewall()
    print(
        "PASS",
        json.dumps(
            {
                "sources": sources,
                "claim_rows": claims,
                **stats,
            },
            sort_keys=True,
        ),
    )


if __name__ == "__main__":
    main()
