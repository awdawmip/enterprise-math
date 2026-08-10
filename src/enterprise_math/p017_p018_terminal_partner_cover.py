"""Reduced terminal-residual partner cover by high-product sign-split tokens.

This finite certificate starts *after* the near-primorial terminal reduction.  It
never scans all 2k signed basin states.

For every terminal low-core residual point x, let A be the squarefree transverse
support radical of the residual side M-x.  Inspect only the mirror partner M+x.
Because the partner lies in the same square basin, any composite partner has a
prime divisor p<=k.  Anchor survival makes p transverse, and mirror separation
makes p absent from A.

Thus exactly one of two routes occurs:

1. no transverse p<=k divides M+x.  The square-root factor horizon certifies
   that M+x is prime;
2. choose the least such p.  Then the sign-split pair token (A,p) satisfies

       A | M-x,   p | M+x,
       A*p >= P_perp(k,J+1) >= k.

   Parity and CRT place the token in one class modulo 2*A*p.  Since the signed
   interval has diameter 2k-2 < 2*A*p, this sign-split token is globally
   single-use.

Hence the terminal residual set is partitioned into direct prime-partner
witnesses and single-use high-product pair tokens.  This is a reduced finite
certificate and a routing theorem, not a uniform Legendre proof: the high-token
branch can still cover every residual point at some scales.
"""

from __future__ import annotations

from math import prod

from .legendre import primes_up_to
from .p017_p018_near_primorial_shell import near_primorial_replacement_profile
from .p017_p018_terminal_candidate_exact import terminal_candidate_exact_profile


def terminal_partner_cover_profile(k: int) -> dict[str, object]:
    """Partition reduced terminal residual points into prime and high-token routes."""
    residual = terminal_candidate_exact_profile(k)
    profile = near_primorial_replacement_profile(k)
    j = int(residual["transverse_primorial_depth"])
    if j != int(profile["transverse_primorial_depth"]):
        raise AssertionError("terminal candidate and near-primorial depths disagree")

    center = k * (k + 1)
    transverse = tuple(
        p for p in primes_up_to(k)
        if p % 2 == 1 and center % p != 0
    )
    blocking = profile["blocking_prime"]
    next_primorial = (
        None
        if blocking is None
        else int(profile["base_primorial_product"]) * int(blocking)
    )

    rows_by_point = {
        int(row["signed_point"]): row
        for row in residual["rows"]
        if row["terminal_low_core_residual"]
    }
    rows: list[dict[str, object]] = []
    prime_points: list[int] = []
    high_points: list[int] = []
    high_tokens: list[tuple[int, int, int]] = []

    for point in residual["terminal_residual_points"]:
        x = int(point)
        row = rows_by_point[x]
        support = tuple(int(p) for p in row["support"])
        radical = int(row["support_radical"])
        if radical != prod(support):
            raise AssertionError("terminal support radical does not equal support product")
        partner = center + x

        partner_prime = None
        for prime in transverse:
            if partner % prime == 0:
                partner_prime = prime
                break

        if partner_prime is None:
            # Any composite integer <(k+1)^2 has a prime factor <=k.  The
            # anchor-surviving odd mirror partner has no anchor factor, so the
            # absence of a transverse factor through k certifies primality.
            if not (k * k < partner < (k + 1) * (k + 1)):
                raise AssertionError("mirror partner left the open square basin")
            prime_points.append(x)
            rows.append(
                {
                    "signed_point": x,
                    "support_radical": radical,
                    "partner": partner,
                    "route": "PRIME_PARTNER_WITNESS",
                    "least_partner_transverse_prime": None,
                }
            )
            continue

        p = int(partner_prime)
        if p in support:
            raise AssertionError("mirror partner reused a transverse prime from the residual side")
        if (center - x) % radical or (center + x) % p:
            raise AssertionError("high-product sign-split token lost one of its side divisibilities")
        token = radical * p
        if next_primorial is None:
            raise AssertionError("composite partner exists but no (J+1)-st transverse prime is available")
        if token < next_primorial or next_primorial < k:
            raise AssertionError("terminal partner token fell below the next transverse primorial")
        if 2 * token <= 2 * k - 2:
            raise AssertionError("high-product sign-split token is not globally single-use")

        high_points.append(x)
        high_tokens.append((radical, p, x))
        rows.append(
            {
                "signed_point": x,
                "support_radical": radical,
                "partner": partner,
                "route": "HIGH_PRODUCT_PAIR_TOKEN",
                "least_partner_transverse_prime": p,
                "pair_token_product": token,
                "pair_token_period": 2 * token,
                "pair_token_single_use": True,
            }
        )

    if len(rows) != int(residual["terminal_residual_count"]):
        raise AssertionError("terminal partner cover lost residual rows")
    if set(prime_points).intersection(high_points):
        raise AssertionError("terminal partner routes are not disjoint")

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "terminal_residual_count": int(residual["terminal_residual_count"]),
        "prime_partner_witness_count": len(prime_points),
        "high_product_pair_token_count": len(high_points),
        "prime_partner_witness_points": tuple(prime_points),
        "high_product_pair_points": tuple(high_points),
        "high_product_pair_tokens": tuple(high_tokens),
        "next_transverse_primorial": next_primorial,
        "prime_witness_certified": bool(prime_points),
        "rows": tuple(rows),
    }
