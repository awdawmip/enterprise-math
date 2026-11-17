# R5: true Y→L likelihood-ratio merger, time-image equality and four-dimensional obstruction

**2026-10-31 (Asia/Shanghai) · AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** This is an auxiliary finite stopping model, not a theorem about native X6 geometry or physical time.

## Sources and scope

GLOBAL_KNOWLEDGE_V1 main@b8580a47728dd9e0df47d938c35c1656bf839ad3; Enterprise Math main@dae896eec630511ed988677bd6b4f134e02a45c7. Read current global bootstrap/manual, P000, ACTIVE worldview, Heartbeat X6, joint-observer/BRC constraints, and portable research protocol at these pins. Previous R5 scientific frontier: 115b2fdb0b652e10648400e95a868028913d4fc9, research_notes/brc_r5_two_parameter_time_rigidity_rotated_gap_20261031_t0943/RESEARCH.md (author-checked, not admitted). Question: does a *genuine downstream chance merger* from Y into the same L likelihood-ratio STOP/CONTINUE state preserve time-hull equality while yielding four-dimensional nonconvexity and ultimately equal four-dimensional hulls?

## Strictly positive two-measure path model

At t=1, labelled origins A0,A1,B,C0,C1 carry Q masses (1/8,1/8,1/4,1/4,1/4) and P masses (1/4,1/4,1/4,1/8,1/8). B,C0,C1 stop at t=1. Each A_i may stop at t=1 or continue with probability x_i. On continuing, its strictly positive Q kernel on Y,L,M,H is
K_Q=(y,l,1-2y-3l/2,y+l/2) with real y,l>0, 2y+3l/2<1; P kernel is (y/2,3l/4,1-2y-3l/2,3(y+l/2)/2). Thus absolute likelihood ratios Y,L,M,H are (1,3/2,2,3) and both kernels normalize.

Y at t=2 may stop or continue with u_i to t=3. If it continues, a genuine natural transition sends Q to L/M_Y with probabilities 1/2,1/2 and P with probabilities 3/4,1/4; reached absolute likelihood ratios are 3/2,1/2. Direct L from A and the Y→L path **merge at the same t=3 likelihood-ratio L state (3/2)**. At L, stopping yields t=3 and continuing yields t=4; other non-Y M,H routes terminate at t=3, and Y→M_Y terminates at t=3. FULL can use separate x_i,u_i,v_i^direct,v_i^via-Y for each A history; seedless LR shares x,u,v across equal time/likelihood-ratio states, in particular one v for both L histories. No persistent seed.

Terminal error rate is eta_lo=1/8 on every path except Y→M_Y at t=3 and Y→L at t=4 when L continues, where it is eta_hi=7/8. The history-sensitive observer is not constant on the L provenance fiber. Both error rates are strictly interior. Observation vector O=(e_P,e_Q,T_P,T_Q) records expected error and stopping time under P/Q. Retain all labelled paths until the prescribed observer is evaluated (typed positive-weight BRC provenance).

## Exact four-observer map and full rank

For seedless LR let p=(x,xu,xv,xuv) and O=b+Mp, where b=(1/8,1/8,1,1) and at the rational example y=1/8,l=1/4 (Q kernel 1/8,1/4,3/8,1/4; P kernel 1/16,3/16,3/8,3/8):

\[
M=\begin{pmatrix}
0&3/512&0&9/512\\
0&3/256&0&3/256\\
31/32&1/32&3/32&3/128\\
15/32&1/32&1/16&1/64
\end{pmatrix}.
\]

More generally put k=eta_hi-eta_lo>0. Four columns are
A=(0,0,1-y/4,1/2-y/4),
B=(ky/16,ky/8,y/4,y/4),
C=(0,0,3l/8,l/4),
D=(3ky/16,ky/8,3y/16,y/8).
Direct determinant expansion gives
\[
\boxed{\det M=k^2 l y^2(y+2)/2048>0}.
\]
At rational instance k=3/4, det M=153/67108864. Five LR deterministic outputs corresponding to p=(0,0,0,0), (1,0,0,0), (1,1,0,0), (1,0,1,0), (1,1,1,1) span affine dimension four. FULL also has rank four.

## Theorem A — equality of entire real two-time images

