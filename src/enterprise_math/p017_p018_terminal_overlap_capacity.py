"""Near-primorial overlap packing for the terminal even-J full-core residual.

At positive even J=J_perp(k), the terminal core-adaptive order is m=J-1 and
every surviving low-core row has a complete-core radical with exactly J
transverse odd primes and product <k.  The near-primorial replacement theorem
says that each such radical differs from the base first-J transverse-prime set
by at most T outsider replacements.

Take two residual radicals D_i,D_j.  Each omits at most T base primes, so they
share at least

    h = max(J-2T,0)

base primes.  The product of any h transverse primes is at least the product of
the first h transverse primes, denoted P_h.  Therefore

    gcd(D_i,D_j) >= P_h,

and the complete cores C_i,C_j satisfy the same lower bound.  P017 CG05 (or the
equivalent elementary divisor+parity spacing law) gives

    2 gcd(C_i,C_j) | x_i-x_j.

For distinct signed points this implies

    |x_i-x_j| >= 2 P_h.

All signed coordinates lie in [-(k-1),k-1], an interval of length 2(k-1), so
ordinary one-dimensional packing yields

    R_core_{J-1}(k)
      <= floor((k-1)/P_h)+1.

This is a genuine row-column joint inequality:

    near-primorial replacement depth
      -> forced prime overlap
      -> full-core gcd weight
      -> signed spacing
      -> residual-row capacity.

It is not by itself a Legendre proof, and it can be weak when 2T>=J.  Its value
is to identify the exact global-packing leverage that remains in CG05 after the
pairwise divisibility law itself has been recognized as tautological on
complete-core rows.
"""

from __future__ import annotations

from math import prod

from .p017_p018_near_primorial_shell import near_primorial_replacement_profile


def terminal_overlap_capacity(k: int) -> dict[str, object]:
    """Return the non-enumerative residual-row capacity from J and replacement depth T."""
    profile = near_primorial_replacement_profile(k)
    j = int(profile["transverse_primorial_depth"])
    if j <= 0 or profile["J_parity"] != "EVEN":
        raise ValueError("terminal overlap capacity requires positive even J_perp(k)")

    replacement_depth = int(profile["replacement_depth"])
    overlap_depth = max(j - 2 * replacement_depth, 0)
    base_primes = tuple(int(p) for p in profile["base_primorial_primes"])
    overlap_product = prod(base_primes[:overlap_depth]) if overlap_depth else 1
    capacity = (k - 1) // overlap_product + 1

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "terminal_order": j - 1,
        "replacement_depth": replacement_depth,
        "forced_common_base_prime_count": overlap_depth,
        "forced_common_product_floor": overlap_product,
        "minimum_signed_spacing": 2 * overlap_product,
        "terminal_residual_row_capacity": capacity,
        "nontrivial_overlap_bound": overlap_depth > 0,
        "base_primorial_primes": base_primes,
    }
