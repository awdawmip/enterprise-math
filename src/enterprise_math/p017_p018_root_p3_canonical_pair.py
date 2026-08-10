"""Canonical two-smallest-factor correction for squarefree fourth-root triples.

Let U=k^2+2k, z=floor(U^(1/4)), and work on the squarefree z-rough survivor
set.  Every composite survivor is either

* a squarefree semiprime with support depth one, or
* a squarefree triple n=a*b*c with z<a<=b<=c<=k.

For a triple choose the canonical pair D=a*b consisting of the two smallest
factors.  Then

    D >= (z+1)^2 > sqrt(U) > k,
    D <= n^(2/3) <= U^(2/3).

Because D>k, the c-window

    k^2/D < c <= U/D

has length 2k/D<2.  All factors are odd, so it contains at most one
parity-compatible odd integer.  Put

    m = floor(U/D),
    c_*(D) = m if m is odd else m-1.

Then a squarefree triple is recovered uniquely from D exactly when

    k^2 < D*c_* <= U,
    c_* is prime,
    c_* >= b.

(The last condition makes D the canonical two-smallest-factor token; it also
implies c_*<=k from D>sqrt(U).)

If R_sf is the squarefree fourth-root rough count, S1_sf its first medium
support moment, and T the canonical-pair count, the support spectrum {0,1,3}
gives

    prime_gap(k) = R_sf - S1_sf + 2*T.

Thus the complete positive second-order correction can be concentrated on one
single-use token per squarefree triple rather than spread with weight 2/3 over
all three pair tokens.

Analytically, T is a semiprime-denominator -> shifted-floor-prime correlation
with denominator scale

    sqrt(U) < D <= U^(2/3).

This module is an exact bounded reference, not an estimate for that
correlation.
"""

from __future__ import annotations

from .legendre import direct_square_interval_prime_count, is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import square_interval_upper
from .p017_p018_root_p3_squarefree_quadratic import squarefree_root_p3_profile
from .p017_p018_root_p3_support_recovery import root_p3_cutoff


def canonical_odd_cofactor_candidate(k: int, token: int) -> dict[str, int | bool]:
    """Return the unique parity-compatible cofactor candidate for odd token D>k."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    if isinstance(token, bool) or not isinstance(token, int) or token <= k or token % 2 == 0:
        raise ValueError("token must be an odd integer >k")
    upper = square_interval_upper(k)
    m = upper // token
    c = m if m % 2 == 1 else m - 1
    return {
        "k": k,
        "token": token,
        "floor_upper_quotient": m,
        "cofactor_candidate": c,
        "candidate_is_odd": c % 2 == 1,
        "candidate_in_square_shell": k * k < token * c <= upper,
        "single_use": 2 * token > 2 * k,
    }


def canonical_pair_triple_rows(k: int) -> tuple[tuple[int, int, int, int, int], ...]:
    """Enumerate (a,b,c,D,n) for squarefree fourth-root triples."""
    z = root_p3_cutoff(k)
    upper = square_interval_upper(k)
    medium = tuple(p for p in primes_up_to(k) if p > z)
    rows: list[tuple[int, int, int, int, int]] = []

    for i, a in enumerate(medium):
        for b in medium[i:]:
            if b == a:
                continue  # squarefree repair
            token = a * b
            if token <= k:
                continue
            if token * b > upper:
                break
            candidate = canonical_odd_cofactor_candidate(k, token)
            c = int(candidate["cofactor_candidate"])
            if not bool(candidate["candidate_in_square_shell"]):
                continue
            if c < b or not is_prime(c):
                continue
            if c == a or c == b:
                continue  # squarefree triple only
            value = token * c
            if not (k * k < value <= upper):
                raise AssertionError("canonical triple left the square shell")
            if token * token <= upper:
                raise AssertionError("canonical pair token failed D>sqrt(U)")
            if token**3 > upper**2:
                raise AssertionError("canonical pair token exceeded U^(2/3)")
            rows.append((a, b, c, token, value))

    return tuple(rows)


def canonical_pair_recovery_profile(k: int) -> dict[str, object]:
    """Cross-check P=R-S1+2T using one canonical token per triple."""
    squarefree = squarefree_root_p3_profile(k)
    rows = canonical_pair_triple_rows(k)
    triple_count = len(rows)
    depth_counts = squarefree["support_depth_counts"]
    if triple_count != int(depth_counts[2]):  # tuple is (depth0,depth1,depth3)
        raise AssertionError("canonical pair count does not equal squarefree triple count")

    rough = int(squarefree["squarefree_rough_count"])
    s1 = int(squarefree["support_moment_1"])
    prime_count = int(squarefree["prime_count"])
    recovered = rough - s1 + 2 * triple_count
    if recovered != prime_count:
        raise AssertionError("canonical pair correction failed to recover prime count")
    if recovered != direct_square_interval_prime_count(k):
        raise AssertionError("canonical pair recovery lost direct prime count")

    return {
        "k": k,
        "fourth_root_cutoff": squarefree["fourth_root_cutoff"],
        "squarefree_rough_count": rough,
        "support_moment_1": s1,
        "canonical_pair_rows": rows,
        "canonical_triple_count": triple_count,
        "prime_count": prime_count,
        "canonical_pair_prime_recovery": recovered,
        "exact_canonical_pair_recovery": True,
    }
