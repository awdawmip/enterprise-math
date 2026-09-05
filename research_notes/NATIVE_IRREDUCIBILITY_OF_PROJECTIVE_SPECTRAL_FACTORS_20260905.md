# Native irreducibility of projective spectral factors

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- projective primitive factors `Omega_d`;
- denominator-Frobenius action of `R_n`;
- native projective discriminant formula;
- integer decimation polynomials.

## 0. Result

The previously experimental irreducibility of the projective primitive factor is now proved by finite spectral arithmetic:

\[
\boxed{
\Omega_d(v)\text{ is irreducible over }\mathbf Q
\qquad(d>2).
}
\tag{IR-1}
\]

No cyclotomic irreducibility theorem, root of unity, or classical Galois identification is required.

The same argument then determines the irreducible decomposition of the oriented primitive factor `Psi_d`.

---

## 1. Prime Frobenius congruence for decimation

For a prime `p`, the integer decimation polynomial satisfies

\[
\boxed{
R_p(v)\equiv v^p\pmod p.
}
\tag{IR-2}
\]

One algebraic proof uses the rescaled Dickson trace polynomial `C_p`.

In the quadratic Laurent extension with `x=z+z^{-1}`,

\[
C_p(x)=z^p+z^{-p}.
\]

Modulo `p`, the freshman's-dream identity gives

\[
(z+z^{-1})^p
=z^p+z^{-p},
\]

hence

\[
C_p(x)\equiv x^p\pmod p.
\]

Since

\[
R_p(v)=2-C_p(2-v),
\]

and `2^p congruent 2 mod p`, one gets (IR-2).

This congruence can alternatively be proved directly from the integer recurrence coefficients.

---

## 2. Good primes permute primitive projective roots

Fix `d>2` and a prime `p` with

\[
p\nmid d.
\]

The denominator transition law under `R_p` is

\[
e\mapsto e/\gcd(e,p).
\]

Therefore denominator `d` remains denominator `d`, and `R_p` permutes the primitive projective roots of `Omega_d`.

In phase-index notation,

\[
\boxed{
R_p(v_{r,d})=v_{pr,d},
}
\tag{IR-3}
\]

with the primitive index understood modulo the projective complement pairing.

---

## 3. Good primes cannot move between distinct irreducible factors

Factor `Omega_d` over `Z[v]` into monic irreducibles and let `f` be one factor.  Let `alpha` be a root of `f`.

For a prime `p \nmid d`, let `g` be the irreducible factor containing the root `R_p(alpha)`.

Then

\[
g(R_p(\alpha))=0,
\]

so irreducibility of `f` gives

\[
\boxed{f(v)\mid g(R_p(v))\quad\text{in }\mathbf Q[v].}
\tag{IR-4}
\]

Because all polynomials are monic integral, Gauss' lemma lets us reduce this divisibility modulo `p`.

Using (IR-2),

\[
g(R_p(v))
\equiv g(v^p)
\equiv g(v)^p
\pmod p.
\]

Therefore the reductions of `f` and `g` have a common factor modulo `p`.  If `f!=g`, this implies

\[
\boxed{p\mid\operatorname{Res}(f,g).}
\tag{IR-5}
\]

But for distinct factors of a squarefree monic polynomial,

\[
\operatorname{Res}(f,g)^2
\mid
\operatorname{Disc}(\Omega_d)
\]

in `Z`.

The native projective discriminant formula shows that every prime divisor of

\[
\operatorname{Disc}(\Omega_d)
\]

divides `d`.  Since `p\nmid d`, (IR-5) is impossible.

Hence

\[
\boxed{f=g.}
\tag{IR-6}
\]

So every prime `p` coprime to `d` preserves each irreducible root block of `Omega_d`.

---

## 4. Transitivity without Dirichlet's theorem

Let `f` be the irreducible factor containing one chosen primitive root `v_(1,d)`.

Take any other primitive index `r` with

\[
1\le r<d,
\qquad
\gcd(r,d)=1.
\]

Factor the ordinary integer `r` into primes:

\[
r=p_1\cdots p_s.
\]

Every `p_i` is coprime to `d`.  By Section 3, each `R_(p_i)` preserves the root set of `f`.

The decimation semigroup law gives

\[
R_r=R_{p_1}\circ\cdots\circ R_{p_s}.
\]

