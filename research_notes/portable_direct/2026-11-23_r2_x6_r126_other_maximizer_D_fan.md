# X6 R126 — Exact D-ray fan for a second Port-10 maximizer, with Port-11 collapse

Date: 2026-11-23 (Asia/Shanghai). Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED. This concerns the **conditional four-positive-weight, six-pair BRC observer** of R121–R125, with its frozen scientific definitions; it makes no claim to native X6 physical time dynamics. P000 and the joint observer-preservation scope remain unchanged.

## Population and precise result

For integer triples \(a=(x,y,z)\ne0\), quotient only by global sign (positive multiples are separate directions), define
\[
q(a)=\max\{\sum_i\max(a_i,0),\sum_i\max(-a_i,0)\},\quad
h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z).
\]
For \(w>0\), let \(F_w(a)=\max_{i<j}|h_i-h_j|/(w_i+w_j)\), \(\eta_p(w)=\min_{0<q(a)\le p}F_w(a)\), and \(N_p(w)=\{\{\pm a\}:0<q(a)\le p,\ 2F_w(a)<3\eta_p(w)\}\). All six pair gaps remain observed; no factor-only projection is used.

Fix \(w_D=(48,577,240,D)\) for **all real \(900\le D\le1300\)**. This includes the R123 exact eight-direction maximum at \(D=978\), a different weight chamber from the previously studied R125 line \((1,3,4,D)\).

**Theorem R126 (exact continuous-parameter and integer-lattice fan).** For these weights:
\[
\eta_{10}(D)=\min\left(\frac1{96},\frac{11}{D+48}\right),\qquad
\eta_{11}(D)=\frac1{625},\qquad
N_{11}(D)=\{\{\pm(10,-5,1)\}\}.
\]
The Port-10 strict-near direction count is exactly
\[
|N_{10}(D)|=\begin{cases}
6,&900\le D\le912,\\
7,&912<D\le976,\\
8,&976<D<6096/5,\\
7,&6096/5\le D\le1300.
\end{cases}
\]
On the whole open eight-direction interval, the complete \(N_{10}\) is
\[
S=\{(1,-3,1),(1,0,0),(4,-1,0),(5,-4,1),
(5,-1,0),(6,-4,1),(9,-5,1),(9,-2,0)\}/\pm.
\]
Thus **every** weight on this open interval exhibits the exact Port \(10\to11\) discontinuity \(8\to1\). At \(D=1008\), the optimizer changes from the constant value \(1/96\) to \(11/(D+48)\), while \(|N_{10}|=8\) is unchanged. In particular, the eight-direction plateau is not confined to a single weight witness.

## Proof: the optimizer and integer certificate

Use \(H_1=x+3y+6z=k\), \(H_2=3x+12y+30z=3\ell\), and \(H_3=7x+39y+126z\). The six denominators in pair order 01, 02, 03, 12, 13, 23 are \(625,288,D+48,817,D+577,D+240\).

**Integer lemma.** If \(q(a)\le10,\ H_2=0,\ |k|\le6\), then every nonzero direction has \(|H_3|\ge11\). Indeed, solving \(H_1=k,H_2=0\) yields
\[
x=4k+6z,\quad y=-k-4z,\quad H_3=12z-11k=k+12(z-k).
\]
If \(|H_3|\le10\), then \(|k|\le6\) forces \(t=z-k\in\{-1,0,1\}\). For \(t=0\), \(a=k(10,-5,1)\), with Port \(11|k|>10\) unless zero. For \(t=1\), the height restriction forces \(k\le-2\), and then \(q\ge15\); for \(t=-1\), it forces \(k\ge2\), again \(q\ge15\). Contradiction.

Both \(a=(5,-1,0)\) and \(a=(4,-1,0)\) have \(q\le10\), with scores respectively \(1/96\) and \(11/(D+48)\) in the stated interval; hence \(\eta_{10}\le E(D)=\min(1/96,11/(D+48))\). Any alleged score below \(E\le1/96\) has \(|H_2|<288/96=3\), so \(H_2=0\), and \(|k|<625/96<7\). The integer lemma gives \(|H_3|\ge11\), hence \(F\ge11/(D+48)\ge E\), a contradiction. This proves the **exact** Port-10 optimum for every real \(D\) in the interval.

