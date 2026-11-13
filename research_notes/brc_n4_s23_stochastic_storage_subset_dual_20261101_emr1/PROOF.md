# BRC N=4 / S23: exact unrestricted stochastic five-state storage floor

**2026-11-01 | portable author-side analytic proof and exact Fraction certificate | UNREVIEWED / NOT_ADMITTED.**

## Model and problem

This is an auxiliary strictly positive six-source BRC N=4 prepared-observer problem, not a native P000 dynamics statement. Latent sources in order are AU0, AU1, AV, BU0, BU1, BV. The six prepared distributions mix six latent distributions using a fixed row-stochastic matrix

\[
M=\begin{pmatrix}
1/2&1/2&0&0&0&0\\
9/20&11/20&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&1/2&1/2&0\\
0&0&0&1/10&9/10&0\\
0&0&0&0&0&1
\end{pmatrix},\qquad
N=M^{-1}=\begin{pmatrix}
11&-10&0&0&0&0\\
-9&10&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&9/4&-5/4&0\\
0&0&0&-1/4&5/4&0\\
0&0&0&0&0&1
\end{pmatrix}.
\]

The common encoder E is any nonnegative row-stochastic 6-by-k matrix fixed before policy selection. Each legal S23 causal stopping policy H induces a six-by-four latent stop-time kernel F(H). For a fully policy-informed decoder D_H (nonnegative row-stochastic k-by-four), the six true readouts are MF(H), the approximations are MED_H, and error is the maximum over six prepared-input TV distances. R(k,full) is the infimum over the common E and all policy-specific decoders of the worst policy error. Finite m strategy labels cannot outperform a fully policy-informed decoder, hence R(k,m) >= R(k,full).

## Theorem 1: support-restricted dual obstruction for every stochastic encoder

Let M be any invertible n-by-n row-stochastic mixing matrix and N=M^{-1}. Assume future operations include every binary terminal indicator policy H_S: earlier stopping stages always continue, time 3 occurs exactly for latent source x in S, and time 4 otherwise. For any k<n and any source subset U with |U|=k+1, define

\[
\Delta(U)=\max_{x,y\in U}\lVert N_{x,*}-N_{y,*}\rVert_1,\qquad
\delta_k=\min_{|U|=k+1}\Delta(U).
\]

Then for **every** common real row-stochastic n-by-k encoder, for all policy-informed stochastic decoders, the worst-case prepared-input TV error is at least 1/Delta(U), hence at least 1/delta_k. Consequently R(k,full) >= 1/delta_k and every finite-tag R(k,m) >= 1/delta_k.

**Proof.** The k+1 rows of E indexed by U are linearly dependent: choose a nonzero real vector z supported on U with z^T E=0. Because E 1_k=1_n, necessarily sum_x z_x=0. Define P=sum_{z_x>0}z_x=sum_{z_x<0}(-z_x)>0, and select S={x:z_x>0}. This H_S is legal, because the S23 third-stage node distinguishes all six terminal sources; all earlier nodes are set to continue.

For any decoder let d be the column of its probabilities of outputting time 3. Put u=1_S and r=M(u-E d). The time-3 event discrepancy in each prepared distribution cannot exceed its four-time total variation, so if all errors are <= epsilon then ||r||_infinity<=epsilon. Since N=M^{-1},

\[
P=z^T u=z^T(u-Ed)=z^TNr\le\lVert N^Tz\rVert_1\epsilon.
\tag{1}
\]

Define probability weights p_x=max(z_x,0)/P and q_y=max(-z_y,0)/P. Both are supported in U. The signed combination of inverse rows is the **external readout dual** identity

\[
N^Tz/P=\sum_{x,y}p_xq_y(N_{x,*}-N_{y,*}).
\]

By the triangle inequality,

\[
\lVert N^Tz\rVert_1\le P\sum_{x,y}p_xq_y
 \lVert N_{x,*}-N_{y,*}\rVert_1\le P\Delta(U).
\tag{2}
\]

Equations (1)-(2) imply epsilon>=1/Delta(U), independent of E, D, S23 policy labels or real arithmetic precision. Since the argument works for every U of k+1 sources, choose the U minimizing Delta. QED.

The signed z and inverse N are dual comparison tools for **external probability readouts**; no negative BRC branch mass or amplitude cancellation is being claimed.

## Theorem 2: exact storage bounds and stochastic k=5 closure

For the displayed exact BRC matrix, all 15 inverse-row distances are rational. Their unique maximum is

\[
\lVert N_{AU0,*}-N_{AU1,*}\rVert_1=40.
\]

Complete enumeration of all 57 source subsets of sizes 2 through 6 yields:

| k | minimizing U (zero-based source indices) | delta_k | lower bound for all stochastic E |
| ---: | :--- | ---: | ---: |
| 1 | (2,5) | 2 | 1/2 |
| 2 | (2,4,5) | 5/2 | 2/5 |
| 3 | (2,3,4,5) | 5 | 1/5 |
| 4 | (1,2,3,4,5) | 45/2 | 2/45 |
| 5 | (0,1,2,3,4,5) | 40 | 1/40 |

All bounds apply even when the decoder has the complete future policy, and hence for any finite number of policy labels. Previous general 1/47 is strengthened to 1/40 for every k<=5. No sharpness is asserted for k<=4.

A prior explicit deterministic five-state encoder merges AU0 with AU1 and stores AV, BU0, BU1 and BV exactly. Deterministic encoders are admissible stochastic encoders. For any complete future policy H, denote the four-time latent output laws by f_0,...,f_5. Decode the merged symbol by

\[
q_H=(19f_0+21f_1)/40,
\]

and decode the other four symbols as their respective f_x. The two AU prepared-input readout errors are respectively plus and minus (f_0-f_1)/40, with TV <=1/40, and the other four prepared inputs are reconstructed exactly. The legal third-stage AU0 indicator achieves equality. Hence the unrestricted, **randomized-encoder**, full-policy minimax is solved:

\[
\boxed{R^{\mathrm{stochastic}\ E}_{5,\mathrm{full}}=\frac1{40}}.
\]

For every finite m, R(5,m)>=1/40. The previously proved 11-parameter midpoint policy grid supplies finite decoder banks approaching the same upper bound, so lim_{m->infinity} R(5,m)=1/40 for the original stochastic-encoder class.

### Rigidity of every optimal five-state stochastic encoder

Suppose a stochastic 6-by-5 E attains full-policy error <=1/40. For any nonzero z in its left nullspace, (1)-(2) and optimality force equality in the diameter bound ||N^T z||_1 <=40 P. The pair (AU0,AU1) is the **unique** inverse-row pair at distance 40. Every positive-to-negative pair with nonzero p_xq_y must therefore be this pair, forcing z to be a scalar multiple of e_0-e_1. Thus the left nullspace is precisely that line, rank E=5, and the two encoder rows E_AU0 and E_AU1 are identical. This is a necessary structural condition: randomizing those rows differently cannot yield the minimum. It is not claimed that every E with identical AU rows is optimal.

## Verification, source boundary and outstanding work

The actually executed Python Fraction VERIFY.py checks MN=I in 36 entries; all 15 pairwise inverse-row distances; the optimum of every one of 57 admissible supports; 140 representative integer zero-sum duals; all 2048 deterministic causal 11-control policies with the explicit k=5 decoder, for 12,288 exact TV comparisons; and a sharp equality instance. The complete stdout is RUN_EVIDENCE.txt. The real-stochastic-encoder universal quantifier is established by the above rank-nullity and dual argument, not finite testing. Behavioral randomized policies receive the exact upper bound from the explicit mixture decoder or the prior full-policy convexification theorem; finite policy labels are a separate problem.

BRC application is typed: six positive source laws, positive prepared mixtures, latent provenance, a lawful future stopping-time observer, and exact analysis of compression residual. The six latent source names do not represent P000's six native spatial axes, while the four output times do not define its independent time dimension. No native P000 X6 / three-dimensional slice transfer, S2 causal information-set embedding, external physical assertion, independent review or formal project admission is claimed.

Frozen GLOBAL_KNOWLEDGE_V1 input: awdawmip/chatgpt-global-knowledge main@6f405b5977bced88a276d67a47d9d87c220dad2c; project current canonical main@c8a23c3049786196117d590abdc90560199f6911. P000 startup projection blob c6d4d2d79b09537bdae55253baef9c28583e44dc agreed with its original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Exact predecessor scientific commits: c22282ef2deea811f7e300c76c7282deefb39f89 (deterministic construction) and 2a4628fce898013c2b5a81344ce301de4632d99d (behavioral convexification). Connected GitHub actor awdawmip. Current native service v0.6.11 answered research_authority_granted=false, with quota 5/5; scoped owner read returned CONTROL_QUOTA. Current formal owner is unverified; no CLAIM, registered activity, Result, review or admission is represented by this portable source artifact.

Next independent mathematical unit: close or tighten the k=4 full-policy stochastic encoder gap above 2/45 using the 64 legal subset-indicator policies and all 2048 deterministic S23 tables. The full behavioral ten-tag problem, S2 transfer and P000 native mapping remain separate open obligations.