For arbitrary FULL real policies define X=(x0+x1)/2, U=(x0*u0+x1*u1)/2, VD=(x0*vD0+x1*vD1)/2, VY=(x0*u0*vY0+x1*u1*vY1)/2, and kappa=y/(2l)>0. The last two observation coordinates satisfy
\[
(T_P,T_Q)=(1,1)+A_T X+B_T U+C_T W,\qquad W=VD+\kappa VY,
\]
because D_T=kappa C_T. Their exact feasible domain is
\[
0\le U\le X\le1,\qquad 0\le W\le X+\kappa U.
\]
Every FULL policy meets the inequalities. Conversely, every triple in this polytope is obtained by seedless LR policy x=X, u=U/X if X>0 (else 0), v=W/(X+kappa U) if denominator is nonzero (else 0). Hence, **for every admissible real y,l, FULL and LR have equal actual two-time images**, not merely equal convex hulls. This is a scope-typed observer projection; it is not safe to discard the fiber for error observation or future L decision.

## Theorem B — four-dimensional convex hulls unequal, although LR image nonconvex

At the rational example use integer support direction J=(42,107,45,-93). Direct multiplication yields
\[
JM=(0,0,-51/32,51/32),\qquad Jb=-235/8.
\]
LR has xuv<=xv, so max_LR(J·O)=-235/8. FULL may choose every x_i=u_i=v_i^via-Y=1 and v_i^direct=0, attaining FULL maximum (each normalized difference x_i u_i v_i^via-Y-x_i v_i^direct<=1):
\[
\boxed{\max_{FULL}J\cdot O=-889/32,\quad\max_{LR}J\cdot O=-235/8,\quad \Delta_J=51/32>0}.
\]
Thus the genuine merger does not solve the equal-four-dimensional-hulls mother question.

Separately, seedless LR's real four-observer image is **nonconvex**. LR policies (x,u,v)=(1,0,0) and (1,1,1) have a midpoint that FULL realizes by assigning the first policy to A0 and the second to A1:
\[
\boxed{O_*=(35/256,35/256,523/256,195/128)}.
\]
The invertible affine map uniquely assigns it monomials p_*=(1,1/2,1/2,1/2). Every LR real policy satisfies p1*p4=p2*p3, while p_* violates it by exactly 1/4. The exact inverse matrix has induced infinity norm 13024/51; residual polynomial is 4-Lipschitz in infinity norm on [0,1]^4. Therefore
\[
\boxed{\operatorname{dist}_\infty(O_*,\mathcal O_{LR})\ge51/208384>0}.
\]
The witness lies in FULL actual image and LR convex hull but outside LR actual image. Nevertheless, full four-dimensional hulls differ by the support gap above.

## Calculation, limits and next problem

Sibling VERIFY.py performs direct path-by-path fractions.Fraction enumeration of 256 FULL and 8 LR deterministic policies; checks P/Q normalization and strict chance positivity, observer matrix/determinant, support maxima, FULL midpoint, explicit LR time reconstruction for all 256 FULL deterministic policies, inverse-norm certificate and positive real-policy distance bound. EXACT_OUTPUT.txt records actual executed output ending PASS_EXACT_R5_YL_PATH_SENSITIVE_ERROR_HULL_OBSTRUCTION. All-real statements follow symbolic identities above; finite enumeration checks a fixed rational instance. No Lean proof, independent review or native Source Result.

**Increment:** A true Y→L natural transition makes equality of the *entire real two-time images* possible with strictly positive P/Q paths and four-dimensional LR rank. The history-sensitive terminal-error probe creates an exact four-dimensional convex-hull obstruction.

**Next unit:** Change the direct/indirect L response rays (or insert another genuinely interacting downstream chance state) to align them in every signed four-observer support direction while retaining rank four. Test each FULL deterministic four-vector with rational Carathéodory certificates or an exact Farkas separator; only after full hull equality, analyze real seedless-image nonmembership. If full Markov sufficiency forces convex occupation-measure image, prove that no-go before parameter search.

**Authority:** Native service returned research_authority_granted=false, executor_binding_configured=false; owner inventory returned CONTROL_QUOTA; control remains CODE_REVIEW_REQUIRED. Authored note does not represent a native CLAIM, owner assignment, Result, review or admitted theorem.
