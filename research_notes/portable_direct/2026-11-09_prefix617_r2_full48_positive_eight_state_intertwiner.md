# PREFIX-617-R2 — Exact minimal eight-state positive realization of all native 48-phase outputs

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR-SIDE EXACT PROOF / EXECUTED NATIVE-BRC CHECKER / INDEPENDENT REVIEW PENDING.

**Frozen scientific input:** awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Scientific dependencies: PREFIX-613–614 (four-point probe; seven-state rank certificates), PREFIX-615 (1+2+4 splitting), PREFIX-616 (scalar positive minimum eight; commit 7731ba823f6eefa0b4182ed02890400885e2c570). Current normative rules and P000 are read separately; nothing here re-pins scientific input or changes the ACTIVE worldview.

## 1. Exact claim and original native input

Let Q(g) be the **original typed X6 STAR/BRC positive-branch-sum** 48-phase transition at six-axis weights (1,1,1,1,0,0), with nonnegative gate g and original zero-based phase indices. The 96 ports and 576 tagged native actions provide the upstream source; this result concerns their precisely defined 48-phase **sum quotient**. Fix the four-point native input difference

\[
d=e_4+e_{11}+e_{14}+e_{32},\qquad a,b,g_t,\lambda\geq0.
\]

After two chronological gates let \(x_0=\lambda Q(b)Q(a)d\); for each finite gate word \(g_1,\ldots,g_t\), let \(x_t=Q(g_t)\cdots Q(g_1)x_0\).

**Theorem 617:** A fixed 8-state, parameter-affine, entrywise nonnegative linear model reconstructs **all 48 original phase sums** at all future steps for this input family. The minimum real linear dimension is exactly 7 and the minimum nonnegative linear dimension is exactly 8. Thus the extra positive coordinate found in PREFIX-616 suffices for full-48 output, not just scalar phase 3.

## 2. Constructive eight-dimensional invariant cone

Let P be the 4-cycle with \(Pe_j=e_{(j+1)\bmod4}\). Define

\[
C=2P,\quad
B(g)=\begin{pmatrix}0&0&0&4(g+3)\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix},
\quad M_8(g)=\operatorname{diag}(C,B(g)).
\]

Write the state \(z=(c_0,c_1,c_2,c_3,w_0,w_1,w_2,w_3)^T\).
The **fixed nonnegative 48×8 output matrix H** has precisely 24 positive entries, listed exhaustively below (all other coefficients zero):

| column | output phase rows | coefficients |
| --- | --- | --- |
| c0 | 2,3,15 | 1 each |
| c1 | 5,28,29 | 1 each |
| c2 | 27,38,39 | 1 each |
| c3 | 16,17,41 | 1 each |
| w0 | 3,14,15 | 1 each |
| w1 | 17,40,41 | 2 each |
| w2 | 26,27,39 | 4 each |
| w3 | 4; 5,29 | 4; 8 each |

Thus even the 32 phase rows identically zero on this generated family are reconstructed exactly.

Let \(A=Q(0)\), \(D=Q(1)-Q(0)\), \(H=[H_C\ H_B]\) with its first/last four columns. Direct native-STAR integer multiplication proves

\[
AH_C=H_CC,\qquad DH_C=0,
\]
\[
AH_B=H_BB(0),\qquad DH_B=H_B(B(1)-B(0)).
\]

Since \(Q(g)=A+gD\) and \(B(g)=B(0)+g(B(1)-B(0))\), we obtain the **symbolic all-gate intertwiner**

\[
\boxed{Q(g)H=HM_8(g)}.
\]

Row reduction gives \(\operatorname{rank}H=8\). Both H and \(M_8(g)\) are entrywise nonnegative for \(g\geq0\). Hence \(H\mathbb{R}_{\geq0}^8\) is an 8-dimensional **invariant positive cone embedded in the native 48-phase space**.

Define the nonnegative initialized state

\[
u_8(a,b,\lambda)=\lambda(0,0,4,4,\ 3+b,3+a,1,\tfrac12)^T.
\]

Another symbolic identity over the independent parameters \(a,b,\lambda\) is

