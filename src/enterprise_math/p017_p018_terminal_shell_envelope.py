"""Replacement-depth envelope for the even-J terminal full-core/tail shell.

The exact near-primorial shell can be enumerated, but its geometry also gives a
non-row-scanning upper bound depending only on local prime-prefix data.

Let B={p_1,...,p_J} be the base transverse-prime prefix with product P_J<k and
let T be the replacement depth.  For a radical at exact replacement depth s,
choose the omitted base set O (|O|=s) and the outsider set V (|V|=s).  The exact
condition is

    P_J * product(V) < k * product(O).

For s>=1, after designating the largest outsider, the other s-1 outsiders are at
least the first s-1 outsider primes p_{J+1},...,p_{J+s-1}.  Therefore every
outsider lies below the local integer cutoff

    U_O = floor((k*product(O)-1) /
                (P_J * product_{t=1}^{s-1} p_{J+t})).

If N_O is the number of transverse outsider primes in (p_J,U_O], the number of
possible outsider s-sets is at most binom(N_O,s).  Hence

    B_s = sum_{O subset B, |O|=s} binom(N_O,s)

is an upper bound for the number of terminal radicals at depth s.  It enumerates
only the small omitted-base subsets and local prime cutoffs, not terminal
radicals or square-basin states.

Let R_s be the minimum radical at replacement depth s.  If a complete core has
h extra prime-multiplicity units beyond its radical, then

    A >= R_s * p_1^h.

Thus

    H_s=max{h:R_s*p_1^h<=k-1}

and the number of exponent vectors above one radical is at most

    binom(J+H_s,H_s).

Finally every terminal tail window attached to A>=R_s has

    |W_A| <= floor(2k/R_s)+1.

Combining the three independent finite resources gives

    W_terminal
      <= sum_{s=0}^T
           B_s * binom(J+H_s,H_s) * (floor(2k/R_s)+1).

This is a rigorous envelope for the total *integer* mass of the disjoint terminal
tail windows.  It uses no primality distribution theorem and does not prove that
those windows contain few primes; the exact terminal residual is at most this
integer mass automatically.

The bound is intentionally stronger than multiplying one worst-case shell size
by one worst-case window width.  It records how replacement depth itself raises
the minimum product and simultaneously reduces both power multiplicity and tail
window width.
"""

from __future__ import annotations

from itertools import combinations
from math import comb, prod

from .legendre import is_prime
from .p017_p018_near_primorial_shell import near_primorial_replacement_profile


def _transverse_outsider_count(k: int, lower_exclusive: int, upper_inclusive: int) -> int:
    if upper_inclusive <= lower_exclusive:
        return 0
    center = k * (k + 1)
    count = 0
    candidate = lower_exclusive + 1
    if candidate <= 2:
        candidate = 3
    if candidate % 2 == 0:
        candidate += 1
    upper = min(k, upper_inclusive)
    while candidate <= upper:
        if center % candidate != 0 and is_prime(candidate):
            count += 1
        candidate += 2
    return count


def _power_depth_from_minimum(k: int, minimum_radical: int, smallest_prime: int) -> int:
    depth = 0
    value = minimum_radical
    while value <= (k - 1) // smallest_prime:
        value *= smallest_prime
        depth += 1
    return depth


def terminal_replacement_depth_envelope(k: int) -> dict[str, object]:
    """Return the depth-by-depth radical/full-core/window envelope."""
    profile = near_primorial_replacement_profile(k)
    j = int(profile["transverse_primorial_depth"])
    depth = int(profile["replacement_depth"])
    base_primes = tuple(int(p) for p in profile["base_primorial_primes"])
    base = int(profile["base_primorial_product"])
    if not base_primes or j != len(base_primes):
        raise AssertionError("terminal base prime prefix is inconsistent")
    smallest = base_primes[0]
    largest_base = base_primes[-1]

    replacement_rows = {
        int(row["replacements"]): row
        for row in profile["replacement_rows"]
        if bool(row["feasible_below_k"])
    }
    rows: list[dict[str, object]] = []
    total_radical_bound = 0
    total_full_core_bound = 0
    total_window_bound = 0

    for replacements in range(depth + 1):
        minimum_row = replacement_rows[replacements]
        minimum_radical = int(minimum_row["minimum_product"])
        if replacements == 0:
            radical_bound = 1
            omitted_rows: tuple[dict[str, object], ...] = ()
        else:
            outsider_prefix = tuple(
                int(p) for p in minimum_row["minimum_outside_primes"]
            )
            smaller_outsider_product = (
                prod(outsider_prefix[:-1]) if replacements > 1 else 1
            )
            omitted_data: list[dict[str, object]] = []
            radical_bound = 0
            for omitted in combinations(base_primes, replacements):
                omitted_product = prod(omitted)
                denominator = base * smaller_outsider_product
                cutoff = (k * omitted_product - 1) // denominator
                outsider_count = _transverse_outsider_count(
                    k,
                    largest_base,
                    cutoff,
                )
                candidate_bound = (
                    comb(outsider_count, replacements)
                    if outsider_count >= replacements
                    else 0
                )
                radical_bound += candidate_bound
                omitted_data.append(
                    {
                        "omitted_base_primes": tuple(omitted),
                        "omitted_product": omitted_product,
                        "outsider_cutoff": cutoff,
                        "eligible_outsider_prime_count": outsider_count,
                        "outsider_subset_bound": candidate_bound,
                    }
                )
            omitted_rows = tuple(omitted_data)

        power_depth = _power_depth_from_minimum(k, minimum_radical, smallest)
        exponent_pattern_bound = comb(j + power_depth, power_depth)
        full_core_bound = radical_bound * exponent_pattern_bound
        per_window_bound = (2 * k) // minimum_radical + 1
        window_mass_bound = full_core_bound * per_window_bound

        total_radical_bound += radical_bound
        total_full_core_bound += full_core_bound
        total_window_bound += window_mass_bound
        rows.append(
            {
                "replacement_depth": replacements,
                "minimum_radical": minimum_radical,
                "radical_candidate_bound": radical_bound,
                "power_depth_bound": power_depth,
                "exponent_pattern_bound_per_radical": exponent_pattern_bound,
                "full_core_candidate_bound": full_core_bound,
                "per_window_integer_mass_bound": per_window_bound,
                "terminal_window_integer_mass_bound": window_mass_bound,
                "omitted_set_rows": omitted_rows,
            }
        )

    return {
        **profile,
        "envelope_rows": tuple(rows),
        "terminal_radical_candidate_bound": total_radical_bound,
        "terminal_full_core_candidate_bound": total_full_core_bound,
        "terminal_window_integer_mass_bound": total_window_bound,
        "bound_is_basin_row_independent": True,
    }
