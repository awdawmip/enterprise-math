# R151 — Clock-gauge obstruction to pointwise reconstruction from full CRT lag covariance

Date: 2026-11-14 (Asia/Shanghai).  
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged).  
Scope: external tied-phase scalar S23 finite Sturmian-word observer, with joint CRT relations retained.  
Mathematical status: author-side exact proof; independent review NOT_REVIEWED.  
Inputs: R146 exact phase-fiber formula, enterprise-math commit b02b0c242b274bc6a82111dbd3600126a2867319; R150 lag inverse, commit 5752b49863398032e72b4b7ebeccc81ff4722401. This is separate from a formally claimed Task and does not alter P000/native X6.

## 1. Definitions

For a binary word \(w\) of length \(m\), put \(s_0=0\) and \(s_j=\sum_{0\le i<j}w_i\). Its open free-intercept slope interval has endpoints

\[
\alpha=\max\left(0,\max_{0\le i<j\le m}\frac{s_j-s_i-1}{j-i}\right),\qquad
\beta=\min\left(1,\min_{0\le i<j\le m}\frac{s_j-s_i+1}{j-i}\right).
\]

For \(\alpha<\beta\), write \(\alpha=a/b,\ \beta=c/d\) reduced and define the *absolute intercept cuts*

\[
U=\min_{0\le j\le m}[b(s_j+1)-ja],\qquad
V=\max_{0\le j\le m}[ds_j-jc].
\]

R146 gives, for \(K=L+1\ge2\), the exact number of floor-phase labels \(N=\lfloor L\theta\rfloor\) realizing \(w\):

\[
\boxed{C_w(L+1)=\left\lceil\frac{Lc-V}{d}\right\rceil-
\left\lfloor\frac{La-U}{b}\right\rfloor-1.}\tag{1}
\]

Let \(g=\gcd(b,d)\) and \(q=(g-1)/2\). R150's *mixed* lower/upper endpoint covariance, retaining the joint CRT clock, is

\[
A_j=((aj-U)\bmod g)-q,\quad B_j=((-cj+V)\bmod g)-q,\quad
\Gamma_w(h)=\frac1{gbd}\sum_{j=0}^{g-1}A_jB_{j+h}.\tag{2}
\]

All indices are modulo \(g\); residues are least nonnegative.

## 2. R151.1: exact common-clock gauge symmetry

**Theorem.** Fix \(n,m\ge1\), \(g=\gcd(n,m)\) and integers \(s,t,u,v\) with \(\gcd(s,n)=\gcd(t,m)=1\). Write

\[
F_{u,v}(h)=\frac1{gnm}\sum_{j=0}^{g-1}
\left(((sj+u)\bmod g)-q\right)
\left(((t(j+h)+v)\bmod g)-q\right).
\]

For every \(r,h\in\mathbb Z\),

\[
\boxed{F_{u+sr,v+tr}(h)=F_{u,v}(h).}\tag{3}
\]

