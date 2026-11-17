# R246 — Exact interior worst case for the two-Perron-mode scalar observer

Date: 2026-11-17 (Asia/Shanghai). Evidence: AUTHOR_PROVED / EXACT_RATIONAL_COMPUTATION_EXECUTED / NOT_REVIEWED. Native BRC EffectHistogram: NOT_EXECUTED. Formal Task CLAIM / Result / Review: NONE.

## Frozen scientific basis

Portable continuation of R245 at commit 9d4d1c25b3b3b267b1b99b4646a94ec9583afe45. Original science is frozen at 43ec6098b1330ae86d0a7863be336c5d97f6ef34. No scientific input was rebased.

Retain the derived seven-source reversible sticky-reset family on 39/100 < s < 41/100, with continuous endpoint extension. Define

\[
\alpha=(1/5,1/4,3/10,9/20,s,2/3,t(s)),\quad
t(s)=\frac{1691s-2615}{2615s-3539},
\]
\[
b_0=13/60,\quad b_j=(5/18)|1/2-\alpha_j|,\quad
\pi_j=b_j/(1-\alpha_j),\quad Z=\sum_j b_j/(1-\alpha_j)^2,\quad
\rho_j=b_j/((1-\alpha_j)^2Z).
\]

The transition is \(P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j\).
For every proper subset \(U\subsetneq\{1,\dots,6\}\), let \(D_U=\{0\}\cup U\) and

\[
\Phi_n(s)=\sum_{U\subsetneq[6]}W_{|U|}\rho_{D_U}^TP_{D_U}^{n-1}{\bf1},
\quad W=(144,576,1440,4320,17280,86400,518400).
\]

The dominant Perron mode of mask 59 has eigenvalue/amplitude \((r,A)\); mask 55 has \((\beta,B)\). Define \(X_n=A r^{n-1}+B\beta^{n-1}\) and \(E_n^{[2]}=\Phi_n/X_n-1\). R245 proves \(E_n^{[2]}>0\) and strict decrease in \(n\ge2\).

## Theorem 1 — The error is not monotone in the parameter

The exact strict inequalities at the single integer time \(n=126\) are

\[
\boxed{
E_{126}^{[2]}(2/5)>E_{126}^{[2]}(39/100),\qquad
E_{126}^{[2]}(2/5)>E_{126}^{[2]}(41/100).}
\]

Both endpoints above are continuous extensions. By continuity the same comparison holds against some interior points near either endpoint. Hence the function \(s\mapsto E_{126}^{[2]}(s)\) on the open interval is neither nondecreasing nor nonincreasing. The continuous extension attains a global maximum at some interior \(s\); this result does not locate that maximizer.

| Parameter | Approximate relative error (diagnostic only) |
|---|---:|
| 39/100, endpoint extension | 0.1359716517392619 |
| 2/5 | 0.1361763657846810 |
| 41/100, endpoint extension | 0.1359522599118395 |

### Exact certificate

For each of the three rational parameters, clear common denominators in the 7-by-7 transition and stationary distribution. Propagate all 63 killed blocks as exact integer matrices through 125 updates to obtain each \(\Phi_{126}\) as a rational number.

For masks 59 and 55, use 96 exact dyadic bisections of the decreasing secular equation to obtain rational lower and upper Perron-root bounds. For any mask \(D\), the Perron amplitude as a function of its root \(x\) is

\[
C_D(x)=\frac{W_{|D|-1}}Z\,
\frac{(\sum_{i\in D}b_i/((1-\alpha_i)(x-\alpha_i)))^2}
{\sum_{i\in D}b_i/(x-\alpha_i)^2}.
\]

The two positive sums in this quotient decrease for \(x>\max\alpha_i\); evaluating them separately at the root-bracket endpoints gives valid rational lower and upper amplitude bounds. Combining root and amplitude bounds yields \(X_{\rm lo}(s)<X_{126}(s)<X_{\rm hi}(s)\).

The checker proves, for each endpoint \(e=39/100,41/100\),

