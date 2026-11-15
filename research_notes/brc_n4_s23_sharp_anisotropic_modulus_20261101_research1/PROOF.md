# BRC N=4 / S23 — sharp anisotropic pointwise modulus and a larger open strict hull-gap neighborhood

2026-11-01. **AUTHOR ANALYTIC PROOF / EXACT V8 BIGINT EXECUTED / UNREVIEWED / NOT ADMITTED.** This is a direct continuation of the three-control exact lawful-versus-hull counterexample at Enterprise Math commit 43ec6098b1330ae86d0a7863be336c5d97f6ef34 and of its uniform perturbation theorem at 08019c1af1e253a0f45623e8c0da9aeef14dbe67. Neither predecessor is asserted to have undergone independent mathematical admission.

## Frozen positive BRC model and observers

Six distinct, positive-source BRC branches are AU0, AU1, AV, BU0, BU1 and BV. Their stop-time law is

\[
F(a,b,c)=\big(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)\big).
\]

The six observed preparation rows mix these six sources with integer weights

\[
20M=\begin{pmatrix}
10&10&0&0&0&0\\9&11&0&0&0&0\\0&0&20&0&0&0\\
0&0&0&10&10&0\\0&0&0&2&18&0\\0&0&0&0&0&20
\end{pmatrix}.
\]

Freeze a_B=1/4, b_AV=0, b_BV=1/3 and all third-stage c controls except c_AV at 1/2. The legal variable triple is (a,b,c)=(a_A,b_U,c_AV), where **b_U is the same causal control** for A- and B-source branches. The exact base box is

\[
Q=[1/2,7/8]\times[1/8,1/2]\times[1/2,7/8].
\]

For this frozen slice the AU0/AU1 and BU0/BU1 *probability rows* coincide, but their original source labels and mixture map are retained. The row laws simplify to

\[
\begin{aligned}
P_{AU}(a,b)&=(a,(1-a)b,(1-a)(1-b)/2,(1-a)(1-b)/2),\\
P_{AV}(a,c)&=(a,0,(1-a)c,(1-a)(1-c)),\\
P_{BU}(b)&=(1/4,3b/4,3(1-b)/8,3(1-b)/8),\\
P_{BV}&=(1/4,1/4,1/4,1/4).
\end{aligned}
\]

Distance between *joint* six-preparation observations is D(P,P')=max_i TV(P_i,P'_i). TV is half the L1 distance on the four terminal labels. All parameter values in this note are real, not grid-restricted.

## Theorem 1 — exact anisotropic pointwise perturbation modulus

For 0<=A,B,C<=1/8 let

