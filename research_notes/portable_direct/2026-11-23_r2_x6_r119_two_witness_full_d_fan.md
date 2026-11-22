# X6 R119 — Two-witness phase transition and complete six-phase Port fan

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR_PROOF / EXACT_INTEGER_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED**.

Model and scope: R90–R118 conditional four-positive-weight BRC observer, all six weighted pair observations retained. This is an exact static integer-observer result; it is not a native X6 time-dynamics claim or a change to the frozen P000 inputs.

## Statement and exact definitions

For nonzero (a=(x,y,z)\in\mathbb Z^3), define
\[
q(a)=\max\{\sum_i\max(a_i,0),\sum_i\max(-a_i,0)\},
\quad h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z).
\]
For positive (w=(A,B,C,D)), let
\[
F_w(a)=\max_{0\le i<j\le3}\frac{|h_i(a)-h_j(a)|}{w_i+w_j},\quad
\eta_p(w)=\min_{0<q(a)\le p}F_w(a),\quad
N_p(w)=\{\{\pm a\}:0<q(a)\le p,\ F_w(a)<\tfrac32\eta_p(w)\}.
\]
Use the integral moment coordinates
\[
t=x+3y+6z,\quad m=x+4y+10z,\quad n=x+6y+20z,
\]
with (m\equiv n\pmod2), inversion
\[
a=(10t-12m+3n,\,-5t+7m-2n,\,t+(n-3m)/2)
\]
and heights (h=(0,t,3m,t+6n)). The gaps in pair order AB, AC, AD, BC, BD, CD are
\[
\boxed{(|t|,\,3|m|,\,|t+6n|,\,|3m-t|,\,6|n|,\,|t+6n-3m|).}\tag{G}
\]

**Theorem (R119, complete section).** Fix (w_D=(11,1,60,D)) with real (1\le D\le121). For **every integer Port (p\ge11)**:
\[
\boxed{\eta_p(w_D)=
\begin{cases}
1/12,&1\le D\le71,\\
6/(D+1),&71\le D\le121.
\end{cases}}\tag{1}
\]
The formulas agree at (D=71). Every strict near direction, at any such (D,p), belongs to the following ten unoriented integer rows. The table also gives the exact first Port.

| Moments ((t,m,n)) | Integer direction (a) | First Port |
|---|---|---:|
| (0,1,-1) | (-15,9,-2) | 17 |
| (0,1,1) | (-9,5,-1) | 10 |
| (0,2,0) | (-24,14,-3) | 27 |
| (1,-2,0) | (34,-19,4) | 38 |
| (1,0,0) | (10,-5,1) | 11 |
| (1,2,0) | (-14,9,-2) | 16 |
| (1,-1,-1) | (19,-10,2) | 21 |
| (1,-1,1) | (25,-14,3) | 28 |
| (1,1,-1) | (-5,4,-1) | 6 |
| (1,1,1) | (1,0,0) | 1 |

For (1\le D\le47), precisely the **four rows with (n=0)** are strict near when Port-feasible. For (47<D\le71), **all ten rows** are strict near when Port-feasible. For (71\le D\le121), retain exactly the R118 row criteria:
- rows (0,1,-1) and (0,1,1): always;
- row (1,-2,0): (D<542/7);
- row (0,2,0): (D<181/2);
- row (1,2,0): (D<211/2);
- remaining five (t=1) rows: (D<107).

In every region, the complete Port atlas is obtained by filtering these rows by their listed minimum (q\le p). In particular, for **all (p\ge38)**,
\[
\boxed{
|N_p(w_D)|=
\begin{cases}
4,&1\le D\le47,\\
10,&47<D<542/7,\\
9,&542/7\le D<181/2,\\
8,&181/2\le D<211/2,\\
7,&211/2\le D<107,\\
2,&107\le D\le121.
\end{cases}}\tag{2}
\]
These are six distinct maximal count phases on the stated interval. At every threshold equality the departing rows are excluded by the strict inequality. (D=71) is a change of optimal witness with **no** near-set count jump. At (D=47), six near directions enter simultaneously on the (D>47) side, although the optimum remains (1/12) on both sides.

## Proof

**Step 1 — optimal value for (1\le D\le71).** By (G), for any nonzero (a):

* If (t\ne0), AB alone gives (F_{w_D}(a)\ge |t|/12\ge1/12).
* If (t=0,n\ne0), BD gives (F_{w_D}(a)\ge6|n|/(D+1)\ge6/72=1/12).
* If (t=n=0), parity forces even nonzero (m), so AC gives (F_{w_D}(a)\ge3|m|/71\ge6/71>1/12).

