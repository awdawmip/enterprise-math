# R022 BRC Semantic Model

**Task:** RS-R022-HASHCLASH-BRC-TOOL-MINING  
**Researcher:** EM-R022-HC7B4A  
**Status:** RESEARCH MODEL / NOT CANONICAL

This file isolates the generic, non-cryptographic semantics transferred from the R022 source study.

---

# 1. Base finite-state model

Let:

- `X_t` be the fine states at stage `t`;
- `U_t` be the declared residual future language from stage `t`;
- `o : X_final -> Y` be the final observable;
- `R_u(x)` be the set of fine final states reachable from `x` under residual future `u`.

Default R022 semantics is **final result-support**:

`Supp_t(x,u) = { o(y) : y in R_u(x) }`.

For a branch denotation `C subset X_t`:

`Supp_t(C,u) = union_{x in C} Supp_t(x,u)`.

Multiplicity, provenance, optimization score and path count are not included unless explicitly added to `o` or the semantic mode.

---

# 2. Residual future equivalence

Define:

`x ==_{U_t} y`

iff

`Supp_t(x,u) = Supp_t(y,u)` for every `u in U_t`.

This is the semantic reference relation for exact token-identification.

The coarsest unrestricted deterministic token for the declared residual semantics is the quotient:

`X_t / ==_{U_t}`.

This does not imply that every useful runtime representation must be deterministic or globally materialized.

---

# 3. Branch carrier

A generic R022 branch token is:

`b = (t, kappa, sigma, mode)`

where:

- `t` = stage;
- `kappa` = fixed external context;
- `sigma` = retained branch/residual signature;
- `mode` = denotation semantics.

A representation map gives:

`Denote(b) subset X_t`.

Critical accounting rule:

The cost of `kappa` must be charged somewhere. A small `sigma` is not a small branch state if a large hidden context is required to interpret it.

---

# 4. Split

For operation `a`, a branch splits when one current token cannot represent all exact successors without losing declared support.

Abstractly:

`Split_a(b) = {b_1, ..., b_k}`

must satisfy

`Supp_{t+1}(union_i Denote(b_i), u)
 = Supp_{t+1}(R_a(Denote(b)), u)`

for every allowed residual suffix `u`.

Minimal split width is relative to:

- declared semantics;
- residual horizon/language;
- allowed token representation class.

---

# 5. Exact union versus token identification

These must not be conflated.

## 5.1 Exact union

If the runtime keeps the exact denotation:

`C = C_1 union C_2`

then support semantics may distribute over the union without requiring `C_1` and `C_2` to have equal futures.

This operation may not compress representation.

## 5.2 Token identification

If the runtime replaces multiple histories/states by one abstract token and forgets distinctions, then it needs a congruence certificate.

This is the true BRC recoalescence operation.

---

# 6. Recoalescence Congruence Certificate (RCC)

Certificate shape:

`RCC(t, kappa, semantics, U_t, sig, proof)`

Sufficient support-exact contract:

For every fine states `x,y` represented by the merged token,

`sig(x) = sig(y)`

implies

`Supp_t(x,u) = Supp_t(y,u)`

for every `u in U_t`.

Then histories sharing `sig` may forget their past and continue under one token.

A local transition-congruence proof can replace explicit enumeration when it implies the same property inductively.

## Semantic strengthening

If the observable includes multiplicity, provenance, or score, equality of plain result support is insufficient. The certificate must preserve the stronger observable.

---

# 7. Context-relative RCC

A signature may be sufficient only under fixed context.

Write:

`sig_kappa(x)`.

Then the certificate is valid only while `kappa` remains unchanged.

HashClash's six-word `connect_bitdata` is interpreted this way:

- residual token = six 32-bit fields;
- context = fixed lower path, upper path, stage, message differences, current bit position.

This is a source-backed example of **conditional residual compression**.

---

# 8. No-Completion Cone Certificate (NCC)

Certificate shape:

