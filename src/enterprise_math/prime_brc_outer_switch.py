"""Prime-BRC outer-factor switching for odd square-basin triprimes.

Owner-local L3 research support on ``research/prime-brc-stage-a``.
No Legendre/P2 theorem is claimed.

For I_k=(k^2,(k+1)^2), every odd triprime n=p*q*r with p<=q<=r has

    q <= k,
    D=p*r > k.

Since D is odd and D>k, there is at most one odd D-multiple in I_k.  Thus the
outer product D uniquely decodes the middle factor q and the original state.
Conversely, an odd P2 modulus D=a*b with a<=b produces a canonical triprime
exactly when its unique odd basin quotient q is prime and a<=q<=b.

The odd unique-hit bit is also the canonical P017 binary carry difference

    eta_D = H_D-H_{2D} = kappa_D-kappa_{2D}

in the D>k range.  Once eta_D=1, all scaled future bits satisfy

    eta_{D*e}=1  <=>  e | q_D

for every odd e>=1.  Hence the scaled carry spectrum is the exact divisor
signature of the residual quotient.
"""

from __future__ import annotations

from math import isqrt

from .legendre import interior_hit_count, square_carry


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return False
    return True


def factor_list(n: int) -> tuple[int, ...]:
    if n < 2:
        raise ValueError("n must be >=2")
    out: list[int] = []
    value = n
    p = 2
    while p * p <= value:
        while value % p == 0:
            out.append(p)
            value //= p
        p = 3 if p == 2 else p + 2
    if value > 1:
        out.append(value)
    return tuple(out)


def odd_unique_hit_candidate(k: int, modulus: int) -> dict[str, int | bool | None]:
    """Decode the unique possible odd hit for an odd modulus D>k."""
    _require_k(k)
    if modulus <= k or modulus % 2 == 0:
        raise ValueError("require odd modulus D>k")
    lower = k * k
    upper = (k + 1) * (k + 1)
    a = lower // modulus
    quotient = a + 1 + (a & 1)  # first odd integer strictly above lower/D
    state = modulus * quotient
    exists = state < upper
    direct_odd_hits = [
        n for n in range(lower + 1, upper)
        if n % 2 == 1 and n % modulus == 0
    ]
    if len(direct_odd_hits) > 1:
        raise AssertionError("odd D>k acquired multiple basin hits")
    if exists != bool(direct_odd_hits):
        raise AssertionError("odd-hit candidate existence disagrees with direct support")
    if exists and direct_odd_hits != [state]:
        raise AssertionError("odd-hit candidate failed exact decode")
    return {
        "k": k,
        "modulus": modulus,
        "base_floor": a,
        "quotient": quotient if exists else None,
        "state": state if exists else None,
        "exists": exists,
    }


def odd_hit_bit(k: int, modulus: int) -> int:
    """eta_D=H_D-H_2D for odd D>k; this is 0 or 1."""
    _require_k(k)
    if modulus <= k or modulus % 2 == 0:
        raise ValueError("require odd modulus D>k")
    direct = interior_hit_count(k, modulus, 2) - interior_hit_count(k, 2 * modulus, 2)
    carry = square_carry(k, modulus) - square_carry(k, 2 * modulus)
    if direct != carry or direct not in (0, 1):
        raise AssertionError("odd unique-hit bit disagrees with binary carry")
    expected = int(odd_unique_hit_candidate(k, modulus)["exists"])
    if direct != expected:
        raise AssertionError("binary carry disagrees with odd-hit decoder")
    return direct


def scaled_future_divisor_bit(k: int, modulus: int, scale: int) -> int:
    """For eta_D=1, certify eta_(D*e)=1 iff e divides q_D (odd e)."""
    _require_k(k)
    if modulus <= k or modulus % 2 == 0:
        raise ValueError("require odd base modulus D>k")
    if scale < 1 or scale % 2 == 0:
        raise ValueError("scale e must be a positive odd integer")
    base = odd_unique_hit_candidate(k, modulus)
    if not base["exists"]:
        raise ValueError("base modulus has no odd basin hit")
    q = int(base["quotient"])
    child = odd_hit_bit(k, modulus * scale)
    expected = int(q % scale == 0)
    if child != expected:
        raise AssertionError("scaled carry failed residual-divisor signature")
    return child


def outer_switch_from_triprime(k: int, n: int) -> dict[str, int]:
    """Map one odd Omega=3 state to its outer P2 modulus D=p_min*p_max."""
    _require_k(k)
    lower = k * k
    upper = (k + 1) * (k + 1)
    if not lower < n < upper or n % 2 == 0:
        raise ValueError("n must be an odd square-basin state")
    fs = factor_list(n)
    if len(fs) != 3:
        raise ValueError("n must have Omega(n)=3")
    p, q, r = fs
    if q > k:
        raise AssertionError("middle triprime factor escaped q<=k")
    D = p * r
    if D <= k:
        raise AssertionError("outer factor product failed D>k")
    decoded = odd_unique_hit_candidate(k, D)
    if not decoded["exists"] or decoded["state"] != n or decoded["quotient"] != q:
        raise AssertionError("outer modulus failed to decode triprime")
    if odd_hit_bit(k, D) != 1:
        raise AssertionError("outer modulus lost binary carry hit")
    return {
        "k": k,
        "n": n,
        "p_min": p,
        "p_mid": q,
        "p_max": r,
        "outer_modulus": D,
        "decoded_middle": q,
    }


def triprime_from_outer_modulus(k: int, modulus: int) -> dict[str, int] | None:
    """Inverse outer switch when D is odd P2 and the decoded prime straddles its factors."""
    _require_k(k)
    if modulus <= k or modulus % 2 == 0:
        return None
    fs = factor_list(modulus)
    if len(fs) != 2:
        return None
    decoded = odd_unique_hit_candidate(k, modulus)
    if not decoded["exists"]:
        return None
    q = int(decoded["quotient"])
    if not _is_prime(q):
        return None
    a, b = fs
    if not (a <= q <= b):
        return None
    n = modulus * q
    factors = factor_list(n)
    if factors != tuple(sorted((a, q, b))):
        raise AssertionError("inverse outer switch failed factor reconstruction")
    return {
        "k": k,
        "n": n,
        "p_min": a,
        "p_mid": q,
        "p_max": b,
        "outer_modulus": modulus,
    }
