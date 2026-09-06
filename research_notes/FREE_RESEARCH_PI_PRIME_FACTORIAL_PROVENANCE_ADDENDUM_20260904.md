# Pi-to-Prime Addendum — The Factor Six as Cubic Provenance, not Sixfold Spatial Degeneracy

Status: `FREE_RESEARCH_ADDENDUM / ANCHOR_EXPOSED / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_BIRTH_SPECTRAL_DETERMINANT_20260904.md`
Dependencies: current #1159 PR #1172 finite Dirichlet/Krawtchouk chain; #1161 internal `Pi_*=tau` completion.

## 1. Why this addendum exists

The parent frontier proved, at current research strength,

\[
\tau^2=6\lim_{M\to\infty} Z_M(2),
\qquad
Z_M(2)=\prod_{p\le M}(1-p^{-2})^{-1}.
\]

P000 independently says Enterprise space has six spatial dimensions. The equality of the two integers `6` was therefore an obvious candidate bridge, but it was left open rather than asserted.

This addendum sharpens that boundary in both directions:

1. naive sixfold spatial degeneracy gives the **wrong functional form**;
2. the current #1159 finite determinant proof already contains a precise, non-spatial source for the coefficient `6`: it is the factorial orbit size `3!` of the cubic normalized coefficient.

---

## PBF-T10 — Sixfold degeneracy no-go for the prime determinant

Let the arithmetic birth block at cutoff `M` be

\[
B_M=\operatorname{diag}(p:p\le M,\ p\text{ prime}),
\]

and define

\[
Z_M(2)=\det(I-B_M^{-2})^{-1}.
\]

A naive attempt to encode P000's six spatial degrees of freedom is to give every prime eigenmode a sixfold spatial degeneracy, i.e. replace `B_M` by

\[
\widetilde B_M=B_M\otimes I_6.
\]

Every prime eigenvalue `p` is then repeated six times. Consequently

\[
\boxed{
\det(I-\widetilde B_M^{-2})^{-1}
=\prod_{p\le M}(1-p^{-2})^{-6}
=Z_M(2)^6.
}
\]

But the internally derived full-turn relation is

\[
\tau^2=6\lim_M Z_M(2),
\]

not

\[
\tau^2=\lim_M Z_M(2)^6.
\]

Therefore:

\[
\boxed{
\text{six-dimensional mode degeneracy}
\neq
\text{the source of the coefficient }6.
}
\]

This excludes the most obvious `six copies of every prime mode` explanation. Any future six-dimensional bridge must use a genuinely coupled incidence/rotation observable, not mere eigenvalue multiplicity.

---

## PBF-T11 — Exact finite source of `1/6` in #1159

Current #1159 Lean theorem `normalized_choose_eq_unit_defects` states

\[
\frac{\binom{M+j}{2j+1}}{M^{2j+1}}
=\frac1{(2j+1)!}
\prod_{r=1}^{j}\left(1-\frac{r^2}{M^2}\right),
\qquad j<M.
\]

At the first nontrivial mode `j=1`, this becomes the exact finite identity

\[
\boxed{
\frac{\binom{M+1}{3}}{M^3}
=\frac16\left(1-\frac1{M^2}\right).
}
\]

Equivalently,

\[
6\binom{M+1}{3}
=(M+1)M(M-1).
\]

The right side is the number of ordered triples of **distinct** slots chosen from an `(M+1)`-slot ordered carrier. The left side is `3!` times the number of unordered three-slot supports. Hence the factor

\[
\boxed{6=3!=|S_3|}
\]

is already present at every finite cutoff as the provenance multiplicity forgotten when six ordered histories recoalesce to one unordered three-event support.

After normalization,

\[
\frac{\binom{M+1}{3}}{M^3}
\longrightarrow\frac1{3!}.
\]

Thus the cubic coefficient of the internal sine-type completion does not need a six-spatial-dimension explanation: its current proof-theoretic origin is a finite `S_3` ordering quotient plus an explicit finite defect `1-1/M^2`.

---

## PBF-T12 — Prime quadratic completion as the cubic provenance quotient

