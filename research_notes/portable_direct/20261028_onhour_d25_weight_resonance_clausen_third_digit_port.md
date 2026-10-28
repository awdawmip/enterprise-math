# D25 original 216 — unique weighted resonance and the third-digit Clausen source defect

Date: 2026-10-28 14:10 Asia/Hong_Kong. Classification: **AUTHOR-SIDE / EXACT ALGEBRAIC THEOREMS / 11 EXECUTED MODULAR CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED**.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Publication: `TP2-B6F4FC938FF94941C1B7`. Research ordinary-control logical label `chatgpt-research-onhour-enterprise-math-20260923`, distinct from CONTROL_PLANE_MAINTENANCE. The label is **not** a service-issued CLAIM or permission. Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

## Scientific question and authentic object

For every prime \(p=6m+1>3\), let \(R=\mathbf Z/p^3\mathbf Z\). The original 216 coefficient and weighted cutoff are
\[
a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3},\qquad
W_p=\sum_{n=0}^{p-1}(6n+1)a_n.
\]
All indexed denominators are units in \(R\), and no original cutoff, sign or weight is replaced. The present question is the precise information loss when applying the *original* weight operator to the finite coefficient state, and its numerical source correction relative to the already-proved original/Clausen bridge.

## Theorem 1 — one and only one resonance of the original weight operator

On the \(R\)-module \(M=R[z]_{\deg<p}\) with its coefficient basis \(1,z,\dots,z^{p-1}\), define \(\mathcal D=1+6z\,\partial_z\). Then
\[
\mathcal D(z^n)=(6n+1)z^n,\qquad
p\mid (6n+1)\ \Longleftrightarrow\ n=m
\quad(0\le n<p).
\]
Proof: If \(6n+1=kp\), then \(1\le k\le5\), while reduction modulo 6 and \(p\equiv1\bmod6\) gives \(k\equiv1\bmod6\), hence \(k=1\) and \(n=m\). Conversely \(6m+1=p\). All other diagonal entries are p-units. Multiplication by diagonal units therefore puts \(\mathcal D\) in Smith normal form
\[
\operatorname{diag}(1,\ldots,1,p,1,\ldots,1).
\]
Consequently
\[
\boxed{\ker(\mathcal D:M\to M)=p^2R\,z^m,\qquad
\operatorname{coker}\mathcal D\simeq R/pR\simeq\mathbf F_p.}\tag{1}
\]
A concrete observer-fiber witness is \(A(z)\) versus \(A(z)+p^2z^m\): they have identical \(\mathcal D A\bmod p^3\) but different unweighted values at \(z=1\) modulo \(p^3\). Thus any future operator requiring the unweighted full-\(p^3\) coefficient must retain this extra coordinate; the **current weighted-\(p^3\) observable** needs only \(a_m\bmod p^2\), since its resonant contribution is \(p\,a_m\). This information-loss theorem does **not** assert a native H0/B0 module rank or an unproved equivalence to the X6 state.

## Theorem 2 — the resonance has a nontrivial, explicit original–Clausen correction

Reuse the prior exact coefficientwise Clausen identity, with the same \(p=6m+1\) and \(0\le n\le2m\):
\[
T_n^{(0)}=\frac{(-3m)_n(-2m)_n(-4m)_n}{2^n(n!)^3},\qquad
E_n=\prod_{j=1}^n(1-p/(2j))^{-1}(1-p/j)^{-1}.
\]
The coefficient of \(z^n\) in the exact Clausen square \(G_m(z)^2\) is \(T_n^{(0)}E_n\), where \(G_m(z)={}_2F_1(-m,-2m;1-p/2;z/2)\). This input is from the already published exact Clausen denominator bridge; it is **consumed**, not reproved.

At the unique resonant index \(n=m\), define exact \(p\)-local rational sums
\[
L_m=\sum_{j=0}^{m-1}\left(\frac1{2(-3m+j)}+
\frac1{3(-2m+j)}+\frac2{3(-4m+j)}\right),\qquad
H_m=\sum_{j=1}^m\frac1j .
\]
All denominators here are p-units. Because \(p=6m+1\), the original numerator parameters equal
\[
1/2=-3m+p/2,\quad1/3=-2m+p/3,\quad2/3=-4m+2p/3.
\]
The three Pochhammer products, term-by-term through \(j<m\), therefore give
\[
a_m\equiv T_m^{(0)}(1+pL_m)\pmod{p^2}.
\]
Independently the exact denominator product gives \(E_m\equiv1+(3p/2)H_m\pmod{p^2}\). Subtracting, then multiplying by the **original resonant weight \(6m+1=p\)**, proves for every such prime
\[
\boxed{(6m+1)\bigl(a_m-T_m^{(0)}E_m\bigr)
\equiv p^2 T_m^{(0)}\left(L_m-\tfrac32H_m\right)\pmod{p^3}.}\tag{2}
\]
The displayed \(p^2\) contribution is part of the previously established \(pD_1\) signed source correction. At \(n=m\), its second-order unweighted jet contributes at order \(p^3\) to the weighted sum and hence may be omitted **only for this mod-\(p^3\) weighted observer**; it remains relevant to distinct future unweighted readouts. This identifies a sharp per-index source port rather than proving the sum of all remaining ports vanishes.

