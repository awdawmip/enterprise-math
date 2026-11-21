"""Reproduce the finite checks against the untouched source enumerator.

This is an author-side mathematical comparison, not an independent audit.
The old and new methods are algorithmically separate: local residue enumeration
versus the closed digit/valuation formulas.  No network or remote writes.
"""
import hashlib
import json
from math import comb
from pathlib import Path
from time import perf_counter

import erdos_parity as original
import compressed_counts as closed
from parity_reduction import odd_positions


ROOT = Path(__file__).resolve().parent


def direct_local(k, p):
    """Local events using v_p(C(n,k)), rather than closed singleton counts."""
    e = original.valuation(original.period(k), p)
    q = p ** e
    z = 0
    a = [0] * k
    for n in range(2 * k, 2 * k + q):
        binomial_val = (closed.factorial_valuation(n, p)
                        - closed.factorial_valuation(k, p)
                        - closed.factorial_valuation(n - k, p))
        failed = [i for i in range(k)
                  if original.valuation(n - i, p) > binomial_val]
        if not failed:
            z += 1
        elif len(failed) == 1:
            a[failed[0]] += 1
    return z, a


def digest_json(value):
    raw = json.dumps(value, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def run():
    start = perf_counter()
    tables = {}
    for k in range(2, 129):
        old = original.count_positions(k)
        new = closed.count_positions(k)
        assert old == new, ("full count disagreement", k)
        assert closed.count_positions(k, 4) == [x % 4 for x in old], k
        assert odd_positions(k) == [i for i, x in enumerate(old) if x % 2], k
        tables[str(k)] = {"H": sum(old), "H_mod4": sum(old) % 4,
                          "odd_positions": [i for i, x in enumerate(old) if x % 2],
                          "position_counts_sha256": digest_json(old)}

    local_count = 0
    for k in range(2, 33):
        for p in original.primes(k):
            z, a = direct_local(k, p)
            nz, na, _ = closed.local_counts(k, p)
            assert (z, a) == (nz, na), ("local count disagreement", k, p)
            local_count += 1

    direct_k = []
    for k in range(2, 11):
        result = [0] * k
        for n in range(2 * k, 2 * k + original.period(k)):
            integer_binomial = comb(n, k)
            failed = [i for i in range(k) if integer_binomial % (n - i)]
            if len(failed) == 1:
                result[failed[0]] += 1
        assert result == closed.count_positions(k), ("direct integer disagreement", k)
        direct_k.append(k)

    old449 = original.count_positions(449)
    new449 = closed.count_positions(449)
    assert old449 == new449, "449 full positions disagree"
    assert closed.count_positions(449, 4) == [x % 4 for x in old449]
    previous449 = json.loads((ROOT / "k449_full_crt.json").read_text())
    assert sum(old449) == int(previous449["H"])
    assert old449[224] == int(previous449["N_center"])
    assert old449[223] == int(previous449["N_223"]) == old449[225]
    odd449 = [i for i, value in enumerate(old449) if value % 2]
    assert odd449 == previous449["odd_positions"] == odd_positions(449) == [223, 225]
    assert sum(old449) % 4 == 2 and old449[224] % 4 == 0
    evidence449 = {
        "k": 449, "period": original.period(449),
        "H": sum(old449), "H_mod4": sum(old449) % 4,
        "N": old449, "N_mod4": [x % 4 for x in old449],
        "odd_positions": odd449, "center": 224,
        "position_counts_sha256": digest_json(old449),
        "local_2": {key: closed.local_counts(449, 2)[2][key]
                    for key in ("h", "m", "e", "digit_factor")},
        "selected_local_counts": {
            str(p): {"z": closed.local_counts(449, p)[0],
                     "a_223": closed.local_counts(449, p)[1][223],
                     "a_224": closed.local_counts(449, p)[1][224],
                     "d_223": closed.local_counts(449, p)[2]["deficits"][223],
                     "d_224": closed.local_counts(449, p)[2]["deficits"][224]}
            for p in (2, 3, 5, 7, 449)
        },
    }
    (ROOT / "k449_comparison.json").write_text(json.dumps(evidence449, indent=2) + "\n")
    report = {
        "status": "PASS_AUTHOR_SIDE_NOT_INDEPENDENT_REVIEW",
        "original_commit": "ab4699ad2a80b0e040c5a5f287cd34a537d75e6f",
        "full_position_comparison": {"inclusive_k_range": [2, 128],
                                     "additional_k": [449]},
        "local_histogram_comparison": {"inclusive_k_range": [2, 32],
                                       "prime_tables": local_count},
        "direct_integer_binomial_comparison_k": direct_k,
        "prior_449_output_agrees": True,
        "tables_2_to_128": tables,
        "k449_positions_sha256": digest_json(old449),
        "seconds": perf_counter() - start,
    }
    (ROOT / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key != "tables_2_to_128"}, indent=2))


if __name__ == "__main__":
    run()
