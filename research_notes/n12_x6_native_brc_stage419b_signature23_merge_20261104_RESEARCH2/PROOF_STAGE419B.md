# Stage419-B — Two further full-horizon merges in the native-X6 double-budget BRC future quotient

Date 2026-11-04; Research2 author-side continuation from Stage418-B, commit `6005a6c06b667468b79d1abcca1cf703286e2a33`, Draft PR #1736. Classification: **AUTHOR_SIDE_PROOF / EXACT_FINITE_EXECUTION / UNREVIEWED / NOT_ADMITTED**. Task-frozen science: account-global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 **blob** `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral rules are separately read from canonical main. This is a restricted ordered-path model embedded in P000's signed native six-axis space.

## Declared observer and future language

Let `D={+E_1,-E_1,...,+E_6,-E_6}` (twelve signed primitive directions); `A=+E_1`, `B=-E_1`. A history is an ordered pair of direction words `(P,Q)`. Its complete observation is `O=(|P|,|Q|,z(P),z(Q),J(P),J(Q),K(P,Q))`, with six signed chart-relative endpoint coordinates `z` for each source, full source-specific **directed** `D×D` adjacency multiplicities `J`, and `K(P,Q)=sum_{j=1}^{min(|P|,|Q|)} 1[P_j=Q_j]` (absolute-position alignment). An attempted operation returns success or failure; every successful intermediate observation is visible.

The future language permits arbitrarily many `APP(a,b)` for any `(a,b)∈D²`, at most two Q-only `POP`s, and at most two paired `CANCEL`s. A `CANCEL` succeeds precisely when **both** source words end in inverse adjacent direction pairs, and then deletes the final two labels of each word. Failed actions are observed and terminate the attempted trace. All equivalences below quantify over every finite such trace and over all twelve native directions.

For `n≥11`, take the Stage411/415 complete initial-observation fiber

`P_i=A^(i-1) B A^(n-i)`, `Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s)`, where `2≤r`, `r+2≤s≤n-1`, and `i∈{r,s}`.

For the present two groups, put `s=n-3`; thus `2≤r≤s-2=n-5`. Define `H_2(n)={(P_r,Q_(r,s)):2≤r≤s-2}` and `H_3(n)={(P_s,Q_(r,s)):2≤r≤s-2}`. They are two distinct classes of the Stage417 fixed finite-test signatures, with `n-6` histories each, and three Stage416 safe suffix keys each.

## Lemma 419.1 — original-word deletion frontier

For any legal future started from **either** of these two groups, let `d_P`, `d_Q` denote the numbers of original labels removed from the respective right ends, and `U,V` the surviving appended suffixes. At every reachable state:

1. `0≤d_P≤2`. The original `B` in P is never removed. If a further `CANCEL` remains available, the surviving original P word ends in at least two A labels.
2. `0≤d_Q≤4`. The first three removed original Q labels, when removed, are A; the possible fourth is its second B at original position `s=n-3`. Removal of that B exhausts **both** POP and **both** CANCEL budgets, so no further destructive action is possible. In particular, the first Q B at position `r≤s-2` always survives.
3. Whether a terminal action is enabled, and whether it removes appended and/or original labels, is determined by `(d_P,d_Q,U,V,remaining POP,remaining CANCEL)` and the **group identity** (`H_2` or `H_3`), independently of `r`.

**Proof.** Each `POP` removes at most one Q label and never alters P. Every successful `CANCEL` can remove at most one original P A as long as P's original suffix has at least two A's: its last two original A's are not inverse, so removing an original P label requires an inverse appended label immediately above it. The initial P A suffix is of length `n-r≥5` in `H_2`, and exactly 3 in `H_3`. Consequently at most two original P A's are removed in two CANCELs. Whenever a CANCEL budget remains, at most one such A has been removed, leaving at least two original P A's in either group. In particular, P's original B cannot be removed.

Initially Q ends in `B A³`. To remove its second B, the three later original A's must first be removed. They cannot be removed by paired CANCEL acting on an all-A original pair; each such removal costs one POP or a paired CANCEL removing one original A against an appended inverse label. Before **any** Q-B removal, at least three of the total four destructive actions (two POP, two CANCEL) must therefore remove these three As. If the B is removed by the **second** CANCEL, both POPs and the earlier CANCEL must already have removed original Q As. No POP then removed an appended Q label. Before that earlier CANCEL can remove one original Q A, Q must have exactly one appended inverse direction above it; since no earlier CANCEL exists and neither POP removed an appended direction, this also forces exactly one previous paired APP, whose P component must be B to enable the P cancellation. Immediately after that earlier CANCEL, P ends in at least two original A's, with no appended suffix on either source.

Now the Q B can be removed on the second CANCEL only as `B` paired with a freshly appended `A` on Q (a simultaneous appended B on P makes both sides cancellable); this removes the B as the **fourth** original Q label and spends all destructive budgets. The alternative cancellation of the two adjacent **original** labels `(A,B)` at positions `s-1,s` requires no appended suffix on Q, hence none on P: the two POPs were spent deleting original As, and paired APP/CANCEL preserve equal appended counts up to this moment. But P's original terminal pair is `AA`, so that CANCEL is disabled. A first-CANCEL removal of the original Q `(B,A)` pair is likewise impossible: exposing that original terminal pair requires two Q POPs, leaving no Q-appended deletion; paired APPs on P cannot produce an enabled inverse P terminal pair while leaving Q with no appended suffix. Thus B removal, when possible, occurs exactly as described, and cannot remove the preceding Q A. No more original Q labels are accessible after budgets are spent.

