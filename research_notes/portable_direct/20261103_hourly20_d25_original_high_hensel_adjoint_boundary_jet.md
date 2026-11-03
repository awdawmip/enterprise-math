# D25 — Original 216 high-strip Hensel adjoint and terminal-source jet

2026-11-03 +08. **Author-side TASK_RESEARCH portable mathematics. UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** Logical research lane: chatgpt-research-hourly-enterprise-math-20260923. Maintenance lane not used: chatgpt-hourly-enterprise-math-20260921. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. This artifact is not a native Source checkpoint or Result.

**Question and reused inputs.** Previous high-band f_s represents original b_(3r+1+s)/p² only modulo p; the onhour lane's repaired middle/high reciprocal carrier expressly is not the original high factorial unit modulo p². Derive the original-source second digit and lift the high-band Green adjoint, preserving the actual terminal edge. Inputs: 20261103_hourly20_d25_fermquotient_middle_second_digit.md, 20261103_hourly20_d25_h2_adjoint_three_moment_normal_form.md, 20261103_onhour_d25_middle_h2_hensel_dual_defect.md, 20261103_onhour_d25_three_edge_hensel_gluing_and_fermat_elimination.md. Their existing results are consumed rather than re-claimed.

Let p=6r+1>=7 be prime, n=3r, chi=(6/p). All congruences are in the p-local ring. Define
\[
b_k=\frac{(2k)!(3k)!}{(k!)^5 216^k},\quad R_k=\frac{b_{k+1}}{b_k}=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3},\quad \epsilon=3+\frac{q_p(2)-3q_p(3)}2\pmod p.
\]
Set Y_s=b_(n+1+s)/p² for 0<=s<=r, and f_0=1, f_s/f_(s-1)=s(36s²-1)/[9(2s+1)^3] for 1<=s<r.

## Theorem A. Genuine high-band p-adic second digit

For 1<=t<=r-1 let
\[
\lambda_t=\frac1{2t}+\frac3{6t-1}+\frac3{6t+1}-\frac3{2t+1},\quad\Lambda_s=\sum_{t=1}^s\lambda_t,\quad\Lambda_0=0\pmod p.
\]
Then
\[
\boxed{Y_s\equiv\frac{\chi}{9}f_s[1+p(\epsilon-3+\Lambda_s)]\pmod{p^2},\quad0\le s<r.}\tag{A}
\]
**Proof.** The original entrance R_n/p=(9p²-1)/[18(p+1)^3]=-1/18(1-3p) modulo p², times the established b_n/p=-2chi(1+p epsilon), gives Y_0=chi/9(1+p(epsilon-3)). For 1<=t<r,
\[
R_{n+t}=\frac{(p+2t)[(3p+6t)^2-1]}{18(p+2t+1)^3}
\equiv\frac{t(36t^2-1)}{9(2t+1)^3}[1+p\lambda_t]\pmod{p^2}.
\]
Each denominator is a p-unit over the stated interior. Multiplying exact consecutive original ratios proves the assertion.

## Theorem B. Original middle/high pair at the next digit

Let j=n-s, x_s=b_j/p and recall the previously proved middle data
\[
u_s=\prod_{t=1}^s\frac{9(2t-1)^3}{t(36t^2-1)},\quad
E_s=\sum_{t=1}^s\big(\frac1{2t}+\frac3{6t-1}+\frac3{6t+1}-\frac3{2t-1}\big),\quad
x_s\equiv-2\chi u_s[1+p(\epsilon+E_s)]\pmod{p^2}.
\]
Direct cancellation proves the exact rational factorization u_s f_s=(2s+1)^(-3). It follows that
\[
\boxed{x_sY_s\equiv-\frac{2}{9(2s+1)^3}[1+p(2\epsilon-3+E_s+\Lambda_s)]\pmod{p^2}.}\tag{B1}
\]
Using j=(p-1-2s)/2, equivalently
\[
\boxed{x_sY_s\equiv (36j^3)^{-1}(1+p\kappa_s)\pmod{p^2},\quad\kappa_s=2\epsilon-3+E_s+\Lambda_s-\frac3{2s+1}\pmod p.}\tag{B2}
\]
B2 extends the existing mod-p Laurent pairing by one original-source digit and preserves orientation, weights, and both separate defects.

