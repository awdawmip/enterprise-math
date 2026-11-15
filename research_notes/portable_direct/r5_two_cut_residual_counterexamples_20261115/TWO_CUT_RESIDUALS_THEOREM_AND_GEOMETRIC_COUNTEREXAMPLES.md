# R5 continuation — exact two-cut optimizer residuals and finite geometric counterexamples

**Date:** 2026-11-15. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
**Scientific lineage:** frozen input 435e77af0d180eac32bd1f9c4c464bc4010b7551; R5 Draft PR #2427, head 695fbb6f989c9193640a2c74c7aef074454b0d3c. Source: research_notes/portable_direct/r5_future_residual_and_two_cut_order_20261115/BOOLEAN_OPTIMIZER_DIAMOND_THEOREM.md. This is an independent derived-observer research note, not native X6 geometry, a new Task/CLAIM, or an independent review.

## Exact model

Take n strictly increasing integer events, with a positive-integer gap sequence. Two distinct selected original gaps a,b have length 3; their closure reduces length 3 to 2 and translates all downstream coordinates left by one without changing event identities or center indices. Choose exactly K distinct center indices among the n events. Require every event to have distance at most 2 from a selected center; minimize the integer sum of all nearest-center distances. Infeasible center sets have cost infinity. Let O_M be the complete family of optimal labeled center-index sets under closure mask M, and let J_M be its optimal sum. This note's claims concerning residuals assume J_empty=J_a=J_b=J_ab=J finite.

## Theorem: two independent observer residuals

Contraction of any selected gaps weakly decreases the nearest-center distances for each fixed labeled center set. The shared optimum J therefore implies

    O_empty subset (O_a intersect O_b) subset (O_a union O_b) subset O_ab.

Define the disjoint **single-cut intersection surplus** P and **joint-only surplus** Q:

    P = (O_a intersect O_b) minus O_empty
    Q = O_ab minus (O_a union O_b).

Then exact disjoint decompositions give

    O_a intersect O_b = O_empty disjoint_union P
    O_ab = (O_a union O_b) disjoint_union Q
    |O_ab| = |O_a|+|O_b|-|O_empty|-|P|+|Q|.

The complete Boolean optimizer diamond is equivalent to **P=Q=empty**, not merely equality of the usual cardinality inclusion-exclusion expression. A scalar cardinality equality could conceal compensating P and Q.

For equal-size labeled sets define d(S,T)=|S minus T| and H(X,O_empty)=max_{S in X} min_{T in O_empty}d(S,T), with H(empty,O_empty)=0. The disjoint union gives the exact general identity

    H(O_ab,O_empty)
      = max(H(O_a,O_empty), H(O_b,O_empty), H(Q,O_empty)).

Thus joint-only optimizer sets can change the exact max-new/min-old replacement distance even when the two single-cut distances are small. The minimum is over **all** old optimizers, not one chosen path.

## Witness 1: intersection identity fails at n=4

Original gaps (3,3,2), selected cuts (0,1), K=3; coordinates for masks empty,a,b,ab are

    (0,3,6,8); (0,2,5,7); (0,3,5,7); (0,2,4,6).

Each optimal sum equals 2. Writing 012 for center indices {0,1,2}, the complete optimizer families are

    O_empty = {012,013}
    O_a     = {012,013,023,123}
    O_b     = {012,013,023}
    O_ab    = {012,013,023,123}.

So P={023}, Q=empty: the intersection equality fails while the union equality holds.

## Witness 2: smallest union failure at n=5

Original gaps (3,2,3,2), selected cuts (0,2), K=3; coordinates empty,a,b,ab:

    (0,3,5,8,10); (0,2,4,7,9); (0,3,5,7,9); (0,2,4,6,8).

Every optimum sum equals 4. Exact optimizer families:

    O_empty = {013,014,023,024}
    O_a     = {013,014,023,024,123,124,134}
    O_b     = {013,014,023,024}
    O_ab    = {013,014,023,024,034,123,124,134}.

Hence P=empty and Q={034}. The center set 034 is infeasible with a single cut (maximum uncovered distance 3), but becomes optimal and feasible when **both** gaps contract (maximum distance 2, sum 4).

**Minimality by event count under these exact hypotheses:** n=3 has only two gaps, and all K=1,2,3 can be checked. With n=4 there is exactly one nonselected original gap g. When g>=3, all original adjacent gaps are >=3, so the base configuration needs all n=4 centers for radius-2 feasibility; the unique full-center family is unchanged. When g is 1 or 2, a finite exact check over all three selections of two cuts and K=1..4 exhausts the remaining cases: no joint-only optimizer appears when the four optima are finite and equal. The reproducible verifier enumerates the g=1,2,3 representatives (36 cases, of which 15 have equal finite J), covering g>3 by the preceding argument. Thus a five-event witness is minimal in this model class.

## Witness 3: strict two-cut maxmin synergy at n=6

Original gaps (3,2,3,3,2), selected cuts (0,2), K=4; coordinates empty,a,b,ab:

    (0,3,5,8,11,13); (0,2,4,7,10,12);
    (0,3,5,7,10,12); (0,2,4,6,9,11).

All four optimum sums equal 4. Exhaustive minimization over the complete old optimizer family gives

    H(O_a,O_empty)=1
    H(O_b,O_empty)=1
    H(O_ab,O_empty)=2.

A joint-only optimizer S={1,2,4,5} has two uncovered event indices, 0 and 3, each at distance exactly 2 after simultaneous closure. Every base optimizer is {0,u,3,v}, with u in {1,2}, v in {4,5}; it therefore shares at most two centers with S. Choosing a matching u,v proves exactly two replacements are sufficient. The full exact enumeration establishes the two single-cut maxima of 1. This is a strict failure of the unconditional extension of the earlier R5 union-derived maxmin formula to arbitrary integer-event geometries.

## Verification, scope and handoff

The paired verifier enumerates all combinations of K labeled center indices, computes exact integer nearest-center costs and feasibility for all four masks, constructs complete optimizer families, calculates both residuals and the exact directed maxmin metric, and checks minimality of the five-event union counterexample on the finite n<=4 domain (with the g>=3 proof above). The verified local Python run returned PASS_EXACT_TWO_CUT_RESIDUALS_AND_MINIMAL_UNION_COUNTEREXAMPLE; the adjacent small Python checker and machine-readable evidence carry complete sets and distances.

The frozen 954-event R5 Boolean diamond for cuts 8 and 9 at K=214..221 remains a special-case result: the present counterexamples refine the conditions under which that structure generalizes. They do not modify the R5 frozen input, native P000 assumptions, or the historical model-specific 64-case proof. **Open unit:** derive a geometric sufficient condition making both P and Q vanish, and implement exact labeled optimizer-DAG subtraction to count P and Q without enumerating full paths; check its result on these witnesses and all 64 frozen R5 backgrounds. The author evidence remains NOT_REVIEWED, and no formal Task, owner, Result, or Activity authority is asserted by this file.
