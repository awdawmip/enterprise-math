# R5: Exact left-endpoint carrier for named finite multi-block observers

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable continuation; no formal CLAIM/RUN, Result or independent mathematical acceptance.

## Parent and frozen evidence

Original R5 source pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Immutable exact 101-budget/256-state center table: SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`; previous R5 18-stage response thresholds retained without alteration. Immediate predecessor: `research_notes/portable_direct/r5_pairwise_joint_observer_20261119/NONCONVEX_HELLY_OBSTRUCTION.md` at `cf32d119d825fed06fd79315b96bd1dccd86a2c1`. That work proved no universal finite Helly order for arbitrary two-block discrete responses. The present theorem gives a constructive lossless alternative with a linear-size **positive support witness** basis.

## Theorem 1: Closed multi-block endpoint carrier

Let `Ω=[a,b]` be a closed real response interval, or `Ω={a,a+1,...,b}` a finite integer chain. There are `n>=1` **named** states, with nonempty allowed response set `A_i⊆Ω` a union of `r_i<=r` nonempty closed contiguous interval components (after merging components if desired). For any response `z`, write its named support bitmask
`M(z)={i∈[n]: z∈A_i}`. Define the family of feasible nonempty named subsets `N={S≠∅: ∩_{i∈S}A_i≠∅}`, and `E` the set of all component **left endpoints**.

Then, for every nonempty `S⊆[n]`:

```
S∈N  ⇔  ∃ e∈E : S⊆M(e).
```

Consequently, the antichain `B=max_⊆{M(e)≠∅:e∈E}` is precisely the family of inclusion-maximal feasible supports; `|B|<=|E|<=Σ_i r_i<=nr`. It is the **unique inclusion-minimal mask witness basis** generating `N` by downward closure, and thus retains every feasibility predicate, including any high-order joint-intersection residual.

**Proof.** If `S` has a common response, choose, for each `i∈S`, one closed component `[l_i,u_i]⊆A_i` containing that response. Their common intersection is the nonempty interval `[max_i l_i, min_i u_i]`. Its left endpoint `e=max_i l_i` equals the left endpoint of one of the selected components and lies in all the selected components. Hence `S⊆M(e)`. Conversely, membership in `M(e)` is a literal common-response witness. Taking maximal members yields `B`; every feasible support belongs to a maximal one. Any exact generating witness-mask collection consists of feasible masks and must contain every maximal feasible mask, proving minimality and uniqueness after removal of redundant nonmaximal masks. QED.

For unbounded intervals, a common-left-endpoint construction additionally needs a finite left boundary or a declared sentinel (e.g. a clipped compact observation domain); the theorem is stated above for closed bounded `Ω`. For open/half-open sets one must also track endpoint-side atoms instead of assuming closed-endpoint witnesses. This is an observer-specific support representation, not a native X6 identity quotient or a theorem of dynamically safe reuse.

## Theorem 2: Arbitrarily high Helly rank still admits a linear carrier

For every `n>=3`, let `Ω=[0,10n]`, and `G_i=(10i-11,10i+1)` for `i=1,...,n`. Define the closed, at-most-two-block set `A_i=Ω\G_i`. The open gaps cover `Ω`, so `∩_{i=1}^n A_i=∅`. But the point `z_i=10i-5` lies in `G_i` and in no other gap; hence `M(z_i)=[n]\{i}`. Every proper named subfamily intersects, while the full family does not. Its unique minimal missing face is `[n]` of order `n`; the pairwise graph is complete `K_n`. Its exact endpoint carrier has precisely `n` maximal support masks `[n]\{i}`, meeting the preceding upper bound at linear order. This extends the preceding *discrete* two-block witness to ordinary **closed real intervals** without assuming a constant Helly number.

This apparent tension is resolved by storing positive **response-witness masks** instead of all negative minimal hyperedges: arbitrary intersection arity is compatible with `O(nr)` maximal observation supports whenever each state's allowed set has at most `r` closed components.

## Executable construction and cost units

Build `E` from the declared named component starts; evaluate `M(e)` for every `e∈E`; discard zero masks and all strict subsets of other masks. With at most `nr` anchors and at most `nr` components, direct membership comparison gives a simple polynomial bound `O(n²r²)` elementary interval comparisons plus `O((nr)²)` mask-containment comparisons; interval sorting/sweeping may improve constants. The `O(nr)` statement describes the number of witness masks, not a complete runtime or memory benchmark.

For the original R5 **scalar** observer `A_i(k,τ)=[c_i(k),c_i(k)+τ]`, one may use at most nine center anchors, recovering the prior pairwise clique/maximal-window support family exactly for all valid centers and thresholds. No center table, BRC type, scientific pin, or Bellman cost is altered by this generalization.

## Exact validation

The locally executed verifier `VERIFY_ANCHOR_CARRIER.py` and `RESULT_ANCHOR_CARRIER.json` give:
* exhaustive **27,000** ordered labeled 3-state families over five discrete responses (30 nonempty allowed at-most-two-run sets per state);
* exhaustive **50,625** ordered labeled 4-state families over four discrete responses (15 such sets per state);
* for each family, all `2^n-1` nonempty subset-feasibility verdicts checked against direct response enumeration;
* rational/integer endpoint construction checked for `n=3,...,12`, with `n` co-singleton maximal masks, full-family infeasibility and every proper-subfamily feasibility;
* pinned R5 bridge for eight named nine-state instances, seven budgets and all 18 exact noise stages: **1,008** support families, each checked against all **511** nonempty named subsets; maximum observed maximal support count six within this sample.

All checks passed under exact Python integers, no floats. The general theorem is symbolic and does not rely on finite enumeration. The verifier checks a **sample** of the frozen R5 population; no new 30,876-pair Bellman enumeration was executed.

## Next research

(1) Apply the carrier to a real constrained multi-interval native observer only after its exact named responses, branch/provenance, and future-operation requirements are specified; certify the needed descent across updates. (2) Compare computing component endpoints and preserving the sorted antichain versus full joint supports, including preprocessing and output recovery. (3) Keep the frozen full-256 eight-error Bellman bracket `8335<=C8*<=8343` as an existing historical bound; this result does not change it.

No new shared Task CLAIM, Source Result, or independent review is asserted.
