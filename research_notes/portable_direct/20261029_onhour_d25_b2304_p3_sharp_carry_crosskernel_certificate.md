# D25 / SECOND-DIGIT-LIFT: B2304 modulo p^3 exact cutoff repair, sharp three-level carry, and a source-resolved 373 cross-kernel witness

Research date: 2026-10-29 Asia/Hong_Kong. Evidence grade: AUTHOR-SIDE / EXACT FINITE-RING DERIVATION / EXECUTED 27-PRIME COEFFICIENT CHECKS / FIXED-373 CROSS-KERNEL INTEGER CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_H0_B0_NOT_EXECUTED.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Canonical Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3** (not rebased). Research-onhour logical conversation: chatgpt-research-onhour-enterprise-math-20260923, never the CONTROL_PLANE_MAINTENANCE conversation. This note is not a Source CLAIM, Result, review, new task, native H0/B0 experiment, or proof of the scalar LIFT target.

## 1. Original object, exact prior art and new question

For each prime p >= 11 with p congruent 3 or 5 (mod 8), in the p-local rationals put

\[
\beta_n=\frac{(1/8)_n(3/8)_n}{(n!)^2},\quad
\gamma_n=\frac{(1/4)_n(1/2)_n(3/4)_n}{(n!)^3},\quad
C_p(z)=\sum_{n=0}^{p-1}\gamma_n z^n.
\]

The **original** complete B2304 sum is \(B_p=[(1+8\theta)C_p(z)]_{z=1/9}\), with \(\theta=z\,d/dz\); coefficientwise \(\gamma_n9^{-n}=\binom{2n}{n}^2\binom{4n}{2n}/2304^n\). The classical Clausen identity, rather than a new axiom, gives the exact identity of formal power series over Q:

\[
\big(\sum_{n\ge0}\beta_nz^n\big)^2=\sum_{n\ge0}\gamma_nz^n.
\]

Source: NIST DLMF 16.12.2, https://dlmf.nist.gov/16.12.E2 . Consume the preceding author-side mod-p^2 truncation and mod-p Frobenius-carry proof at commit eb34b4e9fc759d5695a7e20d7a68d2007e36af97, and the independently executed p373 second-digit certificate at commit 4864ced8447b0953b9023fc017d68c142b9901cb. They are not reproved here.

The new question is the **full third-digit correction**, coefficientwise before evaluation, including the high-degree/source observer and the original weighted operator.

## 2. Theorem T1: complete third-digit cutoff repair (both target classes)

Define integers

\[
(a,b)=\begin{cases}
((p-3)/8,(3p-1)/8),&p\equiv3\pmod8,\\
((5p-1)/8,(7p-3)/8),&p\equiv5\pmod8.
\end{cases}
\]

Write \(K_b(z)=\sum_{n=0}^b\beta_nz^n\). Let \(\Pi_{<p}\) retain **original polynomial degrees** \(0,\dots,p-1\). Define over \(\mathbb F_p\)

\[
Q_a(z)=\sum_{i=0}^a(\beta_i\bmod p)z^i
 =\sum_{i=0}^a\binom ai\binom bi z^i,\qquad
J_{p,b}(z)=\sum_{j=b+1}^{p-1}
  \left(\frac{\beta_j}{p^2}\bmod p\right)z^j.
\]

The quotient is p-integral: the numerator of each p-local \(\beta_j\) has two p factors for \(b<j<p\), while its denominator is a unit. T1 is the exact polynomial congruence

\[
\boxed{C_p(z)\equiv\Pi_{<p}(K_b(z)^2)
             +2p^2\Pi_{<p}(Q_a(z)J_{p,b}(z))
       \pmod{p^3}.}
\tag{T1}
\]

**Proof.** In the range \(0\le n<p\), the numerator factors \(8i+1\) and \(8i+3\) meet their first multiples of p at the steps \(a\) and \(b\) (in the order appropriate to p mod 8). Since \(p\ge11\), neither linear factor in this range can contain \(p^2\). Therefore \(v_p(\beta_n)\) is exactly 0 for \(n\le a\), 1 for \(a<n\le b\), and 2 for \(b<n<p\). In the coefficients below degree p, the formal Clausen identity can use only indices below p. Split its companion series at b: \(K_{p-1}=K_b+p^2J_{p,b}\pmod{p^3}\). Squaring and applying the degree projection gives \(\Pi_{<p}K_b^2+2p^2\Pi_{<p}(K_bJ_{p,b})\). The last factor can be replaced by \(Q_a\bmod p\). The omitted tail square contains \(p^4\). All denominators up to degree p-1 are units, so the argument is coefficientwise in \(\mathbb Z_{(p)}[z]\). This proves T1 without a CM root assumption, numerical interpolation or an infinite-series evaluation.

