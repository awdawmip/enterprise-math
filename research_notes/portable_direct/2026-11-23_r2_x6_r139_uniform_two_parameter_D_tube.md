# X6 R139 — an unbounded two-parameter rigidity tube for Port-10 six-pair BRC strict-near directions

Date: 2026-11-23 (Asia/Shanghai). Status: **author exact rational certificate and analytic perturbation proof PASS; independent mathematical review pending**.

## Frozen scientific scope

Retain the conditional four-positive-weight, all-six-pair BRC integer observer, the declared three-dimensional research slice of native X6, the integer Port=10 and the strict 3/2 near criterion. No change to P000 or native physical dynamics. The frozen R121 and R122 scientific inputs remain:
- `awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`.
- `awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`.

Immediate exact predecessor R138: `awdawmip/enterprise-math@e8e20fdfce40d5415e2f02b51983c7c5928d30ce:research_notes/portable_direct/2026-11-23_r2_x6_r138_D500_all_positive_B_rigidity.md`. Its published verifier is `research_notes/portable_direct/x6_r138_all_B_fixed_D500_verify.py` at `a4d43c75950cf78a153f6ce071bbfeb9937dfe39`.

Use R138's exact definitions: a=(x,y,z) modulo ± only, q(a)<=10; h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z); F_w(a)=max over all six gaps |h_i-h_j|/(w_i+w_j); eta_10=min F_w over 1,935 unoriented Port-10 directions; strict-near means 2F_w(a)<3eta_10(w).

## New theorem — an entire unbounded-B open tube

For **every pair of real parameters**

```
B > 0,
20000/41 < D < 21000/41
```

and weight vector `w=(136,B,176,D)`, the full strict 3/2 near set is **exactly**

```
N_10(w) = {(1,0,0), (5,-4,1), (5,-1,0), (9,-5,1)} modulo ±,
|N_10(w)| = 4.
```

Equivalently, the two-parameter region `B>0, |D-500|<500/41` is entirely four-direction rigid. The B axis is unbounded and D varies continuously. The radius `500/41` is a certified sufficient uniform perturbation radius, **not** a claimed sharp radius.

## Proof

**(1) Strengthen R138's exact one-parameter inequalities uniformly in B.** At the base weight `w_0=(136,B,176,500)`, write `F_0`, `eta_0`, and let `C` denote the four R138 near directions. On each of R138's seven rational B regions, the exact optimizer is `K/L(B)`, where `L(B)=L_0+L_1 B`. Their common denominator vector is `s_0(B)=(136+B,312,636,B+176,B+500,676)`.

For every `a in C` and every pair j, the affine inequality

```
7*g_j(a)*L(B) <= 10*K*s_0j(B)
```

holds. Exactly **7 regions x 4 insiders x 6 pairs = 168** pair inequalities have been checked at all rational region endpoints; the final unbounded region additionally checks the nonnegative recession slope. Consequently

```
F_0(a) <= (10/7)*eta_0  for every a in C.
```

For each one of the other 1,931 directions and each region, there exists a region-uniform pair j satisfying

```
5*g_j(a)*L(B) >= 8*K*s_0j(B).
```

Exactly **7 x 1,931 = 13,517** rational affine exclusion certificates pass, including the unbounded ray. Thus

```
F_0(a) >= (8/5)*eta_0  for every a outside C.
```

Both inequalities hold for all real `B>0`, not merely at the rational test points.

**(2) Perturb only D with a uniform multiplicative envelope.** Put `r=|D-500|<500/41<500`. In the six pair denominators, only the three involving D change. Each such base denominator is `s_0>=500`, since B>0 and all other fixed weights are positive. Therefore every score, including unchanged pairs, satisfies

```
c_- * F_0(a) <= F_D(a) <= c_+ * F_0(a),
c_- = 500/(500+r),   c_+ = 500/(500-r).
```

Taking minima over the same finite direction population gives the identical bounds for `eta_D` in terms of `eta_0`. Hence

```
F_D(a)/eta_D <= kappa * F_0(a)/eta_0    (a in C),
F_D(a)/eta_D >= (1/kappa)*F_0(a)/eta_0 (a outside C),
kappa = (500+r)/(500-r).
```

Because `r<500/41`, we have `kappa<21/20`. For each insider,

```
F_D(a)/eta_D <= kappa*(10/7) < (21/20)*(10/7) = 3/2.
```

For every outsider,

```
F_D(a)/eta_D >= (8/5)/kappa > (8/5)*(20/21) = 32/21 > 3/2.
```

The strict membership and complete exclusion therefore persist for every B>0 and every D in the stated open interval, completing the proof.

## Exact reproducibility and evidence strength

The standalone local entry `x6_r139_uniform_D_tube_verify.py` imports the previously published R138 exact-integer certificate and checks the **168** stronger insider and **13,517** stronger outsider inequalities using Python `fractions.Fraction`; it also checks the exact arithmetic defining the uniform radius. Its executed output:

```
R139 UNIFORM TUBE CERTIFICATE PASS
insider_upper_margin_checks 168 outsider_lower_margin_checks 13517
insider_F_over_eta_upper 10/7 outsider_F_over_eta_lower 8/5
uniform_open_D_interval 20000/41 21000/41
```

The proof is a finite exact inequality certificate plus an analytic multiplicative perturbation bound. Independent mathematical review and any theorem admission remain pending. This theorem concerns the declared observer model, not native six-axis dynamics.

## Next scientific question

Determine the **sharp** uniform D-radius over the entire B>0 ray. Identify the first actual facet where one of the four directions reaches `F_D=3eta_D/2` or an outsider reaches `F_D<3eta_D/2`, and classify whether the infimum over B occurs at finite B or at B->0/infinity. This can be attacked with the R138 seven-chamber affine certificate and a two-real-parameter exact-cell decomposition.
