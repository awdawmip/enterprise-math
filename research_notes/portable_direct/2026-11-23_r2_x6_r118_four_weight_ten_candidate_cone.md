# X6 R118 — Four-weight exact ten-candidate cone and a five-phase parameter fan

Date: 2026-11-23 (Asia/Shanghai). **AUTHOR_PROOF / EXACT_INTEGER_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED**.
Model: the R90–R117 *conditional* four-positive-weight, all-six-pair BRC observer, with unchanged scientific inputs and P000. This is a static integer-observer theorem, not a claim about native X6 temporal evolution.

## Definitions and coordinates

For nonzero integer \(a=(x,y,z)\), define \(q(a)=\max(\sum_i\max(a_i,0),\sum_i\max(-a_i,0))\),
\(h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)\),
\(F_w(a)=\max_{i<j}|h_i-h_j|/(w_i+w_j)\) for positive \(w=(A,B,C,D)\),
\(\eta_p=\min_{0<q(a)\le p}F_w(a)\), and
\(N_p=\{\{\pm a\}:q(a)\le p,F_w(a)<3\eta_p/2\}\).
Use integral moments \((t,m,n)\) with \(m\equiv n\pmod 2\):
\[
h=(0,t,3m,t+6n),\quad
a=(10t-12m+3n,\ -5t+7m-2n,\ t+(n-3m)/2).
\]
All six pair scores are retained. Put \(Y=B+D\).

## Theorem 1 — Exact four-weight cone

For \(A,B,C,D>0\), assume the homogeneous closed conditions
\[
\boxed{
Y\ge6(A+B),\quad Y\ge A+C,\quad
Y\le2(A+C),\quad Y\le A+D,\quad
Y\le2(B+C),\quad Y\le2(C+D).
}\tag{H}
\]
For **every integer \(p\ge10\)**,
\[
\boxed{\eta_p=6/Y.}\tag{1}
\]
Every strict near direction in the unbounded integer lattice belongs to the following ten-row bank. The **complete** near set at any \(p\ge10\) is exactly the rows with \(q\le p\) and all six strict affine slacks
\[
\boxed{S_{ij}(a;w)=9(w_i+w_j)-Y|h_i-h_j|>0\qquad(i<j).}\tag{2}
\]
Consequently the weight-dependence of the complete Port atlas on (H) is a finite hyperplane arrangement with rational polyhedral relatively open cells, not a numerical sampling assertion.

| Integral moments \((t,m,n)\) | Original \(a=(x,y,z)\) | Minimal Port | Gaps AB, AC, AD, BC, BD, CD |
|---|---|---:|---|
| (0,1,-1) | (-15,9,-2) | 17 | 0,3,6,3,6,9 |
| (0,1,1) | (-9,5,-1) | 10 | 0,3,6,3,6,3 |
| (0,2,0) | (-24,14,-3) | 27 | 0,6,0,6,0,6 |
| (1,-2,0) | (34,-19,4) | 38 | 1,6,1,7,0,7 |
| (1,0,0) | (10,-5,1) | 11 | 1,0,1,1,0,1 |
| (1,2,0) | (-14,9,-2) | 16 | 1,6,1,5,0,5 |
| (1,-1,-1) | (19,-10,2) | 21 | 1,3,5,4,6,2 |
| (1,-1,1) | (25,-14,3) | 28 | 1,3,7,4,6,10 |
| (1,1,-1) | (-5,4,-1) | 6 | 1,3,5,2,6,8 |
| (1,1,1) | (1,0,0) | 1 | 1,3,7,2,6,4 |

### Proof, including every Port and boundary weight

