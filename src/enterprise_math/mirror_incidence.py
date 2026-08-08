"""Basin-level transverse-prime incidence for centered mirror pairs."""

from __future__ import annotations

from collections import defaultdict
from math import gcd

from .legendre import anchor_product
from .mirror import mirror_support_separation


def mirror_incidence_summary(k: int) -> dict[str, object]:
    """Reindex surviving mirror-pair support incidences by transverse prime.

    Let S_k={1<=r<=k-1:gcd(r,A_k)=1}.  The returned ``incidence_total`` is

        sum_{r in S_k} (omega_tr(M-r)+omega_tr(M+r)),

    and also the sum of per-prime incidence counts.  If every surviving mirror
    member were composite, root-factor horizon plus mirror separation would
    force this total to be at least 2*|S_k|.  The function reports that threshold
    but does not assume Legendre failure.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")

    anchor = anchor_product(k)
    surviving_radii: list[int] = []
    per_prime: dict[int, int] = defaultdict(int)
    pair_rows: list[dict[str, object]] = []
    incidence_total = 0

    for r in range(1, k):
        if gcd(r, anchor) != 1:
            continue
        surviving_radii.append(r)
        data = mirror_support_separation(k, r)
        lower_support = list(data["lower_support"])
        upper_support = list(data["upper_support"])
        if set(lower_support).intersection(upper_support):
            raise AssertionError("mirror supports unexpectedly overlap")
        for p in lower_support:
            per_prime[p] += 1
        for p in upper_support:
            per_prime[p] += 1
        pair_incidence = len(lower_support) + len(upper_support)
        incidence_total += pair_incidence
        pair_rows.append(
            {
                "radius": r,
                "lower": data["lower"],
                "upper": data["upper"],
                "lower_support": lower_support,
                "upper_support": upper_support,
                "incidence": pair_incidence,
            }
        )

    if incidence_total != sum(per_prime.values()):
        raise AssertionError("state-indexed and prime-indexed incidence sums disagree")

    return {
        "k": k,
        "anchor_product": anchor,
        "surviving_radii": surviving_radii,
        "surviving_pair_count": len(surviving_radii),
        "incidence_total": incidence_total,
        "all_composite_required_minimum": 2 * len(surviving_radii),
        "per_prime_incidence": dict(sorted(per_prime.items())),
        "pairs": pair_rows,
    }
