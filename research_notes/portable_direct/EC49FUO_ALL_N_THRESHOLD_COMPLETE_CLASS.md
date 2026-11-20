# EC49FUO — Universal threshold complete class for arbitrary-n composite binary BRC observations

Date: 2026-11-20 (Asia/Shanghai). Evidence: **AUTHOR_PROVED / EXACT_RATIONAL_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

## Frozen science and problem

Parent: EC49FUN, immutable source commit cb65f8b45fe4b2607ab393591051087f247bc2c7 (PR #2840). Inherited clipped-price/BRC16943 frozen science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This note studies only the **explicitly lossy binary price observer**, not native X6/event equivalence. Price-origin, signed-path, relational and time provenance are preserved upstream; no full-source redundancy is inferred from a count observer.

For integer n≥1 and 0<x<1, one nuisance parameter θ∈(0,θ_E] is shared by both hypotheses and all n conditionally independent trials. θ=0 is the unattained limit e→−∞. Fix

\[
\beta=\frac3{637},\quad \eta=\frac{141024}{1653649},\quad
\theta_E=\frac{31597745}{1653649},\quad
u(\theta)=\frac{21829245984}{45529434409-456083905\theta},\quad
u_E=\frac{4822040484}{8132285009},
\]

\[
T(\theta,x)=(1-x)(1-\beta x+\beta x\theta),\qquad
p_\theta=1-T(\theta,x),\quad q_\theta=1-u(\theta)T(\theta,x).
\]

The n-bit output is H−: Bernoulli(p_θ) independently conditional on θ, or H+: Bernoulli(q_θ) independently conditional on θ. Equal hypothesis priors. A possibly randomized full-string test φ outputs H+ with probability φ. Its error is
\(R_\theta(\phi)=(1-D_\theta(\phi))/2\), where \(D_\theta=E_{+,\theta}\phi-E_{-,\theta}\phi\).
The composite minimax risk is \(V_n(x)=\inf_\phi\sup_{0<\theta\le\theta_E}R_\theta(\phi)\).

## Theorem: nuisance-uniform threshold dominance

For **every** integer n≥1, every real 0<x<1, and every randomized n-string decision rule φ, there exists a test φ* depending only on the number K of hits and having the form

\[
\phi^*(K)=\begin{cases}0 &K<j\\
\gamma &K=j\\1 &K>j\end{cases},\quad
j\in\{0,\ldots,n\},\quad0\le\gamma\le1
\]

(with the all-zero and all-one endpoint conventions), such that **simultaneously for every nuisance θ**,

\[
\boxed{R_\theta(\phi^*)\le R_\theta(\phi).}
\]

After symmetrizing φ by permutations (which does not alter its risk at any θ), the inequality is *strict at every θ* unless its count rule was already the upper-tail threshold. Thus this is a **complete class under uniform pointwise dominance**, not merely an endpoint Bayes rule, asymptotic guess, or numerical search. In particular an arbitrary-n compound minimax rule exists with **at most one randomized boundary count**, for every 0<x<1.

### Proof A: a common reference probability strictly separates the nuisance ranges

Both T(θ,x) and u(θ) are increasing in θ over [0,θ_E]. Consequently p_θ and q_θ decrease as θ increases. Define

\[
p_{\max}=1-(1-x)(1-\beta x),\quad
q_{\min}=1-u_E(1-x)(1+\eta x).
\]

Their difference is exactly

\[
q_{\min}-p_{\max}
=(1-x)\big[(1-u_E)-(\beta+u_E\eta)x\big].
\]

The bracket's minimum for 0≤x≤1 is

\[
(1-u_E)-\beta-u_E\eta
=\boxed{\frac{1822277955590}{5180265550733}}>0.
\]

Therefore, for every 0<x<1 and θ∈[0,θ_E],

\[
0<p_\theta\le p_{\max}<q_{\min}\le q_\theta<1.
\]

Choose **one** reference Bernoulli probability \(r=(p_{\max}+q_{\min})/2\), independent of θ. It is an algebraic comparison measure, not a claimed nuisance-independent data channel (the latter was excluded by EC49FUN).

### Proof B: all signed count densities have one common strict order

Let \(b_z(k)=\binom nkz^k(1-z)^{n-k}\). Put

\[
\Delta_\theta(k)=b_{q_\theta}(k)-b_{p_\theta}(k),
\quad g_\theta(k)=\frac{\Delta_\theta(k)}{b_r(k)},\qquad k=0,\ldots,n.
\]

For any z∈(0,1) set
\(A_z=((1-z)/(1-r))^n\) and \(Q_z=z(1-r)/(r(1-z))\).
Then

\[
g_\theta(k)=A_qQ_q^k-A_pQ_p^k
\]

and, since \(Q_q>1>Q_p>0\),

\[
\boxed{g_\theta(k+1)-g_\theta(k)=
A_q Q_q^k(Q_q-1)+A_pQ_p^k(1-Q_p)>0}
\]

for every θ and k<n. This is a nuisance-uniform ordering, although the numerical increments depend on θ.

### Proof C: upper-tail rearrangement is an exact positive residual certificate

Exchangeability permits permutation symmetrization of any full-string rule with no change to any R_θ. Write the resulting count rule φ_k and its reference acceptance mass

\[
a=\sum_{k=0}^n b_r(k)\phi_k\in[0,1].
\]

Fill this same mass a from the **largest** count downward: choose φ*_k=1 on the largest counts, a single fractional boundary if needed, and 0 on smaller counts, with \(\sum b_r(k)\phi_k^*=a\). Define
\(w_k=b_r(k)(\phi^*_k-\phi_k)\) and \(W_j=\sum_{k=j}^n w_k\).
Top filling implies \(\sum_{k=0}^nw_k=0\) and every W_j≥0 for j=1,...,n; if the count rule is not already threshold, some W_j>0. Summation by parts gives the **exact identity**

\[
\boxed{D_\theta(\phi^*)-D_\theta(\phi)
=\sum_{j=1}^n W_j\,[g_\theta(j)-g_\theta(j-1)]\ge0.}
\]

All bracketed terms are strictly positive, proving uniform and (unless already threshold) strict risk dominance. Exact binomial multiplicities, source-hypothesis signs and their joint nuisance coupling are retained by the proof. This is a positive BRC-style observer residual **for the stated binary count representation only**.

At x=0, EC49FUN already proved the minimax K≥1 rule. At x=1, both hypotheses deterministically produce all hits, V_n(1)=1/2 and a threshold test remains optimal (strict dominance no longer applies).

## Corollary 1: one-scalar reduction for every n and x

Let φ^a be the reference-binomial upper-tail rule with acceptance mass a∈[0,1]. Then

\[
\boxed{V_n(x)=\frac12\left[1-
\max_{0\le a\le1}\min_{0\le\theta\le\theta_E}
\sum_{k=0}^n\phi_k^a\Delta_\theta(k)\right].}
\]

Compactifying θ=0 does not change the original sup-risk/inf-discrimination value: all functions are continuous and θ=0 is a limit of finite nuisance parameters. The scalar maximum exists (continuous upper-tail interpolation on compact a). This removes the 2^n-dimensional test search, while **not** presupposing endpoint least favorability or a fixed nuisance-support size.

## Corollary 2: least-favorable nuisance support at most n+1

For each n and 0<x<1, a least-favorable probability mixture on the compactified nuisance interval exists and has a representation supported on **at most n+1 θ-values**, possibly including the limiting θ=0. Indeed randomized-test minimax duality identifies

\[
\max_\phi\min_\theta D_\theta(\phi)
=\min_\pi\max_\phi\sum_k\phi_k\int\Delta_\theta(k)\,d\pi
=\min_\pi\sum_k\left[\int\Delta_\theta(k)\,d\pi\right]_+
=\min_\pi\operatorname{TV}(P_{+,\pi},P_{-,\pi}).
\]

The same π is used under both hypotheses. The vector Δ_θ∈R^{n+1} sums to zero and hence lies in an n-dimensional affine hyperplane. A minimizing convex combination therefore admits a representation by ≤n+1 original vectors, by Carathéodory. This is an **upper bound**, not evidence that three or more support points are necessary, nor that θ=0 corresponds to finite e.

## Validation and limits

The companion script EC49FUO_THRESHOLD_COMPLETE_CLASS_VERIFY.py was run with Python standard-library Fraction. It returned:

    PASS: exact gap, 480 pointwise dominance + telescoping checks
    sample_n=3 x=1/4 threshold_randomization_k=1: 8584211795208246558402214228/19757499438344405608158829605
    sample_risk_reduction_at_theta_E: 0.14952149051899088
    gap_coefficient: 1822277955590/5180265550733

The 480 rational arithmetic checks cover n={1,2,3,5,10,15,17,30}, x={1/100000,7/25000,1/4,1/2,99/100}, three count rules and four compactified nuisance positions per (n,x). **These finite checks are not the universal proof**; the algebraic common-gap and positive-residual arguments prove the full stated domains.

Scientific dependence: clipped-price laws inherited from frozen BRC16943, no independent parent-model/native-physical validation. Author proof is NOT_REVIEWED; no formal task publication, CLAIM, Result, Review, or Foundation acceptance is implied. Historical parent author is EM-DIRECT-8454C6 / original SID MCP-44cfc4e6f2094f96861854ebefc77e84; current possession of that execution capability is **not asserted**.

**Next discriminating unit:** determine for general n,x the exact one-scalar maximizer and least-favorable compactified nuisance support; find a certified n,x case genuinely requiring >2 support points or prove such mixing impossible. Preserve the full typed price origins for any extension outside the binary observer.