At \(D=1008\) the strict cutoff is \(3\eta_{10}/2=1/64\). The pair constraints 01,02,03,12 imply \(|k|\le9,\ |\ell|\le1,\ |H_3|\le16,\ |k-3\ell|\le12\). Solving \(H_1=k,H_2=3\ell\):
\[
x=4k-3\ell+6z,\quad y=\ell-k-4z,\quad H_3=-11k+18\ell+12z.
\]
For \(|k|\le9,|\ell|\le1,|H_3|\le16\), necessarily \(-11\le z\le11\). Exhaustive integer substitution in this declared finite box, retaining \(q\le10\) and the **four** pair inequalities, yields exactly the eight rows \(S\). Each also satisfies the remaining 13 and 23 pair inequalities, so \(N_{10}(1008)=S\). The attached checker independently scans the complete original \(1,935\)-direction Port-10 lattice and checks this first-four-gap certificate.

For \(900\le D\le1008\), the cutoff is constant and every fixed direction's \(F\) is nonincreasing in \(D\). Consequently no direction may exit as \(D\) grows on this subinterval. Of the eight certified rows, six are already strict near at \(D=900\); \((9,-2,0)\) enters iff \(D>912\), and \((1,-3,1)\) enters iff \(D>976\). There are no other rows because \(N_{10}(D)\subseteq N_{10}(1008)\).

For \(1008\le D\le1300\), the cutoff equals \(33/[2(D+48)]\). Each ratio \(F_w(a)/\eta_{10}\) is nondecreasing in \(D\): every gap term is a nonnegative constant times \((D+48)/c\), \((D+48)/(D+48)\), \((D+48)/(D+577)\) or \((D+48)/(D+240)\), respectively. Thus no new row can enter after 1008. Among \(S\), only \((1,-3,1)\) exits before \(D=1300\): its 23 gap gives
\[
\frac{19}{D+240}<\frac{33}{2(D+48)}
\quad\Longleftrightarrow\quad 5D<6096.
\]
All other seven rows satisfy the strict inequalities through \(D=1300\). Equality correctly excludes the exiting row.

**Port 11.** Let \(u=(10,-5,1)\), with heights \((0,1,0,1)\), \(q(u)=11\), and \(F(u)=1/625\). A smaller-scoring competitor would have \(H_1=0\) and \(H_2=0\); it must be a nonzero multiple of \(b=(6,-4,1)\) with score at least \(12/(D+48)>1/625\) for all \(D\le1300\). Thus \(\eta_{11}=1/625\). For strict near cutoff \(3/1250\), the constant pair gaps force \(|H_1|\le1,H_2=0,|H_1-H_2|\le1\). With \(q\le11\), the only unoriented candidates are
\[
(2,-3,1),(4,-1,0),(6,-4,1),(8,-7,2),(10,-5,1).
\]
The first four have \(|H_3|\ge11\), hence score at least \(11/(D+48)\ge11/1348>3/1250\). Only \(u\) is near, for every real \(D\in[900,1300]\).

The exact Port-10 optimizer tie at \(D=1008\) includes five rows; on its two sides the finite candidate certificate verifies four optimizers before the switch, and a unique optimizer \((4,-1,0)\) afterwards. The count theorem does not require this optional optimizer-multiplicity refinement.

## Exact calculation, limitations, and next question

The attached Python Fraction replay enumerates all **2,541** sign-unoriented integer triples with \(q\le11\) (including **1,935** with \(q\le10\)), checks the eight-row four-gap cut and five-row Port-11 prefilter, and verifies 13 exact rational values of \(D\), including \(912,976,1008,6096/5\) and both sides of the last boundary. It makes **26 complete Port-10/11 snapshots**, all PASS. The uniform continuous-real-parameter conclusions are established by the preceding integer reduction and monotonicity proof, not extrapolated from samples.

Science provenance: R123 simultaneously maximizing sets and exact rational witness [R123 global result](https://github.com/awdawmip/chatgpt-global-knowledge/blob/2e6278dc712114e795d216a62b6c71d139701fd5/journal/enterprise-math/2026-11-23/x6-r123-small-port-simultaneous-maximum-results.json); [R125 D-line](https://github.com/awdawmip/enterprise-math/blob/f1432731ed54a3820bd9fd540cb467bb1d3f3941/research_notes/portable_direct/2026-11-23_r2_x6_r125_D_line_near_fan.md). All hypotheses and source versions are explicitly limited to this six-pair conditional observer; neither the native X6 Task nor its frozen scientific source pin was modified.

Independent review and formal Source admission are pending. The next useful unit is to enlarge the exact D interval, then derive analogous full-ray fans for the other R123 Port-10 maximizer chambers and identify possible optimizer/strict-near fan crossings.
