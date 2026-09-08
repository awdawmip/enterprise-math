"""Finite small-N probe for the beyond-horizon neighbor-square shortcut."""
from __future__ import annotations

import csv
from pathlib import Path

from enterprise_math.brc_neighbor_square_lift_shortcut import (
    try_power2_neighbor_square_shortcuts,
)

LIMITS = (100_000, 500_000, 2_000_000)


def _smallest_prime_factor_sieve(limit: int) -> list[int]:
    spf = list(range(limit))
    if limit > 1:
        spf[1] = 1
    for p in range(2, int((limit - 1) ** 0.5) + 1):
        if spf[p] != p:
            continue
        start = p * p
        for x in range(start, limit, p):
            if spf[x] == x:
                spf[x] = p
    return spf


def _is_squarefree_semiprime(n: int, spf: list[int]) -> bool:
    p = spf[n]
    if p <= 1 or n % p:
        return False
    q = n // p
    return q != p and q > 1 and spf[q] == q


def rows() -> list[dict[str, int]]:
    largest = max(LIMITS)
    spf = _smallest_prime_factor_sieve(largest)
    out: list[dict[str, int]] = []
    for limit in LIMITS:
        semiprimes = triggers = square_hits = factor_hits = 0
        for n in range(15, limit, 2):
            if not _is_squarefree_semiprime(n, spf):
                continue
            semiprimes += 1
            probes = try_power2_neighbor_square_shortcuts(
                n,
                ordinary_horizon=100,
            )
            triggers += len(probes)
            square_hits += sum(probe.square_hit for probe in probes)
            factor_hits += sum(probe.factor_hit for probe in probes)
        out.append({
            "limit": limit,
            "squarefree_odd_semiprimes": semiprimes,
            "beyond_100_triggers": triggers,
            "square_hits": square_hits,
            "factor_hits": factor_hits,
        })
    return out


def write_csv(path: str | Path) -> None:
    data = rows()
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    write_csv(
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_neighbor_square_lift_probe_20260908.csv"
    )
