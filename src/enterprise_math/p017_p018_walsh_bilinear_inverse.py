"""Exact inverse-residue form of the missing orientation-Walsh bilinear input.

The orientation-Walsh/asymptotic-sieve route isolates a parity-sensitive
nonnegative sequence on the upper physical half-window.  Put

    M=k(k+1),
    a_k(s)=1_{M<s<M+k, s odd, gcd(s,M)=1}
           * 2^{omega_trans(2M-s)},

where omega_trans counts distinct transverse odd primes <=k dividing the
opposite mirror state.  Expanding the amplifier gives

    a_k(s)=sum_{d | 2M-s, d squarefree transverse} 1.

Now write s=mn.  For every actual divisor term d one has gcd(d,mn)=1: d is
transverse to M and if a prime divided d and mn it would divide 2M as well.
Therefore m is invertible modulo d and

    d | 2M-mn
      iff n = 2M * m^{-1} (mod d).

The congruence indicator has the exact additive-character expansion

    1_{d|2M-mn}
      = (1/d) sum_{h mod d}
          exp(2*pi*i*h*(n-2M*m^{-1})/d).

Thus every nonzero frequency contains the reciprocal phase

    exp(-2*pi*i*(2M h)*m^{-1}/d),

which is the Kloosterman-fraction structure expected in a Friedlander--Iwaniec
style bilinear input.  This is an algebraic identity; no existing bilinear
Kloosterman estimate is asserted to cover the very thin physical support.

The geometry of that support is equally explicit.  On a dyadic n-block
N<=n<2N, the condition M<mn<M+k gives

    floor(M/n)+1 <= m <= floor((M+k-1)/n).

The m-window at one n therefore has width about k/n.  Near the balanced range
n~k, both m and n are ~k while each vertical fiber contains only O(1) integers.
Across the whole block there are only O(k) physical lattice pairs.  Since
M~k^2, this is the critical square-root-thin regime; a theorem for an ordinary
thick dyadic rectangle does not automatically apply after discarding the empty
part.

This module is an exact interface/diagnostic for the missing bilinear theorem,
not a proof of that theorem or of Legendre's conjecture.
"""

from __future__ import annotations

from cmath import exp, pi
from math import gcd

from .legendre import primes_up_to


def _transverse_primes(k: int) -> tuple[int, ...]:
    M = k * (k + 1)
    return tuple(p for p in primes_up_to(k) if p % 2 == 1 and M % p != 0)


def _squarefree_products(primes: tuple[int, ...]) -> tuple[int, ...]:
    values = [1]
    for prime in primes:
        values += [value * prime for value in tuple(values)]
    return tuple(sorted(values))


