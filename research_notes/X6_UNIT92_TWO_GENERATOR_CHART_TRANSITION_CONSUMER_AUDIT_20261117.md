# X6 Unit92 — two-generator chart-transition failure and exact provenance-preserving adapter

Date: 2026-11-17. **AUTHOR-EXACT / FINITE-EXECUTED / SOURCE-CALL-SITE-INSPECTED / UNREVIEWED / NOT_ADMITTED.** Parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`, Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Frozen scientific P000 pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical source `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; primitive signed BRC original blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.

## Actual parent dependency

Unit90 established a common diagonal sign gauge for the four FCC STAR generators; Unit91 established the disjoint four-gauge atlas for 20 named triads. This unit checks **operator composition across the actual generator-language boundary**, rather than extending those atlas counts abstractly. It also supplies a minimal regression fixture for any actual cross-program adapter.

The two source definitions, frozen independently, are:
- `experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py`, blob `c446d0327f9bf643d5796348ba46cafe96d2915d`: `q_triad` lines 44–50, called at 89, 117, 139. This program imports signed `signed_brc.py` at lines 16–21 for properly typed shortest path counts.
- `research_checks/20261112_x6_star_triad_group_brc_convolution.py`, blob `50cccf09b5dd83cc592ba36db5bc9e14941ce0ce`: `triad_generator` lines 30–34, used at 84, 86, 102; independently imports `endpoint_multiplicity` at line 15 and compares primitive BRC counts at lines 111 and 120.
- Native `signed_brc.py`, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, declares `endpoint_multiplicity` at line 42. `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py`, blob `171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd`, exposes `CoverState` at line 40 and rejects finite-cover signed-native identity at lines 74–86.

The two inspected generator scripts each work in their own generator language. **No direct cross-import / conversion call between those two scripts was found in these exact inspected bodies.** This scope is not a repository-wide proof of absence; available code-index search returned no matches and was not taken as exhaustive coverage.

## Exact two-generator transport theorem

Let (T=\binom{\{0,1,2,3,4,5\}}3) with its 20 sorted named triads, and let (A,B,C,D) be Unit91's disjoint sign charts of sizes 4,4,8,4. For each (t\in T), the unique chart sign (s_t\in\{\pm1\}^6) satisfies (q_t=D_{s_t}g_tD_{s_t}^{-1}). Every diagonal sign matrix is its own inverse. For two consecutive named generator operations, first (a), then (b),

[
q_bq_a=D_{s_b}g_b\underbrace{(D_{s_b}^{-1}D_{s_a})}_{\text{typed chart transition}}g_aD_{s_a}^{-1}.
]

If the middle transition is omitted, the resulting signed permutation equals (q_bq_a) **if and only if** (s_a=s_b), because multiplication by the remaining invertible signed permutations can be cancelled from both ends. For the disjoint atlas this is equivalent to using the same chart. More precisely, the number of basis vectors on which the shortcut differs is exactly the Hamming distance (d_H(s_a,s_b)), since each generator only permutes and signs the basis.

Thus among all 400 **ordered** two-generator words, exactly (4^2+4^2+8^2+4^2=112) are safe under transition omission and exactly **288** are wrong. The distribution of wrong basis-image counts is `{0:112, 2:64, 3:192, 4:32}`, summing to **832** wrong basis images in the 2,400 tested. Including the transition gives the exact correct operator for all 400 pairs. This statement is for the Unit91 **fixed disjoint choice of charts**, not for every possible adaptive global gauge choice.

## Smallest concrete witness

First apply (a=(0,1,2)) in chart D, then (b=(0,2,3)) in chart B, to native (e_0). The correct composed signed generator returns (-e_1), while dropping the intermediate chart transition returns (+e_1). Under the explicitly declared min-zero observer (ho(z)=z-\min(z)\mathbf1), their outputs are respectively ((1,0,1,1,1,1)) and ((0,1,0,0,0,0)). The scalar primitive (L=1) BRC multiplicity is 1 for either endpoint, so **scalar count equality cannot certify preservation of signed endpoint/observer semantics**.

For any finite positive depth modulus (m), the two raw native states (0) and (m\mathbf1) have identical ((ho,\min\bmod m)) cover state. Under any nonuniform sign chart such as Unit91 C, their transformed relative states are distinct: (ho(D_s0)=0) and (ho(D_s(m\mathbf1))) has entries 0 and (2m). Therefore no map on the entire finite-depth cover state alone can implement this mixed-sign chart transport for arbitrary raw integer states. The lossless ((ho,h)) lift from Units 84/90 remains the exact repair. This universal conclusion follows from the displayed symbolic witness; the test checks (m=1,\ldots,10).

## Exact execution and parent action

The standalone Python checker `research_checks/X6_UNIT92_TWO_GENERATOR_CHART_TRANSITION_CHECK_20261117.py` constructs the 20-generator atlas directly, exhausts all 400 ordered pairs and 2,400 basis images, checks signed-permutation identities, checks the min-zero witness and finite-depth fixtures, and emits `research_checks/X6_UNIT92_TWO_GENERATOR_CHART_TRANSITION_RESULTS_20261117.json`. Actual execution under CPython normal/`-O`/`-OO` produced identical JSON outputs with zero failed assertions in normal mode. Local checker SHA256 `4c9102b312a8108c39794198f8d49e59f62a4bba6c1528ffa01fee2716cc0260`; local result SHA256 `014ea44b7e87de2a90cd7924f2e19b90b02d372633f0888fbb2e710809d9a5c1`. Reproducibility concerns this model exactly; no original R063/Helly native benchmark was reexecuted.

This is an **executable type-safety regression and exact counterexample** for a prospective bridge, not a detected defect in either inspected current caller. The mother target still requires a verified historical LP011/LP019 erroneous caller or independent Driver revision, plus remaining 28-LP call graph closure. Next: inspect a genuinely downstream caller of `Sigma_O^(ij)`, PathSqrt, signed BRC or CoverState that actually takes an untyped foreign-coordinate input; record immutable source:line and patch only a demonstrated misuse. Preserve native R063/Helly test target and the original X6 SID/CLAIM/RUN; author GitHub evidence confers no Native write identity.
