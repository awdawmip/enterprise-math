# R641｜真实 PF10 V27 关系更新的带符号观察同余与六轴 S3 历史

Date: 2026-11-08. AUTHOR_SIDE_EXACT_DERIVATION / UNREVIEWED / NOT_ADMITTED.
Frozen signed BRC science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; predecessor R640@d57da3c84cb9add0d563d2c22dfd9a0d503f1ad9.
Actual existing source: enterprise-math@b62110008321d9147212cb89f2627ff613c2550d:
- research_notes/X6_CHANNEL_NONRECIPROCITY_CIRCULATION_BRIDGE_V26_20260906.md (blob a8252050cc03f6930bb86251094d899c04743b60)
- research_notes/X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md (blob c5a02e6727dfc1f70ae4594c3ee807d1760c0be9)
- experiments/x6_dynamic_law_holonomy_v24_20260906/check_channel_circulation_bridge.py (blob 5618dae00632f9f796d3f5a6a692c248ea699131)
- research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md (blob 42b810a8f82c504833027da17884cc4fb2943e5b)

## Exact question

R640 decomposed the recorded PF10 source into 24 nonnegative integer counts X=(I,O,M), with ten signed contrasts T(X)=(u,Ω), u=I−O, Ω=M−M^T. R640 proved integer ker T≅Z^14 and a 14-source-reference lossless full-count reconstruction.

Can T nevertheless be safely used **without these extra 14 source readings** for the actual V26/V27 deterministic active-triad update, as long as PF10 counts are held fixed during the relation transition? We keep the active-triad S⊂{0,...,5}, |S|=3, inside the original six native spatial axes and a *separately typed* four-port internal PF10 source-to-channel injection. We retain the ordered S-history for later V17 S3 holonomy.

## Theorem — exact operation-safe quotient for the fixed-count V27 selector

Let C(S)∈Z^4 be the exact V23 matching code of each of the twenty 3-axis subsets, and N(S) its nine neighbors in J(6,3). On a selected PF10 internal snapshot X=(I,O,M) with fixed u,Ω, define the V26 score for a candidate T∈N(S):

Φ_X(S,T)=u^T C(T)+C(S)^T Ω C(T).

Where the maximum is unique, let g_X(S)=argmax_{T∈N(S)} Φ_X(S,T). Define the one-relation-step update F(S,X)=(g_X(S),X) with **fixed** raw PF10 source counts.

Then for every nonnegative X and X' with T(X)=T(X') and every admissible S,

g_X(S)=g_X'(S),

and their winner score, all nine scores, all ties and score gaps agree. When g is single-valued, the entire S-trajectory, its ordered path and each V17 S3 holonomy computed from the path coincide for any finite number of F-steps. This is a genuine **operation-safe quotient** of the source-count fiber for the declared fixed-count V27 active-triad update.

Proof: Φ_X factors exactly through T(X) because its only dependence on X occurs via u and Ω. Hence the nine scores and their ordered maximizing branches are identical at each S. With X held fixed, induction in the number of updates yields identical active-triad sequences. V17 holonomy is a deterministic ordered composition of shared-axis frame transports and therefore is identical for identical ordered paths. The proof is uniform in X and X' and does not assume positivity of signed contrasts.

Crucial observer typing: The ten-dimensional T is sufficient to predict this declared S-dynamics and its path-derived holonomy **if S and the ordered path are retained**. T alone, with no starting active triad or path record, is not a complete state for those history-dependent outputs. R640's 14-dimensional kernel remains relevant when a future action reads/updates individual I,O,M components or source provenance.

## Exact V27 six-cycle witness and full kernel-family test

Use V27's explicit typed nonnegative counts:

I=(0,0,0,10), O=(2,4,3,0),
M_01=M_12=M_20=1, all other M_ij=0.

Then u=(-2,-4,-3,10) and

Ω=((0,1,-1,0),(-1,0,1,0),(1,-1,0,0),(0,0,0,0)).

The V23 exact four-field matching code and the V27 score choose a unique maximizer at every one of 20 active triads. In particular the recurrent odd six-cycle is

012→123→234→034→035→025→012,

with V17 holonomy permutation (2,1,0) and odd Ori6 charge; the separate 145↔245 two-cycle has identity holonomy.

For each of the 14 R640 integer-kernel basis vectors, add one unit to the V27 nonnegative I/O/M source. These 14 new states are distinct from the original, remain nonnegative, have identical u,Ω, and yield the same entire V27 successor table. Re-run 20 start states through 12 relation steps and compare at every step against the original: 14×20×(1+12)=**3,640 exact transition checks**. The attached Python stdlib checker R641_V27_VERIFY.py reconstructs the V23 code, source contrasts, exact candidate maxima and V17 slot holonomies, and verifies the full finite witness without floating point. Marker: R641_PF10_V27_UPDATE_CONGRUENCE_EXACT_PASS.

## New continuation question

The extant V27 checker **holds PF10 I/O/M counts constant while updating S**; the checked law is F(S,X)=(g_X(S),X). Inspect the project V28–V43 event ledger and field-network papers for a separate, actual update `X→X'` that changes counts with source/port provenance. For such a coupled update, test whether T(X') is determined by T(X), active S and allowed context; if not, supply a concrete same-T different-next-T counterexample and retain the corresponding portion of R640's 14-dimensional repair or another operation-safe invariant. Do not infer a six-dimensional physical evolution law from this auxiliary internal update.

This theorem uses the signed PF10/BRC contrast already present in source, preserves branch and signed orientation, and does not modify P000/ACTIVE worldview. The frozen R462 K coefficients are retained for future signed-branch comparison but not re-used in the PF10 relation update calculation.