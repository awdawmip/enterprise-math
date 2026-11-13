# R701 — Sharp four-port covariance obstruction and six-port S3/V29 holonomy transducer

Date: 2026-11-11 (Asia/Shanghai). Research scope: author-side TASK research, task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`, P000 V5. Status: **EXACT MATHEMATICS + FINITE EXECUTION; UNREVIEWED**. Formal native CLAIM/Result not asserted; frozen scientific pins unchanged.

## 1. Exact inherited carrier and new question

R700/R700b (research branch commit `8eacd161e0d54dbae467aecec2403a2bdf1f6111`) selected a positive-BRC candidate of 60 labelled return-path tokens divided into four bins with capacities `(24,18,6,12)`. It assigned each selected token to a single V29 `PASS(p_i -> p_(i+1 mod 4))` on a directed four-port ring. The count-only observer `u=(e-z,t-e,c-t,z-c)` plus total `s` reconstructs the four-bin histogram. R700b supplied exact boundary-`TRANSFER` correction.

V17 assigns active-triad-loop transport `h in S3`, V29 defines additive internal `PASS` counts and matched `TRANSFER` counts, and V39 declares the based-loop language with `h(gamma;r)=h(r) o h(gamma)`. The remaining question: can the R700 four-port event grammar support a faithful triadic-frame action, and can a typed V29 count carrier encode that non-Abelian holonomy without silently losing BRC source order?

Declare `S3` as permutations of the three slots `{0,1,2}`, represented by image tuples, with `a*b := a o b`; `e=(0,1,2)`, `tau=(1,0,2)`, `c=(1,2,0)`, `c2=(2,0,1)`. Initially map the four *candidate* source-bin labels to `S={e,tau,c,c2}`. This is a declared R700 transducer label, not an assertion that all E* branches or actual X6 channel ports are exactly these four groups.

## 2. Theorem R701.1 — a faithful S3 action cannot preserve the four-port directed ring

Let `C4^->` have vertices 0,1,2,3 and directed arcs `i->i+1 mod 4`. Its full automorphism group is the four rotations `C4`: an automorphism is uniquely determined by the image of vertex 0 and must preserve the chosen successor.

Any covariance action by the full `S3` on these port labels preserving the directed R700 event alphabet is a homomorphism `phi:S3->C4`. Since a 3-cycle has order 3 and C4 has no element of order 3, `phi(c)=1`. The transposition image has order dividing two, hence is identity or the half-turn. In particular there are exactly two such homomorphisms, neither faithful, and the 3-cycle acts trivially on the four ports.

This is a sharp obstruction to **faithful port-level S3 covariance while retaining that fixed directed-four-ring grammar**. It does not obstruct carrying extra S3 frame state alongside the ring; the next construction chooses a faithful port carrier instead.

Under simultaneous inner-frame conjugation, the original four-letter set `{e,tau,c,c2}` is also not closed: conjugation moves tau through all three transpositions. Its smallest conjugacy-stable extension is the full six-element `S3`. This gives a concrete minimal *label saturation* for arbitrary conjugation-reframe operations.

## 3. Construction R701.2 — six typed ports, ordered BRC word and covariant PASS

Choose a single declared X6 Cell anchor, without altering its six spatial axes. Define **six internal port labels** `p_q`, one for each group element `q in S3`; these are decorations of a Cell, not six additional spatial axes or final Cell addresses.

Retain a raw BRC word `w=(g1,...,gn)` with labelled token IDs, multiplicities and event order. Define a candidate transition with active frame state `q`:

`STEP_g(q): PASS(x;p_q -> p_(g*q)), followed by q' := g*q.`

The V29 primitive count operation `PASS(a->b)` increments one nonnegative `M[a,b]` entry; a diagonal PASS for `g=e` is syntactically allowed in the V29 counting grammar, subject to any additional native Link/Port admissibility constraints. The **frame update** is an explicitly proposed companion law, not a consequence of V29 alone. Serial composition yields

