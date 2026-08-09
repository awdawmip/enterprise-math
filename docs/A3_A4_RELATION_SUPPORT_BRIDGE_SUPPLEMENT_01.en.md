# A3 ↔ A4 Relation-Support Bridge — Supplement 01

Status: `ACTIVE RESEARCH NOTE`  
Scope: A4 common-target composition and split-completeness inside the A3-generated support subclass

## 1. Setup

Use the Stage-01 A3-generated symmetric support family on zero-relation classes:

\[
[i]R_r[j]\iff |Z_{ij}|\le r m_i m_j.
\]

Because the predicate is symmetric,

\[
R_r^{-1}=R_r.
\]

A4 common-target composition therefore becomes

\[
\boxed{C_{r,s}=R_r;R_s.}
\]

Stage 01 already proves

\[
R_r;R_s\subseteq R_{r+s}.
\]

## 2. B04 — split-completeness equals budget interpolation

For fixed `r,s`, the equality

\[
\boxed{R_r;R_s=R_{r+s}}
\]

holds if and only if every endpoint pair `[i],[k]` satisfying

\[
|Z_{ik}|\le(r+s)m_im_k
\]

admits at least one quotient class `[j]` such that

\[
|Z_{ij}|\le r m_i m_j,
\qquad
|Z_{jk}|\le s m_jm_k.
\]

Thus A4 split-completeness becomes an **interpolation property of the represented A3 state space**.

The inclusion from left to right is the weighted triangle theorem. The reverse inclusion is exactly the existence of such an intermediate witness.

## 3. A discrete-hole interpretation

Failure of split-completeness does not mean the endpoint radius bound is wrong. It means that the represented quotient state set has no admissible intermediate state at the requested budget split.

Therefore the defect

\[
R_{r+s}\setminus(R_r;R_s)
\]

is a finite set of **missing interpolation witnesses**.

This gives A4 split-completeness a concrete A3/A5 reading: it tests whether the discrete represented state space is sufficiently filled along the relation coordinate to realize the requested decomposition.

## 4. B05 — unit-capacity integer-convex sufficient condition

Suppose all capacities are one and, after zero-relation quotient, the represented integer values form an interval

\[
\{a,a+1,\ldots,b\}.
\]

Then the generated family is split-complete for every non-negative integer `r,s`:

\[
R_r;R_s=R_{r+s}.
\]

### Proof

For unit capacities, `Z_ij=c_i-c_j`, so support is ordinary integer difference:

\[
|c_i-c_k|\le r+s.
\]

Move from `c_i` toward `c_k` by at most `r` integer steps; call the resulting represented value `c_j`. Integer convexity guarantees that `c_j` is present. Then

\[
|c_i-c_j|\le r,
\qquad
|c_j-c_k|\le s.
\]

Hence every total-budget pair has an intermediate witness.

This is a sufficient condition, not claimed necessary in the weighted or general finite case.

## 5. B06 — minimal hole counterexample

Take unit capacities with represented values

\[
\{0,2\}.
\]

Then

\[
(0,2)\in R_2,
\]

but `R_1` is only the identity because the value `1` is absent. Therefore

\[
(0,2)\notin R_1;R_1,
\]

and

\[
\boxed{R_1;R_1\subsetneq R_2.}
\]

The missing state `1` is exactly the missing interpolation witness.

## 6. Consequences

### For A4

Split-completeness should remain a stronger property, not a universal admissible-support axiom. Even supports canonically generated from a closed A3 state can fail it because the represented state set is sparse.

### For A3

The set `R_(r+s) \ (R_r;R_s)` is a new finite observable of representation holes. It distinguishes endpoint closeness from realizable staged transport.

### For A5/P022

Geometry-specific work can ask whether lattice/root-lattice state sets satisfy corresponding interpolation properties, and at what radii. This is a precise route from abstract A4 split-completeness to discrete-geometric geodesic filling.

### For A2/P023

If a future operation assumes two-stage support composition rather than only endpoint support, then `R_(r+s)` alone is not sufficient whenever interpolation witnesses are missing. The extra witness requirement is again a future-compatibility/refinement obligation.

## 7. Executable reference

`relation_support_bridge.py` now includes:

- `common_target_support`;
- `split_complete_at`;
- `missing_interpolations`.

Tests include:

- unit values `{0,1,2}`: `R_1;R_1=R_2`;
- unit values `{0,2}`: strict failure caused by the missing midpoint.
