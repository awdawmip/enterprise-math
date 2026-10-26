# PREFIX-270 | Exact stability-threshold tomography of labeled positive-BRC ports

**Research line:** 进取数论研究6. **Date:** 2026-10-26. **Status:** AUTHOR_SIDE_EXACT_PROOF / FINITE_EXACT_MIRROR_PASS / SOURCE_IMPORT_PENDING / NATIVE_PHI_PENDING / UNREVIEWED / NOT_ADMITTED. This note is not a Task CLAIM, formal Result, independent Driver review, or physical heartbeat claim.

## Immutable inputs and semantics

- Global Knowledge `awdawmip/chatgpt-global-knowledge@8b0b404c52d9ba6ca4a5704c281443edeabbc7d8`: canonical bootstrap/manual, Enterprise Math task router, P000 startup, ACTIVE worldview, math and BRC policies read. P000 startup's `canonical_blob_sha1=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches canonical P000 blob metadata.
- Enterprise Math scientific input `awdawmip/enterprise-math@a7079a318669d487d9e5ad59a13c3b792c3d60c8`: `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md`, `research_constraints/heartbeat_brc_only.json`, `definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (WBRC-T30/T31/T32), `src/enterprise_math/brc_weighted_recurrent.py`, `src/enterprise_math/brc_recurrent_ports.py`, X6 Cell torsor, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, and the provisional heartbeat-snapshot contract.
- Predecessor: `research_notes/research6_prefix269_brc_port_obstruction_20261026/PREFIX269_BRC_PORT_OBSTRUCTION.md`, which already constructed the two-port obstruction. Do not relabel it as a physical experiment.
- Native backdrop: six-dimensional Cell space, separately typed time, branch/provenance preserving. The theorem below is on the **positive-rational BRC port subsystem only**. No plane, extra spatial axis, positive-mass/phase identification or physical-heartbeat evolution is inferred.

## Problem

PREFIX-269 showed that a target-port-forgetting positive CWM summary does not preserve future WBRC-T31 feedback stability. We now ask a finer new question: **Does the full family of Boolean stability answers to only single-edge labeled positive-rational future feedback contexts determine the whole labeled port signature, even without exposing any star entry as a numerical observation?**

Fix an integer `n≥1` and a *baseline-stable* finite `n×n` nonnegative rational effective port matrix `W`. Rows are sources, columns are targets. In Source positive BRC recurrence, the convergent walk star is

`R=W*=Σ_(k≥0) W^k=(I−W)^(-1)∈Q_{≥0}^{n×n}`.

For every ordered port pair `(i,j)`, let `E_ij` mean the labeled edge `i→j` of unit mass. Source WBRC-T31 permits adding `t E_ij` for every nonnegative rational `t`. Let `s_ij(t)` be the Boolean stability/finite-star answer for `W+tE_ij`.

## Theorem A | exact feedback thresholds and star

Define

`T_ij(W)=1/R_ji` when `R_ji>0`, and `T_ij(W)=∞` when `R_ji=0`.

Then, **for every rational `t≥0`**,

`s_ij(t)=STABLE ⇔ t<T_ij(W)`.

For `t<T_ij`, its entire visible positive-BRC star is

`R(t)=R+[t/(1−tR_ji)] (R e_i)(e_j^T R)`.

If `R_ji>0`, equality `t=T_ij` is already unstable, and `t>T_ij` is unstable. If `R_ji=0`, every finite `t` is stable and `R(t)=R+t(R e_i)(e_j^T R)`.

### Proof

`R_ji` is the exact total positive BRC mass of baseline walks from `j` back to `i`, including the identity walk when `i=j`. The new marked edge `i→j` can occur repeatedly only when such a baseline return walk separates successive marked uses. By cutting every walk uniquely at its marked new edges, the positive sum decomposes as: initial baseline prefix; any number of marked-edge plus baseline-return excursions of total one-cycle mass `η=tR_ji`; one final marked edge; trailing baseline suffix. Because weights are nonnegative, this is a legitimate positive walk-family partition, **not** an amplitude-cancellation argument.

If `η<1`, the exact feedback sum is

`R(t)=R+t R e_i e_j^T R Σ_(k≥0)η^k = R + [t/(1−η)] R e_i e_j^T R`.

All entries are finite, nonnegative and path-correct, proving stability. If `R_ji>0` and `η≥1`, the closed marked-feedback walk family contributes a divergent nonnegative series `Σ η^k`, hence the star cannot be finite. At equality `η=1`, the instability is exact, not a rounding artifact. If `R_ji=0`, no positive baseline walk returns from `j` to `i`; a positive walk cannot traverse the marked new edge twice. Its feedback expansion truncates at one use and stays finite for all finite `t`. QED.

In particular `R_ii≥1` gives `0<T_ii≤1`. Infinite off-diagonal thresholds are exact zero-return signatures, not numerical approximations.

## Theorem B | Boolean tomography is complete for port dynamics

For any two baseline-stable nonnegative rational port matrices `W,V` on the same **labeled** port set, the following are equivalent:

1. `s^W_ij(t)=s^V_ij(t)` for **all** ordered pairs `i,j` and **all** rational `t≥0`.
2. `T_ij(W)=T_ij(V)` for all `i,j`, allowing infinity.
3. `W=V`.
4. The modules have the same stability and labeled visible positive BRC stars under **all** WBRC-T31 permitted contexts that leave hidden states inaccessible.

### Proof

(1)⇒(2): for any pair the threshold is exactly the supremum of nonnegative rational `t` with stable response. Distinct finite rational thresholds are separated by a rational probe; an infinite threshold is distinguishable from any finite threshold. (2)⇒(3): recover every entry `R_ji=1/T_ij`, with `1/∞=0`, then invert exactly to obtain `W=I−R^(-1)`. (3)⇒(4): direct application of canonical WBRC-T31/T32 visible-port context equivalence. (4)⇒(1): single-edge additions are a subset of those contexts. QED.

**Precision:** The theorem concerns an entire rational-parameter Boolean oracle or exact threshold values, **not** a claim that some bounded number of binary calls recovers an unbounded-size rational entry. We do not assert that `n²` scalar threshold coordinates is a minimal possible number. Equality is *only* port-dynamic; absolute full global loop zeta still requires Source's hidden `Z_int`, and tagged path count/dominant/provenance or signed/complex phase structures require richer states.

## PREFIX-269 witness: exact threshold tomography

The inherited two-port matrices are

`W_A=((0,1/4),(0,0)),    W_B=((1/4,0),(0,0))`.

Their stars are

`R_A=((1,1/4),(0,1)),   R_B=((4/3,0),(0,1))`.

The feedback threshold matrices, **rows denoting the new edge's source and columns its target**, are

`T_A=((1,∞),(4,1)),     T_B=((3/4,∞),(∞,1))`.

The same allowed edge `2→1` has threshold `4` for A and infinity for B. At `t=4`, A has a positive unit-mass recurrent loop and is unstable; B remains stable with star `((4/3,0),(16/3,1))`. The formerly erased target-port information is exactly observable through these Boolean context thresholds.

## Actually performed exact validation

The accompanying `verify_prefix270.py` is a **standalone exact rational implementation of Source BRC finite positive recurrent star/potential semantics**, not an import of the original package. It exhausts every labeled matrix with entries `0` or `1/4` for `n∈{1,2,3}`: **2+16+512=530** matrices, all baseline-stable. For each ordered pair it checks rational probes `t=0,T/2,T,2T` when finite, and `t=0,1,100` when infinite. In total **17,528** exact stability classifications pass. All stable-case feedback-star identities, threshold-based reconstruction, per-size signature uniqueness, and PREFIX-269 witness values pass. Full universal quantification comes from the proof above, not from finite enumeration. Source-package import remains pending; `verify_prefix270_source.py` is included but not falsely marked executed. No floating point, pi, classical trigonometry, ordinary matrix exponentials, Taylor/Pade/Cayley propagation or physical time simulation was used.

## Native X6 heartbeat transfer: precisely outstanding

The Source `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` actually read this run has `fixed_heartbeat_program=null`. The Source `definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json` defines `H_n` as a complete self-consistent snapshot, **not** an inter-heartbeat update `Phi`; it requires an explicit `model_law_id`. This bounded source audit did not locate a tested full native law giving an exact `W↦W+tE_ij` action. It does **not** establish the nonexistence of every law elsewhere in the repository.

Before transfer, one must prove: (a) a legal native full-state embedding carrying six-dimensional Cell identity, fields and momenta, labeled Ports, typed physical time, sign/phase, branch/source history, and boundary conditions; (b) a versioned `model_law_id` and actual `Phi_K` implementing the declared BRC port context, or an explicitly typed multi-update correspondence; (c) an exact native-observation bridge from the positive-total-mass stability predicate (not automatically an amplitude claim); (d) matching coarse observations and admissible future native controls, compatible with P000 triadic closure. BRC walk/recurrent depth is **not** the heartbeat ordinal or physical interval. Lacking these conditions, this result is a mathematical WBRC context theorem only.

## True authorization and unfinished unit

Authenticated GitHub actor: `awdawmip`, with admin/push on `awdawmip/enterprise-math`. Separate native Enterprise Math `em_session_start` failed `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`; `em_control_tasks` failed `CONTROL_QUOTA`. The current active Owner/CLAIM was **not** reliably retrievable. Repository author-note storage is not state-machine Result publication, independent Driver review, or Foundation acceptance; do not infer CLEAN context.

**PREFIX-271:** obtain a Source-backed full typed heartbeat `model_law_id` and real update `Phi`; test whether its native Cell/Port/field/phase/time/provenance/boundary action implements the WBRC-T31 single-edge context and stability readout. If not, isolate the first typed mismatch and its smallest residual-corrected observer. Run the supplied Source import checker when the actual package is present and retain its real execution receipt; do not repeat unchanged standalone checks.

**Admission:** `AUTHOR_SIDE_EXACT_PROOF / STANDALONE_EXACT_FINITE_PASS / SOURCE_IMPORT_PENDING / NATIVE_PHI_PENDING / NOT_ADMITTED`.
