# R5 — exact global minimum Blackwell support sizes 4, 5 and 6

Research date: 2026-11-11 (Asia/Shanghai).
Scientific freeze preserved: GLOBAL `a01383f825ef9d43b4b754254303298c64041568` / EM `86149263e38c22292c9def1e0f69092efa1be77e`.
This result uses the original seven-LR P/Q–BRC auxiliary Blackwell observer, 30 allowed arcs, original five physical equalities, 26 capacity inequalities, and 21 marginal/martingale equalities. It is a theorem under the frozen model, not a native X6 dynamical theorem.

## Theorem: exact minimal 4-, 5-, and 6-edge instances exist

Put ((r_0,dots,r_6)=(1/10,1/2,3/4,1,5/4,3/2,19/10)).
Use **identical** source and target physical seven-coordinate states (x=y), in the inherited coordinate order (x=(g,a,b,u,v,w,z)). The following exact rational instances are lawful:

| Instance | Physical state x = y | Positive coupling arcs (each diagonal) | Exact positive masses in support order |
|---|---|---|---|
| FOUR | ((1,1,1,27/80,1/10,1/4,1/10)) | ((0,0),(3,3),(5,5),(6,6)) | (15803/72000, 18797/36000, 7/80, 1367/8000) |
| FIVE | ((1,1,1,1/4,1/10,1/4,1/10)) | ((0,0),(1,1),(3,3),(5,5),(6,6)) | (17/100, 7/80, 97/200, 7/80, 17/100) |
| SIX | ((1,1/2,1,1/10,1/10,1/10,1/20)) | ((0,0),(1,1),(2,2),(3,3),(5,5),(6,6)) | (14789/162000, 3/40, 1/4, 11843/40500, 1/5, 14789/162000) |

For each instance, the listed coupling has the **unique** support allowed by all 30 columns, not merely the smallest among some predetermined arcs. Consequently:
[
oxed{N_{min}(mathrm{FOUR})=4,quad N_{min}(mathrm{FIVE})=5,quad N_{min}(mathrm{SIX})=6.}
]

## Proof of global uniqueness (one exact quadratic separation)

Write (m_i=mu_i=
u_i) for the common source/target seven-likelihood-ratio mass vector. In the original 21-row coupling operator (C), target marginal rows are indexed 0–6, source marginal rows 7–13, and target-indexed source-ratio moment rows 14–20. Define the fixed exact rational row vector
[
Y=(r_0^2,ldots,r_6^2; r_0^2,ldots,r_6^2; -2r_0,ldots,-2r_6).
]
Then for each of the **30 allowed coupling columns** ((i,j)),
[
oxed{Y^T C_{ij}=(r_i-r_j)^2.}
]
The prescribed right-hand side is (q=(m,m,(r_jm_j)_{j=0}^6)), so (Y^Tq=0). Therefore every feasible nonnegative coupling (E) obeys
[
0=Y^TC E=sum_{(i,j)}E_{ij}(r_i-r_j)^2.
]
All summands are nonnegative and the seven (r_i) are pairwise distinct. Hence (E_{ij}=0) whenever (i
e j). The marginal equalities now force (E_{ii}=m_i). Thus any feasible coupling is exactly the displayed diagonal one. This proves *global* uniqueness and the three claimed minimal support counts.

The three proposed rational physical tuples satisfy the original structural equalities (g_x=b_x), (g_y=1), (z_y=a_y/10) and equal source/target time readings (because (x=y)). Each of their 26 physical capacity slacks is nonnegative. Direct substitution into the inherited mass map gives the exact mass vectors in the table (all sum to one; index 4 is zero). Each required diagonal arc is among the original 30 permitted arcs; the diagonal coupling satisfies all 21 Blackwell equations exactly. The standalone checker verifies each of these steps with `Fraction` and `SymPy`, without floating point.

## Relationship to earlier R5 frontier

Earlier PR #1945 provided lawful minimal 3-edge diagonal points; PR #1976 gave an exact minimal 7-edge family. In this milestone the exact minimal 4-, 5- and 6-edge gaps are filled by independent, globally unique lawful diagonal examples. Thus **every minimum support count 3, 4, 5, 6, 7 is realized** in the frozen model.

In the same milestone, companion `../brc_r5_e7_support_rigidity_20261111/RESEARCH.md` proves a different phenomenon: for the particular older E7 support set, *any* physically lawful E7-supported coupling has either 3 or 7 positive masses. The new diagonal 4/5/6 examples use other permitted diagonal arcs outside that fixed E7 set. The two theorems coexist without contradiction.

## Verification record

The attached `VERIFY_DIAGONAL_456.py` was actually executed locally; `EXACT_OUTPUT.txt` contains its full observed stdout. Coverage: 3 fully explicit physical states, 26 nonnegative physical slacks each, 5 physical equalities each, 21 Blackwell equations each, the identity (Y^TC_{ij}=(r_i-r_j)^2) for **all 30 allowed arcs**, exact marginal equality and all displayed positive mass values. Logical uniqueness proof uses the squared-difference identity and nonnegativity and is not a 30-choose-k finite support search.

## Next question

Examine whether 4–6 support instances with **non-diagonal** positive couplings exist, and classify which support changes connect the diagonal 3→4→5→6 strata with the exact 7-edge E7 face. Preserve physical feasibility, provenance and global minimality certificates for any new class. Current author-side proofs await independent mathematical review; no formal R5 task publication/CLAIM or Result admission is asserted.
