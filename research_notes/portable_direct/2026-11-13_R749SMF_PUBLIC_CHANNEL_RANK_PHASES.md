# R749SMF — Exact public-channel information strata of an adaptive signed-source controller

Date: 2026-11-13 (Asia/Shanghai). Author-side continuation of R749SMD/R749SME, PR #2193.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Scope: finite conditional signed-Port/BRC provenance model; historical source labels are not extra spatial axes, and no V29/V39 native event permission is asserted.

## 1. Declared conditional observation model

For Z=(X,Y,T) in {−1,+1}³ and internal outputs (A,B,C)=(a,b,c) in {−1,+1}³, use the earlier adaptive controller:
\[
M_{abc,xyz}=\frac{(2+ax)(2+b y_a)(2+c yt)}{64},\quad y_+=y,\ y_-=t.
\]
The internal controller chooses its B-query using the actual A. A public observer subsequently and independently flips A,B,C with probabilities ε_A,ε_B,ε_C in [0,1]. These flips do not feed back into internal controller modes.

Write D(e)=[[1−e,e],[e,1−e]] and N_ε=(D(ε_A)⊗D(ε_B)⊗D(ε_C))M. For a positional subset S of {A,B,C}, let M_S retain exactly the output coordinates in S by marginalizing the rest. The admissible prior domain is the open simplex of strictly positive probability laws on eight historical states; the target is exact affine-linear expectation coordinates sufficient for all observed three-bit word probabilities.

## 2. Theorem — All positional marginals have maximal row rank

For every S, rank_Q(M_S)=2^|S|. In order none/A/B/C/AB/AC/BC/ABC the ranks are 1/2/2/2/4/4/4/8.

Proof: A,B,C have respective conditional signed means
\[
X/2,\quad \beta=(Y+T)/4+X(Y-T)/8,\quad YT/2.
\]
Each is nonconstant. The AB row space has independent Walsh components of 1,X,(1+X/2)Y,(1−X/2)T; the AC row space has 1,X,YT,XYT. The BC row space spans 1,β,YT,β YT, with
\[
\beta+\beta YT=(Y+T)/2,\quad
\beta-\beta YT=X(Y-T)/4,
\]
so these four functions are linearly independent by disjoint Walsh supports. For ABC, condition on A=+: the subsequent queries (Y,YT) bijectively encode (Y,T); on A=−, the queries (T,YT) do likewise. Define B0=[[3/4,1/4],[1/4,3/4]]. The eight-by-eight likelihood matrix is, up to row/column ordering,
\[
M=\operatorname{diag}(Q_+,Q_-)(B0\otimes I_4),
\]
each Q_a a column permutation of B0⊗B0. This proves rank 8 and |det M|=1/4096.

## 3. Theorem — Sharp noisy observer strata

Let S_ε={i: ε_i≠1/2}. Then
\[
\boxed{\operatorname{rank}(N_\epsilon)=2^{|S_\epsilon|},\quad
c_\epsilon=2^{|S_\epsilon|}-1.}
\]
Here c is the minimum independent affine expectation coordinate count retaining *all* observed-word probabilities for arbitrary strictly interior source priors.

Proof: D(e) is invertible unless e=1/2; at e=1/2 the output is an independent fair sign, so its factor may be dropped without changing rank. The remaining factors are invertible and thus rank(N_ε)=rank(M_{S_ε}) by Section 2. A row-space basis containing the constant 1 yields a carrier of size rank−1. The open prior simplex gives the matching affine lower bound by kernel containment.

Consequently 3,2,1,0 informative public positions require 7,3,1,0 independent moments respectively. The endpoints e=0 and e=1 are both information-preserving deterministic labelings.

## 4. Determinant and robust inversion

For all real ε_i in [0,1],
\[
\boxed{|\det N_\epsilon|=2^{-12}\prod_{i=A,B,C}|1-2\epsilon_i|^4.}
\]
For all ε_i≠1/2, in Euclidean vector norm,
\[
\sigma_{\min}(N_\epsilon)\ge\frac18\prod_i|1-2\epsilon_i|,
\quad
\|\mu-\nu\|_2\le
\frac8{\prod_i|1-2\epsilon_i|}\,\|N_\epsilon\mu-N_\epsilon\nu\|_2.
\]
Proof: det(D(e))=1−2e and the threefold Kronecker determinant contributes its fourth power per coordinate. The signed-root factor B0 has least singular value 1/2, each block Q_a has least singular value 1/4, hence σ_min(M)≥1/8. Multiplying by the public product channel gives the inequality.

## 5. Positive-prior contrast with exact TV

Let μ_±(x,y,t)=(1±yt/2)/8, every atom at least 1/16. Both yield the same AB marginal, and the exact complete original laws are P_±(a,b,c)=(4±c)/32. Independent public noise yields
\[
\boxed{\operatorname{TV}(N_\epsilon\mu_+,N_\epsilon\mu_-)=|1-2\epsilon_C|/4.}
\]
Thus this historical relation can be detected purely from C, irrespective of how much A and B are postprocessed.

## 6. Reproducibility and follow-up

The companion standard-library Fraction verifier constructs all eight histories and eight complete words, computes rational ranks/determinants, and checks the 8 positional marginal ranks plus 125 exact triples ε_i in {0,1/4,1/2,3/4,1}. Each triple verifies normalized columns, the exact rank, the determinant formula and the two-prior TV formula. Executed result: PASS; noise-stratum counts (0,1,2,3 informative bits)=(1,12,48,64). Proofs apply for all real ε_i∈[0,1], not just tested fractions. Full code: R749SMF_PUBLIC_CHANNEL_OBSERVER_CHECK.py; results: R749SMF_PUBLIC_CHANNEL_OBSERVER_RESULTS.json.

Next discriminating question: allow noisy A to feed back to the second-query selector, calculate the resulting exact adaptive kernel, and determine whether every positional marginal still has full row rank. Independently obtain a genuinely admitted V29/V39 three-force event/closure witness before assigning any native Port/BRC consequence. Neither task ownership nor native permission is inferred from this author-side mathematical result.
