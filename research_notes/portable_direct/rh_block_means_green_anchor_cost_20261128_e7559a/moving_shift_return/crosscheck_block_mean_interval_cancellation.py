#!/usr/bin/env python3
"""Author cross-check of the new block-mean proof and shared-history arithmetic.

Independent finite rational implementation; it does not import or execute the
block-mean author script and does not rerun predecessor calculations.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def average(values):
    return sum(values, F(0)) / len(values)


def root_bound_exact(u, q, a):
    """Check u <= (a+sqrt(2))*sqrt(q) with only exact rational decisions."""
    if u <= 0:
        return True
    residual = u * u - (a * a + 2) * q
    return residual <= 0 or residual * residual <= 8 * a * a * q * q


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--block-means", type=Path, required=True)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name(
                            "block_mean_author_crosscheck_certificate.json"))
    args = parser.parse_args()
    counts = {"source_vectors": 0, "blockings": 0,
              "same_endpoint_interval_pair_checks": 0,
              "nonnegative_source_coefficient_checks": 0,
              "Jensen_checks": 0, "whole_block_recoveries": 0,
              "point_recoveries_exact_sqrt2_constant": 0}

    for k in range(1, 7):
        X = 2 ** k
        for pattern in range(2):
            source = [F(0)]
            for n in range(1, 2 * X):
                if pattern == 0:
                    source.append(F(n % 7, 13))
                else:
                    source.append(F(10 ** 12 if n == 1 else
                                    10 ** 6 if n % 17 == 0 else n % 5, 19))
            lows = [F(0)] + [source[n] - F(1, 1000 + n)
                            for n in range(1, 2 * X)]
            highs = [F(0)] + [source[n] + F(2, 1000 + n)
                             for n in range(1, 2 * X)]
            prefix, prefix_lo, prefix_hi = [F(0)], [F(0)], [F(0)]
            for n in range(1, 2 * X):
                prefix.append(prefix[-1] + source[n])
                prefix_lo.append(prefix_lo[-1] + lows[n])
                prefix_hi.append(prefix_hi[-1] + highs[n])
            z = [F(n) - prefix[n] for n in range(X, 2 * X)]
            assert all(z[n + 1] - z[n] <= 1 for n in range(X - 1))
            counts["source_vectors"] += 1

            for s in range(k):
                r, M, t = 2 ** s, X // 2 ** s, k - s
                w = [average(z[i * r:(i + 1) * r]) for i in range(M)]
                lo_blocks = [sum(prefix_lo[X + i * r:X + (i + 1) * r], F(0))
                             for i in range(M)]
                hi_blocks = [sum(prefix_hi[X + i * r:X + (i + 1) * r], F(0))
                             for i in range(M)]
                candidates = []
                for j in range(t):
                    d = 2 ** j
                    numerator = sum((max(w[i + d] - w[i], 0) ** 2
                                     for i in range(M - d)), F(0))
                    raw = sum((max(z[n + r * d] - z[n], 0) ** 2
                               for n in range(X - r * d)), F(0))
                    assert r * numerator <= raw
                    candidates.append(numerator / (X * d))
                    counts["Jensen_checks"] += 1

                    for i in range(M - d):
                        left, right = X + i * r, X + (i + d) * r
                        coeff = []
                        for n in range(1, 2 * X):
                            left_count = min(r, max(0, left + r - n))
                            right_count = min(r, max(0, right + r - n))
                            delta = right_count - left_count
                            assert delta >= 0
                            counts["nonnegative_source_coefficient_checks"] += 1
                            coeff.append(delta)
                        true_mass = sum((coeff[n - 1] * source[n]
                                         for n in range(1, 2 * X)), F(0))
                        low_mass = sum((coeff[n - 1] * lows[n]
                                        for n in range(1, 2 * X)), F(0))
                        high_mass = sum((coeff[n - 1] * highs[n]
                                         for n in range(1, 2 * X)), F(0))
                        assert low_mass == lo_blocks[i + d] - lo_blocks[i]
                        assert high_mass == hi_blocks[i + d] - hi_blocks[i]
                        deficit = r * r * d - true_mass
                        assert deficit == r * (w[i + d] - w[i])
                        assert r * r * d - high_mass <= deficit
                        assert deficit <= r * r * d - low_mass
                        counts["same_endpoint_interval_pair_checks"] += 1

                C = max(candidates)
                assert max(z[-1] - z[0] - (r - 1), 0) ** 2 <= t * t * X * C
                counts["whole_block_recoveries"] += 1
                for n in range(X):
                    # The proof actually gives 2r-1 for every noninitial block;
                    # certify its displayed 2r bound with the exact sqrt(2).
                    assert root_bound_exact(z[n] - z[0] - 2 * r, X * C, F(t + 1))
                    if n >= r:
                        block = n // r
                        assert z[n] - w[block - 1] <= F(3 * r - 1, 2)
                    counts["point_recoveries_exact_sqrt2_constant"] += 1
                counts["blockings"] += 1

    dependency_names = ("COARSE_BLOCK_MEANS_AND_RH.md", "certify_block_mean_statistics.py")
    result = {
        "status": "PASS",
        "type": "author cross-check; not independent Review",
        "researcher_id": "EM-DIRECT-E7559A / TASK_RESEARCH",
        "activity": "RA-D2F111EA1C0D4B1DBEFBC1B4",
        "arithmetic": "exact rational arithmetic, including exact sqrt(2) comparisons",
        "counts": counts,
        "checked_source_hashes": [
            {"file": name,
             "sha256": hashlib.sha256((args.block_means / name).read_bytes()).hexdigest()}
            for name in dependency_names
        ],
        "scope": {
            "source": "two nonnegative rational source patterns, one with a large shared history",
            "windows": "X=2^k, 1<=k<=6; every r=2^s with 0<=s<k",
            "same_endpoint_subtraction":
                "all source coefficient differences checked nonnegative before endpoint subtraction",
            "original_scripts_executed": False,
            "previous_certificates_recomputed": False,
            "unbounded_theorem": "author analytic cross-check in AUTHOR_CROSSCHECK_BLOCK_MEANS.md",
        },
    }
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "counts": counts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