## Exact independent integer certificates

Python 3 standard-library modular arithmetic recomputed the original \(\binom{2n}n^2\binom{3n}n/216^n\), the independent terminating triple-Pochhammer coefficient, the exact Clausen denominator product and both p-adic first-order logarithmic sums. It also independently summed the original full signed \(n=0,\ldots,p-1\) cutoff for eleven primes
\[
7,13,19,31,37,43,61,67,73,211,373.
\]
All 11 exact checks of (1)–(2) passed. Target checks of \(W_p\equiv p\bmod p^3\) passed for \(13,19,37,43,61,67,211,373\), as *finite examples only*.

For \(p=373,m=62,p^2=139129,p^3=51895117\), the independently calculated integer residues are
\[
a_{62}=32200,\quad T_{62}^{(0)}=117244,\quad E_{62}=110409\pmod{139129},
\]
\[
L_{62}=151,\quad H_{62}=73,\quad L_{62}-3H_{62}/2=228,\quad
T_{62}^{(0)}=122\pmod{373}.
\]
Therefore \((122)(228)\equiv214\pmod{373}\) and the two distinct original/Clausen resonant weighted terms are
\[
p\,a_{62}=12010600,\qquad p\,T_{62}^{(0)}E_{62}=34132111\pmod{51895117},
\]
\[
\boxed{12010600-34132111\equiv29773606=214\cdot373^2\pmod{373^3}.}\tag{3}
\]
The independent complete original sum gives \(W_{373}=373\bmod373^3\). The original resonant coefficient contributes \(a_{62}=32200\bmod139129\) to its normalized \(W_{373}/373\); the sum of all other original source indices contributes \(106930\bmod139129\). They add to 1 modulo 139129. This demonstrates a **nonzero** original third-digit source correction even at a prime where the whole target congruence holds.

Companion executable: `research_notes/portable_direct/d25_original216_weight_resonance_guard_20261028.py`. Actual execution marker: `PASS_D25_ORIGINAL216_UNIQUE_RESONANCE_SOURCE_DEFECT 11 exact-prime-cases`.

## Theorem 3 — exact harmonic reflection and classical Fermat-quotient transport

Let \(H_j=\sum_{k=1}^{j}k^{-1}\in\mathbf Z_{(p)}\) for \(j<p\), and define the classical Fermat quotient \(q_p(b)=(b^{p-1}-1)/p\bmod p\), for p not dividing b. Reorganizing **the same three original signed shifted-factor sums** gives an *exact rational identity*
\[
L_m=\frac{H_{2m}+H_{3m}+2H_m-4H_{4m}}6.
\]
Since \(p-1=6m\), the reflection \(j\mapsto p-j\) gives \(H_{4m}\equiv H_{2m}\pmod p\). Hence, by elementary algebra alone,
\[
\boxed{L_m-\tfrac32H_m\equiv
\frac{H_{3m}-3H_{2m}-7H_m}6\pmod p.}\tag{4}
\]
Here no outside result beyond elementary finite-field reflection is needed.

