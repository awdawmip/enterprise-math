# Free Research — `S_3`-Equivariant Color Transfer and Scalar Standard Eigenvalue

Status: `FREE_RESEARCH_FRONTIER / TWO_PARAMETER_CLASSIFICATION / STANDARD_EIGENVALUE_EXACT / GLOBAL_S3_KERNEL_IDENTIFIED / COLORED_SCALE_CASCADE_REDUCED / ARITHMETIC_TRANSITION_BOUND_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_DEEPEST_COLORED_TRANSFER_20260904.md`

## 1. Executive advance

Once the deepest lower-scale state retains its three-valued provenance color, every linear `S_3`-equivariant color transition has only two coefficients:

- one diagonal/same-color coefficient;
- one common off-diagonal/color-change coefficient.

Its action on the two-dimensional standard representation is therefore multiplication by one scalar: the difference between those coefficients.

This reduces the colored cascade from a matrix-valued spectral problem to a scalar transition coefficient at every scale.

---

## 2. Canonical two-parameter transfer

For a color vector

\[
h=(h_1,h_2,h_3),
\]

define

\[
\boxed{
(T_{d,o}h)_i
=d h_i+o\sum_{j\ne i}h_j
=(d-o)h_i+o(h_1+h_2+h_3).
}
\tag{2.1}
\]

The symmetric group acts transitively on diagonal index pairs `(i,i)` and separately on off-diagonal pairs `(i,j)`, `i!=j`.  Thus every `S_3`-equivariant three-color matrix has this diagonal/off-diagonal form.

The trivial color line has eigenvalue

\[
\boxed{\lambda_{\rm triv}=d+2o,}
\tag{2.2}
\]

while the standard plane

\[
h_1+h_2+h_3=0
\]

has eigenvalue

\[
\boxed{\lambda_{\rm std}=d-o.}
\tag{2.3}
\]

---

## SCT-T01 — Exact standard energy law

Define the complete color pair energy

\[
\mathcal E_{\rm col}(h)
=(h_1-h_2)^2+(h_2-h_3)^2+(h_3-h_1)^2.
\]

Since

\[
(T_{d,o}h)_i-(T_{d,o}h)_j
=(d-o)(h_i-h_j),
\]

we have, without any centering assumption,

\[
\boxed{
\mathcal E_{\rm col}(T_{d,o}h)
=(d-o)^2\mathcal E_{\rm col}(h).
}
\tag{3.1}
\]

If the transition is Markov normalized,

\[
d+2o=1,
\]

then constants are fixed and all quantitative decay is controlled by the single scalar `d-o`.

---

## 4. The weighted `S_3` lift-project kernel

The global weighted history mixer previously derived is

\[
(\mathcal K_3h)_i
=\frac{h_i+2\bar h}{3},
\qquad
\bar h=\frac{h_1+h_2+h_3}{3}
\]

on the uniform three-color fiber.

Expanding it in diagonal/off-diagonal form gives

\[
\boxed{
d=\frac59,
\qquad
o=\frac29.}
\tag{4.1}
\]

Indeed,

\[
\frac59h_i+rac29(h_j+h_k)
=\frac13h_i+rac29(h_1+h_2+h_3)
=\frac{h_i+2\bar h}{3}.
\]

The Markov condition holds:

\[
\frac59+2\frac29=1.
\]

Its standard eigenvalue is

\[
\boxed{
\lambda_{\rm std}
=rac59-rac29
=rac13,}
\tag{4.2}
\]

and its standard energy survival is

\[
\boxed{
\lambda_{\rm std}^2=\frac19.}
\tag{4.3}
\]

Thus the global `1/9` energy factor is the square of the unique nontrivial eigenvalue of an explicit `S_3`-equivariant Markov kernel.

---

## 5. Deepest balanced kernel

For each endpoint `m`, the deepest cutoff kernel is fiberwise balanced:

\[
\kappa_Y(1,m)=\kappa_Y(2,m)=\kappa_Y(3,m).
\]

As a scalar color transition, equal rows/columns correspond to `d=o`; hence the standard eigenvalue is zero after scalarization.  This restates pointwise standard cancellation in operator language.

To preserve standard energy across descent, the output must remain in the colored bundle before this balanced scalar pushforward is taken.  The colored transfer and scalarized transfer therefore have sharply different roles:

- colored transfer: carries the standard vector to a lower-scale fiber;
- scalar pushforward: projects to the trivial line and kills the standard vector.

---

## 6. Cascade reduction

An arbitrary `S_3`-covariant transition between two colored endpoint layers can now be summarized by

\[
(d_Y(m,m'),o_Y(m,m')).
\]

On the standard bundle its full matrix action is simply

\[
\boxed{
K_Y^{\rm std}(m,m')
=d_Y(m,m')-o_Y(m,m').}
\tag{6.1}
\]

The multi-scale colored problem is therefore a scalar signed kernel on arithmetic endpoints.  The color matrix no longer needs separate diagonalization at each scale.

For a positive Markov color transition,

\[
|d-o|\le d+2o=1.
\]

Strict decay occurs precisely when positive mass changes color.  Pure color preservation has `o=0,d=1` and no standard contraction; complete color randomization has `d=o=1/3` and kills the standard sector.

---

## 7. Formal status

Lean file:

- `EnterpriseMath/Relation/S3EquivariantColorTransfer.lean`.

It formalizes:

1. the two-parameter color transfer;
2. the trivial and standard eigenvalues;
3. invariance of the standard sector;
4. exact pair-energy scaling;
5. Markov preservation of constants;
6. identification of the weighted `S_3` lift-project kernel with `(d,o)=(5/9,2/9)`;
7. the exact `1/3` and `1/9` factors.

Lean-green status is not asserted until workflow completion.

---

## 8. Updated next theorem

The remaining colored transition problem is scalar:

> Determine or bound the standard endpoint kernel
> \[
> K_Y^{\rm std}(m,m')=d_Y(m,m')-o_Y(m,m')
> \]
> produced by the arithmetic deepest-chamber descent.

A bound on its operator norm, together with the exact total deepest mass `1/9`, would close the representation-theoretic portion of the cube-root cascade.
