# D25/LIFT — reflected J second digit as two exact one-parameter terminating 4F3 derivatives

**Date:** 2026-10-23. **Scope:** portable TASK_RESEARCH mathematical derivation; AUTHOR-PROVED EXACT FINITE IDENTITY / FRACTION SELF-CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. This note is neither a Source checkpoint nor a native benchmark, Result, independent review, or proof of LIFT/JT2.

**Frozen parent:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; TP2-B6F4FC938FF94941C1B7. Original Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. The preceding mathematical frontier is the proven BC mirror transfer and the exact curvature-to-single-Beta identity at immutable commits 45f127fee1f2f506fee5b448f90acebcf0fe17d4 and 67538d64a044e9899b96b2d14d83507fc52bb0e0. The known LOW/Beta first-digit and A-block reductions, B11 boundary, and 611-prime endpoint evidence are consumed, not reasserted as new work.

Research provenance: ordinary Research lane chatgpt-research-onhour-enterprise-math-20260923, **not** maintenance lane. Global rules read at verified GLOBAL_KNOWLEDGE_V1 main@61cfa2a580230863c0d02b5f818381adbb3cb11b; P000 startup projection ACTIVE_LOCKED, canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. All identities below are ordinary rational mathematics and make no native X6/physical transfer claim.

## 1. Precise unclosed target

Set m>=1, p=6m+1 (not assumed prime for the new theorem), and let H_N=sum_{j=1}^N 1/j, H_0=0. The original reflected high-band harmonic correction, for 1<=r<=3m, is

\[
J_r=J_r^\circ+\frac{3}{2(3r-1)},\qquad
J_r^\circ=\frac12(H_{r-1}-H_m)
+\frac23(H_{2m}-H_{d_r})
+\frac13(H_{4m}-H_{3m-r}),
\]

\[
d_r=\begin{cases}m-r,&r\le m,\\r-m-1,&r>m.\end{cases}
\]

Define the signed Beta branch weight

\[
\beta_r=\frac{(-1)^m m!(r-1)!}{2^{m+r}(m+r)!},
\qquad c_r=\begin{cases}1,&r\le m,\\1/3,&m<r\le3m.\end{cases}
\]

From the **existing** polynomial Beta observer

\[
B_m(x)=(x-\tfrac12)^m,\quad
P_F(x)=\frac23\sum_{r=1}^{m}F_rx^r+\frac13\sum_{r=1}^{3m}F_rx^r,
\]

