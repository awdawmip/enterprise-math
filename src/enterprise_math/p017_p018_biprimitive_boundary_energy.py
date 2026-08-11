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

Pure boundary formula.
----------------------
Let r_e=k mod e.  Ramanujan expansion of the reduced-residue sum gives, for
m>1,

    k*m*Lambda_m(k)
      = sum_(e|m) mu(m/e) r_e(e-r_e).

Indeed the pair count in one residue class modulo e is

    N_e = k^2/e + r_e(1-r_e/e).

After multiplication by e, the k^2 bulk is independent of e and disappears
because sum_(e|m)mu(m/e)=0.  Primitive Fourier energy is therefore itself a
finite Möbius-signed boundary spectrum.

Euclidean scale descent.
------------------------
Put r=k mod m.  At every primitive frequency a mod m, complete m-periods cancel:

    sum_(j=0)^(k-1)e(a*j/m)
      = sum_(j=0)^(r-1)e(a*j/m).

Hence, with Lambda_m(0)=0,

    Lambda_m(k) = (r/k) Lambda_m(r).

Now r<m.  On this local scale, finite Parseval over all residues has total
energy m*r and the primitive set omits the zero mode of energy r^2, so

    Lambda_m(r) <= 1-r/m.

Thus the universal Euclidean boundary ceiling is

    Lambda_m(k) <= r(m-r)/(k*m),    r=k mod m.

Consequences:

* m>k: r=k, so Lambda_m(k)<=1-k/m;
* 1<m<=k: r(m-r)<=m^2/4, so Lambda_m(k)<=m/(4k), sharpening
  the earlier sinc-tail ceiling m/(3k);
* if m|k, then Lambda_m(k)=0 exactly.

The phase-independent capacity of a bi-primitive block therefore depends only
on the Euclidean boundary coordinate k mod m; complete periods carry zero
primitive energy.

This module gives coefficient-mass bounds only.  It does not control sums of
many bi-primitive blocks or prove a prime-gap theorem.
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
    if isinstance(k, bool) or not isinstance(k, int) or k < 0:
        raise ValueError("k must be nonnegative")
    if isinstance(m, bool) or not isinstance(m, int) or m < 1:
        raise ValueError("m must be positive")
    if k == 0:
        return Fraction(0, 1)
    if m == 1:
        return Fraction(k, 1)
    numerator = 0
    for e in _divisors(m):
        mu = _mobius(m // e)
        if mu == 0:
            continue
        r = k % e
        numerator += mu * r * (e - r)
    value = Fraction(numerator, k * m)
    if value < 0:
        raise AssertionError("primitive tent coefficient mass became negative")
    return value


def primitive_energy_scale_descent(k: int, m: int) -> dict[str, object]:
    """Verify Lambda_m(k)=(r/k)Lambda_m(r), r=k mod m, and its boundary ceiling."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be positive")
    if isinstance(m, bool) or not isinstance(m, int) or m <= 1:
        raise ValueError("m must exceed one")
    r = k % m
    large = primitive_tent_energy(k, m)
    if r == 0:
        local = Fraction(0, 1)
        reconstructed = Fraction(0, 1)
    else:
        local = primitive_tent_energy(r, m)
        reconstructed = Fraction(r, k) * local
    if large != reconstructed:
        raise AssertionError("primitive energy failed Euclidean scale descent")

    boundary_ceiling = Fraction(r * (m - r), k * m)
    if large > boundary_ceiling:
        raise AssertionError("primitive energy exceeded Euclidean boundary ceiling")
    low_quarter_ceiling = None
    if m <= k:
        low_quarter_ceiling = Fraction(m, 4 * k)
        if large > low_quarter_ceiling:
            raise AssertionError("primitive energy exceeded m/(4k) low-product ceiling")
    return {
        "k": k,
        "m": m,
        "remainder_r": r,
        "primitive_energy_at_k": large,
        "primitive_energy_at_remainder_scale": local,
        "reconstructed_from_remainder_scale": reconstructed,
        "euclidean_boundary_ceiling": boundary_ceiling,
        "low_product_quarter_ceiling": low_quarter_ceiling,
        "energy_scale_descent_exact": True,
    }


def primitive_tent_energy_profile(k: int, m: int) -> dict[str, object]:
    """Expose exact boundary rows plus Euclidean and zero-mode ceilings."""
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

    euclidean_ceiling = None
    high_zero_mode_ceiling = None
    low_quarter_ceiling = None
    if m > 1:
        r = k % m
        euclidean_ceiling = Fraction(r * (m - r), k * m)
        if value > euclidean_ceiling:
            raise AssertionError("primitive energy exceeded Euclidean boundary ceiling")
        if m > k:
            high_zero_mode_ceiling = Fraction(m - k, m)
            if value > high_zero_mode_ceiling:
                raise AssertionError("primitive energy exceeded all-residue minus zero-mode ceiling")
        else:
            low_quarter_ceiling = Fraction(m, 4 * k)
            if value > low_quarter_ceiling:
                raise AssertionError("primitive energy exceeded m/(4k) ceiling")
    return {
        "k": k,
        "m": m,
        "primitive_tent_energy": value,
        "boundary_rows": tuple(rows),
        "bulk_cancelled": m == 1 or sum(_mobius(m // e) for e in _divisors(m)) == 0,
        "euclidean_boundary_ceiling": euclidean_ceiling,
        "high_zero_mode_ceiling": high_zero_mode_ceiling,
        "low_product_quarter_ceiling": low_quarter_ceiling,
        "energy_is_pure_boundary_for_nontrivial_modulus": m > 1,
    }


def biprimitive_boundary_energy_ceiling(k: int, n: int, d: int) -> Fraction:
    """Return the phase-independent |B(n,d)| ceiling Lambda_(nd)(k)."""
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in (k, n, d)):
        raise ValueError("k,n,d must be positive integers")
    return primitive_tent_energy(k, n * d)
