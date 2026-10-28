# D25/LIFT GH-79 — Double-zero fiber of the odd-degree source and safe normalization

2026-10-29 Asia/Hong_Kong. Portable TASK_RESEARCH author derivation, stable Research logical conversation \`chatgpt-research-hourly-enterprise-math-20260923\`. Distinct from control-maintenance conversation. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; mother objective \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\` OPEN. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Status: \`AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING\`.

## GH-79A: exact ordinary-point multiplicity bound

Reuse GH-78's original GH-16 finite coefficient polynomial for each prime \`p=4d+3>=7\`:
\[
U_d(z)=\sum_{r=0}^{d}h_rz^r,\quad h_0=1,\quad
\frac{h_{r+1}}{h_r}=\frac{(4r+3)^3}{(4r+4)(4r+5)(4r+6)},
\quad \theta=z\frac{d}{dz}.
\]
The entire polynomial obeys the source-derived differential equation over \(\mathbb F_p\):
\[
\mathscr L U_d=0,\qquad
\mathscr L=\theta(\theta+\tfrac14)(\theta+\tfrac12)
-z(\theta+\tfrac34)^3.
\]
The coefficient of the highest derivative \(U_d'''\) is \(z^3(1-z)\). **Theorem:** At any ordinary point \(a\in\mathbb F_p\setminus\{0,1\}\), \(U_d\) has root multiplicity at most two. Indeed, if \(U_d(a+w)=\sum_{j=k}^{d}b_jw^j\) with \(k\ge3\), the coefficient of \(w^{k-3}\) in \(\mathscr L U_d\) equals
\[
a^3(1-a)k(k-1)(k-2)b_k\ne0
\]
because \(k\le d<p\). Contradiction. No characteristic-zero uniqueness theorem is imported across characteristic \(p\).

The original GH-16 double-pole obstruction is \(\mathcal H_d=(8\theta+5)U_d=8zU'_d+5U_d\). Thus at every ordinary \(a\), if \(U_d(a)=U_d'(a)=0\), then \(U_d''(a)\ne0\) and
\[
\boxed{\mathcal H_d(a)=0,\qquad
\mathcal H_d'(a)=8aU_d''(a)\ne0.}\tag{79.1}
\]
There is a **source-preserving alternative** whenever \(\mathcal H_d(a)=0\):
- if \(U_d(a)\ne0\), the normalized derivative \(U'_d(a)/U_d(a)=-5/(8a)\) is valid;
- if \(U_d(a)=0\), the observer relation forces \(U_d'(a)=0\), and the nonzero second derivative is the necessary repair coordinate.

This is a general conditional theorem, not a claim that \(\mathcal H_d(9)\) vanishes for every prime.

## GH-79B: p=23 exact falsifier of uniform logarithmic normalization

Choose \(p=23,\ d=5,\ z=9\). The original recurrence gives, coefficientwise in \(\mathbb F_{23}\),
\[
\boxed{U_5(z)=1+10z+7z^2+21z^3+19z^4+11z^5.}
\]
At \(z=9\), exact formal derivatives are
\[
(U_5(9),U_5'(9),U_5''(9))=(0,0,21)\pmod{23}.
\]
The original labeled observed obstruction is
\[
\mathcal H_5(z)=(8\theta+5)U_5(z)
=5+15z+9z^2+11z^3+13z^4+12z^5,
\]
\[
(\mathcal H_5(9),\mathcal H_5'(9))=(0,17)\pmod{23},
\quad 17\equiv8\cdot9\cdot21\pmod{23}.
\]
Hence \(U'_5(9)/U_5(9)\) is **undefined**, while the genuine GH-16 obstruction has a *simple* zero; reducing all observer channels to the logarithmic derivative destroys the source behavior. This witness refutes a proposed uniform \(\log U\) normalization, **not** the \(p\equiv7\pmod8\) GH-3 vanishing conjecture.

For the real Laurent rank sources GH-15/GH-16, \(\alpha_{23}=12\), \(Q_{23}=\alpha_{23}9^{2d+2}/8=2\), rank weights
\[
(C_0,\dots,C_5)=(1,9,2,9,3,19).
\]
Consequently the exact *parameter derivatives* of all rank double-pole coefficients are
\[
(A'_0(9),\dots,A'_5(9))=(11,14,17,14,19,3)\ne0
\quad(\bmod23).
\]
This is original-source first-order \(\mathbb F_{23}[\varepsilon]/(\varepsilon^2)\) information; no integer \(23^2\) result is asserted.

## Exact scope of finite checks

Executed Python standard-library script against all 78 primes \(7\le p<2000\) satisfying \(p\equiv7\pmod8\). It constructed GH-16 \(U_d\) independently from its recurrence, evaluated exact \(U_d(9),U'_d(9),U''_d(9),\mathcal H_d(9),\mathcal H'_d(9)\), and checked both derivative identities. In this finite range:
- 37 primes \(p\equiv23\pmod{24}\) showed \(U_d(9)=U_d'(9)=0,\ U_d''(9)\ne0,\ \mathcal H_d'(9)\ne0\).
- 41 primes \(p\equiv7\pmod{24}\) showed \(U_d(9)\ne0,\ U'_d(9)\ne0,\ \mathcal H_d'(9)\ne0\); one has \(U_d''(9)=0\).
- Every tested prime had \(\mathcal H_d(9)=0\). **Each residue-class assertion over all primes remains a conjecture**; the conditional multiplicity theorem and concrete \(p=23\) witness are author-proved.

BRC \`COMPOSE_APPLIED\`: retain original (p,d,r,z), ordered GH-16 coefficient recurrences, U and \(\mathcal H\) distinguished, the jets (U,U',U''), rank Laurent A_r and derivatives, and integer versus dual-number provenance. Do not collapse a vanishing scalar port into a nonexistent logarithmic derivative; retain the \(\mathcal H'\) repair witness. These are external auxiliary arithmetic charts, not X6 native geometry, W/S, or the six native Hasse ports.

## Continuation and authority

Inherited GH-15/16, GH-17/18, GH-75, GH-78 author records are reused with exact hypothesis/domain. GH-79's conditional theorem **does not require GH-75**, whereas GH-77's \(p\equiv3\pmod8\) nonzero transverse slope uses the still-unreviewed GH-75 split.

Next smallest open scientific unit: for \(p\equiv7\pmod8\), prove or refute the two tentative mod-24 alternatives \(\{p\equiv23: U(9)=U'(9)=0\}\) and \(\{p\equiv7: U(9)\ne0,\ \mathcal H(9)=0\}\) with a genuine independent arithmetic/CM certificate, then propagate source-faithfully into original GH-3 endpoints and Laurent first-order residual. Preserve GH-76 p=3 mod8 BL and endpoints, p² and native experiments independently.

2026-10-29 native status 0.6.11: research_authority_granted=false; executor_binding_configured=false; source_sync.control.state=CODE_REVIEW_REQUIRED; own authenticated subject quota active_jobs=5/5. No native CLAIM/open/run/checkpoint or authorized review is asserted. Existing support issue enterprise-math#1558 governs exact old request/session/frontier and staging recovery; these were not modified. P000 ACTIVE, source pin and scheduler settings unchanged.
