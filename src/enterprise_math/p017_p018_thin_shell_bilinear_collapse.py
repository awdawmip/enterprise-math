"""Square-diagonal Generation 3: thin-shell Type-III -> Type-II collapse.

Generation 2 localizes P3 rough triple-prime survivors to the balanced factor
box

    L(k) <= a <= b <= c <= U_k/L(k)^2,

where

    U_k = k^2 + 2k,
    H_c(k) = floor((2k^2-1)^(1/3)) + 1,
    L(k) = floor(k^2/(H_c(k)+1)^2) + 1.

The scale of all three factors is X^(1/3) for X=k^2, but the consecutive-square
shell is only H=2k=X^(1/2) thick.  From k>=202 one has the exact inequality

    L(k)^2 > 2k.

Hence for fixed (a,b) the interval for c has length 2k/(ab)<1.  There is at
most one integer third factor, namely floor(U_k/(ab)), and it enters the shell
iff

    U_k mod (ab) < 2k.

Thus the balanced structural Type-III box has only two free discrete variables.
Moreover the gate is exactly the ordinary short-interval divisor remainder

    r(A_k,d) = |{n in (k^2,U_k] : d|n}| - 2k/d.

This is a SAME_MOTHER specialization of the Chen/Iwaniec bilinear-remainder
mechanism, not a new P2-existence theorem.  No Legendre theorem is claimed.
"""

from __future__ import annotations

from fractions import Fraction

from .legendre import is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff, square_interval_upper
from .p017_p018_cubic_ambiguity_hierarchy import low_partner_core_floor

THIN_SHELL_BILINEAR_THRESHOLD = 202
LAST_THIN_SHELL_FAILURE = 201
SMALL_THRESHOLD_CHECK_END = 223


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def square_shell_width(k: int) -> int:
    """Return the Generation-3 shell width U_k-k^2 = 2k."""
    _require_int("k", k)
    if k < 1:
        raise ValueError("k must be positive")
    return 2 * k


def thin_shell_bilinear_certificate(k: int) -> dict[str, object]:
    """Certify L(k)^2>2k for every k>=202.

    The exact threshold is reconstructed arithmetically.  For 202<=k<=223 the
    final inequality is checked directly.  For k>=224 the returned metadata
    also records the rational inequalities used in the paper proof:

        2^(1/3) < 63/50,
        2/k^(2/3) < 3/50,
        H_c+1 < (33/25) k^(2/3),
        L > (25/33)^2 k^(2/3).

    The executable reference verifies the exact integer conclusion rather than
    using floating point approximations.
    """
    _require_int("k", k)
    if k < THIN_SHELL_BILINEAR_THRESHOLD:
        raise ValueError("thin-shell bilinear collapse is certified for k>=202")

    lower = low_partner_core_floor(k)
    width = square_shell_width(k)
    margin = lower * lower - width
    if margin <= 0:
        raise AssertionError("L(k)^2 failed to exceed the square-shell width")

    if k >= SMALL_THRESHOLD_CHECK_END + 1:
        # 2^(1/3) < 63/50 because 63^3 > 2*50^3.
        if not 63**3 > 2 * 50**3:
            raise AssertionError("fixed rational cube-root comparison changed")
        # 2/k^(2/3) < 3/50 follows from 100^3 < 27*k^2.
        if not 100**3 < 27 * k * k:
            raise AssertionError("k>=224 failed the rational k^(2/3) comparison")
        # k^(1/3) > 2*(33/25)^4 is equivalent after cubing to
        # k*25^12 > (2*33^4)^3.
        if not k * 25**12 > (2 * 33**4) ** 3:
            raise AssertionError("k>=224 failed the final rational margin comparison")
        proof_mode = "RATIONAL_ANALYTIC_TAIL"
    else:
        proof_mode = "FINITE_EXACT_THRESHOLD_WINDOW"

    return {
        "k": k,
        "cubic_low_factor_floor": lower,
        "shell_width": width,
        "floor_square": lower * lower,
        "strict_margin": margin,
        "proof_mode": proof_mode,
        "status": "THIN_SHELL_TYPE_III_TO_TYPE_II",
    }


def reconstruct_last_thin_shell_failure(search_end: int = 223) -> int:
    """Return the last k<=search_end with L(k)^2<=2k."""
    _require_int("search_end", search_end)
    if search_end < 3:
        raise ValueError("search_end must be at least 3")
    failures = [
        k
        for k in range(3, search_end + 1)
        if low_partner_core_floor(k) ** 2 <= square_shell_width(k)
    ]
    if not failures:
        raise AssertionError("bounded threshold reconstruction found no failure")
    return max(failures)


