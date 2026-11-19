# R5 native two-hypothesis exact Bellman certificate and common-error gauge

2026-11-19. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable research, no formal CLAIM/RUN or independent Review.

## Frozen original model

Science pin: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551. Exact 256-state integer center table: EXACT_R5_ALL_101_BUDGETS.json, SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Named hypotheses h=0,...,255; 101 physical actions k=214,...,314, each with deterministic cost k; a correct real observation y obeys 2|y−N_h(k)|≤τ. Up to f unmarked observations are arbitrary corruptions. Repeated/adaptive queries allowed. Unknown varying τ∈[L,U), U=58182461585441404127941754880, has the previously proved identical worst-case support game to fixed τ*=U−1 because centers are integers. We retain named hypotheses and their independent error counters; this is an observer-layer result, not an X6/Port quotient.

Predecessor: [unknown diameter seven-action theorem](https://github.com/awdawmip/enterprise-math/blob/7980545e4f2de4341fb63069f9f926de27d0c5b4/research_notes/portable_direct/r5_256_unknown_tau_seven_core_20261118/RESEARCH.md); [7–8–7 chamber theorem](https://github.com/awdawmip/enterprise-math/blob/4fe9b543bff2b31fb58530af1edff71bf290c54d/research_notes/portable_direct/r5_256_chamberwise_7_8_7_20261118/RESEARCH.md). Previous cost-visible CVA1 theorem is an auxiliary model with hidden-state-dependent resource costs and is not silently imported as R5's physical-cost semantics.

## NPB1 — exact two-hypothesis adaptive minimax value

Fix a pair h≠g and prior minimum required mismatch counts e_h,e_g≤f. Define κ_τ(h,g) as the minimum physical action cost k for which |N_h(k)−N_g(k)|>τ; take κ=∞ if none exists. The exact optimal additional total query cost to identify one of this pair, with arbitrary adaptive queries and at most f unmarked corruptions, is

**V_pair(e_h,e_g;f,τ) = (2f−e_h−e_g+1) κ_τ(h,g).**

Proof (lower bound): correct response intervals overlap exactly when their center gap is ≤τ. For overlapping intervals, an adversary can choose a response compatible with both, spending no mandatory mismatch. For disjoint intervals it can select a response compatible with precisely one of the pair, increasing the other's mismatch count by exactly one. Let r_h=f−e_h, r_g=f−e_g. Distribute at most r_h+r_g such separating responses without exceeding either allowance, and answer every nonseparating query from the overlap. Both hypotheses stay feasible, so a valid identifying policy must pay for at least r_h+r_g+1 separating queries, each costing ≥κ. Every finite maintained transcript has a single feasible fixed truth and an assignment of at most f corruptions; the adversarial lower-bound path is therefore legitimate.

Proof (upper bound): repeatedly ask any cheapest separating action k=κ. Since its correct-response intervals are disjoint, every response increases at least one of e_h,e_g. After r_h+r_g+1 repetitions, at least one hypothesis exceeds f; the pair is identified at cost (r_h+r_g+1)κ. If no separating action exists, overlap responses can retain both forever. For varying unknown τ<U, integer center gaps imply separation at U−1 works at every τ<U, and the adversary can choose constant τ=U−1. Thus the same formula holds for the robust interval.

**Consequently** for any full-256 scalar Bellman error-count state e, the admissible additional-cost lower bound is

V_full(e;f,τ) ≥ max_{h<g:e_h,e_g≤f} (2f−e_h−e_g+1)κ_τ(h,g).

This is a branch-specific pruning heuristic retaining all hypothesis identities. The count f=8 is an error allowance, *not* a query-length horizon.

## NPB2 — exact residual-gauge sufficient state

For each response with correct-support mask S, the error-count update is e'_h=min(f+1,e_h+1_{h∉S}). If some hypothesis remains live, let m=min_h e_h, R=f−m, and d_h=min(R+1,e_h−m). Then the pair (R,d), with all named coordinates retained, is an exact sufficient state for the scalar Bellman continuation.

To update, set v_h=d_h+1_{h∉S}, δ=min_h v_h (0 or 1). If δ>R all hypotheses are excluded. Otherwise set R'=R−δ and d'_h=min(R'+1,v_h−δ).

Proof: the full unsaturated vector increments by the same binary membership vector. Subtracting its new minimum removes precisely δ, while capping at R'+1 preserves every viable/invalid distinction. A previously invalid hypothesis cannot revive. The transition therefore commutes with the quotient; a terminal state has at most one h with d_h≤R. Every response-support transition, terminal outcome and deterministic physical action cost is a function of (R,d) alone. Induction on finite strategy trees gives the same future game and minimax additional value, and equality of every finite stopping tree extends the conclusion to unbounded strategies. This quotient can share equivalent states across different f or absolute mismatch offsets; **no fixed-f memory reduction is asserted** (256 capped f=8 counters already occupy only 128 packed bytes).

## NPB3 — physical cost and lie-count observability

The native action cost k is determined by the controller's own action history and never depends on the hidden hypothesis. Reading accumulated physical cost adds no information to that history. In contrast, e_h is the minimum mismatches required for each hypothesis, not an observed exact number of actual corruptions. Because corruptions are unmarked and may imitate valid responses, the latter number is generally unobservable. Thus the CVA1 state-dependent cost-visible auxiliary model cannot be used as an R5 hidden-lie-count oracle. The actual native information state is the full named mismatch vector, equivalently (R,d) for this scalar model.

## Frozen 256-state exact census and joint-observer obstruction

The original 256×101 integer centers were checked by SHA-256. All 32,640 distinct named pairs were classified at each of the 18 exact τ signature stages, across all 101 actions: 59,339,520 exact pair/action/stage center comparisons. All pairs are separable. At robust τ*=U−1 the histogram of cheapest separating costs is:

| k_min | Named pairs |
| ---: | ---: |
| 214 | 30,528 |
| 215 | 1,216 |
| 223 | 512 |
| 295 | 320 |
| 296 | 64 |
| Total | 32,640 |

Hence max κ=296 and the pairwise root lower bound for eight errors is 17×296=**5,032**. The pre-existing stronger multi-hypothesis lower bound is **8,335**, with C8*≤8,343, so this new bound is chiefly a cheap exact *branch-specific* heuristic.

Across all 18 stages the only species that are ever cheapest pair separators are {214,215,223,294,295,296}; **216 and 217 never are**. Nonetheless neither 216 nor 217 is simulable by any cheaper single query under maximal correct-response-support refinement at τ*=U−1. Concrete witness: maximal support for j=216

{2,18,34,50,66,82,98,114,128,144,160,176,192,208,224,240}

is not contained in any maximal k=217 correct-response support. The machine certificate includes analogous witnesses for j=214,215 against targets 216 and 217. Thus **absence from every cheapest-pair-separator list does not imply multi-hypothesis observer redundancy**. This is a specific higher-order joint-residual obstruction; it does not assert that either 216 or 217 is globally essential to every optimal policy.

## Validation and reproduction

Local full checker VERIFY_NATIVE_PAIR_GAUGE.py, run against the unchanged frozen JSON and stages_18.json, returned:

PASS_R5_NATIVE_PAIR_GAUGE 18 32640 f8_lower 5032 gauge_checks 17544 witnesses 5

It verifies the 17 exact gap thresholds, 18 histograms, all five explicit support witnesses, and checks the real-interval-support versus center-gap equivalence independently for all 228,480 pair/action combinations in the seven-action robust core. The gauge transition is exhaustively checked for **17,544** small capped-vector/mask instances (n=2..4, f=0..3). The pair recurrence is checked for 486 allowance/cost combinations; a separate exact two-hypothesis interval-response Bellman solver independently matches **1,024** finite initial states across 120 seeded variable-center/cost/τ models. All computations use exact integers and event boundaries, not floating approximation. The symbolic proofs above establish the stated general propositions; these finite tests establish their declared implementation coverage.

Local reproducibility package: EnterpriseMath_R5_Native_Pair_Gauge_20261119.zip, containing the full proof, checker, exact 18-stage result JSON, unchanged 1,549,048-byte scientific input, stage definitions, and per-file SHA-256 manifest. The original frozen input is not silently repinned or rewritten into this GitHub branch.

Next unit: incorporate the named live-pair lower bound and residual gauge in the seven-action, f=8 exact Bellman search at τ*=U−1, measuring pruning and update costs on an immutable difficult branch. Seek a certificate that genuinely improves 8335≤C8*≤8343 while preserving Port/X6 provenance and separate formal Result/Review authority.

Source status: independent science, Git branch only pending any canonical intake; Activity association and independent mathematical review to be assessed separately.
