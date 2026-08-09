# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 05

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact coarse-partition MAY/MUST coordinates for the full two-stage budget language

## 1. Setup

Stage 05 associates to every fine endpoint pair `x,z` a finite Pareto frontier

\[
F_{xz}\subset\mathbb N^2
\]

whose upward closure is exactly the truth region of

\[
(x,z)\in R_r;R_s.
\]

Let `P={A,B,...}` be a partition of the A3 zero-relation quotient `X0`.

For coarse blocks `A,B`, define the staged modalities:

- `MAY_(r,s)(A,B)`: at least one fine endpoint pair `x in A, z in B` has a two-stage witness within budgets `(r,s)`;
- `MUST_(r,s)(A,B)`: every fine endpoint pair `x in A, z in B` has some (pair-dependent) intermediate witness within the same budgets `(r,s)`.

The intermediate witness used for MUST may differ across endpoint pairs. The query asks whether the budget works uniformly, not whether one common `y` works for all endpoints.

## 2. Frontier algebra for upward-closed budget sets

For a finite frontier `F`, write

\[
\uparrow F
=
\{(r,s):\exists(a,b)\in F,\ a\le r,\ b\le s\}.
\]

### Union

For finitely many frontiers `F_i`,

\[
\bigcup_i\uparrow F_i
=
\uparrow\operatorname{ParetoMin}\left(\bigcup_iF_i\right).
\]

### Intersection

For two frontiers `F,G`, define coordinatewise join

\[
(a,b)\vee(c,d)=(\max(a,c),\max(b,d)).
\]

Then

\[
\boxed{
(\uparrow F)\cap(\uparrow G)
=
\uparrow\operatorname{ParetoMin}\{p\vee q:p\in F,q\in G\}.
}
\]

Proof: a budget dominates some `p in F` and some `q in G` iff it dominates `p vee q`. Iterating this identity gives the exact finite intersection frontier for any finite family.

## 3. B17 — coarse staged MAY frontier

Define

\[
\boxed{
F^-_{AB}
=
\operatorname{ParetoMin}
\bigcup_{x\in A,z\in B}F_{xz}.
}
\]

Then

\[
\boxed{
MAY_{(r,s)}(A,B)
\iff
\exists p\in F^-_{AB}:p\preceq(r,s).
}
\]

Thus `F^-` is the exact all-budget staged-MAY coordinate.

## 4. B18 — coarse staged MUST frontier

For every fine endpoint pair `(x,z) in A×B`, choose one frontier point

\[
p_{xz}\in F_{xz}.
\]

Take their coordinatewise join

\[
\bigvee_{x,z}p_{xz}
=
\left(
\max_{x,z}p^{(1)}_{xz},
\max_{x,z}p^{(2)}_{xz}
\right).
\]

Define

\[
\boxed{
F^+_{AB}
=
\operatorname{ParetoMin}
\left\{
\bigvee_{x\in A,z\in B}p_{xz}
:
p_{xz}\in F_{xz}
\right\}.
}
\]

Then

\[
\boxed{
MUST_{(r,s)}(A,B)
\iff
\exists p\in F^+_{AB}:p\preceq(r,s).
}
\]

So `F^+` is the exact all-budget staged-MUST coordinate.

The direct construction may be combinatorially expensive. It is a reference specification, not yet an optimized algorithm. Pairwise frontier intersection can be applied incrementally and pruned after every step.

## 5. B19 — P023 task-minimality

The complete MAY truth function on `N^2` uniquely determines `F^-_AB` as its set of coordinatewise-minimal true budgets. Likewise the complete MUST truth function uniquely determines `F^+_AB`.

Therefore, up to finite re-encoding,

\[
\boxed{F^-_{AB}}
\]

is the P023 coarsest repair coordinate for the full staged-MAY budget language, and

\[
\boxed{F^+_{AB}}
\]

is the corresponding coarsest coordinate for staged-MUST.

For the combined modality, retain the pair `(F^-_AB,F^+_AB)`.

This is the exact two-dimensional analogue of Stage 04:

\[
d^-_{AB},d^+_{AB}
\quad\longrightarrow\quad
F^-_{AB},F^+_{AB}.
\]

## 6. MUST implies MAY, but the frontiers need not coincide

For every budget pair,

\[
MUST_{(r,s)}(A,B)\Longrightarrow MAY_{(r,s)}(A,B),
\]

so

\[
\uparrow F^+_{AB}\subseteq\uparrow F^-_{AB}.
\]

This does not require a one-to-one pairing between their frontier points.

The gap between the two upward-closed regions is the staged analogue of the Stage-04 uncertainty interval: budgets in that gap support some fine endpoint pairs but not all of them.

## 7. Example: coarse block `{0,1}` against `{2}`

Use unit states `{0,1,2}` with the geodesic metric.

Fine endpoint frontiers are

\[
F_{0,2}=\{(0,2),(1,1),(2,0)\},
\]

\[
F_{1,2}=\{(0,1),(1,0)\}.
\]

For coarse blocks

\[
A=\{0,1\},\qquad B=\{2\},
\]

MAY is controlled by the easier fine pair:

\[
\boxed{F^-_{AB}=\{(0,1),(1,0)\}.}
\]

MUST must work for both endpoint pairs, hence

\[
\boxed{F^+_{AB}=\{(0,2),(1,1),(2,0)\}.}
\]

This is the staged counterpart of one-step thresholds `d^-=1`, `d^+=2`.

## 8. B20 — one-step endpoint thresholds cannot determine staged semantics

Take two systems whose declared endpoints have the same direct distance `rho=2`:

1. represented states `{0,1,2}`;
2. represented states `{0,2}`.

For singleton coarse endpoint blocks in both systems,

\[
d^-=d^+=2.
\]

So every one-step all-radius MAY/MUST query is identical.

But their two-stage frontiers differ:

\[
\{0,1,2\}:\quad F=\{(0,2),(1,1),(2,0)\},
\]

\[
\{0,2\}:\quad F=\{(0,2),(2,0)\}.
\]

Therefore

\[
\boxed{
(d^-,d^+)\text{ is not sufficient for staged/common-target semantics.}
}
\]

This is an information-separation theorem, not merely an example of a bad implementation.

## 9. Cross-route consequences

### A2/P023

The minimum repair depends on future-language depth. A quotient closed for endpoint queries may fail for staged queries even though every one-step threshold is preserved.

### P018

Precision cannot be ordered only by “number of stored coordinates”. Two summaries of similar size can support different future languages. Semantic closure is the gate.

### A4/E001

The staged MAY/MUST semantics of a coarse object pair has a canonical finite antichain representation in the A3-generated subclass.

### A5/P022

Geometry can compare not only direct distance but the complexity/shape of coarse staged frontiers, exposing different interpolation structure at the same endpoint distance.

## 10. Prior-art discipline

Antichain representation of upward-closed sets and union/intersection operations on Pareto frontiers are established techniques. The project-specific result is their exact placement as task-relative repair coordinates connecting A3, A4 and P023.

## 11. Executable reference

A new reference module implements:

- union of upward-closed frontiers;
- exact intersection via coordinatewise joins with Pareto pruning;
- coarse staged MAY frontier;
- coarse staged MUST frontier;
- exact query evaluation.