def square_interval_divisor_gate(k: int, divisor: int) -> dict[str, object]:
    """Return the exact divisor gate and centered short-interval remainder.

    For d>2k, at most one multiple of d can occur in (k^2,k^2+2k].  If

        U = q*d + s, 0<=s<d,

    the multiple q*d lies strictly above k^2=U-2k iff s<2k.  Therefore

        floor(U/d)-floor(k^2/d) = 1_{U mod d < 2k}.

    The centered remainder is returned exactly as a Fraction.
    """
    for name, value in (("k", k), ("divisor", divisor)):
        _require_int(name, value)
    if k < 1:
        raise ValueError("k must be positive")
    width = square_shell_width(k)
    if divisor <= width:
        raise ValueError("divisor gate requires d>2k so the interval has at most one multiple")

    upper = square_interval_upper(k)
    count = upper // divisor - (k * k) // divisor
    remainder = upper % divisor
    gate = int(remainder < width)
    if count not in (0, 1):
        raise AssertionError("d>2k allowed more than one multiple in the shell")
    if count != gate:
        raise AssertionError("floor difference and endpoint-remainder gate disagreed")

    centered = Fraction(count * divisor - width, divisor)
    return {
        "k": k,
        "upper": upper,
        "shell_width": width,
        "divisor": divisor,
        "upper_remainder": remainder,
        "multiple_count": count,
        "gate": bool(gate),
        "density_main_term": Fraction(width, divisor),
        "centered_remainder": centered,
        "reconstruction": Fraction(width, divisor) + centered,
    }


def balanced_pair_third_factor(k: int, a: int, b: int) -> dict[str, object]:
    """Project one balanced pair (a,b) to its unique shell candidate c.

    This function is arithmetic-only: a and b need not be prime.  It assumes
    the Generation-2 balanced lower floor, which automatically gives ab>2k for
    k>=202.
    """
    for name, value in (("k", k), ("a", a), ("b", b)):
        _require_int(name, value)
    cert = thin_shell_bilinear_certificate(k)
    lower = int(cert["cubic_low_factor_floor"])
    if not (lower <= a <= b):
        raise ValueError("require balanced pair L(k)<=a<=b")

    divisor = a * b
    gate = square_interval_divisor_gate(k, divisor)
    upper = int(gate["upper"])
    candidate = upper // divisor
    ordered = candidate >= b
    ordered_equivalent = a * b * b <= upper
    if ordered != ordered_equivalent:
        raise AssertionError("c>=b and ab^2<=U lost equivalence")

    in_shell = bool(gate["gate"])
    if in_shell:
        value = divisor * candidate
        if not k * k < value <= upper:
            raise AssertionError("gate candidate failed the square-shell interval")
    else:
        value = divisor * candidate
        if k * k < value <= upper:
            raise AssertionError("closed gate still produced an in-shell multiple")

    return {
        **gate,
        "a": a,
        "b": b,
        "pair_product": divisor,
        "candidate_c": candidate,
        "candidate_value": value,
        "candidate_in_shell": in_shell,
        "ordered_candidate": ordered,
        "ordered_gate": ordered_equivalent,
        "candidate_is_prime": is_prime(candidate),
        "prime_triple_gate": in_shell and ordered and is_prime(candidate),
    }


def balanced_prime_triples_via_pairs(k: int) -> dict[str, object]:
    """Enumerate balanced prime triples using only the two free prime variables.

    This is a bounded research/regression observable, not an analytic proof.
    Rows are `(a,b,c,value,offset)` and should match the balanced triple rows in
    the Generation-2 direct factorization enumerator for k>=202.
    """
    cert = thin_shell_bilinear_certificate(k)
    lower = int(cert["cubic_low_factor_floor"])
    upper = square_interval_upper(k)
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
    primes = tuple(p for p in primes_up_to(z2) if p >= lower)

    rows: list[tuple[int, int, int, int, int]] = []
    for index, a in enumerate(primes):
        for b in primes[index:]:
            if a * b * b > upper:
                break
            projection = balanced_pair_third_factor(k, a, b)
            if not bool(projection["prime_triple_gate"]):
                continue
            c = int(projection["candidate_c"])
            value = int(projection["candidate_value"])
            rows.append((a, b, c, value, value - k * k))

    return {
        "k": k,
        "cubic_low_factor_floor": lower,
        "p2_cutoff": z2,
        "balanced_prime_triples": tuple(rows),
        "balanced_prime_triple_count": len(rows),
        "free_discrete_variables": 2,
        "status": "THIN_SHELL_TYPE_III_TO_TYPE_II",
    }
