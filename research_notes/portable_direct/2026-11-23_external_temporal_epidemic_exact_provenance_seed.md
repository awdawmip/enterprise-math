# Temporal-contact contagion: exact rational provenance witnesses (2026-11-23)

**Status:** AUTHOR-CHECKED EXACT FINITE CASES; NOT_REVIEWED. This document is an external-model mathematical seed, not an Enterprise Math Result, BRC implementation, native X6 physical model, Task publication, or empirical epidemiological estimate.

## Problem and assumptions

Seek a finite-horizon, task-query-specific *provenance-preserving* compression and positive-rational BRC interface for temporal spreading, while testing whether it offers a demonstrable benefit over established temporal-graph message passing / dynamic programming. External contact event `(t,u,v)` means the directed infectious attempt `u -> v` is made only if `u` is already infected and `v` is susceptible at that event. Attempts conditionally independent with exact probability `p=1/2`. State includes infected set and ordered successful-transmission source record; no recovery in these two **SI** seeds. It is not a calibrated SIR epidemic.

## Exact witness A: event order affects infection

`V={A,B,C}`, initial `I={A}`, two contacts, `p=1/2`.

* Order `[(A,B),(B,C)]`: exact terminal atoms `(I={A},sources=[]):1/2`, `({A,B},[(A,B)]):1/4`, `({A,B,C},[(A,B),(B,C)]):1/4`; therefore `P(C infected)=1/4`.
* Reverse order `[(B,C),(A,B)]`: atoms `({A},[]):1/2`, `({A,B},[(A,B)]):1/2`; therefore `P(C infected)=0`.

The two schedules have identical time-aggregated contacts but distinct time-respecting reachability. The witness rejects **static-aggregation-as-complete-state**, not correctly specified temporal-network models.

## Exact witness B: infection origin is not determined by final status

`V={A,D,B}`, initially `{A,D}` infected and `B` susceptible. Each of the two listed contacts makes a `p=1/2` attempt only when `B` remains susceptible.

* `[(A,B),(D,B)]`: `P(B remains susceptible)=1/4`; `P(source=A)=1/2`, `P(source=D)=1/4`.
* `[(D,B),(A,B)]`: `P(B remains susceptible)=1/4`; `P(source=A)=1/4`, `P(source=D)=1/2`.

Both have `P(B infected)=3/4`, but conditional on infection `P(source=A | infected)` is respectively `2/3` and `1/3`. The final infection bit cannot answer the source query. A single final-bit observation need not distinguish the two histories.

## Reproducible exact calculation

An exhaustive transition on a rational-weight map `D[(I,h)]`, initially `D[({A},())]=1` (or `I={A,D}` for B), visits each contact in declared order. For an applicable attempt split weight `w` into `w(1-p)` at unchanged `(I,h)` and `wp` at `(I∪{v},h||((u,v),))`; for an inapplicable attempt carry `w` unchanged. Use reduced numerator/denominator arithmetic and merge only identical **full** keys. The final atom lists above are exhaustive and each sums to one; they were independently re-enumerated using Python `fractions.Fraction` in the authoring conversation. Scope: 2 events / 3 nodes only. No generalized proof of BRC efficiency follows.

## Reusable BRC research gap (not yet executed)

Represent the full event-labelled rational path measure, e.g. `(ordered-event-word, transmission-source-word, full SI/SIR state trace, rational weight)`, and explicitly define the typed projection to the existing BRC positive-weight carrier / port operators. Fix query language: terminal infection, time-bounded contact-respecting spread, first-source attribution, conditional-on-infection source, and selected future source-aware interventions. A proposed quotient `q` is safe **only** for its declared future operators and readouts, with a fiber-constancy / transition-compatibility proof or a minimal distinguishing witness. Compare explicit Fraction enumeration, temporal-network conditional DP, published contact-based or pair-based message passing, and genuinely implemented BRC; report provenance storage, state conversion, numerator-denominator growth, setup, update, query, recovery and certificate-check costs. First evaluate SI witnesses; SIR recovery requires a separately declared rational recovery law and additional cases, not an implicit assumption.

Existing Enterprise Math tasks already cover abstract safe quotients and CCF / temporal reliability, notably `RS-BRC-RESTRICTED-PORT-QUOTIENT-20261005` and `RS-EXT-BRC-CCF-TEMPORAL-RELIABILITY-20261116`. No new abstract quotient theorem, epidemiological discovery, biological claim, or speedup is asserted. A worthwhile distinct output must concern **time-stamped contact-event path support, infection-source intervention queries, and fair comparison to the external epidemic solvers**, beyond the reliability task. If this yields no measurable provenance/certificate/cost advantage, report a negative transfer result without expanding the application.

## External prior art (explicit baseline)

* Pan & Saramäki, *Path lengths, correlations, and centrality in temporal networks*, Phys. Rev. E 84, 016105 (2011): https://doi.org/10.1103/PhysRevE.84.016105 — time-respecting temporal paths.
* Koher, Lentz, Gleeson & Hövel, *Contact-Based Model for Epidemic Spreading on Temporal Networks*, Phys. Rev. X 9, 031017, published 2019-08-02: https://doi.org/10.1103/PhysRevX.9.031017 — contact-based dynamic message passing; temporal trees and general graphs.
* *A systematic framework of modelling epidemics on temporal networks*, Applied Network Science (2021): https://doi.org/10.1007/s41109-021-00363-w — temporal SIR pair-based comparison.

**Source-exposure and authority:** informed TASK scientific seed, not CLEAN FREE Phase A. P000 remains protected, external epidemic models stay external, no native X6 or physical correspondence asserted. Formal shared task publication / Researcher-ID / status-machine readback are separate and must be verified before claiming any READY/CLAIM/owner state.
