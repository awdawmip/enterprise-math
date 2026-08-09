# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 09

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact count-complete state for two-stage common-target witnesses and its relation to A4/E001 incidence algebra

## 1. Existence frontier is not count-complete

Stage 08 proved that Pareto pruning is future-safe for existence/budget semantics but can erase witness multiplicity. We now identify the exact finite state for the richer language:

> for every endpoint pair and every budget `(r,s)`, how many represented intermediate states satisfy the two-stage constraints?

Work on the finite zero-relation quotient `X0` with integer metric `rho`.

## 2. B32 — exact witness-cost histogram

For endpoints `x,z`, define

\[
\boxed{
H_{xz}(a,b)
=
|\{y\in X_0:\rho(x,y)=a,\ \rho(y,z)=b\}|.
}
\]

Only finitely many `(a,b)` have nonzero coefficient.

Define the budgeted witness-count function

\[
\boxed{
N_{xz}(r,s)
=
|\{y:\rho(x,y)\le r,\ \rho(y,z)\le s\}|.
}
\]

Then

\[
\boxed{
N_{xz}(r,s)
=
\sum_{a\le r}\sum_{b\le s} H_{xz}(a,b).
}
\]

Thus the full all-budget witness-count language is the two-dimensional prefix-sum transform of the exact cost histogram.

## 3. B33 — exact integer Möbius inversion

Set `N(r,s)=0` whenever either index is negative. Then

\[
\boxed{
H(a,b)
=
N(a,b)-N(a-1,b)-N(a,b-1)+N(a-1,b-1).
}
\]

Therefore the full count-query function and the histogram determine each other exactly using only integer addition/subtraction.

So, up to finite re-encoding,

\[
\boxed{H_{xz}}
\]

is the P023 task-minimal information coordinate for the full two-stage **witness-multiplicity** budget language on one endpoint pair.

This is strictly richer than the existence frontier whenever different witnesses occupy dominated or duplicate cost positions.

## 4. B34 — existence frontier is the Pareto shadow of the histogram

Let

\[
\operatorname{supp}H_{xz}
=\{(a,b):H_{xz}(a,b)>0\}.
\]

Then the Stage-05 existence frontier is exactly

\[
\boxed{
F_{xz}
=
\operatorname{ParetoMin}(\operatorname{supp}H_{xz}).
}
\]

Thus the count-complete state projects to existence state by two irreversible operations:

1. forget positive coefficient magnitudes and retain only support;
2. delete all dominated support points.

This explains B31 structurally rather than as an isolated counterexample.

## 5. Generating polynomial

Package the histogram as the finite bivariate integer polynomial

\[
\boxed{
P_{xz}(u,v)
=
\sum_{a,b}H_{xz}(a,b)u^a v^b.
}
\]

The coefficient of `u^a v^b` is exactly the number of represented intermediates with exact staged cost `(a,b)`.

`P_xz` is information-equivalent to `H_xz`; it is a convenient algebraic representation, not a new ontology.

This echoes P011's use of integer generating polynomials to encode multiplicity spectra, but the variables/semantics differ. The relationship is `COMPOSABLE_INDEPENDENT / SHARED_COEFFICIENT_ENCODING_PATTERN`, not `SAME_MOTHER`.

## 6. B35 — natural-number matrix product gives common-target witness counts

For radius `r`, let `M_r` be the `0/1` matrix of `R_r`:

\[
(M_r)_{xy}=1[xR_ry].
\]

Because the A3-generated support family is symmetric,

\[
\boxed{
(M_rM_s)_{xz}
=
N_{xz}(r,s).
}
\]

Indeed the natural-number matrix product sums

\[
\sum_y 1[xR_ry]1[yR_sz],
\]

which counts exactly the represented intermediate/common-target witnesses.

Booleanizing the result recovers A4 staged existence:

\[
\boxed{
(x,z)\in R_r;R_s
\iff
(M_rM_s)_{xz}>0.
}
\]

This directly connects the bridge to E001/A4 incidence algebra: common-target truth is the positive support of an integer witness-count product, while the integer entry retains multiplicity.

## 7. Strict information hierarchy

For a fixed endpoint pair and two-stage language:

\[
\boxed{
\text{labeled witness identities}
\Rightarrow
H/P
\Rightarrow
F
\Rightarrow
\text{single query bit}
}
\]

where each arrow forgets information relative to the richer language.

- `H/P` preserves all budgeted witness counts but not witness labels;
- `F` preserves all budgeted existence answers but not counts;
- one bit preserves one declared budget query only.

Whether an arrow is a legal collapse is determined solely by the future language.

## 8. B31 revisited

System A with normalized states `0,0.9,2` and System B with `0,0.9,1.1,2` have the same existence frontier for endpoints `0,2`:

\[
F=\{(0,2),(2,0)\}.
\]

But their histograms differ because System B has an additional coefficient at cost `(2,1)`. Hence `N(2,2)` differs (`3` versus `4`).

The histogram detects exactly the information discarded by Pareto compression.

## 9. Cross-route consequences

### A4/E001

The generated symmetric subclass now has the same basic incidence pattern as E001 common-target calculations: integer matrix multiplication counts common targets; boolean support gives existence.

### P011

Both lines use integer coefficient encodings of multiplicity data. Do not merge the semantic theories, but reuse generating-function and inversion techniques where structurally valid.

### A2/P023

The correct coarsest repair changes when the future language changes from existence to count. This is an explicit proof that “same geometric support” does not mean “same sufficient state.”

### P018

Count loss can be treated as a precision loss only when witness multiplicity is a declared observable. Otherwise storing counts is unnecessary detail.

## 10. Prior-art discipline

Two-dimensional histograms, prefix sums, Möbius/inclusion-exclusion inversion, incidence matrices and natural-number matrix products are established tools. The project-specific contribution under test is their exact placement in the task-relative A3→A4→P023 state hierarchy and the explicit connection to the existing E001/P011 multiplicity routes.

## 11. Executable reference

The reference layer adds:

- exact `(a,b)` witness histograms;
- budget prefix-count evaluation;
- inverse recovery of the histogram from all budget counts;
- sparse polynomial coefficient representation;
- common-target witness-count matrices via support-matrix products.
