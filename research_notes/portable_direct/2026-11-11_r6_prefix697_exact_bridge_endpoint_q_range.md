# PREFIX-697-R6 — Exact BRC bridge endpoints and the complete integer crossing band

Date: 2026-11-11 (Asia/Shanghai). Frozen scientific input: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: **AUTHOR_RECOMPUTED / EXACT_189_ROW_ZERO_JET + EXACT_FRACTION_IMPLICATION / UNREVIEWED / NOT_ADMITTED**. Independent research note; no shared Task CLAIM, formal Result or Driver Review is asserted.

## The question and precise domain

PREFIX-696 proved on the auxiliary observer interval

\[
J=[L,R]=[1321/25000,1329/25000]=[0.05284,0.05316]
\]

that \(A(z)=\mathrm{Var}(Y(z,z))-\mathrm{Var}(Y(0,z))>0\), \(B(z)=E[Y(z,z)]-E[Y(0,z)]>0\), and \(Q(z)=B(z)/A(z)\) is analytic, strictly increasing and strictly convex. Thus \(qA(z)-B(z)=0\) has one solution **inside** \(J\) exactly when \(Q(L)<q<Q(R)\); in the closed interval, each endpoint parameter adds its corresponding endpoint root.

The present task is to compute the two endpoint ratios from the actual frozen 189-level survivor recurrence, rather than to infer them from broad Taylor bounds.

## Theorem 697.1: exact endpoint bounds and maximal integer band

The self-contained Python checker recomputes the surviving binomial cells (9,529 nonzero cells across 189 levels), the two separately labelled joint-clock observation branches, the exact \(K_{nm}\) and \(J_{nm}\) bilinear kernels, and the two branch means and variances, using only integer arithmetic and `fractions.Fraction` for proof comparisons. It finds the following **strict rational enclosures**:

\[
\boxed{
\frac{11125016126410650}{10^{15}}<Q(L)<
\frac{11125016126410651}{10^{15}}
}
\]
\[
\boxed{
\frac{46505912169160542}{10^{15}}<Q(R)<
\frac{46505912169160543}{10^{15}}
}.
\]

Equivalently the endpoint ratios are approximately \(11.125016126410650\) and \(46.505912169160542\). The `--full-fractions` option outputs their full exact rational numerators/denominators; the interval endpoints above are checked by *exact cross multiplication* against the same fractions.

Because \(Q\) is continuous and strictly increasing throughout \(J\), the complete real parameter range for a **unique interior** crossing is

\[
\boxed{Q(L)<q<Q(R)}.
\]

In particular, among all nonnegative **integer** parameters, the values yielding an interior crossing are *exactly*

\[
\boxed{q\in\{12,13,\dots,46\}}.
\]

The enlarged integer conclusion strengthens PREFIX-696's certified \(q=12,\dots,45\) interval: **46 is included**, while 11 and 47 lie outside the exact endpoint range. The proof does not infer this from finite samples; the integer classification follows from strict monotonicity and the two exact endpoint enclosures. For arbitrary real \(q\), the open band above is optimal **for this fixed spatial interval** \(J\).

## Theorem 697.2: a rigorous initial bracket for the q=46 crossing

Let \(z_{46}\) be the unique root in \(J\). The exact right endpoint observer gives

\[
m=B(R)-46A(R)>0.
\]

PREFIX-696 established across \(J\)

\[
-1870<A'(z)<-1490,\qquad128<B'(z)<129.
\]

Therefore

\[
-86149<F'_{46}(z)<-68668.
\]

Applying the mean-value theorem between \(z_{46}\) and \(R\) gives the exact rational enclosure

\[
R-\frac{m}{68668}<z_{46}<R-\frac{m}{86149}.
\]

The direct `Fraction` comparisons verify the convenient decimal enclosure

\[
\boxed{0.0531587456<z_{46}<0.0531590002}.
\]

This bracket is useful as a certified starting interval for the previously established safeguarded Newton/readout solver; it is not a native heartbeat-state update.

## Exact calculation path and validation

The finite state predicate is the inherited `alive(n,k)` decision with \(n=1,\ldots,189\), integer denominator \(2^{18}\), and the original strict binomial-survival comparison. For \(z=t/D\) with \(D=25000\), compute

\[
s_n(z)=\sum_{k\in R_n}c_{n,k}\frac{t^k(D-t)^{n-k}}{D^n},
\]

where \(R_n\) is the unchanged frozen survivor row, and \(s_n(0)=c_{n,0}\). With

\[
K_{nm}=\frac{\binom{n+m}{n}}{2^{n+m+1}},\qquad
J_{nm}=\frac{n+m+1}{2}K_{nm},
\]

the common-denominator integer-kernel method of PREFIX-695 evaluates the exact joint moments. Define \(x=s(z)\) and \(y=s(0)\), writing \(\langle x,y\rangle_K=\sum_{nm}x_ny_mK_{nm}\) and similarly for \(J\). The two branch means are

\[
m_d=2\sum_n x_n-\langle x,x\rangle_K,\quad
m_e=\sum_n(x_n+y_n)-\langle y,x\rangle_K.
\]

The corresponding weighted first moments are

\[
h_d=2\sum_n(n+1)x_n-\langle x,x\rangle_J,\quad
h_e=\sum_n(n+1)(x_n+y_n)-\langle y,x\rangle_J.
\]

The exact differences used throughout are

\[
A(z)=2(h_d-h_e)-(m_d^2-m_e^2),\qquad B(z)=m_d-m_e.
\]

No floating-point operations enter a theorem check. Auxiliary float displays are diagnostic only. The original PREFIX-695 full-order checker is retained in the companion program for optional predecessor replay, while the new direct execution evaluates both zeroth-order endpoint moment kernels. The independent local zero-jet implementation completed the calculation and returned `ALL_CHECKS_PASS PREFIX697-R6`; the uploaded companion program encodes the same integer-kernel identities and assertions.

Dependencies: frozen 189-level BRC input at `f42f2906d77f24085c123f3ccfe9667d41caa96d`; PREFIX-695 exact integer-kernel identity; PREFIX-696 strict \(A>0\), \(Q'>0\) and bridge derivative bounds. Evidence is a self-contained checker and compact exact integer-floor output. The proof concerns the typed **auxiliary** \((p,z)\) observer chart, respecting P000 and the ACTIVE six-axis / one-time and residual-fidelity worldview.

## Next discriminating unit

Continue with a piecewise exact/Bernstein derivative or Sturm certificate beyond \(J\), starting from the two new exact endpoint ratios, to learn whether \(Q'(z)>0\) remains valid throughout \([0.052,0.054]\). Then use the resulting one-parameter variance sign partition in the PREFIX-675 mother problem: maximize sampled variance over the complete *auxiliary* triangular parameter domain \(0\le p\le z\le1/2\). Exact source and stored checker should be independently reviewed before Result/Review admission.

Companion files: `PREFIX697_R6_EXACT_ENDPOINTS.py` and `PREFIX697_R6_RESULTS.json`.
