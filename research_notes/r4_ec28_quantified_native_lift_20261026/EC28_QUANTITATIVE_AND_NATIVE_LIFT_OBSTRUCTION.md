# R4-EC28 — Quantitative near-central BRC source gap and native-lift obstruction

**Author-side research, 2026-10-26 (Asia/Shanghai).** Status: exact mathematical derivation and finite integer cross-check; **not** native Result, independent Driver review, Working Truth or Foundation admission.

**Scope and source pins.** GLOBAL_KNOWLEDGE_V1 canonical main \`c6d252e7e402c453dd0eb291d80b0a8a7e8f6821\`, including \`00_BOOTSTRAP.md\`, \`OPERATING_MANUAL.md\`, \`projects/enterprise-math/P000_REALITY_FOUNDATION.json\` (ACTIVE_LOCKED) and ACTIVE worldview. Enterprise Math main \`a0f54b76491aedcde1405c39ad0df86a3ccda6ab\`, including \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`, \`docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md\`, \`research_persistence_policy.json\`, and BRC substrate. Predecessor proof: R4-EC27 at \`da477200d78b9f32243cfd0024b1607659c50ced\`. Authenticated GitHub actor: \`awdawmip\`. Native control tasks: \`CONTROL_QUOTA\`; session creation: \`STATIC_READONLY_SCOPE_DENIED\`, operation_sent=false. No verified active owner/CLAIM; this is a distinctly marked local-author research unit.

## 1. Mathematical object

Let \(e_{n,j}=[x^n u^j]E(x,u)\) be **positive integer counts in the auxiliary ordered-binary BRC clean-source model**:

\[
E(x,u)=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6}.
\]

Set \(F(n,j)=e_{n,j}-e_{n,j-1}\), with \(e_{n,-1}=0\). R4-EC27 proved the all-grade qualitative unimodality \(F(n,j)\ge0\) for \(n\ge10\), \(1\le j\le\lfloor n/2\rfloor\).

We independently checked its critical algebraic steps, in a non-blind author context: substitute \(x=z,\ u=t/z^2\), let \(a(t)=1+2t^2-t^3\), and define \(R(0)=1\) by \(1/R+tR=a\). Then

\[
E(z,t/z^2)=\frac{1-t}{a-z-t/z}
=\frac{(1-t)R}{(1-Rz)(1-tR/z)}.
\]

The nonnegative-\(z\)-power coefficient is therefore \([z^s]E=(1-t)R^{s+1}/(1-tR^2)\). Shifting the index in \(e_{2j+s,j-1}\) cancels the denominator and yields the exact identity

\[
\boxed{\sum_{j\ge0}F(2j+s,j)t^j=(1-t)R^{s+1}},\qquad s\ge0. \tag{1}
\]

The coefficient extraction is legitimate as a \(t\)-adic Laurent expansion with finite negative powers at each \(t\)-degree. This audit checked algebra and finite consequences; it does **not** constitute independent Driver review.

## 2. New theorem: explicit exponential separation in a near-central cone

**Theorem EC28-A.** For all integers \(j\ge5\) and \(2j\le n\le3j-3\),

\[
\boxed{e_{n,j}-e_{n,j-1}\ \ge\ (n-2j+1)\,2^{j-5}>0.} \tag{2}
\]

This is a uniform infinite-parameter quantitative bound, not merely a finite numerical observation.

**Proof.** Put \(Y=R-1-t\) and \(H=(1-t)Y\). The defining quadratic gives

\[
Y=t^4+(2t+t^3)Y+tY^2.
\]

Write \(Y=\sum_{m\ge0}y_mt^m\). Then \(y_0=\dots=y_3=0\), \(y_4=1\), and for every \(m\ge5\),

\[
y_m=2y_{m-1}+y_{m-3}+\sum_{i=0}^{m-1}y_i y_{m-1-i}\ \ge\ 2y_{m-1}.
\]

All \(y_m\) are nonnegative integers, whence \(y_{m-1}\ge2^{m-5}\) for \(m\ge5\). Thus

\[
[t^m]H=y_m-y_{m-1}\ge y_{m-1}\ge2^{m-5}\quad(m\ge5). \tag{3}
\]

For any integer \(p\ge1\), expand \(R=1+t+Y\):

\[
(1-t)R^p=(1-t)(1+t)^p+
\sum_{\ell=1}^{p}\binom p\ell(1+t)^{p-\ell}Y^{\ell-1}H. \tag{4}
\]

Each summand in the sum is coefficientwise nonnegative. If \(j\ge p+2\), the polynomial first term has no \(t^j\) coefficient; the \(\ell=1\) term contributes at least \(p[t^j]H\). Combining (1), (3), (4) gives

\[
F(2j+p-1,j)=[t^j](1-t)R^p\ge p\,2^{j-5}.
\]

Taking \(p=n-2j+1\), the conditions \(p\ge1\) and \(j\ge p+2\) are exactly \(2j\le n\le3j-3\). QED.

**Corollary EC28-A1.** Within the existing EC17 auxiliary reflection law
\(D[n,k]=C[n,n-k]-C[n,k]=e_{n-3,k-1}-e_{n-3,k-2}\), for every integer \(k\ge6\) and \(2k+1\le n\le3k-3\),

\[
\boxed{D[n,k]\ \ge\ (n-2k)\,2^{k-6}>0.} \tag{5}
\]

This bound belongs only to the same positive-count **auxiliary BRC source observer**, not to an unspecified native X6 source count.

## 3. New theorem: support/endpoint/grade transport cannot guarantee source-count shape

**Proposition EC28-B (typed lift obstruction).** In a signed native-X6 path chart, preserving the set of attainable endpoints, ordered time step count, primitive native-axis displacements, grade and concatenation under a surjective path map does not determine source multiplicity or preserve a grade-count unimodality inequality.

**Explicit construction.** Fix a Cell and the native six-axis displacement chart; do not impose a global origin. Model U has primitive transition letters \(A:+E_1\), \(B:+E_2\). Model V has distinguishable source transitions \(A_0:+E_1\), \(A_1:+E_1\), \(B:+E_2\). For paths of length \(n\), define grade \(j\) to be the number of \(B\) transitions. All untraveled native displacements \(E_3,\ldots,E_6\) are **explicitly** zero for these particular paths, not inferred from omission or proposed as a complete three-dimensional slice. Time is separately the ordered \(n\)-step trace, not a seventh spatial coordinate. No force-balance event is postulated, so P000's primitive triadic stability constraints are not altered.

The forgetful map \(\pi(A_0)=\pi(A_1)=A,\ \pi(B)=B\) is surjective, preserves ordered concatenation, grade, endpoint and trace length. In **both** models the grade-\(j\) endpoint is the same six-field displacement \((n-j,j,0,0,0,0)\), so their endpoint support agrees. But the **positive source counts** are

\[
N_U(n,j)=\binom nj,\qquad N_V(n,j)=2^{n-j}\binom nj. \tag{6}
\]

For \(n=10\),

\[
N_U(10,3)=120<210=N_U(10,4),\quad
N_V(10,3)=15360>13440=N_V(10,4). \tag{7}
\]

Hence a support-, endpoint-, grade- and step-compatible quotient can flip the sign of adjacent grade differences; the difference for V is \(-1920\). This is an **exact countermodel to an insufficient transfer criterion**, not a counterexample to EC27 or a claimed discovery about the actual native heartbeat dynamics. QED.

**Sufficient transport condition (conditional).** If a genuine native-to-auxiliary map on each grade is surjective with constant fiber size \(m_{n,j}\ge1\) for every auxiliary source path in grade \(j\), then \(N_{\mathrm{native}}(n,j)=m_{n,j}N_{\mathrm{aux}}(n,j)\). If \(m_{n,j}\) is nondecreasing across the relevant half-row, EC27 positivity and \(N_{\mathrm{aux}}\ge0\) imply the native row's adjacent differences are nonnegative. If \(m_{n,j}=m_n\) is independent of \(j\), the entire row shape and equality cases transfer up to a constant factor. **Neither fiber hypothesis has been established for P000**.

## 4. Verification and claim boundaries

An independent standard-library integer verifier calculates the quadratic-series coefficients directly (without using EC27's \(Y\)-recurrence for its primary \(R\) construction), the rational-kernel rows, the diagonal identity, the quantitative inequality and the exact U/V countermodel. Actual execution: depth \(0\le n\le120\), **3,721** diagonal coefficient comparisons and **1,138** quantitative-cone comparisons, all PASS. The smallest tested bound margin was 0 (the weak inequality is intentional). The exact U/V witness has source-count adjacent differences \(+90\) and \(-1920\).

The unbounded bound (2) follows from the displayed recurrence, coefficientwise positivity and finite algebraic identities, not from 120-depth testing. The countermodel uses elementary binomial enumeration. No Lean check, clean-blind independent Driver review, actual native three-dimensional slice mapping, validated heartbeat transition model, formal RESULT or Research Activity Guard acceptance has occurred.

**BRC reuse:** REUSE_APPLIED to EC17/EC27 positive-count source observer and EC17 reflection; COMPOSE_APPLIED to a quantitative lower bound; typed provenance/multiplicity observer explicitly retained in the lift no-go. No signed amplitudes, gamma positivity assumption, external trigonometric rotation or physical source measurements are inserted.

## 5. Next specific unit: EC29

Construct or refute a **typed native X6 path-to-BRC source map** specifying: (i) legitimate three-dimensional layer selection/embedding in all six native axes; (ii) semantics of the third slice coordinate and any other hidden relation state; (iii) exact primitive and composite update law and ordered independent time; (iv) observer to auxiliary \(n,j\), clean-source event and provenance; (v) forward-operation commutation and grade-by-grade multiplicity/fiber theorem. Test the map first on \(n=2,3\) with actual native transitions, using EC28-B's countermodel as an adversarial fiber check. Without these interfaces, leave native transport explicitly **UNPROVED**, regardless of auxiliary E unimodality or quantitative gaps.

**Publication target:** this independent research note and its exact verifier/report, not a formal CLAIM or Result.