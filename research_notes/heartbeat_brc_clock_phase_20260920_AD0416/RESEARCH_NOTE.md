# Heartbeat World BRC: shared global clock versus local phase residual

Status: `RESEARCH_CONSTRUCTION / EXECUTED_EXACT_FINITE_QUOTIENT / NOT_FOUNDATION`
Date: `2026-09-20`

## Typing

In Heartbeat World the global time coordinate is separately typed. If a heartbeat program has known phase `phi(t)=t mod 6`, that phase can be supplied by the external time port; it need not be copied into every BRC branch.

A distinct question is local desynchronization. Let a local six-channel environment mask be `m in {0,1}^6` and let `delta in Z/6Z` be the local frame's phase offset relative to the shared clock. The raw finite state has 64*6=384 possibilities. Define the globally aligned physical mask

`a = R^delta m`.

The gauge step `G(m,delta)=(R m,delta-1)` leaves `a` unchanged. It changes representation, not the aligned environment.

## Exact 384 -> 64 gauge quotient

Every aligned mask `a` has exactly six raw representatives, one for each delta, so the gauge action is free and the 384 states split into exactly 64 six-element gauge orbits.

Executing the existing T6 predictor with current observation `a` and future actions consisting of the gauge step plus globally framed rotations, reflections and an absolute-slot-0 gate gives profile

`(64,64,64,64,64,64)`.

Thus the aligned 64-state representation is already stable at horizon zero for this future language. The local phase offset is genuinely redundant in this scoped setting.

The effect-valued BRC certificate agrees. A globally framed packet that translates along global `e1` is safe on the 64 aligned-mask classes. A packet whose translation axis is selected by the local offset `delta` rejects that quotient and exact control refinement returns all 384 states.

## 13 -> 64 -> 384 future-information ladder

Use the earlier orientation-blind shape observer `O=(occupied count, adjacent occupied-pair count, opposite occupied-pair count)` on the globally aligned mask.

- With only D6 symmetry-safe globally framed futures, T6 gives `(13,13,13,13,13,13)`.
- Add a globally phase-addressed absolute-slot-0 gate while retaining absolute rotations/reflections: `(13,32,52,63,64,64)`. The physical aligned orientation becomes necessary, but the local phase offset remains gauge.
- Add a local-slot-0 toggle that acts in the local frame: `(13,113,353,383,384,384)`. All local phase offsets become distinguishable; stable count is 384 at depth 4.

Therefore global time phase and local phase residual must be typed separately. A shared exogenous clock can serve all branches once, while branch-specific desynchronization is real state whenever later actions can use it.

## General shared-clock factorization

Let legal events satisfy `p=phi(t)` for a deterministic globally available phase program, and suppose the observer and every declared future operation use `p` only through the time port `t`. Then the projection `(x,t,p)->(x,t)` is lossless on legal states because `p` is reconstructed as `phi(t)`, and every future operation descends.

If two legal states can share `(x,t)` but carry different local phase residuals `delta`, and any declared future observer/effect distinguishes those residuals, the projection deleting delta is unsafe. The local-axis packet above is a finite exact witness.

For a uniform raw 384-state model, the local-offset repair carries exactly `log2(6)≈2.585` conditional bits beyond the 64-state aligned mask. This is finite Shannon accounting, not a fixed storage implementation or a physical information law.

## Validation and boundary

The existing predictive quotient and ControlPacket implementations were reused. Previous 18 tests plus three new phase tests pass: 21/21. The experiment is a six-channel diagnostic environment, not full twelve-direction occupancy; it makes no production Nollm, physical synchronization, semantic-memory, independent-review or Foundation claim.
