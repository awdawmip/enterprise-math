"""Exact primitive tent energy as a pure divisor-boundary spectrum.

For a cross modulus m>1, the self-dual bi-primitive tent block has Fourier form

    B = k/m * sum_(h in Z, gcd(h,m)=1)
          W_hat(h*k/m) e(h*rho/m).

Periodize h=a+l*m over reduced residues.  The sinc-squared identity gives a
nonnegative coefficient

    alpha_m(a)
      = 1/(k*m) |sum_(j=0)^(k-1) e(a*j/m)|^2,

so

    |B| <= Lambda_m(k),

where

    Lambda_m(k)=sum_(a mod m, gcd(a,m)=1) alpha_m(a).

The total primitive coefficient mass has an exact finite boundary formula.  Let

    r_e = k mod e.

Ramanujan expansion of the reduced-residue sum gives

    k*m*Lambda_m(k)
      = sum_(e|m) mu(m/e) r_e (e-r_e),      m>1.

Indeed the pair count in one residue class modulo e is

    N_e = k^2/e + r_e(1-r_e/e).

After multiplication by e, the k^2 bulk is independent of e and disappears
because sum_(e|m) mu(m/e)=0.  Thus primitive Fourier energy is itself a pure
Möbius-signed boundary spectrum.

When m>k, finite Parseval over all residues gives total energy m*k.  Reduced
residues omit at least the zero frequency, whose energy is k^2, hence

    Lambda_m(k) <= 1-k/m.

This sharpens the previous universal high-product ceiling |B|<=1 and shows that
primitive hard blocks vanish continuously as m approaches the critical surface
m=k from above.

This module gives coefficient-mass bounds only; it does not control sums of many
bi-primitive blocks or prove a prime-gap theorem.
"""

from __future__ import annotations

from fractions import Fraction


def _divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def _mobius(n: int) -> int:
    if n < 1:
        raise ValueError("Mobius argument must be positive")
    remaining = n
    count = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            count += 1
            if remaining % p == 0:
                return 0
        p += 1
    if remaining > 1:
        count += 1
    return -1 if count % 2 else 1


def primitive_tent_energy(k: int, m: int) -> Fraction:
    """Return Lambda_m(k) exactly from the divisor-boundary formula."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be positive")
    if isinstance(m, bool) or not isinstance(m, int) or m < 1:
        raise ValueError("m must be positive")
    if m == 1:
        return Fraction(k, 1)
    numerator = 0
    rows: list[tuple[int, int, int]] = []
    for e in _divisors(m):
        mu = _mobius(m // e)
        if mu == 0:
            continue
        r = k % e
        term = mu * r * (e - r)
        numerator += term
        rows.append((e, r, term))
    value = Fraction(numerator, k * m)
    if value < 0:
        raise AssertionError("primitive tent coefficient mass became negative")
    return value


def primitive_tent_energy_profile(k: int, m: int) -> dict[str, object]:
    """Expose the exact boundary rows and the high-product zero-mode improvement."""
    if m < 1 or k < 1:
        raise ValueError("k,m must be positive")
    rows: list[dict[str, int]] = []
    if m == 1:
        value = Fraction(k, 1)
    else:
        numerator = 0
        for e in _divisors(m):
            mu = _mobius(m // e)
            if mu == 0:
                continue
            r = k % e
            term = mu * r * (e - r)
            numerator += term
            rows.append({"e": e, "mu_m_over_e": mu, "remainder_r_e": r, "boundary_term": term})
        value = Fraction(numerator, k * m)
    high_zero_mode_ceiling = None
    if m > k:
        high_zero_mode_ceiling = Fraction(m - k, m)
        if value > high_zero_mode_ceiling:
            raise AssertionError("primitive energy exceeded all-residue minus zero-mode ceiling")
    return {
        "k": k,
        "m": m,
        "primitive_tent_energy": value,
        "boundary_rows": tuple(rows),
        "bulk_cancelled": m == 1 or sum(_mobius(m // e) for e in _divisors(m)) == 0,
        "high_zero_mode_ceiling": high_zero_mode_ceiling,
        "energy_is_pure_boundary_for_nontrivial_modulus": m > 1,
    }


def biprimitive_boundary_energy_ceiling(k: int, n: int, d: int) -> Fraction:
    """Return the phase-independent |B(n,d)| ceiling Lambda_(nd)(k)."""
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in (k, n, d)):
        raise ValueError("k,n,d must be positive integers")
    return primitive_tent_energy(k, n * d)
