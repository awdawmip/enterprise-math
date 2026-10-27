# D25/LIFT SB-TRANSFER-C — exact finite Green boundary transport and correlated principal parts

> **2026-10-27 source-level provenance correction:** The originally drafted section label “R55” is historical/local, not a new canonical sequential R55: the repository already contained `20261027_hourly_d25_midpoint_high_chart_lift_r54_r55.md` with R55 on the original full scalar's sharp precision. This independent **SB-TRANSFER-C** concerns the *general rational Green adjoint boundary-change matrix* for arbitrary observer weights and the c1-specific source syzygies; it consumes R47/R50, R51/R52 and the earlier genuine low-half R53 and midpoint/high R54/R55 rather than recrediting them. Its restriction to c1 does not solve the real R23 full W/S supercongruence. No canonical numbering, task authority or mathematical acceptance is acquired by author publication.


2026-10-27 (Asia/Hong_Kong). Portable author-derived research for the TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923. Exact task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Mother D25/LIFT/JT2 remains OPEN; frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

Classification: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This note treats the original rational W/S two-source recurrence and exact finite observers, not an original-class H0/B0 native run, six-channel Hasse assertion, canonical Source checkpoint or full W/S supercongruence.

## R55.1 — universal one-step finite Green boundary transport

Use R47's unchanged original W/S two-source recurrence and labelled difference d_k=W_k-S_k. Define

\[
\alpha_k=a_k-b_k,\qquad
\beta_k=a_ka_{k+1}-b_kb_{k+1},\qquad
\gamma_k=a_kb_k(a_{k+1}-b_{k+1}).
\]

The exact recurrence is

\[
\alpha_kd_{k+2}-\beta_kd_{k+1}+\gamma_kd_k=0. \tag{55.1}
\]

Fix arbitrary rational observer weights c_0,...,c_{N-1}, and let C_N,C_{N+1} be R50's authentic finite Green boundary coefficients, satisfying

\[
\sum_{k=0}^{N-1}c_kd_k=-C_Nd_N-C_{N+1}d_{N+1}.
\]

**Theorem R55.1.** Whenever \(\gamma_N\neq0\), the *same unchanged source and observer* obey the shifted authentic boundary identity

\[
\boxed{\sum_{k=0}^{N-1}c_kd_k=-C'_{N+1}d_{N+1}-C'_{N+2}d_{N+2},}\tag{55.2}
\]

\[
\boxed{
\begin{pmatrix}C'_{N+1}\\C'_{N+2}\end{pmatrix}
=
\begin{pmatrix}
\beta_N/\gamma_N&1\\
-\alpha_N/\gamma_N&0
\end{pmatrix}
\begin{pmatrix}C_N\\C_{N+1}\end{pmatrix}.
}\tag{55.3}
\]

This is the R50 adjoint boundary for the extended horizon N+1 with new weight c_N=0; the low-end observable and both source labels are unmodified.

**Proof.** Solve (55.1) for d_N:
\(d_N=(\beta_Nd_{N+1}-\alpha_Nd_{N+2})/\gamma_N\). Substitution into the original exact Green identity proves (55.2) and (55.3); appending c_N=0 leaves the bulk sum unchanged. The uniquely defined R50 finite adjoint at the later horizon produces these same two coefficients. QED.

## R55.2 — integral boundary shift and the special three-prime singularity

Let p>=13 be prime with p congruent to 1 modulo 6, and set \(N=\lfloor(3p-1)/4\rfloor+1\). R51 proves

\[
v_p(\alpha_N)=\lambda_p,\qquad
\lambda_p=\begin{cases}1,&p\in\{139,199,277\},\\0,&\text{otherwise},\end{cases}
\]

and R53 proves \(a_{N+1}-b_{N+1}\in\mathbb Z_p^\times\). Since \(a_N,b_N\) are units,

\[
\boxed{\gamma_N=a_Nb_N(a_{N+1}-b_{N+1})\in\mathbb Z_p^\times.}\tag{55.4}
\]

Consequently, the entire boundary relocation matrix (55.3) is p-integral, with determinant \(\alpha_N/\gamma_N\). Its first row contains the unit entry 1, hence

\[
\boxed{\operatorname{SNF}(T_N)=\operatorname{diag}(1,p^{\lambda_p})}
\tag{55.5}
\]

up to p-adic unit factors. At ordinary target primes this is a coefficient-space integral automorphism. At the exceptional three primes it has precisely one lost residue digit modulo p, even though the original labelled source state remains two-dimensional. More specifically, \(\beta_N\equiv a_N(a_{N+1}-b_{N+1})\not\equiv0\pmod p\) at the exceptional primes. General Green coefficient vectors do **not** automatically improve their pole order under this shift: exact correlation of their leading parts matters.

For the specific low-rank c_1=1 observer, R51 has the exact coefficients

