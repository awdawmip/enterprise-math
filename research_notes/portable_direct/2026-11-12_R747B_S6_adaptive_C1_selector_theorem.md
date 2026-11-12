# R747B — S6 symmetry obstruction and optimal adaptive C1 selector

Date: 2026-11-12. Status: author-side **conditional mathematical proof** with executed exact finite incidence audit, not independently reviewed or admitted as a native Result.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142; parent PO-X6-UPPER-STRUCTURE-20260906.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R747 at ed44c4e1f6c7bd2adc545fa60047619f71a59992, research_notes/portable_direct/2026-11-12_R747_C1_framed_port_connection_exact_S3_holonomy.md. The normative current-read overlay is separate from frozen science.

## Question and typed scope

R747's retained-slot C1 edge update is unique, reversible, S6-covariant, and descends from a *framed* triad to its oriented wiring W for **externally specified** edge paths. The new question is whether an adaptive selector of each next edge can respect exact S6 symmetry while preserving that orientation-only quotient.

Let A={0,1,2,3,4,5}. Each signed port is (i,s), i in A and s in {+,-}. A frame at fixed Cell and positive equal quantum is F=(p0,p1,p2), with three **different underlying axes**. Its directed cyclic wiring is W(F): p0 -> p1 -> p2 -> p0. Write rho(F)=(p1,p2,p0). Exactly three cyclic frames represent one W.

A strict one-port replacement edge e=(p,r) chooses an existing port p and a signed new port r on an axis unused by F. There are precisely 3*3*2=18 legal edges per frame, not merely new ports on the old removed axis with opposite sign. T_e keeps two surviving signed ports in their original named slots and inserts r in the vacated slot. S6 permutes axis labels, preserving signed port incidence and named slots. rho cyclically changes the slot naming.

The observation and future-operation class here comprises oriented wiring W, its signed-port successor relation, and optionally the **chosen source edge as retained BRC provenance**. It excludes any named-slot readout unless the R747 anchor is restored. T_e is an abstract R747 **candidate incidence update**. No V29 PASS, V39 Cell/Link/Port event, TRIADIC_CLOSURE_E license, or physical probability law is asserted.

## Theorem 1 — No deterministic unassisted S6-equivariant strict selector

There is **no** deterministic function f assigning one legal edge to every framed C1 state and satisfying f(sigma F)=sigma f(F) for every sigma in S6.

**Proof.** Fix F. Every permutation of its three unused axes fixes F exactly, including its three named slots. These permutations form an S3 subgroup of the frame stabilizer. If f(F)=(p,(j,s)), then j must be one of those unused axes. A three-cycle of the unused axes fixes F and changes j. Equivariance would require f(F) to remain unchanged, a contradiction. This obstruction persists if f depends only on W. It disappears if one supplies an external covariantly transformed unused-axis selector or relaxes exact S6 equivariance; neither is silently assumed. QED.

## Theorem 2 — Sharp support bounds and explicit repair

Consider a probability kernel on legal edges that is S6-equivariant. A stabilizer of a state must preserve the edge probabilities; hence every positive-probability support contains an entire stabilizer orbit.

**Frame-observed case.** The stabilizer of a named frame fixes all used axes and permutes the three unused axes, so is S3. For each choice of removed port p and new sign s, its edge orbit has size 3. Thus the smallest possible support is **3**. Fixing slot 0 and choosing the new positive port uniformly on one of the three unused axes attains the bound (but uses the named slot and therefore is not W-quotient-safe).

**Orientation-only W-observed case.** The stabilizer of W contains the S3 on unused axes. If the three old signs are identical, it also contains the C3 of cyclic permutations of used axes preserving the directed cycle. The stabilizer is C3 x S3 (order 18), with two edge orbits of size 9 (one for each new sign). If the old signs are mixed, no nontrivial cyclic permutation preserves the signs; the stabilizer is S3 (order 6), with six edge orbits of size 3. Consequently the **pointwise optimal support** of an S6-equivariant orientation-only kernel is

| Old signs | Stab(W) | Orbits on 18 edges | Minimum support |
|---|---|---|---|
| +++ or --- | C3 x S3, order 18 | 9,9 | 9 |
| Every mixed pattern | S3, order 6 | 3,3,3,3,3,3 | 3 |

