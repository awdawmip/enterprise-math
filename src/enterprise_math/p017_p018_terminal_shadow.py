"""Deterministic terminal shadow and counterexample saturation.

The half-cutoff decomposition leaves two kinds of states in the consecutive-
square interval: actual primes and semiprimes ``p*q`` with

    k/2 < p <= k < q < 2k+4.

Before testing whether ``q`` is prime, each high prime ``p`` already determines
one or two *odd reciprocal candidates*.  Their offsets form a deterministic
shadow ``C_k``.  The decisive set identity is

    PrimeOffsets(k) = HalfRoughOffsets(k) \ C_k.

Indeed every half-rough composite belongs to the shadow by the terminal
Buchstab classification.  Conversely, if a shadow state ``p*q`` is half-rough
then ``q`` must be prime: for k>=10, a composite q<2k+4 has a prime factor at
most sqrt(2k+3)<=k/2, contradicting half-roughness.

Thus a Legendre counterexample at k is equivalent, inside this half-cutoff
language, to complete shadow saturation

    HalfRoughOffsets(k) subseteq C_k.

This is still an exact reformulation rather than a proof.  It is useful because
it separates the two missing analytic tasks cleanly: lower-bound the half-rough
set, or upper-bound/avoid its deterministic reciprocal shadow.

The reciprocal geometry is almost involutive.  Let Phi_k(x) be the least odd
integer strictly greater than k^2/x.  For a high prime p the shadow candidates
are Phi_k(p) and, when it still lies in the interval, Phi_k(p)+2.  Conversely
for *every* shadow edge p*q in the interval,

    Phi_k(q)=p,

because 0 < p-k^2/q <= 2k/q < 2 and odd integers are spaced by two.

The optional second candidate is also an exact discrete shell-edge event.  If
``a=k-p`` and ``u=floor(a^2/(2p))``, it occurs exactly when

    floor((a+1)^2/(2p)) = u+1.

No prime-distribution assertion is hidden in these identities.
"""

from __future__ import annotations

from .legendre import is_prime, primes_up_to
from .p017_p018_square_anchor_sieve_diagonal import half_cutoff_rough_decomposition
from .p017_p018_terminal_buchstab import high_prime_odd_quotient_candidates


def odd_reciprocal_successor(k: int, x: int) -> int:
    """Return the least odd integer strictly greater than k^2/x."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    if isinstance(x, bool) or not isinstance(x, int) or x <= 0:
        raise ValueError("x must be a positive integer")
    quotient, _remainder = divmod(k * k, x)
    candidate = quotient + 1
    if candidate % 2 == 0:
        candidate += 1
    if not (candidate * x > k * k):
        raise AssertionError("reciprocal successor did not clear the square anchor")
    if candidate >= 3 and (candidate - 2) * x > k * k:
        raise AssertionError("reciprocal successor was not the least odd successor")
    return candidate


def terminal_candidate_shadow(k: int) -> dict[str, object]:
    """Build the high-prime reciprocal shadow without testing cofactor primality."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")

    high_primes = tuple(p for p in primes_up_to(k) if 2 * p > k)
    shadow_edges: list[tuple[int, int, int, int]] = []
    shell_crossings: list[tuple[int, int]] = []

    for p in high_primes:
        data = high_prime_odd_quotient_candidates(k, p)
        candidates = data["candidates"]
        reciprocal = odd_reciprocal_successor(k, p)
        if int(candidates[0]["q"]) != reciprocal:
            raise AssertionError("primary candidate is not the reciprocal successor")

        a = int(data["a"])
        shell_index = int(data["shell_index"])
        crossing = ((a + 1) * (a + 1)) // (2 * p) == shell_index + 1
        if crossing != bool(data["double_candidate"]):
            raise AssertionError("double candidate lost its shell-edge criterion")
        if crossing:
            shell_crossings.append((p, shell_index))

        for item in candidates:
            q = int(item["q"])
            offset = int(item["offset"])
            if odd_reciprocal_successor(k, q) != p:
                raise AssertionError("terminal reciprocal edge lost its reverse map")
            shadow_edges.append((p, q, k * k + offset, offset))

    # Different high primes may generate the same composite shadow state only
    # when an additional small factor is present; the shadow is a set of offsets.
    shadow_offsets = tuple(sorted({offset for _p, _q, _n, offset in shadow_edges}))

    return {
        "k": k,
        "high_primes": high_primes,
        "shadow_edges": tuple(sorted(shadow_edges)),
        "shadow_offsets": shadow_offsets,
        "shadow_count": len(shadow_offsets),
        "shell_crossings": tuple(shell_crossings),
        "near_involution_verified": True,
    }


def half_rough_shadow_saturation(k: int) -> dict[str, object]:
    """Verify PrimeOffsets = HalfRoughOffsets \ TerminalShadow exactly."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")

    half = half_cutoff_rough_decomposition(k)
    shadow = terminal_candidate_shadow(k)

    half_rough = set(int(r) for r in half["half_rough_offsets"])
    shadow_offsets = set(int(r) for r in shadow["shadow_offsets"])
    prime_offsets = set(int(r) for r in half["prime_offsets"])
    semiprime_offsets = set(int(edge[3]) for edge in half["semiprime_edges"])

    if half_rough - shadow_offsets != prime_offsets:
        raise AssertionError("half-rough minus shadow failed to recover prime offsets")
    if half_rough & shadow_offsets != semiprime_offsets:
        raise AssertionError("half-rough shadow intersection is not the semiprime tail")

    # Directly verify the nontrivial converse used above: a half-rough shadow
    # candidate has prime cofactor.
    shadow_by_offset: dict[int, list[tuple[int, int]]] = {}
    for p, q, _value, offset in shadow["shadow_edges"]:
        shadow_by_offset.setdefault(int(offset), []).append((int(p), int(q)))
    for offset in half_rough & shadow_offsets:
        if not any(is_prime(q) for _p, q in shadow_by_offset[offset]):
            raise AssertionError("half-rough shadow state has no prime cofactor")

    saturated = half_rough <= shadow_offsets
    counterexample = not prime_offsets
    if saturated != counterexample:
        raise AssertionError("shadow saturation is not equivalent to prime-gap failure")

    return {
        **shadow,
        "half_rough_offsets": tuple(sorted(half_rough)),
        "half_rough_count": len(half_rough),
        "prime_offsets": tuple(sorted(prime_offsets)),
        "prime_count": len(prime_offsets),
        "semiprime_offsets": tuple(sorted(semiprime_offsets)),
        "prime_offsets_equal_half_rough_minus_shadow": True,
        "counterexample_shadow_saturated": saturated,
        "counterexample_equivalence_verified": True,
        "shadow_cardinality_certificate_margin": len(half_rough) - len(shadow_offsets),
    }