For a **second, optional external-arithmetic observer**, consume the *classical, pre-existing* Eisenstein/Emma-Lehmer congruences
\[
H_{3m}\equiv-2q_p(2),\quad
H_{2m}\equiv-\tfrac32q_p(3),\quad
H_m\equiv-2q_p(2)-\tfrac32q_p(3)\pmod p.
\]
These are imported standard harmonic congruences (not claimed as our discoveries): Emma Lehmer, *Annals of Mathematics* **39** (1938), 350–360, DOI https://doi.org/10.2307/1968791 ; the p/6 statement is also documented at https://oeis.org/A238201 . Substituting them in (4), using \(q_p(ab)\equiv q_p(a)+q_p(b)\pmod p\), yields
\[
\boxed{L_m-\tfrac32H_m\equiv
2q_p(2)+\tfrac52q_p(3)
=\tfrac12q_p(2^4\,3^5)=\tfrac12q_p(3888)
\pmod p.}\tag{5}
\]
Equation (2) therefore has the sharper entirely exact-number-theoretic form
\[
\boxed{(6m+1)(a_m-T_m^{(0)}E_m)
\equiv\frac{p^2T_m^{(0)}}2q_p(3888)\pmod{p^3}.}\tag{6}
\]
This is a **source-port formula**, not a formula for the total original sum. In particular a zero at one prime does not imply all-prime zero. The new work is the derivation connecting this *particular original resonant source* to the imported classical quotient; no novelty is claimed for Lehmer's identities.

The same independent standard-library checker now also verifies (4), all three classical congruences and (5)–(6) at 11 primes, without floating point. At p=373 the exact additional residues are
\[
(H_m,H_{2m},H_{3m},H_{4m})=(73,108,338,108),\
(q_p(2),q_p(3),q_p(3888))=(204,301,83).
\]
Thus \(83/2\equiv228\pmod{373}\) and \(122\cdot228\equiv214\pmod{373}\), agreeing with the original independent \(214p^2\) certificate. At p=13, \(q_{13}(3888)=0\bmod13\), whereas p=373 gives 83; this illustrates that the isolated source defect is not universally zero.

**Exact next mathematical unit:** combine (6) with a genuine, independent formula for the **remaining original source indices** in the Clausen \(pD_1+p^2D_2\) bookkeeping. The required remainder at each target prime must cancel \(\tfrac12T_m^{(0)}q_p(3888)\) and the other existing p-adic source ports. Do not sum a tautological decomposition of the already-known full W and call it an all-prime proof.

## BRC and native-world typing

**BRC COMPOSE_APPLIED** to the original finite signed integer carrier \((p,n,6n+1,a_n,T_n^{(0)},E_n,\nu_p,\text{source label})\). Original index n and weight, all low/middle/high bands and residual \(p^2\cdot214\) remain distinguishable. Observer is \(\mathcal D A\bmod p^3\), original \(W_p\bmod p^3\), separately the unweighted future operations on A. Equation (1) is an exact fiber-constancy obstruction, and (2) is a source-preserving repair coordinate. The scalar polynomial z is an explicitly **external arithmetic observation**, not an independent native spatial plane, X6 cell coordinate, physical dynamics, or a same-original-class H0/B0 divided-power computation. P000 Heartbeat native X6 Cell plus separately typed time and its joint-relation preservation constraints remain intact.

## Source execution status and exact continuation

Current Site gateway read at 2026-10-28 14:01 Asia/Hong_Kong: v0.6.11, `research_authority_granted=false`, `write_relay_enabled=false`, static machine read-only, so no new current session, Source winning CLAIM, OPEN, native checkpoint, formal activity or Result is asserted. Prior on-hour recovery bridge request `research-onhour-20261027-0501-recovery-r13` / kimi-query-bridge #6575 is a successful read of historical local session pointers and neutral staging; prior dispatch `research-onhour-20261027-0507-dispatch-r13` / #6576 has final FAILED / TimeoutExpired. Do not replay or borrow any maintenance identity. Current Site checkpoint read returned ACCESS_DENIED. Project README/source claims still require legal canonical Source continuation for formal execution.

Native evidence priority: `awdawmip/enterprise-math#1559` was OPEN at 2026-10-28 14:10 Asia/Hong_Kong, actual executing owner not established. Required original \(p=373\) H0/B0 divided-power \([X]U\bmod139129\), module rank, semilinear Frobenius direction/eta, original signed odd Green/Hesse, \(\kappa\), \(\Delta_p-R_p\), full raw provenance and independent reproduction. This author-side scalar certificate **does not** satisfy that experiment.

Smallest next mathematical task: insert the exact resonant contribution (2) into the existing low/middle/high \(D_1,D_2,\gamma,G'\) bookkeeping, identify a *non-circular* telescoping identity for the **remaining indices** which cancels the p373 value 214 and general \(T_m^{(0)}(L_m-\tfrac32H_m)\) across both frozen target classes. The fully general \(W_p\equiv p\bmod p^3\) remains OPEN. Other Research lanes' recent GH-36/GH-37 proofs are separately sourced, with no borrowed ownership or automatic contribution merger. D25/LIFT/JT2 remains OPEN. The author note/program are pending independent review and formal Source admission.
