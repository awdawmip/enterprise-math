# X6 R120 — A four-dimensional dual-cone, two-witness theorem for the strict 3/2 BRC direction atlas

Date: 2026-11-23. Mathematical status: **AUTHOR_PROOF / EXACT_RATIONAL_SPOT_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED**. Model: same *conditional* four-positive-weight all-six-pair integer BRC observer and moment inverse as R118–R119; unchanged P000/worldview, no asserted native time/physical transfer.

Let (w=(A,B,C,D)>0), (U=A+B), (T=A+C), (Y=B+D).
For the six-pair score (F_w(a)), Port (q(a)), optimum (\eta_p) and strict (3/2) near set (N_p), use the exact definitions from [R119](2026-11-23_r2_x6_r119_two_witness_full_d_fan.md).
The integral heights and gap coordinates are
\[
h=(0,t,3m,t+6n),\quad m\equiv n\pmod2,
\]
\[
g=(|t|,3|m|,|t+6n|,|3m-t|,6|n|,|t+6n-3m|).
\]

## Theorem — two sufficient, homogeneous four-weight cones

Define the *first-witness* cone
\[
\boxed{\mathcal C_{\rm AB}:\quad Y\le6U,\quad T\le6U,\quad C\ge A,\quad D\ge B.}\tag{C1}
\]
Define the *second-witness* cone by R118's hypotheses
\[
\boxed{\mathcal C_{\rm BD}:\quad Y\ge6U,\quad Y\ge T,\quad Y\le2T,\quad
Y\le A+D,\quad Y\le2(B+C),\quad Y\le2(C+D).}\tag{C2}
\]
All coordinates are strictly positive, while the displayed inequalities allow equality.

For **every real weight in either cone** and **every integer (p\ge11)**,
\[
\boxed{
\eta_p(w)=
\begin{cases}
1/U,&w\in\mathcal C_{\rm AB},\\
6/Y,&w\in\mathcal C_{\rm BD}.
\end{cases}}\tag{1}
\]
Both formulas agree if both cones apply, because their inequalities force (Y=6U).

Furthermore, throughout this *entire union* of positive-weight cones, the complete strict (3/2) near set in the **unbounded integer lattice** is a subset of the **same ten unoriented moment directions** from R118/R119:
\[
\begin{gathered}
(0,1,-1),(0,1,1),(0,2,0),\\
(1,-2,0),(1,0,0),(1,2,0),\\
(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1).
\end{gathered}\tag{2}
\]
The moment inverse and exact Port thresholds (17,10,27,38,11,16,21,28,6,1) are unchanged. A row belongs to (N_p) **if and only if** its Port is (le p) and it meets all six pairwise strict affine tests:
\[
\boxed{
\begin{cases}
2U\,g_{ij}<3(w_i+w_j),& w\in\mathcal C_{\rm AB},\\
Y\,g_{ij}<9(w_i+w_j),& w\in\mathcal C_{\rm BD}.
\end{cases}}\tag{3}
\]
Thus these two homogeneous positive-weight cones admit an **exact finite rational polyhedral fan** for all Port values (p\ge11). This is a sufficient region, not a maximality assertion.

## Proof (all real weights, all integer directions)

The integral moment transform and parity are exact. For any nonzero integer triple, there are three exhaustive cases:

1. (t\ne0): the AB observation gives (F_w\ge1/U).
2. (t=0,n\ne0): the BD observation gives (F_w\ge6/Y).
3. (t=n=0): parity forces a nonzero even (m), and AC gives (F_w\ge6/T).

Hence the global lower bound is (F_w\ge\min\{1/U,6/Y,6/T\}).

On (C1), (Y\le6U) and (T\le6U) give (6/Y\ge1/U) and (6/T\ge1/U), so (F_w\ge1/U). The integral direction (a=(10,-5,1)), moment ((1,0,0)), Port 11, has heights ((0,1,0,1)). Its nonzero scores are
\[
1/U,\quad1/(A+D),\quad1/(B+C),\quad1/(C+D).
\]
The two inequalities (D\ge B), (C\ge A) ensure all three latter denominators are at least (U); therefore its score is precisely (1/U). This proves the first branch of (1).

On (C2), (Y\ge6U) and (Y\ge T) ensure (1/U\ge6/Y) and (6/T\ge6/Y), so (F_w\ge6/Y). The integral moment ((0,1,1)), vector ((-9,5,-1)), Port 10, has heights ((0,0,3,6)). Its nonzero gaps are AC=3, AD=6, BC=3, BD=6, CD=3. The four upper inequalities in (C2) imply all five ratios are (le6/Y), with equality at BD. This proves the second branch.

For **(C1)**, strict nearness (F_w<3/(2U)), applied to AB, AC and BD, gives
\[
|t|<3/2,\quad |m|<T/(2U)\le3,\quad|n|<Y/(4U)\le3/2.
\]
For **(C2)**, strict nearness (F_w<9/Y) gives instead
\[
|t|<9U/Y\le3/2,\quad |m|<3T/Y\le3,\quad|n|<3/2.
\]
In both cases, integrality yields (|t|\le1, |m|\le2, |n|\le1). With (m\equiv n\pmod2), removal of zero and global sign quotient, there are exactly three candidate rows at (t=0), seven at (t=1), namely (2). Each passes the strict-near definition exactly when (3) and its known Port condition hold. This proves the complete atlas and the unbounded-Port claim. QED.

## Relation to established results and checks

- (C2) **recovers R118 (H)**, with its exact optimum and ten-row bank. (C1) is a new four-dimensional sufficient region on the other side of (Y=6U), avoiding any requirement that the second witness be optimal there. The union strictly extends the original R118 domain.
- The entire R119 section (w_D=(11,1,60,D)), (1\le D\le121), belongs to (C1) for (D\le71) and to (C2) for (D\ge71). Its six count phases and Port atlas remain available in R119.
- Exact integer replay through Port 38 independently tested (w=(3,2,5,7)\in\mathcal C_{\rm AB}\setminus\mathcal C_{\rm BD}) (near count 1, optimum 1/5), (w=(7,1,27,50)\in\mathcal C_{\rm BD}\setminus\mathcal C_{\rm AB}) (near count 7, optimum 2/17), and (w=(11,1,60,71)) in their intersection (near count 10, optimum 1/12). For each sample all **95,133** unoriented nonzero vectors of Port≤38 were checked against the analytic optimum and ten-row bank; no sub-optimal counterexample or outsider was found. Finite tests corroborate the algebraic proof; independent review is pending.

**Next problem:** determine whether either sufficient cone can be further enlarged by replacing its present short witness with a new one, or derive a global near-direction maximum that uses the two-witness arrangement without assuming either cone's specific inequalities. Preserve the original native X6/R063 program separately.