def walsh_upper_sequence_weight(k: int, state: int) -> dict[str, object]:
    """Return a_k(s) and its exact squarefree divisor expansion."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(state, bool) or not isinstance(state, int) or state < 1:
        raise ValueError("state must be a positive integer")
    M = k * (k + 1)
    in_window = M < state < M + k
    admissible = bool(in_window and state % 2 == 1 and gcd(state, M) == 1)
    opposite = 2 * M - state if in_window else None
    if not admissible:
        return {
            "k": k,
            "center": M,
            "state": state,
            "in_upper_physical_window": in_window,
            "admissible": False,
            "opposite_state": opposite,
            "opposite_transverse_support": (),
            "squarefree_divisor_terms": (),
            "walsh_sequence_weight": 0,
        }

    assert opposite is not None
    support = tuple(p for p in _transverse_primes(k) if opposite % p == 0)
    divisors = _squarefree_products(support)
    weight = 2 ** len(support)
    if len(divisors) != weight or any(opposite % divisor for divisor in divisors):
        raise AssertionError("Walsh sequence divisor expansion failed")
    return {
        "k": k,
        "center": M,
        "state": state,
        "in_upper_physical_window": True,
        "admissible": True,
        "opposite_state": opposite,
        "opposite_transverse_support": support,
        "squarefree_divisor_terms": divisors,
        "walsh_sequence_weight": weight,
    }


def inverse_residue_divisor_row(k: int, m: int, n: int, divisor: int) -> dict[str, object]:
    """Verify d|2M-mn iff n=2M*m^{-1} mod d for one actual Walsh term."""
    for name, value in (("m", m), ("n", n), ("divisor", divisor)):
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} must be a positive integer")
    state = m * n
    data = walsh_upper_sequence_weight(k, state)
    if not bool(data["admissible"]):
        raise ValueError("mn must lie in the admissible upper physical window")
    if divisor not in data["squarefree_divisor_terms"]:
        raise ValueError("divisor must be an actual squarefree transverse term of 2M-mn")

    M = int(data["center"])
    opposite = int(data["opposite_state"])
    if opposite != 2 * M - m * n or opposite % divisor:
        raise AssertionError("declared Walsh divisor does not divide 2M-mn")
    if gcd(divisor, M) != 1:
        raise AssertionError("Walsh divisor is not transverse to M")
    if gcd(divisor, m * n) != 1:
        raise AssertionError("actual transverse divisor unexpectedly intersects mn")

    if divisor == 1:
        inverse_m = 0
        target = 0
        residue_identity = True
    else:
        inverse_m = pow(m, -1, divisor)
        target = (2 * M * inverse_m) % divisor
        residue_identity = n % divisor == target
        if not residue_identity:
            raise AssertionError("inverse-residue form failed for an actual Walsh divisor")

    return {
        "k": k,
        "center": M,
        "m": m,
        "n": n,
        "state": state,
        "opposite_state": opposite,
        "divisor": divisor,
        "gcd_divisor_mn": gcd(divisor, m * n),
        "inverse_m_mod_divisor": inverse_m,
        "target_n_residue": target,
        "actual_n_residue": n % divisor,
        "inverse_residue_identity": residue_identity,
    }


def additive_character_inverse_indicator(k: int, m: int, n: int, divisor: int) -> dict[str, object]:
    """Check the exact additive-character expansion of the inverse residue indicator."""
    row = inverse_residue_divisor_row(k, m, n, divisor)
    d = int(row["divisor"])
    if d == 1:
        character_sum = 1 + 0j
        indicator = 1
    else:
        residue_difference = int(row["actual_n_residue"]) - int(row["target_n_residue"])
        character_sum = sum(
            exp(2j * pi * h * residue_difference / d)
            for h in range(d)
        ) / d
        indicator = int(residue_difference % d == 0)
    if abs(character_sum - indicator) > 1e-9:
        raise AssertionError("additive-character inverse-residue expansion failed")
    return {
        **row,
        "direct_congruence_indicator": indicator,
        "additive_character_value": character_sum,
        "additive_character_identity": True,
        "nonzero_frequency_phase": "exp(-2*pi*i*(2M*h)*inverse(m,d)/d)",
    }


def walsh_bilinear_divisor_rows(k: int, m: int, n: int, critical_only: bool = True) -> dict[str, object]:
    """Expose every inverse-residue divisor term for one physical product mn."""
    state = m * n
    data = walsh_upper_sequence_weight(k, state)
    if not bool(data["admissible"]):
        raise ValueError("mn must lie in the admissible upper physical window")
    divisors = tuple(int(d) for d in data["squarefree_divisor_terms"])
    if critical_only:
        divisors = tuple(d for d in divisors if d <= k)
    rows = tuple(inverse_residue_divisor_row(k, m, n, d) for d in divisors)
    if len(rows) == 0 or rows[0]["divisor"] != 1:
        raise AssertionError("Walsh bilinear divisor family lost the unit divisor")
    return {
        **data,
        "m": m,
        "n": n,
        "critical_only": critical_only,
        "returned_divisors": divisors,
        "inverse_residue_rows": rows,
    }


def physical_dyadic_geometry(k: int, N: int) -> dict[str, object]:
    """Return the exact lattice geometry of M<mn<M+k on N<=n<2N."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(N, bool) or not isinstance(N, int) or N < 1:
        raise ValueError("N must be a positive integer")
    M = k * (k + 1)
    rows: list[dict[str, int]] = []
    total = 0
    nonempty = 0
    max_width = 0
    for n in range(N, 2 * N):
        m_min = M // n + 1
        m_max = (M + k - 1) // n
        count = max(0, m_max - m_min + 1)
        total += count
        if count:
            nonempty += 1
            max_width = max(max_width, count)
        rows.append(
            {
                "n": n,
                "m_min": m_min,
                "m_max": m_max,
                "physical_m_count": count,
            }
        )
    return {
        "k": k,
        "center": M,
        "N": N,
        "dyadic_n_low": N,
        "dyadic_n_high_exclusive": 2 * N,
        "rough_m_scale_M_over_N": M / N,
        "rough_vertical_width_k_over_N": k / N,
        "nonempty_n_fibers": nonempty,
        "total_physical_lattice_pairs": total,
        "maximum_vertical_fiber_size": max_width,
        "balanced_square_root_regime": (N <= k < 2 * N),
        "rows": tuple(rows),
    }