Under the **original future observer**, let \(w=1/9\), \(D_B=1+8\theta\), and define the three source-distinguished contributions
\(U_B=[D_BK_b^2]_w\),
\(H_B=[D_B(1-\Pi_{<p})K_b^2]_w\), and
\(R_B=[D_B\Pi_{<p}(Q_aJ_{p,b})]_w\).
Then

\[
\boxed{B_p\equiv U_B-H_B+2p^2R_B\pmod{p^3}.}
\tag{T1-weighted}
\]

The subtraction of \(H_B\) happens **before** any finite-field substitution or differentiation. This is a typed BRC carrier: retain ordered pair \((i,j)\), signed contribution, \(i+j\), p-valuation, branch and observer operation; scalar total-only compression would lose a necessary later derivative/cutoff port. Applied BRC route: COMPOSE_APPLIED (finite-ring source-preserving observer); this does not claim a native X6 or original H0/B0 calculation.

## 3. Theorem T2: sharp degree/valuation filtration of the high carry

For p congruent 5 mod 8, \(2a\ge p\) and \(2b>p\). Write \(c_n=[z^n]K_b^2\). Then

\[
v_p(c_n)\ge1\quad(n>2a),\qquad
v_p(c_n)\ge2\quad(n>a+b),
\]

and these bounds are **sharp** at the layer endpoints:

\[
v_p(c_{2a})=0,\quad
v_p(c_{a+b})=1,\quad
v_p(c_{2b})=2.
\tag{T2}
\]

Here \(2a=p+(p-1)/4\), \(a+b=(3p-1)/2\), \(2b=(7p-3)/4\). **Proof:** coefficients are the pair sum \(\sum_{i+j=n,\,i,j\le b}\beta_i\beta_j\). If \(n>2a\), at least one index is \(>a\); if \(n>a+b\), either both indices are \(>a\), or at least one would be \(>b\), which is excluded. At degree \(2a\), only the pair (a,a) has valuation zero; at degree \(a+b\), only (a,b) and (b,a) have valuation one; at degree \(2b\), only (b,b) exists, with valuation two. Thus the corresponding endpoint coefficients are respectively \(\beta_a^2\bmod p\), \(2\beta_a\beta_b\bmod p^2\), and \(\beta_b^2\bmod p^3\), and no cancellation can raise their valuations. For p congruent 3 mod 8, \(2b=(3p-1)/4<p\), hence **there is no over-cutoff carry at all**, while T1's \(p^2\) missing-partner correction remains.

This supplies the exact next-two-digits extension of the previously established mod-p Frobenius carry: one cannot retain only the degree range through \(2a\) when computing mod \(p^2\) or mod \(p^3\).

## 4. Executed p=373 certificate and exact A216/B2304 source decomposition

For p=373, \(p^2=139129\), \(p^3=51895117\), \(a=233\), \(b=326\), and the three sharp endpoints have degrees \(466,559,652\). Executed pure-integer recurrence and **independent original binomial** readout give the following actual values mod \(p^3\):

| Source and observer | Residue mod 51895117 |
| --- | ---: |
| \(U_B=[(1+8\theta)K_{326}^2]_{1/9}\) | 49669053 |
| \(H_B=[(1+8\theta)(1-\Pi_{<373})K_{326}^2]_{1/9}\) | 14329914 |
| \(R_B=[(1+8\theta)\Pi_{<373}(QJ)]_{1/9}\), mod 373 | 246 |
| \(2(373)^2R_B\) | 16556351 |
| Original \(B_{373}\), independently from binomials | 373 |
| \(U_A=[(1+6\theta)H_{124}^2]_{1/2}\) | 51756361 |
| Original A216 third-digit partner correction \(2p^2R_A\) | 139129 |
| Original \(A_{373}\), independently from binomials | 373 |

