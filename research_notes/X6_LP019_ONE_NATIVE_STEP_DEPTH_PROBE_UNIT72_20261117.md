# X6 Unit72 — A single typed native-step quadratic comparator resolves the residual two-depth ambiguity

Date: 2026-11-17. Role: TASK_RESEARCH, author-side. Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. Status: **AUTHOR-EXACT / FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Immutable scientific basis and actual scope

- Frozen signed-X6 scientific source: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, P000 V5, six signed native primitive axes and a chosen Cell anchor. The three selected signed axes 0,1,2 form a *restricted embedded native X6 state slice*; axes 3,4,5 have displacement zero. This is not an independent native plane or new physical dimension.
- Original frozen `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`: `spatial_norm_squared` returns the component sum of squares; `shortest_path_multiplicity` is the positive integer multinomial.
- Historical comparison pin: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Retain joint relation, signed steps, named axes, source/provenance and operation scope. No P000/Foundation change.
- This is a new active-observer repair of the Unit69–71 residual common-depth ambiguity. Those already-saved theorems and the original frozen native R063/Helly benchmarks are consumed, not rerun.

## Exact universal theorem

For an arbitrary signed selected three-axis displacement `z=(z0,z1,z2)∈Z³`, define
```
h=min(z0,z1,z2),  r=z-h(1,1,1),  min(r)=0,
G(z)=Σ z_j²,  T(z)=Σ |z_j|,  R=Σ r_j,  Q=Σ r_j².
O(z)=(r,G(z),T(z)).
```
The old exact observer-fibre quadratic is
`3h²+2Rh+(Q-G)=0`. Set `D=R²+3(G-Q)`. When `O(z)` has *two distinct globally admissible integer depths* `h_-<h_+`, they are necessarily
`h_±=(-R±sqrt(D))/3`, with `D>0`; the selected shortest length `T` already holds for both.

For **any named selected native positive axis** `e_i`, form the observable *one native signed primitive-step quadratic difference* at the chosen Cell:
```
Δ_i(z)=G(z+e_i)-G(z)=2z_i+1=2(r_i+h)+1.
K_i(r)=3+6r_i-2R  (integer known from the pre-probe observer).
B_i(z)=sgn(3Δ_i(z)-K_i(r)) ∈ {-1,+1}.
```
Then the exact identity
```
3Δ_i(z)-K_i(r)=6h+2R
                  = -2sqrt(D) if h=h_-,
                  = +2sqrt(D) if h=h_+.
```
proves that the **single binary comparator** `B_i` uniquely selects the actual depth among the two possibilities for *every selected axis i*. Recover
`h=(-R+B_i sqrt(D))/3` and `z=r+h(1,1,1)`; embed with the three omitted signed components fixed to zero. This also recovers the exact native BRC shortest-path multiplicity `T!/∏|z_j|!` and the signed path provenance needed by subsequent typed operations.

The comparator uses one new *tagged active native operation and its quadratic readout*. It is not a claim that the already passive triple `(r,G,T)` contains this information. A binary discriminator is **worst-case necessary** for lossless native-state recovery because there exist exactly two distinct native states with identical passive `O`; any zero-additional-information deterministic decoder outputs the same state on both. It is **sufficient** by the identity above. For a singleton fibre no extra bit is necessary. This establishes the exact information bound for this declared two-candidate model and this native probe, not physical instrumentation or temporal dynamics.

### Two independent discriminating witnesses

1. `r=(3,0,0), G=18, T=6`: depths `(-3,+1)`; native signed triple displacements `(0,-3,-3)` and `(4,1,1)` have positive shortest-path BRC multiplicities `20` and `30`. Along named axis `i=1` (zero-based), `Δ_i=(-5,3)`, `K_i=-3`, so `3Δ_i-K_i=(-12,+12)`; the binary comparator separates the two.
2. `r=(0,2,4), G=11, T=5`: depths `(-3,-1)`; native displacements `(-3,-1,1)` and `(-1,1,3)` have the **same positive shortest-path BRC multiplicity 20**. For named axis `i=0`, `Δ_i=(-5,-1)`, `K_i=-9`, so `3Δ_i-K_i=(-6,+6)`. Both raw deltas are negative: testing the sign of `Δ_i` alone fails; the *observer-calibrated* one-bit threshold succeeds. This explicitly extends Unit71's operation-safety distinction beyond all-length unweighted BRC.

## Real finite, independently executed author-side verification

