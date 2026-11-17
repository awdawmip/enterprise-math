# X6 Unit80 — signed C12 root plus complete BRC path-jet: exact information repair

Date: 2026-11-17. Parent objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Classification: **AUTHOR-EXACT / FINITE-EXHAUSTIVE-EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is new author evidence, **not** a native PROGRESS, review, or proof of an executed original R063/Helly benchmark.

## Original problem and preserved types

Keep frozen signed-X6 P000 scientific input commit `59538f585d037d09ef687b28715c4bc1a3f9fe03` and archival plane corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; the chosen Cell is chart zero, not the physical geometric origin. Unit79 showed that a nonzero signed C12 microtrace root `R=x3` has a uniquely determined next macro Cell `x4`, but the second following microstate `x5` has 2–5 possible values once both original positive BRC INNER/OUTER branches and source triads are allowed. The next question is how much of this ambiguity an **existing, actually computed path observable** can remove.

The independent source consumer `experiments/x6_rotation_path_tensor_jet_20260906/check_x6_rotation_path_tensor_jet.py` (current Git blob `4f193358c94ee4252507e40cc19d1cc61a185bd4`) defines the exact noncommutative **discrete-subsequence** tensor jet (lines 48–83), the genuine INNER/OUTER primitive-step words (108–121), degree-2 antipodal-pair count quotient (187–214) and degree-3 full-branch signature (227–253). It already establishes a 1/27/64 separation within a named frame (lines 166–184). Unit80 applies that typed carrier to **Unit79's twenty signed nonzero root classes across all named frames and both orientations**, where the source frame was not supplied as part of the root.

## Finite population, observer and theorem

For each `0<=i<j<k<6`, orientation `eps=+/-`, and BRC branch word `beta in {0,1}^6`, take the six macro phases

`p+=(e_i,-e_j,e_k,-e_i,e_j,-e_k)`,
`p-=(e_i,-e_k,e_j,-e_i,e_k,e_j,-e_k)`.

**Correction to the displayed p- list:** the six phase entries actually used throughout the proof and checker are `p-=(e_i,-e_k,e_j,-e_i,e_k,-e_j)`. The immediately preceding seven-token shorthand is an editorial typo; only this explicitly corrected six-entry definition is normative. (This explicit correction preserves the original executable bytes without concealing a textual transcription error.)

Each macro edge from `a=p_r` to `b=p_(r+1)` has two length-two positive-BRC alternatives: INNER primitive steps `(-a,b)` via the chosen Cell, or OUTER steps `(b,-a)` via `a+b`. The corresponding microtrace has `x_(2r)=p_r`, `x_(2r+1)=0` for INNER and `p_r+p_(r+1)` for OUTER. Nonzero `R=x3` forces `beta_1=1`, yielding precisely `20*2*32=1280` labeled full-branch histories, grouped into twenty signed roots. These 1280 histories, including distinct source frames and branch words, are the entire declared finite domain.

For the full **closed** twelve primitive-step word `s_1,...,s_12`, define

`S_d=sum_(1<=t1<...<td<=12) s_t1 (tensor) ... (tensor) s_td` for `d=1,2,3`.

The central **operation-specific** result is:

1. The full-loop degree-two jet `S2` recovers the original **three named source axes**, regardless of the lost source axis in `R`. It also recovers the three counts `c_r=beta_r+beta_(r+3)` for `r=0,1,2`. Thus `(R,S2)` restricts the second post-root state `x5` to at most **two** values. A single choice bit suffices and is necessary exactly on those degree-two fibers where `c2=1`.
2. Exhaustively over all 1280 histories, `R` alone gives 20 signatures, each x5-ambiguous; `(R,S2)` gives **720 signatures** of which **240** have two different x5 outcomes (640 histories), and `(R,S3)` gives **1280 signatures** with **zero** x5 ambiguity. The latter is an exact finite injection certificate, also consistent with the existing named-frame third-order theorem.
3. The least supplementary information for the **bounded x5 output** once `(R,S2)` has been measured is 0 bits on the 480 unambiguous degree-two signatures and **1 bit** on the 240 ambiguous signatures. This is a conditional, variable-rate information statement; it is not a claim that full branch provenance, individual `beta`, or an arbitrary future process is restored by `S2`.

**Proof of the S2 reconstruction.** The complete closed path has `sum_t s_t=0`. Every primitive step is a signed unit basis vector. Therefore

`(S2)_(a,a) = ((sum_t s_(t,a))^2 - sum_t s_(t,a)^2)/2 = -2`

for each of the three used axes `a in {i,j,k}`, since each occurs exactly four times, and is zero for all other axes. The diagonal therefore identifies precisely `{i,j,k}`. For distinct axes `a,b`, the entry is antisymmetric. Changing one macro edge `(a_r,b_r)` from INNER to OUTER replaces `(-a_r,b_r)` by `(b_r,-a_r)`, changing `S2` by `a_r tensor b_r - b_r tensor a_r`; cross-block terms are unaffected because both alternatives have the same total displacement `b_r-a_r`. Antipodal macro edges `r,r+3` have the same skew increment, so the whole `S2` depends exactly on the counts `c0,c1,c2`.

