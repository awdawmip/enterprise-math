"""Complete-core / unique-large-tail dichotomy in the P017 square basin.

Fix k>=2 and an anchor-surviving signed basin state

    n = M-x,  M=k(k+1),  0<|x|<k,

so

    k^2 < n < k(k+2) < (k+1)^2

and gcd(n,M)=1.  Let C(n) be the complete transverse small-prime core: the
product of p^v_p(n) over all primes p<=k with p∤M.  Anchor survival means every
prime factor <=k of n is transverse, so C(n) contains *all* such factors with
full valuation.

There is an exact finite-boundary dichotomy.

1. High complete core.  If C(n)>k-1, then C(n) cannot equal k or k+1 because
   gcd(C(n),M)=1.  Hence C(n)>=k+2 and

       q=n/C(n) < k(k+2)/(k+2)=k.

   If q>1 it has a prime divisor <=q<k, which would be another small prime
   factor of n and therefore already belong to C(n), contradiction.  Thus

       C(n)>k-1  =>  q=1 and n=C(n).

   A high-core row is therefore a fully k-smooth basin state; the complete-core
   label is literally the state.

2. Low complete core.  If C(n)<=k-1 and C(n)>1, then

       q=n/C(n) > k^2/(k-1) > k+1.

   By completeness of C(n), q has no prime factor <=k.  Because
   q<=n<(k+1)^2, q cannot be composite: a composite with every prime factor >k
   is at least (k+1)^2.  Hence

       C(n)<=k-1, C(n)>1  =>  n=C(n)q with q>k prime.

The empty-support case C(n)=1 is exactly a prime basin state in the existing
P017 signed-support semantics.

Thus every anchor-surviving signed state is exactly one of:

    PRIME;
    FULLY_K_SMOOTH (n=C(n)>k-1);
    ONE_LARGE_PRIME_TAIL (n=C(n)q, C(n)<=k-1, q>k prime).

For the core-adaptive Bonferroni majorant, all remaining correction error is
therefore carried by the ONE_LARGE_PRIME_TAIL class.  At positive even terminal
J, the low-core theorem further forces support size J and residual weight one.
This reconnects the proof-precision frontier to the already-relayed large-tail
injectivity / quotient-channel geometry without introducing a new factorization
mother theorem.

No Legendre proof is claimed.
"""

from __future__ import annotations

from .legendre import is_prime
from .p017_p018_bonferroni_precision import signed_support_profile
from .p017_p018_core_adaptive_bonferroni import complete_transverse_core


def complete_core_tail_row(
    k: int,
    state: int,
    support: tuple[int, ...],
) -> dict[str, object]:
    """Classify one row, assuming ``support`` is its complete transverse support."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(state, bool) or not isinstance(state, int):
        raise ValueError("state must be an integer")
    if not (k * k < state < k * (k + 2)):
        raise ValueError("state must lie in the open P017 square basin")

    normalized = tuple(sorted(int(p) for p in support))
    core = complete_transverse_core(state, normalized)
    if state % core != 0:
        raise AssertionError("complete core failed to divide state")
    quotient = state // core

    if not normalized:
        if core != 1 or not is_prime(state):
            raise AssertionError("empty transverse support was not a prime state")
        kind = "PRIME"
    elif core > k - 1:
        if core in (k, k + 1):
            raise AssertionError("transverse complete core hit an anchor value")
        if quotient != 1 or core != state:
            raise AssertionError("high complete core retained a nontrivial quotient")
        kind = "FULLY_K_SMOOTH"
    else:
        if quotient <= k or not is_prime(quotient):
            raise AssertionError("low complete core did not leave one prime tail >k")
        kind = "ONE_LARGE_PRIME_TAIL"

    return {
        "k": k,
        "state": state,
        "support": normalized,
        "support_size": len(normalized),
        "complete_transverse_core": core,
        "quotient": quotient,
        "kind": kind,
        "large_prime_tail": quotient if kind == "ONE_LARGE_PRIME_TAIL" else None,
    }


def complete_core_tail_profile(k: int) -> dict[str, object]:
    """Classify every anchor-surviving signed state by the exact dichotomy."""
    profile = signed_support_profile(k)
    rows: list[dict[str, object]] = []
    counts = {
        "PRIME": 0,
        "FULLY_K_SMOOTH": 0,
        "ONE_LARGE_PRIME_TAIL": 0,
    }
    seen_large_tails: set[int] = set()

    for row in profile["rows"]:
        data = complete_core_tail_row(
            k,
            int(row["state"]),
            tuple(int(p) for p in row["support"]),
        )
        signed_point = (
            int(row["radius"])
            if str(row["side"]) == "lower"
            else -int(row["radius"])
        )
        enriched = {
            **data,
            "radius": int(row["radius"]),
            "side": str(row["side"]),
            "signed_point": signed_point,
        }
        rows.append(enriched)
        kind = str(data["kind"])
        counts[kind] += 1
        if kind == "ONE_LARGE_PRIME_TAIL":
            tail = int(data["quotient"])
            if tail in seen_large_tails:
                raise AssertionError("large prime tail was reused across signed states")
            seen_large_tails.add(tail)

    if sum(counts.values()) != int(profile["signed_state_count"]):
        raise AssertionError("complete-core/tail classification lost signed rows")
    if counts["PRIME"] != int(profile["prime_state_count"]):
        raise AssertionError("prime class disagrees with signed support profile")

    return {
        "k": k,
        "signed_state_count": int(profile["signed_state_count"]),
        "prime_state_count": counts["PRIME"],
        "fully_k_smooth_count": counts["FULLY_K_SMOOTH"],
        "one_large_prime_tail_count": counts["ONE_LARGE_PRIME_TAIL"],
        "large_prime_tails_globally_distinct": True,
        "rows": tuple(rows),
    }
