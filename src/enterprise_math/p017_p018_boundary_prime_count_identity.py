"""Terminal P017×P018 boundary-carry identity for primes between consecutive squares.

This module records the representation endpoint reached after combining the
existing least-global-single-use token order with the exact anchor-Mobius
centered carry decomposition.

Put

    M = k(k+1),
    K = k-1,
    X = k(k+2)-1,

and let J be the transverse primorial depth below k (equivalently below K).
The existing token-reuse theorem chooses

    m_* = least positive odd m with m>=J.

At this order any positive Bonferroni defect has support size at least m_*+1>J.
Its squarefree transverse radical therefore exceeds K, so every defect unit is
already high-core / globally single-use.  Hence

    T_{m_*} = H^core_{m_*},
    B_{m_*}-H^core_{m_*} = U,

where U is the exact composite signed-state count.  There is no remaining
low-core Bonferroni error.  Increasing support order, complete-core precision or
p-adic precision cannot improve exactness beyond this point.

Now split every exact anchor-surviving squarefree divisor fiber as

    F_surv(D)=B(D)+C(D),

with B(D) the anchor-Mobius floor bulk and C(D) its finite centered boundary
carry mass.  Let A_eff be the product of the effective odd anchor primes.
For any divisor weight w,

    sum_D w(D) B(D)
      = sum_(q<=K, gcd(q,A_eff)=1)
          sum_(D|q, D transverse) w(D).

Taking full squarefree Mobius weight w(D)=mu(D), including D=1, annihilates every
small shadow integer q carrying a transverse odd prime.  Under the anchor-coprime
condition, transverse support is empty iff q is a power of two: any odd prime
factor of q is <k; if it divided M it would be an effective odd anchor and is
excluded, otherwise it is transverse.  Therefore the complete floor bulk is
exactly the dyadic axis

    L_2(K) = #{1,2,4,...<=K} = 1+floor(log_2 K).

Consequently the exact prime count in the open square basin is

    pi((k+1)^2)-pi(k^2)
      = L_2(K)
        + sum_(D squarefree transverse, D<=X) mu(D) C(D).

The D=1 carry is included.  Its value is the parity discrepancy between the
actual signed odd anchor-surviving window and the unpolarized floor bulk.
Equivalently, if

    Delta_A(K)=sum_(a|A_eff) mu(a) [floor(K/a) mod 2],

then the ordinary terminal Bonferroni bulk leaves the explicit gap

    N_signed-B^bulk_{m_*}=L_2(K)+Delta_A(K).

This identity is an exact reformulation, not a proof of Legendre's conjecture.
It marks a **representation boundary**: after terminalization all sieve
precision errors have vanished, and proving positivity is exactly the problem
of proving a lower bound for the remaining cross-modulus boundary-carry Mobius
sum.  Classical full inclusion-exclusion owns the generic Mobius cancellation;
the project-specific content is the centered square-basin carry split and its
connection to the proof-precision route.
"""

from __future__ import annotations

from math import gcd

from .legendre import primes_up_to, squarefree_divisors_with_mu
from .p017_p018_bonferroni_precision import signed_support_profile
from .p017_p018_core_adaptive_bonferroni import core_adaptive_signed_profile
from .p017_p018_effective_anchor import effective_odd_anchor_primes
from .p017_p018_signed_boundary_carry import anchor_surviving_divisor_boundary_carry
from .p017_p018_token_reuse_precision import least_global_single_use_odd_order


