# A3 ↔ A4 Bridge — Current Research State

Status: `ACTIVE RESEARCH CHECKPOINT / DO NOT PROMOTE AS FOUNDATION YET`  
Scope: resume map for the A3 relation-state ↔ A4 support/correspondence ↔ A2/P023 quotient-safety bridge

## 1. Ownership and branches

- A3 owner: `research/core/relation-quotient`.
- A4 owner: `research/core/admissible-support-relations`.
- Bridge owner: `research/core/relation-support-bridge` / Draft PR #83.
- General quotient-safety mother theorems: A2/P023 (`research/p023-composition-safe-collapse`).
- Cross-branch coordination: Research Relay Issue #82.

The bridge is a consumer of A3 and A4, not a replacement for either. It must not absorb A3 partition algebra, A4 arbitrary correspondence theory, or P023 general factorization merely because a specialization is useful here.

## 2. Current bridge theorem chain

### B01–B03 — generator and quotient boundary

From a closed A3 weighted state

`Z_ij=m_j*c_i-m_i*c_j`,

first quotient by `Z_ij=0`, then define

`x R_r y iff |Z_ij| <= r*m_i*m_j`.

This generates a restricted A4 admissible-support family. Universal fine support descends to coarse support under A3 partition aggregation, but the converse fails by signed cancellation.

### B04–B06 — interpolation

A4 split-completeness becomes existence of represented intermediate states. Consecutive unit states are split-complete; `{0,2}` fails the `1+1` split.

### B07–B09 — integer metric and geodesic defect

The generated support family is exactly the radius filtration of

`rho(x,y)=ceil(|Z_ij|/(m_i*m_j))`.

Global split-completeness is equivalent to `rho` being the intrinsic shortest-path metric of its radius-one graph. `Gamma=d_G1-rho` (infinity if disconnected) is the interpolation/geodesic defect.

### B10–B12 — endpoint MAY/MUST precision

For coarse blocks `A,B`:

- `d^- = min rho` is the all-radius MAY threshold;
- `d^+ = max rho` is the all-radius MUST threshold;
- `(d^-,d^+)` is the task-minimal combined endpoint coordinate up to finite re-encoding.

The direct A3 aggregate threshold `bar rho` is a different observable: `bar rho<=d^+`, but there is no universal order relation with `d^-`.

### B13–B20 — staged/two-stage Pareto state

For endpoints `x,z`, every intermediate `y` has cost `(rho(x,y),rho(y,z))`. The Pareto-minimal antichain `F_xz` exactly represents all two-stage budget existence queries.

For coarse blocks:

- `F^-` is the exact staged-MAY frontier;
- `F^+` is the exact staged-MUST frontier.

One-step thresholds do not determine staged semantics.

### B21–B23 — arbitrary future depth

At depth `k`, the exact existence state is the Pareto frontier `F^(k)` of represented chain-cost vectors in `N^k`.

If the support metric is geodesic/split-complete, then for every finite depth

`R_r1 ; ... ; R_rk = R_(r1+...+rk)`

and `F^(k)` is the weak-composition simplex of the endpoint distance. Hence geodesicity is a finite-future existence-compression certificate.

### B24–B27 — exact support-language quotient

The labeled integer metric state `(X0,rho)` determines every generated primitive support relation and every finite support word. The complete primitive support family also recovers `rho`.

Therefore `(m,c,Z)->(X0,rho)` is future-safe for the generated support language.

It is not future-safe for richer A3 partition aggregation: explicit same-metric A3 states can yield different aggregate coarse thresholds.

### B28–B31 — online antichain compression

Existence frontiers compose by exact antichain convolution. Dominated prefix costs can be erased permanently for future existence/budget queries because concatenation preserves dominance.

This compression is not witness-count complete.

### B32–B40 — count-complete coefficient layer

Two-stage exact cost histogram `H(a,b)` is information-equivalent to all budgeted witness counts by integer prefix sums and finite-difference inversion. Natural-number support-matrix products count common targets; boolean support gives existence.

At arbitrary depth, count tensors `H^(k)` compose by non-negative-integer coefficient convolution. Their positive support, followed by Pareto pruning, gives the existence frontier `F^(k)`.

Even when geodesicity collapses all finite-depth existence semantics to endpoint `rho`, witness multiplicity can remain different. Count-sensitive languages therefore require richer state.

