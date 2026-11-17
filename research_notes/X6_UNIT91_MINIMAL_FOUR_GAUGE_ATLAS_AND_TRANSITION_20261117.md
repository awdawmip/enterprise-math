# X6 Unit91 — minimal four-chart sign-gauge atlas for all 20 named triadic generators

Date: 2026-11-17. State: **AUTHOR-EXACT / FINITE-EXECUTED / SOURCE-CALL-SITE-INSPECTED / UNREVIEWED / NOT_ADMITTED**. Parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`, Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Scientific pins P000 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; named signed BRC source blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.

## Motivating real source consumer distinction

Unit90 inspected the actual generators `q_triad` (all three selected images negative) at `experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py`, blob `c446d0327f9bf643d5796348ba46cafe96d2915d`, and the one-negative `triad_generator` at `research_checks/20261112_x6_star_triad_group_brc_convolution.py`, blob `50cccf09b5dd83cc592ba36db5bc9e14941ce0ce`. Under a global named-axis-preserving sign gauge `D_s(e_a)=s_a e_a`, the two generators coincide by conjugation on a particular sorted triple `i<j<k` exactly when `s_i=s_k=-s_j`. A **single** chart can cover all four actually used FCC STAR triples, but no chart covers all 20 possible triples.

This unit resolves the next exact question: **how many such gauge charts are minimally sufficient to cover all 20 named triads without changing the six-axis label alphabet?**

## Finite exact minimality theorem

Let `T=C({0,...,5},3)`, so `|T|=20`. For a sign chart `s∈{±1}^6`, define its compatible subset

`C(s)={ (i,j,k)∈T : i<j<k, s_i=s_k=-s_j }`.

An atlas is a family of sign charts whose compatible sets cover `T`. Then the *minimum possible number of global diagonal sign charts* is **exactly four**:

`min{|A| : union_{s in A} C(s)=T } = 4.`

**Proof by exact finite certificate.** Enumerate all `2^6=64` sign assignments and assign each its 20-bit compatibility mask. Discard the empty mask and deduplicate equal masks; exactly **26 distinct nonempty masks** remain. Their cardinality distribution is six masks of size four, twelve masks of size six, and eight masks of size eight. Every possible 3-mask combination lies among the `C(26,3)=2600` choices explicitly checked in the accompanying source, and none has bitwise OR equal to the all-ones 20-bit mask. Thus no atlas of at most three charts covers `T`; a smaller cover would extend to a three-chart choice. An explicit four-chart partition below proves the bound is attained.

Exact enumeration of all `C(26,4)=14950` four-mask combinations finds 165 covering sets; exactly 42 contain the compatible mask of the current FCC STAR source's gauge. These counts quantify choices of distinct compatible-subset masks, **not** choices of original 64 sign strings or inequivalent physical chart systems.

## Four-chart *disjoint* partition witness

Use six signed entries in zero-based axis order. The following atlas partitions all 20 triples with no pairwise overlap:

| Chart | Signed gauge `s` | Assigned sorted triples `i,j,k` | Count |
|---|---|---|---:|
| A | `(-,-,-,-,+,-)` | 045,145,245,345 | 4 |
| B | `(-,-,+,-,+,+)` | 023,123,234,235 | 4 |
| C | `(-,-,+,+,-,-)` | 024,025,034,035,124,125,134,135 | 8 |
| D | `(-,+,-,-,-,-)` | 012,013,014,015 | 4 |

The 4+4+8+4 sets have union all 20 and pairwise empty intersections. Chart C is exactly one of Unit90's two global gauges for the four FCC STAR triples `025,034,124,135` (its negative is projectively equivalent for conjugation), so this is a particularly relevant minimal atlas for the actual source. The remaining C-compatible four triples `024,035,125,134` also have an exact named signed chart bridge without requiring extra chart changes.

**Important type boundary:** This four-chart minimum is for the defined finite six-axis *diagonal sign-gauge cover* language. It is not a lower bound on unrestricted axis-permutation, adaptive port-bearing, many-to-one observer or arbitrary representation schemes. Nor does its numeral four identify the four carrier STAR charts as four native spatial planes.

## All-length word transport with explicit gauge transitions

For any ordered word of named generator labels `t_1,...,t_L`, select an admissible chart `s_r` for each `t_r`. Then at the signed native state-transform level,

```text
q_{t_L} ... q_{t_1}
  = D_{s_L} g_{t_L} (D_{s_L}^{-1}D_{s_{L-1}}) g_{t_{L-1}}
      ... (D_{s_2}^{-1}D_{s_1}) g_{t_1} D_{s_1}^{-1}.
```

Each intermediate `D_{s_{r+1}}^{-1}D_{s_r}` is a **typed sign-gauge coordinate transition**; it is not silently discarded, counted as a native force event, or added as a seventh axis. Because every `D_s` is diagonal with entries ±1, it preserves native six-axis `G=Σz_a²`, shortest displacement length `T=Σ|z_a|`, and positive BRC path multiplicities **after signed-letter relabeling**, but not necessarily the untransported observer `rho(z)=z-min(z)*1`. Unit90 supplies the explicit two-state fiber witness `rho(0)=rho(1)`, `rho(D_s0)≠rho(D_s1)`. Relative and finite-depth consumers must retain/reconstruct common depth and provenance before applying this transport.

For words remaining in the four FCC STAR generator set, take one constant chart C; all transitions vanish algebraically and Unit90's all-word conjugacy follows. Words requiring other compatible groups have state-dependent chart transitions. The minimal atlas and transition formula do **not** prove chronologically legal physical 160-event serialization or original triadic balance.

## Actual executable and source evidence

`research_checks/X6_UNIT91_MINIMAL_FOUR_GAUGE_TRIAD_ATLAS_CHECK_20261117.py` is a standalone exact finite enumeration of all 64 gauges, all 20 triads, 26 distinct compatibility masks, 2600 three-chart combinations, 14950 four-chart combinations, 165 valid covers and 42 covers retaining the STAR gauge; additionally it certifies the explicit four-way disjoint partition. Machine-readable certificate: `research_checks/X6_UNIT91_MINIMAL_FOUR_GAUGE_TRIAD_ATLAS_RESULTS_20261117.json`. A separately executed plain-Python integer/set calculation reproduced the same 26/2600/0/14950/165/42 counts and the 4+4+8+4 disjoint exact partition; no original R063/Helly benchmark was executed.

No current code path has been shown to perform an actually incorrect named-generator conversion. This is a **positive interoperability atlas** plus a sharp lower bound within its typed language, not historical blame for LP011/LP019, whose original erroneous file/line remains `UNRESOLVED_PROVENANCE`.

## Parent continuation

Unit90 is already preserved in Source with its proof/checker/certificate/continuation. Unit91 is the minimal global-cover refinement and supplies a four-chart, 20-triad exact conversion specification. Preserve the original X6 SID/CLAIM/RUN and unanswered Native semantic PROGRESS separately; GitHub author publication does not authorize a role-bound checkpoint or independent review.

Next actual scientific action: inspect one source consumer crossing from four FCC STAR signed generators to the 20-triad `q_triad` family, `signed_brc.endpoint_multiplicity`, `CoverState` or a min-zero observer, testing whether it already transports labels, observer and chart transitions. If none actually converts generator families, record that as a scoped negative source finding rather than manufacturing an error. Feed original-code source evidence to the independent Driver's pending `REQUEST_REVISION` for LP011/LP019 and continue source-bound 28-LP reconciliation. Original scheduling and notifications untouched.
