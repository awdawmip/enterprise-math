# R022 to R021 Feedback — Branch-Recoalescence Collapse Tool Mining

**From:** EM-R022-HC7B4A / RS-R022-HASHCLASH-BRC-TOOL-MINING  
**To:** R021 Branching Collapse Tool Calculus  
**Status:** RESEARCH FEEDBACK / NOT CANONICAL  
**R022 taskbook:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`

## Executive recommendation

R022 recommends that R021 keep the Branch-Recoalescence Collapse program, but sharpen it around **typed residual certificates** rather than around the visual metaphor of many branches.

The first two passes established a dual certificate calculus:

- **RCC — Recoalescence Congruence Certificate:** positive certificate that histories may forget their past and share one residual future token.
- **CS-NCC — Context-Scoped No-Completion Cone Certificate:** negative certificate that a dependency-footprint class has empty completion support and may be pruned while the certificate scope remains valid.

The third pass unifies both under a more general support-semantic object:

- **RJC — Residual Join Certificate:** an exact rewrite of a live branch configuration into another configuration with the same pointwise join of residual future-support signatures.

This exposes a new primitive — **collective residual dominance** — and a hard negative boundary: minimum exact residual-basis optimization contains SET COVER.

At the same time, R022 found no reason to claim that BRC is a new generic search algorithm or a new algebra. The external structures substantially root to standard automata, dynamic programming/state memoization, meet-in-the-middle, nogood pruning, backtracking, CEGAR, powerset/join semantics and Set Cover.

---

## 1. Which R021 branch carrier best matches md5collgen?

**Answer: branch-token refinement over a retained fine payload.**

md5collgen's dispatcher computes a small continuation-control label from a larger IV and then passes the IV into the selected specialized solver.

So the correct carrier is not `small token replaces fine state`; it is

`(retained continuation payload, small branch-control token)`.

R021 should distinguish control signature bits, payload/context bits, and denotation/support metadata in branch-storage accounting.

The source-shaped finite model found 9 route-relevant physical IV bits; all 9 are necessary if the signature must be a raw-coordinate subset; 5 compiled route labels fit in 3 fixed-width bits.

---

## 2. Which carrier best matches HashClash path populations?

**Answer: constraint-cell/support branching with context-relative residual tokens.**

Forward/backward `differentialpath` objects are partial constraint paths, not literal concrete fine states.

At the connector, the carrier becomes `six-word residual connect token + fixed lower/upper connection context`.

Therefore R021 should use a first-class **context-relative residual branch carrier** and charge the context somewhere in the representation budget.

---

## 3. What is genuine safe recoalescence versus only search convergence?

HashClash `md5_connect_bits` expands connector states one bit at a time and then sorts/removes exact duplicate six-word residual states. Under the same lower/upper path and connection context, duplicate residual states have the same remaining connector feasibility behavior.

That is a source-backed local RCC for final-support/existence semantics.

Same current endpoint, same coarse output, same distance, or same score are not automatically safe merge certificates.

R021 should keep exact union bookkeeping distinct from token identification/forgetting.

---

## 4. CS-NCC must carry a dependency footprint and invalidation rule

The second-pass audit sharpened the original NCC.

HashClash does not reuse a failed lower-path prefix as a permanent context-free nogood. `isgood` reuse depends on how much of the upper path remains equal (`bequal`) and on the relevant masked residual prefixes; cached failure is invalidated when those dependencies change.

Recommended certificate:

`CSNCC(stage, failure_depth, dependency_footprint, semantics, proof_of_empty_completion)`.

A cached certificate may be reused only when the candidate/context has the same sufficient dependency footprint.

Synthetic kill test: changing one context component at the failure depth turns a previously failing branch into a successful one, so context-free failure reuse is unsound.

---

## 5. Branch budget requires exactness typing

HashClash `ubound/maxcond`, tunnel/best-path ranking, timeout kills and fixed `k -> max(k-1,0)` rollback are useful search engineering, not exact support transformations by themselves.

R021 should type every budget action as:

- `EXACT` — every removed branch has an exact certificate;
- `REPLAY_EXACT` — evicted distinctions are recoverable from charged checkpoints/replay descriptions;
- `HEURISTIC` — rank/score/width/time pruning may lose support and exactness is not claimed.

An uncertified width-cap kill test changes final support from `{0,1}` to `{0}`.

---

## 6. Third-pass unification: Residual Join Certificate (RJC)

Fix scope

`omega = (stage, context, residual language, observable, semantics=SUPPORT)`.

For branch `b`, let

`phi_omega(b) : U -> P(Y)`

be its complete residual final-support signature.

For live configuration `C`, define

`J_omega(C) = vee_{b in C} phi_omega(b)`

using pointwise union.

An **RJC** for `C => D` proves

`J_omega(C) = J_omega(D)`.

Then:

- RCC is idempotence: equal signatures satisfy `x vee x = x`;
- CS-NCC is bottom elimination: `x vee bottom = x`;
- pairwise dominance is absorption: `x <= y => x vee y = y`;
- new **collective dominance** allows `b` to be removed when `phi(b)` is covered by the join of several survivors even if no single survivor dominates it.

This is standard join-semilattice semantics, not a new algebraic theorem. Its value is a single exact BRC rewrite contract.

---

## 7. Collective dominance kills pairwise-antichain completeness

One residual future, supports:

- `A={1,2}`
- `B={1,3}`
- `C={2,3}`.

All three are pairwise incomparable, so pairwise dominance removes nothing.

Nevertheless every branch is covered by the union of the other two, and any two branches preserve the total support `{1,2,3}`.

Therefore `pairwise dominance complete = false`.

A maximal antichain of residual signatures can still contain exact collective redundancy.

---

## 8. Residual Join Basis and the 0/1/many-world normal form

Fix an admissible token dictionary `D`.

For target residual element `z`, define

`nu_D(z) = min |S|`

such that `S subseteq D` and the join of `S` equals `z`.

A minimizing `S` is a **Residual Join Basis (RJB)**.

Then:

- `nu_D(z)=0` exactly for empty/bottom residual support;
- `nu_D(z)=1` when one admissible token represents the entire target residual join;
- `nu_D(z)>1` when genuinely multiple admissible residual worlds are required.

This gives R021 a local exact branch-width quantity, but it is explicitly dictionary-relative.

If arbitrary exact union tokens are synthesized for free, width trivially becomes one; token denotation/construction cost must therefore be charged.

---

## 9. Exact minimum residual basis contains SET COVER

Reduction from SET COVER:

- use a singleton residual language;
- use the Set-Cover universe as final output atoms;
- create one admissible branch token per input subset;
- let each branch residual support equal that subset.

Then a subconfiguration preserves the total residual join iff its corresponding subsets cover the target universe.

Therefore minimum exact existing-token branch-basis optimization is Set Cover in this finite explicit-signature model.

Consequences:

- generic minimum exact branch-basis optimization is NP-hard;
- decision form is NP-complete in the explicit finite model;
- weighted token costs yield weighted-cover variants;
- universal polynomial `branch_budget_optimizer` claims should be rejected absent additional structure.

This is a direct complexity boundary for R021's minimal-width problem.

---

## 10. Local irredundance is not global optimality

A six-token pairwise-incomparable synthetic family has exact irredundant bases of widths 3 and 4.

A local reducer that removes one currently redundant branch at a time can terminate at width 4 even though width 3 is achievable.

Therefore `locally irredundant = globally minimum` is false, and exact pruning order can affect the terminal representation.

---

## 11. Certificate validity is future-language relative

An RJC valid for future language `U` remains valid after restriction to `U' subseteq U`.

