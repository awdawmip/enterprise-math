"""Generation 3: the minimal-P2 rough endpoint freezes nontrivial bilinear Möbius sign.

Let z2=floor((k^2+2k)^(1/3)).  Every z2-rough square-shell state has
Omega<=2, and every rough composite is a squarefree semiprime (there is no
perfect square strictly between consecutive squares).

Now suppose a z2-rough state t in the shell has a nontrivial factorization

    t = m*n,  m>1, n>1.

Each factor contributes at least one prime factor.  Since Omega(t)<=2, both m
and n must be prime.  Since t is not a square, they are distinct.  Therefore

    mu(t)=mu(mn)=+1.

Thus any FI-shaped bilinear form restricted *after* the minimal-P2 rough sieve,
with both factor variables in nontrivial ranges, has frozen state Möbius sign.
It cannot obtain parity-breaking cancellation from mu(mn) itself.  Prime states
have no nontrivial factorization and are absent from such ranges.

Consequently the Friedlander--Iwaniec parity resource must be consumed before
this final rough restriction (or through an equivalent descent identity which
retains mixed-Omega states).  This is a structural explanation of why the P2
root cutoff is a parity endpoint rather than merely another bilinear layer.

The theorem does not say every possible weighted bilinear expression is
nonnegative: auxiliary coefficients such as gamma(n,C) may have signs.  It says
specifically that the **state Möbius factor mu(mn)** is identically +1 on every
nontrivial factorization of the final z2-rough support.
"""

from __future__ import annotations

from .p017_p018_p2_parity_endpoint import p2_parity_endpoint
from .p017_p018_square_parity_bilinear_target import mobius


def p2_nontrivial_factorization_sign_freeze(k: int) -> dict[str, object]:
    """Reconstruct every nontrivial factorization of z2-rough shell states."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")

    endpoint = p2_parity_endpoint(k)
    rows: list[tuple[int, int, int, int]] = []

    for p, q, value, offset in endpoint["semiprime_rows"]:
        if p <= 1 or q <= 1 or p == q:
            raise AssertionError("P2 endpoint semiprime lost its nontrivial distinct factors")
        if mobius(value) != 1:
            raise AssertionError("P2 rough semiprime did not have positive Möbius sign")
        rows.append((p, q, value, offset))
        rows.append((q, p, value, offset))

    # Prime rough rows intentionally generate no m,n>1 factorization rows.
    return {
        "k": k,
        "p2_cutoff": endpoint["p2_cutoff"],
        "rough_count": endpoint["rough_count"],
        "prime_count": endpoint["prime_count"],
        "semiprime_count": endpoint["semiprime_count"],
        "ordered_nontrivial_factorization_rows": tuple(rows),
        "ordered_nontrivial_factorization_count": len(rows),
        "all_state_mobius_signs_positive": True,
        "prime_states_have_no_nontrivial_factorization": True,
        "status": "P2_BILINEAR_MOBIUS_SIGN_FREEZE",
    }
