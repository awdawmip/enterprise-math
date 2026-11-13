# A3 all-scale orbit naturality and intrinsic quotient-square classification

**Date:** 2026-11-13. **Status:** new self-contained Driver mathematical audit at A3 restricted-carrier strength; not a Native Review or replacement for the original frozen Result.

**Original attribution:** Task `RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION`; publication `TP2-D2D715EB36415B0CA0C5`; Result `RR-9FF7F84F01C577774649`; researcher `EM-A3SCR-7A41D2`. The original return and its exact radial defect formula remain the source of the problem and classification. This proof upgrades its finite quotient-path census to an all-radius theorem and separates two notions of quotient naturality. It builds on the Driver's earlier [single-probe quotient descent theorem](2026-11-13_a3_single_binary_probe_centralizer_theorem.md), from the same shared review context; it is **not** a second independent review.

## 1. Typed model and two questions

Use the A3 restricted carrier
[
 B_n={xinmathbb Z^4: sum_{i=1}^4 x_i=0,quad|x|_inftyle n},quad S_r=B_rsetminus B_{r-1}.
]
Let (ho_g=operatorname{sgn}(g)P_g) for (gin S_4), let (h=(12)), and let (H={e,h}) act globally through (ho_h) on the finite carrier. Put (X_n=A^{B_n}), where **(|A|ge2)**, with the pushforward convention (T_*f=fcirc T^{-1}). The projection (pi_n:X_n	o X_n/H) forgets only this declared residual-(H) orientation.

For (1le dle n), (D_{n,d}(g)) acts by (ho_g) on shells (rge n-d+1), and by identity below. The restriction (J_n:X_{n+1}	o X_n) is (H)-equivariant. Fix (g_-) for the lower depth-(d) action and (g_+) for the upper depth-(d) action; set (q=n-d+1).

We distinguish:

**(O) Output-orbit equality:** for *every* upper state (fin X_{n+1}),
[
pi_n(J_n D_{n+1,d}(g_+)_*f)
=pi_n(D_{n,d}(g_-)_*J_n f).
]
Both sides are defined as paths followed by a **final** quotient. This comparison does not presuppose that either intermediate (D) descends to a quotient.

**(Q) Intrinsic quotient-square:** both (D_{n+1,d}(g_+)) and (D_{n,d}(g_-)) induce their own well-defined operators on (X_{n+1}/H) and (X_n/H), and these induced maps commute with the induced restriction. This is a strictly typed square of quotient operators.

## 2. General orbit-rigidity lemma

**Lemma.** Let (Y) be finite and let (h:Y	o Y) be an involution. Let (Kinoperatorname{Sym}(Y)). With at least two label values, the condition
[
 orall fin A^Y,quad K_*fin{f,h_*f}
]
is equivalent to (Kin{mathrm{id},h}).

**Proof.** Choose two distinct labels. For the indicator state of a singleton (x), the condition forces (Kxin{x,hx}). Injectivity of (K) implies that on each two-element (h)-orbit, (K) is either identity or its transposition; each fixed point is fixed. If two distinct two-element orbits received different choices, the two-site indicator state with one marked point in each orbit would be sent to neither itself nor its global (h)-image. Hence the choices agree across all two-element orbits. Therefore (K=mathrm{id}) or (K=h) on all of (Y). The cases with zero or one two-element orbit are immediate. The converse is tautological. QED.

In particular, equality of **every** two-path output orbit forces their carrier difference to be one single global residual element. Arbitrary shellwise or orbitwise uses of (h) cannot replace the same global (h).

## 3. A3 shell faithfulness