For `eps=+` and ascending frame `i<j<k`, the independent components are
`(S2)_(i,j)=-c0, (S2)_(j,k)=-c1, (S2)_(i,k)=+c2`.
For `eps=-` they are
`(S2)_(i,k)=-c0, (S2)_(j,k)=+c1, (S2)_(i,j)=+c2`.
The signs of the nonzero root `R=e_k-e_j` or `R=e_j-e_k` determine `eps` and `j,k`; the diagonal of `S2` determines the missing `i`, and the signed off-diagonal entries determine the three `c_r`. In particular `c2=beta2+beta5`. When `c2=0` or `2`, `beta2` is fixed. When `c2=1`, exactly the alternatives `(beta2,beta5)=(0,1)` and `(1,0)` remain and realize distinct `x5=0` or `x5=x4-e_i`. This proves the two-output bound, and the two realized outcomes prove the one-bit lower bound. The `S3` finite injection is validated by the exact integer census below; the pre-existing named-frame degree-three source proves the corresponding fixed-frame subcase.

**Important temporal type:** `S2,S3` above are measured on the **whole completed twelve-step loop**, including steps that occur after `x5`. This provides retrospective decoding or a completed-loop handoff observer, **not causal real-time prediction** at `x3`. A causal update must carry the relevant branch/frame choices or observe their later revelation, as in Unit79.

## Exact executed verification

The self-contained, original-model-reproducing checker is
`research_checks/X6_UNIT80_ROOT_TENSOR_JET_EXACT_CHECK_20261117.py`, immutable commit `ae7cdc9aefa5b10ee05cbbdc7a48e8299391c43c`, verified Git blob `dfd11ad15442dbe50a92a55a1df4f02d8dbfba58`, SHA256 `a884d0dcb162905312696ecdd38378320e693cd934a43e911a3c1d995de5fae9`.
The emitted exact integer JSON is
`research_checks/X6_UNIT80_ROOT_TENSOR_JET_RESULTS_20261117.json`, immutable commit `a3c2cd7bad567a3f4c4f20b0f88785e02a98dacd`, verified Git blob `d9c62b21c7c235c6fc923556d2931ccf41f97f7b`, SHA256 `b4e48eca146c671261a74223b283c57cfffb1947007fcb43a592ea21480ff9c9`.

| Exact observable | Distinct signatures | Signatures with different x5 | Histories in ambiguous signatures | Maximum x5 outcomes |
| --- | ---: | ---: | ---: | ---: |
| root R | 20 | 20 | 1280 | 5 |
| (R,S2) | 720 | 240 | 640 | 2 |
| (R,S3) | 1280 | 0 | 0 | 1 |

For `(R,S2)` the exact signature-size histogram is `{1:320, 2:320, 4:80}`; for `(R,S3)` it is `{1:1280}`. The verifier checks the source-axis diagonal invariant, all six direction-specific skew entries, exact loop closure, class counts and output discrimination. It ran in local CPython normal, `-O`, and `-OO` modes and produced identical JSON bytes in all three modes, with **zero failed checks**. It is a self-contained exact enumerator of these source-defined BRC rules; it does not claim to have rerun the frozen full native benchmark.

## Additional current consumer source:line audit

Outside the prior nine-file Unit79 audit, exact current-source reads checked: `x6_rotation_path_groupoid_v2.../check_rotation_path_groupoid.py` (blob `cafc32fe407a935d5ba8d3847f3880c6ef644329`, lines 48–65); `x6_rotation_path_tensor_jet.../check_x6_rotation_path_tensor_jet.py` (blob `4f193358c94ee4252507e40cc19d1cc61a185bd4`, lines 108–253); `x6_rotation_path_dagger_jet.../check_rotation_path_dagger_jet.py` (blob `51a567303d2d6da37c82dda418b82c5d90a1e4a9`, lines 29–38, 125–132); `x6_signed_cycle_atlas_v12.../check_signed_cycle_atlas.py` (blob `9c5bfac5c2d317d38221aca732c8250944051f15`); `x6_dynamic_law_holonomy_v24.../check_dynamic_law_holonomy.py` (blob `b323a4e56b2ed2fe6a70b3a87060c99c90d5fe14`); `x6_phase_chirality_d12_v14.../check_phase_chirality_d12.py` (blob `be12bb72e694ec330e372d40dab4b1b9dd58dc26`); `x6_branch_selector_context_v3.../check_branch_selector_context.py` (blob `bb8fd71bafa5b8c53c5170d2347baa0f2c06f5fb`, lines 26–75); and `x6_rotation_law_selection_v3.../check_equivariant_branch_laws.py` (blob `62d03a89c19518c3d80ebee3589952d1755d4ff8`).

The actual examined modules keep frame, branch, or explicit contextual typing, so no incorrect root-only deterministic `x5` caller was confirmed in this bounded eight-file set. Their correct typed operations are preserved. The old LP011 dominant-axis and LP019 positive-count cancellation **alleged historical wrong callers remain UNRESOLVED_PROVENANCE**; resolving those needs actual frozen source:line and a downstream consumer, not a generic analogy to this result.

## Continuation

Mother task remains OPEN. Reuse Units64–79 and their exact GitHub/Activity evidence, the signed-sector/G25, 72/111 and filled-disk results, and the frozen R063/Helly execution records. The next useful discriminant is the archival LP011/LP019 exact caller search and remaining 28-LP genuine downstream contracts, followed by independent Driver `REQUEST_REVISION`. Original native GitHub-Chat Research SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-579c8e23625448582b421831` and RUN `RUN-fb25028676f9692ab1bacaee` are provenance from the existing lane; current read-only continuation cannot authorize a separate Sites subject to publish its PROGRESS. Original queued/success receipts must be consumed by ID, not replayed.