## Theorem C. Hensel-lifted finite Green adjoint with nonzero exiting flux

For t=s+1 define
\[
A(s)=\frac{t(6t-1)(6t+1)}9,\quad D(t)=\frac{108t^2+4t-1}{18(2t+1)},\quad
\mathcal L_pP(s)=[A(s)+pD(s+1)]P(s+1)-(2s+1)^3P(s).
\]
For every polynomial P with p-integral coefficients:
\[
\boxed{\sum_{s=0}^{r-1}\mathcal L_pP(s)Y_s\equiv-\frac{\chi}{9}[1+p(\epsilon-3)]P(0)+\frac{p\chi}{18}(2r+1)^3f_{r-1}P(r)\pmod{p^2}.}\tag{C}
\]
**Proof.** The exact forward flux cofactor equals
\[
(2s+3)^3R_{n+s+1}=\frac{(2t+1)^3(p+2t)[(3p+6t)^2-1]}{18(p+2t+1)^3}
\equiv A(s)+pD(t)\pmod{p^2}.
\]
The denominator 2t+1 is a p-unit for ALL 1<=t<=r, including t=r. Therefore the exact cofactor telescopes as (2s+3)^3 P(s+1)Y_(s+1)-(2s+1)^3P(s)Y_s; its finite sum is (2r+1)^3P(r)Y_r-P(0)Y_0. The original exit R_(4r)/p=1/2 modulo p implies Y_r=p chi f_(r-1)/18 modulo p². Insert the proven entrance Y_0. The logarithmic derivative lambda_r has a 1/p pole, so the endpoint is handled by the nonsingular D(t) expansion instead. In particular the previous vanishing mod-p terminal becomes a genuinely nonzero mod-p² P(r) flux.

For signed H2(p)=sum_(k=3r+1)^(4r)(6k+1)b_k, the same original lift yields
\[
\boxed{H2(p)/p^2\equiv\frac{\chi}{9}\sum_{s=0}^{r-1}f_s\{(6s+4)+p[3+(6s+4)(\epsilon-3+\Lambda_s)]\}\pmod{p^2}.}\tag{D}
\]
This preserves the genuine 3p part of the signed original weight. It refines the H2 observer modulo p^4, but by itself does not prove the frozen mother W_(p-1)=p modulo p^3 for p mod24 in {13,19}.

## Executed exact validation and research frontier

Companion Python-standard-library checker constructs original p-free factorial units; independently checks all oriented middle/high x_s,Y_s, exact u_s f_s, B1/B2, exact Taylor cofactor at EVERY edge, genuine Y_r, (C) for P=1,s,s²,s³,6s+4, and signed (D). Actual local result: **PASS 148 primes, 7<=p<=2000 and p=1 mod6; 22,952 oriented positions.** Samples (p, H2/p² modulo p²) = (7,33), (13,75), (19,161), (37,797), (373,68898); corresponding p=373 H2 modulo p^4 = 9585709842. The algebra proves the general formulas; finite tests are independent integer regression, not a formal independent review or native experiment.

BRC carrier: original b_j and b_(p-j), valuations 1/2, oriented j=n-s, middle defect E_s, high defect Lambda_s, chi, Fermat epsilon, original signed weight, and terminal P(r). These transformations preserve their stated mod-p² observer, not any unmeasured future operation. Native Heartbeat-X6/P000 and immutable science pin are unchanged.

Next unit: use (C) in a genuinely p-dependent signed low-middle-high Green/WZ coupling, respecting edges 2r,3r,4r. Test exact p=13,19,373 certificates before universal mother claim. The high second digit helps discriminate proposed lifted certificates; the original mother second-digit cancellation remains open.

Native control observed on 2026-11-03: Gateway 0.6.11 returned UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, control quota 5/5. Earlier read-only recovery issue #6637 (2026-11-01) reported session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94, no local pending/run/unopened/upload and two neutral preserved staging manifests; continuation #6638 definitively FAILED. That dated recovery is not current Source ownership. No new CLAIM/OPEN/native checkpoint/Result/review/registration; preserve old sessions and protected staging.