`q_n = g_n * ... * g_1 * q_0`.

For `q0=e`, this is exactly V39's **declared group-composition convention**. Every generator step is labelled by its original BRC branch and remains available to source-sensitive observers.

The right gauge action `R_k(q)=q*k^(-1)` commutes with every fixed-label step:
`R_k(g*q)=g*R_k(q)`.
It is a faithful action on the six ports. For simultaneous conjugation frame changes `C_k(q)=k*q*k^(-1)`, `C_k(g*q)=C_k(g)*C_k(q)`. This second covariance law uses the six-label conjugacy-closed alphabet. Hence the same construction supports both a fixed-label right-gauge action and a conjugating-label active-frame action, with separately stated semantics.

Six ports are sufficient and are minimal **when each distinct S3 frame must itself have a distinct port label**. Faithful actions on fewer points are a different design problem; the predictive state minimality below is independent of that encoding choice.

## 4. Theorem R701.3 — exact telescoping V29-to-S3 recovery

Let `M` be the cumulative nonnegative six-port PASS ledger produced by **one contiguous, path-consistent** STEP word, with fixed known initial frame `q0`. Write `delta_q` for the basis-vector port incidence and `u_int=(M-M^T)1`.

Each step `q_(i-1)->q_i` contributes `delta_(q_(i-1))-delta_(q_i)`. Therefore

`u_int=sum_(i=1)^n(delta_(q_(i-1))-delta_(q_i)) = delta_(q0)-delta_(qn).`

For `q0=e`, `u_int=0` means `qn=e`; otherwise the unique negative port component is exactly `qn`. Thus the six-port internal contrast alone recovers the complete six-valued S3 holonomy `h=qn` for this declared event language, for **every finite word**.

For a known arbitrary base frame, decode the endpoint and compute `h=qn*q0^(-1)`. If matched boundary transfers have been recorded in V29 and leave this frame STEP law unchanged, use the R700b correction
`u_int=u_observed-Rin+Rout`;
the same decoder then applies. The incoming/outgoing count vectors remain nonnegative stored ledgers. If future operations query independent network cycle current `j`, keep `j` alongside the decoded `h` as required by V39.

Why this does not contradict V37/V38: their coarse **network-current** or untyped occurrence histograms allow event orders with the same counts but distinct holonomies. Here the **port address of each PASS depends on the previous frame**. That path-consistency law makes the final signed port contrast encode the endpoint. A free multiset of independently emitted four-ring arcs has no such law. Source-order is still retained for more demanding raw-Path or provenance futures.

## 5. Sharp collision and repaired observation

Consider two positive BRC token words `w1=(tau,c)` and `w2=(c,tau)`. Both select exactly one tau and one c token, so the original R700 four-port ring has the **same complete matrix M**, not just the same `(u,s)`. Both have histogram `(0,1,1,0)`, total `s=2`, and four-port contrast `(0,1,0,-1)`.

Yet V39 sequential frame composition gives:
`h(w1)=c*tau=(2,1,0)`;
`h(w2)=tau*c=(0,2,1)`.
They are different. The six-port STEP words have different directed PASS arcs and different endpoints; their corrected internal contrasts recover those endpoints. This is the minimal two-token noncommuting witness for why the old four-ring count transducer cannot alone serve frame-sensitive futures.

## 6. Theorem R701.4 — six future-return prediction classes

Use the declared alphabet `S={e,tau,c,c2}` and futures consisting of an arbitrary finite word from S, followed by a single Boolean observation `[final frame = e]`. All six S3 frames are reachable from the base, and each inverse `q^(-1)` has a representing future word of length at most **two** in S. For two different current frames q,r, append a word representing `q^(-1)`: it returns q to identity but not r.

