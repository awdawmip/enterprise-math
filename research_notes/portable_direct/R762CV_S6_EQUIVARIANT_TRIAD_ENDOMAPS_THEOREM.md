# R762CV — Complete S6-equivariant signed-triad candidate update classification

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Researcher: EM-X6-3050F6; original Run RUN-2f66fcc8f96765967a2e8cae.
Date: 2026-11-17. Grade: complete elementary proof and author-side exact finite verification; independent review NOT_REVIEWED.

## Frozen source and exact scope

Frozen P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md.
Original taskbook: @e3f42efac29a2da2d95be391f3231a664e2fade0.
Predecessor R762CU: Draft PR #2620, commit 15374751a4ce6931b5a4bc83f68c27f756320bb6.

This exact finite theorem concerns only the already-declared signed X6 *candidate Force-Port triad* carrier. S6 acts by permuting native axes (signs unchanged). It provides **candidate deterministic update laws** to test against a future sourced native TRIADIC_CLOSURE_E event rule. Nothing in the proof licenses a particular native event or V17/V29/V39 transport.

Let I={1,...,6}. Let Ω be the 160 unsigned-order, signed-support triads T={(i₁,ε₁),(i₂,ε₂),(i₃,ε₃)}, with distinct axes and ε_j ∈{+,-}. Let Ω_k denote the 20,60,60,20 triads having exactly k negative signs (k=0,1,2,3). A deterministic unmarked S6-equivariant update is F:Ω→Ω such that F(gT)=gF(T). State contains only the signed triad, without a distinguished Port, trajectory memory, Cell/Link decoration or hidden source tag.

## Theorem 1 — exact count of deterministic S6-equivariant candidate updates

The exact number of all such self-maps F is

\[
\boxed{4\cdot6\cdot6\cdot4=576.}
\]

The choices per source orbit Ω_k are (4,6,6,4).

**Proof.** Fix T in Ω_k and partition the six axes into A (k negative), B (3-k positive), C (3 unused). Its stabilizer is H=S_A×S_B×S_C. For a transitive G-set G/H, G-equivariant maps to any G-set X are in bijection with H-fixed points of X: the representative's target must be H-fixed; conversely each fixed target determines gT↦g(target), independently of the representative g. Here X=Ω.

An H-fixed signed target triad includes every axis of a block A,B,C or none, and any included block has a constant sign. Exactly three axes must be included. For k=0 or 3, the nonempty blocks have sizes 3 and 3, so choose the original support or its complement, with either common output sign: 2×2=4 choices. For k=1 or 2 the block sizes are 1,2,3, so the only size-three support combinations are A∪B (two independently chosen signs: 4 choices) and C (one common sign: 2 choices). Thus six. The four disjoint domain orbits have independent restrictions, yielding 4×6×6×4=576. ∎

## Theorem 2 — five exact restricted families

| Constraint on F | Per-k candidate counts | Global maps |
|---|---|---:|
| S6-equivariance | 4,6,6,4 | **576** |
| Preserve the occupied three axes | 2,4,4,2 | **64** |
| Preserve number k of negative Ports | 2,1,1,2 | **4** |
| Also commute with simultaneous sign reversal (without k preservation) | k=3 follows k=0; k=2 follows k=1 | **24** |
| Preserve k and commute with simultaneous sign reversal | homogeneous pair coupled; mixed signs fixed | **2** |

**Proof.** In the exhaustive H-fixed list above, retaining original support leaves (2,4,4,2) maps on the four domain orbits. Under k preservation, mixed signs have only the original assignment on A and B: their alternative support C must be uniformly signed, so it would have zero or three negatives. Homogeneous triads retain either their original support or their complement with the original common sign. This gives (2,1,1,2). Simultaneous sign flip sends Ω_0↔Ω_3 and Ω_1↔Ω_2 and commutes with S6. Requiring F(-T)=-F(T) uniquely determines the latter restrictions from the former and reduces the counts to 4×6=24; together with k preservation it gives 2×1=2. ∎

## Corollary 3 — exact mixed-sign rigidity

Under S6-equivariance, sign-count preservation and simultaneous sign reversal covariance, there are exactly two unmarked deterministic candidate updates:

* identity everywhere;
* J, equal to the identity on every mixed-sign triad and equal to the *support-complement involution* on every homogeneous triad (the three unused axes inherit the common sign).

They both square to identity. In particular, no mixed-sign candidate can change under a deterministic update satisfying all three properties without an additional state or relaxing an assumption.

This is a sharp conditional incompatibility test for any future sourced event licence. **It is not a universal prohibition on native rotations:** in particular sign-count conservation and global reversal may not be properties of the actual event. Nor does this contradict R762CU's 3-sheeted homogeneous chosen-Port repair: a map on whole triads is a different output type from selecting an individual Port.

## BRC scope, proof interface and future-observer question

This is a one-branch N-BRC candidate carrier: each T has the unique successor F(T) with positive multiplicity one. If native dynamics instead selects a specific source Port, the R762CU tag/branch identities or an equivalent lossless repair are required. Port choice, native ordered path, signed area, multiplicity and Cell decoration remain visible when the intended observation depends on them. No quotient of that full observer language follows from these 576 combinatorial possibilities alone.

New discriminating question: given an exact legal TRIADIC_CLOSURE_E Cell/Link/Port rule and V17/V29/V39 transport, determine whether its transition on the signed-triad fragment is deterministic, S6-covariant, sign-count-preserving and reversal-covariant. If so, the present two-law classification is a complete test. If not, retain the needed native source, Port and pair-area residuals and compute the minimal observer-safe BRC state for actual licensed words.

## Exact verification and durable frontier

R762CV_VERIFY.py is standard-library Python, enumerating all 160 states, all 720 group elements, stabilizers of sizes 36/12/12/36 and their fixed target sets. It independently constructs each of the 20 local orbit-equivariant candidate maps and verifies **633,600** covariance equalities. The nonidentity involution J is also checked against 115,200 covariance equalities, all 160 square-to-identity, k-preservation and sign-reversal conditions. R762CV_EVIDENCE.json contains the counts. No float arithmetic is used. Theorem is proved for the full finite signed candidate population; no extrapolation from sampling is made.

Already completed and not repeated: R762CU optimal 240 selected-Port cover, R762CT source-resolved BRC theorem, R762CH/CK signed pair-area provenance. New full classification here is the next reusable candidate-law filter. Native-law selection and independent review remain pending.