On every (S_r), (rge1), the signed (S_4) action (ho) is faithful. Indeed, the three roots (r(e_i-e_4)), (i=1,2,3), lie in (S_r) and span the sum-zero standard three-space. If (ho_g) fixed (S_r) pointwise, it would act trivially there. For even (g), this requires (P_g=I), so (g=e). For odd (g), it would require (P_g=-I) on the standard space, which is impossible: its trace would be (-3), whereas the standard permutation trace is (#mathrm{Fix}(g)-1ge-1). Thus (g=e). Also (ho_h) is nontrivial on every (S_r), since it sends (r(e_3-e_4)) to its negative.

Both (ho_g) and (ho_h) preserve each shell and fix the origin.

## 4. Universal classification of (O)

Let (U) and (L) be the two carrier permutations of (B_n) induced respectively by upper-then-restrict and restrict-then-lower. The original A3 shell calculation gives their difference (K=LU^{-1}):
[
K|_{S_r}=
egin{cases}
ho_e,&r<q,\
ho_{g_-},&r=q,\
ho_{g_-g_+^{-1}},&q<rle n.
end{cases}
]
Because restriction (J_n) is surjective on label states, (O) is equivalent to (orall uin X_n, K_*uin H_*u). By the lemma, (K=ho_e) or (K=ho_h) **globally** on (B_n).

- If (qge2), the inner shell (S_1) has (K=ho_e), while (ho_h) acts nontrivially there. Thus (K=ho_e) globally. Shell (S_q) forces (g_-=e); when (dge2), overlap shell (S_{q+1}) additionally forces (g_+=e).
- If (q=1), the shell (S_1) forces (g_-in H). If (nge2), the overlap shell (S_2) must carry the **same** global (H) element, forcing (g_+=e). If (n=1), the upper aligner never acts on retained sites and is unrestricted.

Hence for every integer (nge dge1), without a finite-radius cutoff:

| Geometric regime | Exact output-orbit equality (O) |
|---|---|
| (qge2, d=1) | (g_-=e), arbitrary (g_+in S_4) |
| (qge2, dge2) | (g_-=e, g_+=e) |
| (q=1, nge2) | (g_-in H, g_+=e) |
| (n=d=1) | (g_-in H), arbitrary (g_+in S_4) |

This upgrades the original exact finite census for (O) to a universal statement in the explicitly defined A3 carrier model. It does not use the invalid frame-only (Hg_-g_+^{-1}H) criterion.

## 5. Universal classification of (Q)

The earlier single-binary-probe theorem gives, for every nonempty active shell and (|A|ge2),
[
D_{m,d}(g)	ext{ descends to }X_m/H
 Longleftrightarrow 
gin C_{S_4}(h)={e,(12),(34),(12)(34)}.
]
Therefore (Q) holds exactly when (O) holds **and both aligners belong to this centralizer**. The complete classification is:

| Geometric regime | Exact intrinsic quotient square (Q) |
|---|---|
| (qge2, d=1) | (g_-=e, g_+in C_{S_4}(h)) |
| (qge2, dge2) | (g_-=e, g_+=e) |
| (q=1, nge2) | (g_-in H, g_+=e) |
| (n=d=1) | (g_-in H, g_+in C_{S_4}(h)) |

**Sharp boundary witness:** (n=d=1, g_-=e, g_+=(23)) satisfies (O) because (g_+) acts only on the dropped outer shell. But (g_+
otin C_{S_4}(h)), so the upper operator has no quotient descent, and no intrinsic quotient-square (Q) exists. This distinguishes a valid comparison after restriction from an invalid claim about operators on quotient spaces.

The all-scale classification and the normalizer criterion concern this restricted A3 observer. In the project's native HEARTBEAT_WORLD X6 model, any stronger spatial/observer interpretation requires an explicit embedding/readout and preservation of the declared future-operation horizon; none is inferred here.

## 6. Independent finite regression and exact counting

An independent local Python exact-integer permutation check enumerated **all 24×24 aligner pairs** for every (1le dle nle4), evaluating the actual carrier (K) over every site of each shell and testing whether (K) was globally (e) or (h). No floating point arithmetic was used. Results:

| ((n,d)) | ((1,1)) | ((2,1)) | ((2,2)) | ((3,1)) | ((3,2)) | ((3,3)) | ((4,1)) | ((4,2)) | ((4,3)) | ((4,4)) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Number satisfying (O) out of 576 | 48 | 24 | 2 | 24 | 1 | 2 | 24 | 1 | 1 | 2 |

All **5,760** pair/regime checks agreed with the analytic classification. For the ten regimes, the corresponding (Q) counts are (8,4,2,4,1,2,4,1,1,2), by intersecting the verified (O) pairs with the four-element centralizer for both aligners. This finite regression catches implementation or sign errors; §§2–5, not the finite count, prove the arbitrary-radius theorem.

## 7. Review and portfolio implications

The original A3 frozen Result remains attributed to its original researcher and is kept byte-for-byte. The present proof strengthens the exact quotient output-orbit classification, clarifies a prior domain-of-definition ambiguity, and supplies the intrinsic quotient-square alternative. A future native review should adjudicate the originally frozen Result **with its precise original claims**, the already documented alphabet and faithfulness hypotheses, the original hard-target criteria, and this supplemental proof as provenance-disclosed context. It should not label the new theorem a second independent review pass.

**State at publication:** mathematical Driver audit/check complete. Native Result review/acceptance, Task DONE and mother Objective closure are separate pending decisions. The original review-flow attempts returning `DRIVER_FLOW_CURRENT_RESULT_REQUIRED` are preserved; no new review or follow-up packet is asserted by this note.
