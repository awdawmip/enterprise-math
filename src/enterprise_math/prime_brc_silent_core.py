"""Prime-BRC polarity-silent ambiguity core.

Owner-local L3 research support for ``research/prime-brc-stage-a``.

The signed midpoint defect

    chi_d(k)=2 floor(M/d)-floor(k^2/d)-floor((k+1)^2/d),
    M=k(k+1),

is a ternary directional carry readout.  A composite endpoint is called
``polarity-silent`` when every proper divisor has chi=0.  The point of this
module is not to claim a prime-existence theorem, but to classify the exact
no-resurrection ambiguity left by a polarity-only runtime encoding.

For k>=10 and an anchor-surviving mirror endpoint n=M+-r, polarity silence
forces n to be a semiprime p*q with k/2<p<=k<q.  Moreover, for each fixed least
prime p in (k/2,k], at most one anchor-surviving polarity-silent semiprime in the
whole square basin can have least prime p.
"""

from __future__ import annotations

from math import gcd, isqrt

from .prime_brc_phase import square_basin_frame, square_midpoint_defect


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def least_prime_factor(n: int) -> int:
    if n < 2:
        raise ValueError("n must be at least 2")
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return d
    return n


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    if n < 2:
        raise ValueError("n must be at least 2")
    out: list[tuple[int, int]] = []
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            e = 0
            while value % p == 0:
                value //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if value > 1:
        out.append((value, 1))
    return tuple(out)


def proper_divisors(n: int) -> tuple[int, ...]:
    """Return all proper divisors d with 1<d<n."""
    fs = factorization(n)
    values = [1]
    for p, e in fs:
        prior = list(values)
        values = []
        for base in prior:
            power = 1
            for _ in range(e + 1):
                values.append(base * power)
                power *= p
    return tuple(sorted(d for d in values if 1 < d < n))


def polarity_signature(k: int, n: int) -> tuple[tuple[int, int], ...]:
    """Nonzero proper-divisor midpoint-polarity signature."""
    frame = square_basin_frame(k)
    if not frame["lower"] < n < frame["upper"]:
        raise ValueError("n must lie strictly inside the square basin")
    return tuple(
        (d, value)
        for d in proper_divisors(n)
        if (value := square_midpoint_defect(k, d)) != 0
    )


def polarity_silent(k: int, n: int) -> bool:
    """Whether every proper divisor of n has zero midpoint polarity."""
    return not polarity_signature(k, n)


def mirror_endpoint(k: int, radius: int, side: int) -> int:
    frame = square_basin_frame(k)
    if not 1 <= radius < k:
        raise ValueError("radius must satisfy 1<=r<k")
    if side not in (-1, 1):
        raise ValueError("side must be -1 or +1")
    return frame["center"] + side * radius


def silent_core_classification(k: int, radius: int, side: int) -> dict[str, object]:
    """Classify one anchor-surviving polarity-silent composite endpoint.

    This executable certificate checks the general elementary theorem:

    * k>=10, 1<=r<k, gcd(r,k(k+1))=1;
    * n=M+-r is composite and polarity-silent;
    * then p=spf(n) satisfies k/2<p<=k;
    * k^3>8(k+1)^2 forces Omega(n)=2;
    * hence n=p*q with distinct primes and q>k.

    The proof is mathematical; this routine is deterministic replay/falsification
    support for concrete inputs.
    """
    if k < 10:
        raise ValueError("silent-core theorem interface requires k>=10")
    frame = square_basin_frame(k)
    if gcd(radius, frame["center"]) != 1:
        raise ValueError("radius must survive the anchor sieve")
    n = mirror_endpoint(k, radius, side)
    p = least_prime_factor(n)
    if p == n:
        raise ValueError("endpoint is prime, not a silent composite")
    if not polarity_silent(k, n):
        raise ValueError("endpoint is not polarity-silent")

    # If p<=k/2 then q=n/p>2k.  Since the strict square basin has only 2k
    # integer states, q can hit it only once, forcing chi_q=+-1; contradiction.
    q0 = n // p
    if p * 2 <= k:
        if q0 <= 2 * k:
            raise AssertionError("p<=k/2 failed to force complementary divisor >2k")
        if square_midpoint_defect(k, q0) == 0:
            raise AssertionError("unique >2k basin hit unexpectedly had zero polarity")
        raise AssertionError("polarity-silent composite violated p>k/2")

    if not (k**3 > 8 * (k + 1) ** 2):
        raise AssertionError("k>=10 cubic depth inequality failed")

    fs = factorization(n)
    omega = sum(e for _p, e in fs)
    if omega != 2:
        raise AssertionError("silent composite escaped the semiprime core")
    if len(fs) != 2 or any(e != 1 for _p, e in fs):
        raise AssertionError("silent semiprime failed distinct-prime factorization")
    p1, q1 = fs[0][0], fs[1][0]
    if p1 != p or not (2 * p > k and p <= k < q1):
        raise AssertionError("silent semiprime factor range failed")
    if p * q1 != n:
        raise AssertionError("factor reconstruction failed")
    if frame["center"] % p == 0 or frame["center"] % q1 == 0:
        raise AssertionError("anchor-surviving endpoint acquired an anchor factor")

    upper_q_bound_num = 2 * (k + 1) ** 2
    if not q1 * k < upper_q_bound_num:
        raise AssertionError("cofactor upper bound q<2(k+1)^2/k failed")

    return {
        "k": k,
        "radius": radius,
        "side": side,
        "n": n,
        "least_prime": p,
        "cofactor_prime": q1,
        "omega": omega,
        "least_prime_above_half": True,
        "cofactor_above_k": True,
        "cofactor_bound_numerator": upper_q_bound_num,
        "cofactor_bound_denominator": k,
        "signature": (),
    }


