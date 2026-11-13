# R5 — fixed-seven-arc transfer support has an exact 3-or-7 dichotomy

- Research date: 2026-11-11 (Asia/Shanghai).
- Classification: author-side exact mathematical result; independent review and Source Result admission pending.
- Frozen scientific pins (unchanged): GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`.
- Predecessor: PR #1976 (complete lawful seven-arc polygon), PR #1990 (one 7→3 bridge), PR #2002 (seven-functional optimal center). Parallel later PR #2008 concerns observation-score recovery, not this support classification.

## Mathematical setting

Use the original seven-likelihood-ratio P/Q–BRC Blackwell *auxiliary observer* with ratios
[
(r_0,dots,r_6)=(1/10,1/2,3/4,1,5/4,3/2,19/10).
]
Keep the original 14 physical parameters, five affine physical equalities, all 26 nonnegative capacity slacks and the 21 original marginal/martingale Blackwell equalities. The exact source/target mass map, time map, physical constraints and 21-row coupling operator are implemented without numerical approximations in `VERIFY_E7_RIGIDITY.py`.

Consider any nonnegative coupling whose support is contained in the seven permitted arcs, **in this exact order**:
[
E_7=((0,0),(3,3),(4,3),(4,5),(6,5),(6,6),(0,3)).
]
Let (oldsymbol e=(e_{00},e_{33},e_{43},e_{45},e_{65},e_{66},e_{03})), let (u=e_{66}), and let (w=e_{43}).

## Theorem (complete support-size dichotomy on the E7 face)

For **every** physically lawful source/target parameter pair and every nonnegative Blackwell coupling supported on (E_7), the seven masses necessarily satisfy the exact identities
[
oxed{oldsymbol e=
left(u+rac{13}{9}w, 
1-2u-rac{479}{90}w, 
w, rac85 w, w, u, rac5{18}wight).}
]
Moreover, the three diagonal masses obey the universal positive bounds
[
oxed{
e_{00}gerac{5964292503}{31998447800},quad
e_{33}gerac{6493976683}{23998835850},quad
e_{66}gerac{105459003}{31998447800}.}
]
Consequently the number of strictly positive masses is **exactly 3 when (w=0)**, and **exactly 7 when (w>0)**. In this fixed-seven-arc lawful face, positive support sizes 4, 5 and 6 are absent.

The statement describes the *displayed coupling's support* on this fixed arc face. It does not assume it is the minimum coupling support among all 30 allowed arcs. The predecessor's seven-edge minimality certificates apply independently to the subset of points for which their stated positivity hypotheses hold.

## Proof

1. Build the full affine system in the 21 unknowns consisting of 14 physical coordinates and the seven displayed coupling masses. Its 26 equations comprise the five physical equalities and the original 21 Blackwell equations. Exact rational row reduction gives (operatorname{rank}M=operatorname{rank}(Mmid b)=18), so the solution affine space has dimension 3.
2. The seven coupling components of every point in this affine space are precisely the boxed two-parameter expression. This is certified by substituting one particular exact solution and every vector of the exact three-dimensional nullspace; see the code's `expected` assertion.
3. The martingale equation at target 3 yields ((r_0-r_3)e_{03}+(r_4-r_3)e_{43}=0), hence (e_{03}=5e_{43}/18). At target 5 it yields ((r_4-r_5)e_{45}+(r_6-r_5)e_{65}=0), hence (e_{45}=8e_{65}/5). The source/target mass equations plus the **two original physical time-matching equalities alone** force (e_{43}=e_{65}): the associated 23-by-21 matrix has exact rank 16, unchanged when the row representing (e_{43}-e_{65}) is appended. This is a stronger source-local statement than the bridge-path calculation.
4. To prove global diagonal positivity, write the full affine solution as (oldsymbol z=Z+Nt), (tinmathbb R^3), with the particular solution and nullspace basis determined by exact Gauss–Jordan elimination. The 26 physical capacities and 7 coupling nonnegativities become 33 inequalities (s=Gt+hge0). The following nonnegative multipliers satisfy (N_j=sum_ilambda_{j,i}G_i) and (Z_j-sum_ilambda_{j,i}h_i=L_j), exactly:

   | diagonal | multiplier map (zero-based row index of the 33 slacks) | proven lower bound (L_j) |
   |---|---|---|
   | (0,0) | 7:258866609/7999611950; 9:6637059773/28798603020; 11:67/162 | 5964292503/31998447800 |
   | (3,3) | 7:10760514869/35998253775; 9:26982033/1599922390; 25:67/81 | 6493976683/23998835850 |
   | (6,6) | 7:40746489481/71996507550; 9:7504029773/28798603020; 11:67/162 | 105459003/31998447800 |

   Therefore (e_j=L_j+sum_ilambda_{j,i}s_ige L_j>0). The program verifies all identities as exact rationals, including each coefficient and each constant.
5. All four offdiagonal masses are positive multiples of the same (wge0). Their simultaneous vanishing/nonvanishing, together with strict positivity of the three diagonal masses, proves the dichotomy.

## Verified witnesses and computation scope

The exact fully physical seven-edge witness (14 physical coordinates, source 7 then target 7) is
[
p=(156235560/159992239,156235560/159992239,156235560/159992239,
105459003/319984478,0,0,0,1,1,54533236/159992239,421433145/1279937912,
37904219/319984478,210515139/1279937912,1/10).
]
Its seven positive arc masses in the specified order are
[
(5964292503/31998447800,1274997718/3999805975,40561155/319984478,32448924/159992239,40561155/319984478,105459003/31998447800,22533975/639968956).
]
The legal three-edge endpoint is obtained by setting both original seven-coordinate physical tuples equal to ((1,1,1,27/80,1/10,27/80,1/10)), with diagonal masses (7933/36000,10067/18000,7933/36000) and other masses zero.

The standalone SymPy/Fraction checker was **actually executed** on the displayed input. It checked all 21 exact Blackwell equations for both witnesses, the five original physical equations, all 26 physical capacity inequalities, the exact affine ranks, the universal coefficient identities, the time-only cross-pair relation and the three nonnegative dual certificates. The raw local stdout is saved in `EXACT_OUTPUT.txt`. Numerical LP was used only to discover the rational witness and candidate certificates; the published mathematical checks use exact rational arithmetic.

## Next question

Classify **other** legal 4-, 5- and 6-edge supports among all 30 permitted edges, particularly supports near the diagonal 3-edge family that are not contained in (E_7). Use the same exact 14-coordinate physical constraints and martingale equations; enumerate or identify orbit classes of candidate supports and certify feasibility or infeasibility. Preserve exact ownership/task admission separately; this author-side result does not assert an R5 formal CLAIM or independent mathematical review.