\[
Q_N=\frac{a_N/B-b_N/A}{D},\qquad
Q_{N+1}=\frac{1/A-1/B}{D},\qquad
D=a_N-b_N,\;A=w_N/w_1,\;B=s_N/s_1,
\]

with \(U-V=Q_Nd_N+Q_{N+1}d_{N+1}\). They satisfy two **source-specific exact syzygies**

\[
\boxed{Q_N+a_NQ_{N+1}=\frac1A,\qquad
Q_N+b_NQ_{N+1}=\frac1B.}\tag{55.6}
\]

**Proof.** Expanding the first left-hand side gives
\((a_N/B-b_N/A+a_N/A-a_N/B)/D=1/A\); replace a_N by b_N in the last term to obtain 1/B. These are rational equalities for every rank where the original transitions are defined; they are not restricted to a finite sample.

At the exceptional primes, R51 gives \(v_p(Q_N)=v_p(Q_{N+1})=-4\), but \(v_p(1/A)=v_p(1/B)=-3\). Thus
\(p^4(Q_N+a_NQ_{N+1})\equiv0\pmod p\). For every *freely varying* labelled \((U,V)\in\mathbb Z_p^2\), not merely the factorial initial pair, let \(x_j=d_j/p^3\). Exact source evolution implies

\[
x_{N+1}=a_Nx_N+D_N(B/p^3)V\equiv a_Nx_N\pmod p.
\]

Therefore the apparently order-\(p^{-1}\) principal parts of the old fourth-order Green boundary terms cancel for *every state in the actual correlated source image*. Treating x_N and x_{N+1} as independent would discard that information. In the new boundary coordinates (55.3), R53 proves each coefficient has valuation at least -3 and their minimum is exactly -3. The fourth-order singularity of the old endpoint choice is removable by an **authentic one-rank boundary relocation** for this low-rank observer; it is not automatically removable for arbitrary c_k or for the undeveloped full Hasse/PF observer.

## Executed author verification

The independent exact Fraction checker 20261027_hourly_d25_green_boundary_relocation_r55_check.py was run locally. It checks both identities (55.6), calculates the transformed coefficient pair both from (55.3) and directly from the new source endpoints, checks gamma_N is a unit, and evaluates exact rational p-adic valuations at p=13,19,37,139,181,199,277,373. It returned PASS. The local Git blob and connected-GitHub readback are the same: f7e86b34efacbf17bbfce9fe79ae4a1300a05f74.

| p | N | old first valuation | old second | shifted first | shifted second |
|---:|---:|---:|---:|---:|---:|
| 13 | 10 | -3 | -3 | -3 | -3 |
| 19 | 15 | -3 | -3 | -3 | -3 |
| 37 | 28 | -3 | -3 | -2 | -3 |
| 139 | 105 | -4 | -4 | -3 | -3 |
| 181 | 136 | -3 | -3 | -3 | -3 |
| 199 | 150 | -4 | -4 | -3 | -3 |
| 277 | 208 | -4 | -4 | -3 | -3 |
| 373 | 280 | -3 | -3 | -3 | -3 |

The all-prime claims follow from algebra plus R51/R53, not from extrapolating these eight tests. Independent Driver review, Lean formalization, original H0/B0, [X]U modulo p^2 and native p=373 execution remain separate evidence obligations.

## BRC source fidelity and next frontier

BRC COMPOSE_APPLIED to the signed labelled two-source carrier, exact diagonal source operations, valuation-sensitive finite dual observer and boundary-change operation. The Smith invariant and the syzygies preserve branch/provenance correlations; the leading p-adic residues are not independent positive masses. This rational arithmetic representation is not a proved native X6 dynamics or complete three-dimensional slice. P000 is unchanged.

New portable unit R55 consists of the exact all-observer boundary relocation matrix, its p-integral invariant factors, and the two source syzygies with their universal correlated-principal-part cancellation. Earlier R47–R54 results retain their original scope and credit.

**Next precise scientific unit:** obtain the original R23 low-half weighted discrepancy and R36 fixed-z=2 six-channel PF-Green concomitant at their exact scientific pins. Apply (55.3) to the *actual full coefficient vector*; identify any true extra finite or positive-infinity Hasse source and test unchanged-input, source-labelled cross-rank WZ telescoping against R38–R42 high-rank valuations, including p=139,181,199,277,373. Do not replace the native experiment or CM/Frobenius eta/kappa tests with this portable rational computation.

**Native control:** The own-lane recovery at awdawmip/kimi-query-bridge#6622 and continuation #6623 (2026-10-27 19:58 +08) show no current winning CLAIM or authorized run. Source persisted checkpoint and later predecessor CLAIM still disagree, covered by awdawmip/enterprise-math#1558. Preserve the old service session, request IDs, 16 contribution IDs and two neutral staging manifests; do not replay the rejected continuation_prepare. GitHub portable publication is not native Source publish_checkpoint, Result, independent review or Research-Activity registration; the latter remains REGISTER_PENDING until a current authorized write and readback.
