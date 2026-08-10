"""Finite near-primorial full-core shell for the even-J terminal residual.

At positive even J=J_perp(k), terminal order m=J-1 leaves exactly one residual
bit on each low complete-core row.  Such a row has a complete transverse core A
with

    A <= k-1,
    omega(rad A)=J.

The near-primorial replacement theorem enumerates *all* possible J-prime
radicals R<k.  For a fixed radical R with support primes p_i, every complete core
has the unique form

    A = R * product p_i^{f_i},   f_i>=0,

subject only to A<=k-1.  Therefore the entire terminal low-core shell is a finite
radical-replacement × prime-power lattice independent of the rest of the square
basin.

The prime-power direction also has a scale-wide analytic ceiling.  Let P_J be
the minimum J-prime transverse radical and p_1 the smallest transverse prime.
If A contains h prime-multiplicity units beyond its radical, then

    A >= P_J * p_1^h.

Thus

    h <= H_pow(k)=max{h : P_J*p_1^h <= k-1}.

When H_pow=0 the complete terminal shell is forced squarefree before any state
enumeration.  Together with the replacement depth T this gives a two-coordinate
finite shell `(replacement depth, power depth)`.

For every candidate A, the exact anchor-surviving signed divisor fiber
F_surv(A) is available from the anchor-Möbius centered-boundary layer.  Since a
terminal row with complete core A must lie in that divisor fiber,

    R_terminal(k) <= sum_A F_surv(A).

This already gives a finite non-row-scanning capacity.  Consuming the exact
all-support full-core incidence I_full(A) yields the stronger identity

    R_terminal(k) = sum_A I_full(A),

because every candidate A has exactly J support directions and hence terminal
Bonferroni defect one, while every terminal residual row has exactly one such
complete core.

The equality is a representation theorem, not a uniform Legendre deficit.  The
capacity sum is intended as the cheaper pressure object; exact I_full(A) may
still require a nontrivial Möbius calculation.
"""

from __future__ import annotations

from .p017_p018_full_core_incidence import full_core_incidence_mobius
from .p017_p018_near_primorial_shell import (
    near_primorial_radical_candidates,
    near_primorial_replacement_profile,
)
from .p017_p018_signed_boundary_carry import anchor_surviving_divisor_boundary_carry


def terminal_power_depth_ceiling(k: int) -> dict[str, object]:
    """Return H_pow=max{h:P_J*p_1^h<=k-1} for the even-J terminal shell."""
    profile = near_primorial_replacement_profile(k)
    base = int(profile["base_primorial_product"])
    primes = tuple(int(p) for p in profile["base_primorial_primes"])
    if not primes:
        raise AssertionError("positive even J has no base transverse prime")
    smallest = primes[0]

    depth = 0
    value = base
    while value <= (k - 1) // smallest:
        value *= smallest
        depth += 1
    first_forbidden = value * smallest if depth == 0 else value * smallest
    # `value` is P_J*p_1^depth and fits.  One further p_1 does not.
    if value > k - 1:
        raise AssertionError("power-depth loop ended on a non-fitting product")
    if value * smallest <= k - 1:
        raise AssertionError("power-depth ceiling is not maximal")

    return {
        **profile,
        "smallest_transverse_prime": smallest,
        "power_depth_ceiling": depth,
        "largest_minimum_power_product": value,
        "first_forbidden_power_product": value * smallest,
        "terminal_shell_forced_squarefree": depth == 0,
    }


def _full_blocks_for_support(k: int, primes: tuple[int, ...]) -> tuple[int, ...]:
    """Enumerate all A<=k-1 with exactly the declared radical support."""
    if not primes:
        return ()
    values: list[int] = []

    def extend(index: int, current: int) -> None:
        if index == len(primes):
            values.append(current)
            return
        prime = primes[index]
        value = current * prime
        while value <= k - 1:
            extend(index + 1, value)
            if value > (k - 1) // prime:
                break
            value *= prime

    extend(0, 1)
    return tuple(sorted(values))