The reverse fails: two branches can agree on the current short language and differ when a new future operation/word is added.

Therefore RJC/RJB caches need a residual-language or language-version scope just as CS-NCC caches need a context/dependency scope.

---

## 12. Duplicate recoalescence requires idempotent semantics

Two duplicate support branches can be merged exactly for Boolean support because union is idempotent.

The same merge changes path multiplicity from 2 to 1.

Therefore duplicate branch identification is not semantics-neutral.

R023's Boolean/result-support Lean carrier should remain scoped as-is; multiplicity/provenance require weighted/tagged carriers rather than importing RCC unchanged.

---

## 13. Recommended R021 compiler architecture

### Cheap exact normalization

1. RCC hash-cons equal signatures;
2. CS-NCC remove certified bottom cones;
3. pairwise dominance removal;
4. context/language-scoped certificate cache reuse with invalidation.

### Bounded collective normalization

5. collective-dominance search;
6. bounded exact RJB optimization by exhaustive/ILP/SAT-style search with proof/certificate.

### Resource fallback

7. `REPLAY_EXACT` checkpoint eviction if live width must be reduced without losing semantics;
8. otherwise `HEURISTIC` mode with exactness claim disabled.

Candidate tool name: `residual_join_normalizer`.

---

## Final R021 handoff

**Most valuable third-pass addition:** RCC + CS-NCC + dominance are all low-cost cases of a **Residual Join Certificate**, while exact 0/1/many-world normalization is the dictionary-relative **Residual Join Basis** problem, generically Set-Cover hard.

**Recommended sharpened R022 classification:**

`BRC_RESIDUAL_CERTIFICATE_ALGEBRA_FOUND / RCC_NCC_UNIFIED_AS_JOIN_REWRITES / COLLECTIVE_DOMINANCE_FOUND / EXACT_BRANCH_BASIS_SET_COVER_HARD / SUPPORT_IDEMPOTENCE_BOUNDARY_CLASSIFIED / R021_FEEDBACK_READY / NOT_CANONICAL`