\[
\Omega_Q(A,B,C)=\sup\{D(P(a,b,c),P(a',b',c')):(a,b,c)\in Q,\ (a',b',c')\in[0,1]^3,
\ |a-a'|\le A,\ |b-b'|\le B,\ |c-c'|\le C\}.
\]

Then the **exact**, attained supremum is

\[
\boxed{\Omega_Q(A,B,C)=\max\left\{
 A,\ \frac78 A+\frac12B+AB,\
 \frac78 A+\frac12C+AC,\ \frac34B
\right\}.} \tag{1}
\]

In particular, for 0<=d<=1/8,

\[
\boxed{\Omega_Q(d,d,d)=\frac{11}{8}d+d^2.} \tag{2}
\]

This improves the previous pairing estimate 3d/2 and its first-order constant, from 3/2 to the **sharp** 11/8. The word sharp here refers to the full pointwise perturbation class in (1), not to the Hausdorff distance between two particular observed boxes.

### Proof, upper bound

Any three-atom probability vectors u,v satisfy TV(u,v)=max_j |u_j-v_j|. In AU and BU, merge the two equal last stop atoms *only for calculating this declared four-stop TV*, retaining their original source labels; AV already has three nonzero atoms. Thus AU's relevant coordinates are a, (1-a)b, and (1-a)(1-b). For paired inputs in (1), a>=1/2, b∈[1/8,1/2], and 1-a'<=1/2+A. Consequently

\[
\begin{aligned}
|a-a'|&\le A,\\
|(1-a)b-(1-a')b'|&\le \tfrac12 A+(\tfrac12+A)B,\\
|(1-a)(1-b)-(1-a')(1-b')|&\le \tfrac78 A+(\tfrac12+A)B.
\end{aligned}
\]

The last bound dominates the second. Likewise AV's three effective coordinates obey, respectively,

\[
A,\quad \tfrac78 A+(\tfrac12+A)C,\quad \tfrac12 A+(\tfrac12+A)C.
\]

BU contributes exactly (3/4)|b-b'|<=3B/4, and BV is constant. The maximum of the four row bounds proves <= in (1).

### Proof, simultaneous attainability of the scalar maximum

Each candidate in (1) has a **legal pair of policies** witnessing it: the first-stage term A by a=1/2,a'=1/2-A with b,c unchanged; the AU tail term by a=1/2,b=1/8 and a'=1/2-A,b'=1/8-B (c unchanged); the AV third-atom term by a=1/2,c=7/8 and a'=1/2-A,c'=7/8+C (b unchanged); the BU term by b=1/8,b'=1/8-B with a,c unchanged. The respective event differences are exactly

\[
 A,\quad \frac78 A+\frac12 B+AB,\quad
 \frac78 A+\frac12 C+AC,\quad\frac34 B.
\]

Every witness lies within the stated legal cube because A,B,C<=1/8. Hence the supremum is >= each term and matches the universal bound. When A=B=C=d, the dominant term is 11d/8+d², proving (2).

## Theorem 2 — nonuniform endpoint stability for two Chebyshev radii

Let Q' be **any** real parameter box whose lower and upper endpoint deviations from Q are at most A in the a-coordinate, B in the b-coordinate and C in the c-coordinate. Take 0<=A,B,C<=1/8 and require the perturbed endpoints to stay legal and ordered. Let S_Q=P(Q), let

\[
R_{\rm lawful}(Q)=\min_{z\in S_Q}\sup_{x\in S_Q}D(x,z),
\qquad
R_{\rm hull}(Q)=\min_{z\in\operatorname{conv}(S_Q)}\sup_{x\in S_Q}D(x,z).
\]

Write G(Q)=R_lawful(Q)-R_hull(Q). Then

\[
\boxed{G(Q')\ge G(Q)-4\Omega_Q(A,B,C).} \tag{3}
\]

To prove this, pair corresponding parameters of Q and Q' using identical three independent affine coordinates t_a,t_b,t_c∈[0,1]. Every matched coordinate varies at most the stated endpoint deviation, in both directions. Equation (1) gives d_H(S_Q,S_Q')<=Ω in the joint max-TV norm. Convex hull is nonexpansive for Hausdorff distance: match the same finite convex weights across paired points. For two nonempty compact adversary sets and center sets each within η in Hausdorff distance, their minimax radius differs by at most 2η, by pairing a center and adversary in both directions and applying the triangle inequality. Apply this once to lawful centers and once to hull centers to get (3). The modulus is *exact pointwise*, while this Hausdorff/radius consequence is a **valid upper stability guarantee**, not a claim of optimality for every box Q'.

## Corollary — expanded uniform six-endpoint open region

The independently recorded base-box analytic theorem supplies

\[
R_{\rm hull}(Q)=3/16,\qquad
R_{\rm lawful}(Q)=(\sqrt{43}-5)/8,
\qquad
G(Q)=(2\sqrt{43}-13)/16.
\]

For every real six-endpoint box Q' at coordinatewise endpoint distance at most d<=1/800 from Q,

\[
\boxed{G(Q')\ge
 \frac{2\sqrt{43}-13}{16}
 -\frac{11}{2}d-4d^2
 >\frac{1}{4000}>0.}\tag{4}
\]

The strict lower inequality in (4) is valid uniformly on 0<=d<=1/800. Indeed at d=1/800 the modulus is exactly 1101/640000 and the correction is 1101/160000. The proposed positive margin >1/4000 is equivalent to

\[
\sqrt{43}>\frac{131141}{20000},
\]
whose *strict* exact rational certificate is
\[
43-(131141/20000)^2=2038119/400000000>0.
\]

The previous open region with d<=1/1024 is now enlarged to d<=1/800 (approximately 28% larger permitted displacement in each of the six endpoints), while the certified uniform positive margin improves from >1/2560 at the old boundary to >1/4000 at the larger boundary. At the same original d=1/1024, the improved theorem gives the stronger explicit algebraic bound G(Q')>=G(Q)-4(11d/8+d²). These are guarantees for **all real boxes** in the specified region.

For anisotropic endpoint budgets there is a direct consequence without choosing a common d: positivity is guaranteed whenever 4Ω_Q(A,B,C)<(2√43-13)/16. This permits larger changes in individual controls when the others move less; it does not claim that the known sufficient region is maximal.

## Verification, source and scope

VERIFY.js is the actually executed exact BigInt program (rational arithmetic plus the ordered quadratic field Q(√43)). It computes all six BRC source laws and mixing rows, checks the four-policy hull witness against eight base vertices, checks the explicit radical lawful-center polynomial and eight-vertex upper certificate, the three saturated event equalities, the four types of sharp modulus witness, 2,916 exact strategy-pair comparisons on selected grids, and the positive rational-square certificate above. The real-parameter results rely on the displayed analytical bounds, an exact extremal witness and multiaffine/coordinatewise convex vertex reasoning; the finite grid is a check of implementation and constants, **not a proof of continuity or universal optimality**.

BRC usage: all six positive branch identities and the joint observation map are preserved through probability mixing; only the declared total-variation observer merges equal stop atoms in this frozen slice. No claim is made for arbitrary future observers or operations. This is an exact finite BRC/S23 statistical model, not a result about native P000 six-axis Cell geometry, its independent time, a full three-dimensional research slice, or the general eleven-control ten-label minimax problem. Frozen scientific inputs have not been updated; full minimax bounds remain [1/2,2/3] for k=4,6. This is author-side evidence awaiting applicable native owner, Result and independent review authority.
