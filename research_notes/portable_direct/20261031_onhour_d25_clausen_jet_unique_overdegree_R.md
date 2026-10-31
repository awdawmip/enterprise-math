# D25/SECOND-DIGIT-LIFT — unique overdegree boundary of the Clausen p-adic parameter jet

2026-10-31 Asia/Hong_Kong. Research logical lane: chatgpt-research-onhour-enterprise-math-20260923 (separate from control maintenance). Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. **Frozen science pin** c47e13e4aba0e006366f989d6334d443f6333ae3. P000 ACTIVE_LOCKED and current ACTIVE residual-fidelity position unchanged. **AUTHOR-DERIVED / EXACT EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / PORTABLE_ONLY**. This is external p-adic mathematics, not the native H0/B0 divided-power experiment.

## 1. Original source and exact Clausen observer

For a prime p=6l+1≥7, set

\[
a_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
A_p=\sum_{n=0}^{p-1}(6n+1)a_n .
\]

The previously known **classical Clausen identity** is

\[
{}_3F_2(1/2,1/3,2/3;1,1;z)
=\big[{}_2F_1(1/6,1/3;1;z)\big]^2.
\]

Take H(z)=Σ_{0≤k<p}h_k z^k with h_k=(1/6)_k(1/3)_k/(k!)², θ=z d/dz, W=1+6θ, and τ_{<p}, τ_{≥p} the coefficientwise truncation operators. By Clausen's identity and exact coefficient comparison through degree p−1,

\[
A_p=[W\,\tau_{<p}(H^2)]_{z=1/2},\quad
M=H(1/2),\quad N=[(1+12\theta)H]_{z=1/2},
\quad MN=[W H^2]_{z=1/2}.
\]

These are exact rational equalities for the original weighted 216 model (with H truncated at p). No supercongruence has been assumed.

## 2. All-prime parameter-jet support theorem

Let t be an ordinary **formal hypergeometric parameter**, not native time. For 0≤k<p,

\[
K_k(t)=\frac{(-l+t/6)_k(-2l+t/3)_k}{(k!)^2}
=u_k+t v_k+t^2 w_k+O(t^3),
\quad J_r(z)=\sum_{k=0}^{p-1}[t^r]K_k(t)z^k\ (0\le r\le2).
\]

**Theorem.** For every prime p=6l+1≥7 in the indicated local coefficient ring Z_(p):

\[
H(z)\equiv J_0(z)+p J_1(z)+p^2 J_2(z)\pmod{p^3}
\quad\text{coefficientwise},
\]

\[
\deg J_0\le l,\quad \deg J_1\le 2l,\quad \deg J_2\le p-1.
\]

For 2l<k<p there is the exact rational equality

\[
u_k=v_k=0,\qquad
w_k=\frac{(-1)^l l!(2l)!(k-l-1)!(k-2l-1)!}{18(k!)^2}.
\]

**Proof.** We have −l+p/6=1/6 and −2l+p/3=1/3. Denominators 6,3,k! are p-units for k<p, so substituting t=p into the Taylor polynomial is exact modulo p³. At k>l the first rising factorial contains one factor t/6, and at k>2l the second also contains t/3. The first two coefficient arrays thus have sharp support bounds. Multiplying the two linear factors at indices l and 2l gives the displayed w_k, with the remaining factors producing (−1)^l l!(k−l−1)! and (2l)!(k−2l−1)!. QED.

Because p=6l+1, degrees of J0², J0J1, J1² are ≤2l,3l,4l <p. Consequently **the only product with a degree≥p term through precision p³** is the p² term 2J0J2:

\[
\boxed{A_p\equiv MN-p^2 B_p\pmod{p^3}},
\qquad
B_p=\left[2W\,\tau_{\ge p}(J_0J_2)\right]_{z=1/2}\bmod p.
\tag{1}
\]

This is an exact operator/scope-specific *single-overdegree-port* representation. It does not erase the other source-labeled Euler–Clausen terms in the original 11-region decomposition, nor prove the remaining second-digit cancellation.

## 3. Identification of the existing signed R_p without source substitution

For 0≤i≤l, u_i=binom(l,i)binom(2l,i). An overdegree monomial i+k≥p has k=p−a, 1≤a≤i. Define

\[
g_i=\binom li\binom{2l}i2^{-i}\pmod p,\quad
c_a=2^{-(p-a)}w_{p-a}\pmod p .
\]

Tracking W's original signed 6n+1 weight before reduction,

\[
\boxed{B_p=2\sum_{i=1}^{l}g_i
\sum_{a=1}^{i}(1+6(i-a))c_a\pmod p.}
\tag{2}
\]

Using Wilson's theorem on the factorial w_{p−1}, and 2^{p−1}≡1 (mod p),

