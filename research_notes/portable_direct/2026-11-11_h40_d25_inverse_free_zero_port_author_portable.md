# D25/LIFT — Integer-lifted two-port recurrence; inverse-free zero detection

**Date:** 2026-11-11. **Status:** AUTHOR_PROVED / EXACT_RATIONAL_AND_FINITE_FIELD_VERIFIED / UNREVIEWED / NOT_ADMITTED. Author-side portable mathematics, **not** a native Source CLAIM/checkpoint, accepted review, native X6 experiment, or proof of the universal zero-port character conjecture.

**Lineage:** Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN). Historical Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; scientific pin awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3 remains frozen. Input: prior author-derived exact two-port ODE recurrences at `research_notes/portable_direct/2026-11-11_h40_d25_two_port_differential_ode_closure_author_portable.md`. No claim of new native ownership or independent audit.

For m>=0, e∈{0,1}, define
\[
K_m^{(e)}(X)=\sum_{k=0}^m {m\choose k}{2m+e\choose k}X^k,\quad A_m=K_m^{(e)}(1/2),\quad B_m=(1-6e)A_m+6(K_m^{(e)})'(1/2).
\]

The **pair** (A_m,B_m), not its product, is the retained BRC observer. The existing rational theorem is
\[
d_n A_{n+1}=\alpha_n A_n+\beta_n A_{n-1}+\gamma_n A_{n-2},\qquad
c B_n=s_n A_n+t_n A_{n-1}+\rho B_{n-1}.
\]
Negative subscripts are zero; A_0=1, B_0=1-6e. Branch coefficients are:

| e | c | rho | d_n | alpha_n | beta_n | gamma_n | s_n | t_n |
|---|---:|---:|---|---|---|---|---|---|
|0|5|1|40(n+1)(2n+1)|371n²+331n+80|-81n²+137n-60|2n²-5n+3|24n+5|36n-25|
|1|8|5|64(n+1)(2n+3)|648n²+1096n+480|-371n²+331n-80|10n²-15n+5|-40|204n-35|

**Theorem (integral lifting and zero-preserving observer).** Set q_n=c d_n, P_n=∏_{j=0}^{n-1}q_j, U_n=P_n A_n, T_n=c^n P_n B_n, Q_n=c^nP_n (empty product=1). Then U_0=1, T_0=1-6e, Q_0=1, and

\[
U_{n+1}=c[\alpha_n U_n+\beta_n q_{n-1}U_{n-1}+\gamma_n q_{n-1}q_{n-2}U_{n-2}],
\]
\[
T_{n+1}=c^n[s_{n+1}U_{n+1}+t_{n+1}q_nU_n]+\rho q_n T_n,\qquad
Q_{n+1}=c q_nQ_n.
\]

Terms with negative indices vanish. All U_n,T_n,Q_n are integers and

\[
Q_m=\begin{cases}500^m(2m)!,&e=0,\\2048^m(2m+1)!,&e=1.\end{cases}
\]

For **every prime p>=5 of the form p=6m+1+4e**, Q_m is a unit modulo p. Consequently

\[
A_m\equiv c^m U_m Q_m^{-1}\ (\bmod p),\qquad
B_m\equiv T_m Q_m^{-1}\ (\bmod p).
\]
In particular
\[
A_m\equiv0\ (\bmod p)\iff U_m\equiv0\ (\bmod p),\quad
B_m\equiv0\ (\bmod p)\iff T_m\equiv0\ (\bmod p).
\]

**Proof.** Multiply the rational A recurrence by P_{n+1}=c d_n P_n; replace P_n/P_{n-1}=q_{n-1} and P_n/P_{n-2}=q_{n-1}q_{n-2}. This yields the U recurrence. Multiply the B recurrence at n+1 by c^nP_{n+1} and substitute U,T: this yields the T recurrence. Integrality follows by induction from the integer recurrences and initial states. The product identities ∏_{j<n} d_j=20^n(2n)! (e=0), respectively 32^n(2n+1)! (e=1), give the displayed Q. Since 2m+1<p at the target index and the base 500 (resp. 2048) is coprime to the applicable prime, Q_m is invertible (p=5 has m=0 and Q_0=1). Reconstruction and zero equivalence follow. QED.

**Algorithmic refinement with full cost model.** The direct input conversion uses e=0 for p≡1 mod6, e=1 for p≡5 mod6, m=(p-1-4e)/6. Keep U's three most recent states, T, the two most recent q's, Q and c^n; this is a constant number of O(log p)-bit field words. Each of m steps uses O(1) field additions/multiplications and **zero inversions**. For the two zero-port decisions there are zero inversions overall; for numerical values (A_m,B_m) a **single final inverse Q_m^{-1}** is reused for both. This improves auxiliary space from the previous inverse-table O(m) words to **O(1)**, while leaving time **O(m)** field operations plus at most one inversion; no sublinear time or general p-adic theorem is claimed.

**Exact checks (author side):** Independent rational binomial formulas verify 56 port-value identities for two branches and m=0..13; independent direct modular binomial sums cross-check 301 primes (p<=2000); the cleared recurrence runs through all **5131 primes 5<=p<=50000** (prior 5130 count started at p=7). All checks pass. The finite classifier counts 2583 A-zero and 2548 B-zero, including p=5. Source-native or independent review is not implied. Checker/certificate are in the local portable three-file bundle `D25_INVERSE_FREE_TWO_PORTS_AUTHOR_PORTABLE_20261111.zip`; these files' GitHub publication requires separate verification, if any.

**Remaining:** The observed (-6/p) port-selection theorem for *all* primes is still unproved here. Reuse this fast inverse-free exact checker to test genuine new finite-field identities, and retain provenance, epsilon, ordered ports and reconstruction scalar. Original UR V2 four-file object remains an *unrecovered original* (94687 bytes; SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76); do not reconstruct its claim or redo its mathematics.

**Control receipts:** `h40-20261111-0949-exact-d25-continuation` and `h40-20261111-0946-canonical-tasks` remained QUEUED at last read; use their original IDs for result/reconcile, do not create replacements. Native own recovery returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. Owner-level private custody does not establish this lane's platform identity, CLAIM or session authority. Formal Source checkpoint / Result / review remain pending.
