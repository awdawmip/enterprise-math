# EC49FXY — Conditional indexed-spectrum adaptive observation theorem

Date 2026-11-23. Frozen scientific input BRC16943. Parent EC49FXX, immutable commit bb2ea3ab8678a0caf13be11ad2ed09cbd845e327; preceding EC49FXW/FXV/FXU and their genuine-Farey census are retained. Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED. Scope: original frozen scalar C11 auxiliary Boolean observation model; no native X6 transfer.

## Distinguishing a change in information order

Keep the exact physical predicate C11(h,n)=P10(h mod 10,n mod 10) times 1[9h+10n !=0 (mod 11)]. For each genuine reduced Farey anchor 0<a<b<=H, use the frozen determinant-one rephasing and normalized 110-bit product trace u. Let sigma(u) be its complete 110-entry INDEXED reflection-defect spectrum.

Prior EC49FXX required ONE fixed set of physical Boolean sites S to be chosen BEFORE spectrum observation, and its extra-Boolean-probe optimum N_H(r) depends on H. Here the observer receives sigma(u) FIRST and is permitted to select different physical sites S_sigma AFTER the spectrum, to distinguish all u with that sigma and b<=H at minimum Hamming distance r. We price ONLY the subsequently read Boolean sites. The acquisition cost of the complete indexed spectrum is NOT included in either fixed or adaptive comparison.

Let A_H(r) be the minimum worst-case number of such post-spectrum Boolean readings, with A_H(r)=infinity when a remaining equal-spectrum pair cannot attain distance r even if all 110 sites are read.

## General exact adaptive-fiber lemma

Given any finite family of binary strings with an observed side-information partition into fibers of size at most two, let Delta_f be the set of differing indices for a two-element fiber f. Let mu be the minimum size of Delta_f across all two-element fibers; use mu=infinity if none exists. For every positive integer r, the exact minimum worst-case post-side-information cost is 0 if no doubleton exists, is r if r<=mu and some doubleton exists, and is infeasible if r>mu.

Proof. In any two-element fiber every selected binary site contributes at most one to Hamming distance, so at least r selected sites are necessary. All 110 measurements together distinguish a given pair on exactly Delta_f; if |Delta_f|<r the task is infeasible. Conversely, once its fiber is revealed, choose any r different indices from Delta_f; their Hamming distance is exactly r. On singleton fibers select none. The worst-case cost attains the lower bound. QED.

## Exact theorem for the frozen genuine Farey C11 model

For every integer H>=2, the smallest full-physical-trace Hamming distance among any two different genuine normalized states of height <=H with the SAME indexed reflection spectrum is:

mu_H = infinity for 2<=H<=13; 40 for 14<=H<=15; and 20 for all H>=16.

Therefore for every positive integer r:

A_H(r) = 0 for H<=13;
A_H(r) = r for H=14 or 15 and r<=40;
A_H(r) = r for H>=16 and r<=20;
A_H(r) = INFEASIBLE otherwise.

In particular, with a complete indexed spectrum supplied, a globally valid selector can use the full 600-state atlas without knowing H: for every r<=20, choose any r sites in the revealed doubleton's difference set, or no sites on singleton fibers. Its worst-case additional Boolean cost is EXACTLY r; a 20-site difference pair makes any universally-valid r>=21 infeasible.

## Finite-census proof of the three transitions

The exact normalizations of 72 ten-phase residue representatives give 50 P10 support words. The reduced rational anchors exhaust 600 normalized states by height b=139. Their complete indexed reflection spectra form 478 fibers: 356 singletons, 122 doubletons, none with more than two different states. Each doubleton has a common 11-factor (full or one column deleted). Its physical difference support equals G x (Z/11 minus the deleted column), for a nonempty ten-row XOR support G. In all 122 pairs the support has at least 20 sites.

First ambiguous pair at H=14: anchors 7/10 and 1/14, difference size 40. Another size-40 doubleton first appears by H=15: anchors 1/11 and 13/15. At H=16, anchors 3/4 and 1/16 give a size-20 doubleton, and none of the remaining 122 pairs has smaller support. The thresholds follow. Since all 600 normalized states occur by height 139, H beyond 139 cannot create a new trace or a smaller support. Together with the analytic fiber lemma, this proves the theorem.

## Cost comparison and provenance

At H=52 and r=5, fixed-before-spectrum cost is 17 from EC49FXX, versus post-spectrum cost 5 here. At H>=64 and r=10 the old fixed cost is 33, versus the adaptive cost 10. These are additional physical Boolean-site counts conditional on a supplied indexed spectrum. The side-channel read itself may carry nontrivial real resource cost.

The derived measurement index is a scalar auxiliary observer; the fiber quotient is sufficient for the declared conditional future Boolean readout, not a blanket lossless reduction of branch, height, anchor provenance, joint relations, or Heartbeat X6 state. No P000/ACTIVE worldview files were changed.

## Reproduction and next objective

Execute: node research_notes/portable_direct/EC49FXY_CONDITIONAL_SPECTRUM_ADAPTIVE_VERIFY.js

The self-contained program reconstructs genuine anchor states from the frozen integer predicate and verifies the 600/478/122 census, 66,000 original-C11 integer equalities, 15,180 H-by-r cases with H=2..139 and r=1..110, and explicit r-site selections for every feasible doubleton. Its emitted JSON is in EC49FXY_CONDITIONAL_SPECTRUM_ADAPTIVE_OUTPUT.json. This is an author crosscheck; no independent review has been claimed.

Next problem: price acquisition of the indexed spectrum as a declared physical observation operation, quantify overlap/reuse with subsequent Boolean readings and derive TOTAL measurement cost. A pure scalar quotient is not sufficient for a native-X6 transfer; retain branch, phase, anchor and provenance residuals and require an explicit transfer map. No shared CLAIM, Result, Review or task completion is asserted by this research note.