`NCC(t, kappa, failure_depth, prefix_sig, dependency_mask, proof)`.

Contract:

For every fine state/branch `x` matching the certified residual-prefix signature under context `kappa`,

`Supp_t(x,u) = empty`

for every allowed residual completion `u` in the certified suffix language.

Then every matching branch may be pruned.

This is the negative dual of RCC:

- RCC: equal nonempty/possibly nonempty futures may share a token;
- NCC: a whole signature class has empty future and may disappear.

HashClash's failure-prefix skip in `md5connect` is the source witness motivating NCC.

---

# 9. Branch Signature Router (BSR)

Let continuation implementations be `{A_a}`.

Define correctness domain:

`D_a = {x : A_a is correct on x for the declared semantics}`.

A router is:

- `sigma : X -> Z`;
- `alpha : Z -> A`.

Correctness iff:

`for every z, sigma^{-1}(z) subset D_{alpha(z)}`.

## BSR Cover Theorem

When cost is the number of distinct selected algorithms/labels, minimum BSR label count equals the minimum number of correctness domains `{D_a}` whose union covers `X`.

Consequences:

1. solver-routing minimality can differ from semantic future-equivalence;
2. overlapping solver domains can produce nonunique minimal routers;
3. a “minimal signature” claim must name the allowed encoding family.

## Representation classes

At least distinguish:

- raw coordinate subset;
- arbitrary compiled label;
- algebraic/compressed encoding.

md5collgen synthetic result:

- 9 physical route-relevant bits all necessary as raw coordinates;
- five compiled continuation labels;
- three fixed-width control bits;
- full IV payload still retained.

---

# 10. BRC-Connect

At interface stage `t`:

- `F_t` = forward branch cone;
- `B_t` = backward branch cone.

An interface map `I_t` is exact when it preserves the declared completion relation.

A generic connector:

`Connect_t(f,b)`

may return support only if the interface relation proves a legal full continuation exists.

Endpoint equality is not generally sufficient.

## Coarsest exact connection interface

Define two interface-side states equivalent when they induce the same completion support against every admissible opposite-side context.

The quotient of this relation is the semantic lower bound for unrestricted exact connection tokens.

Actual source encodings may refine this quotient.

---

# 11. Branch-local safe operations

A partial operation:

`n : D -> X`

is branch-local safe under signature `sig` when, for its legal domain,

`sig(n(x)) = sig(x)`

or when it maps to a known RCC-equivalent target token.

The legal domain is part of the operation type.

## Algebra

Safe partial operations do not generally form a monoid because composition may be undefined.

Appropriate default structure:

**partial transformation category / semigroupoid with domain guards.**

Closure into a monoid/group requires extra hypotheses.

---

# 12. Exact-BRC no-rewind principle

If:

1. an RCC was exact for the declared residual language;
2. semantics/context do not change;
3. no additional heuristic pruning loses support;

then a later support failure cannot be repaired merely by separating histories that were merged under that RCC.

Therefore semantic rewind is evidence of one of:

- inexact/budgeted earlier collapse;
- changed future language/context;
- stronger later observable;
- independent heuristic pruning.

---

# 13. Causal refinement depth

For a failed inexact/budgeted run with checkpoints:

`C_0, C_1, ..., C_k`,

define the **latest recoverable checkpoint** as the greatest `j < k` for which a collapsed class at `j` contained representatives with different residual feasibility and replaying a discarded feasible representative can recover a valid final result.

Define:

`causal_refinement_depth = k - j`.

This is a BRC diagnostic, not a claim of novelty over CEGAR/backjumping.

---

# 14. Recoalescence defect

For finite residual language:

`Delta_U(b1,b2)
 = {u in U : Supp(b1,u) != Supp(b2,u)}`.

Then:

`|Delta_U| = 0`

iff the branches are support-future-equivalent.

This is an exact diagnostic.

It is not generally a useful monotone scheduling potential:

- computing it may be as hard as future-equivalence itself;
- arbitrary branch-local operations need not decrease it;
- coarse geometric/state-space distance can move in the opposite direction.

R022 therefore rejects a generic scalar Recoalescence Potential Scheduler.

---

# 15. Resource model

For a BRC execution charge at least:

- `S_static` — static tables/compiled representation;
- `W_peak` — peak live branch width;
- `N_live` — cumulative live branch count;
- `B_token` — branch-token bits;
- `B_context` — retained external context bits/storage;
- `Work` — total transition/search work;
- `JoinWork` — connector work;
- `ReplayWork` — rewind/re-execution;
- `Depth` — serial/critical execution depth;
- `Precompute` — precomputation/minimization cost.

A valid Pareto comparison cannot omit hidden branch metadata.

---

# 16. Bidirectional width objective

For split stage `t` and exact interface `I_t`, R022 recommends R021 expose:

- `W_F(t)`;
- `W_B(t)`;
- `B_I(t)`;
- `JoinWork(t)`;
- `Depth(t)`.

Generic optimization:

`min_{t,I_t exact}
  Objective(W_F, W_B, B_I, JoinWork, Depth, Replay)`.

This extends one-directional minimal branch width without claiming novelty over meet-in-the-middle.

---

# 17. Compiler primitive contracts

## `branch_signature_router`

Input:
finite states, continuation correctness domains, encoding family.

Output:
correct signature, selector, minimality/deletion witnesses, token/payload accounting.

## `brc_connect`

Input:
forward cone, backward cone, exact interface declaration.

Output:
completion support, interface certificate, join cost.

## `recoalescence_certificate`

Input:
candidate token class, residual language, semantics.

Output:
RCC or counterexample future.

## `no_completion_cone_certificate`

Input:
candidate residual-prefix class.

Output:
NCC or surviving completion witness.

## `safe_neutral_moves`

Input:
branch invariant, partial moves.

Output:
safe legal domains and composability relation.

## `brc_refine_backtrack`

Input:
failed inexact/budgeted checkpoint trace.

Output:
latest recoverable checkpoint, distinction, causal refinement depth.

## `future_signature_defect`

Input:
two tokens, finite residual language.

Output:
exact discrepancy set/count.

## `branch_budget_optimizer`

Input:
exact candidate strategies plus fully charged resource metrics.

Output:
Pareto frontier / selected policy.

---

# 18. Generic kill conditions

Any proposed BRC tool is rejected if:

1. it secretly retains full fine state while claiming a tiny token;
2. it merges by current output/endpoints without residual congruence;
3. it requires provenance/multiplicity later but discarded them;
4. its local safe moves are composed outside legal domains;
5. its rewind policy cannot recover a feasible discarded world;
6. its distance heuristic is presented as exact without monotonicity proof;
7. its Pareto win disappears after token/context/join/replay metadata is charged;
8. its alleged novelty is only standard MITM/backtracking/CEGAR/NFA behavior renamed.

---

# 19. Source-to-model transfer boundary

The semantic model intentionally transfers only structure:

- md5collgen -> continuation-control routing;
- HashClash forward/backward -> branch cones;
- HashClash connector -> context-relative residual state;
- exact duplicate connector state -> RCC witness;
- failure-prefix skip -> NCC witness;
- tunnel-like freedom -> guarded partial safe moves;
- timeout rollback -> motivation for, but not proof of, causal refinement;
- path budgets -> branch-economics axes.

No cryptographic security claim, collision complexity theorem, or operational attack primitive is part of the generic model.

---

# 20. R022 semantic verdict

The source study supports a coherent BRC semantics based on:

`split + context-relative residual tokens + RCC positive merge + NCC negative prune + exact interface connect + guarded local moves + metadata-aware budgets`.

The semantics is useful for R021.

The generic algorithmic ingredients are predominantly established ideas; the Enterprise Math contribution is the exact collapse/certificate interface and the discipline preventing semantic or metadata cheating.
