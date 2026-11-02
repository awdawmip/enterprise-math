# BRC N=4 S23: exact fixed-bank radii on five- and six-dimensional B-side continua

**Date:** 2026-11-02. **Type:** author-side exact mathematical proof and executed integer certificate; UNREVIEWED / NOT_ADMITTED. **Scientific pin:** 43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged). **Specific ten-decoder bank:** 57a6db1d81068504cca2b3a6ea809a63555473d6 (unchanged). **Direct predecessor:** 8d85ec601ca5e64cee562ddc9f4ef687443e83dd.

## Statement

In the original BRC S23 model with a shared four-state causal encoder, six separately labeled positive-weight preparations and seven fixed plus three explicit free stochastic decoder matrices, write the eleven causal parameters as

\[
z=(z_0,z_1,z_2,z_3,z_4;\ z_5,z_6,z_7,z_8,z_9,z_{10}).
\]

Keep the concrete ten-decoder bank \(\mathcal B=\{D1,D2,D3,D4,D6,D7,D8,K1_{\rm old},K2_{\rm old},K3_{\rm repair}\}\) exactly as in the cited pin. Define

\[
L_D(z)=\max_{0\le i<6}\frac12\sum_{j=0}^3|P_{ij}(z)-Q_{ij}(D)|,\qquad m_{\mathcal B}(z)=\min_{D\in\mathcal B}L_D(z).
\]

Consider the complete real B-side families

\[
\mathcal C_6=\{(s,1/3,9/20,0,0;\ 1,h,k,\ell,r,m):s,h,k,\ell,r,m\in[0,1]\},
\]

\[
\mathcal C_5=\{z\in\mathcal C_6:r=0\}.
\]

**Theorem (this fixed decoder bank).**

\[
\boxed{\max_{z\in\mathcal C_5}m_{\mathcal B}(z)=91/145},\qquad
\boxed{\max_{z\in\mathcal C_6}m_{\mathcal B}(z)=19/30}.
\]

Thus freeing \(z_9\) after the other five coordinates raises the sharp *fixed-bank* radius by exactly \(19/30-91/145=1/174\). The theorem covers all real parameter points, not only a finite mesh.

## Original six-source observation law

Use the original six raw, source-labeled preparations AU0,AU1,AV,BU0,BU1,BV. The index maps are

~~~text
A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
G=(0,0,1,2,2,3)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
~~~

For source \(i\), take \(x=z_{A_i},b=z_{B_i},c=z_{C_i}\), and

\[
R_i(z)=\bigl(x,(1-x)b,(1-x)(1-b)c,(1-x)(1-b)(1-c)\bigr).
\]

The full observed six-row tuple is \(P(z)=(M/20)R(z)\); the decoder observation tuple is \(Q(D)=(M/20)(D_{G_i,*})_{i=0}^{5}\). Every source identity, the nonuniform mixing, and the causal sharing of parameters are retained. All seven fixed and three rational stochastic decoder kernels are reproduced in VERIFY.js.

## Exact lower witnesses

For the 5D family use

\[
W_5=(5/29,1/3,9/20,0,0;\ 1,1,0,0,0,0).
\]

The ten individual decoder risks, in the bank's stated order, are

\[
(19/30,1,1,2/3,24/29,2/3,91/145,91/145,19/30,24/29).
\]

For the 6D family use

\[
W_6=(1/5,1/3,9/20,0,0;\ 1,1,0,1/5,1,0).
\]

All ten decoder risks are

\[
(19/30,1,1,2/3,4/5,2/3,16/25,239/375,19/30,4/5).
\]

These two legal rational policies yield the respective lower bounds. Both vectors are checked exactly by the executable source.

## Finite exact certificate implies upper bounds over all real points

Partition \(s\) at \(0,5/29,1/5,2/5,3/5,4/5,1\); partition each other free coordinate at \(0,1/5,2/5,3/5,4/5,1\).

For \(\mathcal C_5\), the partition has \(7\cdot6^4=9072\) grid vertices and \(6\cdot5^4=3750\) closed cells, each having 32 corners. For \(\mathcal C_6\), it has \(7\cdot6^5=54432\) vertices and \(6\cdot5^5=18750\) closed cells, each with 64 corners.

For **every** cell the saved verifier computes, using integers, the maximum of each decoder's six-source TV risk over **all of that cell's corners**; it chooses the lowest-index decoder that minimizes this maximum. It checks that the selected worst-corner radius is at most \(91/145\) on all 3750 five-dimensional cells and at most \(19/30\) on all 18750 six-dimensional cells. The maximum selected cell radius equals its bound in each family. The complete ordered selection indices, decoder histograms and witness risk vectors are stored in RUN_EVIDENCE.json.

For each source row, no one of the six freed coordinates occurs more than once in its causal product. Each \(R_i\) is therefore separately affine in the six parameters; the linear mixture \(M/20\) preserves this. At any point of a closed d-dimensional cell, the **same entire six-row tuple** \(P(z)\) is the tensor-product convex combination of the \(2^d\) corner tuples, with shared nonnegative coefficients summing to one. For a fixed \(D\), TV is convex; the maximum over the six source-specific TV distances is convex too. Consequently

\[
L_D(z)\leq\max_{c\ \mathrm{corner\ of\ the\ cell}}L_D(c).
\]

The certified **single decoder per cell** therefore covers every real interior point of that cell, and the finite cell partition covers each declared cube. Combining these continuum upper bounds with the rational lower witnesses proves both sharp equalities.

## Exact arithmetic and reproducibility

Run: node VERIFY.js > RUN_EVIDENCE.recomputed.json.

All probabilities are scaled by \(N=6090000\) and stored as safe integers. The verifier checks stochastic normalization, all six causal products, source-mixing divisibility by 20, and both complete vertex/cell sets. It uses the integer value \(\max_i\sum_j|NP_{ij}-NQ_{ij}|\); division by \(2N=12180000\) gives TV. Both thresholds \(2N\cdot91/145\) and \(2N\cdot19/30\) are integers. Every operation fits the JavaScript safe integer range. The saved RUN_EVIDENCE.json is the actual execution output, not a placeholder; the exact source and output Git blobs are individually identified by GitHub.

The prior author-side \(3/5\) lower certificate for the reoptimized three-kernel problem on \(S18\cup J([0,1])\cup F5([0,1]^5)\) remains applicable. With \(\mathcal C_6\) adjoined, the exact **reoptimized** optimum has a current author-side interval

\[
\boxed{3/5\le R_{\rm joint}(S18\cup J\cup F5\cup\mathcal C_6)\le19/30}.
\]

The right endpoint is furnished by the concrete bank; sharpness for reoptimized arbitrary real kernels is unresolved. The full eleven-parameter ten-label mother problem has the separately sourced interval \([1/2,2/3]\). This author-side proof and its immutable source capture do not assert a native CLAIM, a Result or independent mathematical admission.
