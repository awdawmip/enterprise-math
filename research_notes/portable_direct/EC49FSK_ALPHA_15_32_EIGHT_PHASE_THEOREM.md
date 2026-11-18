# EC49FSK — 原生 BRC16943 双价格八相区定理（α=15/32）

Date: 2026-11-18. Scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Inherited exact frontier: EC49FSJ, PR #2691, immutable commit `54324197c6566c5e3ac17b530b0b744f2b473400`.
Research scope: **finite native named-observer identification decision-tree model**, 141 named profiles, 310 original configurations, all 228 physical named observations. Uniform prior. No replacement by anonymous binary questions, no thinning of physical named-observer set.

## Statement

Let (t>0). q32 and q34 each cost ((1-15/32)t=17t/32), and q140 costs ((1-z)t) for an independent real discount (z\in[0,1]). All other named observations cost (t). Trees must be finite, deterministic, adaptive, complete, and correctly distinguish each of the 141 source profiles. Define (F(z)=141\mathbb E[\mathrm{cost}]/t) minimized over all such trees.

Then, for **every real** (z\in[0,1]),
[
 F(z)=
 \begin{cases}
 306-182(15/32)-10z,&0\le z\le 1/6,\\
 308-182(15/32)-22z,&1/6\le z\le39/224,\\
 305-173(15/32)-29z,&39/224\le z\le7/24,\\
 304-169(15/32)-32z,&7/24\le z\le5/14,\\
 309-169(15/32)-46z,&5/14\le z\le2/5,\\
 311-169(15/32)-51z,&2/5\le z\le15/32,\\
 311-151(15/32)-69z,&15/32\le z\le563/1152,\\
 319-93(15/32)-141z,&563/1152\le z\le1.
 \end{cases}
]
Every open interval has a unique optimal *cost vector* ((U,Q,K)) among the eight witnesses listed above, where (U) is the total number of observations across the 141 paths, (Q=N_{32}+N_{34}), and (K=N_{140}). Hence **eight distinct fixed-tree cost types are necessary and sufficient** for the entire slice (trees of the same cost type can be nonunique).

The exact endpoint optimum values, ordered by
(z=0,1/6,39/224,7/24,5/14,2/5,15/32,563/1152,1),
are
(3531/16,10513/48,1532/7,20683/96,47791/224,33821/160,1663/8,79295/384,4301/32).

## Constructive optimality and finite exhaustion

1. The original source data are `EC49FPG_PROFILE.csv` (SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`) and `frozen_original_master.txt` (SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`). Both reconstruction decoders in the inherited source code agree on the 228 fully named response vectors of length 141. The pin is unchanged.
2. Exact integer-scaled **228-observer** Bellman dynamic programming was actually run at all nine exact rational breakpoints. Their computed results are reproduced in `EC49FSK_EXACT_CERTIFICATE.json`, with individual point receipts in the accompanying full evidence archive. The finite dynamic program enumerates all informative source-named questions for every encountered profile subset; a one-profile subset has zero future cost. The recurrence counts the length-weighted total price of the question plus optimal children, and integer scaling removes numerical approximation.
3. Eight actual complete native-tree witnesses attain the claimed affine costs; each was replayed against all 141 profiles, checking response labels, unique terminal profile, and no repeated named observation on a path. The maximal depth is four. The lossless witnesses are available as `EC49FSK_EIGHT_WITNESS_TREES_ZLIB_BASE64.txt`; the full source, scripts, receipts and tree JSON are included in the offline self-contained package.
4. Let (G(z)) be the infimum of the affine total costs of **all** legal complete trees. It is concave, and the eight witness envelope (L(z)) satisfies (G(z)\le L(z)). At each of the nine exact rational vertices Bellman exhaustion establishes (G(z_i)=L(z_i)). On each interval ([z_i,z_{i+1}]) one witness is affine and equals (L) throughout, so concavity yields (G(z)\ge L(z)) there. Consequently (G=L) at every real point in ([0,1]). Distinct open-interval slopes (K\in\{10,22,29,32,46,51,69,141\}) force at least eight distinct cost types.

## Validation, interpretation, and next unresolved question

- Local certificate checker output: `PASS`, nine endpoint receipts match the eight-tree envelope; 8/8 trees are replayed over 141/141 source profiles; max tree depth 4; original 228 named partitions retain their exact response identities.
- At (z=0,1/6,39/224,7/24), a second decoder with an independently implemented exact Bellman solver completed and returned the same values. The remaining five points were checked with the primary exhaustive solver and complete witnesses; their **second-decoder** calculations were not completed after the computational timeout. This distinction is retained in the manuscript and logs.
- The theorem concerns the pinned finite identification model. It is not a claim that q32, q34 or q140 are physical time steps or that a new native X6 spatial direction has been added. P000 / Heartbeat World and joint observer-provenance requirements are preserved.
- Mathematics status: `AUTHOR_PROVED / EXACT_FINITE_PRIMARY_CHECKED / INDEPENDENT_PARTIAL / NOT_REVIEWED`. No formal Task publication, CLAIM, Result, Review or Activity checkpoint is asserted by this portable research file.

**Next:** classify the joint ((\alpha,z)) corridor (\alpha\in[7/16,1/2]), (z\in[0,1]), using the newly certified `15/32` slice as an additional interior anchor. In particular determine whether the eight cost types persist, whether interior positive-area cost types appear, and all exact rational vertices of the lower-envelope subdivision. This is a proposed direction, not a preassigned conclusion.