Exact integer checker: `research_checks/X6_UNIT72_SIGNED_ONE_STEP_DEPTH_PROBE_CHECK_20261117.py`, immutable commit `06463dbb0725b4e38493c014bef524519159dd02`, Git blob `687c59ba939e5a24f7bd7cf9fa6a339082b89b80`. Machine-readable result: `research_checks/X6_UNIT72_SIGNED_ONE_STEP_DEPTH_PROBE_RESULTS_20261117.json`, immutable commit `8fb00b9a806608fe6b02243b692c2419628ed1ad`, blob `6c6bb3aa0347f943cc20d1c31474ef8cff6f15cf`.

The executable enumerates every one of the `25³=15,625` native signed selected triples on `[-12,12]³`; it finds `14,887` observed `(r,G,T)` signatures. It solves the *global integer* root equation for each observed signature, finding `912` signatures with two admissible depths (some second representatives lie outside the finite cube). Among these, `408` have equal unweighted BRC shortest-path counts and `504` unequal. It checks each axis' integer comparator against the closed-form discriminant for all 912 double signatures: `2,736` comparisons, **0 failures**. Arithmetic is exact integers/factorials/integer square root; no floating-point tolerance.

This checker is an **independently implemented exact oracle** using the already-frozen algebraic native metric law; it does **not** import or rerun the original `signed_brc.py` benchmark, whose own precise path-count executions were completed and preserved in Units62/71. Its exhaustive finite window supports the declared coverage; the all-integer theorem follows from the algebraic identity, not from the finite count.

## Historical caller/source audit: new narrowly scoped observations

Actual current-main executable source files inspected in this run with Git blobs and line-typed decisions:

- `experiments/brc_dominant_degeneracy_quotient_check.py` blob `33740d338fdc0459bb5ef07a9afc01892fae4752`: lines 21–26 use `max` on **positive rational branch weights**, and 168–202 on generic graph leading path weights. **KEEP** as weighted-BRC histogram/graph semantics; these lines do not implement the alleged LP011 signed-native singleton-axis argmax.
- `experiments/brc_foundation_retrofit_check.py` blob `8dbc1bdde0d63979f0b84d431e39864639aca423`: lines 192–247 carry derived signed oriented holonomy and `cwm_recoalesce` of **strictly positive weights**, with the two orientations not subtracted as natural N-BRC mass. **KEEP** as derived weighted/provenance algebra; not an LP019 positive-native-BRC signed cancellation caller.
- `tests/test_brc_weighted_foundation_tool.py` blob `69963f8a1089a87b6fb48e648f15ef19bff70e56`: lines 108–112 explicitly reject negative positive-carrier weights. **KEEP**.
- Previously inspected positive-chart matroid checker blob `bce4453d740ac3c0c401843b732dc78c74056883` was revisited for exact context at lines 407–427: generic Boolean-BRC incidence; no native positive-mass subtraction.
- GitHub connected code-index searches of selected exact strings returned empty; index incompleteness means **no whole-repository absence conclusion**.

LP011 alleged historical wrong signed-native dominance source:line and LP019 alleged subtraction of positive native N-BRC mass source:line remain `UNRESOLVED_PROVENANCE`. This new mathematical theorem supplies an explicit, operation-safe active-repair interface; it does not retroactively supply a missing historic error location.

## Parent/frontier and action

Parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; exact Task/publication above. Native prior Units69–71 progress request `onhour-20261117-0259-x6-unit69-71-native-progress-v1` is **SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED**, authenticated, Source commit `0c1fdb23d6566f8bb74f96759099899016d015d7`; do not replay. Current original native read-only continuation request `onhour-20261117-0404-x6-current-continuation-read-v1` was initially QUEUED; its eventual original receipt must be consumed before role-bound follow-up. Existing author Researcher `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`, claim `MCP-579c8e23625448582b421831`, run `RUN-fb25028676f9692ab1bacaee`; all require current live Source authorization for any new native semantic write.

Continue: (a) bind this scoped Unit72 GitHub/Activity evidence into the original run via valid canonical semantic checkpoint only with fresh own winning-claim authorization; (b) trace precise frozen historical LP011/LP019 bad source:line if evidence exists and complete remaining actual 28-LP live consumers; (c) independent Driver `REQUEST_REVISION` remains for that role. Preserve frozen science and existing R063/Helly experiments and all previous units. No schedule, task authority, frozen Result or independent review change.
