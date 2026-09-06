# X6 internal/channel V3R: triadic-state-induced C3 channel circulation

Status: `FREE_RESEARCH / EXACT CONDITIONAL CLASSIFICATION / CORRECTED 2026-09-06 / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Depends on:
- corrected `X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md`;
- `X6_AXIS_CHANNEL_FRAME_GAUGE_AND_FLAT_TRANSPORT_V2_20260906.md`;
- `X6_SIGNED_INTERNAL_Q_GAUGE_CORRECTION_V5_20260906.md`.

## 1. Question

V2 shows that bare pure spatial translation cannot generate a nontrivial deterministic channel permutation under translation invariance and full unsigned `S6` covariance. Does the already-existing triadic internal state supply enough relational structure to permit nontrivial local channel dynamics?

Yes.

## 2. Residual symmetry of an ordered active triad

Fix a global axis-channel gauge frame and a reference ordered unsigned triad

`tau_0=(1,2,3)`.

This note classifies a **sign-blind** channel permutation rule; signed force information remains separately typed.

The subgroup fixing `tau_0` pointwise is the `S3` permuting inactive channels `{4,5,6}`.

An `S6`-equivariant local rule `tau -> U_tau` therefore has

`U_tau0 in C_{S6}(S3_inactive)`.

The centralizer is exactly `S3_active`, fixing the inactive channels pointwise. Hence six deterministic active-block permutations are symmetry-allowed.

## 3. Cyclic token-origin invariance reduces S3 to C3

The triples

`(a,b,c)`, `(b,c,a)`, `(c,a,b)`

represent one oriented cycle with different token-origin conventions. Requiring the unsigned channel rule to ignore that arbitrary origin means the chosen active permutation must commute with `(a b c)`.

The centralizer of this C3 in the active S3 is C3 itself.

Thus the cyclic-origin-invariant rules are exactly:

- identity;
- forward 3-cycle;
- reverse 3-cycle.

If nontrivial circulation is required, precisely two chiral choices remain.

## 4. PF-10 passage is exactly the nontrivial C3 solution

For one ordered signed triad frame with underlying axes `(i0,i1,i2)`, the instantaneous unsigned PF-10 passage is

`i0 -> i1 -> i2 -> i0`.

This is one of the two nontrivial C3 solutions above. Reversing the oriented triad gives the inverse cycle.

Therefore the directed PF-10 passage is symmetry-classified rather than an arbitrary extra decoration within the declared sign-blind permutation model.

## 5. Corrected signed internal update still conserves passage orientation

The historical arbitrary-sign shorthand

`R(d0,d1,d2)=(-d1,-d2,-d0)`

is superseded.

For the canonical oriented generator and a frame

`F=((i0,i1,i2),(s0,s1,s2))`,

the correct tokenwise update is

`R_can(F)=((i1,i2,i0),(-s0,-s1,-s2))`.

After forgetting signs, the axis tuple still undergoes only the cyclic reindexing

`(i0,i1,i2)->(i1,i2,i0)`.

Therefore the unsigned directed passage cycle is unchanged:

`U_{R_can F}=U_F`.

So all unsigned C3 conclusions of the original V3 remain valid after the signed correction.

Under independent sign-frame changes the canonical signed generator transports inside the four-twist bundle from V5; every twist has the same unsigned 3-cycle projection.

## 6. Exact quotient hierarchy

For the 960 full ordered signed triad frames:

- active unsigned support: 20 states;
- directed unsigned C3 passage: 40 states;
- each passage has a 24-element full-frame fiber.

Those 24 frames split further into four corrected C6 orbit sectors, each of length six. The four sectors encode relative signed/twist information invisible to unsigned channel circulation.

Thus

`UNSIGNED_C3_CHANNEL_CIRCULATION != COMPLETE_SIGNED_INTERNAL_STATE`.

## 7. Spatial transport versus internal channel evolution

Under V2:

- pure spatial channel parallel transport is identity after one global gauge choice under the full-symmetry model;
- active triadic internal state permits a nontrivial C3 permutation inside the three active channels;
- inactive channels remain fixed.

So nontrivial channel dynamics is sourced by internal relation state rather than bare spatial translation.

## 8. State-dependent channel holonomy

For a sequence of internal triadic events, cumulative unsigned channel transport is the ordered product of their C3 permutations.

Repeated events on the same oriented active triad give an exact C3 period. Changing active triads can give noncommuting products and genuine channel holonomy sourced by internal history.

Order/provenance must therefore remain unless a safe quotient is proved.

## 9. Relation to frame/channel V4 and all-20 A6 integration

Every corrected signed generator twist has the same positive-axis permutation projection `rho_S`. Hence the existing minimal frame/channel coupling

`U_S = pi(Q_S)=rho_S`

and the exact sequence

`1 -> (C2)^6 -> R_triad -> A6 -> 1`

remain unchanged.

Likewise the common `A6` skeleton shared by triadic positive-frame dynamics, unsigned channel circulation and orientation-preserving all-20 chart transport is unaffected.

## 10. Current V3 frontier

Closed under the declared sign-blind permutation model:

- ordered active triad permits exactly S3_active channel permutations;
- cyclic-origin invariance reduces these to C3;
- exactly two nontrivial chiral circulations remain;
- PF-10 directed passage realizes one such circulation;
- passage orientation is invariant along the **corrected** signed internal C6 orbit;
- channel holonomy can arise from changing internal triadic states.

Open:

- sign/twist-sensitive channel laws;
- amplitude/weight-dependent mixing;
- neighboring-Cell channel exchange;
- physical calibration/observable interpretation.

No Foundation promotion is made.
