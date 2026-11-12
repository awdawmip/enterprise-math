# R748 — Exact spectrum and all-horizon source residual in the signed-Port C1 BRC observer

Date: 2026-11-12 (Asia/Shanghai). Parent Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Frozen scientific source: a72226e2430ffa4786321ac86e7f0c599d5f0389. Prior exact author-side candidate: R747 (PR #2157, commit cbbb54aa1024a4849540d66adc7a98d1e1d48d9b). All statements here are inside the proposed finite C1 Port process over native X6. They do not claim native V29/V39 execution.

## 1. Typed model and BRC observer

There are six native axes; keep signs separate. Let S={(i,s):0<=i<6,s∈{-1,+1}} be the twelve signed Ports. A visible state v is an unordered pair of Ports on distinct axes; hence |V|=C(6,2)*4=60. Define the integer adjacency A[v,w] to be one precisely if v and w share exactly one *identical signed Port* and their union has three distinct axes, otherwise zero. A is symmetric and every row has 16 ones.

A *fixed-source* state is an oriented signed triad with an observed phase, represented by a directed edge (v,w) with A[v,w]=1; its deterministic C1 shift is (v,w)↦(w,v △ w), with △ the symmetric difference of signed-Port sets. R747 proves exact period three for all 960 such states. By contrast, independently drawing one of sixteen source continuations after **every** observation produces the Markov kernel P=A/16. Forgetting source is therefore an observer projection with a specified future-composition scope, not a silent identification of the two processes.

## 2. Exact spectrum theorem and proof

**Theorem.** The complete eigenvalue multiset of A is

\[
\boxed{16^{[1]},\quad 8^{[6]},\quad 4^{[5]},\quad 0^{[15]},\quad (-2)^{[24]},\quad (-4)^{[9]}}
\]

where bracket exponents are algebraic multiplicities.

**Proof.** For each axis pair i<j write the sign-Fourier decomposition
\[
f_{ij}(s,t)=\alpha_{ij}+\beta_{ij,i}s+\beta_{ij,j}t+\gamma_{ij}st.
\]
Directly from the signed-Port intersection rule,
\[
(Af)_{ij}(s,t)=\sum_{k\notin\{i,j\}}\sum_{u=\pm1}
[f_{ik}(s,u)+f_{jk}(t,u)],
\]
interpreting f by axis labels. The summation over u cancels every term containing u. It follows that alpha, beta and gamma are invariant independent subspaces.

On the 15-dimensional alpha space, A is twice the adjacency operator of the line graph L(K6):
\[
(A\alpha)_{ij}=2\sum_{k\ne i,j}(\alpha_{ik}+\alpha_{jk}).
\]
Constant alpha yields eigenvalue 16 (dimension 1). Alpha of the form u_i+u_j, with sum_i u_i=0, yields eigenvalue 4 (dimension 5). The remaining kernel of unsigned vertex-edge incidence, defined by sum_{j≠i} alpha_{ij}=0 for all i, yields eigenvalue -4. Its dimension is 15−6=9: the incidence matrix has rank 6, since a left-kernel vector t would satisfy t_i+t_j=0 for all distinct i,j, forcing every t_i=0.

For beta, fix one axis i. Its five coefficients beta_{ij,i} evolve under 2(J5−I5): the common coefficient has eigenvalue 8, and the four-dimensional zero-sum subspace eigenvalue −2. The six axes give multiplicities 6 and 24. Every gamma coefficient disappears on summing over the discarded third sign, so all 15 gamma dimensions have eigenvalue zero. The independent dimensions add to 60, completing the spectral proof. The entire construction commutes with the S6 native axis-label permutation skeleton. QED.

## 3. Every-step return, determinant and rational BRC recurrence

The signed-axis permutation group (including simultaneous relabeling of the two signs per axis) acts transitively on visible pairs and commutes with A. Therefore each diagonal entry of A^n equals tr(A^n)/60. For every n>=1 and visible pair v,
\[
\boxed{(P^n)_{vv}=
\frac{16^n+6\,8^n+5\,4^n+24(-2)^n+9(-4)^n}
{60\,16^n}.}
\]
The zero-eigenvalue sector contributes 0 for n>=1. The n=2 value is 1/16; n=3 is 7/256 (recovering R747); n=4 is 49/2048.

The exact determinant is
\[
\det(I-zA)=(1-16z)(1-8z)^6(1-4z)^5(1+2z)^{24}(1+4z)^9.
\]
This is an exact finite BRC closed-walk algebraic observable. For nonnegative rational t, the total-all-length positive mass of tA converges iff 16t<1 (the ordinary stochastic choice t=1/16 is the critical boundary for summing all lengths). No floating-point spectral inference enters these results.

## 4. Exact mixing and persistent source-memory defect

P=A/16 is symmetric stochastic. Its eigenvalue 1 is simple and all other eigenvalues have absolute value at most 1/2. Hence the graph is connected, nonbipartite, and the independent-resampling observer converges to uniform stationary pi=1/60. By vertex-transitivity, the diagonal of every spectral projector of multiplicity m is m/60. For n>=1,
\[
\chi^2(P^n(v,\cdot)\Vert\pi)
=6\,4^{-n}+14\,16^{-n}+24\,64^{-n},
\]
and consequently
\[
\|P^n(v,\cdot)-\pi\|_{\mathrm{TV}}
\le\frac12\sqrt{6\,4^{-n}+14\,16^{-n}+24\,64^{-n}}.
\]

Select instead a hidden oriented triad once (uniformly among the 16 lifts of initial v), keep the source, and advance the exact C1 shift. Its visible return probability is
\[
p_{\mathrm{retained}}(n)=\mathbf1_{\{3\mid n\}}\quad(n\ge0).
\]
In particular for n=3k>=3 the retained process returns with probability 1, while the independently resampled process tends to 1/60. Thus the all-horizon residual is exactly
\[
\boxed{\lim_{k\to\infty}
[p_{\mathrm{retained}}(3k)-(P^{3k})_{vv}]=59/60.}
\]
The source-losing observer and source-preserving composition differ by an order-one quantity at arbitrarily long horizons, despite sharing the same 16 one-step choices. The previous/current visible pair is the sharp 4-bit repair for exact serial C1 dynamics (R747), without permanent full-history storage.

## 5. Validation and limits

The accompanying standard-library Python verifier constructs all 60 signed-Port pairs and all 960 directed edges, checks 60 independent **exact** eigenvectors by matrix multiplication, then independently calculates integer A^n for n=1..6 and verifies every trace and per-vertex diagonal against the spectral formula. The resulting parsable JSON is included verbatim. The finite enumeration verifies the particular graph and the full proof establishes formulas for every n.

The precise pending parent-task step is to read a genuinely valid TRIADIC_CLOSURE_E event from the task-frozen native Cell/Link/Port rules, execute or derive its actual V29 PASS/V39 successor and flow for one and three events, and compare the resulting native observer composition with the C1 pair map. Keep a typed defect if the updates do not commute; this theorem does not assert correspondence merely from notation.
