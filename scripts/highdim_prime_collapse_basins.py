#!/usr/bin/env python3
"""Generate the 2D--19D prime-collapse basin tables.

Research status: computational exploration only.
Primary carrier: additive quadratic shell sum(x_i^2).
Controls: triangular and linear additive shells.

The script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import math
import statistics
from pathlib import Path
from typing import Callable, Dict, List, Tuple


FamilyFn = Callable[[int], int]

FAMILIES: Dict[str, FamilyFn] = {
    "quadratic": lambda x: x * x,
    "triangular": lambda x: x * (x + 1) // 2,
    "linear": lambda x: x,
}


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = math.isqrt(n)
    for q in range(3, r + 1, 2):
        if n % q == 0:
            return False
    return True


def max_x(family: str, nmax: int) -> int:
    if family == "quadratic":
        return math.isqrt(nmax)
    if family == "triangular":
        x = 0
        while (x + 1) * (x + 2) // 2 <= nmax:
            x += 1
        return x
    if family == "linear":
        return nmax
    raise ValueError(family)


def build_dp(
    family: str, nmax: int, dmax: int
) -> Tuple[Dict[int, List[List[int]]], List[List[int]]]:
    """Return ordered support DP and unordered orbit-count DP.

    ordered[d][n][s] counts ordered x in N_0^d with readout n and
    exactly s nonzero coordinates.

    orbit[n][s] counts multisets of s strictly-positive coordinate values
    with readout n. It is used only as a compact orbit inventory.
    """
    f = FAMILIES[family]
    values = [f(x) for x in range(max_x(family, nmax) + 1)]
    if values[0] != 0 or len(values) != len(set(values)):
        raise AssertionError("family values must be strictly increasing from 0")
    positive = values[1:]

    ordered: Dict[int, List[List[int]]] = {}
    prev = [[0] * (dmax + 1) for _ in range(nmax + 1)]
    prev[0][0] = 1
    ordered[0] = prev

    for d in range(1, dmax + 1):
        cur = [[0] * (dmax + 1) for _ in range(nmax + 1)]
        for total in range(nmax + 1):
            for s in range(d):
                c = prev[total][s]
                if not c:
                    continue
                cur[total][s] += c  # new coordinate is zero
                for value in positive:
                    if total + value > nmax:
                        break
                    cur[total + value][s + 1] += c
        ordered[d] = cur
        prev = cur

    orbit = [[0] * (dmax + 1) for _ in range(nmax + 1)]
    orbit[0][0] = 1
    for value in positive:
        for total in range(value, nmax + 1):
            for s in range(1, dmax + 1):
                orbit[total][s] += orbit[total - value][s - 1]

    return ordered, orbit


def shell_count(ordered: Dict[int, List[List[int]]], d: int, n: int) -> int:
    return sum(ordered[d][n])


def support_metrics(counts: List[int], d: int):
    total = sum(counts)
    if total == 0:
        return {
            "total": 0,
            "min_support": None,
            "max_support": None,
            "mean_support": None,
            "mode_support": None,
            "support_entropy": None,
        }

    active = [(s, c) for s, c in enumerate(counts) if c]
    mean_support = sum(s * c for s, c in active) / total
    peak = max(c for _, c in active)
    mode_support = min(s for s, c in active if c == peak)
    probs = [c / total for _, c in active]
    entropy = -sum(q * math.log(q) for q in probs)
    entropy_norm = entropy / math.log(len(probs)) if len(probs) > 1 else 0.0
    return {
        "total": total,
        "min_support": min(s for s, _ in active),
        "max_support": max(s for s, _ in active),
        "mean_support": mean_support,
        "mode_support": mode_support,
        "support_entropy": entropy_norm,
    }


def fixed_face_survival(ordered, d: int, n: int):
    cur = shell_count(ordered, d, n)
    if cur == 0:
        return None
    return shell_count(ordered, d - 1, n) / cur


def local_same_mod8_log_gap(ordered, primes, nmax: int, d: int, window: int = 32):
    gaps = []
    for p in primes:
        if p == 2:
            continue
        candidates = [
            n
            for n in range(max(3, p - window), min(nmax, p + window) + 1)
            if n % 2 == 1 and not is_prime(n) and n % 8 == p % 8
        ]
        candidates.sort(key=lambda n: (abs(n - p), n))
        candidates = candidates[:4]
        if not candidates:
            continue
        p_log = math.log1p(shell_count(ordered, d, p))
        c_logs = [math.log1p(shell_count(ordered, d, n)) for n in candidates]
        gaps.append(p_log - statistics.mean(c_logs))
    return statistics.mean(gaps), statistics.median(gaps), len(gaps)


def f12(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return format(value, ".12g")
    return str(value)


def write_rows(path: Path, fieldnames, rows) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: f12(row.get(k)) for k in fieldnames})


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def generate(nmax: int, dmin: int, dmax: int, outdir: Path) -> None:
    if dmin < 2 or dmax < dmin:
        raise ValueError("require 2 <= dmin <= dmax")
    outdir.mkdir(parents=True, exist_ok=True)

    primes = [n for n in range(2, nmax + 1) if is_prime(n)]
    composites = [n for n in range(2, nmax + 1) if not is_prime(n)]

    all_dp = {
        family: build_dp(family, nmax, dmax)
        for family in FAMILIES
    }

    # Full long table.
    long_fields = [
        "family", "prime", "dimension", "p_mod8", "birth_dimension",
        "ordered_state_count", "orbit_count", "min_support", "max_support",
        "mean_support", "mode_support", "support_entropy",
        "fixed_face_survival", "basin_fingerprint",
    ]
    long_rows = []

    for family, (ordered, orbit) in all_dp.items():
        for p in primes:
            birth = next(
                (d for d in range(1, dmax + 1) if shell_count(ordered, d, p) > 0),
                None,
            )
            for d in range(dmin, dmax + 1):
                metrics = support_metrics(ordered[d][p], d)
                total = metrics["total"]
                previous = shell_count(ordered, d - 1, p)
                face = fixed_face_survival(ordered, d, p)

                if total:
                    # Exact collapse identity: fixed-face survival equals mean zero fraction.
                    rhs = 1.0 - metrics["mean_support"] / d
                    if abs(face - rhs) > 1e-12:
                        raise AssertionError((family, p, d, face, rhs))

                if total == 0:
                    band = "empty"
                elif previous == 0:
                    band = "birth"
                elif face < 0.25:
                    band = "tight"
                elif face < 0.5:
                    band = "medium"
                else:
                    band = "loose"

                fingerprint = (
                    f"{family[0].upper()}-r{p % 8}-b{birth}-"
                    f"m{metrics['mode_support']}-{band}"
                )
                long_rows.append({
                    "family": family,
                    "prime": p,
                    "dimension": d,
                    "p_mod8": p % 8,
                    "birth_dimension": birth,
                    "ordered_state_count": total,
                    "orbit_count": sum(orbit[p][: d + 1]),
                    "min_support": metrics["min_support"],
                    "max_support": metrics["max_support"],
                    "mean_support": metrics["mean_support"],
                    "mode_support": metrics["mode_support"],
                    "support_entropy": metrics["support_entropy"],
                    "fixed_face_survival": face,
                    "basin_fingerprint": fingerprint,
                })

    long_path = outdir / "prime_dimension_basin_long.csv"
    write_rows(long_path, long_fields, long_rows)

    # Dimension summary with local same-mod-8 composite controls.
    summary_fields = [
        "family", "dimension", "prime_count", "prime_coverage_count",
        "prime_coverage_ratio", "prime_mean_log1p_state_count",
        "composite_mean_log1p_state_count",
        "local_same_mod8_prime_minus_composite_mean_log_gap",
        "local_same_mod8_prime_minus_composite_median_log_gap",
        "local_matched_prime_count", "prime_mean_support_nonempty",
        "prime_mean_fixed_face_survival_nonempty",
        "prime_mean_support_entropy_nonempty",
    ]
    summary_rows = []
    for family, (ordered, _orbit) in all_dp.items():
        for d in range(dmin, dmax + 1):
            prime_metrics = []
            prime_counts = []
            for p in primes:
                metrics = support_metrics(ordered[d][p], d)
                prime_counts.append(metrics["total"])
                if metrics["total"]:
                    prime_metrics.append((
                        metrics["mean_support"],
                        fixed_face_survival(ordered, d, p),
                        metrics["support_entropy"],
                    ))

            gap_mean, gap_median, matched_n = local_same_mod8_log_gap(
                ordered, primes, nmax, d
            )
            composite_logs = [
                math.log1p(shell_count(ordered, d, n)) for n in composites
            ]
            summary_rows.append({
                "family": family,
                "dimension": d,
                "prime_count": len(primes),
                "prime_coverage_count": sum(c > 0 for c in prime_counts),
                "prime_coverage_ratio": sum(c > 0 for c in prime_counts) / len(primes),
                "prime_mean_log1p_state_count": statistics.mean(
                    math.log1p(c) for c in prime_counts
                ),
                "composite_mean_log1p_state_count": statistics.mean(composite_logs),
                "local_same_mod8_prime_minus_composite_mean_log_gap": gap_mean,
                "local_same_mod8_prime_minus_composite_median_log_gap": gap_median,
                "local_matched_prime_count": matched_n,
                "prime_mean_support_nonempty": statistics.mean(x[0] for x in prime_metrics),
                "prime_mean_fixed_face_survival_nonempty": statistics.mean(x[1] for x in prime_metrics),
                "prime_mean_support_entropy_nonempty": statistics.mean(x[2] for x in prime_metrics),
            })

    summary_path = outdir / "dimension_summary.csv"
    write_rows(summary_path, summary_fields, summary_rows)

    # Birth registry for all three readouts.
    birth_fields = [
        "family", "prime", "p_mod8", "birth_dimension",
        "max_support_seen_by_d19", "orbit_count_by_d19",
    ]
    birth_rows = []
    for family, (ordered, orbit) in all_dp.items():
        for p in primes:
            birth = next(
                (d for d in range(1, dmax + 1) if shell_count(ordered, d, p) > 0),
                None,
            )
            supports = [s for s, c in enumerate(ordered[dmax][p]) if c]
            birth_rows.append({
                "family": family,
                "prime": p,
                "p_mod8": p % 8,
                "birth_dimension": birth,
                "max_support_seen_by_d19": max(supports) if supports else None,
                "orbit_count_by_d19": sum(orbit[p][: dmax + 1]),
            })
    birth_path = outdir / "birth_registry.csv"
    write_rows(birth_path, birth_fields, birth_rows)

    # Quadratic support spectrum A_s(p).
    quadratic_ordered, _ = all_dp["quadratic"]
    spectrum_fields = ["prime", "p_mod8"] + [f"s{s}" for s in range(1, dmax + 1)]
    spectrum_rows = []
    for p in primes:
        row = {"prime": p, "p_mod8": p % 8}
        for s in range(1, dmax + 1):
            row[f"s{s}"] = quadratic_ordered[s][p][s]
        spectrum_rows.append(row)
    spectrum_path = outdir / "quadratic_support_spectrum.csv"
    write_rows(spectrum_path, spectrum_fields, spectrum_rows)

    # Quadratic C_d(p) matrix.
    count_path = outdir / "quadratic_count_matrix.csv"
    count_fields = ["prime"] + [str(d) for d in range(dmin, dmax + 1)]
    count_rows = []
    for p in primes:
        row = {"prime": p}
        for d in range(dmin, dmax + 1):
            row[str(d)] = shell_count(quadratic_ordered, d, p)
        count_rows.append(row)
    write_rows(count_path, count_fields, count_rows)

    # Strong reconstruction check: C_d is the binomial lift of the support spectrum.
    for p in primes:
        for d in range(dmin, dmax + 1):
            reconstructed = sum(
                math.comb(d, s) * quadratic_ordered[s][p][s]
                for s in range(1, d + 1)
            )
            actual = shell_count(quadratic_ordered, d, p)
            if reconstructed != actual:
                raise AssertionError((p, d, reconstructed, actual))

    for path in [summary_path, spectrum_path, count_path, birth_path, long_path]:
        print(f"{path.name}\t{sha256(path)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=199)
    parser.add_argument("--d-min", type=int, default=2)
    parser.add_argument("--d-max", type=int, default=19)
    parser.add_argument("--out", type=Path, default=Path("highdim_prime_basin_out"))
    args = parser.parse_args()
    generate(args.max_n, args.d_min, args.d_max, args.out)
