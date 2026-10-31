# D25: Two-sided clipped Clausen boundary, p≡13/19 asymmetry, narrow Gosper no-go

**Date:** 2026-10-31. **State:** AUTHOR-SIDE / ALGEBRAIC ARGUMENTS PROVED AS STATED / FINITE EXACT CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / NATIVE SOURCE CHECKPOINT PENDING. This author artifact creates no CLAIM, Research-Activity registration, Result or independent review.

**Mother:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged. The D24 UR is frozen. The native p=373 same-original-class benchmark in issue #1559 remains NOT_EXECUTED / PENDING_OWNER. Prior original-series six valuation ports, reflected I5 and explicit I3/I4 from commits abca20f33ef41943d70135000f27a7af3ed802e0 and 02c9eb67f475382903ac9911e661012be7191662 are consumed, not re-proved.

Let p>3 be prime, and let

\[
a_k=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k},\quad
b_k=\frac{\binom{4k}{2k}\binom{2k}{k}^2}{2304^k},\quad
A_p=\sum_{k=0}^{p-1}(6k+1)a_k,\quad
B_p=\sum_{k=0}^{p-1}(8k+1)b_k.
\]

Define two distinct Gauss sequences

\[
\alpha_i=\frac{(1/6)_i(1/3)_i}{2^i(i!)^2},\qquad
\beta_i=\frac{(1/8)_i(3/8)_i}{9^i(i!)^2}.
\]

All relevant denominators are p-units for indices <p.

## Theorem 1: exact two-sided signed clipped-square decomposition

Define
\[
g_\alpha=\sum_{i<p}\alpha_i,\quad h_\alpha=\sum_{i<p}(12i+1)\alpha_i,\quad
g_\beta=\sum_{i<p}\beta_i,\quad h_\beta=\sum_{i<p}(16i+1)\beta_i,
\]
\[
T_\alpha=\sum_{\substack{0\le i,j<p\\i+j\ge p}}(6(i+j)+1)\alpha_i\alpha_j,\qquad
T_\beta=\sum_{\substack{0\le i,j<p\\i+j\ge p}}(8(i+j)+1)\beta_i\beta_j.
\]

Then **exactly in rational arithmetic**, not merely modulo a prime power,
\[
\boxed{A_p=g_\alpha h_\alpha-T_\alpha,\quad B_p=g_\beta h_\beta-T_\beta.}
\]
Therefore
\[
A_p-2B_p+p\chi_{-3}(p)
=g_\alpha h_\alpha-2g_\beta h_\beta-T_\alpha+2T_\beta+p\chi_{-3}(p).
\]
This is an **equivalent decomposition of an UNPROVED p⁴ conjecture**, not its cancellation proof.

**Proof.** Classical Clausen: for a+b=1/2,
\[
[{}_2F_1(a,b;1;z)]^2={}_3F_2(2a,2b,1/2;1,1;z).
\]
Substitute (a,b,z)=(1/6,1/3,1/2) and (1/8,3/8,1/9). Coefficient comparison gives a_n=Σ_{i+j=n}α_iα_j and b_n=Σ_{i+j=n}β_iβ_j for every n≥0. Product of the truncated Gauss sums includes all i,j<p, while original A_p,B_p keep only i+j<p. Symmetrizing (12j+1) yields 6(i+j)+1 and symmetrizing (16j+1) yields 8(i+j)+1. Subtract the exact clipped triangle. **Important:** Tα and Tβ are *clipped two-index Gauss-square tails*, not the full original a_n,b_n tails at n≥p or the six original-series I0–I5 ports.

With c=6 for α or c=8 for β, let S_x(t)=Σ_{t≤j<p}x_j, U_x(t)=Σ_{t≤j<p}j x_j. Then exact O(p) terminal computation:
\[
T_x=\sum_{i=1}^{p-1}x_i\big[(ci+1)S_x(p-i)+cU_x(p-i)\big].
\]
Retain the two-index observer/source data for any future operation that is not certified to descend to this terminal scalar.

## Theorem 2: sharp residue-class-dependent cutoff valuation

For p=6ℓ+1, the recurrence α_{i+1}/α_i=(6i+1)(3i+1)/(36(i+1)^2) yields v_p(α_i)=0 on [0,ℓ], 1 on (ℓ,2ℓ], 2 on (2ℓ,p). If i+j≥p, not both i,j≤2ℓ; at least one α factor has valuation 2. Consequently **Tα≡0 mod p² universally for p≡1 mod6** (indeed each tail term individually).

For p≡19 mod24 write p=8t+3. The recurrence β_{i+1}/β_i=(8i+1)(8i+3)/(576(i+1)^2) has valuation steps at i=t (8i+3=p) and i=3t+1 (8i+1=3p). Thus v_p(β_i)=0 on [0,t], 1 on (t,3t+1], 2 on (3t+1,p). Because 2(3t+1)<p, i+j≥p implies at least one valuation-2 factor. Therefore **Tβ≡0 mod p² termwise throughout p≡19 mod24**.

