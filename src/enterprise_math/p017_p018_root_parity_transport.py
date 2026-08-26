"""Generation 3: exact parity-defect transport from root-P3 to root-P2.

For j in {2,3}, let z_j be the exact root cutoff and define on the corresponding
rough square-shell set

    R_j = count,
    M_j = sum mu(n),
    D_j = R_j - M_j = sum (1-mu(n)).

At z3 every state has Omega<=3.  Its contribution to D_3 is:

    prime                         2,
    squarefree semiprime          0,
    squarefree triple             2,
    repeated-factor triple        1.

At z2 every state is prime or squarefree semiprime, hence D_2=2*pi(I_k).
Every root-P3 triple has least factor <=z2 and is therefore removed by the
descent z3->z2.  Some root-P3 semiprimes are also removed, but they have
1-mu=0 and do not affect D.  Prime states are never removed.

Therefore exactly

    D_2 = D_3 - 2*T_sf - T_rep,

where T_sf is the number of squarefree root-P3 triples and T_rep the number of
root-P3 triples with a repeated prime factor.

The repeated part has a finite signed-capacity bound.  A repeated triple has
some p>z3 with p^2|n.  Since (z3+1)^2>sqrt(U)>k, one has p^2>k, so odd parity
and p^2-divisibility give one residue class modulo 2p^2 with period >2k.  Each
prime p can therefore support at most one repeated triple state in the shell.
Moreover p^3<=n<=U forces p<=z2.  Hence

    T_rep <= # {prime p : z3<p<=z2}.

This identifies the large signed loss in the P3->P2 descent with the
squarefree fully-k-smooth triple core.  It does not bound that core and does not
prove a prime exists.
"""

from __future__ import annotations

from .legendre import primes_up_to
from .p017_p018_buchstab_cutoff_ladder import (
    almost_prime_cutoff,
    rough_survivor_offsets,
)
from .p017_p018_square_parity_bilinear_target import mobius


def root_parity_transport(k: int) -> dict[str, object]:
    """Evaluate the exact D3->D2 parity-defect identity on one finite k."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")

    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
    r3_offsets = rough_survivor_offsets(k, z3)
    r2_offsets = rough_survivor_offsets(k, z2)

    d3 = 0
    squarefree_triples: list[tuple[int, int]] = []
    repeated_triples: list[tuple[int, int, int]] = []

    # Reconstruct Omega only through prime factors >z3.  The root cutoff
    # guarantees no state needs more than three factors counted with multiplicity.
    factor_primes = tuple(p for p in primes_up_to(k) if p > z3)
    for offset in r3_offsets:
        value = k * k + offset
        mu = mobius(value)
        d3 += 1 - mu

        remaining = value
        factors: list[int] = []
        for p in factor_primes:
            while remaining % p == 0:
                factors.append(p)
                remaining //= p
            if remaining == 1:
                break
            if p * p > remaining:
                break
        if remaining > 1:
            factors.append(remaining)
        factors.sort()
        if len(factors) > 3:
            raise AssertionError("root-P3 state exceeded Omega=3")

        if len(factors) == 3:
            if len(set(factors)) == 3:
                if mu != -1:
                    raise AssertionError("squarefree triple lost negative Möbius sign")
                squarefree_triples.append((value, offset))
            else:
                if mu != 0:
                    raise AssertionError("repeated triple lost zero Möbius sign")
                repeated_prime = next(p for p in set(factors) if factors.count(p) >= 2)
                if not (z3 < repeated_prime <= z2):
                    raise AssertionError("repeated triple prime left the z3-z2 root band")
                repeated_triples.append((repeated_prime, value, offset))

    d2 = sum(1 - mobius(k * k + offset) for offset in r2_offsets)
    rhs = d3 - 2 * len(squarefree_triples) - len(repeated_triples)
    if d2 != rhs:
        raise AssertionError("exact P3-to-P2 parity-defect transport failed")

    # At the P2 endpoint D2=2*pi because semiprimes have mu=+1.
    prime_count = sum(1 for offset in r2_offsets if mobius(k * k + offset) == -1)
    if d2 != 2 * prime_count:
        raise AssertionError("P2 parity defect failed to equal twice the prime count")

    repeated_capacity_primes = tuple(p for p in primes_up_to(z2) if p > z3)
    repeated_by_prime = {p: 0 for p in repeated_capacity_primes}
    for p, _value, _offset in repeated_triples:
        repeated_by_prime[p] += 1
    if any(count > 1 for count in repeated_by_prime.values()):
        raise AssertionError("one repeated prime supported two odd shell states")
    if len(repeated_triples) > len(repeated_capacity_primes):
        raise AssertionError("repeated triple count exceeded prime-column capacity")

    return {
        "k": k,
        "p3_cutoff": z3,
        "p2_cutoff": z2,
        "r3_count": len(r3_offsets),
        "m3_sum": len(r3_offsets) - d3,
        "d3_parity_defect": d3,
        "r2_count": len(r2_offsets),
        "m2_sum": len(r2_offsets) - d2,
        "d2_parity_defect": d2,
        "squarefree_triple_rows": tuple(squarefree_triples),
        "squarefree_triple_count": len(squarefree_triples),
        "repeated_triple_rows": tuple(repeated_triples),
        "repeated_triple_count": len(repeated_triples),
        "repeated_triple_capacity_primes": repeated_capacity_primes,
        "repeated_triple_capacity_bound": len(repeated_capacity_primes),
        "prime_count_from_d2": d2 // 2,
        "transport_identity": True,
        "status": "ROOT_P3_TO_P2_PARITY_DEFECT_TRANSPORT",
    }