\[
\boxed{Hu_8(a,b,\lambda)=\lambda Q(b)Q(a)d}.
\]

Induction by the intertwiner yields the promised full-output formula:

\[
\boxed{
x_t=HM_8(g_t)\cdots M_8(g_1)u_8(a,b,\lambda)
=\lambda Q(g_t)\cdots Q(g_1)Q(b)Q(a)d
}
\]

for every finite nonnegative gate word. No per-observer tuning is used: **one H reproduces every phase simultaneously**.

## 3. Exact minimum and the hidden positive coordinate

To certify the signed lower bound, rebuild the seven native columns

\[
E=[A^2d,\ DAd,\ ADd,\ A^3d,\ A^2Dd,\ A^4d,\ A^3Dd].
\]

The original row minor at (2,3,4,5,16,17,26) is \(-16384\). The stages of the gate-word reachable span have ranks \(3,5,7\); A and D preserve \(\operatorname{im}E\). Therefore this family has real linear dimension exactly 7 under full 48-phase observation.

For the nonnegative lower bound, the existing phase-3 observation is a component of the full output. Its seven-dimensional word-observability minor equals \(-2097152\) and its gate-zero matrix \(T_0\) satisfies \(\operatorname{tr}(T_0^2)=-4\). A hypothetical seven-state positive realization of the same full family would also be a minimal realization of the phase-3 word series, therefore similar to \(T_0\). However every entrywise nonnegative square matrix M has \(\operatorname{tr}(M^2)=\sum_{ij}M_{ij}M_{ji}\geq0\). Contradiction. Together with the explicit eight-state construction,

\[
\boxed{d_{\mathrm{linear}}^{\mathrm{full48}}=7,\qquad d_{\mathrm{nonnegative}}^{\mathrm{full48}}=8}.
\]

This minimum is for fixed finite-dimensional **linear** realizations representing the entire declared family and every future gate word.

The geometric reason for the gap is equally exact. Put \(\ell=(-1,1,-1,1,0,0,0,0)\); then

\[
\boxed{\ell M_8(g)=-2\ell,\qquad \ell u_8(a,b,\lambda)=0}.
\]

All initialized trajectories therefore occupy the invariant 7-dimensional hyperplane \(-c_0+c_1-c_2+c_3=0\) inside the 8-dimensional positive lift. The missing positive coordinate corresponds to an unexcited -2 cycle eigenmode, while H itself has full column rank 8.

## 4. Independent native-BRC exact computation

Standalone checker: PREFIX617_R2_full48_positive_eight_state_checker.py. It constructs the original STAR phase enumeration, branch transitions and 48×48 Q(g) from the frozen native formula, then checks both symbolic identities, the hyperplane, positive coefficients, rank, original signed rank and trace-square certificates.

The executed tests comprise 48 distinct combinations of initial gates, subsequent nonnegative integer/rational gate words (including zeros) and nonnegative scales. They produced **540 complete native 48-phase states**, **25,920 exact phase-coordinate equalities**, **30,240 nonnegativity checks**, and a maximum numerator/denominator bit length of 21. All exact assertions passed. The universal theorem is established by the displayed symbolic identities, not by finite-test extrapolation.

Evidence: PREFIX617_R2_full48_positive_eight_state_checker.py and PREFIX617_R2_native48_positive_eight_state_results.json. Arithmetic follows the actual native positive-branch BRC phase-sum operator; no pi, trigonometric approximation, Taylor series, matrix exponential or floating-point fallback.

## 5. Next mathematical question

Construct a typed native 96-port/tagged-path observer and test whether its future operations preserve the quotient implemented by H. If they do, expose a verified adapter. If not, construct two original 96-port inputs with equal 48 phase sums whose allowed future port operations separate them; then characterize the minimum additional provenance-sensitive coordinates. Separately benchmark full input preparation, bit complexity, 8-entry gate updates, 24-coefficient output recovery and verification against signed 7-state and native 48-phase implementations.

Author-side proof and exact computation are complete. Independent Driver review, Native Result, and any Foundation promotion retain their separate authority requirements.
