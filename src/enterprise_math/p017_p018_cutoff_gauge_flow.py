"""Exact cutoff-gauge flow on squarefree P3 survivors.

Fix the consecutive-square interval I_k=(k^2,k^2+2k] and let the sieve cutoff
y move inside the stable P3 band z_3(k)<=y<z_2(k).  After removing squareful
states, every y-rough survivor has one of three support depths relative to
(y,k]:

    prime                 c=0, mu=-1
    squarefree semiprime  c=1, mu=+1
    squarefree triple     c=3, mu=-1.

Let R_y,S_y,T_y,M_y denote respectively the squarefree rough count, first
medium-support moment, triple count, and Möbius sum.  Both finite prime
detectors are exact throughout the band:

    P = R_y - S_y + 2*T_y,
    3P = 2*R_y - M_y - S_y.

When the cutoff crosses a prime p, only states whose least prime factor is p
are removed.  Let E_p and T_p be the numbers of removed squarefree semiprimes
and triples.  Then the exact jump vector is

    Delta R = -(E_p+T_p),
    Delta S = -(E_p+3T_p),
    Delta T = -T_p,
    Delta M = -E_p+T_p.

Consequently

    Delta(R-S+2T)=0,
    Delta(2R-M-S)=0.

The cutoff is therefore a genuine gauge coordinate for the exact prime
observable.  Raising it transports arithmetic mass between support overlap and
Möbius sign without changing the answer.

The ordered Möbius/Buchstab transport is exactly the accumulated Delta M flow.
This does not make the flow analytically trivial: estimating E_p and T_p
pointwise remains the parity-sensitive task.
"""

from __future__ import annotations

from .legendre import is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff, square_interval_upper
from .p017_p018_root_p3_mobius_support import mobius_value


def is_squarefree(value: int) -> bool:
    """Return whether value has no squared prime divisor."""
    if value < 1:
        raise ValueError("value must be positive")
    for p in primes_up_to(int(value**0.5) + 1):
        if value % (p * p) == 0:
            return False
    return True


def squarefree_cutoff_profile(k: int, cutoff: int) -> dict[str, int]:
    """Enumerate (R,S,T,M,P) for one cutoff in the stable P3 band."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
    if not z3 <= cutoff <= z2:
        raise ValueError("cutoff must lie between the P3 and P2 root cutoffs")

    small = tuple(primes_up_to(cutoff))
    medium = tuple(p for p in primes_up_to(k) if p > cutoff)
    upper = square_interval_upper(k)
    R = S = T = M = P = 0

    for n in range(k * k + 1, upper + 1):
        if any(n % p == 0 for p in small):
            continue
        if not is_squarefree(n):
            continue
        support = tuple(p for p in medium if n % p == 0)
        c = len(support)
        if c not in (0, 1, 3):
            raise AssertionError("squarefree stable-P3 profile left support spectrum {0,1,3}")
        R += 1
        S += c
        T += int(c == 3)
        M += mobius_value(n)
        P += int(c == 0)

    if P != R - S + 2 * T:
        raise AssertionError("quadratic cutoff-gauge invariant failed")
    if 3 * P != 2 * R - M - S:
        raise AssertionError("affine cutoff-gauge invariant failed")

    return {
        "k": k,
        "cutoff": cutoff,
        "p3_cutoff": z3,
        "p2_cutoff": z2,
        "rough_squarefree_count": R,
        "support_moment_1": S,
        "triple_count": T,
        "mobius_sum": M,
        "prime_count": P,
    }


def cutoff_prime_jump(k: int, p: int) -> dict[str, int | bool]:
    """Verify the exact E_p/T_p jump when the cutoff crosses prime p."""
    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
    if p not in primes_up_to(k) or not (z3 < p <= z2):
        raise ValueError("p must be a prime in the stable P3 cutoff band")

    previous_primes = [q for q in primes_up_to(p - 1)]
    previous_cutoff = previous_primes[-1] if previous_primes and previous_primes[-1] >= z3 else z3
    before = squarefree_cutoff_profile(k, previous_cutoff)
    after = squarefree_cutoff_profile(k, p)

    upper = square_interval_upper(k)
    E = T = 0
    small_before = tuple(primes_up_to(previous_cutoff))
    for n in range(k * k + 1, upper + 1):
        if n % p != 0 or any(n % q == 0 for q in small_before):
            continue
        if not is_squarefree(n):
            continue
        mu = mobius_value(n)
        # p is the least prime factor; P3 squarefree types are semiprime/triple.
        if mu == 1:
            E += 1
        elif mu == -1:
            T += 1
        else:
            raise AssertionError("squarefree removed row has zero Möbius value")

    dR = int(after["rough_squarefree_count"]) - int(before["rough_squarefree_count"])
    dS = int(after["support_moment_1"]) - int(before["support_moment_1"])
    dT = int(after["triple_count"]) - int(before["triple_count"])
    dM = int(after["mobius_sum"]) - int(before["mobius_sum"])

    expected = (-(E + T), -(E + 3 * T), -T, -E + T)
    if (dR, dS, dT, dM) != expected:
        raise AssertionError("cutoff-gauge local jump vector failed")
    if dR - dS + 2 * dT != 0:
        raise AssertionError("quadratic prime detector was not gauge invariant")
    if 2 * dR - dM - dS != 0:
        raise AssertionError("affine prime detector was not gauge invariant")

    return {
        "k": k,
        "prime_cutoff_crossed": p,
        "previous_cutoff": previous_cutoff,
        "removed_semiprimes": E,
        "removed_triples": T,
        "delta_R": dR,
        "delta_S": dS,
        "delta_T": dT,
        "delta_M": dM,
        "quadratic_invariant_jump": dR - dS + 2 * dT,
        "affine_invariant_jump": 2 * dR - dM - dS,
        "exact_cutoff_gauge_flow": True,
    }
