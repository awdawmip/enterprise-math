# R749STF — Minimal one-bit future-observer repair and rational noise bounds

Date: 2026-11-17. Status: AUTHOR_EXACT_NOT_REVIEWED. This is independent portable mathematical research on the frozen five-labeled-source auxiliary scalar model at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. It is **not** a native X6/BRC Cell/Link/Port theorem, shared Task Result, Review, or P000 change.

## Model and pinned premise

For weights (1,1,2,3,6), the five coordinates remain distinctly labeled and the first unit-weight coordinate is marked. Put

\[
\Omega_n=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le n-1\},\qquad
C_n=|\Omega_n|,\qquad T_n=\sum_{k\in\Omega_n} k_1.
\]

Set \(S(n)=18n^4+54n^3-345n^2+2070n-16315\) and
\[
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108},\qquad
\mathcal O_n^{(m)}(e,d)=(Y_{n+6j}(e,d))_{j=0}^{m-1}.
\]
Each candidate uses the same error pair in \([-2,2]^2\) throughout its observations, with distinct pairs allowed for distinct cutoffs.

**Pinned, load-bearing predecessor:** R749STB at [PR #2616, commit d2a4436f](https://github.com/awdawmip/enterprise-math/blob/d2a4436f4ed42aba25a54f9b7015e4c4a776c944/research_notes/portable_direct/2026-11-17_R749STB_STABLE_THREE_READ_COLLISION_CURVE.md) previously author-certified that for each real \(e\in I=[-151/100,-149/100]\), there is a legal analytic pair of states
\[
s_0(e)=(73,e,d(e)),\qquad s_1(e)=(77,E(e),D(e))
\]
with identical first three scalar observations \(y(e)\), and the **strict uniform fourth-read gap**
\[
\tag{STB}
Y_{95}(E(e),D(e))-Y_{91}(e,d(e))>1/100000.
\]
The new proof uses this earlier theorem as a dependency; the current arithmetic checker does not rerun R749STB's 199-coefficient Bernstein certificate. Its independent review remains pending.

## Theorem A — Exact minimal sufficient augmentation on the collision sheet

Restrict the state set to the union of these two paired analytic branches. From the three-read prefix alone, the minimum additional discrete alphabet needed to recover **all** future scalar observations has size exactly **two**, i.e. one bit.

*Necessity:* For every \(e\in I\), both states have the same \(y(e)\), while their fourth readouts differ strictly by more than \(10^{-5}\). For any predictor \(r(y)\), the triangle inequality gives
\[
\max\{|r(y(e))-Y_{91}(e,d(e))|,\,
|r(y(e))-Y_{95}(E(e),D(e))|\}>1/200000.
\]
This also applies to the larger of the two *expected* absolute losses under any randomized forecast. Hence a zero-extra-bit observer cannot forecast the fourth read with uniform error at most \(5\cdot10^{-6}\), even on exact prefixes.

*Sufficiency:* Save \(b=0\) for \(q=73\) and \(b=1\) for \(q=77\). Given the first two readouts \(y_0,y_1\), let \(n_i=q+6i\), \(X_i=(y_i+S(n_i)/108)/n_i^3\), and \(V_i=C_{n_i}X_i-T_{n_i}\). The two equations \(e-X_i d=V_i\) invert exactly:
\[
\boxed{d=\frac{V_0-V_1}{X_1-X_0},\qquad e=V_0+X_0d.}
\]
The denominator is uniformly \(>1\) for both cutoff classes throughout \([-2,2]^2\), as shown below. Thus the bit plus prefix recovers the unique parameter pair and every \(Y_{q+6j}\) for **all integers \(j\ge0\)**. First-two-read injectivity within each known cutoff ensures each restricted prefix has exactly two states, one from each branch. One bit is necessary and sufficient.

This one-bit tag records *cutoff identity* on a specific auxiliary observer fiber. It is not asserted to be a native spatial axis or a genuine X6 signed-Port/source identifier. A native lifting theorem still needs a separately verified embedding and future-operation preservation.

## Theorem B — Exact finite-noise stable inversion

Let the bit be correct, and \(|z_i-y_i|\le\eta\) for the first two scalar reads, with \(0\le\eta\le10^{-8}\). Apply the same inverse to \(z_0,z_1\), obtaining \((\tilde e,\tilde d)\); clip each coordinate to \([-2,2]\) to get \((\hat e,\hat d)\).

The exact labeled-source count recurrence gives
\[
(C_{73},T_{73})=(707343,8931013),\quad
(C_{79},T_{79})=(1020943,13914446),
\]
\[
(C_{77},T_{77})=(906087,12046216),\quad
(C_{83},T_{83})=(1285543,18379893).
\]
For \(q\in\{73,77\}\), let \(C_0=C_q,C_1=C_{q+6}\) and similarly for \(T\). The normalized gap has identity
\[
(C_0+d)(C_1+d)(X_1-X_0)
=T_1C_0-T_0C_1+d(T_1-T_0)+e(C_0-C_1).
\]
Its numerator is bounded below by the same expression at \(d=-2,e=2\), while its denominator is at most \((C_0+2)(C_1+2)\). Therefore, for *all* allowed \(e,d\),
\[
X_1-X_0\ge
\begin{cases}
724220177653/722160341025>1,&q=73,\\
1167840027137/1164818183505>1,&q=77.
\end{cases}
\]
The exact positive integer margins are 2059836628 and 3021843632.

Put \(\rho=\eta/q^3\le1/4\), \(K_d=2(C_q+C_{q+6}+4)\),
\(M_n=(T_n+2)/(C_n-2)\), and
\(K_e=C_q+2+(M_q+1/4)K_d\).
Since \(|\tilde X_i-X_i|\le\rho\), the noisy normalized gap is at least \(1-2\rho\ge1/2\). Subtraction of the two inverse equations gives
\[
|\hat d-d|\le K_d\rho,\qquad
|\hat e-e|\le K_e\rho.
\]
For \(n=q+6j\), the exact rational-fraction difference formula and coordinate clipping imply
\[
\boxed{|Y_n(\hat e,\hat d)-Y_n(e,d)|\le A_{q,j}\eta,\quad
A_{q,j}=\frac{n^3}{q^3(C_n-2)}(K_e+M_nK_d).}
\]
The reproducible exact checker proves \(A_{73,3}<98\) and \(A_{77,3}<103\). Therefore, at the **fourth read**, the bit-conditioned forecast error is at most \(103\eta\) (strictly less when \(\eta>0\)), and in particular \(<1.03\cdot10^{-6}\) when \(\eta\le10^{-8}\). In contrast, without the bit even an *exact* common prefix has minimax fourth-read error \(>5\cdot10^{-6}\).

There is also a uniform bound for **all future scalar reads**, with no horizon restriction:
\[
\boxed{\sup_{j\ge0}|Y_{q+6j}(\hat e,\hat d)-Y_{q+6j}(e,d)|\le66000\eta.}
\]
Indeed, for \(n\ge73\) the integer Cartesian box \(0\le k_i\le\lfloor(n-1)/(5w_i)\rfloor\) lies in \(\Omega_n\), giving \(C_n\ge(n-1)^5/112500\), hence \(C_n-2\ge(n-1)^5/225000\). Moreover \(T_n\le(n-1)C_n\), so \(M_n<2n\). Since \(n/(n-1)\le73/72\), one obtains
\[
A_{q,j}\le
\underbrace{\frac{225000(73/72)^5}{q^3}\left(\frac{K_e}{q^2}+\frac{2K_d}q\right)}_{U_q<66000}
\]
for every \(j\ge0\). Both \(U_q<66000\) are certified as exact rational inequalities by the companion code, not inferred from finite sampling.

## Evidence, scope, next frontier

The standard-library-only program R749STF_BINARY_REPAIR_CERT.py regenerates the five-source integer generating-function coefficients; verifies the integer counts, both global determinant margins, both exact inverse-conditioning factors, the fourth-step factors and two all-horizon factors; then emits R749STF_BINARY_REPAIR_RESULTS.json. It is an exact arithmetic certificate for **the new corollaries** and does not independently prove STB's analytic collision existence or perform a native X6/BRC calculation. All mathematics is author-side, not independently reviewed or promoted.

Next useful problems: find a five-read exact collision to improve the global bound \(5\le m_*\le11\); construct a sharper robust inter-cutoff gap for (602,604); or lift the tagged binary carrier to an actual source-preserving BRC Port/Cell interface with explicit allowed future operations.