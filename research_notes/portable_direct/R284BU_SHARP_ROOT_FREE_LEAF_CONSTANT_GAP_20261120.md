# R284BU — Exact constant-gap extremal theorem for a frozen two-leaf star-Port observer

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK_PASSED / NOT_REVIEWED. Independent portable mathematical work; this note is not a native CLAIM, Result, Review or Activity-authority assertion.

## Scientific source and precise model

Continue R284BT_DOUBLE_FROZEN_PORT_ALIASES_AND_SHARP_FINITE_NOISE_20261120.md, immutable proof commit 5bdcd48073feebc726bff19bb98bbde517ab1237, in awdawmip/enterprise-math. Keep its earlier R284BS source freeze, the project's P000/ACTIVE worldview and the distinction between a scalar observer and full signed/provenance-bearing state. The present determinant observation is an auxiliary algebraic Port model, not an executed native BRC or X6 experiment.

Let H be any integer at least 2 and let C range over integer matrices with entries in {1,...,H} of size 4 by 4. Freeze the two leaf controls d_1=t and d_2=s. The free controls are d_0,d_3,z_1,z_2,z_3. Define

\[
F_C(d_0,d_3,z)=\det\bigl(\operatorname{diag}(d_0,t,s,d_3)-C-\sum_{i=1}^3 z_i E_{0i}\bigr).
\]

We study the response difference for C,D identical except that D_{03}=C_{03}+1 (and C_{03} is chosen so D remains in the alphabet).

## Theorem: exact extremal constant gap for every alphabet

For every H>=2 and every pair of integers t,s>=H²+1, define

\[
m_H(t,s)=ts-(H-1)(t+s),\qquad
M_H(t,s)=H(t+H-1)(s+H-1).
\]

Then for all such single-entry pairs C,D, their response difference is a control-independent integer:

\[
F_D-F_C=-G(C),\qquad 0<m_H(t,s)\le G(C)\le M_H(t,s).
\]

Both endpoints are attained by explicit admissible matrix pairs. Consequently the **exact minimum absolute constant gap within this single-edge perturbation family** is

\[
\boxed{m_H(t,s)=ts-(H-1)(t+s).}
\]

For the one-reading finite-field circular-residue observation with real adversarial circular error radius rho (indeed for any number of adaptive readings using the same frozen t,s), uniform exact recovery of all H^16 candidates requires

\[
\boxed{2\rho<ts-(H-1)(t+s).} \tag{1}
\]

This is a necessary condition, not an asserted sufficient condition: other candidate pairs can produce exact response aliases or smaller control-independent gaps. In particular t=s is covered by R284BT's exact alias strip.

## Proof by a three-by-three cofactor, including endpoint witnesses

Write the leaf block B=diag(t,s,d_3)-C_{1:3,1:3}, root-to-leaf column b=(C_{01},C_{02},C_{03})^T and leaf-to-root column v=(C_{10},C_{20},C_{30})^T. Block determinant expansion is

\[
F_C=(d_0-C_{00})\det B-(b+z)^T\operatorname{adj}(B)v.
\]

Since the only change is b_3 by +1, F_D-F_C=-[\operatorname{adj}(B)v]_3. This component equals the determinant of B with its third column replaced by v. Set

\[
a=C_{11},\ e=C_{22},\ b=C_{12},\ d=C_{21},\
g=C_{31},\ h=C_{32},\
u_1=C_{10},\ u_2=C_{20},\ u_3=C_{30}.
\]

The exact response difference magnitude is thus

\[
\begin{aligned}
G={}&u_3\big((t-a)(s-e)-bd\big)\\
   &+u_2\big((t-a)h+bg\big)
   +u_1\big(dh+(s-e)g\big). \tag{2}
\end{aligned}
\]

All nine variables are independently drawn from {1,...,H}. Formula (2) is independent of every free control and of the other seven entries not displayed.

For t,s>=H²+1 we have t-a,s-e>=H²-H+1>=H+1, hence

\[
(t-a)(s-e)-bd\ge(H+1)^2-H^2=2H+1>0.
\]

The coefficients of u_1,u_2,u_3 in (2) are positive. The coefficients of g,h are positive as well. Thus to minimize G set u_1=u_2=u_3=g=h=1, and to maximize set them all to H. The slopes in a and e are respectively -u_3(s-e)-u_2h and -u_3(t-a)-u_1g, both strictly negative. Therefore a=e=H at the minimum and a=e=1 at the maximum.

For the minimum, the remaining b,d dependence becomes

\[
G=(t-H)(s-H)+(t-H)+(s-H)+b+d-bd.
\]

Since b+d-bd=1-(b-1)(d-1), choose b=d=H, obtaining G_min=ts-(H-1)(t+s).

For the maximum, the b,d dependence is H²(b+d)-Hbd; each separate slope is H(H-d) or H(H-b), nonnegative on the alphabet. Choose b=d=H, obtaining G_max=H(t+H-1)(s+H-1).

All choices can be embedded into actual 4x4 matrices by filling unspecified entries with 1, setting C_{03}=1, and increasing it to D_{03}=2. For the minimizing witness use a=e=b=d=H and g=h=u_1=u_2=u_3=1. For the maximizing witness use a=e=1 and b=d=g=h=u_1=u_2=u_3=H.

For either witness the circular distance between F_C and F_D modulo any prime is at most its ordinary absolute difference G. At the minimum witness, closed circular error balls overlap once 2rho>=G_min, and an adversary can report a common midpoint at every adaptive measurement. This proves (1). QED.

## R284BT bridge and exact checks

For H=2,t=5,s=50: m=195 and M=612. This reproduces the two extrema in R284BT's numerical census with a **general algebraic extremal certificate**. That source's global sharp radius rho<97.5 continues to rely on its separate 65,536-matrix full-signature census. Other new instances are (H,t,s)=(3,10,13), m=84, M=540, and (4,17,35), m=439, M=3040.

The companion standard-library checker enumerates every one of the H^9 nine-variable configurations for six explicit cases:

| H | t | s | min G | max G | configurations |
|---|---:|---:|---:|---:|---:|
| 2 | 5 | 50 | 195 | 612 | 512 |
| 2 | 5 | 5 | 15 | 72 | 512 |
| 2 | 7 | 10 | 53 | 176 | 512 |
| 3 | 10 | 13 | 84 | 540 | 19683 |
| 3 | 19 | 37 | 591 | 2457 | 19683 |
| 4 | 17 | 35 | 439 | 3040 | 262144 |

Total: 303,046 exhaustive exact-integer configurations. An independent 4x4 Leibniz determinant also checks the actual response difference at three free-control settings for three witness configurations in each case: 54 crosschecks. Evidence and code: R284BU_root_free_leaf_gap_checker.py and R284BU_root_free_leaf_gap_verification.json in the same directory. Finite checking corroborates the theorem; universal validity follows from (2) and the extremal proof, not extrapolation from the six examples. Independent mathematical review: NOT_REVIEWED.

## Scope and next research unit

An identical scalar response under frozen controls is an observer fibre, not a proof of equivalence of distinct directed-edge states under future control release, different Port geometries or native Heartbeat World operations. Preserve the full matrices, branch/directional provenance and declared future observations. The immediate next mathematical problem is to classify **all** constant response differences, including pairs changing several entries, and identify when the lower ceiling (1) is globally attainable rather than merely necessary. The further route is a finite-field control construction with a tractable decoder and explicit resource accounting. No Task/CLAIM, Result or independent Review is created by this research note.
