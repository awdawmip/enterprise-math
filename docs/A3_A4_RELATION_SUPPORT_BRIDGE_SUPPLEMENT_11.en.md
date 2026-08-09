# A3 ↔ A4 ↔ P021 ↔ A2/P023 Bridge — Supplement 11

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact integer coupling defect for witness-identity erasure in one-step composition counts

## 1. Motivation

P021 direction transport proved that cardinality shadows are not composition-complete in general. For one middle direction class with `m` exact incidences it introduced predecessor/successor witness profiles

\[
l=(l_1,\ldots,l_m),
\qquad
r=(r_1,\ldots,r_m),
\]

with

\[
L=\sum_i l_i,
\qquad
R=\sum_i r_i,
\qquad
N=\sum_i l_i r_i,
\]

where `N` is the exact matched three-edge-chain count.

P021 Stage 12 proved the sufficient condition

\[
\text{one of }l,r\text{ uniform}
\Longrightarrow
mN=LR.
\]

This note identifies the exact obstruction and therefore strictly generalizes that safe-reduction regime.

## 2. B41 — integer coupling defect

Define

\[
\boxed{
\Delta(l,r)
=
m\sum_i l_i r_i
-
\left(\sum_i l_i\right)
\left(\sum_i r_i\right).
}
\]

Equivalently,

\[
\boxed{
\Delta(l,r)
=
\sum_{1\le i<j\le m}
(l_i-l_j)(r_i-r_j).
}
\]

### Proof of the pair-difference identity

Expand the right-hand side:

\[
\sum_{i<j}
(l_ir_i+l_jr_j-l_ir_j-l_jr_i).
\]

Each diagonal term `l_i r_i` occurs exactly `m-1` times, while the off-diagonal terms together give

\[
\sum_{i\ne j}l_i r_j
=LR-\sum_i l_i r_i.
\]

Hence the total is

\[
(m-1)N-(LR-N)=mN-LR.
\]

The defect is a signed integer. No averaging, probability, or rational arithmetic is required.

## 3. B42 — exact cardinality-sufficiency criterion

The exact matched count satisfies

\[
\boxed{
N=\frac{LR+\Delta}{m}.
}
\]

The numerator is automatically divisible by `m` because it equals `mN`.

Therefore

\[
\boxed{
\Delta=0
\iff
mN=LR.
}
\]

Thus cardinality-only composition from `(m,L,R)` is exact **if and only if** the coupling defect vanishes.

This is the exact safe-erasure criterion for this declared one-step count observable.

## 4. B43 — P021 uniform-fiber theorem is a strict sufficient subcase

If `l_i=c` for every `i`, then

\[
N=cR,
\qquad
L=mc,
\]

so `mN=LR` and `Delta=0`. The same argument holds when `r` is uniform.

Hence P021 Stage 12 is recovered immediately.

But uniformity is not necessary.

Example:

\[
l=(0,0,1),
\qquad
r=(0,2,1).
\]

Both profiles are non-uniform, yet

\[
m=3,
\quad
L=1,
\quad
R=3,
\quad
N=1,
\]

and therefore

\[
\Delta=3\cdot1-1\cdot3=0.
\]

So the true structural condition is zero coupling defect, with uniformity only one easy-to-check sufficient regime.

## 5. Aligned and anti-aligned minimal examples

For `m=2`, take

\[
l=(1,0).
\]

### Aligned

\[
r=(1,0)
\]

gives

\[
L=R=1,
\quad
N=1,
\quad
\Delta=1.
\]

### Anti-aligned

\[
r=(0,1)
\]

gives the same marginal cardinalities

\[
L=R=1,
\]

but

\[
N=0,
\quad
\Delta=-1.
\]

Thus the sign and magnitude of `Delta` record exact middle-incidence coupling information that is invisible to the marginals.

## 6. B44 — `Delta` is the P023 coarsest one-step repair up to re-encoding

Take the coarse state

\[
q=(m,L,R)
\]

and the declared future observable

\[
h=N.
\]

P023-T02 says `(q,N)` is the coarsest one-step repair of `q` for exact composition count.

Given `q`, the maps