Exactly, \(49669053-14329914+16556351=51895490\), hence \(B_{373}\equiv373\pmod{51895117}\).
The earlier second-digit high-carry value is recovered: \(14329914\bmod139129=138756=-373\bmod139129\).
The **full same-prime source-resolved bridge residual** is

\[
( U_A-U_B )+H_B+(2p^2R_A-2p^2R_B)
=2087308+14329914-16417222=0.
\tag{373-witness}
\]

This is a genuine zero integer identity for the chosen reduced representatives, not just a vague numerical agreement. It is *not* a proof of the all-prime bridge. The existing independently computed A216 correction was also recomputed by the new exact program as a regression, not claimed as newly discovered.

The executed checker covers 27 listed primes in the two mod-8 classes, validates all coefficients \(0\le n<p\) modulo \(p^3\), the three-stage carry endpoint conditions, the source-tagged weighted observer, and independent original B binomial sums. It also compares original A and B sums and all three source contributions for p=373. Actual program:
research_notes/portable_direct/d25_b2304_p3_full_cutoff_transport_guard_20261029.py,
immutable commit 0858ae0b00242039248280c0d765d99f2e24a72a,
Git blob f40f89c5e482d43ffca0a414f07b912bbb8f45e7;
locally executed source bytes matched the remote immutable Git blob.

Observed terminal checks:
PASS_D25_B2304_P3_UNIFORM_TRUNCATION_REPAIR 27 primes
CROSS_373: A_original=373, A_square=51756361, A_repair=139129,
B_square=49669053, B_high=14329914, B_repair=16556351,
B_original=373, A_minus_B=0.

## 5. Exact remaining frontiers and admission boundary

The **minimum next mathematical unit** is the *uniform* finite-character/CM/WZ evaluation of
\[
\mathcal D_p=(U_A-U_B)+H_B+2p^2(R_A-R_B)
\pmod{p^3}
\]
for both frozen target classes p congruent 13 and 19 modulo 24, using the original source-tagged p-adic carriers. The p congruent 19 class has \(H_B=0\); the p congruent 13 class has a sharp three-layer \(H_B\). A finite zero at 373, or a classical Clausen identity by itself, does not close this task. The taskbook's original scalar Delta-R port remains a separate unfulfilled proof obligation; a proof of A=B would require its exact source-aligned implication before any LIFT/JT2 completion statement.

**Native acceptance remains distinct and highest priority**: existing support https://github.com/awdawmip/enterprise-math/issues/1559, OPEN/PENDING_OWNER as checked this run. A genuinely authorized original-class native H0/B0 evaluator must compute p=373 divided-power \([X]U\bmod139129\), module rank, semilinear Frobenius direction and eta normalization, signed odd Green/Hesse, original kappa and Delta_p-R_p, with raw reproducible code/version, provenance and independent review. This finite-ring computation is not that benchmark, and no native code was substituted.

**Control recovery truth:** prior historical recovery Issue #6575 (request research-onhour-20261027-0501-recovery-r13) is read-only and showed no own winning Source claim/run, only a session pointer/neutral preserved staging; the original dispatch Issue #6576 (request research-onhour-20261027-0507-dispatch-r13) ended FAILED/TimeoutExpired. Current Site gateway had research_authority_granted=false, control active quota=5/5, and own checkpoint-list read was ACCESS_DENIED; these are concrete observations, not proof of global impossibility. No protected registration/prepare/claim/open/dispatch/Result mutation was attempted. Source-native session, claim, run, request and successful formal checkpoint remain **UNVERIFIED/NONE IN THIS RUN**, not invented from GitHub author-side commits. Reconcile the original request and current exact Source continuation *only under genuinely authorized execution context*, preserving frozen pin and the Research/maintenance lane separation.

State at this author-side semantic checkpoint: PROVED FINITE-RING DERIVATION / EXECUTED INTEGER REGRESSION / PUBLISHED PROJECT-NOTE AND SCRIPT / NOT INDEPENDENTLY REVIEWED / NOT ADMITTED / SOURCE_SYNC_DEBT. Do not replay earlier Clausen, 216 reflection, 781-prime scans or composite falsifiers as if they were new tasks. Do not mark native #1559 done or disable the ongoing research scheduler.
