"""Finite diagnostic for local divisor-layer lift opportunities."""
from __future__ import annotations

import csv
from pathlib import Path

from enterprise_math.divisor_layer_lift import (
    is_squarefree_semiprime_small,
    neighborhood_profile,
    squarefree_prime_layer_encoder,
)

LIMITS = (1000, 2000, 5000, 10000, 20000)
RADII = (1, 2, 3, 4)


def rows() -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for limit in LIMITS:
        values = [n for n in range(20, limit) if is_squarefree_semiprime_small(n)]
        for radius in RADII:
            forcing = strong = tau6 = modal_strong = 0
            for n in values:
                profile = neighborhood_profile(n, radius)
                forcing += bool(profile.factor_forcing_layers)
                strong += bool(profile.strong_encoder_layers)
                tau6 += 6 in profile.strong_encoder_layers
                modal = profile.modal_layer
                modal_strong += bool(
                    modal and squarefree_prime_layer_encoder(2, modal) is not None
                )
            out.append(
                {
                    "limit_exclusive": limit,
                    "radius": radius,
                    "squarefree_semiprimes": len(values),
                    "any_factor_forcing": forcing,
                    "strong_2r_prime_layer": strong,
                    "tau6_neighbor": tau6,
                    "mode_strong_2r_prime_layer": modal_strong,
                    "strong_all_pct": strong / len(values),
                    "strong_mode_pct": modal_strong / len(values),
                    "all_over_mode_ratio": strong / modal_strong if modal_strong else "",
                }
            )
    return out


def write_csv(path: str | Path) -> None:
    data = rows()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    write_csv(
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "divisor_layer_lift_probe_20260908.csv"
    )
