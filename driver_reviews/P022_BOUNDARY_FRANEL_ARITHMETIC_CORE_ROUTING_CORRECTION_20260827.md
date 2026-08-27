# Driver Review Correction — P022 Boundary Franel Arithmetic Core Routing

Status: `DRIVER_FINAL / MATHEMATICAL_ACCEPTANCE_PRESERVED / ROUTING_CORRECTED / TYPED_SPLIT`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Result: `RR-8323CFDCB99F7832F51F`

Prior immutable review: `DR-710AC1A4CB63750F94CB`

Interim publication-resolution flow: `PI-P022PUB-20260827-01 / PS-P022PUB-20260827-01`

## 1. Correction scope

The mathematical disposition of the prior review is preserved:

`RR-8323CFDCB99F7832F51F = ACCEPTED_WITH_NARROWING / EXACT_REDUCTION`.

This correction changes only destination and portfolio routing. It does not withdraw, strengthen, or re-prove the accepted reduction

\[
q\mid F_{6m}
\iff
R_m(q)\equiv0\pmod q.
\]

The current-main resolution that selected `TP2-2346F5D3E731ED56DB0A` as operational is also superseded only as a routing conclusion. All three legacy publications remain immutable research evidence.

## 2. Why the prior destination is not sufficient

The prior review routed fixed-kernel nonvanishing to

`TP2-2346F5D3E731ED56DB0A / RS-P022-OBSERVATION-HISTORY`

and described that publication as a live line.

That routing is not exact for two independent reasons.

First, the publication's taskbook hard target is the composite Franel equal-depth mechanism:

`P022_COMPOSITE_FRANEL_ESCAPE_CLOSED_OR_MINIMAL_EXACT_EXCEPTION_FROZEN`.

It consumes the first-reentry kernel classification as an input, but its next action attacks equality of positive Franel depths through forced-midpoint first jets and harmonic pairing. It does not make all-parameter nonvanishing of the fixed kernel `R_m(q)` its hard target.

Second, the shared legacy task id had already been claimed for `TP2-DE338F269CA11E9BC01B` at `2026-08-27T16:39+08:00`. The later attempted claim for `TP2-2346F5D3E731ED56DB0A` occurred at `16:48+08:00` while the first lease was live. Under the canonical single-task reducer, that later shared-task claim does not establish an independent live execution lineage. The publication remains valuable retained evidence, but it is not the correct destination for the fixed-kernel theorem.

## 3. Correct typed destinations

The two open arithmetic residues are therefore split.

### A. Fixed first-reentry kernel

Typed task:

`RS-P022-FRANEL-FIRST-REENTRY-KERNEL-NONVANISHING`

Publication:

`TP2-18D80E295208AC91EB70`

Hard target:

`P022_FIXED_TRUNCATED_FRANEL_KERNEL_ALL_M_NONVANISHING_PROVED_OR_REFUTED`

This task alone owns proof or refutation of

\[
R_m(q)\not\equiv0\pmod q
\]

for the admissible `q=18m-1`, `12m-1`, `12m+1` prime constellation.

### B. Composite equal-depth escape

Typed task:

`RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE`

Publication:

`TP2-E4537008BB8B0CCFF88F`

Hard target:

`P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE_CLOSED_OR_MINIMAL_EXCEPTION_FROZEN`

This task owns the separate p-adic first-jet/equal-depth mechanism recovered in `TP2-2346F5D3E731ED56DB0A`.

The bounded forced-midpoint route `TP2-D78DBA0243911E0363FA` remains retained evidence and receives no duplicate successor.

## 4. Additional independent pressure

A Driver-side clean reconstruction extended the finite pressure test to `q<200,000` without importing P022 implementation modules:

- admissible twin-boundary candidates: `254`;
- candidates in complete-escape classes `17,35 (mod 72)`: `131`;
- zero-status mismatches among `F_(6m)`, the integer kernel `S_m`, and the reverse kernel `R_m(q)`: `0`;
- observed zeros: `0`.

This remains finite regression only and does not alter the accepted exact-reduction scope.

## 5. Final control disposition

`DR-710AC1A4CB63750F94CB = MATHEMATICALLY_ACCEPTED / DESTINATION_SUPERSEDED`.

`PI-P022PUB-20260827-01 = RETAINED_HISTORICAL_CONTROL_EVIDENCE / ROUTING_CONCLUSION_SUPERSEDED`.

`MATHEMATICAL_DISPOSITION = PRESERVED`.

`LEGACY_OPERATIONAL_PUBLICATION = TP2-DE338F269CA11E9BC01B`.

`CURRENT_FIXED_KERNEL_DESTINATION = RS-P022-FRANEL-FIRST-REENTRY-KERNEL-NONVANISHING`.

`SIBLING_TYPED_FRONTIER = RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE`.

`TP2-2346F5D3E731ED56DB0A = RETAINED_COMPOSITE_EQUAL_DEPTH_EVIDENCE`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.