If \(t\ne0\), the AB observation is at least \(1/(A+B)\ge6/Y\). If \(t=0,n\ne0\), the BD observation is at least \(6|n|/Y\ge6/Y\). If \(t=n=0\), parity makes \(m\) even, so nonzero \(m\) contributes at least \(6/(A+C)\ge6/Y\) through AC. This establishes the *global* lower bound over all nonzero integer vectors. For \((t,m,n)=(0,1,1)\), the heights are \((0,0,3,6)\), Port is 10, and BD attains \(6/Y\). Its other five pair scores are bounded by \(6/Y\) using precisely the four upper inequalities in (H). This proves (1).

If a direction is strictly near, \(F_w(a)<9/Y\). AB gives \(|t|<9(A+B)/Y\le3/2\), hence \(|t|\le1\). AC gives \(|m|<3(A+C)/Y\le3\), hence \(|m|\le2\). BD gives \(|t+6n|<9\), so \(n\in\{-1,0,1\}\). Modulo simultaneous sign, choose \(t=0\) or \(1\); parity \(m\equiv n\pmod2\), removal of the zero vector and moment inversion give exactly three \(t=0\) rows and seven \(t=1\) rows. No other integer vector at larger Port is possible. Each surviving row satisfies the strict-near definition exactly when its six slacks (2) are positive. QED.

## Theorem 2 — Complete five-phase section, including equality

Fix \(w=(11,1,60,D)\) with real \(71\le D\le121\). All these weights satisfy (H), and
\[
\eta_p(11,1,60,D)=\frac6{1+D}\qquad(p\ge10).
\]
The two \(t=0\) rows \((0,1,\pm1)\) are always near once Port-feasible. The eight other rows have these exact entry conditions (and their respective Ports from the preceding table):

| Row(s) | Strict near condition |
|---|---|
| (1,-2,0) | \(D<542/7\), limiting BC slack \(542-7D\) |
| (0,2,0) | \(D<181/2\), limiting BC slack \(543-6D\) |
| (1,2,0) | \(D<211/2\), limiting AC slack \(633-6D\) |
| (1,0,0), (1,-1,-1), (1,-1,1), (1,1,-1), (1,1,1) | \(D<107\), limiting AB slack \(107-D\) |

All other slacks are positive on each row's claimed interval. Therefore for **every \(p\ge38\)**:
\[
\boxed{|N_p|=
\begin{cases}
10&71\le D<542/7,\\
9&542/7\le D<181/2,\\
8&181/2\le D<211/2,\\
7&211/2\le D<107,\\
2&107\le D\le121.
\end{cases}}\tag{3}
\]
At each transition equality, the affected row is excluded (strict threshold). For \(10\le p<38\), simply filter the same rows by their exact Ports. Substituting the six gap columns in (2) proves the listed linear thresholds; together with Theorem 1 this proves the entire real-parameter section, without a bounded-Port assumption. For instance, at \(D=75\) all ten rows are near for \(p\ge38\), and all slacks are strictly positive, so the ten-row bound is attained on an open weight neighborhood.

## Exact check, sources and open question

An independently enumerated *finite* replay covers all **95,133 nonzero unoriented integer triples at Port \(\le38\)** for each of **11 rational D samples** (including equality at all four thresholds): **1,046,463 vector/sample comparisons**. Exact integer cross multiplication checks the full six-pair norm, no vector below \(6/Y\), the entire near set and Ports \(10,11,16,17,21,27,28,38\). All match the symbolic classification; the companion checker and JSON record the results. The continuum and unlimited-Port quantifiers are proved in the analytic argument. An independent mathematical review remains open.

R117 source: \`research_notes/portable_direct/2026-11-23_r2_x6_r117_two_parameter_first_outsider_strip.md\`. Additional applicable inputs: P000 V5 and locked X6 foundations, the ACTIVE worldview, \`docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context\`, \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`, \`research_priorities/research_method.json\`. The observer retains all six pair relations, and none of these results are promoted to native heartbeat physics.

**Next question:** determine the maximally connected exact weight chambers of (H), and whether a second optimal witness extends the ten-row structure across \(Y=6(A+B)\). The native X6/R063 program is a separate Task with its own claim and authority.