def terminal_full_core_candidates(k: int) -> dict[str, object]:
    """Enumerate the complete finite A-shell of even-J terminal low cores."""
    radicals = near_primorial_radical_candidates(k)
    j = int(radicals["transverse_primorial_depth"])
    if j <= 0 or radicals["J_parity"] != "EVEN":
        raise ValueError("terminal full-core shell requires positive even J_perp(k)")
    power_bound = terminal_power_depth_ceiling(k)

    rows: list[dict[str, object]] = []
    seen: set[int] = set()
    power_depth = 0
    for radical_row in radicals["candidate_rows"]:
        radical = int(radical_row["radical"])
        primes = tuple(int(p) for p in radical_row["radical_primes"])
        blocks = _full_blocks_for_support(k, primes)
        if radical not in blocks:
            raise AssertionError("terminal radical failed to appear as its squarefree full block")
        for full_block in blocks:
            if full_block in seen:
                raise AssertionError("distinct radical rows produced the same full core")
            seen.add(full_block)
            quotient = full_block // radical
            extra = 0
            remaining = quotient
            for prime in primes:
                while remaining % prime == 0:
                    remaining //= prime
                    extra += 1
            if remaining != 1:
                raise AssertionError("full block acquired a prime outside its radical support")
            if extra > int(power_bound["power_depth_ceiling"]):
                raise AssertionError("enumerated terminal block exceeded the analytic power-depth ceiling")
            power_depth = max(power_depth, extra)
            rows.append(
                {
                    "full_core": full_block,
                    "radical": radical,
                    "radical_primes": primes,
                    "replacement_depth": int(radical_row["replacements"]),
                    "extra_prime_multiplicity": extra,
                }
            )

    rows.sort(key=lambda row: int(row["full_core"]))
    if bool(power_bound["terminal_shell_forced_squarefree"]) and power_depth != 0:
        raise AssertionError("analytic squarefree terminal shell produced a powered full core")
    return {
        **radicals,
        "power_depth_ceiling": int(power_bound["power_depth_ceiling"]),
        "smallest_transverse_prime": int(power_bound["smallest_transverse_prime"]),
        "full_core_rows": tuple(rows),
        "full_core_candidates": tuple(int(row["full_core"]) for row in rows),
        "full_core_candidate_count": len(rows),
        "maximum_extra_prime_multiplicity": power_depth,
        "terminal_shell_squarefree": power_depth == 0,
        "terminal_shell_forced_squarefree": bool(power_bound["terminal_shell_forced_squarefree"]),
    }


def terminal_shell_divisor_capacity(k: int) -> dict[str, object]:
    """Upper-bound terminal residual rows by exact anchor-surviving A-divisor fibers."""
    shell = terminal_full_core_candidates(k)
    rows: list[dict[str, object]] = []
    total = 0
    for full_core in shell["full_core_candidates"]:
        data = anchor_surviving_divisor_boundary_carry(k, int(full_core))
        capacity = int(data["anchor_surviving_fiber_size"])
        total += capacity
        rows.append(
            {
                "full_core": int(full_core),
                "anchor_surviving_divisor_capacity": capacity,
                "raw_divisor_capacity": int(data["raw_signed_fiber_size"]),
                "effective_odd_anchor_primes": tuple(data["effective_odd_anchor_primes"]),
            }
        )
    return {
        **shell,
        "capacity_rows": tuple(rows),
        "terminal_residual_divisor_capacity": total,
    }


def terminal_shell_exact_incidence(k: int, *, verify_direct: bool = False) -> dict[str, object]:
    """Evaluate the exact terminal residual identity through I_full(A)."""
    shell = terminal_full_core_candidates(k)
    rows: list[dict[str, object]] = []
    total = 0
    for full_core in shell["full_core_candidates"]:
        data = full_core_incidence_mobius(k, int(full_core), verify_direct=verify_direct)
        count = int(data["full_core_incidence"])
        total += count
        if count:
            rows.append(
                {
                    "full_core": int(full_core),
                    "full_core_incidence": count,
                    "support_primes": tuple(data["support_primes"]),
                }
            )
    return {
        **shell,
        "nonzero_full_core_rows": tuple(rows),
        "terminal_residual_exact_incidence": total,
        "terminal_residual_identity": True,
    }