**Proof.** Under the simultaneous shift of offsets, the two centered signals become the former signals at \(j+r\) and \(j+r+h\). Reindex by \(j'=j+r\) in the complete sum over \(\mathbb Z/g\mathbb Z\). This proves (3), including \(g=1\), where the covariance is zero. QED.

Thus the entire correlation waveform is invariant under common clock-origin translation. R150's inverse recovers the second signal only once the first signal's alignment \(u\) (equivalently its reference clock) has been retained.

## 3. R151.2: actual Sturmian counterexample and infinite discrepancy

Consider the two length-five words

\[
\boxed{w_A=01001,\qquad w_B=10010.}\tag{4}
\]

Their prefix-sum sequences are respectively \((0,0,1,1,1,2)\) and \((0,1,1,1,2,2)\). Direct substitution into the endpoint and intercept formulas gives

| quantity | \(w_A\) | \(w_B\) |
|---|---:|---:|
| \(\alpha,\beta\) | \(1/4,1/2\) | \(1/4,1/2\) |
| \(a,b;c,d\) | \(1,4;1,2\) | \(1,4;1,2\) |
| \(U,V\) | \(3,0\) | \(4,1\) |

For both, \(g=2\), the first signal uses \((n,s,u)=(4,1,-U)\) and the second \((m,t,v)=(2,-1,V)\). Since \((-4,1)\equiv(-3+1,0-1)\pmod 2\), equation (3) applies with \(r=1\). Directly evaluating (2) yields the *identical complete mixed-lag waveform*

\[
\boxed{(\Gamma_A(0),\Gamma_A(1))=(\Gamma_B(0),\Gamma_B(1))
=(-1/32,\ 1/32).}\tag{5}
\]

However, the exact pointwise phase-fiber counts from (1) are

\[
C_A(L+1)=\left\lceil L/2\right\rceil-
\left\lfloor (L-3)/4\right\rfloor-1,\tag{6}
\]
\[
C_B(L+1)=\left\lceil (L-1)/2\right\rceil-
\left\lfloor (L-4)/4\right\rfloor-1.\tag{7}
\]

Write \(L=4q+r\), \(0\le r<4\). For residues \(r=0,1,2,3\), their ordered pairs of counts are respectively \((q,q),(q+1,q),(q+1,q+1),(q+1,q+1)\). The \(r=0\) case begins at \(q=1\), because \(L\ge1\). Therefore

\[
\boxed{C_A(L+1)-C_B(L+1)=
\begin{cases}1,&L\equiv1\pmod4,\\0,&\text{otherwise},\end{cases}
\quad L\ge1.}\tag{8}
\]

At \(K=2\), corresponding to \(L=1\), **\(C_A(2)=1\)** but **\(C_B(2)=0\)**: the first word is realized, and the second is absent. As an explicit original-floor witness, \(\theta=67/200\) gives the five increments of the original observer equal to \(01001\). For \(K=4q+2\), the multiplicities disagree by one for every \(q\ge0\), arbitrarily far into the coefficient range.

**Corollary (nonfactorization).** No function of \((m,K,\alpha,\beta,\Gamma_w(0),\ldots,\Gamma_w(g-1))\) equals \(C_w(K)\) for all finite Sturmian words and all \(K\ge2\). Even the binary presence predicate \(C_w(K)>0\) is not a function of these data: (4) has identical inputs at \(m=5,K=2\) and distinct outputs. This disproves the proposed reduction of *pointwise phase-fiber presence* to complete mixed CRT covariance plus slope support. It does not contradict R150's inverse given the separately known first-clock alignment.

## 4. R151.3: certified sufficient repair coordinate

The full pair of absolute intercept cuts \((U,V)\), together with the reduced slope endpoints, is sufficient to recover \(C_w(K)\) for every \(K\ge2\) by (1). At one fixed \(L\), the two integer cuts

\[
N_{\rm low}=\left\lfloor(La-U)/b\right\rfloor,\quad
N_{\rm high}=\left\lceil(Lc-V)/d\right\rceil
\]

are sufficient, because \(C_w(K)=N_{\rm high}-N_{\rm low}-1\), with presence exactly when \(N_{\rm high}-N_{\rm low}\ge2\). This is an exact observer-scoped factorization; no uniqueness or global minimality of the repair encoding is asserted. If a downstream operation asks whether a *specific* integer phase fiber survives, retain the underlying phase label and cut data instead of replacing them by a time-averaged covariance.

For this external scalar observer, the distinction is an exact instance of the project's joint-relation/residual-fidelity principle: full relative lag correlations can preserve coupling while forgetting an absolute phase-origin datum relevant to a different observer. P000's native X6 axioms are unchanged.

## 5. Validation, source, and next unit

The companion self-contained Python program **R151_check.py** uses only exact integers and fractions. It exhaustively checks (3) for \(g=1,\ldots,8\), all units, offsets and common shifts: **3,437** configurations and **23,777** shifted covariance comparisons. Exhaustive enumeration of finite Sturmian words of lengths \(1,\ldots,5\) detects the first same-support/full-wave/different-\(C(2)\) collision at length five (52 word records inspected); the code stops at this first collision. It checks (8) at 83 coefficients, including \(10^{100}+1\), and independently reconstructs the original rational floor-event partition for \(L=1,\ldots,48\), checking both words in 96 cases. All checks passed with marker **R151_CRT_GAUGE_POINTWISE_NONFACTOR_PASS**; see **R151_verification.json** for the exact report. The algebraic proofs establish their universal and infinite-scope statements; finite tests cross-check the implementation and boundary convention.

**Next question:** classify all same-slope-support/full-waveform gauge orbits within length-\(m\) Sturmian words and determine the smallest pointwise cut/alignment record that suffices for every \(K\). Use the repaired phase observer to study the unresolved all-length saturation threshold \(T(m)=(m-2)\lfloor(m-1)/2\rfloor+1\) for \(m\ge5\), preserving the original frozen science pin and any relevant provenance.