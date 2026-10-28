# D25/LIFT GH-76: all-prime double-pole cancellation for the p ≡ 3 (mod 8) Laurent resolvent

2026-10-29 Asia/Hong_Kong. **AUTHOR-DERIVED / SOURCE-COROLLARY / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is a new cross-branch corollary of GH-15/16, GH-17/18 and the newly proved author-side GH-74/75 CM–Cartier prime-class selection law. It is a portable mathematical result, not native Source acceptance, Result, or Driver review. Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION stays OPEN, task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. The stable Research lane is chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance.

## Statement and complete short proof

Let p ≥ 11 be any prime with p ≡ 3 (mod 8), write p = 8m+3 and d = (p-3)/4 = 2m, and fix the ORIGINAL GH-15/16 rational cyclic resolvent R_9(x) over F_p at z=9. For each rank 0 ≤ r ≤ d, its Laurent expansion at x=r+ε is

R_9(r+ε)=A_r ε^{-2}+B_r ε^{-1}+H_r+O(ε).

GH-15 supplies C_r A_r=A and C_r ∈ F_p^× throughout the genuine finite rank window. GH-16 proved the exact global obstruction

A = (α_p 9^{2d+2}/8) · \mathcal H_d(9),

with α_p ∈ F_p^× and the distinct obstruction polynomial \mathcal H_d(z)= Σ_{s=0}^d (8s+5)(3/4)_s^3 z^s/[s!(5/4)_s(3/2)_s].

Since d=2m, GH-17 gives the FULL polynomial factorization \mathcal H_d(z)=F_m(z)G_m(z) in F_p[z], preserving two distinct labeled channels. The newly author-proved GH-75 applies to every such prime and divides them into disjoint classes:

* p≡11 (mod 24): G_m(9)=0, F_m(9)≠0;
* p≡19 (mod 24): F_m(9)=0, G_m(9)≠0.

Thus for EVERY prime p≡3 (mod 8), p≥11, \mathcal H_d(9)=0 and hence A=0. Because each C_r is a unit, ALL rank double-pole coefficients A_r=0. GH-15 proves that at rank d+1 the successor Laurent residue V_{-1} also vanishes because A=2z C_d V_{-1} (z=9 is a unit). Consequently, the unique GH-13/GH-15 rational cyclic resolvent R_9(x) is at worst **simple-polar at each genuine finite rank** and regular at the successor rank d+1.

This is a **uniform all-prime theorem on the p≡3 (mod8) subfamily**. It does not invoke the original truncation T_{p,9} as an assumption, or a finite-sample extrapolation. It is conditional only on the mathematical correctness of the cited author proof chain; formal independent review and native admission have not yet occurred.

## Precise surviving first-order obstruction

Retain GH-15's first logarithmic source moment L = Σ_{r<d}ℓ_r and its genuine Laurent residue B=B_0. With A=0, the source-preserving finite-window identity simplifies, but does NOT disappear:

T_{p,9} = C_d(H_d + (8d+1)) - H_0 + B L  in F_p.      (GH-76b)

The symbols H_0,H_d are GH-15's finite Laurent constant terms of R_9, not the GH-73 elliptic Hasse polynomial H_p(T) or GH-16 obstruction polynomial \mathcal H_d. The endpoint and BL term must remain. For the executed earlier exact GH-15 samples, p=19 gives B=8, L=14, BL=17 mod19; p=43 gives B=29, L=16, BL=34 mod43. Therefore "double pole vanishes" does not imply a pole-free Gosper certificate, nor does it independently establish T_{p,9}=0.

The distinct p≡7 (mod8) subfamily of p≡3 (mod4) is OUTSIDE the GH-17 Clausen half-degree factorization scope and remains a separate arithmetic obstruction. The original GH-3 p≡3 (mod4) all-prime truncation, GH-20/21 second digits, W/S, six Hasse channels, R23/R36 Green coupling and native p=373 H0/B0 experiment remain individually OPEN.

## BRC / observer and next proof action

**BRC COMPOSE_APPLIED:** preserve (p,d,r,z), source weights C_r, signed F/G labels, obstruction \mathcal H_d, Laurent orders A_r/B_r, first moment L, constant terms H_0,H_d, and successor rank d+1. The observer operation is exact rankwise Laurent extraction followed by source-weighted finite summation. The A=0 projection is safe only for the pole-order-2 output; collapsing B or endpoint terms destroys the future T_{p,9} observer. This is an external auxiliary scalar chart and makes no claim about native six-dimensional X6 Cell geometry. P000 ACTIVE remains unchanged.

**Next precise question:** for all p≡3 (mod8), seek an independent arithmetic identity cancelling the THREE separate remaining contributions C_d(H_d+8d+1), -H_0 and BL, without recycling the original T sum as its own certificate. For p≡7 (mod8), first derive an appropriate arithmetic obstruction method, without incorrectly extending GH-17.

## Immutable inherited author-side evidence

- GH-15/GH-16 proof: research_notes/portable_direct/20261028_hourly_d25_gh15_gh16_finite_laurent_counterterm.md, previously verified at enterprise-math main, fixed prior commit c5fab90f2bbe1cbe8581cef4179aa532cf040388.
- GH-17 factorization: research_notes/portable_direct/20261028_hourly_d25_gh17_gh18_clausen_half_gauss_coprime.md, existing commit c9732de542130f4d376f9833973b1538b1306d47.
- GH-74/GH-75 complete new arithmetic proof: research_notes/portable_direct/20261029_hourly_d25_gh74_gh75_cm_cartier_split_proof.md, commit 6a7cbaebed0ca6ce1050bb97047e320569e41200, Git blob bab2ce095ae967251e36dc1ce8b5a31c48780ea6. Independent finite-field checker path 20261029_hourly_d25_gh74_gh75_cm_cartier_check.py.
