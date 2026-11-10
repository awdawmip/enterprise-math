# PREFIX-683-R6 — Strictly increasing, strictly concave large-slot BRC variance crossover

Date: 2026-11-11 (Asia/Shanghai). Scope: independent TASK_RESEARCH author-side increment. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Precise frozen input and dependency

Use exactly the 189-level survivor observer model from PREFIX-682 at enterprise-math commit d437f76a2d52b617e938130c9cb9e8e61257c5a9, whose proof and Fraction checker certify a local simple pole and a unique large-q variance crossover. Let Y(p,z) be the maximum of the two independent Poissonized first-stop clocks, and set

\[
A(z)=\operatorname{Var}(Y(z,z))-\operatorname{Var}(Y(0,z)),
\quad B(z)=\mathbb{E}Y(z,z)-\mathbb{E}Y(0,z).
\]

Writing \(V_q(p,z)=q^2\operatorname{Var}(Y(p,z))-q\mathbb{E}Y(p,z)\), the diagonal-minus-edge difference is \(q[qA(z)-B(z)]\). On \(I=[0.0532600,0.0532610]\), PREFIX-682 has already certified for every real z in I:

\[
-1800<A'(z)<-1600,\quad 100<B'(z)<150,\quad
793/100<B(z)<794/100.
\]

For each real \(q\ge10000\), it established a unique \(z(q)\in I\) satisfying \(qA(z(q))=B(z(q))\), and \(z(q)<z_A\), with \(A(z_A)=0\).

## New theorem

For **all real \(q\ge10000\)**, the unique crossover branch \(z(q)\) is smooth, strictly increasing, and **strictly concave**. Moreover,

\[
\boxed{\frac{793}{100q(1800q+150)}<z'(q)
<\frac{794}{100q(1600q+100)}}.
\]

An explicit *strict curvature estimate* holds:

\[
\boxed{z''(q)<-\frac{3145\cdot793}{100q(1800q+150)^2}<0.}
\]

For any two real slots \(10000\le q_1<q_2\), one obtains the fully explicit interval propagation certificate

\[
\boxed{
\frac{793(q_2-q_1)}{100q_2(1800q_2+150)}
<z(q_2)-z(q_1)<
\frac{794(q_2-q_1)}{100q_1(1600q_1+100)}.
}
\]

This yields certified order and sensitivity information for a continuum of large slot parameters using the existing BRC observer carrier.

## Proof

**1. Second derivative budget.** At c=0.0532605, the unchanged PREFIX-682 exact jet floors are floor(10^8 A''(c))=-6657264578649 and floor(10^8 B''(c))=-99474141353. Therefore \(|A''(c)|<66573\) and \(|B''(c)|<995\). PREFIX-682's certified third derivative majorants on the relevant domain are

\[
|A'''|\le218571424275456,\qquad |B'''|\le69527880576.
\]

As \(|z-c|\le1/2000000\) on I, the mean-value theorem gives

\[
|A''(z)|<66573+218571424275456/2000000<110000000=:M_A,
\]
\[
|B''(z)|<995+69527880576/2000000<36000=:M_B.
\]

**2. Smoothness and first-derivative bounds.** Put \(T(q)=q[-A'(z(q))]+B'(z(q))\). Then \(1600q+100<T(q)<1800q+150\), so \(F_z=-T\ne0\) for \(F(q,z)=qA(z)-B(z)\). The implicit function theorem and uniqueness join the local solutions into one smooth branch. Differentiation of \(F(q,z(q))=0\) gives

\[
z'(q)=\frac{A(z(q))}{T(q)}=\frac{B(z(q))}{qT(q)}>0,
\]

establishing the rational enclosure.

**3. Uniform strict concavity.** Twice differentiating \(F(q,z(q))=0\) gives

\[
T(q)z''(q)=2A'(z(q))z'(q)+[qA''(z(q))-B''(z(q))]z'(q)^2.
\]

Using the bounds from Steps 1–2, for all real q>=10000,

\[
\begin{aligned}
|qA''-B''|z'
&<\frac{794}{100}\frac{M_A+M_B/q}{1600q+100}\\
&\le\frac{794}{100}
\frac{110000000+36000/10000}{1600(10000)+100}\\
&=\frac{109175003573}{2000012500}<55.
\end{aligned}
\]

As \(2A'<-3200\) and \(z'>0\), the numerator of \(Tz''\) is strictly less than \((-3200+55)z'=-3145z'\). Since \(T<1800q+150\), and \(z'>793/[100q(1800q+150)]\),

\[
z''<-\frac{3145z'}{1800q+150}
<-\frac{3145\cdot793}{100q(1800q+150)^2}<0.
\]

No numerical sign sampling or assumption about the signs of A'' and B'' enters this proof.

**4. Interval propagation.** Strict concavity gives decreasing z'. For q1<q2, the mean value theorem implies \((q2-q1)z'(q2)<z(q2)-z(q1)<(q2-q1)z'(q1)\). Inserting Step 2's rational envelopes proves the last assertion.

## Validation, provenance and next discriminating question

Accompanying Python checker PREFIX683_R6_CONCAVITY_CERTIFICATE.py (standard-library Fraction only) independently verifies the *new rational implications* of the already-published PREFIX-682 derivative/jet certificate. Actual arithmetic check result: NEW_RATIONAL_BOUND_CHECKS_PASS. The 189-level survivor recurrence and its exact prior jet calculation are reused at their immutable commit, and were not recomputed in this run. The displayed calculus identities supply the mathematical proof; this program tests its load-bearing rational inequalities. Status: AUTHOR_DERIVED / EXACT_RATIONAL_BOUND_CHECKED / UNREVIEWED / NOT_ADMITTED.

Reusable method: propagate a uniquely pinned BRC-observer crossover through slots by an implicit derivative and curvature envelope; BRC reuse status REUSE_APPLIED. Next precise open question: certify the signs of F'_q=qA'-B' on [0.053,0.0532600] with locally signed Bernstein coefficients, connecting the q>=18 existence interval to the q>=10000 unique branch. In parallel, use PREFIX-675's certified complete edge maximum to prune the ordered two-dimensional triangle 0<=p<=z<=1/2. Both preserve the frozen scientific pin and the separation from native Heartbeat/P000 semantics.