Thus the Myhill–Nerode predictive equivalence relation has exactly **six classes**, with optimal fixed-length binary state memory `ceil(log2 6)=3 bits`. A family of at most two-letter return probes already separates all six; this is a stronger observation than querying the current holonomy directly. The result concerns deterministic future execution of the declared STEP alphabet.

## 7. Native X6 active-triad origin of the S3 macro generators

The source V17 shared-axis replacement connection supplies based loops in `J(6,3)`. Using **0-based native axis labels** within the full X6 world, take

`A:012 -> 013 -> 023 -> 012` and
`B:012 -> 023 -> 123 -> 012`.

Transport the three frame slots by preserving shared-axis slots and giving the entering axis the leaving axis's slot. The exact result in the declared *slot-to-axis tuple* convention is
`h(A)=(0,2,1)`, `h(B)=(1,0,2)`; their products generate S3. All six frames arise from concatenations of at most **three** A/B based loops (at most nine active-triad switches). V36's existing constructive directed Cell-ring theorem provides an autonomous candidate network realization for each such cyclic active-triad word under its V20 update assumptions.

This is an actual V17 active-triad *conditional model* realization of all required group holonomies. The six-port V29 STEP **transducer** is a separate candidate interface: binding its PASS records, dependency order and admissible physical X6 Link/Port connectivity to those V36 macro loops remains the precise native integration question. Distinguish slot-to-axis tuples from inverse axis-to-slot permutation conventions when comparing historical loop listings.

## 8. Exact verifier and evidence

File `R701_S3_PORT_LIFT_VERIFY.js` implements finite S3 permutations, four-cycle automorphisms, V17 axis-slot transport, right/conjugation covariance, all source-token words of length 0..6, V29 nonnegative PASS ledger increments, telescoping endpoint decode, matched boundary correction, exact two-token collision and return-future distinguishability. It was actually executed as a self-contained JavaScript checker; an independent local Python checker was also run on the same declared objects.

Execution: `R701_S3_PORT_LIFT_EXACT_PASS`.
Coverage: 4 automorphisms; 432 group covariance equations; 5,461 words; 32,766 path/gauge comparisons; 12,276 one-in/one-out boundary-pair corrections; six predictive classes with length-two witnesses. Every assertion passed. The mathematical theorem's arbitrary-word scope follows from group composition and the telescoping proof, not from finite-length testing.

Source references (all exact historical provenance, not Foundation promotion):
- `p000_reality_foundation.json` V5 and `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` at current Source revision.
- `research_notes/portable_direct/2026-11-11_R700_V29_BRC_four_ring_contrast_recovery.md` at `8eacd161e0d54dbae467aecec2403a2bdf1f6111`.
- `research_notes/portable_direct/2026-11-11_R700b_V29_matched_transfer_contrast_repair.md` at the same commit.
- `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md` (Git blob `6849ebd3fc776fb7da3b46627376490aba3dad99`).
- `research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`, `research_notes/X6_ACTIVE_LOOP_TO_DIRECTED_RING_REALIZATION_V36_20260906.md`, and `research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md` (V39 blob `8151d0b6a4b65225b93d858bbc8a5d7037bf9cef`).

## 9. Precise next discriminating experiment

Bind one generated A/B macro loop to one concrete V36 multi-Cell packet and its V29 network transfer ledger. Specify an allowed Link/Port morphism from the six **internal frame labels** to actual per-Cell port objects and an event order that implements `PASS(q->gq)` without injecting an externally chosen frame update. Check that its actual returned frame matches V17's h, V29's matched TRANSFER graph and V39's based loop pair `(j,h)` under **one and the same** path history. If not, retain the precise failed Link/Port constraint and test a derived transducer tied to actual V20 updates.

The mother's required primitive `TRIADIC_CLOSURE_E` and full force/path dynamics remain open; this research supplies an exact observer/interface candidate and a faithful-port covariance obstruction. No P000, ACTIVE worldview, task publication or mathematical admission state is changed.
