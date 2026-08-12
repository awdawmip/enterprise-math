"""Tent-Poisson precision and exact frequency-conductor descent.

Fix an anchor-surviving physical factor state s=mn=M+r with M=k(k+1).  Put

    M = n Q + t,      0<=t<n,

and for an odd divisor channel d coprime to n let

    r_(n,d) = Q + 2 t n^{-1} (mod d).

Use the nonnegative compactly supported tent

    W(u)=(1-|u|)_+,

whose Fourier transform (with e(x)=exp(2*pi*i*x)) is

    W_hat(x)=(sin(pi*x)/(pi*x))^2.

Poisson summation on the progression j=r_(n,d) mod d gives the exact analytic
identity

  sum_(j=r mod d) W((n*j-t)/k)
    = k/(n d) * sum_(h in Z)
        W_hat(h*k/(n*d))
        e( h*r/d - h*t/(n*d) ).

Using additive reciprocity, the phase is

    Psi_h(n,d)
      = h*M/(n*d) - 2*h*t*d^{-1}/n          (mod 1).

The P017 anchor-survival condition implies gcd(s,M)=1.  Hence every factor n|s
satisfies gcd(n,M)=1, so gcd(t,n)=1: the reciprocal numerator is automatically
nondegenerate.

Now let

    g=gcd(h,n), q=n/g, h'=h/g.

Then gcd(h',q)=1 and, with t_q=R_q(M), the *entire* phase and Fourier scale
descend exactly:

    Psi_h(n,d) = Psi_h'(q,d)                 (mod 1),
    h*k/(n*d) = h'*k/(q*d).

Thus every nonprimitive frequency is literally a primitive copy on a lower
divisor conductor q|n.  Under the exact critical Walsh truncation d<=k, each
conductor has natural frequency scale

    H_q=q*d/k <= q.

Frequency precision therefore closes under divisor descent instead of creating
an unbounded new state direction.

For the tent transform, |W_hat(x)|<=min(1,1/(pi^2*x^2)).  If H=n*d/k and one
keeps frequencies |h|<T(H+1), T>1, the omitted Fourier contribution after the
prefactor 1/H has absolute value at most

    2/(pi^2*(T-1)).

This is a uniform analytic tail ceiling.  The module records phase/state
identities and precision ceilings; it does not claim the remaining primitive
Kloosterman sums are bounded strongly enough for Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, pi, sin


def tent_fourier(x: float) -> float:
    if x == 0.0:
        return 1.0
    value = sin(pi * x) / (pi * x)
    return value * value


def tent_frequency_scale(k: int, n: int, d: int) -> Fraction:
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 1 for value in (k, n, d)):
        raise ValueError("k,n,d must be positive integers")
    return Fraction(n * d, k)


def tent_tail_error_ceiling(T: float) -> float:
    """Uniform tail ceiling after |h|>=T(H+1), valid for every H>0 and T>1."""
    if T <= 1.0:
        raise ValueError("T must exceed 1")
    return 2.0 / (pi * pi * (T - 1.0))


def euclidean_poisson_frequency_state(
    center: int,
    n: int,
    d: int,
    h: int,
) -> dict[str, object]:
    """Return the exact primitive conductor state of one Poisson frequency."""
    if isinstance(center, bool) or not isinstance(center, int) or center < 1:
        raise ValueError("center must be positive")
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be positive")
    if isinstance(d, bool) or not isinstance(d, int) or d < 1:
        raise ValueError("d must be positive")
    if isinstance(h, bool) or not isinstance(h, int):
        raise ValueError("h must be an integer")
    if gcd(center, n) != 1:
        raise ValueError("frequency-conductor theorem requires gcd(center,n)=1")
    if gcd(n, d) != 1:
        raise ValueError("frequency-conductor theorem requires gcd(n,d)=1")

    t = center % n
    if gcd(t, n) != 1:
        raise AssertionError("Euclidean remainder lost anchor-survival nondegeneracy")
    inv_d_n = pow(d, -1, n)
    original_phase = Fraction(h * center, n * d) - Fraction(2 * h * t * inv_d_n, n)

    g = gcd(abs(h), n) if h != 0 else n
    q = n // g
    h_prime = h // g
    t_q = center % q if q > 1 else 0
    if q > 1:
        if gcd(h_prime, q) != 1 or gcd(t_q, q) != 1:
            raise AssertionError("reduced frequency state is not primitive")
        inv_d_q = pow(d, -1, q)
        reduced_phase = Fraction(h_prime * center, q * d) - Fraction(
            2 * h_prime * t_q * inv_d_q, q
        )
    else:
        inv_d_q = 0
        reduced_phase = Fraction(h_prime * center, d)

    difference = original_phase - reduced_phase
    if difference.denominator != 1:
        raise AssertionError("Poisson phase failed exact conductor descent modulo one")

    return {
        "center": center,
        "n": n,
        "d": d,
        "h": h,
        "remainder_t_n": t,
        "frequency_gcd": g,
        "reduced_conductor_q": q,
        "primitive_frequency_h_prime": h_prime,
        "reduced_remainder_t_q": t_q,
        "inverse_d_mod_n": inv_d_n,
        "inverse_d_mod_q": inv_d_q,
        "original_phase": original_phase,
        "reduced_phase": reduced_phase,
        "phase_difference_integer": int(difference),
        "frequency_conductor_descent_exact": True,
    }


def critical_frequency_closure(k: int, q: int, d: int) -> dict[str, object]:
    """Record H_q=q*d/k and the exact critical implication d<=k => H_q<=q."""
    H = tent_frequency_scale(k, q, d)
    return {
        "k": k,
        "q": q,
        "d": d,
        "frequency_scale_H_q": H,
        "critical_divisor_range": d <= k,
        "frequency_no_finer_than_conductor": (not d <= k) or H <= q,
    }
