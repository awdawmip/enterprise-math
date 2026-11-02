# D25: second-lift central binomial reflection and complete Cauchy carry modulo p^3 (2026-11-02)

Status: AUTHOR-DERIVED / EXACT-PROVED (two theorems) / EXACT-CHECKED (207 primes) / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research conversation chatgpt-research-hourly-enterprise-math-20260923. Extends research_notes/portable_direct/20261102_hourly_r11_d25_cauchy_truncation_carry.md; no native control authority is claimed.

## Exact coefficients and the retained observer

For every prime p=6r+1 >=7 let

\[
A_m=\binom{2m}{m}^{2}\binom{3m}{m}/216^m,\quad
B_j=\binom{2j}{j}/8^j,\qquad 0\le m,j<p.
\]

The omitted Cauchy triangle m+j>=p contributes moments
\[
J_0=\sum_{m+j\ge p}A_mB_j,\qquad
J_1=\sum_{m+j\ge p}(m+j)A_mB_j.
\]
The sum always runs over 0<=m,j<p. Source: Roman Le Lan, Series for 1/pi arising from Cauchy product, arXiv:2604.03327v2 (2026-04-10), together with the preceding D25 exact p^2 truncation theorem; the p-adic conjecture in the paper is not imported as a theorem.

## Theorem 1: a universal reflected coefficient to the next digit

For any prime p>=5 and 1<=s<p/2 define
\[
u_s=-\frac1{4sB_s},\quad
H_n=\sum_{t=1}^n t^{-1},\quad
q_p(8)=\frac{8^{p-1}-1}{p},\quad
h_s=2(H_{2s-1}-H_{s-1})-q_p(8)\pmod p.
\]

Then all denominators are p-units and
\[
\boxed{\frac{B_{p-s}}p\equiv u_s(1+ph_s)\pmod{p^2}.}
\]

Proof. The following identity in rational integers is exact:
\[
\frac1p\binom{2p-2s}{p-s}=
\frac{\prod_{j=1}^{p-2s}(p+j)\big(\prod_{t=1}^{s-1}(p-t)\big)^2}{(p-1)!}.
\]
Writing the first product as (p-2s)! times \(\prod_{j\le p-2s}(1+p/j)\), expanding the remaining factors \(p-t=-t(1-p/t)\) modulo p^2, and using \(H_{p-2s}\equiv H_{2s-1}\pmod p\) proves
\[
\frac1p\binom{2p-2s}{p-s}\equiv
-\frac{2}{s\binom{2s}{s}}\bigl[1+2p(H_{2s-1}-H_{s-1})\bigr]\pmod{p^2}.
\]
Multiply by 8^{-(p-s)} and use 8^{1-p}=1-pq_p(8) modulo p^2. QED.

## Theorem 2: the complete p^3 second-carry law

For 1<=m<=3r write
\[
U_m=\sum_{s=1}^m u_s,\quad V_m=\sum_{s=1}^m(m-s)u_s,\quad
\widehat U_m=\sum_{s=1}^m u_sh_s,\quad
\widehat V_m=\sum_{s=1}^m(m-s)u_sh_s.
\]
Define low-index lifts modulo p^2
\[
K_0^{[2]}=\sum_{m=1}^{2r}A_mU_m,\qquad
K_1^{[2]}=\sum_{m=1}^{2r}A_mV_m.
\]
Define six corrected provenance ports (modulo p):
\[
\begin{aligned}
D_0&=\sum_{m=1}^{2r} A_m\widehat U_m,&D_1&=\sum_{m=1}^{2r} A_m\widehat V_m,\\
M_0&=\sum_{m=2r+1}^{3r}(A_m/p)U_m,&M_1&=\sum_{m=2r+1}^{3r}(A_m/p)V_m,\\
L_0&=\sum_{m=3r+1}^{4r}(A_m/p^2)\sum_{j=p-m}^{3r}B_j,&
L_1&=\sum_{m=3r+1}^{4r}(A_m/p^2)\sum_{j=p-m}^{3r}(m+j)B_j.
\end{aligned}
\]
For all primes p=6r+1 >=7,
\[
\boxed{J_0\equiv pK_0^{[2]}+p^2(D_0+M_0+L_0)\pmod{p^3},}
\]
\[
\boxed{J_1\equiv pK_1^{[2]}+p^2(D_1+K_0^{[2]}+M_1+L_1)\pmod{p^3}.}
\]

Proof. The p-valuations of A_m on the successive intervals [0,2r], [2r+1,3r], [3r+1,4r], [4r+1,p-1] are 0,1,2,3; those of B_j are 0 for j<=3r, 1 above. For m<=3r, every omitted term has j=p-s>3r and Theorem 1 applies. The first interval contributes pK_i^[2] plus p^2D_i; the weight m+j=p+(m-s) contributes the extra p^2K_0^[2] to J1. The second interval contributes p^2M_i. On 3r+1<=m<=4r precisely the low-j range p-m<=j<=3r survives, yielding p^2L_i. Every other term has valuation at least three. QED.

The low-j ports L0,L1 preserve genuine information missed by extending high-tail reflection across the whole triangle. This reduction is certified only for the declared p^3 readout.

## Exact executable checks and new finite certificates

The companion Python standard-library script independently constructs complete omitted moments J0/J1 via prefix sums modulo p^3 and checks the two theorems for all 207 primes <=3000 with p≡1(mod6). A separate integer binomial reconstruction of original coefficients for p=7,13,19,31,37,43,373 also passes. Its 107 target primes in classes 13/19 recheck the previously discovered K0≡0, K1≡-1/2 modulo p; these two universal identities remain open.

For the tested target primes, observed second-carry digits (J0/p^2 mod p, (2J1+p)/p^2 mod p) are:
13:(7,9); 19:(1,8); 37:(22,14); 43:(1,39); 61:(37,2); 373:(252,173); 1171:(326,305). These are finite exact certificates; the companion log records all six D/M/L component digits.

BRC: COMPOSE_APPLIED to source-preserving Cauchy p^2 kernel. Carrier is the original (m,j) with factorial valuations and signed weights; observer is the ordered pair (J0,J1) together with D/M/L port labels. The p-adic formulas use external integer/field arithmetic, not a claimed P000-native geometry transfer.

Next mathematical unit: independently prove or falsify the K0 and K1 congruences on all p≡13,19(mod24); investigate WZ/finite-field hypergeometric/CM Hasse-invariant routes. Use the D/M/L ports to carry the resulting relation to the original 216 modulo-p^3 goal. Preserve prior finished math and frozen science pins.

## Control preservation

Historical own recovery via kimi-query-bridge#6637 was read-only SUCCEEDED: session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94; no pending mutation/run/unopened claim/upload; historical staging dispositions remained neutral. Existing exact continuation #6638 was FAILED / UPSTREAM_CODE_REVIEW_REQUIRED (five named current control checkers), so it was not replayed. Fresh Gateway 0.6.11 status on 2026-11-02 still shows CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5. Repair owner: enterprise-math#1558. H0/B0 issue #1559 separately outstanding. No session_start, CLAIM, OPEN, native checkpoint, Result, review or formal admission occurred in this unit. Current write is neutral author-side Git evidence; Researcher registration remains pending.
