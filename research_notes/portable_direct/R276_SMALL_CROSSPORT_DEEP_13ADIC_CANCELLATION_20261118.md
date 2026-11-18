# R276 — Arbitrarily deep 13-adic cancellation from arbitrarily small positive cross-Port edges

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED.
Scientific lineage: R275 (same branch), R273–R274@f9a93873f1b8d724519434a660f70c91971229b0; frozen scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Typed setting: finite strictly recurrent BRC matrix with three distinct, **visible labeled Ports** and rational nonnegative edge masses. WBRC-T30/T31/T32 are reused without revising them.

## The problem and the exact reduction

Use directed weights

```
W(P,u)=[[0,1/4,1/4],
        [2/(1+P),0,u],
        [2/(1+P),u,0]],
P=13^t, t>=1, u>=0.
```

For any `u` with `2/(1+P)+u<1`, every row sum is strictly below 1 and the recurrent star exists. Write

```
D(P,u)=det(I-W)=P/(1+P)-u/(1+P)-u^2,
S_00(P,u)=(1-u^2)/D(P,u).
```

The determinant is the exact signed cycle-cover expression from R275. The `-u/(1+P)` term is the combined weight of two new directed triangles; the `-u^2` term is the new nonhub 2-cycle. Both retain their actual positive edge provenance before determinant signs are taken.

The original `u=0` graph has `D=P/(1+P)`, `S_00=(1+P)/P`, hence `v13(S_00)=-t`.

## Theorem A — generic two-scale phase law

Assume `u>0` is a positive rational with nonnegative strict-stability condition above and `r=v13(u)>=1`. If `r!=t`, then

```
v13(D(P,u))=min(t,r),
v13(S_00(P,u))=-min(t,r).
```

For the critical scale `r=t`, write `z=u/P` (a 13-adic unit). If `z != 1 (mod 13)`, then `v13(D)=t` and `v13(S_00)=-t`; if `z == 1 (mod 13)`, the first nonzero determinant coefficient is at a higher 13-adic order, and its actual order must be computed.

**Proof:** `D=P/(1+P)-u/(1+P)-u^2`. The valuations of the three terms are `t,r,2r`; for `r!=t` the minimum is unique. Since `v13(1-u^2)=0`, the star valuation is the negative determinant valuation. For `r=t`, divide by P and reduce mod13: `D/P == 1-z (mod 13)`. This also demonstrates precisely where cancellation can occur, without declaring every critical-scale case resonant.

## Theorem B — arbitrary extra depth at vanishingly small real cross-edge mass

For arbitrary **independent** integers `t,h>=1`, set

```
P=13^t,  M=1+13^h,
u=P/[M(1+P)].
```

All weights are positive rationals. Each row sum is strictly below 1: the hub row sum is `1/2`, and each other row has sum `[2+P/M]/(1+P)<1` for the stated P,M.

The following is an *exact* identity:

```
D(P,u)=P(M-1)[M+P(M+1)]/[M^2(1+P)^2].
```

As `v13(P)=t`, `v13(M-1)=h`, and `M+P(M+1) == 1 (mod 13)`, while the denominator is a 13-adic unit,

```
v13(D)=t+h,
v13(S_00)=-(t+h),
13^(t+h) S_00 == 1 (mod 13).
```

In particular, **for every fixed t and every real epsilon>0** one may choose h arbitrarily large so that `0<u<epsilon`, yet the normalized 13-adic Port response has pole depth `t+h` and grows without bound as h increases. Compared with the `u=0` baseline, the two added crossed Port edges increase pole depth by exactly `h` digits.

**Proof:** Substitute u into the determinant. Multiplying by `M^2(1+P)^2` gives
`P[M^2(1+P)-M-P] = P(M-1)[M+P(M+1)]`.
The valuation formula follows because M, 1+P, and the bracket are 13-adic units. The numerator `1-u^2` is also a 13-adic unit. Finally
`13^(t+h)S_00=(1-u^2)M^2(1+P)^2/[M+P(M+1)] == 1 (mod 13)`.
The real weight u tends to zero for fixed t as h tends to infinity; the strict-stability inequality persists.

This is **13-adic precision amplification**, not a claim of unbounded ordinary-real response: for fixed P, the real rational star tends to the finite baseline `(1+P)/P` as u approaches zero. The effect arises from numerator/denominator divisibility, an explicit example of why observer precision and real magnitude are distinct.

## Exact evidence and provenance

The independent stdlib checker `R276_crossport_ultrametric_checker.py` evaluates the full 3×3 determinant through permutation expansion and the (0,0) cofactor, verifying strict row-sum stability and exact Fraction identities. It checks every `1<=t<=8, 1<=h<=6` (48 additional-depth cases) and every unequal pair `1<=t,r<=8` with `u=13^r/[4(1+13^r)]` (56 generic cases): **104 exact cases, PASS**. The complete bounded output is stored in `R276_verification.json`. The universally quantified results follow from the symbolic proof above.

Foundation contribution is a scoped positive-rational, labeled-Port 13-adic feedback theorem; it uses the exact cycle-cover algebra and known BRC Port lease. Mathematical authorship is not external independent review; no formal Result or Foundation admission is claimed.

## Next open problem

Characterize the valuation of feedback determinants for larger directed graphs when several cycle-cover terms have the same smallest prime-adic valuation, including the effect of provenance-preserving mixed cycles and Schur elimination. Construct a minimal exact retained observer state for a *specified* finite sequence of allowed visible-Port additions, then compare it with the full `W_eff` signature required by WBRC-T32 for unrestricted contexts. A separate provenance-preserving connection from R269 auxiliary source orbits to native BRC Ports remains open.
