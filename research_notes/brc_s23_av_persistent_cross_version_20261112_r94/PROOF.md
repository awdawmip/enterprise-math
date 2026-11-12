# R94 — Exact independent source/certificate versions and stable-champion transfer

Date: 2026-11-12. Status: author-side proof and executable prototype; independent review pending.
Scientific input pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Source lineage: R82, R86, R90–R93. Object: finite rational circular-source auxiliary BRC observer, with identities `(time,branch)`. The project-native X6 physical-world transfer is not part of this theorem.

## Definitions and theorem R94.1

Let `M_t(θ)` denote exact Boolean directed circular-arc membership at parameter θ under fixed observation signature `σ=(j,x,a,b)`. For source identity set `S`, `W_S(θ)=max{(t,branch)∈S:M_t(θ)}`, or `NONE` if empty, ordered lexicographically. A **certified** OUT rectangle `(σ,r,J,[p,q])` proves that every source time in the covered residue/time span is OUT for every **real** θ in the closed rational interval `J`.

Take any two finite version histories: source sets `S_i` and independently edited certified-box sets `B_j`. Replace R92's rebuilt certificate interval index with R93's path-copy persistent augmented AVL index, separated by `(σ,r)`, while keeping R90/R91/R92's exact membership oracle and winner recovery. **For every historical pair (i,j)**, the resulting output agrees with exact all-real classification of `W_{S_i}` on the query interval: `STABLE_NONE`, `STABLE((t,branch))`, or `CHANGES` with two rational parameter witnesses carrying distinct full identities.

**Proof.** R93's augmented AVL intersection search retrieves exactly the certified boxes whose parameter intervals intersect the requested closed interval, including endpoints. Nonintersecting boxes cannot contribute to R89's union-cover test. Thus R89's exact endpoint/open-cell-midpoint joint-cover decision equals a full scan's decision. A true cover only prunes source subtrees for which every relevant source time is certified OUT; R90/R91 point and full-interval subtree pruning are therefore sound. For every unpruned time R87's two-polarity procedure uses R90's complete rational critical-point partition, and R92 witness/absence caching retains its exact implication conditions. The winner observer retains complete branch identities; time-only membership caching does not identify branches. These steps hold for every independent version pair, so both edit histories commute at the mathematical query output. QED.

## Theorem R94.2 — Delta-dominance transfer

Suppose the old source version is already exactly proved `W_S(θ)=w` for every θ in `I`, where `w=(t,b)` is a full identity. For a new source version `S'`, assume (a) `w∈S'` and (b) every identity `e∈S'\S` with `e>w` is certified OUT throughout `I`. Then `W_{S'}(θ)=w` throughout `I`. If the old result is `STABLE_NONE`, deleting any identities and adding only identities certified OUT on `I` retains `STABLE_NONE`.

**Proof.** A retained old winner remains eligible. Deletion cannot introduce a higher qualified identity. Any added lower identity remains dominated; any added higher identity is ruled out by its exact OUT certification. Hence the maximum stays w. For old NONE, all old candidates were absent and all added candidates are certified absent. QED.

The necessary complete-identity condition has concrete counterexamples: deleting the stable champion can change the answer; inserting a larger branch under the same eligible time can change `(5,1)` to `(5,2)`. When the sufficient conditions fail the implementation returns an unresolved transfer, then falls back to exact classification; it does not assert change. For an old CHANGES witness pair, analogous independent pointwise checks on the two surviving winners and newly added higher identities suffice to preserve those witnesses.

## Implementation and exact coverage

The R94 implementation uses the **unchanged R82/R86/R90/R91/R92/R93 Python/Fraction sources** as dependencies. It implements a per-`(σ,r)` immutable R93 certificate-root map, exposes R92's `.overlapping()` API, retains all old source and certificate roots, tests R94.2's transfer conditions, and benchmarks heap, R91 scan, R92 rebuild and R94 persistent index.

A reproducibility archive `R94_RESEARCH_BUNDLE.zip` contains complete executable `check_r94.py`, unchanged dependencies, this proof and JSON evidence. The complete Python driver is also recorded in compressed base64 source form `check_r94.py.gz.b64` when available; decode using `base64 -d check_r94.py.gz.b64 | gzip -d > check_r94.py`. All oracle arithmetic uses exact `fractions.Fraction` and finite critical partition; timing uses `perf_counter_ns`.

Verification: 51 source/certificate histories built from 128 exact certified OUT boxes and 50 independent edits; 17 version classifications, 12 cross-version classifications, 25 valid delta-champion transfers, negative transfer tests (champion deletion and same-time branch increase), one NONE transfer, and a 75-update adversarial experiment with 75 independently verified CHANGES witness pairs. Both reference classifier and tested implementation use all-real rational partitions, not probabilistic samples.

## Measured resource trade-off (representative process)

For selected 17 cold historical queries, median milliseconds: ephemeral heap 1.7143; R91 all-box scan 2.5390; R92 rebuilt index query 0.7783; R94 persistent index query 0.7096. A single rebuild of the final R92 certificate index took median 0.5279 ms, separate from query timing. In 51 historical versions 149 unique R90 source AVL nodes and 291 unique R93 certificate AVL nodes remained reachable. Python recursive retained object graph estimates: 41,240 and 65,536 bytes respectively, excluding the separate certificate catalog, interpreter overhead and peak RSS.

In matched 22 source versions with nine excluded later times: R82 triple-index edit total 0.448 ms, R86 full-profile edit total 2.086 ms; R86 total query time 0.080 ms, R94 pruned classifier 4.824 ms, heap 9.928 ms. In 30 versions with 17 later excluded times: R82 edit 1.056 ms, R86 edit 4.619 ms; R86 query 0.179 ms, R94 query 10.348 ms, heap 24.861 ms. The R82 triple index itself is not a complete STABLE/CHANGES classifier, so its update numbers are not complete answer latencies.

These are single-process Python measurements with interpreter noise; the exact verification and node counts are separate evidence. They establish **two useful regimes**: full winner-profile R86 can amortize eagerly when an unchanged interval/signature is queried repeatedly, while persistent OUT certification and delta-dominance can reuse evidence across independent source and certificate edits. Next science: systematic mixed intervals/signatures and bit-complexity accounting, and a measured strategy selector choosing eager profile, indexed pruning or certified delta-transfer. Formal Task Owner/CLAIM/Review remains a separate current-control question.