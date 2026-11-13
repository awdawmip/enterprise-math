# R749SG — Exact ancestry survival and minimal Walsh residual for mixed signed-Port paths

Date: 2026-11-12. Author-side research continuation of R749SF, PR #2177. Scientific input fixed at enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, with conditional finite kernel from R749SF at 066958c8da10e4d67395f3c9b6942a8d9d26daa7. P000 six native axes, three-axis slice and joint-observer-preservation constraints remain in scope. No native Cell/Link/Port event is asserted.

## Domain

An unsigned directed edge is (A,B), each a pair of different axes in {0,...,5}, with |A∩B|=1; there are 120 such edges. Each edge admits eight signed lifts, one signed value on each axis of A∪B. A legal next edge is (B,C), with |B∩C|=1; there are eight choices of C. In the homogeneous R749SF conditional model at parameter 0<p<1, when C=A△B the sign of the exposed axis in A\B undergoes a BSC with correlation θ=8p/(1+7p), while the two signs on B are copied. Otherwise the new-axis sign on C\B is a fresh independent fair coin, and both B signs are copied; reappearance of the forgotten axis label alone does not restore its historical signed provenance. All fresh coins are independent.

For a fixed legal unsigned path of m transitions, attach to each current signed token either one of the three *initial* named-sign ancestors with a nonnegative integer number h of forced BSC crossings, or ⊥ (an independent post-start fair sign). Initially every token has a distinct ancestor with h=0. A forced move copies both B ancestors and carries the A\B ancestor to the new occurrence with h+1, if that ancestor exists; a nonforced move replaces the new token's ancestry by ⊥. There is no merging. Let k be the number of surviving original ancestors in the final three-token state.

## Theorem 1 — Full exact conditional kernel, every finite path

For an initial sign assignment s and terminal assignment t, and the surviving terminal tokens x with initial ancestor a(x) and crossing count h(x),

\[
K_{\mathrm{path}}(s,t)=2^{-(3-k)}
\prod_{x:\,a(x)\ne\bot}
\frac{1+\theta^{h(x)}s_{a(x)}t_x}{2}.
\]

Proof: Induct on the number of path transitions. Each forced transition composes one independent binary symmetric sign-flip channel on precisely the exposed token, multiplying its existing correlation by θ. A nonforced transition replaces that token by a new independent fair sign, whose distribution is unchanged by later independent sign-flip channels. Both surviving B tokens are passed without modification. Distinct token ancestries are never merged, proving the product formula at every finite step. The formula extends to p=0 with θ=0 and the usual 0^0=1 convention; at p=1 only forced observed paths have positive probability.

## Theorem 2 — Sharp rank and minimal sufficient Walsh family

For S contained in the three original named axes define χ_S(s)=∏_{a∈S}s_a and μ̂_0(S)=E[χ_S]. Given any terminal subset T of the final three axes: if T includes a token with ancestry ⊥, then μ̂_m(T)=0; otherwise

\[
\widehat\mu_m(T)=
\theta^{\sum_{x\in T}h(x)}
\widehat\mu_0(\{a(x):x\in T\}).
\]

Thus for 0<p<1 the 8×8 conditional prior-to-terminal signed channel has rank **2^k**. Its nonconstant detectable initial-prior space has dimension **2^k−1**, with an exact minimal linear sufficient basis consisting of the Walsh moments of all nonempty subsets of the k surviving initial ancestors. This is a rank claim for arbitrary initial signed distributions and a specified complete final signed-lift distribution; no inference about the physical bit cost of representing arbitrary real probabilities is made.

Proof: Walsh characters form a complete basis on {±1}³. By the displayed pullback formula, each terminal character maps either to zero or to a nonzero multiple of a distinct initial Walsh character on the surviving ancestors. Every subset occurs, and θ>0, so precisely 2^k independent characters, including the constant, remain. In the interior of the initial 8-simplex, independent perturbations along all omitted Walsh directions preserve nonnegativity for sufficiently small amplitude, proving sharpness of the linear rank.

## Theorem 3 — Exact source-ledger repair dimension

Suppose the task requires both the terminal distribution and later arbitrary queries of the **initial** signed source. At fixed path and known 0<p<1, the terminal distribution identifies 2^k−1 nonconstant initial moments by division by their known nonzero θ crossing factors. To reconstruct all seven independent initial moments for arbitrary priors, a minimal complementary *linear moment ledger* has dimension

\[
(2^3-1)-(2^k-1)=8-2^k.
\]

The exact sizes for k=3,2,1,0 are respectively 0,4,6,7. One explicit repair stores the original Walsh moments containing at least one erased ancestor. A single nonforced reset from an otherwise untouched initial triad preserves two singleton moments and their pair moment, but erases the reset singleton, its two pair moments and the triple (four dimensions).

At p=0, any surviving lineage that has crossed at least one forced BSC also loses dependence on its initial sign: in the rank formula replace k by the number of surviving original lineages having h=0. At p=1 every positive-probability unsigned path is all-forced and the channel is invertible (rank 8). The ledger restores previously retained information; it is not a claim that observing a future unsigned path recreates erased source information.

## Theorem 4 — Joint information omitted by singleton-only readouts

The two valid initial distributions μ_±(s)=(1±s_i s_j)/8 have identical zero singleton moments but opposite i,j pair moments ±1. After three consecutive forced C1 transitions on a 3-axis cycle, their terminal pair moments are ±θ². Their exact total-variation distance is θ²; for p=1/2, θ=8/9, this is 64/81. Consequently, retaining only singleton sign expectations is insufficient for complete terminal inference for arbitrary correlated initial signed distributions, even when every observed move is forced. This is an exact, scope-typed joint-relation preservation example.

## Exact verification

The standard-library rational checker R749SG_WALSH_ANCESTRY_EXACT_CHECK.py verifies the one-step local finite structure and selected multi-step conditional 8×8 kernels against the product formula. It enumerates **all** unsigned support paths of lengths 1, 2, 3 from all 120 starting directed edges, respectively 960, 7,680, 61,440 paths, and counts surviving initial ancestors:

| Path length | k=0 | k=1 | k=2 | k=3 |
|---|---:|---:|---:|---:|
| 1 | 0 | 0 | 840 | 120 |
| 2 | 0 | 5880 | 1680 | 120 |
| 3 | 17640 | 41160 | 2520 | 120 |

For θ=8/9 it compares exact rational signed transition compositions to the product law on all 960 one-step support paths, one eighth of 2-step paths, and one sixty-fourth of 3-step paths; it verifies matrix ranks on the checked 1-/2-step paths, p=0 and p=1 forced 3-step endpoints, and the joint pair-moment example. Finite checks support but do not replace the induction for arbitrary m. See the attached executable checker and JSON result. All outputs are model-internal conditional research, pending independent review.

## Next discriminating scientific unit

For any declared future signed-Port query family, take the backward Walsh span of those queries under the permitted finite conditional path kernels. Its rank supplies a smaller task-specific exact provenance ledger than the full 8-lift distribution when the query family permits one. Determine the minimal adaptive query span across allowed future observations, separately from determining whether native V29/V39 permits the underlying event transitions.