## 3. Current semantic state ladder

The current bridge does **not** define one universal precision scalar. It defines a language-indexed state ladder:

`A3 exact relation state (m,c,Z)`

→ `(X0,rho)` for the complete generated-support algebra

→ `H^(k)` / coefficient polynomial for fixed-depth witness-count semantics

→ `F^(k)` Pareto antichain for fixed-depth existence semantics

→ selected threshold(s) or truth bit for narrower declared queries.

A legal arrow is justified only by a theorem that the discarded information cannot affect the declared future language.

## 4. Independent selector axis from current A3 work

A3 has concurrently developed the guard-image lattice

`L_G=W(K_A)`

for hidden piecewise selectors. It is a different hidden-information object from support metric/frontier state.

- rank zero: guard visible/descends;
- full rank: every strict orthant is reachable;
- rank one: exact reachable patterns reduce to one integer interval;
- arbitrary refinement can move `exact -> non-exact -> exact` because branch effects may become visible before the selector does.

Therefore “more precision” is not a semantic order by itself. Support-state and selector-state should only be combined by a declared product/interaction language and a new factorization proof.

## 5. Verification state

Ordinary finite/integer proofs are written in Supplements 01–10.

Reference implementations and regression tests are present for:

- A3-generated support and partition cancellation;
- integer metric/geodesic defect;
- MAY/MUST threshold profiles;
- two-stage and coarse staged Pareto frontiers;
- arbitrary-depth existence frontiers;
- support-language metric quotient;
- recursive antichain convolution;
- two-stage and arbitrary-depth witness-count coefficient state.

Independent in-session bounded reconstruction found no mismatch in:

- 111,132 small weighted states for geodesic/split-completeness equivalence;
- 62,192 coarse profiles for staged MAY/MUST frontier semantics;
- 14,016 state-depth cases for recursive antichain and count convolution against direct path enumeration;
- 4,672 weighted states for histogram/prefix-count inversion.

These checks support but do not replace repository CI. Direct checkout-based pytest is not claimed in this research session because the local execution environment previously failed GitHub DNS resolution.

## 6. Research Relay state

Key bridge results through B40 have been posted to Issue #82 and targeted downstream to P023, P018, A4/E001 and P022 where relevant.

Current rule for continuing this branch:

1. read new Relay entries before introducing another general abstraction;
2. inspect the current A3/A4/P023 heads before every substantial stage;
3. if a mother theorem already exists downstream/upstream, add only the specialization/corollary here;
4. relay positive and negative boundaries with equal priority.

## 7. Current branch-integration state

The A3 base has advanced while the bridge was active. Current A3 additions include piecewise-affine quotient and guard-image-lattice work. The bridge bilingual manifest has been semantically updated to include those dependency pairs, but PR #83 may still require a clean dependency sync/replay before it becomes mergeable.

Do not force-merge or overwrite A3. Preserve A3 ownership and replay only bridge-owned files if a clean restack becomes necessary.

## 8. Next research questions

Highest-value next questions are:

1. **Count-aware online compression:** find the smallest recursive coefficient state for selected multiplicity languages; determine when coefficient distributions themselves admit safe pruning/aggregation.
2. **Identity layer:** characterize exactly when witness labels can be erased while counts remain future-complete, connecting A4/E001 and P021 witness-transport results.
3. **Support × selector product language:** combine `(X0,rho)` with A3 guard-image state only under an explicit mixed operation algebra; determine the coarsest compatible product quotient.
4. **P023 extraction:** isolate which B-results are merely worked specializations of P023 and which bridge-specific arithmetic/metric statements remain here.
5. **A5/P022 specialization:** test `Gamma`, missing exact splits and frontier complexity on actual intrinsic lattice/root-lattice geometries.
6. **Prior-art audit:** before any numbered-problem or Foundations promotion, audit metric quotient, antichain dynamic programming, abstract interpretation MAY/MUST, multiobjective path algebra, incidence/count semirings, and automata/congruence literature.

## 9. Promotion boundary

Do not assign a new `P` number or promote this bridge into `FOUNDATIONS` yet.

A future promotion should require:

- clean replay on current main/A3 dependencies;
- repository CI;
- prior-art/novelty boundary;
- stable separation of A3, A4 and A2 ownership;
- evidence that the integrated state-ladder principle adds durable project value beyond a collection of standard tools.
