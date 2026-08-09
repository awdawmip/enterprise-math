# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 04

Status: `ACTIVE RESEARCH NOTE`  
Scope: task-minimal exact coordinate for the full two-stage/common-target budget language

## 1. Why endpoint thresholds are not enough

Stage 04 showed that one-step all-radius MAY/MUST semantics is exactly captured by scalar thresholds `d^-` and `d^+`. Stage 02/03 showed that two-stage support additionally depends on whether intermediate states actually exist.

Therefore a full staged query language needs a richer, but still finite, coordinate.

Work on the A3 zero-relation quotient `X0` with integer metric

\[
\rho(x,z)=\min\{r:xR_rz\}.
\]

For fixed ordered endpoints `x,z`, every possible intermediate state `y` has a two-stage budget cost

\[
\boxed{c_y(x,z)=(\rho(x,y),\rho(y,z))\in\mathbb N^2.}
\]

## 2. B13 — staged budget Pareto frontier

Let

\[
C_{xz}=\{c_y(x,z):y\in X_0\}.
\]

Order `N^2` coordinatewise:

\[
(a,b)\preceq(r,s)\iff a\le r\text{ and }b\le s.
\]

Define the finite Pareto-minimal antichain

\[
\boxed{F_{xz}=\operatorname{Min}_{\preceq}(C_{xz}).}
\]

Then for every integer budget pair `(r,s)`,

\[
\boxed{
(x,z)\in R_r;R_s
\iff
\exists(a,b)\in F_{xz}:a\le r,\ b\le s.
}
\]

### Proof

By definition, `(x,z) in R_r;R_s` iff some represented intermediate `y` satisfies

\[
\rho(x,y)\le r,
\qquad
\rho(y,z)\le s.
\]

This is exactly the statement that one cost point in `C_xz` lies below `(r,s)`. Every finite cost set has a Pareto-minimal point below each of its points, so dominated costs can be deleted without changing any query answer.

Thus the upward closure of `F_xz` is exactly the complete truth set of all two-stage budget queries.

## 3. B14 — frontier is task-minimal for the whole two-stage language

Let

\[
H_{xz}(r,s)=1[(x,z)\in R_r;R_s].
\]

The full truth function `H_xz` determines `F_xz` uniquely: `F_xz` is exactly the set of coordinatewise-minimal budget pairs at which `H_xz` becomes true.

Conversely B13 shows `F_xz` reconstructs `H_xz` for every `(r,s)`.

Therefore, up to re-encoding,

\[
\boxed{F_{xz}}
\]

is the P023 coarsest repair coordinate for the **entire two-stage integer-budget query language** on the endpoint pair.

This refines the Stage-04 hierarchy:

- one fixed `(r,s)` query: one truth bit;
- all one-step radii: one scalar threshold (`d^-` or `d^+` depending on modality);
- all two-stage budget pairs: one finite Pareto antichain `F_xz`;
- unrestricted future operation words: use the general P023 compatible-quotient closure.

The required state grows with the declared future language, not with an abstract demand to keep all fine detail.

## 4. B15 — triangle lower boundary

For every `(a,b) in F_xz`, the metric triangle inequality gives

\[
\boxed{a+b\ge\rho(x,z).}
\]

Let `n=rho(x,z)`. The endpoint choices `y=x` and `y=z` give costs

\[
(0,n),\qquad(n,0).
\]

Both are Pareto-minimal. Therefore every frontier contains its two endpoint costs, while any internal point records a genuinely useful represented intermediate state.

Define the exact anti-diagonal

\[
G_n=\{(k,n-k):0\le k\le n\}.
\]

## 5. B16 — geodesic/split-complete frontier theorem

For a fixed endpoint pair `x,z` with `n=rho(x,z)`, the following are equivalent:

1. every integer budget split of the exact total distance is realizable;
2. every `k=0,...,n` has a represented state `y_k` with
   \[
   \rho(x,y_k)=k,
   \qquad
   \rho(y_k,z)=n-k;
   \]
