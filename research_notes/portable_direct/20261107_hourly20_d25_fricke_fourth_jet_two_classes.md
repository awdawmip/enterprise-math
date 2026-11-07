# D25: Fourth Fricke jets and the 19-class Gauss-source bridge (2026-11-07)

**Status:** AUTHOR-SIDE PROVED ALGEBRA (declared CM-root hypotheses); EXACT FINITE CHECKS 107/107; UNREVIEWED; NOT_ADMITTED. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Research lane `chatgpt-research-hourly-enterprise-math-20260923`; do not use maintenance lane `chatgpt-hourly-enterprise-math-20260921`.

**Previously available inputs (not re-proved):** `20261107_hourly20_d25_signed_fricke_third_jet.md` at `8057b55cad5a4bce533a7ff1a289bac387786643`; `20261107_hourly20_d25_weighted_low_degree_jet_bridge.md` at `fbe820347866f8b8f8ae6d48da534f0889203672`; independent Fricke rational maps from `20261107_hourly20_d25_fricke_weighted_local_twojet.md` at `625a4d42db5e4b379f9e3f021b3ca5e983d948e0`. Existing 216 CM0 and 13-class CM/Hasse root results keep their original admission strength.

## Theorem 1: 19-class exact folding

For every prime `p=8k+3>3`, define `H_k(w)=Σ_{j=0}^k binom(3k+1,j)binom(k,j)w^j` in `F_p[w]`. Let `G_p(w)=Σ_{j=0}^{p-1}(1/8)_j(3/8)_j/(j!)² w^j`, and `B_<p(w)=Σ_{j=0}^{p-1}(1/4)_j(1/2)_j(3/4)_j/(j!)³ w^j`, both modulo p.

**Exact unconditional polynomial identity:** `G_p=H_k` and `B_<p=H_k²`.

Proof: modulo p, `1/8=-(3k+1)` and `3/8=-k`. The Gauss series terminates at j=k, with coefficients `binom(3k+1,j)binom(k,j)`. Clausen's coefficient identity yields `B_<p=projection_<p(G_p²)`. Since `deg H_k²=2k=(p-3)/4<p`, the projection is identity. QED.

For `p=8k+5`, previously established Frobenius folding is `G_p²=(1-w^p)(1-w)H_k²`, `B_<p=(1-w)H_k²`. Thus in both classes, `G_p²=f_p(w)B_<p`, where `f_p=1-w^p` for the 5-class and `f_p=1` for the 3-class. All positive derivatives of `f_p` of order <p vanish in characteristic p. At `w0=1/9`, `f_p(w0)=8/9` or `1`, respectively.

Crucial BRC limit: this is characteristic-p derivative invisibility, **not** a p-adic source-port equivalence. In characteristic zero `d(w^p)/dw=pw^{p-1}`, and coefficient-lift defects must be retained for a p²/p³ weighted transfer.

## Theorem 2: all-order Gauss-jet recurrence and fourth weighted derivatives

The 216 truncated Gauss polynomial `F_m(z)=Σ_{j≤m}binom(m,j)binom(2m,j)z^j` (`p=6m+1`) and the 2304 Gauss polynomial `G_p(w)` satisfy the same second-order operator with distinct eigenvalues:
`x(1-x)Y''+(1-3x/2)Y'-λY=0`,
with `(x0,λ)=(1/2,1/18)` for F, or `(1/9,3/64)` for G.

Assume `Y(x0)=0`. Then `Y'(x0)≠0`: the ODE at an ordinary point and successive differentiation would otherwise kill every derivative of a polynomial of degree <p. Put `v_n=Y^(n)(x0)/Y'(x0)`, `v0=0,v1=1`. Differentiating n times gives
```
x0(1-x0) v[n+2] =
  [n(n+1/2)+λ] v[n]
  - [1-3*x0/2+n(1-2*x0)] v[n+1].
```
This holds for the polynomial jets of orders below p, since the denominator is a unit.

Let `P_A=(1+6θ)A_<p`, `P_B=(1+8θ)B_<p` with `θ=x d/dx`. In the indicated characteristic-p folding, normalized derivatives of `P_A`, `P_B` at the CM roots are the same as for `R_c=(1+cθ)Y²=Y²+2cxYY'`, with c=6 or 8. The recurrence gives
`(v2,v3,v4)_A=(-1,65/9,-247/9)` and `(v2,v3,v4)_B=(-135/16,78489/512,-2119203/512)`.
Taylor expansion of `Y²+2cxYY'` through order four yields **new fourth weighted ratios** and records their prerequisites:
```
P_A''/P_A'  =  4/3
P_A'''/P_A' =  116/9
P_A''''/P_A'=  1520/27
P_B''/P_B'  = -99/16
P_B'''/P_B'=  29403/256
P_B''''/P_B'= -12026313/4096
```
The first two derivative ratios in each group are earlier 13-class results; the fourth and the 19-class extension are the present contribution. In terms of class-specific H-source derivatives,
`P_B'(1/9)=128 H_k'(1/9)²/81` for p≡13 mod24, whereas `P_B'(1/9)=16 H_k'(1/9)²/9` for p≡19 mod24.

