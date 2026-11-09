# PREFIX-631-R6 — Uniform signed-BRC variance-gradient reversal and interior valley

Date: 2026-11-09 (Asia/Shanghai).
Researcher-ID: EM-DIRECT-002083 / TASK_RESEARCH.
Research-Activity-ID: RA-18623CB7378E739729E2025A.
Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen science pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.

## Question and exact model

Continue PREFIX-630: what happens to the native-action stopping-time variance gradient beyond the proved decreasing region? Preserve the first-passage statistical observer from PREFIX-621, with two signed informative directions, informative probabilities p_i/q and (1-p_i)/q, the confidence-diameter rule beta=1/40, width 1/4 and first possible direction stop at 25, forced at 189. The full 96-port BRC graph is a frozen scientific dependency, not a newly executed experiment.

Write V_q(p_1,p_2)=Var(T_q). The native choices are q=12 (slot 0) or q=24 (slots 1/2); the moment formulas also define real q>=12. Reduce signs by symmetry to the parameter square [0,1/2]^2.

## Theorem: every parameter slice in a rational bracket has a variance valley

For **every** real p_2 in [37/256,39/256] and every real q>=12,

\[
\boxed{\partial_1 V_q(3/20,p_2)<0,\qquad \partial_1 V_q(1/6,p_2)>0.}
\]

Consequently for each such (q,p_2), the continuous function p_1 -> V_q(p_1,p_2) **attains a local minimum at some interior point** c in (3/20,1/6). At least one critical point exists there. Uniqueness and the location of a global maximum are separate questions.

This is a genuine reversal of the gradient sign; PREFIX-630 proved a negative gradient at p_1=1/8, while the new result proves a positive gradient at p_1=1/6, uniformly across the entire stated p_2 interval. The new statement does not assume the older fixed Bernstein envelope is an exact gradient.

## Proof and executable certificate

Let A[n,k] be the exact surviving-prefix word counts from the PREFIX-621 dyadic rule (D=2^18), and for n=0,...,188 define
\[
s_n(p)=\sum_{k=0}^n A[n,k]p^k(1-p)^{n-k}.
\]
The accompanying standard-library certificate reconstructs these counts; checks first stop 25, zero survivors at 189, and s_25(p)=1-p^{25}-(1-p)^{25}.

Set w(n,m)=C(n+m,n)/2^{n+m+1}, z(n,m)=(n+m+1)w(n,m)/2, and sum n,m=0,...,188. The independent Poisson-clock laws (PREFIX-622) give
\[
\mu=\sum_ns_n(p_1)+\sum_ms_m(p_2)-\sum_{n,m}w(n,m)s_n(p_1)s_m(p_2),
\]
\[
H=\sum_n(n+1)s_n(p_1)+\sum_m(m+1)s_m(p_2)-\sum_{n,m}z(n,m)s_n(p_1)s_m(p_2).
\]
Write U=partial_1 mu, J=partial_1 H and W_1=2(J-mu U). The exact native-action variance derivative is
\[
\frac{\partial_1 V_q}{q^2}= W_1-\frac{U}{q}.
\]
For each fixed p_1 in {3/20,1/6}, \mu,U,J are polynomials in p_2 of degree at most 188; W_1 is degree at most 376. Substitute p_2=(37+2t)/256, 0<=t<=1, and represent the resulting polynomials in the degree-376 Bernstein basis. Every basis function is nonnegative and their sum is one.

The certificate computes all **377 exact rational Bernstein coefficients** for W_1, U and W_1-U/12, by exact power-to-Bernstein conversion, the product identity
\[
B_{i,d}(t)B_{j,d}(t)=\frac{\binom di\binom dj}{\binom{2d}{i+j}}B_{i+j,2d}(t),
\]
and exact degree elevation. The complete coefficient checks give:

* At p_1=3/20: all coefficients of W_1 are **strictly negative**, and all coefficients of U are **strictly positive**.
* At p_1=1/6: all coefficients of W_1-U/12 and U are **strictly positive**.

Thus at 3/20, W_1-U/q<0 for all q>=12; at 1/6, W_1-U/q >= W_1-U/12>0. Polynomial differentiability and the extreme-value theorem show an interior minimum on each closed [3/20,1/6] slice, since neither endpoint can minimize in the presence of these one-sided derivative signs. This proves the theorem.

## Executed verification

Command: \`python PREFIX631_R6_uniform_gradient_reversal_certificate.py\`.
Local result: \`ALL_CHECKS_PASS [('3/20', 'NEGATIVE'), ('1/6', 'POSITIVE')]\`.
Two sets of 377 complete rational coefficient checks (no sample-grid interpolation). The script also independently recomputes both endpoint moments and checks equality with the first/last Bernstein coefficients.

Numerical display only (exact inequalities decided by Fraction arithmetic):
- p_1=3/20: maximum coefficient of W_1-U/12 approximately -226.730572975; minimum approximately -658.316327638.
- p_1=1/6: minimum coefficient of W_1-U/12 approximately +32.354010366; maximum approximately +352.877116977.
- Every U coefficient in both cases is positive.

The proven claim is confined to the frozen signed-observer **statistical sampling model**, not a new 96-port native graph execution. The research is author-proved and rationally checked, pending independent review.

## Next distinguishing question

Use the same exact rational Bernstein engine to locate and classify the full set of stationary points in (3/20,1/6) for p_2 in [37/256,39/256], and separately connect the earlier negative-gradient region 1/14<=p_1<=1/8 with a uniform exact certificate. Compare candidate interior valleys with edge maxima only after the required global bounds are established.

The real session and activity above are Source-registered. This independent mathematical note is not a formal CLAIM, Result or Review for the separately dispatched RS-X6-NATIVE-ROTATION-DYNAMICS task.