def silent_fixed_p_certificate(k: int, p: int) -> dict[str, object]:
    """Return the exact fixed-p silent-capacity certificate for k>=10.

    Preconditions are the only branch where ambiguity can survive:
    p is prime, k/2<p<=k, p is transverse to M, and chi_p=0.

    Write k=p+t, t(t+1)=h*p+s and Q=floor(M/p).  Directional carry
    recovery gives either two p-hits (both carry bits zero) or four p-hits
    (both one).  In the two-hit case the cofactor candidates are consecutive,
    hence at most one can be an odd prime.  In the four-hit case they are
    Q-1,Q,Q+1,Q+2.  Only one parity pair can be prime.  The two possible
    prime pairs cannot both be silent:

      Q,Q+2: silence of lower Q would imply t+h<=s<t;
      Q-1,Q+1: silence of upper Q+1 would imply t+h+s+2<p,
               while s>=p-t.

    Thus at most one polarity-silent semiprime can lie in a fixed p shell.
    """
    if k < 10:
        raise ValueError("requires k>=10")
    if not _is_prime(p) or not (p <= k < 2 * p):
        raise ValueError("require prime p with k/2<p<=k")
    frame = square_basin_frame(k)
    if frame["center"] % p == 0:
        raise ValueError("fixed-p certificate requires a transverse prime")
    if square_midpoint_defect(k, p) != 0:
        raise ValueError("fixed-p silent ambiguity requires chi_p=0")

    t = k - p
    if not 1 <= t <= p - 2:
        raise AssertionError("transverse high p produced invalid t")
    h, s = divmod(t * (t + 1), p)
    qmid = frame["center"] // p
    lower_bit = int(s < t)
    upper_bit = int(s >= p - t)
    if lower_bit != upper_bit:
        raise AssertionError("chi_p=0 failed equal directional carry bits")
    hit_count = 2 + lower_bit + upper_bit
    if hit_count not in (2, 4):
        raise AssertionError("fixed-p hit count escaped {2,4}")

    if hit_count == 2:
        quotient_candidates = (qmid, qmid + 1)
        obstruction = "CONSECUTIVE_COFACTORS_AT_MOST_ONE_ODD_PRIME"
    else:
        quotient_candidates = (qmid - 1, qmid, qmid + 1, qmid + 2)
        if not (p - t <= s < t):
            raise AssertionError("four-hit branch lost double-carry residue window")
        # If Q,Q+2 are the prime-parity pair, lower Q silence would require
        # Q <= k+s+1, i.e. t+h<=s, impossible because s<t.
        if t + h <= s:
            raise AssertionError("forbidden lower-Q silent inequality unexpectedly held")
        # If Q-1,Q+1 are the prime-parity pair, upper Q+1 silence would require
        # t+h+s+2<p, impossible because s>=p-t.
        if t + h + s + 2 < p:
            raise AssertionError("forbidden upper-(Q+1) silent inequality unexpectedly held")
        obstruction = "FOUR_HIT_PARITY_PAIR_CANNOT_BOTH_BE_SILENT"

    # Directly enumerate the small exact p-window as a replay guard.
    silent_semiprimes: list[int] = []
    for q in quotient_candidates:
        n = p * q
        if not (frame["lower"] < n < frame["upper"]):
            continue
        if q <= k or not _is_prime(q):
            continue
        radius = abs(n - frame["center"])
        if not 1 <= radius < k or gcd(radius, frame["center"]) != 1:
            continue
        if polarity_silent(k, n):
            silent_semiprimes.append(n)
    if len(silent_semiprimes) > 1:
        raise AssertionError("fixed p shell contains multiple silent semiprimes")

    return {
        "k": k,
        "p": p,
        "t": t,
        "h": h,
        "s": s,
        "Q": qmid,
        "lower_carry_bit": lower_bit,
        "upper_carry_bit": upper_bit,
        "hit_count": hit_count,
        "quotient_candidates": quotient_candidates,
        "obstruction": obstruction,
        "silent_semiprimes": tuple(silent_semiprimes),
        "capacity": len(silent_semiprimes),
    }


def silent_core_capacity(k: int) -> dict[str, object]:
    """Enumerate the anchor-surviving silent core and verify the branch bound.

    The theorem-level combinatorial consequence is

        #silent composite endpoints <= # {prime p: k/2<p<=k}.

    This remains a capacity theorem, not a Legendre proof: non-silent composite
    endpoints still need independent control.
    """
    if k < 10:
        raise ValueError("requires k>=10")
    frame = square_basin_frame(k)
    silent: list[tuple[int, int, int, int, int]] = []
    by_p: dict[int, list[int]] = {}
    for radius in range(1, k):
        if gcd(radius, frame["center"]) != 1:
            continue
        for side in (-1, 1):
            n = frame["center"] + side * radius
            p = least_prime_factor(n)
            if p == n or not polarity_silent(k, n):
                continue
            data = silent_core_classification(k, radius, side)
            q = int(data["cofactor_prime"])
            silent.append((radius, side, n, p, q))
            by_p.setdefault(p, []).append(n)
    if any(len(values) > 1 for values in by_p.values()):
        raise AssertionError("silent fixed-p branch capacity exceeded one")

    prime_branches = tuple(p for p in range(k // 2 + 1, k + 1) if _is_prime(p))
    if len(silent) > len(prime_branches):
        raise AssertionError("silent core exceeded the prime-branch count bound")
    return {
        "k": k,
        "silent_endpoints": tuple(silent),
        "silent_count": len(silent),
        "prime_branch_count": len(prime_branches),
        "prime_branches": prime_branches,
        "capacity_bound_holds": True,
        "status": "EXACT_CAPACITY_THEOREM_REPLAY_NOT_PRIME_EXISTENCE",
    }
