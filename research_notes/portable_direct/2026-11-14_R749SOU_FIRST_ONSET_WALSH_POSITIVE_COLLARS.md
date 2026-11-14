# R749SOU — Two exact positive-gap onset collars from the first Walsh threshold

**Date:** 2026-11-14. **Scientific status:** AUTHOR_ANALYTIC_NOT_REVIEWED.
**Frozen science:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
**Exact dependencies:** R749SOS–SOT, [PR #2399](https://github.com/awdawmip/enterprise-math/pull/2399) @ `5f2830988e31eae99d9ef11882e626b56b022552`; source-fiber transport in R749SOG, [PR #2376](https://github.com/awdawmip/enterprise-math/pull/2376).
**Model:** frozen auxiliary 16-atom Walsh source observer; no native X6/V29/V39 correspondence asserted.

## Definitions and theorem

Let (kinmathbf F_2^4), (chi_m(k)=(-1)^{mathrm{popcount}(mmathbin{&}k)}), (A=chi_3), (B=chi_{12}), (C=chi_{15}=AB). Define the complete compatible fiber

[
F_{t,s}=left{p_{t,s,h,u,v,w,z}(k)=rac{1+tA(k)+sB(k)+hC(k)+uchi_1(k)+vchi_2(k)+wchi_4(k)+zchi_8(k)}{16}ge0quadorall kight}.
]

The full-simplex free and fiber-calibrated minimax TV radii are
[
ho(t,s)=inf_{qinDelta_{16}}sup_{pin F_{t,s}}mathrm{TV}(p,q),qquad
ho^{mathrm{cal}}(t,s)=inf_{qin F_{t,s}}sup_{pin F_{t,s}}mathrm{TV}(p,q),qquad
g=ho^{mathrm{cal}}-ho .
]

Put (t_*=5/22), (G(t)=(22t-5)/48), and consider
[
mathcal W_t={(t,s):5/22<tle1/4, |s-1/2|le G(t)/8},quad
mathcal W_s={(t,s):5/22<sle1/4, |t-1/2|le G(s)/8}.
]

**Theorem (all real parameters).** Every point of (mathcal W_t) satisfies
[
oxed{g(t,s)ge rac{371}{6128}G(t)>0.}
]
Every point of (mathcal W_s) satisfies the same bound with (s) replacing (t). On the lower side (sle1/2) of (mathcal W_t) there is the stronger (g(t,s)ge G(t)/16). These are disjoint triangular regions, each of area (1/33792), total area (1/16896). Their apexes, ((5/22,1/2)) and ((1/2,5/22)), lie on the zero-gap locus by the exact line theorem.

The first triangle has bounding rays
[
s=rac12pmrac{11}{192}left(t-rac5{22}ight),quad 5/22le tle1/4;
]
its largest half-width is (1/768).

## Proof

**1. Exact line value.** R749SOT established on the entire real interval (5/22le tle1/4):
[
ho(t,1/2)=rac{7-2t}{16},qquad ho^{mathrm{cal}}(t,1/2)=rac{1+t}{3},qquad g(t,1/2)=G(t).
]
This uses the pinned source-pair TV lower bound, event-dual calibrated lower bound, and explicit affine centers with full exact rational joint-vertex certificates. Here (0le G(t)le1/96).

**2. Compatible-fiber transport.** For (0le t,s<1) let
[
r_{t,s}(k)=rac{1+tA(k)+sB(k)+min(t,s)C(k)}{16}.
]
Examining the four ((A,B)) groups gives (min_k r_{t,s}(k)=(1-max(t,s))/16). Fix (t), start with any (pin F_{t,s_0}), set (d=|s_1-s_0|), (alpha=d/(1-max(t,s_0))le1) and
[
Phi(p)(k)=(1-alpha)p(k)+alpha r_{t,s_0}(k)+rac{(s_1-s_0)B(k)}{16}.
]
Every atom of (alpha r) is at least (d/16), so (Phi(p)ge0). Walsh orthogonality preserves unit mass, (A) moment (t), the legal zero moments and all required moments except (B), which becomes (s_1). Thus (Phi(p)in F_{t,s_1}). Also
[
mathrm{TV}(p,Phi(p))lealpha,mathrm{TV}(p,r)+d/2lealpha+d/2.
]
Using the same construction in reverse yields the exact two-way Hausdorff estimate
[
H(F_{t,s_0},F_{t,s_1})le rac{d}{1-max(t,s_0,s_1)}+rac d2.
]

**3. Radius stability and positivity.** The free minimax TV radius is (1)-Lipschitz in the fiber's TV-Hausdorff distance: keep the old center and approximate each source. The calibrated radius is (2)-Lipschitz: approximate the center as well as the sources. Applying in both directions gives
[
g(t,s_1)ge g(t,s_0)-3H.
]
In our triangle (d=|s-1/2|le G(t)/8le1/768), and (tle1/4<1/2-d), hence both transports apply and
[
Hlerac{d}{1/2-d}+rac d2.
]
For (G=G(t)>0), this yields
[
egin{aligned}
g(t,s)&ge G-3left(rac d{1/2-d}+rac d2ight)\
&ge Gleft(1-rac3{4-G}-rac3{16}ight)\
&ge Gleft(1-rac{288}{383}-rac3{16}ight)
=rac{371}{6128}G>0 .
end{aligned}
]
When (sle1/2), the minimum of the two reference margins is (1/2), giving (Hle(5/2)d) and (gge G-(15/2)dge G/16).

**4. Swap symmetry and area.** Exchange the two low bits of (k) with the two high bits. This permutation swaps (chi_3leftrightarrowchi_{12}), fixes (chi_{15}), and swaps ((chi_1,chi_2)leftrightarrow(chi_4,chi_8)). It bijects (F_{t,s}) with (F_{s,t}) and preserves TV and both optimization domains. Therefore, for **all real (0le t,sle1)**,
[
ho(t,s)=ho(s,t),quad ho^{mathrm{cal}}(t,s)=ho^{mathrm{cal}}(s,t),quad g(t,s)=g(s,t).
]
This proves the second positive collar. As (1/4-5/22=1/44), the first triangular area is
[
int_{5/22}^{1/4}rac{G(t)}4,dt=rac1{33792}.
]
The triangles are disjoint: the first has (tle1/4), (sge1/2-1/768>1/4), and the second reverses the roles. Their combined area is (1/16896).

## Verification, interpretation and open problem

Run `python research_notes/portable_direct/R749SOU_WALSH_ONSET_COLLARS_EXACT_CHECK.py` (Python 3, standard library only). Its companion `R749SOU_WALSH_ONSET_COLLARS_RESULTS.json` reports PASS. The checker uses `Fraction` for all arithmetic, validates constants, endpoints, positivity and exact TV estimates in 40 explicitly mapped two-way source transports, and tests the complete 16-atom Walsh bit-swap. The analytic inequalities and the pinned R749SOS–SOT exact line theorem supply the universal real-parameter proof. The finite examples are a regression check, not a numerical substitute for those arguments.

**Scope:** author-side mathematical result in the frozen auxiliary source model, awaiting independent review and native X6/V29/V39 typed observer correspondence. **Next discriminating question:** determine the exact neighboring polyhedral minimax chambers and matching event-dual certificates at ((5/22,1/2)), including whether the actual two-dimensional (g=0)/(g>0) boundary has a corner.
