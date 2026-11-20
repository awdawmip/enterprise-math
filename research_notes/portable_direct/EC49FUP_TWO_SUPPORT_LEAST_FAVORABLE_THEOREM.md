# EC49FUP — Two-support least-favorable nuisance theorem for every number of binary observations

Date: 2026-11-20 (Asia/Shanghai). Evidence: **AUTHOR_PROVED / EXACT_RATIONAL_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

## Source scope, parent and representation

Parent: EC49FUO, immutable research commit 8df5788adcd977cc809a0e27da180833317e3dfa (PR #2842); inherited frozen BRC16943 science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This theorem applies to the explicit, deliberately lossy clipped-price **binary count observer**. It does not assert sufficiency of count data for native X6, labeled price-origin, signed-path or joint event observables. P000 and source-provenance restrictions remain unchanged.

Fix any integer n≥1 and real width 0<x<1. A **single common** nuisance parameter θ∈(0,θ_E] governs both hypotheses and all n conditionally independent Bernoulli observations, with the boundary θ=0 corresponding only to the limit of finite original nuisance parameters. The exact parent probabilities are

\[
\beta=\frac3{637},\quad \theta_E=\frac{31597745}{1653649},\quad
u(\theta)=\frac{21829245984}{45529434409-456083905\theta},
\]
\[
T(\theta,x)=(1-x)(1-\beta x+\beta x\theta),\quad
p_\theta=1-T(\theta,x),\quad q_\theta=1-u(\theta)T(\theta,x).
\]

Under H− the n bits have Bernoulli(pθ) law and under H+ Bernoulli(qθ). Equal hypothesis priors. For a randomized test φ, let Dθ(φ)=E_{+,\theta}φ−E_{−,\theta}φ, so its error is (1−Dθ(φ))/2. The composite minimax value is V_n(x)=½(1−max_φ min_{θ∈[0,θ_E]} Dθ(φ)); the minimum over θ=0 is the closure of the original θ>0 problem.

The EC49FUO **uniform threshold-rearrangement theorem** has already shown: for every full-bit φ there is a single upper-tail count rule uniformly dominating φ over every θ; and a common reference binomial mass b_r(k)>0 yields strict increasing signed-density ratios Δθ(k)/b_r(k), where

\[
\Delta_\theta(k)=\binom nk[q_\theta^k(1-q_\theta)^{n-k}-p_\theta^k(1-p_\theta)^{n-k}].
\]

This is the only result from EC49FUO that the following new theorem needs.

## New theorem: two nuisance points suffice

**Theorem (uniform in n and x).** For every n≥1 and x∈(0,1), the compactified composite minimax game possesses an optimal upper-tail count threshold test and a least-favorable probability distribution π* on [0,θ_E] supported on **at most TWO distinct nuisance parameters**.

The test and π* form a saddle point for the shared-nuisance discrimination game:

\[
D_\theta(\phi^*)\ge v,\quad\forall\theta\in[0,\theta_E],\qquad
\int D_\theta(\phi)\,d\pi^*(\theta)\le v,\quad\forall\phi,
\]
\[
v=\int D_\theta(\phi^*)\,d\pi^*(\theta)=1-2V_n(x).
\]

Hence, in this exact binary observer, the general n+1 support upper bound in EC49FUO is improved to the **constant bound 2**, independent of n. This is an existence bound; some least-favorable mixtures might use more support without necessity. If π* includes θ=0, it belongs to the compactified game, while finite θ>0 can approximate its risk arbitrarily closely in the original parameter model.

### Proof: threshold coordinate is a one-dimensional concave decision game

Choose the common reference probability r from EC49FUO, and b_r(k)=Binomial(n,r){k}. For reference acceptance mass a∈[0,1], fill counts from k=n downward, obtaining φ^a; at most one count j is randomized. Let a_j=Σ_{k=j}^n b_r(k), with a_{n+1}=0 and a_0=1. On the interval a∈[a_{j+1},a_j],

\[
\phi^a_k=\begin{cases}
0&k<j,\\
(a-a_{j+1})/b_r(j)&k=j,\\
1&k>j.
\end{cases}
\]

Define Fθ(a)=Σ_k Δθ(k)φ^a_k. Its slope on that interval is

\[
s_{\theta,j}=\frac{\Delta_\theta(j)}{b_r(j)}.
\]

The inherited signed-density order gives s_{θ,0}<s_{θ,1}<⋯<s_{θ,n}. Since increasing a successively fills n,n−1,…,0, the slopes of Fθ(a) **strictly decrease with a**. Therefore Fθ is continuous and concave, piecewise affine on a partition shared by all θ. The map θ↦Fθ(a) is continuous on compact [0,θ_E]. The original test game and the scalar game have the same value for every pure θ and every nuisance mixture, by uniform pointwise threshold dominance.

Apply the elementary convex-concave minimax theorem to a∈[0,1] and probability measures π on [0,θ_E]. Both are compact convex; \(\int F_\theta(a)d\pi(\theta)\) is concave in a and affine in π. Thus a saddle pair (a*,π) exists. Put

\[
v=\min_\theta F_\theta(a^*),\qquad
C=\{\theta:F_\theta(a^*)=v\}.
\]

Because π is minimizing at a*, its support lies in C. Denote by Lθ and Rθ respectively the left and right slopes of Fθ at a*, with Lθ≥Rθ. Each is continuous in θ, since all Fθ share the same finite a-breakpoint partition.

**Interior point 0<a*<1.** Optimality of a* for the concave function Fπ(a)=∫Fθ(a)dπ gives

\[
\int L_\theta d\pi\ge0\ge\int R_\theta d\pi.
\]

Therefore there are θ+∈C with L_{θ+}≥0 and θ−∈C with R_{θ−}≤0. If any θ∈C satisfies Rθ≤0≤Lθ, its pure mass alone has its maximum at a*, hence is least favorable.

Otherwise every active slope interval lies strictly to one side of zero. In particular R_{θ+}>0 and L_{θ−}<0, so R_{θ−}<0. Set

\[
\lambda=\frac{-R_{\theta-}}{R_{\theta+}-R_{\theta-}}\in(0,1),\qquad
\pi_2=\lambda\delta_{\theta+}+(1-\lambda)\delta_{\theta-}.
\]

Then the mixture's right slope at a* is zero, and its left slope is at least its right slope, hence nonnegative. The mixture's concave objective is consequently maximized at a*. Both θ± belong to C, so the mixture attains v at a*. This gives the required saddle with two support points.

**Boundary a*=0 or a*=1.** At a*=0, the π-average right derivative is ≤0, hence some θ∈C has right derivative ≤0 and its individual concave Fθ is maximized at 0. At a*=1 the analogous left derivative is ≥0. A single active pure nuisance parameter is then sufficient.

This proves both the bound and saddle property. No finite mesh, asymptotic step, or assumption that the two nuisance values are θ=0 and θ_E enters the theorem.

### Constructive optimality certificate

For an interior saddle a*, the two support candidates are **active** nuisance points tied at Fθ(a*)=v; their left/right slopes surround zero. For a randomized count j (a* strictly inside a binomial reference-mass interval), Lθ=Rθ=sθ,j and the mixture weight can be chosen to cancel the signed density at that count:

\[
\lambda s_{\theta_+,j}+(1-\lambda)s_{\theta_-,j}=0.
\]

At a deterministic threshold, check the corresponding mixture one-sided slope inequalities Lπ≥0≥Rπ. Combine these scalar optimality conditions with an exact global inequality Fθ(a*)≥v to certify the complete infinite nuisance interval.

This reduces the worst-case nuisance **support-size search** to one or two points. Locating those points and proving a global nuisance inequality for arbitrary n,x remains a separate, well-defined algebraic optimization problem.

## Exact rational witness and validation

Take n=15, x=7/25000, and θ endpoints 0 and θ_E. Let Aθ be the difference of probabilities of K≥1 and dθ=Δθ(1). The randomized K=1 decision probability

\[
\alpha=1-\frac{A_{\theta_E}-A_0}{d_{\theta_E}-d_0}
\]

equalizes the discrimination at both endpoints. The least-favorable endpoint mixture gives weight

\[
\lambda=\frac{-d_0}{d_{\theta_E}-d_0}
\]

to θ_E. Exact rational arithmetic proves d0<0<dE, 0<α<1, 0<λ<1, D0(α)=DE(α), and that the mixed signed count distribution is negative at K=0, zero at K=1, and positive at every K=2,…,15. Numerically, α≈0.9999182197507327, λ≈0.9485077982871909 and minimax risk≈0.0021136736626381075. The full θ-continuum minimax claim for this sample uses the already saved analytic parent theorem EC49FUI; this run's companion script checks the exact saddle algebra and 1001 rational θ mesh points, which alone would not certify the continuum.

Local verification: Python 3 standard library Fraction, companion script EC49FUP_TWO_SUPPORT_VERIFY.py, returned PASS. No independent mathematical review or formal task admission has been performed.

## Current provenance, statuses, next question

Original EC49 lineage author: EM-DIRECT-8454C6; prior public SID MCP-44cfc4e6f2094f96861854ebefc77e84 is **historical attribution only**, not a private execution capability held by this run. Current formal CLAIM/Result/Review are not established, and independent author-side portable publication does not claim them. Status: AUTHOR_PROVED / EXACT_RATIONAL_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED.

**Next scientific problem:** classify when the optimal least-favorable compactified support can be reduced to a single θ, and identify the two contact points (endpoints versus interior) as functions of n and x; develop exact semialgebraic certificates of the global nuisance inequality. A separate observer-refinement direction is to quantify the information lost from tagged native price origins under the binary count projection, retaining the declared BRC/X6 types.
