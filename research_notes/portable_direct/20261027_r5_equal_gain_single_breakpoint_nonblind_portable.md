# R5: exact single-breakpoint criterion for one-parameter LR/full support equality

**Date:** 2026-10-27 (Asia/Taipei). **Status:** PORTABLE / NONBLIND / UNREVIEWED / NOT_ADMITTED. This is an additional algebraic consequence and strict rational witness derived from the author's Bellman formula; **not** an independent native Driver review, a frozen Result, a formal V2 Task, or a claim of convex-hull equality. Shared prior R5/D25/F7 discussion is disclosed. Preserve the original R5 author and contribution provenance.

## Frozen inputs and exact scope

- Predecessor: `awdawmip/enterprise-math@280f748a12052a8a2cd55a1d79a38ef32a7234b1:research_notes/brc_r5_16leaf_jensen_hull_gate_20261027/PROOF.md`, Theorem 1, equations (1)-(2).
- Current project read on entering this derivation: `main@540f16070a643cffc3d995fda6406f84c6a1a5af`. Global knowledge read `main@f1fc9291d6ec574001ccc54e9d3cb8c410f2f3ab`. P000 immutable original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; active research object remains a three-dimensional slice of native X6, not an external plane.
- The following theorem concerns an **external** finite positive two-measure stopping tree, with four equal-mass t=2 histories, two hidden t=1 groups, ratio R=1 on each observed prefix, and terminal Bayes gains `g_{A0},g_{A1},g_{B0},g_{B1} >= 0`. It uses support directions `J_s=P(D=Q)+Q(D=P)+s E_Q(tau)` for real `s>=0`. The external tree may be statically tagged with native X6 cell paths; no native dynamics, BRC–Shor arithmetic substitution or physical inference follows.

## Theorem: testing only the seedless-LR indifference price suffices for this entire support ray

Let `m_A=(g_A0+g_A1)/2`, `m_B=(g_B0+g_B1)/2`, `m=(m_A+m_B)/2`, and `s_0=m/2`. For each `g=A,B` set
```
F_g(s) = ((g_g0-s)_+ + (g_g1-s)_+)/2 - s,
Delta(s)=V_LR(s)-V_full(s)
        = ([F_A(s)]_+ + [F_B(s)]_+)/2 - (m-2s)_+,
x_+ = max(x,0).
```
(The formula is exactly the predecessor's full Bellman identity, without its optional within-group condition.)

For these nonnegative gains, the following three assertions are equivalent:

1. `Delta(s)=0` for **every** `s>=0` in this one-parameter support family.
2. `Delta(s_0)=0` at **one explicitly computable price**, `s_0=m/2`.
3. `m_A=m_B` **and** for each group `max(g_g0,g_g1) <= 3 min(g_g0,g_g1)`.

**Proof.** Since `(x-s)_+ >= x-s`, each `F_g(s) >= m_g-2s`. Convexity gives
```
Delta(s) >= ( (m_A-2s)_+ + (m_B-2s)_+ )/2 -(m-2s)_+ >= 0.
```
(1) implies (2). Conversely suppose (2). At `s_0=m/2`, the LR positive-part term is zero. If `m_A != m_B`, the larger group mean exceeds `m`, hence that group's `F_g(s_0) >= m_g-m >0`, contradiction. Thus `m_A=m_B=m`. Write `u_g=max(g_g0,g_g1)`, `v_g=min(g_g0,g_g1)`. At `s_0=(u_g+v_g)/4` one checks exactly that
```
[F_g(s_0)]_+ = (u_g-3v_g)_+/8,
Delta(s_0) = ((u_A-3v_A)_+ +(u_B-3v_B)_+)/16.
```
Hence (2) forces `u_g<=3v_g` for both groups; this is (3). Under (3), `m_g/2<=v_g`. The predecessor's proved Bellman threshold reduction is therefore applicable for all `s>=0`, yielding
```
Delta(s) = ((m_A-2s)_+ +(m_B-2s)_+)/2 -(m-2s)_+ = 0,
```
since `m_A=m_B=m`. Thus (3) implies (1). QED.

**Consequence for the mother question.** This is an exact, cheap necessary rejection certificate for four-dimensional equal-hull candidates: **any failure of (3) produces a rational support separation at the single price `s_0`** whenever the terminal gains are rational. Passing the certificate proves equality only for the `(1,1,0,s)` support ray, **not** full four-dimensional convex-hull equality or a seedless-LR image mismatch. This distinction is load-bearing.

## A strictly positive 16-leaf witness missing from the predecessor's unequal-group example

Reuse the predecessor's terminal likelihood-ratio vector `Y=(1/10,99/100,101/100,19/10)` and kernel `K(p)=(p,1/2-p,1/2-p,p)`. At equal prefix masses `Q(g,j)=P(g,j)=1/4`, choose
```
p_A0=79/178, p_A1=11/178, p_B0=p_B1=45/178.
```
All 16 terminal `Q(g,j,k)=K(p_gj)_k/4` and `P(g,j,k)=Y_k Q(g,j,k)` are strictly positive; both measures normalize to one, and all t=1/t=2 prefix likelihood ratios are exactly one. The resulting conditional gains are
```
g_A0=2/5, g_A1=3/50; g_B0=g_B1=23/100;
m_A=m_B=m=23/100,   s_0=23/200.
```
Thus the group means are **equal** (the old Jensen group-means test vanishes), but group A has `u_A>3v_A`, so this new refinement detects a strictly positive support gap:
```
Delta(23/200)=11/800,
V_LR(23/200)=223/200,
V_full(23/200)=881/800.
```
The exact `(1,1,0,23/200)` support direction separates full-history observation from `conv(O_LR)`, without assuming a finite grid approximates arbitrary randomized policies. This example is **excluded**, not an equal-hull candidate.

## Finite arithmetic cross-check and recovery

A separate standard-library `fractions.Fraction` checker enumerated 7^4 = **2401** nonnegative gain quadruples with coordinates `k/20, k=0..6`, and for each also checked 17 price samples `s=i/40, i=0..16`. It found no discrepancy in (2) iff (3), no negative `Delta`, and no nonzero sample gap when (3) holds. The explicit strictly positive kernel above was checked for rational normalization and `Delta=11/800`. These finite checks are sanity checks; the displayed algebra, not finite sampling, proves the continuum-of-s claims.

Exact local checker: `EM_DRIVER_R5_GAIN_BREAKPOINT_AUDIT_20261027.py`; exact stdout: `EM_DRIVER_R5_GAIN_BREAKPOINT_AUDIT_20261027.txt`. A succeeding authorized publisher may mirror these files, preserving their bytes. No native Driver DA or clean independence is claimed.

**Next discriminating research unit:** enforce both equal group means and the 3:1 child-gain threshold when selecting new positive rational candidates; then test the remaining four-observer support directions with exact rational full-vector convex-hull membership. Do **not** promote one-ray equality to full-hull equality. Native Result/review/follow-up must use the current authority and exact review set, not this author-level note.
