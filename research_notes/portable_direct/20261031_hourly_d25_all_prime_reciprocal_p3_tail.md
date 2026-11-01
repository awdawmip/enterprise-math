# D25/LIFT — all-prime reciprocal p³ tail, with two differential boundary sources

2026-10-31, TASK_RESEARCH portable author-side mathematics. Logical conversation: \`chatgpt-research-hourly-enterprise-math-20260923\`, distinct from maintenance. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen Source \`c47e13e4aba0e006366f989d6334d443f6333ae3\`; P000 ACTIVE_LOCKED unchanged. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. These are external p-adic polynomial identities, not P000 native X6 results.

## Scope and attribution

Previous same-lane GH-174/GH-175 and reciprocal Gauss–Clausen mirror reports established the p≡1(mod6) case; the all-prime factorial valuation and sharp coefficientwise prefix were also proved earlier. This unit **extends the reciprocal polynomial and two-source operator identities to every p≡5(mod6), including the special p=5 weighted exception**, and integrates a uniform p⁴ scalar correction. No rediscovery, independent review or prior-art exhaustion is claimed.

## Theorem — original coefficient, all primes p≥5

Let a_n=binom(2n,n)^2 binom(3n,n)/216^n=(2n)!(3n)!/((n!)^5 216^n), θ=X d/dX and W=1+6θ. For prime p≥5 set h=floor((p−1)/3), q=floor(2p/3)=p−1−h, N=q+1=p−h.

The previously proved exact valuation formula v_p(a_n)=floor(2n/p)+floor(3n/p) gives v_p(a_n)=3 on N≤n≤p−1. Hence T_p(X)=p^{−3} Σ_{n=N}^{p−1}a_n X^n lies in Z_(p)[X]. Let bars denote coefficientwise reduction mod p.

**Uniform reflected-tail polynomial identity:**

\[
\boxed{\overline T_p(X)=-\frac1{18}\sum_{k=1}^{h}\frac{X^{p-k}}{k^3\overline{a_k}}\quad\text{in }\mathbf F_p[X].}\tag{1}
\]

Every denominator is invertible because 1≤k≤h<p/3. For F_p(X)=Σ_{n=0}^{p−1}(6n+1)a_nX^n, this yields the full **fourth-digit polynomial correction**

\[
\boxed{F_p(X)-\sum_{n=0}^{q}(6n+1)a_nX^n\equiv
\frac{p^3}{18}\sum_{k=1}^{h}\frac{6k-1}{k^3\overline{a_k}}X^{p-k}\pmod{p^4}.}\tag{2}
\]

In particular the scalar at original fixed X=1 satisfies

\[
\boxed{\frac{F_p(1)-\sum_{n=0}^{q}(6n+1)a_n}{p^3}
\equiv \frac1{18}\sum_{k=1}^h\frac{6k-1}{k^3\overline{a_k}}\pmod p.}\tag{3}
\]

Lifts of right-side mod-p residues do not change results after multiplication by p³.

**Proof.** Wilson's theorem and Fermat's little theorem give
(2p−2)!/p ≡ (p−1)!(p−2)! ≡ −1 (mod p),
(3p−3)!/p² ≡ 2((p−1)!)²(p−3)! ≡ −1 (mod p),
and ((p−1)!)⁵·216^{p−1}≡−1 (mod p). Thus a_{p−1}/p³≡−1 (mod p).

The exact coefficient recurrence is
a_{n+1}/a_n=(2n+1)(3n+1)(3n+2)/(36(n+1)³).
Put b_k=(a_{p−k}/p³) mod p. For 1≤k<h, reflection of this recurrence gives

\[
\frac{b_{k+1}}{b_k}\equiv
\frac{36k^3}{(2k+1)(3k+1)(3k+2)}
=\frac{k^3\overline{a_k}}{(k+1)^3\overline{a_{k+1}}}\pmod p.
\]

Therefore k³ ā_k b_k is constant. Since a_1=1/18 and b_1=−1, its constant value is −1/18. This proves (1). Apply W and use 6(p−k)+1≡1−6k to obtain (2), then set X=1 to obtain (3). QED.

At p=5, h=1 and 6h−1=5, so the **weighted** tail is 0 coefficientwise modulo p⁴ while the unweighted T_p is not zero modulo p. At every p≥7 the weighted X^{p−1} coefficient of T_p is 5≠0 mod p, so no coefficientwise p⁴ prefix can omit it. This is an observer-dependent distinction, not a claim of universal scalar non-cancellation.

## Theorem — two universal differential sources

For \(\mathcal L=\theta^3-\frac X2(\theta+\frac12)(\theta+\frac13)(\theta+\frac23)\),

\[
\boxed{\mathcal L\overline T_p(X)=
N^3\,\overline{a_N/p^3}\,X^N-\frac1{18}X^p\quad\text{in }\mathbf F_p[X].}\tag{4}
\]

Proof: the exact a_n recurrence cancels every interior coefficient. The first term X^N is the omitted-predecessor boundary N³a_N/p³; the final term X^p is
−(2p−1)(3p−2)(3p−1)/36·a_{p−1}/p³ ≡ −1/18 mod p. This remains nonzero even for p=5 where W T_p ≡0 mod 5. The p≡1mod6 instance was GH-174; this extends the scope, not the origin of that lemma. QED.

## Actual precise regression and boundaries

The adjacent executable standard-library Python file uses the original rational recurrence modulo p⁴. It checks every mirrored coefficient, all coefficients of (4), terminal coefficients, (2) at X=1, and independent integer-binomial coefficients at twelve anchor primes. Executed once on 2026-10-31: **548 primes 5≤p<4000 PASS**, including **277 primes p≡5mod6**; **337,559** individual mirror indices, twelve direct-binomial anchors. Examples (p,h,weighted tail mod p, X^N boundary coefficient): (5,1,0,4), (7,2,6,5), (11,3,6,9), (13,4,5,5), (19,6,4,1), (373,124,278,277). Program marker: \`PASS_D25_ALL_PRIME_RECIPROCAL_P3_TAIL_TWO_BOUNDARY_EXACT\`. Exact script SHA256 d0f46bac4777b6d2870564cf5061c27876d71386a27d53792949c0848f1754f0, execution-log SHA256 af99ce3d26e2f1f27060da5d60916ecc56b35c99166dea82bb0bb9d77c64f03f. Finite tests are regression evidence, **not** the universal proof.

Literature guard: the 216-series occurs in Ramanujan's 3√3/π identity (MathOverflow Q508786); different p-adic series in Guo–Zudilin 2018 \`arxiv:1803.01830\` and Qi 2026 \`arxiv:2604.04006\` are not substitutes for this exact 216 target.

**BRC interface:** retain source-tagged p,n,a_n,weight W, valuation wall, mirror index, coefficient-vs-scalar observer, p³ division, original X=1 and two boundary impulses. COMPOSE_APPLIED the existing exact valuation/mirror interfaces; no transfer to P000 native geometry or cancellation of unsigned mass by signed sums.

**Next exact mathematics:** Frozen D25 all-prime-target scope remains prove the complete signed \`C+L-J+I≡0 (mod p)\` for p≡13,19(mod24). Formula (3) gives a **fourth-digit** correction and does not close this **third-digit** proof. Seek a finite WZ/CM bridge preserving original 216 weighting and both lower valuation-wall sources. Do not redo GH-174 p≡1 case or promote the all-prime character scan to a theorem.

**Control:** This run's native status reported Gateway 0.6.11, research_authority_granted=false, executor_binding_configured=false, 5 active/5 max jobs, new_job_allowed_by_quota=false and upstream code review required. #6424/#6425 are historical read-only SUCCEEDED receipts with execution_authorized=false, not a current owner claim. No session, CLAIM, OPEN, Source-native checkpoint, freeze, Result, review or activity registration has been performed here. Protected earlier staging left untouched. Existing owner support: \`awdawmip/enterprise-math#1558\`; native experiment \`#1559\`. Exact follow-up when current Source allows: fresh own recovery → canonical continuation → lawful identity/session transition → typed successor prepare → winning CLAIM → authorized OPEN → fresh Source readback → truthful native checkpoint.