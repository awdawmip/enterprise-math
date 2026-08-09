# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 07

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact factorization of the whole generated-support language through the integer metric, and its boundary against richer A3 operations

## 1. The compression question

Earlier stages used the integer metric

\[
\rho(x,y)=\min\{r:xR_ry\}
\]

as a derived A3→A4 object. We now ask a stronger P023-style question:

> for which entire future operation language is `rho` itself already a complete coarse state?

The answer is exact for the generated support language.

## 2. Define the support language

Let `L_supp` be the finite-expression language generated from the primitive radius relations

\[
R_r=\{(x,y):\rho(x,y)\le r\},
\qquad r\in\mathbb N,
\]

using finite relational composition. One may also allow finite union, intersection and converse without changing the theorem below; all are operations on finite relations already determined by the primitive `R_r` family.

The labeled quotient-state set `X0` is part of the state because the language can ask about specific endpoint classes.

## 3. B24 — metric factorization theorem

Every `L_supp` expression is uniquely determined by

\[
\boxed{(X_0,\rho).}
\]

### Proof

For every radius `r`, `R_r` is obtained by the threshold rule

\[
(x,y)\in R_r\iff\rho(x,y)\le r.
\]

Finite relation composition/union/intersection/converse is computed entirely from the resulting finite relations. Therefore structural induction on any support-language expression reconstructs its exact result using only `(X0,rho)`.

Hence the map

\[
(m,c,Z)
\longmapsto
(X_0,\rho)
\]

is a future-safe quotient for the whole generated-support language.

No exact `Z_ij`, capacity, total, rational density, or hidden real completion is required after this language boundary has been declared.

## 4. B25 — information equivalence for the full primitive support language

Conversely, the complete family of primitive support truths recovers `rho` exactly:

\[
\boxed{
\rho(x,y)=\min\{r:(x,y)\in R_r\}.
}
\]

Therefore `(X0,rho)` and the full labeled primitive support family `{R_r}` contain exactly the same information up to finite re-encoding.

Consequently, for a future language that includes all labeled primitive radius queries, `rho` is not merely sufficient; it is a canonical information-complete coordinate for that language.

This is a P023 statement about semantic information content, not a claim about minimum machine bits or optimal serialization.

## 5. B26 — nested legal-collapse hierarchy

We now have an explicit chain of progressively more task-specific states:

\[
\boxed{
(m,c,Z)
\longrightarrow
(X_0,\rho)
\longrightarrow
\text{task-specific thresholds/frontiers}
}
\]

with different proof obligations at each arrow.

### Full A3 relation-state language

Keep `(m,c,Z)` or another representation known to reconstruct it when future operations need exact signed weighted relations, capacities, partition aggregation, or reconstruction.

### Full generated-support language

`(X0,rho)` is exact by B24.

### Restricted endpoint/staged query language

Stage 04–06 permit further compression to:

- scalar thresholds;
- coarse MAY/MUST intervals;
- two-stage Pareto frontiers;
- fixed-depth Pareto antichains;
- under geodesicity, endpoint `rho` alone again for every finite support depth.

Thus legal compression is a ladder indexed by the declared future language.

## 6. B27 — negative boundary: `rho` is not a full A3 quotient state

The metric forgets sign and sub-unit normalized relation detail. Those distinctions can matter to A3 partition aggregation.

Take equal capacities

\[
m=(2,2,2,2)
\]

and two total vectors

\[
c=(-3,-2,-1,2),
\]

\[
\tilde c=(-3,-1,-2,2).
\]

Both produce the same labeled integer relation metric

\[
\rho=
\begin{pmatrix}
0&1&1&3\\
1&0&1&2\\
1&1&0&2\\
3&2&2&0
\end{pmatrix}.
\]

Now use the same A3 partition

\[
A=\{0,1\},\qquad B=\{2,3\}.
\]

For the first fine state, the direct aggregated coarse threshold is

\[
\bar\rho_{AB}=2,
\]

while for the second it is

\[
\tilde{\bar\rho}_{AB}=1.
\]

Therefore two A3 states with identical `(X0,rho)` can evolve differently under the A3 operation “aggregate this declared partition and then read the coarse relation threshold.”

Hence

\[
\boxed{
(X_0,\rho)\text{ is future-safe for }L_{supp}
\text{ but not for the full A3 partition-operation language.}
}
\]

This is exactly the sort of boundary P023 requires us to state before discarding detail.

## 7. Relation to A3 piecewise non-monotonicity

B24 does not say that replacing `(m,c,Z)` by `rho` is universally “more efficient precision.” It says the replacement is exact **for a declared language**.

If a later program adds partition aggregation, signed-response, piecewise guards, or other A3 operations that read distinctions erased by `rho`, the quotient must be re-audited and repaired. The A3 piecewise result independently shows that even arbitrary refinement can fail to preserve exactness unless the refined state exposes the right semantic distinctions.

## 8. A closed support-language state machine

Given `(X0,rho)`:

1. generate any primitive `R_r` by thresholding `rho`;
2. compute any finite support word by relation composition;
3. compute common-target relations;
4. compute all fixed-depth Pareto frontiers;
5. test geodesicity/split-completeness;
6. if geodesic, collapse every finite support word to total budget.

Thus the support-language subsystem is closed after the A3→metric quotient.

## 9. Cross-route consequences

### A2/P023

B24/B27 together are a clean worked example of task-relative quotient legality: one state reduction is exact for one operation algebra and invalid for a richer one.

### A4

For the generated subclass, `(X0,rho)` can be treated as a complete finite support-state representation. Arbitrary A4 relations remain outside this generated subclass.

### A3

Do not replace the A3 weighted relation core by `rho`. Use `rho` only as a support-language quotient/interface.

### P018

This is an explicit precision projection whose legal future scope is mathematically declared rather than inferred from intuition.

## 10. Prior-art discipline

A metric determines its radius relations, and finite relational algebra on those relations is standard mathematics. The project-specific contribution under test is the explicit semantic placement of this quotient inside the A3→A4→P023 architecture and the exact counterexample showing where that quotient ceases to be legal.

## 11. Executable reference

The reference layer adds:

- support relations generated directly from a metric matrix;
- finite support-word evaluation;
- metric reconstruction from a complete primitive radius family;
- the B27 same-metric/different-A3-aggregation regression counterexample.
