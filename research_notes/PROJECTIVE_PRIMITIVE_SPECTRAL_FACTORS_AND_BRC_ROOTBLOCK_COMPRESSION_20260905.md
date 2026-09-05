# Projective primitive spectral factors and exact BRC root-block compression

Status: `FREE_RESEARCH / EXACT PROJECTIVE-SPECTRAL THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Cross-line relevance: current BRC rational-function root-block compiler.

## 1. Complement invariance of primitive spectral factors

Let `Psi_d(u)` be the monic primitive denominator-`d` spectral factor, `d>2`.

Primitive indices are stable under

`r -> d-r`.

The corresponding spectral roots obey

`u_(d-r,d)=4-u_(r,d)`.

Therefore the primitive root set is invariant under

\[
\sigma(u)=4-u,
\]

and hence

\[
\boxed{\Psi_d(4-u)=\Psi_d(u).}
\tag{PR-1}
\]

Because `phi(d)` is even for `d>2`, the degree is compatible with this involution.

The invariant polynomial ring is

\[
\mathbf Z[u]^{\sigma}
=\mathbf Z[u(4-u)].
\]

Thus there is a unique monic polynomial

\[
\Omega_d(v)\in\mathbf Z[v],
\qquad
\deg\Omega_d=\varphi(d)/2,
\]

such that

\[
\boxed{
\Psi_d(u)
=(-1)^{\varphi(d)/2}
\Omega_d(u(4-u)).
}
\tag{PR-2}
\]

The sign is forced by monicity because `u(4-u)` has leading coefficient `-1`.

---

## 2. Projective primitive roots

Set

\[
v=u(4-u)=R_2(u).
\]

The roots of `Omega_d` are exactly the complement-paired primitive roots

\[
\boxed{
v_{r,d}=R_2(u_{r,d}),}
\tag{PR-3}
\]

with `r` taken modulo the pairing `r ~ d-r`.

Therefore the projective primitive spectrum has exactly

\[
\boxed{\varphi(d)/2}
\]

roots.

This is the algebraic effect of forgetting the trace/complement sheet.

---

## 3. Normalized factor relation

Normalize both primitive factors to value one at zero:

\[
\widehat\Psi_d(0)=1,
\qquad
\widehat\Omega_d(0)=1.
\]

Then the sign and primitive-mass constant disappear, and (PR-2) becomes

\[
\boxed{
\widehat\Psi_d(u)
=\widehat\Omega_d(R_2(u)).
}
\tag{PR-4}
\]

Thus the original primitive factor is literally the pullback of the projective factor through the two-to-one spectral decimation quotient.

---

## 4. Projective Frobenius law

Because all integer decimation maps commute,

\[
R_n(R_2(u))=R_2(R_n(u)).
\]

Combine this with the primitive pullback law for `widehatPsi_d` and injectivity of polynomial substitution by the nonconstant map `R_2`.

For `d>2`,

\[
\boxed{
\widehat\Omega_d(R_n(v))
=
\prod_{e/\gcd(e,n)=d}
\widehat\Omega_e(v).
}
\tag{PR-5}
\]

Thus the projective primitive factors inherit the same denominator-Frobenius system as the oriented factors, but with half the root degree.

---

## 5. Resultants square under the two-sheet lift

Let `m,n>2`, `m!=n`.

For monic polynomials `f,g`, pulling both back through the quadratic map `R_2` duplicates every base root into its two complement preimages.  Consequently

\[
\left|
\operatorname{Res}_u(f(R_2(u)),g(R_2(u)))
\right|
=
\left|
\operatorname{Res}_v(f(v),g(v))
\right|^2.
\]

Apply this to (PR-2):

\[
\boxed{
|\operatorname{Res}(\Psi_m,\Psi_n)|
=
|\operatorname{Res}(\Omega_m,\Omega_n)|^2.
}
\tag{PR-6}
\]

Therefore the native prime-power resultant law for the oriented primitive factors immediately descends to

\[
\boxed{
|\operatorname{Res}(\Omega_m,\Omega_n)|
=
\begin{cases}
 p^{\varphi(m)/2},&n/m=p^a,\\
 1,&\text{otherwise},
\end{cases}
}
\tag{PR-7}
\]

for `2<m<n`, with the symmetric version for arbitrary ordering.

So projectivization halves not only the algebraic degree but also the prime-power resultant exponent.

---

## 6. Discriminant lift formula

Let

\[
h=\varphi(d)/2.
\]

For each root `v_i` of `Omega_d`, the quadratic equation

\[
R_2(u)=v_i
\]

has the complement pair of roots.  Their squared separation is

\[
4(4-v_i).
\]

Cross-pair resultants contribute the square of each base root difference.  Hence

\[
\boxed{
\operatorname{Disc}(\Psi_d)
=4^h\Omega_d(4)\operatorname{Disc}(\Omega_d)^2
}
\tag{PR-8}
\]

for the real-root orientation in which the discriminants are positive.  In sign-free arithmetic form, take absolute values.

This gives an exact bridge from oriented primitive discriminants to projective ones.

---

## 7. Midpoint value law

The special value `u=2` is the fixed midpoint of the complement involution and satisfies

\[
R_2(2)=4.
\]

Thus

\[
|\Psi_d(2)|=|\Omega_d(4)|.
\]

A purely finite divisor/decimation argument gives, for `d>2`,

\[
\boxed{
|\Omega_d(4)|
=|\Psi_d(2)|
=
\begin{cases}
1,&d\text{ odd},\\
 p,&d=2p^a\text{ for a prime }p,\\
1,&d\text{ even and }d/2\text{ is not a prime power}.
\end{cases}
}
\tag{PR-9}
\]

For powers of two this includes the value `2`.

This is the spectral midpoint analogue of the familiar prime-power special-value split, obtained here from the finite spectral divisor system.

---

## 8. BRC root-block meaning

The current BRC compiler works over rational-function coefficient fields and preserves variable-rotation naturality.  The projective factor theorem supplies an exact optional quotient for a declared `2x2` boundary-transfer sector.

If only the projective trace defect

\[
v=4-\frac{(\operatorname{tr}A)^2}{\det A}
\]

is an allowed observation, then a primitive oriented root block `Psi_d` may be replaced by the degree-halved projective block `Omega_d`.

This compression is:

- exact for repetition/decimation observations;
- over `Z[v]` / the BRC rational-function field;
- compatible with the denominator-Frobenius action;
- explicit about information loss.

What is lost is the complement/trace sheet.  Therefore this quotient must **not** be used when the requested observation depends on:

- the sign of the trace;
- oriented phase;
- frame-sensitive path transfer;
- distinguishing `u` from `4-u`.

This is an example of a genuinely operation-safe quotient for one declared observable family, not a universal BRC quotient.

---

## 9. Compatibility note

In a later classical readout, `Omega_d` is the real-trace/minimal-polynomial object attached to primitive roots of unity.  Numerical factorization for `3<=d<=30` agrees with irreducibility of the projective factor of degree `phi(d)/2`.

Irreducibility is **not** promoted here as a native theorem unless a proof independent of the classical cyclotomic/Galois identification is supplied.  The exact native statements are (PR-1)-(PR-9) excluding that later irreducibility label.

Freeze:

`PROJECTIVE_TRACE_QUOTIENT_HALVES_PRIMITIVE_ROOT_DEGREE`.

`ORIENTED_RESULTANT = PROJECTIVE_RESULTANT^2`.

`BRC_PROJECTIVE_ROOTBLOCK_COMPRESSION = EXACT_FOR_DECLARED_PROJECTIVE_OBSERVATIONS`.