\[
\Phi_{126}(2/5)X_{\rm lo}(e)-\Phi_{126}(e)X_{\rm hi}(2/5)>0.
\]

The certified margin hashes are, respectively, edfb6bc0dff0c6812164223cf8e52558c839541457a6b3838a3f90fd5f479550 and 51a37c7bbfac33e8a3e10508cdd20ce6948308397bbb0585613882ba40cdffe2. These hashes identify the exact positive rational margins, whose actual integer signs (not rounded decimals) are verified by the executable program.

## Theorem 2 — An exact first-crossing tolerance has an interior worst case

Set \(\delta=17/125=0.136\), and let

\[
N_{\delta}(s)=\min\{n\ge2:E_n^{[2]}(s)<\delta\}.
\]

Then

\[
\boxed{N_{\delta}(39/100)=126,\qquad
N_{\delta}(2/5)=127,\qquad N_{\delta}(41/100)=126.}
\]

Six independent strict rational comparisons verify \(E_{125}>\delta>E_{126}\) at both endpoint extensions and \(E_{126}>\delta>E_{127}\) at the midpoint. R245's strict decrease in event time proves these are the first crossings. By continuity, parameters just inside both ends have \(N_\delta=126\), whereas the interior parameter \(2/5\) needs event 127. Thus an endpoint-only maximization principle for arbitrary tolerances is disproved in this model.

These inequalities do not determine the optimal parameter-uniform thresholds for the specific 1% and 0.1% tolerances, which remain between the previously established bounds.

## Lemma 3 — Exact rank-one integer recurrence

For each killed block and \(v_i^{(0)}=1\), the original transition has the rank-one update

\[
v_i^{(k+1)}=\alpha_i v_i^{(k)}+(1-\alpha_i)\tau_k,\qquad
\tau_k=\sum_{j\in D}\pi_jv_j^{(k)}.
\]

At rational parameters, let \(C\) be the LCM of denominators of all \(\alpha_i\), \(Q\) the LCM for all \(\pi_j\), \(d=CQ\), \(h_i=d\alpha_i\), \(u_i=C(1-\alpha_i)\), and \(w_j=Q\pi_j\). These are integers and the exact scaled recurrence is

\[
z_i^{(k+1)}=h_i z_i^{(k)}+u_i\sum_{j\in D}w_jz_j^{(k)},
\qquad v_i^{(k)}=z_i^{(k)}/d^k.
\]

The 63 proper masks satisfy \(\sum_D|D|=249\) and \(\sum_D|D|^2=1071\). The straightforward dot-and-update implementation uses at most \(3(249)=747\) scalar integer multiplications per event iteration, against 1071 for dense multiplication. Arithmetic-operation count improves from \(O(n\sum_D|D|^2)\) to \(O(n\sum_D|D|)\) after parameter preparation. Exact equality of the dense and rank-one \(\Phi_{126}\) calculations was executed for all three anchors. The bit-complexity and practical runtime comparison remain to be measured.

## Reproduction and evidence

Run the Python 3 standard-library file R246_exact_nonmonotone_parameter_certificate.py in this directory; it writes the full exact rational comparison certificate as JSON to standard output. The companion R246_verification.json stores the checked summary, 96-bisection root enclosures, two cross-product margin digests, six tolerance margin digests and validation scope. All final comparisons use Fraction and arbitrary-precision integers, with a PASS result; floating-point displays are diagnostic.

**Next actionable research:** Seek a certified parameter-wide sign/threshold argument at event counts 270 and 403 (or a counterexample), using the exact rank-one propagation and tangent derivatives together with rational Perron root/amplitude bounds. Separately measure full bit cost versus the 230-order recurrence and 256-state direct propagation.

This analysis concerns an auxiliary positive scalar observer. P000, the ACTIVE X6 heartbeat worldview, and joint relation preservation remain intact. No native signed/port/source/branch/multiplicity/cross-moment state has been collapsed or claimed to be reconstructed by this scalar quantity.