The internal #1159 sine-type product has

\[
\frac{S(x)}x
=1-\frac{x^2}{3!}+O(x^4)
=\prod_{n\ge1}\left(1-\frac{x^2}{n^2\tau^2}\right).
\]

Comparing the quadratic coefficient gives

\[
\sum_{n\ge1}\frac1{n^2}=\frac{\tau^2}{3!}.
\]

Unique factorization gives

\[
\boxed{
Z_{\mathbb P}(2)
:=\prod_p(1-p^{-2})^{-1}
=\frac{\tau^2}{3!}.
}
\]

So the most faithful current geometric/combinatorial reading is

\[
\boxed{
\text{quadratic prime-birth completion}
=
\text{full-turn-square completion divided by cubic provenance multiplicity }3!.
}
\]

This is stronger and better typed than the earlier tempting statement `the 6 comes from six spatial dimensions`.

The finite #1159 coefficient says exactly what the quotient forgets: ordering provenance among three distinct rotation-mode slots. The prime determinant says what survives on the arithmetic side: irreducible multiplicative birth directions observed at the first stable quadratic completion order.

---

## 4. Relation to Weighted-BRC typing

This interpretation matches the global branch-typing rule:

- support and multiplicity/provenance are different carriers;
- positive multiplicity is not silently discardable;
- recoalescing several histories into one support state is a typed quotient;
- logarithms are optional derived readouts.

Here the `S_3` orbit has support size one after recoalescence but provenance multiplicity six before quotienting. The coefficient `1/6` is therefore naturally a provenance-normalization factor, not a new primitive spatial metric constant.

No claim is made that current Weighted-BRC theorem IDs themselves imply the Dirichlet coefficient theorem; the compatibility is semantic/typing, while the exact coefficient identity comes from the #1159 finite determinant chain.

---

## 5. Stronger native bridge question

The old open question was:

> Is the coefficient `6` forced by P000's six spatial dimensions?

PBF-T10 shows that naive spatial degeneracy is the wrong mechanism. The sharper question is now:

> Can the exact finite `S_3` three-history provenance quotient already present in the #1159 Dirichlet rotation carrier be realized as a genuine local Enterprise rotation-history cell/trace, so that the six ordered histories are native finite trajectories which recoalesce to one retained support state?

This would connect three current pieces without a numerical coincidence:

\[
\text{native finite rotation histories}
\to
S_3\text{-provenance recoalescence}
\to
\frac1{3!}\text{ cubic coefficient}
\to
Z_{\mathbb P}(2)=\tau^2/3!.
\]

A particularly discriminating route is to compare this with #1161's native commuting diamond, where two orderings `X_iX_j` and `X_jX_i` give a two-history provenance fiber. A genuine three-generator extension would need to justify six admissible orderings without reviving the superseded native-vector identity or treating the three-axis research slice as the whole six-dimensional world.

Until such a finite native trace is constructed, the `S_3` interpretation is exact at the current finite Dirichlet rotation-mode carrier and **not yet** promoted to a G0 native cell theorem.

---

## Current classification

- `SIXFOLD_EIGENVALUE_DEGENERACY -> Z(2)^6`: `PROVED / FINITE LINEAR ALGEBRA`.
- `SIXFOLD_DEGENERACY EXPLAINS 6*Z(2)`: `REFUTED`.
- `NORMALIZED CUBIC COEFFICIENT = (1/3!)(1-1/M^2)`: `LEAN-PROVED IN #1172 DEPENDENCY`.
- `6 = S3 ORDERED-TRIPLE PROVENANCE MULTIPLICITY`: `EXACT FINITE COMBINATORIAL INTERPRETATION`.
- `Z_P(2)=tau^2/3!`: `RESEARCH-PROVED GIVEN #1159 INFINITE PRODUCT`.
- `S3 PROVENANCE QUOTIENT IS LITERAL G0 ENTERPRISE ROTATION CELL`: `OPEN / NOT_DERIVED`.
- `FACTOR 6 = P000 SPACE DIMENSION`: `NO LONGER PREFERRED; NAIVE VERSION REFUTED`.