\[
J_m^{(2)}=\int_0^{1/2}B_m(x)
\left(3P'_J(x)-\frac{P_J(x)}x-\frac{P_1(x)}{2x}\right)dx,
\]

and the exact Euler–Beta moment
\(\int_0^{1/2}x^{r-1}B_m(x)dx=\beta_r\), it follows **exactly** that

\[
\boxed{J_m^{(2)}
=\sum_{r=1}^{3m}c_r\beta_r
\left[(3r-1)J_r^\circ+1\right].}
\tag{1}
\]

The +1 in (1) is essential: the pole correction contributes +3/2, while the separate P_1 term contributes -1/2. It cannot be erased before pairing.

## 2. New head/tail derivative certificate, valid for every m

Write the rising factorial as (a)_k. All parameter formulas are finite rational functions analytic near t=0. Let

\[
\beta_1=\frac{(-1)^m}{2^{m+1}(m+1)},\qquad
\beta_{m+1}=\frac{(-1)^m(m!)^2}{2^{2m+1}(2m+1)!}.
\]

Define the two normalized finite products

\[
G_H(t)=\frac{m!}{(1+t/2)_m}
\frac{(m+2t/3)_{m+1}}{(m)_{m+1}}
\frac{(3m+t/3)_{m+1}}{(3m)_{m+1}},
\]

\[
G_T(t)=\frac{(1+2t/3)_{2m}}{(1)_{2m}}
\frac{(2m+t/3)_{2m+1}}{(2m)_{2m+1}}.
\]

Both equal 1 at t=0. Now set

\[
\Phi_H(t,z)=\beta_1G_H(t)\sum_{k=0}^{m-1}
\frac{(1+t/2)_k(1-m-2t/3)_k(1-3m-t/3)_k}
{(m+2)_k(1-m)_k(1-3m)_k}z^k,
\tag{2H}
\]

\[
\Phi_T(t,z)=\frac{\beta_{m+1}}3G_T(t)
\sum_{k=0}^{2m-1}
\frac{(1)_k(m+1+t/2)_k(1-2m-t/3)_k}
{(2m+2)_k(1+2t/3)_k(1-2m)_k}z^k.
\tag{2T}
\]

**Theorem (two-block parameter certificate):** The original *fully weighted* reflected high-band second digit, including the r>m tail, has the exact representation

\[
\boxed{\begin{aligned}
J_m^{(2)}={}&
\left[\left(3z\partial_z+2\right)\partial_t\Phi_H(t,z)
+\Phi_H(t,z)\right]_{t=0,z=1/2}\\
&+
\left[\left(3z\partial_z+3m+2\right)\partial_t\Phi_T(t,z)
+\Phi_T(t,z)\right]_{t=0,z=1/2}.
\end{aligned}}
\tag{3}
\]

These are two **explicitly truncated** generalized hypergeometric parameter families. In standard notation (including the usual 1/k! factor), the first sum is truncated 4F3 with numerator parameters (1,1+t/2,1-m-2t/3,1-3m-t/3), denominator (m+2,1-m,1-3m); the second is truncated 4F3 with numerator (1,1,m+1+t/2,1-2m-t/3), denominator (2m+2,1+2t/3,1-2m). Both formal parameter excesses are **m+t/2**. This common excess is structural information for subsequent contiguous searches, not permission to replace either finite sum by a full nonterminating 4F3: the negative-integer denominator parameters make that replacement invalid without a separate limiting/continuation proof.

All denominators of (2H) for 0<=k<m, and of (2T) for 0<=k<2m, are nonzero near t=0. No singular formal term or removed tail has been concealed.

## 3. Proof without empirical extrapolation

At t=0, the k-th coefficients of (2H) and (2T), evaluated at z=1/2, are respectively \(\beta_{k+1}\) and \(\beta_{m+1+k}/3\), by direct factorial cancellation. Differentiation of the finite rising-factorial products yields

\[
\left.\partial_t\log G_H\right|_0=
-\frac12H_m+\frac23(H_{2m}-H_{m-1})
+\frac13(H_{4m}-H_{3m-1}),
\]

\[
\left.\partial_t\log\left[
\frac{(1+t/2)_k(1-m-2t/3)_k(1-3m-t/3)_k}
{(m+2)_k(1-m)_k(1-3m)_k}\right]\right|_0
=\frac12H_k+\frac23(H_{m-1}-H_{m-1-k})
+\frac13(H_{3m-1}-H_{3m-1-k}).
\]

The sum is exactly \(J_{1+k}^\circ\), with \(d_{1+k}=m-1-k\). Similarly,

\[
\left.\partial_t\log G_T\right|_0=
\frac23H_{2m}+\frac13(H_{4m}-H_{2m-1}),
\]

\[
\left.\partial_t\log\left[
\frac{(1)_k(m+1+t/2)_k(1-2m-t/3)_k}
{(2m+2)_k(1+2t/3)_k(1-2m)_k}\right]\right|_0
=\frac12(H_{m+k}-H_m)-\frac23H_k
+\frac13(H_{2m-1}-H_{2m-1-k}).
\]

Their sum is exactly \(J_{m+1+k}^\circ\), with \(d_{m+1+k}=k\). Applying \(3z\partial_z+2\) to z^k in the head gives \(3(k+1)-1\); applying \(3z\partial_z+3m+2\) in the tail gives \(3(m+1+k)-1\). Adding the **undifferentiated** \(\Phi_H,\Phi_T\) contributes exactly the +1 in (1). Summing finite coefficients proves (3) for all m>=1, independently of primality or computer tests.

This is a real match to the earlier J-HEAD-BRIDGE: the head differential recovers its shared \(L_n^\sharp\) harmonic port under the actual Beta weight; the tail differential separately preserves the piecewise \(d_r=r-m-1\) and its mandatory factor 1/3. Neither is silently identified with low-binomial \(b_n\) weights.

## 4. Actual joint-observer obstruction (no invented standalone cancellation)

The previously proved curvature-to-Beta port is

\[
T_m=\sum_{n=0}^m b_n(6n-1)
  (H_{2m+n}^{(2)}-H_{2m}^{(2)})
\equiv I_m\pmod p,
\]

\[
I_m=\sum_{j=0}^{m-1}
\frac{(-1)^j\binom{m-1}{j}}{2^j(2m+j+1)^2},
\qquad b_n=\frac{(-1)^n}{2^n}\binom mn.
\]

To check the tempting shortcut \(J_m^{(2)}\stackrel{?}{\equiv}I_m/3\pmod p\), use (3) with the original full r>m tail. Independent exact-rational generation from finite product derivatives and from the original reflected harmonics gave:

| p | m | head mod p | tail mod p | I_m mod p | J_m^(2)-I_m/3 mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 12 | 6 | 10 | **6** |
| 19 | 3 | 4 | 15 | 16 | **1** |
| 31 | 5 | 21 | 1 | 6 | **20** |
| 37 | 6 | 19 | 36 | 28 | **21** |

All inverses are of p-units. Hence the *standalone* curvature/J cancellation is **false already in both frozen prime classes**. This does **not** contradict the previously proved pairwise divided-digit mirror conservation: the full LOW observer still contains \(\mathsf M_m^\sharp-2V_m\), its divided-first-digit normalization, and related Beta terms. No experiment or proof of their joint cancellation is claimed here.

**Exact author self-check:** For every m=1,...,20, two independent finite constructions agreed as rational numbers: (i) the original piecewise \(J_r^\circ\) and factorial Beta weights in (1); (ii) derivative pairs (value, first derivative) of all finite products in (2H),(2T), with \(z=1/2\). The comparison checked head and tail **separately**, without a modular reduction. This is reproducibility evidence, not a proof of general m (given above), independent review, or native benchmark evidence.

## 5. BRC/observer scope and next non-repeated scientific unit

**BRC: COMPOSE_APPLIED / REUSE_APPLIED.** Branch identity is the original signed rational high-band r, with the head/tail selector c_r, factorial Beta weight and first-order deformation port retained separately. The observer reads \(J_m^{(2)}\), the derivative at t=0 and (only when p is prime) p-unit residues. The map to the two truncated 4F3 parameter families is lossless for this specific observable by (3); it is **not** a statement of positive mass, physical X6 transport or equivalence under arbitrary future operations.

**Minimum next action:** Apply actual finite contiguous/telescoping operations to the **joint** scalar
\[
\frac{\mathcal A_m\Theta_m-1}{p}
+\mathcal A_m\bigl(2^{-m}C_m-2V_m
+\mathsf M_m^\sharp+J_m^{(2)}\bigr)-\chi_p,
\]
using (3) for the complete J-port. The mirror-conservation correction is to be retained at the divided-digit stage. Search first for a common terminating contiguous recurrence at z=1/2 for (2H)+(2T) and the low second-jet family; prove any cancellation or retain an explicit nonzero defect. The original endpoint/native benchmark and independent review remain open. Do not substitute an unverified infinite hypergeometric identity for this finite target.

**Control provenance and recovery debt:** The own Research-lane recovery Issue #6186 has a previously verified local ACTIVE projection with source_authority_verified=false, no own claim/run and a neutral preserved-staging manifest; exact D25 continuation #6187 returned PREREQUISITE_NOT_SUCCEEDED; original dispatch #6188 ultimately FAILED / TimeoutExpired (not NO_DISPATCH). These original requests were read without resubmission. Current direct Sites service 0.6.11 reports research_authority_granted=false and exposes no direct dedicated recovery_status action. Support issue awdawmip/enterprise-math#1539 owns that unresolved Source-session prerequisite. No session, CLAIM, run, Source checkpoint, Result, freeze, publication admission or native benchmark is represented by this independent GitHub proof note. Remain REGISTER_PENDING / SYNC_DEBT until the genuinely authorized lane can register and checkpoint; maintain original frozen source pin and schedule/notification settings without modification.