def dyadic_bulk_axis_count(k: int) -> int:
    """Return #{2^j<=k-1:j>=0}."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    return (k - 1).bit_length()


def terminal_boundary_structure(k: int) -> dict[str, object]:
    """Return the exact terminal bulk gap and anchor parity carry."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    K = k - 1
    token = least_global_single_use_odd_order(k)
    order = int(token["least_global_single_use_odd_order"])
    depth = int(token["transverse_primorial_depth"])
    if order < depth:
        raise AssertionError("terminal single-use order fell below transverse depth")

    anchors = effective_odd_anchor_primes(k)
    mobius_rows = squarefree_divisors_with_mu(list(anchors))
    anchor_coprime_count = sum(mu * (K // a) for a, mu in mobius_rows)
    parity_delta = sum(mu * ((K // a) & 1) for a, mu in mobius_rows)
    signed_state_count = anchor_coprime_count + parity_delta
    dyadic = dyadic_bulk_axis_count(k)
    terminal_bulk = anchor_coprime_count - dyadic
    bulk_gap = signed_state_count - terminal_bulk
    if bulk_gap != dyadic + parity_delta:
        raise AssertionError("terminal dyadic/parity bulk-gap identity failed")

    return {
        "k": k,
        "K": K,
        "transverse_primorial_depth": depth,
        "terminal_single_use_odd_order": order,
        "effective_odd_anchor_primes": anchors,
        "anchor_coprime_small_shadow_count": anchor_coprime_count,
        "anchor_parity_boundary_carry": parity_delta,
        "signed_state_count_from_bulk_plus_parity": signed_state_count,
        "dyadic_bulk_axis_count": dyadic,
        "terminal_bonferroni_floor_bulk": terminal_bulk,
        "terminal_bulk_gap": bulk_gap,
    }


def terminal_core_exactness_diagnostic(k: int) -> dict[str, object]:
    """Bounded direct-row check that the terminal core-adaptive majorant is exact."""
    structure = terminal_boundary_structure(k)
    order = int(structure["terminal_single_use_odd_order"])
    profile = core_adaptive_signed_profile(k, order)
    if int(profile["residual_core_excess"]) != 0:
        raise AssertionError("terminal single-use order left low-core defect")
    if int(profile["core_adaptive_sum"]) != int(profile["exact_nonempty_union"]):
        raise AssertionError("terminal core-adaptive majorant is not the exact union")
    return {
        **structure,
        "exact_composite_union": int(profile["exact_nonempty_union"]),
        "ordinary_bonferroni_sum": int(profile["ordinary_bonferroni_sum"]),
        "high_core_correction": int(profile["high_core_defect_correction"]),
        "residual_core_excess": 0,
        "terminal_core_adaptive_exact": True,
    }


def _squarefree_transverse_products(k: int, cutoff: int):
    """Yield (D,mu(D)) for bounded exact diagnostics, including D=1."""
    center = k * (k + 1)
    transverse = tuple(
        p for p in primes_up_to(k)
        if p != 2 and center % p != 0
    )

    def visit(start: int, value: int, mu: int):
        yield value, mu
        for index in range(start, len(transverse)):
            prime = transverse[index]
            if value > cutoff // prime:
                break
            yield from visit(index + 1, value * prime, -mu)

    yield from visit(0, 1, 1)


def boundary_carry_prime_count_diagnostic(k: int) -> dict[str, object]:
    """Directly verify prime_count = dyadic axis + full Mobius carry sum.

    This enumerator is intended only for bounded regression.  The finite identity
    itself is exact for every k.
    """
    structure = terminal_boundary_structure(k)
    xmax = k * (k + 2) - 1
    carry_sum = 0
    term_count = 0
    for divisor, mu in _squarefree_transverse_products(k, xmax):
        data = anchor_surviving_divisor_boundary_carry(k, divisor)
        carry_sum += mu * int(data["anchor_mobius_boundary_carry_mass"])
        term_count += 1

    predicted = int(structure["dyadic_bulk_axis_count"]) + carry_sum
    actual = int(signed_support_profile(k)["prime_state_count"])
    if predicted != actual:
        raise AssertionError("full boundary-carry Mobius identity missed prime count")
    return {
        **structure,
        "squarefree_boundary_term_count": term_count,
        "full_boundary_mobius_carry_sum": carry_sum,
        "predicted_prime_count": predicted,
        "actual_prime_count": actual,
        "boundary_prime_count_identity": True,
    }