**Construction of one globally defined optimal kernel K.** Fix the new port's sign to +; this selects a sign, *not* a preferred spatial axis. When all old signs agree, pick any old port p and any unused axis independently uniformly: nine edges with exact rational weight 1/9 each. When the signs are mixed, remove the uniquely identified minority-sign old port and pick an unused axis uniformly: three edges with exact rational weight 1/3 each. This rule depends only on the signed port set recoverable from W and is S6-equivariant. Each displayed lower bound is therefore attained. QED.

These support bounds concern distinct signed source edges, not implementation random bits or physical event frequencies. They are exact finite group-action results.

## Theorem 3 — Adaptive all-finite-horizon quotient, with pathwise provenance coupling

Let K(W,de) be a Markov edge-selection policy depending only on the current oriented wiring, with every chosen edge legal. The retained-slot update yields an exact quotient from F to W for all finite adaptive horizons, even though the selector chooses its next edge as a function of the evolving W.

**Proof.** F and rho F have identical signed port sets, hence identical legal edge sets and the same W. Couple their edge choices by selecting the same e under the common kernel. R747 proves T_e(rho F)=rho(T_e F); therefore the successor states have the same oriented wiring and the same selected signed edge identity/provenance. Repeat the coupling inductively. This proves identical entire W and chosen-edge histories for any finite horizon. The explicit optimal kernel from Theorem 2 qualifies and is S6-equivariant. QED.

For deterministic selectors and the exact W-valued one-step readout, the criterion is sharp: a selector f descends to W **iff** f(rho F)=f(F) on every cyclic fiber. Distinct legal replacements of a fixed signed port set yield distinct *new signed port sets*, hence distinct W readouts, proving necessity. Sufficiency follows by rho-commutation and induction. This quotient criterion is separate from the stronger S6-covariance obstruction in Theorem 1.

A future named-slot query still distinguishes the three cyclic frames, so R747's three-valued anchor repair remains necessary and sufficient in that expanded observation class.

## Reproducible finite audit

The companion R747B_SYMMETRIC_SELECTOR_VERIFY.py executes *exact incidence and finite-permutation checks* (no physical dynamics, pi, trigonometry, native residual arithmetic or stochastic sampling). Actual output: R747B_SYMMETRIC_SELECTOR_RESULTS.json with status PASS.

- Enumerates all 960=6*5*4*2^3 signed frames and 320 distinct oriented wirings.
- Checks all 17,280=960*18 cyclic retained-slot commutation cases and policy invariance under cyclic slot rotation.
- The eight ordered-sign patterns represent all framed S6 orbits. On each it checks 720 permutations times 18 legal edge updates, totaling 103,680 covariance cases, plus 5,760 policy covariance cases.
- Directly enumerates frame and W stabilizer edge orbits: sizes [9,9] for the two all-equal patterns, and [3,3,3,3,3,3] for all six mixed patterns.
- The all-horizon theorem follows from induction, not extrapolation of the finite checks.

BRC use: the carrier is R747's signed C1 framed/incidence branch grammar; the observer is the exact oriented wiring plus optional selected-edge provenance; the contraction fiber and future operations are explicitly stated. No positive branch count is treated as force cancellation.

## Open interface question and preservation

R747's six S3 holonomies and fixed-edge orientation quotient remain unchanged. This theorem adds a minimal symmetry-preserving autonomous selection mechanism (three or nine exact candidate branches) and a deterministic-selector obstruction. The next discriminating task is to test **actual** frozen V29/V39 Cell/Link/Port guards for (a) one-port replacement and retained TRIADIC_CLOSURE_E and (b) R744's first-hop reverse PASS, using source-preserving branch records. A failed native guard is a result about that particular candidate operation, not a P000 revision.

The separate Source typed continuation request r747-managed-typed-prepare-20261112-v1 was rejected as CANONICAL_REJECTED: OUTPUT_PREFIX_NOT_ALLOWED. This author-side note is not a replay, substitute CLAIM, Source Result, Driver review or native event authorization. Preserve exact prior identity EM-X6-BD7DE5 / RA-2B88F5E322CC012B6E3F33F8 without asserting active ownership.
