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

## Core third-pass delta

Fix scope `omega = (stage, context, residual language, observable, semantics=SUPPORT)`. For branch `b`, let `phi_omega(b) : U -> P(Y)` be its complete residual final-support signature; for configuration `C`, let `J_omega(C)=vee_{b in C} phi_omega(b)`.

An **RJC** for `C => D` proves `J_omega(C)=J_omega(D)`.

Special cases:

- RCC = idempotence (`x vee x=x`);
- CS-NCC = bottom elimination (`x vee bottom=x`);
- pairwise dominance = absorption (`x<=y => x vee y=y`);
- **collective dominance** = a branch can be deleted when its signature is covered by the join of several survivors.

Minimal counterexample: `A={1,2}`, `B={1,3}`, `C={2,3}`. All are pairwise incomparable, yet any two preserve total support `{1,2,3}`. Therefore pairwise dominance/maximal-antichain pruning is incomplete.

Define the dictionary-relative **Residual Join Basis** width `nu_D(z)` as the minimum number of admissible tokens whose residual signatures join to target `z`. This gives an exact local 0/1/many-world normal form.

General minimum RJB contains SET COVER: use one residual word, Set-Cover universe elements as final outputs, and one branch signature per input subset. Thus generic exact minimum branch-basis optimization is NP-hard in the explicit finite-signature model; the decision form is NP-complete. Universal polynomial exact ABB claims should therefore be rejected absent additional structure.

A second kill test shows pairwise-incomparable exact irredundant bases can have widths 3 and 4, so local redundant-branch deletion can terminate at a nonminimum exact basis.

Certificate validity remains residual-language relative: validity for a larger `U` survives restriction, but extending the future language can invalidate an old RJC.

Duplicate recoalescence is also semantics-dependent: support union is idempotent, but multiplicity addition is not. A support-safe `{p,q}->{p}` merge changes multiplicity 2 to 1. R023's Boolean support scope should remain unchanged.

## Recommended R021 implementation delta

1. add `ResidualJoinCertificate` as the configuration-level exact rewrite contract;
2. add `residual_join_basis_width = nu_D(J(C))` with admissible dictionary/version and token cost;
3. add collective-dominance search after RCC/CS-NCC/pairwise reductions;
4. mark exact global RJB minimization as Set-Cover-hard in the general explicit model;
5. keep budget modes `EXACT / REPLAY_EXACT / HEURISTIC`;
6. cache RJC/RJB with both context/dependency and residual-language scope;
7. require idempotent aggregation or stronger weighted/tagged carrier before duplicate identification beyond support semantics;
8. candidate tool: `residual_join_normalizer`.

## Sharpened R022 classification

`BRC_RESIDUAL_CERTIFICATE_ALGEBRA_FOUND / RCC_NCC_UNIFIED_AS_JOIN_REWRITES / COLLECTIVE_DOMINANCE_FOUND / EXACT_BRANCH_BASIS_SET_COVER_HARD / SUPPORT_IDEMPOTENCE_BOUNDARY_CLASSIFIED / R021_FEEDBACK_READY / NOT_CANONICAL`
