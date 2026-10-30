# D25/LIFT GH-137–GH-138: exact Casoratian and blind-band observer rank boundary

Date: 2026-10-30 (Asia/Hong_Kong). Research lane: `chatgpt-research-hourly-enterprise-math-20260923`. Mother task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.

**Evidence class:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Neither this Git file nor any portable program is a canonical Source checkpoint or authorized run. Old service session, request and staging are untouched.

## Input: established results and exact scope

For an odd prime \(p\ge5\), let \(N=(p-1)/2\), \(k=\mathbb F_{p^2}\), \(g_B(X)=X^2+X+B\), and \(d=B(1-4B)\). Use the GH-129 coefficient rows
\[
r_s=(A_s,E_s),\quad A_s=[X^N]g_B^{p-s},\quad E_s=[X^{3N+1}]g_B^{p-s},\qquad 1\le s\le N.
\]
For actual character moments \(m_s=S_{N+s}(B)\), GH-129 gives \(m_s=-A_sU-E_sV\) with Frobenius channels \(U=C^p,\ V=D^p\) (here \(D\) is GH-129's Hasse coefficient combination, distinct from the determinant below). This is inherited mathematics, not a new CM special-value evaluation.

On the smooth locus \(d\ne0\), GH-135 proved for each coefficient row
\[
4d\,s(s+1)r_{s+2}-2s(2s+1)(1-8B)r_{s+1}+(1-16s^2)r_s=0\quad(1\le s\le N-2).
\tag{1}
\]
GH-133 established the initial Wronskian \(A_1E_2-A_2E_1=-Nd^{N-1}\).

## GH-137 — exact all-window Casoratian theorem

Define \(\mathcal D_s=A_sE_{s+1}-A_{s+1}E_s\) for \(1\le s<N\). Then
\[
\boxed{\mathcal D_s=-N\,d^{N-s}\prod_{j=1}^{s-1}\frac{1-16j^2}{4j(j+1)}.}\tag{2}
\]
All scalar denominators are nonzero modulo \(p\); after expression as polynomials this identity extends to \(d=0\), but inversions below are restricted to \(d\ne0\).

**Proof.** From (1), \(r_{s+2}=\alpha_sr_{s+1}+\beta_sr_s\) with \(\beta_s=(16s^2-1)/(4ds(s+1))\). Therefore
\[
\mathcal D_{s+1}=-\beta_s\mathcal D_s=
\frac{1-16s^2}{4ds(s+1)}\mathcal D_s.
\]
Iteration from GH-133's exact \(\mathcal D_1\) proves (2). Both sides are polynomials in \(B\), and equality on the localization at nonzero \(d\) implies equality in the integral domain \(\mathbb F_p[B]\).

Set \(s_*=\lfloor(p+1)/4\rfloor\). For primes \(p\ge11\), precisely \(j=s_*\) within the recurrence range has \(1-16j^2\equiv0\bmod p\); for \(p=5,7\), this index lies at/after the last valid adjacent window. Thus for **every** odd \(p\ge5\) and smooth \(B\),
\[
\boxed{\mathcal D_s\ne0\ (1\le s\le s_*),\qquad
\mathcal D_s=0\ (s_*<s<N).}\tag{3}
\]
The first \(s_*\) adjacent pairs of moments recover the **entire formal two-channel state** \((U,V)\); no adjacent pair strictly after that boundary does. This is an exact observer-rank statement, not the assertion that two real elliptic curves realize every formal channel pair.

## GH-138 — central triangle for both prime classes

Write \(p=4h+\varepsilon\), \(\varepsilon=1\) or \(3\), \(h\ge1\). The central index is \(s_*=h\) for \(\varepsilon=1\), and \(s_*=h+1\) for \(\varepsilon=3\). Define \(e_*=3h+1\) in the first class, \(e_*=1\) in the second. Exact coefficient identities:
\[
\boxed{E_{s_*}=e_*,\quad E_{s_*+1}=0,\quad
A_{s_*+1}=(-1)^h\binom Nh[B(1-4B)]^h.}\tag{4}
\]
Consequently \(\mathcal D_{s_*}=-e_* (-1)^h\binom Nh d^h\ne0\) for smooth \(B\). All \(E_s\) with \(s\ge s_*+1\) vanish by degree.

**Independent combinatorial proof.** The maximum \(X\)-degree of \(g_B^{p-s}\) is \(2(p-s)\). For \(p=4h+1\), the coefficient of \(X^{3N+1}=X^{6h+1}\) in \(g_B^{3h+1}\) is \(3h+1\), and in \(g_B^{3h}\) is zero. For \(p=4h+3\), the corresponding coefficients in \(g_B^{3h+2}\) and \(g_B^{3h+1}\) are \(1,0\). For \(t=p-s_*-1\), multinomial extraction gives
\[
A_{s_*+1}=\sum_{a=0}^h c_aB^{h+a},\qquad
c_a=\frac{t!}{a!(N-2a)!(h+a)!}.
\]
Every denominator is invertible in \(\mathbb F_p\). Both residue classes satisfy \(c_0=\binom th\equiv(-1)^h\binom Nh\), and
\[
\frac{c_a}{c_{a-1}}=\frac{(N-2a+2)(N-2a+1)}{a(h+a)}
\equiv-4\frac{h-a+1}{a}\pmod p,
\]
since the numerator plus \(4(h-a+1)(h+a)\) equals \(-2p(a-h-1)\). Hence \(c_a=c_0\binom ha(-4)^a\), proving (4). For \(p\equiv3\bmod4\), this recovers GH-136; the \(p\equiv1\bmod4\) branch and the exact rank boundary are new here.

For \(d\ne0\), the central pair reconstructs
\[
U=-m_{s_*+1}/A_{s_*+1},\qquad
V=-(m_{s_*}+A_{s_*}U)/e_*.\tag{5}
\]
For every upper-tail index \(s\ge s_*+1\),
\[
m_s=(A_s/A_{s_*+1})m_{s_*+1}.\tag{6}
\]
This tail-only quotient is safe for **tail-only future observations**, not for recovering \(V\) or \(S_1=-U^p(V+2B^pU)\). A formal fiber witness is \((U,V)=(1,0)\) versus \((1,1)\): equal tails but \(S_1\) differs by \(-1\). No assertion that this pair consists of two actual Hasse parameters is made.

## Original mark and p=3347

For \(p\equiv3\bmod8,\ p\ge11\), the original mark \(T=2\sqrt2/3\), \(B_0=(1+T)/8\) satisfies \(d=1/144\in\mathbb F_p^\times\). Thus **every adjacent determinant lies in the prime field**, although individual rows need not. The full-rank to rank-one transition is exactly at \(s_*\).

For \(p=3347\): \(N=1673,h=836,s_*=837\), and GH-136 supplied \(A_{838}=954\). Direct modular evaluation of both (2) and (4) yields the **new exact determinant certificate**
\[
\boxed{\mathcal D_{837}(B_0)=2393\ne0,\qquad\mathcal D_{838}(B_0)=0\quad\bmod3347.}
\]
This is not a new complete finite-field character-sum enumeration.

## Exact checks and provenance

A standard-library Python checker builds the coefficient polynomials directly by multinomial expansion, tests (2)–(4) for 44 primes \(5\le p<200\) and multiple \(B\in\mathbb F_p\), enumerates every \(B\) for primes up to 43, tests all adjacent pairs for 11 original marked \(B_0\in\mathbb F_{p^2}\), and verifies the 3347 modular product independently. Observed:
`PASS_GH137_GH138_ROW_CASORATIAN` and `P3347_EXACT central_index=837 A_successor=954 last_nonzero_det=2393 first_zero_det=0`.
Finite checks are not the proof of the all-prime statements.

BRC observer carrier: \((p,B,s,U,V,\chi_k,\text{coefficient/source provenance})\). The future operations and fiber restrictions are explicitly scoped above. The finite-field auxiliary model does not purport to redefine the native six-dimensional P000/Heartbeat world.

**Remaining:** independently evaluate the originally marked central pair or \(S_1\) using CM/Jacobi/Gauss/\(p\)-adic theory, then test whether it predicts \(R_{3347}(9)=0\) without circular GH-129 reconstruction. GH-3, GH-83, native D25 \(H_0/B_0\) divided-power, \([X]U\bmod p^2\), Frobenius direction, \(\eta\) and \(p=373\) obligations remain open. Native Research authorization/Source reconciliation remains a separate control task. No scheduler or protected Source pin was modified.