The direction (a_*= (10,-5,1)) has ((t,m,n)=(1,0,0)), Port 11, and (h=(0,1,0,1)). Its six observations are (1/12,0,1/(11+D),1/61,0,1/(60+D)), whose maximum equals (1/12) for (D\ge1). Thus (1) holds for every (p\ge11) in this half-section.

**Step 2 — optimal value for (71\le D\le121).** These weights meet all six homogeneous hypotheses (H) of the previously proved R118 ten-candidate cone. The R118 lower bound and the Port-10 witness ((t,m,n)=(0,1,1)), (a=(-9,5,-1)), yield (\eta_p=6/(1+D)) for (p\ge10). This agrees with the Step-1 formula at (D=71).

**Step 3 — full integer-lattice enclosure for (1\le D\le71).** Strict nearness now means (F<3/2\cdot1/12=1/8). Hence AB, AC and BD imply
\[
|t|<12/8=3/2,\qquad |m|<71/24<3,\qquad |n|<(1+D)/48\le3/2.
\]
All are integers. Consequently (|t|\le1, |m|\le2, |n|\le1). Together with (m\equiv n\pmod2), removal of the zero vector, and simultaneous sign reversal, these are exactly the ten displayed moment rows: three with (t=0) and seven with (t=1). There are no missing directions at arbitrarily large Port.

If (D\le47), BD further yields (|n|<(D+1)/48\le1), so (n=0). Exactly four displayed rows have (n=0). For these rows, the six pairwise ratios are bounded above respectively by
\[
1/12,\quad6/71,\quad1/(11+D),\quad7/61,\quad0,\quad7/(60+D),
\]
all strictly below (1/8) for (D\ge1). Therefore all four are near when Port-feasible.

If (47<D\le71), all ten rows satisfy the same strict threshold. For the six (n=\pm1) rows, their six ratios are bounded by
\[
1/12,\quad6/71,\quad7/(11+D)<7/58,\quad7/61,\quad6/(D+1)<1/8,\quad10/(60+D)<10/107;
\]
each is below (1/8). The four (n=0) rows remain near. The only exact entry wall in the new section is therefore (D=47), and equality excludes all six (n=\pm1) rows. This proves the new portion of the Port atlas.

**Step 4 — upper section and completeness.** For (D\ge71), invoke R118's already proved exact ten-row theorem and its six-affine-slack classifications. The R118 thresholds (542/7,181/2,211/2,107) give the remaining four departures. Combining these with Step 3 and Port filtering proves (2), including all equalities and the unbounded Port quantifier. QED.

**Source correction:** In R118's proof, its displayed phrase “BD gives (|t+6n|<9)” should read **“BD gives (6|n|<9)”** under the declared heights. Both inequalities restrict the stated (n\)-range in that setting, and the enumerated ten-row theorem remains valid. Here the correct BD identity is used throughout.

## Exact replay / certificate

The accompanying standalone `x6_r119_two_witness_d_fan_verify.py` enumerates each of the **95,133** unoriented nonzero integer triples with Port (\le38), independently evaluating all six original height gaps (not merely the reduced ten-row list). For **17 exact rational** (D) samples, it checks the proposed optimum has no smaller competitor, tests complete strict near-set equality to the ten-row classifier, verifies the Port counts, and checks all six phase boundaries including (D=47), (542/7), (181/2), (211/2), and (107). Thus **1,617,261 vector/sample pairs** were covered in the author's local exact replay; no floating point arithmetic is used. Results are in `x6_r119_two_witness_d_fan_results.json`. This finite replay is supplementary to the all-real-(D), all-(p\) analytic proof.

Previous exact result: [R118 at immutable commit 9508c71f](https://github.com/awdawmip/enterprise-math/blob/9508c71f4e3c7e90d1a3106d4cb548accacfed38/research_notes/portable_direct/2026-11-23_r2_x6_r118_four_weight_ten_candidate_cone.md). Source status remains AUTHOR_PROOF, with independent mathematical review not performed.

## Next questions

The two-witness mechanism suggests a more general four-weight union of chambers: identify explicit sufficient inequalities guaranteeing (\eta_p=\min\{1/(A+B),6/(B+D)\}) while preserving a finite near-row bank. The (D<1) and (D>121) ends of this section also remain to classify. The native X6 rotation/triadic time model and original R063 six-file benchmark are independent and not discharged by this conditional static BRC result.
