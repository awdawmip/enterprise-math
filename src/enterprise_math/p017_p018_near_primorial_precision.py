"""Near-primorial adaptive order for the P017 product-adaptive sieve.

Let P_perp(k,j) be the product of the first j odd primes transverse to
M=k(k+1), and define

    J=J_perp(k)=max{j : P_perp(k,j)<k}.

Choose the odd order

    m_*(k) = J       if J is odd,
             J-1     if J is positive even,
             1       if J=0.

This is exactly the least stable odd residual-exact order coming from the
transverse-primorial support ceiling, but it also controls the whole-basin
product-adaptive error.

Case 1: J odd.
----------------
Then m_*=J and every ordinary Bonferroni defect token uses J+1 distinct
transverse primes.  By maximality of J, either there are not J+1 usable primes,
or

    P_perp(k,J+1) >= k > k-1.

Hence every defect token has squarefree product >k-1, so a fortiori its complete
prime-power block is >k-1.  The product-adaptive correction removes every token:

    B~_{m_*} = U

pointwise on the complete anchor-surviving signed basin.  Thus the adjusted
majorant is globally exact, not only residual-exact.

Case 2: J positive even.
------------------------
Then m_*=J-1 and every defect token selects exactly J distinct transverse
primes.  The product-adaptive error can only come from complete selected blocks
A<=k-1 whose radical has exactly J distinct transverse primes.  Since
P_perp(k,J+1)>=k (or no J+1st transverse prime exists), this is the terminal
near-primorial support shell below the parent cutoff: adding one further distinct
transverse support prime is impossible while staying below k.

At the same order, the residual S<k hard core is already ordinary-Bonferroni
exact, because each residual mirror side has support at most J-1.  Therefore in
the even-J case the whole-basin product-adaptive excess is supported entirely
outside repeated residual high-support complexity and is represented by the
finite J-prime full-block shell A<=k-1.

Examples:

* k=8191: J=4, m_*=3, even-J near-primorial shell;
* k=20000: J=4, m_*=3;
* k=65536 and 131071: J=5, m_*=5, odd-J => globally exact adjusted majorant;
* k=255255: J=3, m_*=3, odd-J => globally exact adjusted majorant;
* k=524287: J=6, m_*=5, even-J; reusable error is confined to six-prime
  full blocks below k.

This theorem does not say the exact adjusted union count is automatically small
enough to prove Legendre.  It isolates its terminal product-support complexity.
"""

from __future__ import annotations

from .p017_p018_product_adaptive_bonferroni import product_adaptive_uniform_exactness
from .p017_p018_transverse_primorial import (
    residual_exact_bonferroni_order,
    transverse_odd_primorial,
    transverse_primorial_depth,
)


def near_primorial_adaptive_order(k: int) -> dict[str, object]:
    """Return J_perp, the parity-selected odd order m_*, and shell type."""
    depth = transverse_primorial_depth(k)
    j = int(depth["transverse_primorial_depth"])
    if j <= 0:
        order = 1
    elif j % 2 == 1:
        order = j
    else:
        order = j - 1

    required = order + 1
    minimum = transverse_odd_primorial(k, required)
    residual = residual_exact_bonferroni_order(k)
    if int(residual["least_guaranteed_exact_odd_order"]) != order:
        raise AssertionError("near-primorial order disagrees with residual exact-order ceiling")

    uniform = product_adaptive_uniform_exactness(k, order)
    odd_j = j % 2 == 1
    if odd_j and not bool(uniform["product_adaptive_majorant_uniformly_exact"]):
        raise AssertionError("odd J failed to force globally exact product-adaptive majorant")

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "adaptive_odd_order": order,
        "selected_token_prime_count": required,
        "J_parity": "ODD" if odd_j else "EVEN",
        "minimum_selected_transverse_primes": tuple(minimum["transverse_primes"]),
        "minimum_selected_product": int(minimum["product"]),
        "minimum_selected_product_complete": bool(minimum["complete"]),
        "globally_exact_product_adaptive_majorant": bool(
            uniform["product_adaptive_majorant_uniformly_exact"]
        ),
        "residual_ordinary_bonferroni_exact": True,
        "remaining_error_shell": (
            "NONE"
            if bool(uniform["product_adaptive_majorant_uniformly_exact"])
            else "J_DISTINCT_TRANSVERSE_PRIME_FULL_BLOCKS_BELOW_K"
        ),
    }


def reusable_near_primorial_block_shape(
    k: int,
    full_block: int,
) -> dict[str, object]:
    """Verify the necessary shape of one reusable terminal block in the even-J case."""
    data = near_primorial_adaptive_order(k)
    j = int(data["transverse_primorial_depth"])
    if data["J_parity"] != "EVEN" or j <= 0:
        raise ValueError("reusable near-primorial shell exists only for positive even J")
    if isinstance(full_block, bool) or not isinstance(full_block, int) or not (1 <= full_block <= k - 1):
        raise ValueError("full_block must satisfy 1<=A<=k-1")

    # Count distinct prime factors and ensure all are transverse.
    remaining = full_block
    primes: list[int] = []
    candidate = 2
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            primes.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1:
        primes.append(remaining)

    center = k * (k + 1)
    if len(primes) != j:
        raise ValueError("terminal reusable block radical must have exactly J distinct primes")
    if any(prime == 2 or prime > k or center % prime == 0 for prime in primes):
        raise ValueError("terminal reusable block primes must be odd and transverse")

    next_minimum = transverse_odd_primorial(k, j + 1)
    if bool(next_minimum["complete"]) and int(next_minimum["product"]) < k:
        raise AssertionError("J was not maximal below the parent cutoff")

    return {
        **data,
        "full_block": full_block,
        "radical_primes": tuple(primes),
        "radical_prime_count": len(primes),
        "terminal_J_prime_shell": True,
        "one_more_distinct_transverse_prime_cannot_fit_uniformly": True,
    }
