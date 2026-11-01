# BRC N=4 / S23: unique exact Chebyshev policy anchor on the full 11-control box

**Date:** 2026-11-01. **Classification:** AUTHOR_ANALYTIC_PROOF + EXECUTED_EXACT_INTEGER_CHECK; **UNREVIEWED / NOT_ADMITTED**. This is a finite six-source statistical/observer experiment; no native P000 X6/independent-time dynamics claim.

## Frozen model and relation to previous frontier

Source frontier: PR #1765, \`research_notes/brc_n4_s23_local_exact_box_geometry_20261101_research1/PROOF.md\` at commit \`cbf1b28ec5a33bc2763aa8d5c02a4cb1b02337da\`. Retain its six labelled sources, 11 causal controls
\`theta=(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)\`,
source-index maps
\`A=(0,0,0,1,1,1)\`, \`B=(2,2,3,2,2,4)\`, \`C=(5,6,7,8,9,10)\`,
and four-stop law
\[
F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
\]
The six prepared laws are \(p_i(\theta)=\sum_{x=0}^5 M_{ix}F(\theta_{A_x},\theta_{B_x},\theta_{C_x})\), where
\[
20M=\begin{pmatrix}
10&10&0&0&0&0\\
9&11&0&0&0&0\\
0&0&20&0&0&0\\
0&0&0&10&10&0\\
0&0&0&2&18&0\\
0&0&0&0&0&20
\end{pmatrix}.
\]
The same nonnegative BRC observer weights preserve all six source identities. Readout distance is \(d(P(\theta),P(z))=\max_{0\le i<6}\operatorname{TV}(p_i(\theta),p_i(z))\). The prior exact local-box theorem already proves that, for fixed \(z\), the supremum over a box occurs at a vertex. Our new result **optimizes the anchor itself** and proves uniqueness.

## Theorem A: exact full-box Chebyshev radius, even against unconstrained centres

Let \(Q=[0,1]^{11}\), and \(r_Q(z)=\sup_{\theta\in Q}d(P(\theta),P(z))\). Define also an unconstrained prepared-row centre \(q=(q_i)_{i=0}^5\in(\Delta_4)^6\), with radius \(r_Q^{free}(q)=\sup_{\theta\in Q}\max_i\operatorname{TV}(p_i(\theta),q_i)\). Then
\[
\boxed{\min_{z\in Q}r_Q(z)=\min_{q\in(\Delta_4)^6}r_Q^{free}(q)=3/4.}
\]
The unconstrained centre is uniquely \(q_i=(1/4,1/4,1/4,1/4)\) in **every** row, and the realizing **policy anchor is also unique**:
\[
\boxed{z_*=(1/4,1/4,1/3,1/3,1/3;\;1/2,1/2,1/2,1/2,1/2,1/2).}
\]
In contrast, the coordinatewise midpoint \(z_{mid}=(1/2)^{11}\) has exact radius \(7/8\).

**Proof, lower bound and free uniqueness.** The four global strategies
(i) \(a_A=a_B=1\);
(ii) \(a_A=a_B=0,b_U=b_{AV}=b_{BV}=1\);
(iii) all \(a\)'s and \(b\)'s zero, all six \(c\)'s one;
(iv) all controls zero
produce, respectively, \(p_i=e_1,e_2,e_3,e_4\) **simultaneously for all six rows**. For any candidate free row \(q_i\), \(\operatorname{TV}(e_j,q_i)=1-q_{ij}\). Radius at most \(3/4\) forces \(q_{ij}\ge1/4\) for each of the four j, hence equality throughout. Conversely a uniform \(q_i\) has TV at most \(3/4\) to every four-stop distribution (by convexity or \(\operatorname{TV}(p,u)\le\max_j \operatorname{TV}(e_j,u)=3/4\)). Thus \(3/4\) is optimal and each free row centre is uniquely uniform.

**Proof, policy existence.** With the displayed \(z_*\), each latent source receives the parameters \((a,b,c)=(1/4,1/3,1/2)\), so \(F=(1/4,1/4,1/4,1/4)\). Every prepared row is therefore uniform, proving the policy upper bound.

**Proof, uniqueness of the policy.** Any optimal policy anchor must yield uniform prepared rows, as just shown. The pure AV prepared row \(i=2\) forces \(a_A=1/4\), \(b_{AV}=1/3\), \(c_{AV}=1/2\). The pure BV row \(i=5\) forces \(a_B=1/4\), \(b_{BV}=1/3\), \(c_{BV}=1/2\). In the AU rows \(i=0,1\), stop-2 mass \((1-a_A)b_U=1/4\) forces \(b_U=1/3\). The AU stop-3 masses then give
\((c_{AU0}+c_{AU1})/2=1/2\) and \((9c_{AU0}+11c_{AU1})/20=1/2\); the nonzero determinant forces \(c_{AU0}=c_{AU1}=1/2\). Analogously BU rows \(i=3,4\) give
\((c_{BU0}+c_{BU1})/2=1/2\) and \((2c_{BU0}+18c_{BU1})/20=1/2\), hence \(c_{BU0}=c_{BU1}=1/2\). All 11 controls are fixed. QED.

**Midpoint calculation.** At \(z_{mid}\), every row equals \(F(1/2,1/2,1/2)=(1/2,1/4,1/8,1/8)\). The maximal TV to any prepared row is \(\max_j(1-q_j)=7/8\), attained by the globally feasible \(e_3\) or \(e_4\). Thus the midpoint gives an avoidable \(1/8\) excess in this global-box radius.

## Theorem B: exact unique anchor on a two-control legal face

Let \(Q_2\) fix all controls to zero except \(s=a_A,t=b_U\in[0,1]\). With the same prepared-law distance, but the supremum and anchor restricted to this face,
\[
\boxed{\min_{z\in Q_2} r_{Q_2}(z)=2/3},
\qquad \boxed{z_{2,*}:\ s=1/3,\ t=1/2}.
\]
The optimum is unique. The face's coordinate midpoint \(s=t=1/2\) has exact radius \(3/4\), while its full diameter is \(1\).

**Proof.** On rows \(i=0,1\), both AU sources have the same four-stop law
\(F(s,t,0)=(s,(1-s)t,0,(1-s)(1-t))\). Its image is the entire triangular probability simplex on stops \(1,2,4\), including all three atoms \(e_1,e_2,e_4\). Any anchor with radius at most \(2/3\) must assign each of those three stops at least \(1/3\), hence must equal \((1/3,1/3,0,1/3)\). The unique corresponding parameters are \(s=1/3,t=1/2\). At this policy, prepared rows \(0,1\) have radius \(2/3\); row 2 varies over \(\operatorname{conv}\{e_1,e_4\}\) around \((1/3,0,0,2/3)\), giving radius \(2/3\); rows 3,4 vary over \(\operatorname{conv}\{e_2,e_4\}\) around \((0,1/2,0,1/2)\), giving radius \(1/2\); row 5 stays \(e_4\), giving radius zero. Thus the claimed optimum is attained. At \(s=t=1/2\), rows 0,1 have centre \((1/2,1/4,0,1/4)\), whose farthest atom has TV \(3/4\); the remaining rows are at most \(1/2\). The face diameter is one because its row 0 attains \(e_1,e_2\). QED.

## Consequences, BRC scope and evidence

This proves that a coordinate midpoint is **not** generally a minimax anchor for the earlier exact local-TV-radius certificates; indeed \(r_{Q_2}(z_{2,*})=2/3>\Delta(Q_2)/2=1/2\), so replacing radius by half the diameter is also invalid. The explicit optimal anchors can be used for branch-and-bound when a box contains this face or when full-box baseline selection matters. The paired non-identical AU and BU source-mixture observers make the full policy anchor identifiable; merging those prepared rows would not justify the same uniqueness conclusion. No six-source provenance erasure or P000 transfer is implied.

\`VERIFY.js\` performs exact integer arithmetic with 24-tick control inputs and common prepared-law denominator 480. It evaluates all \(2^{11}=2048\) binary full-box vertices for both full anchors, all four two-control face vertices for both face anchors, and the four global/three face atom constructions. All checked row maxima are recorded in \`RUN_EVIDENCE.json\`. The extension from vertices to **all real** policies and the optimality/uniqueness statements rely on the analytical arguments above and the prior exact multi-affine vertex theorem, not on finite tests. The already-published ten-label minimax interval \(1/2\le R_{\rm beh}(k,10)\le2/3\) for \(k=4,6\) is not changed; the present problem is the one-anchor *prepared-law geometry*, not ten-label bank optimization.

**Admissibility:** AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED. Native owner/CLAIM, independent review and foundation admission are separate. P000 native six-axis Cell, independent time, observer/future-operation preservation and S2 causal-transfer obligations remain open.
