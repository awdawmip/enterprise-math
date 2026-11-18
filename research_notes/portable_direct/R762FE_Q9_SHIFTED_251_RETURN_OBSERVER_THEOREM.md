# R762FE — Mod-9 shifted-return BRC observer: sharp 57-trit loss and 251-scalar certificate

Date: 2026-11-19 (Asia/Shanghai). Scope: six named positive BRC branches, all 729 terminal coefficients in the three-coordinate **research slice**, not the native signed Cell/Link/Port event. This is independent portable research under the immutable scientific taskbook \`awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`. Preserve P000 and \`TRIADIC_CLOSURE_E\` unchanged. Inputs R762EM/EO (127 distinct eigenvalues, one zero, remaining \(v_3(\lambda)\ge1/3\)) and R762FC (unshifted 58-trit observer loss) are author-side, NOT_REVIEWED.

## Exact statement

Let \(G=(\mathbb Z/9\mathbb Z)^3\), \(R=\mathbb Z[G]\), and
\[
P=1+X+Z+XY+YZ+XYZ,
\quad a_n=[0]P^n,\quad r=126.
\]
Every monomial is a *named positive BRC path choice*. Let
\[
H^+=(a_{i+j+1})_{0\le i,j<126},
\qquad B^+=([g]P^{j+1})_{g\in G,\ 0\le j<126}.
\]
The columns of \(B^+\) are complete \(729\)-terminal vectors. All coordinates retain their third component.

**Theorem (sharp shifted precision loss).**
\[
\boxed{\min\{k\ge0:\ \forall M\ge0,\ \forall c\in\mathbb Z^{126},
\ H^+c\in 3^{M+k}\mathbb Z^{126}\Longrightarrow
 B^+c\in3^M\mathbb Z^{729}\}=57.}
\]
Thus dropping the zero-eigenvalue mode by shifting the observer to time 1 reduces the original 127-dimensional observer to 126 dimensions, and reduces the *optimal* uniform terminal precision surcharge from 58 to 57 trits. The 126×126 Hankel matrix is rationally invertible: the return moments are a Vandermonde sum with nonzero positive integer multiplicities for the 126 distinct nonzero eigenvalues, and the characteristic-zero determinant is nonzero.

## Exact Smith certificate

Use the deterministic six-branch convolution in \`R762FE_Q9_SHIFTED_SMITH_VERIFY.cpp\`; all calculations are integers reduced modulo \(3^p\), with \(p=140\) and independently repeated at \(p=180\). Simultaneously perform 3-adic Smith row/column elimination
\[
U H^+ V=\operatorname{diag}(3^{e_j}u_j),\
U,V\in GL_{126}(\mathbb Z_3),\quad u_j\in\mathbb Z_3^\times.
\]
Apply *the same column operations* to all rows of \(B^+\). Define \(b_j=\min_gv_3((B^+V)_{g,j})\). Both precision runs agree on **every one of the 126 triples**
\((e_j,b_j,e_j-b_j)\), recorded in \`R762FE_Q9_SHIFTED_SMITH_EVIDENCE.json\`:

- \(v_3(\det H^+)=\sum e_j=6104\), \(\max e_j=112\);
- \(\max_j(e_j-b_j)=57\), attained at zero-based \(j=125\) with \((e,b)=(112,55)\);
- all certified pivot and output valuations are less than 140, and all are identical at 140/180 trits;
- direct recomputation using the tracked right-operation matrix \(V\) yields \(v_3(H^+V e_{125})=112\) and \(v_3(B^+V e_{125})=55\). One attaining terminal is zero-based index 2, i.e. \((0,0,2)\).

**Proof of sufficiency.** As
\[
B^+(H^+)^{-1}
=(B^+V)\operatorname{diag}(3^{-e_j}u_j^{-1})U,
\]
the sharp column valuation bound shows every entry of \(3^{57}B^+(H^+)^{-1}\) lies in \(\mathbb Z_3\). Consequently \(H^+c\in3^{M+57}\) implies \(B^+c\in3^M\mathbb Z_3^{729}\), hence in \(3^M\mathbb Z^{729}\).

**Proof of necessity.** The smallest 3-adic entry valuation in \(B^+(H^+)^{-1}\) is exactly \(-57\): the pivot direction \(j=125\) attains it, and right multiplication by unimodular \(U\) cannot increase the fractional ideal of *all* entries. More concretely, the integral representatives \(c\equiv Ve_{125}\pmod{3^{140}}\) from the program satisfy
\[
v_3(H^+c)=112,\qquad v_3(B^+c)=55.
\]
Taking \(M=56,\ k=56\) gives \(112\ge M+k\) but \(55<M\), falsifying every uniform \(k\le56\). This is a finite, explicit algorithmic integral witness; the right-operation matrix is not assumed available by fiat.

## 251-return infinite-period certificate (conditional on pinned R762EM/EO)

For the *same* \(P\), let \(L>0\), \(3\mid L\), \(b=L/3\), \(N\ge9\), \(h\ge1\), and
\[
f(n)=\max(0,\lfloor n/3\rfloor-2),\
\Delta_n=P^{n+L}-3^bP^n,\
d(s)=[0]\Delta_s=a_{s+L}-3^b a_s.
\]
If the following **251** scalar congruences hold:
\[
\boxed{d(s)\equiv0\pmod{3^{f(\min(s,N+125))+b+h+57}},
\quad s=N,N+1,\ldots,N+250,}
\]
then for all \(n\ge N\),
\[
\boxed{3^{-f(n+L)}P^{n+L}\equiv3^{-f(n)}P^n\pmod{3^h}}
\]
as complete \(729\)-coefficient vectors.

**Derivation.** The degree-127 monic integer minimal polynomial from R762EM factors \(\mu(T)=TQ(T)\), with \(Q\) monic of degree 126 (R762EO: exactly one distinct zero eigenvalue). Thus \(P\cdot Q(P)=0\) and every \(\Delta_n\) with \(n\ge1\) has an **integral** representation in the 126 columns \(P^1,\ldots,P^{126}\). Write \(\Delta_{N+i}=B^+c^{(i)}\), \(0\le i<126\). Its return moment vector is
\[
(H^+c^{(i)})_j=d(N+i+j),\quad 0\le j<126.
\]
The 251 requested scalars cover every \(i+j\in[0,250]\), and the exponent in the hypothesis is at least \(f(N+i)+b+h+57\). The reconstruction theorem gives \(\Delta_{N+i}\in3^{f(N+i)+b+h}\mathbb Z[G]\) for all 126 base positions.

Every nonzero root of \(Q\) has \(v_3(\lambda)\ge1/3\) by the pinned R762EO spectral result. Therefore the coefficient of \(T^{126-j}\) in \(Q\) is divisible by \(3^{\lceil j/3\rceil}\). The monic recurrence \(Q(P)P^n=0\), applied to \(\Delta_n\), propagates the 126 base congruences because
\[
f(n+126)-f(n+126-j)\le\lceil j/3\rceil.
\]
Finally \(f(n+L)=f(n)+L/3\) for \(n\ge N\ge9\), so the displayed normalized vector periodicity follows.

**Scope of optimality:** 57 trits is exact for the universal *linear terminal reconstruction* implication, not a lower bound on every special actual-period instance. The 251-scalar h=7/h=8 high-precision period checks are a defined future computation, **not performed** here.

## Reproduction and evidence

Build \`g++ -O3 -std=c++17 R762FE_Q9_SHIFTED_SMITH_VERIFY.cpp -lgmpxx -lgmp -o r762fe\`. Run \`./r762fe 140\` and \`./r762fe 180\`; compare \`e\`, \`b\`, \`penalties\`, and the direct witness valuations. Code generates all 729 paths of \(P^n\) for \(1\le n\le252\), both \(H^+\) and \(B^+\), and verifies the terminal witness against unmodified original matrices. Both runs were actually performed locally, returning PASS with matching triples and witness. This is an author-side exact finite certificate, not an external reviewer or Lean check.

## Next scientific question

Evaluate the 251 high-index return congruences at h=7 or h=8 with modular fast recurrence/powering; measure preprocessing, precision, time and endpoint recovery cost against the existing 729-terminal window check. Separately, use the actual signed Cell/Link/Port incidence and V17/V29/V39 future-observer semantics to address the frozen native triadic-closure hard target.
