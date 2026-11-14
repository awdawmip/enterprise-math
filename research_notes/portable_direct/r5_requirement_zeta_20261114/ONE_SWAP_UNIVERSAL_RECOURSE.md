# R5 — exact one-center recovery for all 28-gap closure backgrounds, K=293–314

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED (2026-11-14). Scientific input fixed at `435e77af0d180eac32bd1f9c4c464bc4010b7551`; mathematical claim is confined to the frozen 954-event derived integer-coordinate, radius-two indexed-center observer.

## Statement (complete quantifiers)

Let I={0,...,27} label all original 3-gaps, x^B denote closing gaps B, and Opt_B(K) the collection of cost-minimizing feasible K-element original-index center subsets (nearest selected-event distance summed over all 954 events). For i in {15,17}, every integer K in [293,314], and **every** B subset I\{i}, define

rho_B(S;K) = min_{T in Opt_B(K)} |S\T|,

R_i(K) = max_{B subset I\{i}} max_{S in Opt_(B union {i})(K)} rho_B(S;K).

Then **R_15(K)=R_17(K)=1** throughout K=293,...,314. The order max-background, max-new-optimum, min-old-optimum is part of the theorem. Even a newly optimal S chosen adversarially can recover an old optimum by replacing at most one center. The lower bound is strict for every B: some newly optimal S requires exactly one change.

## Reduction to four exact finite checks

Prior pinned proof in `RESEARCH.md`: at these budgets, J_B(K) is independent of B, every all-closed optimizer S has a unique least enabling mask M(S), and M(S) subset {15,17}. Consequently Opt_B(K) is the subfamily satisfying M(S) subset B.

Fix i and B not containing i, S in Opt_(B+i)(K). If i not in M(S), then S is already in Opt_B(K), so rho=0. Otherwise A=M(S)\{i} is either empty or the other special singleton. S is an optimizer of A+i; if a one-center modification T is optimal for A, then T is also optimal for B by monotonicity and cost invariance. It is therefore enough to certify **every** optimizer S at just the following four base transitions:

- 15 -> none, where cut index 15 is removed;
- 17 -> none, where cut index 17 is removed;
- both -> 17, where cut index 15 is removed;
- both -> 15, where cut index 17 is removed.

These are 22*4=88 finite cases. The inverse direction in the labels indicates recourse from a new closed geometry to its predecessor.

## Exact optimizer-path enumerator

For sorted center indices j_1<...<j_K the radius-two coverage cost splits into a prefix cost, one edge cost between each consecutive pair, and a suffix cost. There is an edge j->q precisely when every intermediate event is within distance two of the closer endpoint; its integer weight is w(j,q)=sum_{j<t<q}min(x_t-x_j,x_q-x_t). Each feasible edge spans at most seven coordinate units. A valid center path uses prefix and suffix event costs as in the already published `VERIFY_R5_REQUIREMENT_ZETA.py`.

Compute forward exact integer costs F_t(j) for a prefix of t selected centers ending at j. Compute backward exact integer costs G_m(j) for m further selected centers after j, including the terminal suffix. An optimal K-center path can pass through (t,j) exactly when F_t(j)+G_(K-t)(j)=J(K). On this path, j->q is allowed exactly when F_(t+1)(q)=F_t(j)+w(j,q) and its successor has total optimal completion J(K). Both checks are applied.

For each target physical gap with starting **event** index h (h=194 for cut 15, h=245 for cut 17), record all selected center-index patterns within [h-9,h+9]. The path enters this window from a selected index in [h-16,h-10], because consecutive selected centers span at most seven index positions. Enumerate all optimal prefixes at these boundary states using F and G; traverse every optimal path transition until the first center index greater than h+9, and retain its pattern. The backward cost certifies global completion. Every full optimal center subset has one enumerated local pattern. Duplicate patterns are deduplicated (which is legitimate for the universal local repair property).

## Local-surgery certificate

For every enumerated local pattern P, compare the new and old event coordinates on the event window [h-6,h+7]. Either its selected centers already give the **same feasible local cost** in both geometries, or the exact checker finds p in P intersect [h-4,h+5] and q in [h-4,h+5]\P so that replacing p by q makes the old local distances all <=2 and keeps their exact sum equal to the original new local sum.

This is a complete global certificate: a change of a center within [h-4,h+5] can affect only events in [h-6,h+7], because event gaps are >=1 and coverage radius is two. Closing/opening the specific 3-gap can alter a distance <=2 only between its immediately adjacent event endpoints, already in this window. Every center that can contribute to a nearest distance <=2 for its events lies within [h-9,h+9], so the recorded pattern determines these local scores; all other event scores stay unchanged. Thus every certified one-swap T is feasible in the old geometry and satisfies C_old(T)=C_new(S)=J(K). It belongs to Opt_old(K).

The exhaustive exact test passes for all 31,336 local pattern records across the 88 transition/budget cases. For each, the checker stores whether the pattern was already old-compatible or gives an exact one-swap transformation. An asserted positive one-swap pattern in each case also independently supplies a strict lower-bound witness; alternatively the earlier all-background strictness theorem in PR #2398 gives strictness for every B.

## Exact evidence

Executable verifier `VERIFY_R5_UNIVERSAL_UNIT_RECOURSE.py` imports `frozen`, `close`, and `INF` from the original `VERIFY_R5_REQUIREMENT_ZETA.py` in this directory (the original script is already preserved in this PR, pinned scientific input unchanged). The verifier uses Python integers without floating point; it computes all shortest-path states and local patterns rather than sampling global optimum sets.

Observed run: `PASS_EXACT_R5_UNIT_RECOURSE_ALL_BACKGROUNDS`; 22 budgets, 88 exact cases, 31,336 distinct case-local patterns checked, no unresolved pattern. `EXACT_R5_UNIT_RECOURSE_SUMMARY.json` records every budget's transition pattern counts and one-swap counts. The script prints the expanded 88-case rows including replacement types and path-boundary counts. Local repair candidates seen for cut 15 include 191->192, 198->197 and 198->196; for cut 17, 242->243 and 249->248 (0-based event-center indexes).

These counts are **patterns**, not counts of full optimal K-subsets; one pattern can represent many complete paths. Exhaustive coverage derives from the dynamic-programming path decomposition and the local-score support lemma.

## Scope, provenance, continuation

The theorem settles the previously open frozen-R5 max-background/max-new-optimum/min-old-optimum question for K=293..314. It does not cover the separate generic unbounded recourse family (PR #2407) or K=214..291 of the frozen R5 instance. Native X6 path and provenance state, the 2,520-byte certificate and original 8,192-prefix-query benchmark are separate frozen objects, not replaced by this derived center-observer result.

Sources: original R5 frozen science pin above; exact optimizer/filter derivation in this PR's `RESEARCH.md` and `EXACT_R5_REQUIREMENT_ZETA.json`; prior strictness at PR #2398, commit `e469fa1eaa167b566c1e08012ca571041758d4fc`. Next mathematical unit: classify maximal necessary recourse below K=292 and test whether any other cut can have a nontrivial minimal enabling mask. Independent review remains NOT_REVIEWED; this is no claim of formal Task/CLAIM/Result admission.