For p≡13 mod24 write p=8t+5. The valuation steps occur at j₁=(5p−1)/8=5t+3, j₂=(7p−3)/8=7t+4. Then v_p(β_i)=0 for i≤j₁, 1 for j₁<i≤j₂, 2 after j₂. The pair (i,j)=(j₁,j₁) belongs to i+j≥p, has two p-unit β factors, and has p-unit signed weight 8(i+j)+1=10p−1. Consequently **the beta clipped-square tail has valuation-zero individual sources on the 13-class**. At p=13, exact aggregate Tβ≡7761 mod 13⁴, hence Tβ≡156=−13 mod169, so v₁₃(Tβ)=1: **even the aggregated Tβ is not universally p²-divisible on the 13-class**. This is a concrete obstruction to a class-blind p²-tail deletion.

## Theorem 3: narrowly scoped rational single-index Gosper no-go

For original unweighted sequences,
\[
r_a(k)=a_{k+1}/a_k=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3},\quad
r_b(k)=b_{k+1}/b_k=\frac{(4k+1)(2k+1)(4k+3)}{288(k+1)^3}.
\]
There exists **no rational** R(k)∈Q(k) with r_a(k)R(k+1)−R(k)=6k+1, nor with r_b(k)R(k+1)−R(k)=8k+1.

**Proof.** Each ratio has one triple pole at −1, its zeros lie strictly between −1 and 0, and its limit at infinity is respectively 1/2 or 1/9, not 1. If R had poles, pick one z of maximal real part. R(k+1) is regular at z, forcing z to be the unique ratio pole −1. Pick one w of minimal real part, Re(w)≤−1. At k=w−1 the shifted R is singular and unshifted R regular; the ratio would need a zero at w−1. Its zeros lie in (−1,0), demanding Re(w)>0, contradiction. Thus R is polynomial. Since r(∞)≠1 and the target is degree 1, deg R=1; cancellation of the ratio's triple pole at −1 forces R(k+1) divisible by (k+1)^3 and hence deg R≥3, impossible.

Nor can a mixed p-independent **separated rational** antiderivative F(k)=R(k)a_k+S(k)b_k exist for the weighted difference. Indeed a_k/b_k is not rational(k): its consecutive ratio tends to (1/2)/(1/9)=9/2, whereas the consecutive ratio of any nonzero rational(k) tends to 1. Such a mixed identity would therefore split into the two impossible scalar equations. **Scope:** this excludes only that rational one-index p-independent ansatz; p-dependent finite transforms, multivariate WZ, CM and q-microscope routes are NOT excluded.

## Actual finite computation and sharp witnesses

The attached separate program d25_twosided_clausen_20261031.py uses Python standard-library exact integers and p-unit modular inverses. On **all 52 primes p≤1200 with p≡13,19 mod24**, checked both original coefficient recurrences, both Gauss recurrences, O(p) suffix-form exact two-sided identities mod p⁴, beta/alpha valuation bounds, and the *still-conjectural* affine bridge. For p=13,19,37,43,67,373 it also computed independent original integer binomial expressions for A and B. **All finite assertions PASS; none imply an infinite-prime proof**.

|p|A mod p⁴|B mod p⁴|gαhα|gβhβ|Tα|Tβ|
|--:|--:|--:|--:|--:|--:|--:|
|13|19786|24180|8801|3380|17576|7761|
|19|82327|41173|31787|55974|79781|14801|
|67|16542032|18346610|16335538|18853867|19944627|507257|
|373|11832087049|5916043711|1636018284|6205292529|9160809876|289248818|

In particular Tβ(13) mod169 =156, whereas Tβ(19) mod361=0. Keep these as distinct integer/sign/valuation/source observations, not Frobenius or native geometry data.

## Exact continuation

**Parent remains open:** prove A_p≡p mod p³ for p≡13,19 mod24 or derive a genuine counterexample; stronger A_p−2B_p+pχ_{−3}(p)≡0 mod p⁴ remains UNPROVED. **Next smallest scientific action:** construct an actual two-index, residue-class-aware finite WZ/CM relation between both clipped square tails and product sources (especially p≡13 beta unit sources) together with the already proven original-series I3–I5 boundary; do not repeat completed high-port arithmetic. A fully p-dependent proof would not conflict with the rational no-go.

**Native evidence still missing:** #1559 fixed p=373 *same-original-class* H0/B0 divided-power [X]U mod139129, true semilinear Frobenius/basis/rank, odd signed Hesse/Green, κ and independent reproduction. Owner/executor is pending. No scalar regression replaces it.

**Control and contribution provenance:** Research lane chatgpt-research-onhour-enterprise-math-20260923 strictly separate from maintenance chatgpt-hourly-enterprise-math-20260921. Historical own recovery receipt at awdawmip/kimi-query-bridge#6632 has no current winning CLAIM/open/run; original request research-onhour-20261031-0205-dispatch-r15 at #6633 terminal FAILED UPSTREAM_CODE_REVIEW_REQUIRED. Do not replay request or borrow owner/session. Old neutral staging is not Source progress. This is **author-side saved proof/evidence only**, REGISTER_PENDING / NOT_ADMITTED; next lawful Source continuation must verify original receipt/own exact Source and ownership. Keep P000/ACTIVE worldview and immutable scientific source pin unchanged; recurring task configuration remains untouched.
