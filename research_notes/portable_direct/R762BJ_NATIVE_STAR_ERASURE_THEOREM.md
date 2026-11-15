# R762BJ — Native X6 star-triple observer: exact recovery, erasure thresholds and BRC provenance

Status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`. Date: 2026-11-15. Independent portable scientific output associated with task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`; this author paper is not a formal Result or Driver review.

## Frozen scientific input and mathematical scope

The task's frozen science pins are:
- `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`
- `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`
- `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`

This work uses the **already-defined native coordinate** `Obs_S(z)=can3((z_i)_{i∈S})`, not the still-to-be-defined signed force-closure predicate `TRIADIC_CLOSURE_E`. It continues the observer-safety question after R762BI (PR #2493, immutable `adae22d555add18c777b591ffba9078dde876ece`), which studied a distinct conditional GF(2) orientation-parity readout.

Fix a native Cell anchor and its signed chart `z∈Z^6`. For all `2≤i<j≤6`, define the labelled Port-1 star observer
`O_{1ij}(z)=(z_1-m,z_i-m,z_j-m)`, where `m=min(z_1,z_i,z_j)`.
There are ten possible star rows. For any subset `H` of these ten, define a graph `G_H` on leaves `{2,3,4,5,6}`, one edge `ij` per retained triple `1ij`. Let `U(H)` be the isolated leaves.

## Theorem 1 — Exact observer fibers and full-Cell repair

For every `z,w∈Z^6`, `O_H(z)=O_H(w)` if and only if there exists an integer `t` with
`w_1-z_1=t`, `w_i-z_i=t` for every nonisolated leaf `i`, while `w_i-z_i` is arbitrary for every isolated leaf.

The additive kernel therefore is
`K_H=Z*(e_1+Σ_{i∉U(H),i≥2} e_i) ⊕ ⊕_{i∈U(H)}Z*e_i`,
of rank `1+|U(H)|`.

Thus `O_H` determines the full signed *relative* X6 Cell `Z^6/Δ`, `Δ=Z(1,1,1,1,1,1)`, exactly iff `G_H` has **no isolated leaf**. For such H, retaining the integer common depth `z_1` reconstructs the complete signed native Cell chart.

*Proof.* A retained row reveals `z_i-z_1=O_{1ij}(z)_i-O_{1ij}(z)_1` and `z_j-z_1=O_{1ij}(z)_j-O_{1ij}(z)_1`. Hence every incident leaf's difference to anchor axis 1 is exactly reconstructed. An isolated leaf never appears and is unconstrained. Conversely, a common integer shift of all read coordinates leaves each min-zero triple unchanged, and arbitrary shifts on unread leaves do too. These account for every fiber, proving kernel, rank and repair. □

The theorem concerns actual signed coordinate charts. It does not identify a min-zero triple with an admissible physical three-force closure or with a full Cell address codec.

## Theorem 2 — Exact optimum under known labelled erasures

Let `M(e)` be the least number of retained Port-1 star triples sufficient to reconstruct the relative signed native Cell after *any* adversarial deletion of up to e known labelled rows. For `e=0,1,2,3`,

`(M(0),M(1),M(2),M(3))=(3,5,8,10)`.

The number of distinct optimal labelled families is `(30,12,15,1)`. More generally,
`H survives e erasures ⇔ min_{i∈{2,...,6}} deg_{G_H}(i)≥e+1`.

*Proof.* By Theorem 1, reconstruction is equivalent to every leaf remaining incident to an observed edge. All rows containing leaf i form exactly its incident edges. Deleting ≤e rows isolates a leaf precisely when that leaf has initial degree ≤e. This proves the sharp criterion.

The handshake lemma gives at least `ceil(5(e+1)/2)` graph edges for minimum degree `e+1`. These bounds are attained:

- e=0: three edges cover five vertices iff they form a two-edge path on three vertices and a disjoint edge on the remaining two. Choose the path center (5 ways) and its two neighbours (6 ways): 30.
- e=1: five edges require every vertex degree 2; a simple 2-regular graph on five vertices is exactly a 5-cycle, yielding `(5-1)!/2=12`.
- e=2: eight edges mean deleting two edges from `K_5`. The minimum degree remains ≥3 precisely when those two deleted edges are disjoint: `binom(5,4)*3=15`.
- e=3: every vertex needs degree 4, forcing `K_5`: one family with ten edges.

This proves all minima and optimal-family counts. □

For the complete ten-row star, all ≤3 known row erasures preserve the relative Cell. Erasing the four rows containing any one specified leaf is a sharp information-loss witness. These are **row erasure**, not unknown-value bit error, guarantees.

## Theorem 3 — Declared future-operation safety

Suppose H covers every leaf, so the equivalence relation is `z∼w ⇔ z-w∈Δ`. This equivalence is preserved by every primitive signed coordinate-step update `T_i^±(z)=z±e_i` and by the admitted native `S_6` axis-permutation skeleton. Therefore the observer quotient is future-operation safe for *coordinate-only* observations under finite compositions of these operations, with the integer common-depth repair restoring full signed Cell identity when required.

*Proof.* For simultaneous coordinate translations, `T_i^±z-T_i^±w=z-w`. For any permutation P, `PΔ=Δ`. Both are exact equality statements over Z. □

No assertion here is made for currently unverified physical triadic-force update/port dynamics or rotations beyond the admitted `S_6` skeleton.

## Exact BRC/provenance counterexample

For any Cell c, two native two-step paths `(+E_1,+E_2)` and `(+E_2,+E_1)` terminate at the same spatial Cell `c+e_1+e_2`. All labelled coordinate observers, including the complete Port-1 star with depth repair, agree on the endpoint. Yet the ordered primitive steps and path-branch identities differ. The established exact signed shortest-path BRC theorem assigns multiplicity `2!=2` to this displacement. Hence this spatial quotient is not, without additional operation-specific evidence, a Link/Port/history-safe quotient. The full signed path and branch provenance must remain available to any history-dependent `TRIADIC_CLOSURE_E` test.

## Reproducibility and evidence

Companion Node.js verifier `R762BJ_NATIVE_STAR_ERASURE_VERIFY.js` uses only exact integers and built-in assertions. Run with `node R762BJ_NATIVE_STAR_ERASURE_VERIFY.js`. It exhaustively checks all 1024 labelled subfamilies and all applicable erasure subsets for e=0..3, and enumerates `{-1,0,1}^6` across all subfamilies. The JSON evidence records:

| e | minimum rows | optimal families | all admissible families |
|---|---:|---:|---:|
| 0 | 3 | 30 | 768 |
| 1 | 5 | 12 | 253 |
| 2 | 8 | 15 | 26 |
| 3 | 10 | 1 | 1 |

Verification counts: 4096 subfamily/erasure-budget comparisons, 746496 exact chart-family reconstructions and 14580 diagonal-shift observer-invariance checks. General results hold over all `Z^6` by the proofs; the finite checker verifies the declared finite domains. Independent review: `NOT_REVIEWED`.

## Next discriminating mathematical question

Read a Source-authenticated allowed **signed force** `TRIADIC_CLOSURE_E` Cell/Link/Port predicate and the exact V17/V29/V39 legal updates. Form its genuinely permitted triadic incidence family, then compute the actual signed observation fibers, rank/distance when a binary readout is justified, and a future-safe BRC quotient retaining force and ordered path provenance. In the current P000 frozen sources, the three-force minimum and pairwise native 120° relation are fixed, while the complete signed incidence/dynamics remains open. The V1R signed 960-state port-frame and V17 active-frame models remain separately typed research constructs.

Related exact sources: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md`, `research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md`.
