from __future__ import annotations

from dataclasses import dataclass
from math import isqrt
from typing import Iterable, Tuple


@dataclass(frozen=True)
class ShellSourceCandidate:
    Y: int
    Z: int
    S: int
    T: int


def squarefree_part(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    d = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            d *= p
        p += 1 if p == 2 else 2
    if n > 1:
        d *= n
    return d


def norm_pair(r: int, p: int, q: int) -> int:
    return p * p - r * q * q


def aggregate_from_digits(r: int, digits: Iterable[int]) -> Tuple[int, int]:
    """Return (p,q) for P=sum alpha^(d-1-j) digit_j = p+alpha*q."""
    p = 0
    q = 0
    for digit in digits:
        p, q = r * q + int(digit), p
    return p, q


def return_norm_divisor(r: int, d: int) -> int:
    if d < 1:
        raise ValueError("d must be positive")
    return r ** ((d + 1) // 2)


def shell_return_candidates(s: int, r: int, d: int, p: int, q: int) -> Tuple[ShellSourceCandidate, ...]:
    """Reconstruct integral norm-shell sources compatible with one aggregate return block.

    Let alpha=sqrt(r), B=(r-1)(s-4)^2, x=Y+alpha*Z with N(x)=-B,
    and x'=alpha^d*x + P, P=p+alpha*q.  If x' also has norm -B,
    this routine returns all integral (Y,Z) satisfying the two shell equations.

    It does not claim endpoint-dynamical legality.  Exact branch accessibility must
    still be certified by the endpoint oracle / correction word.
    """
    if s < 3 or s == 4 or r < 5 or isqrt(r) ** 2 == r or d < 1:
        raise ValueError("require s>=3, s!=4, nonsquare r>=5, d>=1")
    B = (r - 1) * (s - 4) ** 2
    NP = norm_pair(r, p, q)
    if NP == 0:
        return ()

    C = B * ((-r) ** d - 1) - NP
    raw = []
    if d % 2 == 0:
        den = 2 * (r ** (d // 2))
        if C % den:
            return ()
        S = C // den
        t2_num = S * S + B * NP
        if t2_num < 0 or t2_num % r:
            return ()
        t2 = t2_num // r
        t0 = isqrt(t2)
        if t0 * t0 != t2:
            return ()
        for T in {t0, -t0}:
            y_num = p * S + r * q * T
            z_num = q * S + p * T
            if y_num % NP == 0 and z_num % NP == 0:
                raw.append(ShellSourceCandidate(y_num // NP, z_num // NP, S, T))
    else:
        den = 2 * (r ** ((d + 1) // 2))
        if C % den:
            return ()
        T = C // den
        s2 = r * T * T - B * NP
        if s2 < 0:
            return ()
        s0 = isqrt(s2)
        if s0 * s0 != s2:
            return ()
        for S in {s0, -s0}:
            y_num = p * S + r * q * T
            z_num = q * S + p * T
            if y_num % NP == 0 and z_num % NP == 0:
                raw.append(ShellSourceCandidate(y_num // NP, z_num // NP, S, T))

    # Stable deduplication; the square root can be zero.
    seen = set()
    out = []
    for item in raw:
        key = (item.Y, item.Z, item.S, item.T)
        if key not in seen:
            seen.add(key)
            out.append(item)
    return tuple(out)


def norm_divisibility_holds(s: int, r: int, d: int, p: int, q: int) -> bool:
    """Necessary shell-to-shell congruence r^ceil(d/2) | N(P)+B."""
    B = (r - 1) * (s - 4) ** 2
    return (norm_pair(r, p, q) + B) % return_norm_divisor(r, d) == 0


def rational_square(n: int) -> bool:
    if n < 0:
        return False
    u = isqrt(n)
    return u * u == n


def shell_correction_field_possible(r: int, d: int) -> bool:
    """Necessary field condition for a return block P with N(P)=-B.

    If source x, correction P, and target alpha^d*x+P all lie on the same
    nonzero norm shell, then Delta=N(alpha^d)(N(alpha^d)-4) must have a square
    root in Q(sqrt(r)).  For positive rational Delta this is equivalent to
    Delta being a rational square or Delta/D being one, where D is the
    squarefree part of r.
    """
    if r < 2 or isqrt(r) ** 2 == r or d < 1:
        raise ValueError("require nonsquare r>=2 and d>=1")
    nA = (-r) ** d
    Delta = nA * (nA - 4)
    if Delta < 0:
        return False
    D = squarefree_part(r)
    if rational_square(Delta):
        return True
    return Delta % D == 0 and rational_square(Delta // D)


def affine_index_from_z(s: int, z: int) -> int | None:
    m = 2 * (s - 2)
    c = s - 4
    num = z + c
    if num % m:
        return None
    return num // m


def target_pair(r: int, d: int, candidate: ShellSourceCandidate, p: int, q: int) -> Tuple[int, int]:
    """Return (Y',Z') for xi'=alpha^d xi + (p+alpha*q)."""
    Y, Z = candidate.Y, candidate.Z
    if d % 2 == 0:
        scale = r ** (d // 2)
        return scale * Y + p, scale * Z + q
    scale = r ** ((d - 1) // 2)
    return r * scale * Z + p, scale * Y + q


def verify_dynamic_chord(s: int, r: int, d: int, p: int, q: int,
                         candidate: ShellSourceCandidate, predecessor_fn):
    """Deterministically certify one shell chord using the unique predecessor oracle.

    predecessor_fn must have signature predecessor_fn(s,r,child_index)->parent_index|None.
    Returns the unique forward endpoint-index path k_t,...,k_{t+d+1} on success,
    otherwise None.  No correction word is an input.
    """
    Y, Z = candidate.Y, candidate.Z
    Yp, Zp = target_pair(r, d, candidate, p, q)
    k0 = affine_index_from_z(s, Z)
    k1 = affine_index_from_z(s, Y)
    kd = affine_index_from_z(s, Zp)
    kd1 = affine_index_from_z(s, Yp)
    if None in (k0, k1, kd, kd1) or min(k0, k1, kd, kd1) < 1:
        return None

    rev = [kd1]
    cur = kd1
    for _ in range(d + 1):
        cur = predecessor_fn(s, r, cur)
        if cur is None:
            return None
        rev.append(cur)
    path = list(reversed(rev))
    if path[0] != k0 or path[1] != k1 or path[-2] != kd or path[-1] != kd1:
        return None
    return tuple(path)