The possible original terminal patterns are therefore entirely fixed: for P the relevant terminal original word is A (and at least AA if a CANCEL remains); for Q it is a suffix of `BA³`, possibly reduced to the common predecessor A after removal of the B, when the remaining destructive budgets are zero. Together with the common U,V and budgets this fixes terminal tests and the original/appended boundary type. Induction on successful actions proves (3). ∎

## Theorem 419.2 — two additional all-future equivalence classes

For each `n≥11`, **all histories within `H_2(n)` are observationally equivalent** under the full language above. Independently, all histories within `H_3(n)` are observationally equivalent. The two groups remain future-distinguishable by the already published Stage417 fixed tests.

**Proof.** Compare any two histories from one of the two groups under a common attempted trace. Use the invariant that both reached states have the same deletion counters `(d_P,d_Q)`, surviving appended words `(U,V)`, destructive budgets, and full observations `O`. Initially it holds: the fiber fixes O, and the counters and appended suffixes are empty. Lemma419.1 gives identical next-operation enabledness and, if successful, identical updates to counters, appended words, and budgets.

To complete the induction, verify the full observer, not merely endpoints. Both initial six-vector endpoints are identical within the fiber. Deleted original labels have the common sequences `A^dP` for P, and `A^min(dQ,3)` followed when `dQ=4` by `B` for Q. Adding the common appended words preserves six-vector equality.

For J, every removed original P edge is AA. Removed original Q edges, in order from the right, are AA, AA, BA and (when `d_Q=4`) AB. The attached junction with U or V and internal appended edges depend only on the common deletion counters, the common remaining original terminal direction and the common appended suffix. Thus the complete **directed** adjacency histogram for each source is preserved at each step.

For K, write `t=min(n-d_P,n-d_Q)=n-max(d_P,d_Q)≥n-4=s-1`. Among the first t original aligned positions, group `H_2` has exactly one mismatch, at position `s` (P has A, Q has B); hence its equal-position count is `t-1[t≥s]`. Group `H_3` has exactly one mismatch at `r≤s-2`, so its original-prefix count is `t-1`. Crucially these formulas are independent of r *within the specified group*. Every aligned comparison after position t contains at least one appended label; any original label involved lies at index at least `s`. The original suffixes on indices ≥s are identical within `H_2` and, separately, identical within `H_3` (P's B occurs at s only in H_3; Q's B at s in both). These remaining comparisons are functions of the common `(d_P,d_Q,U,V)` alone. Therefore K is preserved even in the unequal-length, post-POP and post-CANCEL states.

By induction every successful observation agrees; a denied operation is denied on both histories. This proves all finite traces and all twelve-direction APP choices. ∎

## Corollary 419.3 — improved parameterized minimum-state interval

Stage416 supplied 32 sufficient raw suffix keys for `F_n`, n≥11. Stage417 proved that four keys of signature 0 merge; Stage418 proved the analogous four-key merge of signature 1, giving 26 sufficient states. Here each of the distinct signatures 2 and 3 contains three raw keys, all now proven equivalent: each merge saves **two** more keys. Stage417's 16 mutually distinguishable finite-test signatures retain the lower bound. Hence, for all integers `n≥11`,

`16 ≤ q_{2 POP,2 CANCEL}(F_n) ≤ 26 - 2 - 2 = 22`.

The four now proven future-equivalence classes (signatures 0,1,2,3) have respective populations `(n-7)(n-8)`, `2(n-7)`, `n-6`, `n-6`. For `n=16` their populations are `(72,18,10,10)` and account for 110 of the 156 original histories. The other twelve finite-test signatures remain the exact minimization problem; the inherited upper-bound construction has 18 states for those twelve signatures.

## Executed validation and reproducibility

`REPRO_STAGE419B.js` uses only exact integer, string and finite combinatorial operations; it generates the full parametric fiber, computes both source endpoints, each full directed adjacency histogram J, exact absolute-position K and failed-action behavior, and checks all three existing safe suffix representatives for both target groups. Run: `node REPRO_STAGE419B.js > REPRO_STAGE419B_EXECUTED.json`.

Execution verifies for every n=11..40 that each target group has `n-6` histories, three suffix keys, and equal full initial observation. For n=11 it executes **961,524 bounded trace instances** across both groups (some trace families overlap): up to one APP from all 12 directions with both destructive budgets; up to two APP from all 12 directions with ≤1 POP and ≤1 CANCEL; up to two APP from four directions with full budgets; and up to three APP from ±E1 with full budgets. Each trace checks all intermediate full observations and attempted action enabledness of the three suffix representatives. Marker: `STAGE419B_SIGNATURE_2_3_MERGE_PASS`.

The universal result is from Lemma419.1 and Theorem419.2; bounded traces are a computational cross-check. No review or native Source Result is conferred by the reproducibility result. The original frozen science and P000 machine source remain unchanged.

## Next research unit

Stage420-B should examine finite-test signatures 4–7 (`s=n-2` and the associated relative B placements; confirm exact membership against the Stage417 source). Retain both full directed J and joint K during POP/CANCEL. For each signature either exhibit a full-horizon budget-aware bisimulation among its raw keys or a shortest explicit distinguishing trace over all twelve signed directions. Then invoke Stage412 Euler/K counting on the resulting certified partition. Formal native ownership, Result and independent Driver review require their separate authority path.
