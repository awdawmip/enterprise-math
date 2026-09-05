# Character-weighted primitive rotation modes: Gauss traces and Dirichlet-L limits

Status: `FREE_RESEARCH / TYPED SIGNED-AMPLITUDE EXTENSION / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Classification: `PHASE-B SIGNED/COMPLEX READOUT; NOT POSITIVE-MASS CARRIER`
Depends on:
- internal power-series rotation law `(S,C,tau)`;
- primitive denominator mode labels;
- internal mode-radius limit and lower bound.

## 1. Internal finite phase root

Let

\[
\mathcal E(x):=C(x)+iS(x).
\]

The internally proved addition laws imply

\[
\mathcal E(x+y)=\mathcal E(x)\mathcal E(y).
\]

For a primitive denominator `d`, define

\[
\boxed{
\omega_d:=\mathcal E(2\tau/d).
}
\tag{CDL-1}

Since `E(2tau)=1`,

\[
\boxed{\omega_d^d=1.}
\tag{CDL-2}

This is a downstream complex/signed-amplitude readout of the internal real rotation law.  The native finite spectral carrier itself remains real/integer-rational before this extension.

## 2. Character-weighted primitive trace

Let `chi` be a Dirichlet character modulo `d`, viewed on the finite unit group

\[
U_d=(\mathbb Z/d\mathbb Z)^\times.
\]

Define the finite Gauss-type rotation trace

\[
\boxed{
G_{d,\chi}(q)
:=\sum_{r\in U_d}\chi(r)\omega_d^{qr}.
}
\tag{CDL-3}

No infinite Fourier transform appears: this is a finite weighted sum over the already declared primitive mode labels.

If `(q,d)=1`, multiplication by `q` permutes `U_d`.  Substitute `s=qr`:

\[
G_{d,\chi}(q)
=\sum_{s\in U_d}\chi(q^{-1}s)\omega_d^s
=\chi(q)^{-1}G_{d,\chi}(1).
\]

For unitary Dirichlet characters,

\[
\boxed{
G_{d,\chi}(q)
=\overline{\chi(q)}\,G_{d,\chi}(1),
\qquad(q,d)=1.
}
\tag{CDL-4}

This is the finite Gauss covariance law derived purely by relabeling primitive rotation modes.

For primitive characters, the standard finite character argument extends (CDL-4) to the usual Gauss-sum vanishing/covariance at nonunits; that refinement is classical finite character theory and is not needed for the present structural statement.

## 3. Principal character recovers the Ramanujan channel

For the principal unit-group weight, the complex trace is the ordinary finite phase sum over primitive residues.  Its real part at even phase multiplication is the Ramanujan sum:

\[
\boxed{
\operatorname{Re}G_{d,1}(q)=c_d(q).
}
\tag{CDL-5}

Thus the unweighted positive/real primitive trace developed earlier is the principal-character coordinate of the larger signed-amplitude mode atlas.

Nonprincipal characters are invisible if all primitive labels are recoalesced into an unsigned total trace.

## 4. Twisted reciprocal finite spectral moments

Let `chi` have period `d`.  Extend it to integers in the usual Dirichlet-character way, with zero on nonunits if desired.

For a length `M` divisible by `d`, define

\[
\boxed{
\mathcal Z_{s,\chi}(M)
:=\sum_{k=1}^{M-1}
\frac{\chi(k)}{\rho_{k,M}^{2s}},
\qquad s\ge1.
}
\tag{CDL-6}

This is a finite signed/amplitude-weighted spectral observable.  It is not a positive mass.

Internal phase quantization gives, for each fixed `k`,

\[
\rho_{k,M}\longrightarrow k\tau.
\]

The intrinsic lower bound

\[
\rho_{k,M}\ge2k
\]

and `|chi(k)|<=1` give the summable majorant

\[
\left|\frac{\chi(k)}{\rho_{k,M}^{2s}}\right|
\le\frac1{(2k)^{2s}}.
\]

Therefore dominated convergence along multiples of `d` yields

\[
\boxed{
\mathcal Z_{s,\chi}(M)
\longrightarrow
\frac1{\tau^{2s}}
\sum_{k\ge1}\frac{\chi(k)}{k^{2s}}
=
\frac{L(2s,\chi)}{\tau^{2s}}.
}
\tag{CDL-7}

This gives a finite-rotation spectral realization of even positive Dirichlet-L values.

## 5. Principal specialization gives even zeta

For the trivial character of conductor one,

\[
L(2s,1)=\zeta(2s),
\]

and (CDL-7) reduces to the already derived full finite-spectrum moment limit

\[
\zeta(2s)=\beta_s\tau^{2s}.
\]

For principal characters modulo a finite modulus, the limit removes the corresponding Euler factors, matching the finite spectral Möbius-sieve theorem.

Thus the sieve and character routes are two compatible specializations of the same mode-labeled finite spectrum.

## 6. Information carried by the signed channel

The positive/unweighted primitive trace computes gcd-class arithmetic such as Ramanujan sums after appropriate phase parity resolution.

A nonprincipal character assigns signed or complex amplitude to the same primitive labels.  Those amplitudes satisfy orthogonality and Gauss covariance but sum to zero under positive recoalescence.

Hence

\[
\boxed{
\text{UNSIGNED PRIMITIVE TRACE}
\neq
\text{CHARACTER-WEIGHTED AMPLITUDE TRACE}.
}
\tag{CDL-8}

The distinction is operational: collapsing the signed channel destroys all nonprincipal Dirichlet-character coordinates and therefore all corresponding `L(2s,chi)` limits.

## 7. Finite harmonic atlas on U_d

The irreducible characters of the finite abelian group `U_d` form an orthogonal basis of complex functions on `U_d`.  Therefore the mode-label function

\[
r\mapsto \omega_d^{qr}
\]

has the exact finite expansion

\[
\omega_d^{qr}
=\frac1{|U_d|}
\sum_\chi
G_{d,\chi}(q)\,\overline{\chi(r)}
\]

with the usual finite character normalization.

Thus the primitive denominator spectrum supports two complementary finite coordinate atlases:

```text
Ramanujan / gcd-class atlas:
    positive or centered decimation traces

full unit-group atlas:
    character-weighted signed/complex Gauss traces
```

The second is strictly richer and requires the signed/amplitude carrier.

## 8. Scope

No novelty is claimed for classical Gauss sums, character orthogonality or Dirichlet L-series.  The theorem-candidate content is their typed realization on the project-internal finite rotation-mode carrier and the direct internal-radius completion (CDL-7).

No functional equation, zero-free region or RH/GRH claim is made here.

Freeze:

`PRINCIPAL_PRIMITIVE_TRACE -> RAMANUJAN_CHANNEL`.

`CHARACTER_WEIGHTED_PRIMITIVE_TRACE -> GAUSS_CHANNEL`.

`TWISTED_FINITE_RECIPROCAL_MODES -> L(2s,chi)/TAU^(2s)`.

`SIGNED_AMPLITUDE_CHANNEL != POSITIVE_MASS_CHANNEL`.