Hence

\[
R_r(v_{1,d})=v_{r,d}
\]

also lies in `f`.

Thus `f` contains **all** roots of `Omega_d`.  Since `Omega_d` is monic and squarefree,

\[
f=\Omega_d.
\]

This proves (IR-1).

No theorem on primes in arithmetic progressions is used; factoring the finite representative `r` is enough.

---

## 5. Exact oriented/projective factor relation

Recall the normalized pullback

\[
\widehat\Psi_d(v)
=\widehat\Omega_d(R_2(v)).
\tag{IR-7}
\]

and the projective denominator-Frobenius law

\[
\widehat\Omega_d(R_2(v))
=
\prod_{e/\gcd(e,2)=d}
\widehat\Omega_e(v).
\tag{IR-8}
\]

There are two cases.

### `d` odd

Both `e=d` and `e=2d` satisfy

\[
e/\gcd(e,2)=d.
\]

Therefore

\[
\boxed{
\widehat\Psi_d(v)
=
\widehat\Omega_d(v)
\widehat\Omega_{2d}(v).
}
\tag{IR-9}
\]

Returning to monic normalization gives

\[
\boxed{
\Psi_d(v)=\Omega_d(v)\Omega_{2d}(v)
\qquad(d>1\text{ odd}).
}
\tag{IR-10}
\]

Both factors are irreducible by (IR-1), each of degree

\[
\varphi(d)/2.
\]

Hence this is the complete irreducible factorization of the oriented primitive block.

### `d` even

The only denominator preimage is `e=2d`.  Thus

\[
\boxed{
\Psi_d(v)=\Omega_{2d}(v)
\qquad(d>2\text{ even}).
}
\tag{IR-11}
\]

Therefore

\[
\boxed{
\Psi_d\text{ is irreducible over }\mathbf Q
\quad(d>2\text{ even}).
}
\tag{IR-12}
\]

For odd `d>1`, `Psi_d` has exactly two irreducible factors, exchanged by the oriented/complement-sheet structure.

---

## 6. Arithmetic meaning of the two oriented factors for odd denominator

When `d` is odd, primitive oriented indices split into two classes:

- odd numerators;
- even numerators.

Every prime coprime to `2d` is odd, so the good-prime Frobenius action preserves this parity.  The two irreducible factors in (IR-10) are exactly these two oriented sheets.

Projectivization identifies the complement/sign information and returns the single irreducible factor `Omega_d` of degree `phi(d)/2`.

Thus the earlier distinction

```text
projective scalar root block
versus
oriented/frame-retaining root block
```

has an exact irreducibility interpretation.

---

## 7. BRC compiler consequence

For a declared spectral projective root block, the BRC rational-function compiler may now treat

\[
\Omega_d
\]

as a genuine irreducible block over `Q`, not merely as an empirically irreducible polynomial for small `d`.

For the oriented block:

- even `d>2`: `Psi_d` is already irreducible;
- odd `d>1`: `Psi_d` splits canonically into the two irreducible projective-denominator blocks `Omega_d` and `Omega_(2d)`.

This gives an exact algebraic rule for when the orientation sheet doubles the irreducible root-block count.

Hard boundary: this theorem concerns the spectral family.  It does not imply irreducibility of arbitrary BRC root blocks with the same degrees.

---

## 8. Structural synthesis

The native irreducibility proof uses only

```text
integer decimation modulo p
  + denominator Frobenius
  + native projective discriminant prime support
  + resultant divisibility
  + factorization of a finite primitive index r into primes
```

and yields

```text
Omega_d: always one irreducible projective primitive block

Psi_d:
  d even -> one irreducible oriented block Omega_(2d)
  d odd  -> two irreducible oriented-sheet blocks Omega_d * Omega_(2d)
```

Freeze at free-research strength:

`PROJECTIVE_PRIMITIVE_FACTOR_OMEGA_d = NATIVELY_IRREDUCIBLE`.

`ORIENTED_PRIMITIVE_IRREDUCIBILITY_IS_CONTROLLED_BY_DENOMINATOR_PARITY`.

`BRC_ORIENTATION_SHEET_COUNT_HAS_AN_EXACT_SPECTRAL_IRREDUCIBLE_BLOCK_READOUT`.
