# P018 Quotient-Root Atlas Ternary Carry — Driver-Accepted Formal Theorem Node

Status: `DRIVER_ACCEPTED_L4_FORMAL_THEOREM / LEAN_CHECKED / NO_FOUNDATION_MUTATION`

Date: `2026-08-28`

Node:

`P018_QUOTIENT_ROOT_ATLAS_TERNARY_CARRY_THEOREM`

Authority:

`driver_reviews/P018_TERNARY_CARRY_THRESHOLD_TO_CARDINALITY_DRIVER_REVIEW_20260827.md`

Immutable accepted result:

`RR-046FB92F6C42BB24A56C / DR-674A8EC67ED785D968FA`

Formal source:

`EnterpriseMath/Precision/RootStateAtlasCardinality.lean`

Formal source blob:

`e46d6037257d4f330d6cd46459beb0bc1a11ba5d`

## 1. Canonical research-theorem statement

Let `n>=1` and `r>=1`. For positive denominators `1<=d<=n`, define

`phi(d) = R_r(floor(n/d))`,

and let `S_r(n)` be the finite set of distinct values of `phi`.

Define the exact state-coalescence horizon and high-denominator cutoff

`H = R_(r+1)(r*n - 1)`,

`D = floor(n/(H+1)^r)`.

Then the denominator/root atlas has the following exact structure.

### A. High chart

For every `1<=d<=D`,

`phi(d) > H`,

and the map `d |-> phi(d)` is injective on `1,...,D`.

Hence the high chart contributes exactly `D` distinct root states.

### B. Low chart

For every `d>D`,

`phi(d) <= H`.

Every positive root

`1,2,...,H-1`

is realized by at least one denominator. The only optional low state is the horizon state `H` itself.

For `H>0`, the horizon state is realized exactly when

`(D+1)*H^r <= n`.

The formal proof treats `H=0` separately rather than silently applying the positive-horizon decomposition.

### C. Exact binary cardinality

Let

`kappa = 1` if `(D+1)*H^r <= n`, and `kappa = 0` otherwise.

Then, uniformly including the `H=0` boundary,

`|S_r(n)| + 1 = D + H + kappa`.

Equivalently, for `H>0`,

`|S_r(n)| = D + H - 1 + kappa`.

### D. Exact ternary carry normal form

Put

`q = floor(H/r)`,

`X = (H+1)^r`,

`Y = H^r`,

`A = max(q*X,(q+1)*Y)`,

`B = (q+1)*X`,

and define

`tau = 0` for `n<A`,

`tau = 1` for `A<=n<B`,

`tau = 2` for `B<=n`.

Then

`|S_r(n)| + 1 = H + q + tau`.

In the original Lean indexing `r=s+1`, these are exactly the theorems

- `EnterpriseMath.Precision.quotientRootStates_binary_cardinality`;
- `EnterpriseMath.Precision.quotientRootStates_ternary_cardinality`.

## 2. Structural mechanism

The proof is not a fitted count formula.

It factors the finite atlas into two disjoint charts:

1. a high-denominator chart with exact injectivity;
2. a contiguous forced low-root interval plus one optional horizon state.

The binary carry records whether that unique horizon state occurs. A separately proved three-point band for `D` then compresses the binary description into the monotone three-valued carry `tau`.

Thus the exact count is reduced from a denominator scan over `1,...,n` to one `(r+1)`-st integer root, a small number of exact divisions, and one or two threshold comparisons.

## 3. Binding guards

- This node concerns the finite positive-denominator quotient-root atlas `R_r(floor(n/d))` with `1<=d<=n`.
- It does not assert the same atlas structure for arbitrary monotone floor maps, arbitrary quotient semigroups, or real/continuum limits.
- The `H=0` case is part of the theorem but has separate structural handling.
- `kappa` and `tau` are state-count boundary carries. They are compatible with the Enterprise carry viewpoint but are not declarations that every T5 carry has this form.
- The explanatory asymptotic formulas in Python documentation are not promoted by this node as additional L4 Lean theorems.
- The finite `19,992`-case regression is evidence only; general validity is supplied by the Lean proof.
- No primality, factoring-speedup, Legendre, or prime-gap theorem follows from this node.
- No Foundation primitive or native geometry is modified.

## 4. Formal certificate

Original warning-fatal certification:

- Lean workflow `#888`;
- run `33038025114`;
- job `98405044303`;
- command `lake build --wfail -KCI EnterpriseMath`;
- conclusion `SUCCESS`.

Current-main semantic integration was independently revalidated by Lean workflow `#898`, whose warning-fatal compile step and workflow both concluded `SUCCESS` on the theorem-identical source blob.

Direct source audit found no `sorry`, `admit`, or custom axiom.

## 5. Reusable consequence surface

The theorem can safely be reused through the following exact consequences:

- high/low quotient-root atlas decomposition;
- injective high chart;
- forced contiguous low-root interval;
- unique optional horizon state;
- exact binary state-count formula;
- exact ternary threshold normal form.

The executable reusable interface is harvested separately as the domain operator

`domain.precision.quotient_root_atlas_carry`.