**Hypothesis ledger:** Existing CM0 supplies `F_m(1/2)=0` for the frozen target classes, and prior CM/Hasse work supplies `H_k(1/9)=0` for p≡13 mod24. For p≡19 mod24, the universal H-root is **still unproved here**: only the folding and recurrence are unconditional; the 19-class evaluated ratios require the root hypothesis. Finite exact observations do not change this.

## Theorem 3: signed fourth Fricke jet, conditional on the CM roots

Take the established maps
```
z(t)=108t²(t+9)(t+8)²/(t+12)^6
w(t)=256t³(t+8)(t+9)³/(t²+36t+216)^4 .
```
For T_ε=ε6√2 in F_(p²), ε=±1, both maps give `z(T)=1/2`, `w(T)=1/9` and have nonzero first derivatives. Since both weighted functions vanish simply under the declared root conditions, a unique *formal local* scalar gauge `γ_ε(t)=P_A(z(t))/P_B(w(t))` exists.

For a composite function `X=P(x(t))` denote `R=X''/X'`, `S=X'''/X'`, `U=X''''/X'`. The chain rule gives
```
R = r2*x' + x''/x'
S = r3*(x')² + 3*r2*x'' + x'''/x'
U = r4*(x')³ + 6*r3*x'*x'' + 3*r2*(x'')²/x'
    + 4*r2*x''' + x''''/x'
```
where `rj=P^(j)/P'` in the corresponding Gauss variable. Product differentiation at a *simple common zero* yields
```
ell = γ'/γ   = (R_A-R_B)/2
q   = γ''/γ  = (S_A-S_B-3*ell*R_B)/3
r   = γ'''/γ = (U_A-U_B-4*ell*S_B-6*q*R_B)/4 .
```
Substitution of exact rational Fricke derivatives at the two signed branches, using the fourth ratios above, yields
```
γ_ε'''/γ_ε(T_ε) = -6697/72 + ε*3157√2/48
(log γ_ε)'''(T_ε) = -7829/144 + ε*66431√2/1728 .
```
The two trace/norm pairs over the quadratic branch extension are `(-6697/36, -223/10368)` and `(-7829/72, 35591/1492992)`. Each expression has p-unit denominators in both target prime classes. The class-dependent **gauge amplitudes** must not be collapsed:
```
γ_ε(T_ε) = ε*(6561√2/1024)*(F_m'(1/2)/H_k'(1/9))² , p≡13(mod24)
γ_ε(T_ε) = ε*(729√2/128)*(F_m'(1/2)/H_k'(1/9))²  , p≡19(mod24).
```
Their scalar prefactors differ by 9/8, precisely the inverse 13-class Frobenius carry factor. The logarithmic jets agree across classes only after retaining the distinct fold/amplitude and Cauchy-source labels. **A locally adjustable gauge to any finite jet order is not a global weighted p³ identity** and does not prove mother-target completion.

## Independent arithmetic and next precise action

Executed `d25_fricke_fourth_jet_two_classes_20261107.py`: all **107 primes p<3000** in classes 13 and 19 mod24 (53/54) passed original, unfactored weighted 3F2 derivatives through order four. All samples also have H_k(1/9)=0 and H_k'(1/9)≠0. Separately the two signed rational Fricke branches were differentiated symbolically through fourth order, confirming both displayed gauge coordinates. Exact witnesses (A and B derivative vectors of orders 1..4 mod p):
`p=13: A=(6,8,8,7), B=(11,1,5,0)`;
`p=19: A=(5,13,18,0), B=(7,3,12,14)`;
`p=373: A=(211,157,150,205), B=(320,258,293,177)`.

Mother objective `Δ_p-R_p≡0 (mod p), p≡13,19 (mod24)` remains **OPEN**. The immediate new proof obligation is a **universal 19-class H_k(1/9)=0** argument (prefer an explicit CM/Hasse or character-sum bridge); next investigate p-adic lifting of the characteristic-p Frobenius derivative, coefficient lifts and labeled Cauchy carry ports against the signed Fricke 4-jet. The original native p373 experiment is NOT replaced by this finite-field script. Method classification: `COMPOSE_APPLIED` (existing Clausen, Gauss ODE, prior CM0, 13-class folding, externally established Fricke maps); no new shared top-level BRC tool family claimed.

**Native state:** Site `CONFIGURED_NOT_LIVE_VERIFIED`; current `em_status` failed `BACKEND_IDENTITY_OR_VERSION_MISMATCH` and `operation_sent=false`. Old requests `em-h20-20261106-1324-d25-task-r13`, `em-h20-20261106-1324-d25-cont-r13` and unknown session/claim/run/staging preserved. `REGISTER_PENDING`; native checkpoint, Result, freeze, review and admission NOT WRITTEN. Support `awdawmip/enterprise-math#1558`.
