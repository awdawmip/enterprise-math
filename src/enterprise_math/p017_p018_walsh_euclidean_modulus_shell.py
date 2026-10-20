"""Euclidean modulus-shell compiler for P017/P018 Walsh boundary channels.

The Walsh divisor/Kloosterman interface writes a transverse congruence through
inverse residues.  At the consecutive-square center the same information has an
exact Euclidean-shell representation with no modular inverse.

Fix k>=3, M=k(k+1), and an odd modulus d<=k transverse to M.  Write

    k = a d + s,                 0<=s<d,
    s(s+1) = h d + u,           0<u<d.

Since k=s mod d,

    M = k(k+1) = d Q0 + u,

with the exact quotient center

    Q0 = a(k+s+1)+h.

The two orientation root families in the physical radius window are therefore

    lower-divisible channel:
      r = u + j d,
      (M-r)/d = Q0-j;

    upper-divisible channel:
      r = d-u + j d,
      (M+r)/d = Q0+j+1.

Only integers j producing 1<=r<k and odd r are retained.  Thus every modulus
shell a=floor(k/d) is a pair of finite quotient channels with unit quotient
step.  The modular inverse visible after further factorization is a coordinate
choice, not the only exact representation of the boundary geometry.

For the high-modulus shell d>(k-1)/2 one has a=1.  Each orientation then has at
most one physical odd radius, recovering the single-use boundary regime.  For
smaller d the number of possible lifts is O(a), making a=floor(k/d) the natural
execution-depth coordinate for a divisor-switch analysis.

This is an exact Euclidean/P018 compiler for the Walsh boundary relation.  It
does not estimate primes and does not prove a short dual-Titchmarsh theorem.
"""

from __future__ import annotations

from math import gcd


def euclidean_modulus_shell(k: int, modulus: int) -> dict[str, object]:
    """Return the exact (a,s,h,u,Q0) shell coordinates for one odd transverse d."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if (
        isinstance(modulus, bool)
        or not isinstance(modulus, int)
        or modulus < 3
        or modulus > k
        or modulus % 2 == 0
    ):
        raise ValueError("modulus must be odd with 3<=d<=k")
    d = modulus
    M = k * (k + 1)
    if gcd(d, M) != 1:
        raise ValueError("modulus must be transverse to M")
    a, s = divmod(k, d)
    h, u = divmod(s * (s + 1), d)
    if not (0 < u < d):
        raise AssertionError("transverse modulus produced zero Euclidean center remainder")
    Q0 = a * (k + s + 1) + h
    if M != d * Q0 + u:
        raise AssertionError("Euclidean modulus-shell reconstruction failed")
    return {
        "k": k,
        "center": M,
        "modulus": d,
        "shell_quotient_a": a,
        "scale_remainder_s": s,
        "remainder_quotient_h": h,
        "center_remainder_u": u,
        "quotient_center_Q0": Q0,
        "high_modulus_single_use_shell": d > (k - 1) // 2,
    }


def euclidean_orientation_channels(k: int, modulus: int) -> dict[str, object]:
    """Enumerate the exact physical odd-radius lifts and their unit-step quotients."""
    shell = euclidean_modulus_shell(k, modulus)
    d = int(shell["modulus"])
    M = int(shell["center"])
    u = int(shell["center_remainder_u"])
    Q0 = int(shell["quotient_center_Q0"])

    lower_rows: list[dict[str, int]] = []
    j = 0
    while True:
        radius = u + j * d
        if radius >= k:
            break
        if radius >= 1 and radius % 2 == 1:
            quotient = Q0 - j
            if M - radius != d * quotient:
                raise AssertionError("lower Euclidean channel factorization failed")
            lower_rows.append({"j": j, "radius": radius, "quotient": quotient})
        j += 1

    upper_rows: list[dict[str, int]] = []
    j = 0
    while True:
        radius = d - u + j * d
        if radius >= k:
            break
        if radius >= 1 and radius % 2 == 1:
            quotient = Q0 + j + 1
            if M + radius != d * quotient:
                raise AssertionError("upper Euclidean channel factorization failed")
            upper_rows.append({"j": j, "radius": radius, "quotient": quotient})
        j += 1

    if bool(shell["high_modulus_single_use_shell"]):
        if len(lower_rows) > 1 or len(upper_rows) > 1:
            raise AssertionError("high modulus shell retained multiple lifts in one orientation")

    return {
        **shell,
        "lower_divisible_channel": tuple(lower_rows),
        "upper_divisible_channel": tuple(upper_rows),
        "lower_channel_size": len(lower_rows),
        "upper_channel_size": len(upper_rows),
        "unit_quotient_step": True,
    }


def verify_direct_modulus_roots(k: int, modulus: int) -> dict[str, object]:
    """Cross-check shell channels against direct divisibility over every odd radius."""
    data = euclidean_orientation_channels(k, modulus)
    d = int(data["modulus"])
    M = int(data["center"])
    lower_direct = tuple(
        r for r in range(1, k, 2)
        if (M - r) % d == 0
    )
    upper_direct = tuple(
        r for r in range(1, k, 2)
        if (M + r) % d == 0
    )
    lower_shell = tuple(int(row["radius"]) for row in data["lower_divisible_channel"])
    upper_shell = tuple(int(row["radius"]) for row in data["upper_divisible_channel"])
    if lower_direct != lower_shell or upper_direct != upper_shell:
        raise AssertionError("Euclidean shell channels disagree with direct modulus roots")
    return {
        **data,
        "direct_lower_radii": lower_direct,
        "direct_upper_radii": upper_direct,
        "direct_root_crosscheck": True,
    }
