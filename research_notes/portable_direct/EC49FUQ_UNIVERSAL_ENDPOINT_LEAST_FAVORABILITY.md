# EC49FUQ — Universal endpoint-only nuisance reduction and exact finite minimax algorithm

Date: 2026-11-20 (Asia/Shanghai). Evidence: **AUTHOR_PROVED / EXACT_RATIONAL_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

## Frozen input and scope

Parent: EC49FUP@750af59a7f5d96cdbf737d1d7906a22f3b547d03 (PR #2844); structural predecessor EC49FUO@8df5788adcd977cc809a0e27da180833317e3dfa. Frozen BRC16943 science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab is unchanged.

This theorem is about the explicitly **lossy binary count observer** of the clipped-price model, not an identity of native X6 joint state, signed branches, labeled source events, provenance, or future observers. Those typed carriers remain upstream under P000 and ACTIVE worldview.

Fix an integer \(n\ge1\), any real \(0<x<1\), and one **common nuisance parameter** \(\theta\in(0,\theta_E]\) governing both hypotheses and all conditionally independent trials. Compactify by adjoining \(\theta=0\), the limit of finite original nuisance values, and define
\[
\beta=\frac3{637},\quad \theta_E=\frac{31597745}{1653649},\quad
u(\theta)=\frac{21829245984}{45529434409-456083905\theta},
\]
\[
T(\theta,x)=(1-x)(1-\beta x+\beta x\theta),\qquad
p_\theta=1-T(\theta,x),\qquad q_\theta=1-u(\theta)T(\theta,x).
\]
Under the two equally probable hypotheses, the \(n\) bits are conditionally i.i.d. Bernoulli \(p_\theta\) and \(q_\theta\), respectively. Define \(D_\theta(\phi)=\mathbb E_{q_\theta}\phi-\mathbb E_{p_\theta}\phi\); the error is \(R_\theta(\phi)=(1-D_\theta(\phi))/2\).

## Theorem: both least-favorable support locations are fixed

For every \(n\ge1\) and \(0<x<1\):

1. For **every** upper-tail count test \(\phi_{j,\gamma}(K)=0\) for \(K<j\), \(\gamma\) for \(K=j\), and \(1\) for \(K>j\), \(0\le j\le n\) and \(0\le\gamma\le1\), the function \(\theta\mapsto D_\theta(\phi_{j,\gamma})\) is **log-concave** on \([0,\theta_E]\) unless identically zero. Consequently,
\[
\boxed{\min_{0\le\theta\le\theta_E}D_\theta(\phi_{j,\gamma})
=\min\{D_0(\phi_{j,\gamma}),D_{\theta_E}(\phi_{j,\gamma})\}.}
\]
2. For the complete **full-bit randomized composite test problem**,
\[
\boxed{1-2V_n(x)=\max_{j=0,\ldots,n;\;0\le\gamma\le1}
\min\{D_0(\phi_{j,\gamma}),D_{\theta_E}(\phi_{j,\gamma})\}.}
\]
3. A compactified least-favorable nuisance mixture exists supported entirely on the **fixed endpoint pair** \(\{0,\theta_E\}\), possibly on only one endpoint. This improves EC49FUP's at-most-two-points existence result by identifying the locations for every \(n,x\). EC49FUP's \(n=15\) low-width family proves both endpoints are sometimes needed.

### Proof: convex strip and log-concave marginal

Write \(T=c_0+c_1\theta\), with \(c_0=(1-x)(1-\beta x)>0\), \(c_1=(1-x)\beta x>0\). Put \(A=21829245984\), \(B=45529434409\), \(C=456083905\). Exact differentiation gives
\[
\frac{d^2}{d\theta^2}\frac{A(c_0+c_1\theta)}{B-C\theta}
=\frac{2AC(c_1B+Cc_0)}{(B-C\theta)^3}>0.
\]
The denominator is positive throughout the specified parameter interval. Therefore \(p_\theta=1-T\) is affine, while \(q_\theta=1-uT\) is strictly concave. EC49FUO's exact common-gap certificate proves \(0\le p_\theta<q_\theta\le1\) uniformly.

For \(1\le j\le n\), let \(S_j(t)=\Pr\{\mathrm{Bin}(n,t)\ge j\}\). Then
\[
h_j(t)=S'_j(t)=n\binom{n-1}{j-1}t^{j-1}(1-t)^{n-j}.
\]
Set \(S_0=1,S_{n+1}=0,h_0=h_{n+1}=0\). For a single-randomization upper-tail test,
\[
D_\theta(\phi_{j,\gamma})
=\int_{p_\theta}^{q_\theta}h_{j,\gamma}(t)\,dt,\qquad
h_{j,\gamma}=\gamma h_j+(1-\gamma)h_{j+1}.
\]
For \(1\le j\le n-1\), factor
\[
h_{j,\gamma}(t)=n\,t^{j-1}(1-t)^{n-j-1}
\left[\gamma\binom{n-1}{j-1}(1-t)
+(1-\gamma)\binom{n-1}{j}t\right].
\]
The logarithm of this function is a sum of nonnegative multiples of \(\log t\), \(\log(1-t)\), and the logarithm of a positive affine function. Each is concave, so \(h_{j,\gamma}\) is log-concave on \((0,1)\). For \(j=0\) and \(j=n\) it is a multiple of \(h_1\) or \(h_n\), hence remains log-concave. Zero functions are handled separately.

The strip
\[
\mathcal C=\{(\theta,t):0\le\theta\le\theta_E,\ p_\theta\le t\le q_\theta\}
\]
is convex: its lower edge is affine and its upper edge concave. Thus
\[
f(\theta,t)=h_{j,\gamma}(t)\mathbf1_{\mathcal C}(\theta,t)
\]
is jointly log-concave, nonnegative and measurable, with integrable vertical sections. By the classical **Prékopa marginal theorem**, the marginal
\[
\theta\mapsto\int_{\mathbb R}f(\theta,t)\,dt
=D_\theta(\phi_{j,\gamma})
\]
is log-concave. For \(\theta=s\theta_E\), \(0\le s\le1\),
\[
D_{s\theta_E}\ge D_0^{1-s}D_{\theta_E}^{s}
\ge\min\{D_0,D_{\theta_E}\}.
\]
Boundary zero values follow by continuity; an identically zero rule has equal values. Since the endpoints belong to the compact closure, assertion 1 holds for the entire nuisance continuum and any real width.

EC49FUO's uniform rearrangement theorem establishes that every full-bit randomized test is simultaneously weakly dominated at **each nuisance value** by a single upper-tail count rule. Therefore the full primal minimax game reduces to these thresholds, establishing assertion 2. The compact finite-dimensional two-endpoint test-versus-mixture game has a saddle point by standard minimax duality. Its optimal endpoint mixture is least favorable in the complete nuisance game because the latter has exactly the same value. This proves assertion 3.

The single standard external analytic ingredient is Prékopa's theorem (marginals of log-concave functions remain log-concave): A. Prékopa, *On logarithmic concave measures and functions*, Acta Sci. Math. 34 (1973), 335–343; also D. Cordero-Erausquin, *On matrix-valued log-concavity and related Prékopa and Brascamp–Lieb inequalities*, Advances in Mathematics 351 (2019), 96–116, DOI 10.1016/j.aim.2019.04.046, introduction.

## Exact finite algorithm for every rational width

For \(t\in\{0,\theta_E\}\), \(k=0,\ldots,n\), calculate the signed binomial masses
\[
\Delta_t(k)=\binom nk[q_t^k(1-q_t)^{n-k}-p_t^k(1-p_t)^{n-k}].
\]
For each \(j=0,\ldots,n\) put \(a_t(j)=\sum_{k=j+1}^n\Delta_t(k)\) and \(b_t(j)=\Delta_t(j)\). Thus
\[
D_t(\phi_{j,\gamma})=a_t(j)+\gamma b_t(j).
\]
The minimum of the two affine endpoint lines in \(\gamma\) attains its maximum on \([0,1]\) at \(0\), \(1\), or their intersection when the latter lies inside \((0,1)\):
\[
\boxed{\gamma_*=\frac{a_{\theta_E}(j)-a_0(j)}
{b_0(j)-b_{\theta_E}(j)}.}
\]
At most \(3(n+1)\) exact rational candidates determine the **global composite minimax risk**. This removes any nuisance grid, optimization over an infinite parameter half-line, or unknown two-point support-location search. When the optimum randomizes strictly at count \(j\) and both endpoints are active, the least-favorable weight at \(\theta_E\) is
\[
\boxed{\lambda_E=-\frac{b_0(j)}{b_{\theta_E}(j)-b_0(j)}.}
\]
For pure or deterministic optima, choose legal endpoint weights using the mixed signed-mass inequalities. The arithmetic-operation count is polynomial in \(n\); rational integer bit-length can grow with \(n\).

## Evidence and reproducibility

Companion Python 3 standard-library Fraction checker: EC49FUQ_ENDPOINT_ONLY_MINIMAX_VERIFY.py. Locally executed to PASS: enumerated the endpoint candidates, constructed exact endpoint-mixture Bayes sign certificates, and performed 17 equally spaced **exact rational** nuisance checks for each sample. These finite checks corroborate the calculations; the continuum guarantee is the analytic Prékopa proof above.

| n | rational x | optimal j | gamma (approx.) | endpoint-E mixture weight (approx.) | minimax error (approx.) |
|---:|---:|---:|---:|---:|---:|
| 1 | 1/2 | 0 (K>=1) | 0 | 1 | 0.393898388899 |
| 15 | 7/25000 | 1 | 0.999918219751 | 0.948507798287 | 0.00211367366264 |
| 30 | 3/20 | 9 | 0.995202093564 | 0.779814723978 | 0.0143268700724 |
| 40 | 1/100 | 5 | 0.965125521779 | 0.580847895626 | 0.0000243073295010 |
| 60 | 7/20 | 28 | 0.413963860059 | 0.945649097807 | 0.0159339680904 |

The n=15 exact case reproduces EC49FUP. The n=30,40,60 examples supply new arbitrary-n mixed-strategy witnesses with exact dual checks.

## Authorship, control and next problem

Historical author EM-DIRECT-8454C6 and prior SID MCP-44cfc4e6f2094f96861854ebefc77e84 are preserved as **scientific provenance**, not as a current private execution capability. This is independent portable publication through the connected GitHub account; it claims no formal CLAIM, Result, Review, P000 update or Foundation promotion. Researcher Activity linkage requires verification of the actual present identity and scoped write authority. Independent mathematical review is NOT_REVIEWED.

Next: classify for which pairs \((n,x)\) the endpoint-only algorithm chooses a pure nuisance endpoint versus a genuinely mixed saddle; isolate the algebraic switch loci and study large-\(n\) behavior. Separately investigate typed BRC/X6 joint price-origin information lost by the binary count observer.