3. the staged Pareto frontier is exactly
   \[
   \boxed{F_{xz}=G_n.}
   \]

If this holds for every endpoint pair, it is equivalent to the global split-completeness/geodesic condition B08.

### Why no extra Pareto points survive in the geodesic case

Suppose `(a,b)` is any intermediate cost. Triangle inequality gives `a+b>=n`. Choose integer

\[
k\in[\max(0,n-b),\min(a,n)].
\]

In a geodesic pair, `(k,n-k)` is represented and satisfies

\[
(k,n-k)\preceq(a,b).
\]

Hence every cost above the anti-diagonal is dominated; the only Pareto-minimal costs are the exact geodesic splits.

## 6. Stage-05 defect language

The frontier exposes more structure than the scalar geodesic defect `Gamma`.

### Missing exact splits

Define

\[
\boxed{M_{xz}=G_{\rho(x,z)}\setminus F_{xz}.}
\]

`M_xz` records exactly which zero-slack budget splits lack a represented intermediate witness.

### Detour frontier points

Any frontier point with

\[
a+b>\rho(x,z)
\]

is a nondominated **detour witness**: it helps some staged queries, but only with positive total slack.

Thus `F_xz` distinguishes:

- exact geodesic interpolation;
- missing exact splits;
- useful but slack-consuming detours.

`Gamma` answers the global unit-path question; `F_xz` answers every two-stage budget query.

## 7. Examples

### `{0,1,2}`

For endpoints `0,2`, `rho=2` and the three represented intermediate choices produce

\[
F_{0,2}=\{(0,2),(1,1),(2,0)\}=G_2.
\]

### `{0,2}`

Only endpoint witnesses exist:

\[
F_{0,2}=\{(0,2),(2,0)\}.
\]

The missing split set is

\[
M_{0,2}=\{(1,1)\}.
\]

### Connected but non-geodesic example

Take equal capacity `10` with totals `(0,7,14,20)`, corresponding to normalized positions `0,0.7,1.4,2` but represented and computed entirely by integers.

For endpoints `0,2`, direct integer relation distance is `rho=2`, while the radius-one graph path uses three edges. The two internal intermediates have costs `(1,2)` and `(2,1)`, each dominated by an endpoint cost. Hence

\[
F_{0,2}=\{(0,2),(2,0)\},
\]

so the exact `(1,1)` split is missing even though the unit graph remains connected.

This distinguishes finite detour from complete disconnection.

## 8. Cross-route consequences

### A2 / P023

This is a concrete task-minimal repair hierarchy. The canonical state for all two-stage support budgets is not necessarily the full witness set; it is the Pareto frontier of witness costs. A proposed coarser encoding is legitimate exactly when it preserves that frontier/truth function on every quotient fiber.

### A4

Common-target composition acquires a compact exact budget signature in the A3-generated metric subclass.

### A5 / P022

Geometry-specific holes can now be classified by their missing anti-diagonal splits and detour frontiers, not only by graph connectivity or shell counts.

### A3

The bridge separates three progressively richer observables:

\[
\rho
\quad\to\quad
(d^-,d^+)
\quad\to\quad
F_{xz}.
\]

Each is sufficient for a different declared future language.

## 9. Prior-art discipline

Pareto frontiers, upward-closed subsets of `N^2`, multiobjective shortest-path costs, and antichain representations are established prior art. No novelty claim is made for those general tools.

The project-specific contribution under test is the exact derivation of this antichain repair coordinate from the A3-generated A4 support family and its placement in P023's task-relative legal-collapse hierarchy.

## 10. Executable reference

A new reference module computes:

- Pareto-minimal budget antichains;
- `F_xz` for every endpoint pair;
- exact staged query answers from the frontier;
- missing exact splits `M_xz`;
- the geodesic anti-diagonal criterion.
