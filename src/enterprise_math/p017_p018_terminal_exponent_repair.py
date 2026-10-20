"""Prime-power repair depth of the terminal near-primorial core shell.

At positive even J=J_perp(k), terminal low-core rows have exactly J distinct
transverse small primes and complete transverse core C<k.  The near-primorial
shell supplies the squarefree radical D=rad(C), with D>=P_J where P_J is the
product of the first J transverse odd primes.

Write

    C = D * product_{p|D} p^{a_p}

and let

    e(C) = sum_{p|D} a_p = Omega(C)-J

be the number of extra prime-power exponent units beyond the squarefree radical.
If p_1 is the smallest transverse odd prime, every extra unit multiplies by at
least p_1.  Hence

    P_J * p_1^e(C) <= C < k.

Define the uniform terminal exponent-repair depth

    E_pow(k) = max{e>=0 : P_J*p_1^e < k}.

Then every terminal low core satisfies e(C)<=E_pow(k).  In particular
E_pow(k)=0 forces **prime-power rigidity**: every low terminal complete core is
squarefree and equals its radical.

For one candidate radical D with least support prime p_min(D), the sharper local
depth E_D is defined by D*p_min(D)^e<k.  The exponent vector has J nonnegative
coordinates and total at most E_D, so the number of possible complete-core
lifts above D is at most

    binom(J+E_D, E_D).

This is a finite multiplicity-repair coordinate complementary to the
near-primorial support-replacement depth T.  It is not a Legendre proof.
"""

from __future__ import annotations

from math import comb

from .p017_p018_near_primorial_shell import near_primorial_radical_candidates


def _multiplicative_depth(base: int, prime: int, limit: int) -> int:
    if base <= 0 or prime < 2 or limit <= 0:
        raise ValueError("base, prime, and limit must be positive with prime>=2")
    depth = 0
    value = base
    while value <= (limit - 1) // prime:
        value *= prime
        depth += 1
    return depth


def terminal_exponent_repair_profile(k: int) -> dict[str, object]:
    """Return global and per-radical prime-power repair depths below k."""
    data = near_primorial_radical_candidates(k)
    j = int(data["transverse_primorial_depth"])
    if j <= 0 or data["J_parity"] != "EVEN":
        raise ValueError("terminal exponent repair requires positive even J_perp(k)")

    base_primes = tuple(int(p) for p in data["base_primorial_primes"])
    base = int(data["base_primorial_product"])
    smallest = base_primes[0]
    global_depth = _multiplicative_depth(base, smallest, k)

    rows: list[dict[str, object]] = []
    candidate_core_upper_bound = 0
    for row in data["candidate_rows"]:
        radical = int(row["radical"])
        support = tuple(int(p) for p in row["radical_primes"])
        if len(support) != j:
            raise AssertionError("terminal radical has wrong support size")
        local_depth = _multiplicative_depth(radical, support[0], k)
        if local_depth > global_depth:
            raise AssertionError("local exponent depth exceeded the global repair depth")
        lift_count_bound = comb(j + local_depth, local_depth)
        candidate_core_upper_bound += lift_count_bound
        rows.append(
            {
                "radical": radical,
                "support": support,
                "least_support_prime": support[0],
                "local_exponent_repair_depth": local_depth,
                "complete_core_lift_count_bound": lift_count_bound,
                "locally_prime_power_rigid": local_depth == 0,
            }
        )

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "support_replacement_depth": int(data["replacement_depth"]),
        "base_primorial_product": base,
        "smallest_transverse_prime": smallest,
        "global_exponent_repair_depth": global_depth,
        "globally_prime_power_rigid": global_depth == 0,
        "candidate_radical_count": int(data["candidate_count"]),
        "complete_core_candidate_count_upper_bound": candidate_core_upper_bound,
        "radical_rows": tuple(rows),
    }
