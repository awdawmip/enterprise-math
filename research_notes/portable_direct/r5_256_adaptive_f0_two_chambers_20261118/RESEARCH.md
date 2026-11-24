# R5: exact 256-hypothesis adaptive zero-error minimax in two noise chambers

Date: 2026-11-18 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is independent portable-direct scientific preservation, not Task CLAIM/Result/Review.

## Frozen model and proposition

Scientific input commit: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`. Input \`EXACT_R5_ALL_101_BUDGETS.json\`, SHA-256 \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`. There are exactly 256 **named** scalar hypotheses h=0,...,255 and physical budget actions k=214,...,314. Action k has cost k, and a correct real observation y lies in [N_h(k)-τ/2,N_h(k)+τ/2]. The **zero-corruption** (\`f=0\`) policy may select the next budget and stop according to previous observations. Its objective is the minimum worst-case accumulated cost for certain identification of the named h.

Let
- L = 25845652773852463277015040000,
- U = 58182461585441404127941754880,
- T = 1876919155234970890319953920000,
- D = 1882951873548292168718745600000.

**Theorem (exact adaptive f=0 values):**
1. For every real τ in [L,U), \`C_0^adaptive(τ)=735\`. The only optimal first budget actions are 216, 223, and 296.
2. For every real τ in [T,D), \`C_0^adaptive(τ)=955\`. The only optimal first budget actions are 215, 224, and 298.

At the second chamber the previously saved all-f **fully prepaid fixed-batch** theorem gives \`C_0^fixed=957\`; observation-dependent next-budget choice saves exactly 2 cost units. For the fifth chamber the previously saved fixed batch is 216+223+296=735 and is already adaptive-optimal.

## Exhaustive finite proof and cost recurrence

For any candidate set S⊆H, each possible real y produces support \`R_k(y)={h in H: |N_h(k)-y|≤τ/2}\`. For equal-radius closed intervals the inclusion-maximal supports are exactly the maximal sets of sorted centers lying in a window of width τ. They can be constructed by a two-pointer integer scan over all 256 centers. Independently, the verifier recomputes every maximal support by sweeping all exact interval endpoint events \`2N_h(k)±τ\` and testing endpoints and between-endpoint samples; agreement is checked for all 101 budgets at all four tested thresholds.

A support strictly contained in another can be discarded for a worst-case zero-error minimax recursion: retaining more named candidates cannot lower future cost. For each actual maximal support C, the next candidate set is S∩C. If S∩C=S is possible, querying k cannot improve the worst-case cost: with the same S still possible, skipping this positive-cost query and using its continuation is never worse. Therefore it is sufficient to enumerate strictly informative actions.

Define \`V_d(S)\` as the optimal worst-case future cost using at most d further queries; \`V_d(S)=0\` if |S|≤1, and \`V_0(S)=+∞\` if |S|>1. For d>0 and |S|>1,

\`V_d(S) = min_{k informative on all nonempty outcomes} [k + max_{C: S∩C≠∅} V_{d-1}(S∩C)]\`.

All candidate sets are exact 256-bit integers, all observations/threshold comparisons exact Python arbitrary-precision integers, and all 101 actions are enumerated. \`V_d\` is a Bellman identity (induction on remaining depth). The verifier reconstructs one minimizing policy, recursively checks every possible maximal response support, and verifies its exact worst-case cost. Its search also enumerates all optimal first actions.

There is no missing deeper strategy at the claimed optima: every query costs at least 214; four queries cost at least 856>735 in the fifth chamber, and five queries cost at least 1070>955 in the near-critical chamber. Thus d=3 and d=4 suffice for **unrestricted finite adaptive policies** at these optima. Exact exhaustive Bellman values are independently checked at both integer boundary thresholds in each chamber. Since N_h(k) are integers, for every real τ<U the separation/support decisions are bounded by those at U−1, and similarly τ<D by D−1. Monotonicity of minimax cost in τ and identical endpoint Bellman values yield each complete real half-open chamber.

## Actual executed checks

\`python VERIFY_R5_ADAPTIVE_ZERO_ERROR.py EXACT_R5_ALL_101_BUDGETS.json\`

Exited 0 with \`PASS_R5_256_ADAPTIVE_F0_EXACT_TWO_CHAMBERS\`. Endpoints: L and U−1 each return 735, first actions [216,223,296]; T and D−1 each return 955, first actions [215,224,298]. Exact Bellman memoized states: L 1,056; U−1 915; T and D−1 each 2,615. Independently generated support sets agree for all 101 budgets at all four endpoints; the complete minimizing policies are regenerated and exhaustively rechecked against all possible response support branches. The source 954-event aggregation is inherited from the declared immutable input and is not rerun.

## Typing, provenance, and next unsolved unit

These theorems concern **the frozen scalar observer language** under f=0, not a collapse of Heartbeat World native X6, signed branches, source/time or joint-observer residuals. The 256 named configurations remain distinguished throughout the exact search. P000, current ACTIVE worldview and observer-fidelity requirements remain unchanged.

Earlier scientific sources: PR #2427 fixed-batch all-f theorem \`06450ad3a3b37fef64d32bcd0a5bf89143c904ac\`, sharp threshold / near-critical all-f theorem \`20c2b210c6d6ea4ed41caf6efd311c4a2c039a0d\`, fixed-order optional-stop theorem \`76a2b421dac37a9d2c38ed819e3bcfb22151d345\`. The new result is an adaptive **zero-corruption** benchmark and an exact witness that adaptivity can reduce near-critical costs even when fixed-order stopping alone cannot.

**Next:** develop residual-preserving pruning/certificates for the full 256-hypothesis **f=8** adaptive minimax in the fifth chamber, whose currently verified bounds remain 8335≤C_8^*≤8343. Reuse the exact maximal-response enumeration and per-named-hypothesis mismatch counters; do not identify independent hypotheses solely by a shared scalar quotient. Current independent review: NOT_REVIEWED.