\[
N\mapsto\Delta=mN-LR
\]

and

\[
\Delta\mapsto N=(LR+\Delta)/m
\]

are mutually inverse on realizable states.

Therefore `(q,Delta)` and `(q,N)` induce the same partition of fine witness profiles. Hence

\[
\boxed{
(m,L,R,\Delta)
}
\]

is a canonical integer re-encoding of the P023 coarsest repair for this one-step count language.

This does **not** claim minimum machine-bit length; it is a statement about exact quotient information.

## 7. B45 — matrix coupling defect

Let `A_{\alpha i}` count left witnesses from coarse source class `alpha` into exact middle incidence `i`, and let `B_{i\beta}` count right witnesses from `i` into coarse target class `beta`.

Define marginals

\[
L_\alpha=\sum_i A_{\alpha i},
\qquad
R_\beta=\sum_i B_{i\beta},
\]

and exact composite count matrix

\[
C_{\alpha\beta}
=\sum_i A_{\alpha i}B_{i\beta}.
\]

Define the coupling-defect matrix

\[
\boxed{
D_{\alpha\beta}
=
mC_{\alpha\beta}-L_\alpha R_\beta.
}
\]

Then entrywise

\[
\boxed{
D_{\alpha\beta}
=
\sum_{i<j}
(A_{\alpha i}-A_{\alpha j})
(B_{i\beta}-B_{j\beta}).
}
\]

and

\[
\boxed{
C_{\alpha\beta}
=
\frac{L_\alpha R_\beta+D_{\alpha\beta}}{m}.
}
\]

Thus, given `m` and the left/right marginal count vectors, `D` is information-equivalent to the exact current composite count matrix `C`.

The entire cardinality-shadow matrix multiplication rule is exact iff

\[
\boxed{D\equiv0.}
\]

Uniformity of every relevant left row or right column is sufficient for the corresponding defect entries to vanish, but again is not necessary.

## 8. B46 — repair scope boundary

`Delta` or `D` repairs **the declared current composition-count observable**. It does not restore exact middle witness labels.

Therefore it is not automatically future-complete for:

- a later composition that needs to join on exact witness identity;
- labeled witness transport;
- operations that distinguish different fine profiles sharing the same marginals and current composite count;
- any richer P021/A4 future language not factoring through the repaired count state.

This is exactly the P023 distinction between one-step repair and closure under a whole future operation algebra.

The correct hierarchy is:

\[
\text{marginals}
\xrightarrow{+\Delta}
\text{exact current count}
\quad\text{(one-step safe)}
\]

versus

\[
\text{witness-sensitive future algebra}
\Rightarrow
\text{retain/refine additional witness structure}.
\]

## 9. Relation to Stage 09–10 count tensors

Stage 09–10 kept exact counts indexed by staged cost vectors. B41–B45 address a different compression axis: how much exact middle-incidence coupling must be retained when one first aggregates witness identity to marginals.

The two structures can be combined when the declared future language needs both:

- cost-sensitive multiplicity;
- exact composition through an aggregated middle class.

But they should not be silently merged into one universal state.

## 10. Relation to P011

The pair-difference formula resembles an integer covariance/correlation numerator. Such algebra is established prior art. P011 likewise uses integer multiplicity summaries before optional normalization.

The project-specific point here is not discovery of covariance. It is the exact use of `Delta` as a P023 repair coordinate for witness-identity erasure and the strict generalization of P021's uniform-fiber safe-reduction condition.

## 11. Prior-art discipline

Dot-product/marginal identities, covariance numerators, contingency-table coupling, and matrix multiplication are standard mathematics. No novelty claim is made for those primitives.

The current contribution under test is their placement in the Enterprise Math state hierarchy:

`witness identity -> marginals + coupling defect -> exact current composition count`,

with an explicit future-language boundary and a direct theorem-level connection between P021 and P023.

## 12. Executable reference

The bridge reference layer adds:

- scalar coupling defect and pair-difference identity;
- exact recovery of composition count from marginals + defect;
- matrix coupling-defect calculation;
- uniform and non-uniform zero-defect examples;
- aligned/anti-aligned same-marginal counterexamples.