\[
c_1=\frac{(-1)^l l!(2l)!(5l-1)!(4l-1)!}{18}
\equiv\frac{1}{18(l+1)(2l+1)}
\equiv\frac1{10}\pmod p.
\]

The factorial reflections are (5l−1)!≡(−1)^l/(l+1)! and (4l−1)!≡1/(2l+1)!. The ratio of consecutive c_a from the formula for w is

\[
\boxed{c_{a+1}/c_a\equiv
36a^2/((6a+5)(3a+2))\pmod p},\quad1\le a<l.
\]

Its denominators are p-units on this interval. The seed and recurrence exactly agree with the **previously frozen** c_a definition in research_notes/portable_direct/20261031_onhour_d25_E2_first_digit_dependency_closure.md and the associated original signed Clausen R_p double sum. Thus

\[
\boxed{B_p\equiv R_p\pmod p;\quad
A_p\equiv MN-p^2R_p\pmod{p^3}.}\tag{3}
\]

The R_p equality is a proved identification of previously established mathematics. The new derivation is the degree-support uniqueness and explicit jet transport.

## 4. New finite-jet form of the exact remaining second-digit obligation

On frozen primes p≡13,19(mod24), the previously completed first-digit UR gives M≡0 (mod p), MN≡p (mod p²), and hence J0(1/2)≡0 (mod p). Define **p-integral** numbers at z=1/2:

\[
L_0=J_0(1/2)/p+J_1(1/2),\quad
N_0=[(1+12\theta)J_0]_{1/2},\quad
N_1=[(1+12\theta)J_1]_{1/2}.
\]

Then L0N0≡1 (mod p). Expanding M/p=L0+pJ2(1/2) modulo p² and N=N0+pN1 modulo p² inside (1) proves

\[
\boxed{\frac{A_p-p}{p^2}\equiv
\frac{L_0N_0-1}{p}
+L_0N_1
+J_2(1/2)N_0
-B_p\pmod p.}\tag{4}
\]

The first quotient is integral under the stated frozen first-digit theorem. The **remaining mathematical target** is a single all-target proof that the right side vanishes; its four displayed sources are integer carry, first-jet derivative, second jet, and original signed R boundary. This is a different observer decomposition of the still-open original C01+F2+I_p cancellation, not an independently proved vanishing or an altered target.

## 5. Actual exact finite computation

Executed a self-contained Python standard-library integer-and-modular-inverse verifier on **67 primes p≡1(mod6), 7≤p<800**, including **37 target primes p≡13,19(mod24)**. At every prime the script independently checked: all original integer-binomial a_n vs full Clausen coefficient convolution for every n<p; all three parameter jets modulo p³ and their degree walls; each explicit high w_k; B_p=Q/p²=the independently reconstructed frozen R_p, with Q=MN−A_p taken modulo p³; and (4) at every target prime. Anchor (p,B_p,R_p,residual) values: (7,3,3,not-target), (13,0,0,0), (19,12,12,0), (37,11,11,0), (43,15,15,0), (61,3,3,0), (67,21,21,0), (373,196,196,0). Marker: PASS_D25_CLAUSEN_UNIQUE_OVERDEGREE_JET_SIGNED_R_EXACT. This is finite validation, not an all-prime proof of the target.

Local complete execution and proof sources were prepared under the same respective filenames. No Lean formalization or original-class H0/B0 native execution is claimed. The original benchmark remains awdawmip/enterprise-math#1559, OPEN/unassigned on 2026-10-31, requiring p373 original divided-power [X]U mod139129, real semilinear Frobenius/basis, module rank, signed Green/Hesse, κ and independent repetition.

## 6. BRC and recovery

The BRC carrier retains (original 216 index/weight, p and p-adic valuation, formal jet degree, Gauss index, overdegree p−a, signed W observer, original R source and scientific pin). Jet parameter t is not a seventh spatial axis or a native temporal field. Equation (4) is observer-scoped; it is not an information-loss certificate across future native operations.

At the 2026-10-31 read, Gateway 0.6.11 reports research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED and native control quota 5/5. Own prior recovery awdawmip/kimi-query-bridge#6632 has no current claim/run; original dispatch #6633 ended FAILED/UPSTREAM_CODE_REVIEW_REQUIRED. Historic staging is neutrally archived, not adopted as Result. No native session/CLAIM/OPEN/checkpoint/Result/review authority is inferred from publishing this author-side note. Formal Source state: REGISTER_PENDING / SYNC_DEBT.

**Next exact mathematical move:** seek a finite shifted-parameter WZ/CM certificate equating the three lower jet sources in (4) to the **signed** overdegree B_p, requiring nonzero anchor p=19 and p=373; keep the existing original 11-port and native H0/B0 benchmarks unchanged. Reconcile own original requests and current exact continuation before any future role-bound Source write. Do not use maintenance identity.
