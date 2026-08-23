#!/usr/bin/env python3
"""Cyclic ray-polynomial census for the Enterprise tri-sector allocation.

For a primitive S12 ray (u,v,0), gcd(u,v)=1, and m>=1, the fixed
tri-sector shell spiral sends the three cyclic rotations to quadratic labels

  F0(m) = B_{(u+v)m} + v m
  F1(m) = F0(m) + (u+v)m
  F2(m) = F0(m) + 2(u+v)m,

where B_r = 3r(r-1)/2 + 1.

The script measures per-slot prime rate, C3 imbalance, full-bright C3 count,
and complete-coverage gates at q=3,5,7. Placement is fixed before primality
is tested. Finite census statistics are not infinitude theorems.
"""

from __future__ import annotations

import argparse
import csv
import math
import statistics
from pathlib import Path

_MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in _MR_BASES:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def label(u: int, v: int, cyclic_slot: int, m: int) -> int:
    s = u + v
    r = s * m
    base = 3 * r * (r - 1) // 2 + 1
    return base + (cyclic_slot * s + v) * m


def saturated_gate(u: int, v: int, q: int) -> bool:
    for m in range(1, q):
        if all(label(u, v, k, m) % q for k in range(3)):
            return False
    return True


def census(max_sum: int, samples: int):
    rows = []
    for u in range(max_sum + 1):
        for v in range(max_sum + 1 - u):
            if u == v == 0 or math.gcd(u, v) != 1:
                continue
            counts = [0, 0, 0]
            triple_count = 0
            for m in range(1, samples + 1):
                flags = [is_prime(label(u, v, k, m)) for k in range(3)]
                for k, flag in enumerate(flags):
                    counts[k] += int(flag)
                triple_count += int(all(flags))
            rates = [c / samples for c in counts]
            mean = statistics.mean(rates)
            cv = statistics.pstdev(rates) / mean if mean else 0.0
            gates = [q for q in (3, 5, 7) if saturated_gate(u, v, q)]
            gate_product = math.prod(gates)
            rows.append({
                "u": u,
                "v": v,
                "complexity_u_plus_v": u + v,
                "samples_per_slot": samples,
                "slot0_prime_count": counts[0],
                "slot1_prime_count": counts[1],
                "slot2_prime_count": counts[2],
                "slot0_rate": rates[0],
                "slot1_rate": rates[1],
                "slot2_rate": rates[2],
                "mean_rate": mean,
                "c3_cv": cv,
                "full_c3_prime_count": triple_count,
                "saturated_gates": "*".join(map(str, gates)),
                "gate_product": gate_product,
            })
    return rows


def pareto_front(rows):
    out = []
    for r in rows:
        dominated = False
        for s in rows:
            if (
                s["mean_rate"] >= r["mean_rate"]
                and s["c3_cv"] <= r["c3_cv"]
                and (
                    s["mean_rate"] > r["mean_rate"]
                    or s["c3_cv"] < r["c3_cv"]
                )
            ):
                dominated = True
                break
        if not dominated:
            out.append(r)
    return out


def run(max_sum: int, samples: int, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    rows = census(max_sum, samples)
    rows.sort(key=lambda r: (-r["mean_rate"], r["c3_cv"], r["complexity_u_plus_v"]))
    path = out / f"ray_census_sum{max_sum}_m{samples}.csv"
    fields = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    midpoint = next(r for r in rows if r["u"] == r["v"] == 1)
    front = pareto_front(rows)
    midpoint_dominated = midpoint not in front

    maximal_gate = [r for r in rows if r["gate_product"] == 105]
    min_gate_complexity = min(r["complexity_u_plus_v"] for r in maximal_gate)
    min_gate_classes = [
        (r["u"], r["v"])
        for r in maximal_gate
        if r["complexity_u_plus_v"] == min_gate_complexity
    ]

    print(f"RAYS={len(rows)}")
    print(f"CSV={path}")
    print(
        "MIDPOINT="
        f"counts={midpoint['slot0_prime_count']}/"
        f"{midpoint['slot1_prime_count']}/"
        f"{midpoint['slot2_prime_count']},"
        f"mean={midpoint['mean_rate']:.12f},"
        f"cv={midpoint['c3_cv']:.12f},"
        f"gate={midpoint['gate_product']},"
        f"pareto={not midpoint_dominated}"
    )
    print(f"MAX_GATE_CLASSES={len(maximal_gate)}")
    print(f"MIN_MAX_GATE_COMPLEXITY={min_gate_complexity}")
    print(f"MIN_MAX_GATE_CLASSES={min_gate_classes}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-sum", type=int, default=10)
    parser.add_argument("--samples", type=int, default=1500)
    parser.add_argument("--out", type=Path, default=Path("native_enterprise_ray_out"))
    args = parser.parse_args()
    run(args.max_sum, args.samples, args.out)
