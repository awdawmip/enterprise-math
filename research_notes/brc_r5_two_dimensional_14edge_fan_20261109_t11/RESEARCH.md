# R5 — Exact two-dimensional physical 14-edge Blackwell atlas: sharp triangular fan and full-width rectangle

Date: 2026-11-09 (Asia/Shanghai). **Author-side exact proof, locally executed rational verification, independent review pending.**

Frozen scientific inputs unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Reuses the complete literal predecessor endpoint certificates from [PR #1843](https://github.com/awdawmip/enterprise-math/pull/1843), immutable commit `7244646fed297cc29e2af74755c3fe909c21ff01`. Statistical observer: seven-LR-node P/Q-BRC, a restricted observer within the declared Enterprise Math worldview.

## Stronger theorem — a full-width two-dimensional rectangle via an exact observer-kernel lift

The following strengthens the triangular fan above by **preserving a nonzero transverse width at the endpoint \(\lambda=1\)**. It also illustrates a use of BRC residual bookkeeping: change the source's hidden flow coordinates along an *exact kernel of the declared statistical observer*, while retaining that internal flow distinction for other possible operations.

Define the nonzero source-flow direction

$
K=\left(
-\frac{49400}{295513},
-\frac{49400}{295513},
-\frac{49400}{295513},
-\frac{33345}{591026},
\frac{132145}{295513},
-\frac{33345}{591026},
1
\right).
$

Exact substitution into the frozen maps proves

$
M(X_0+K)-M(X_0)=0,\qquad
T_P(X_0+K)-T_P(X_0)=T_Q(X_0+K)-T_Q(X_0)=0,
$

and \(K_g=K_b\). Since all these maps are affine, \(K\) lies in their common linear kernel globally on the flow-coordinate space. Set

$
\widetilde D_X=D_X-K,\qquad \widetilde D_Y=D_Y.
$

The mass variation of \(x\) is unchanged, as are both stop-time equalities, the source \(g=b\) identity, and the exact nonnegative transport formulas. Only the *physical source-flow lift* changes.

**Full rectangle theorem.** For **every pair of real numbers**

$
\boxed{0\le\lambda\le1,\qquad 0\le\delta\le\frac1{120}}
$

the physical flows

$
\widetilde x(\lambda,\delta)
=(1-\lambda)X_0+\lambda X_1+\delta\widetilde D_X,\qquad
\widetilde y(\lambda,\delta)
=(1-\lambda)Y_0+\lambda Y_1+\delta D_Y
$

are lawful FULL_HIST source and seedless F-face LR target, have exactly equal stopping times, and admit a declaration-independent Blackwell transport with **at most 14 positive edges**. The transport is the *same two-chart formula* \(E^A,E^B\) displayed in the preceding theorem, now over the full closed rectangle.

**Proof.** The support \(\{(0,0),(3,3),(6,6)\}\) of \(D\) belongs to both charts, and \(K\) changes neither source marginals nor stop times. Therefore all 21 transport equations and the seedless identities are exact affine identities. The left chart rectangle \(\lambda\in[0,1/2],\delta\in[0,1/120]\) has its four corners at A0, AH and the two new top certificates A0top, AHtop. The right chart rectangle has its corners BH, B1 and BHtop, B1top. The independent VERIFY_RECTANGLE.py checks all four new top certificates using exact Fraction arithmetic: each physical capacity, seedless identity, full Q/P normalization, stop-time equality, 21 transport equations and matrix nonnegativity passes. The original \(\delta=0\) corners were already verified. Affine convexity proves the result for all reals in the full rectangle. The same exact marginal Jacobian determinant \(-367/48000\) remains nonzero; this is a genuine 2D rectangle in statistical marginal space.

**Exact sharpness for this fixed lifted ray.** At \(\lambda=0\), the source starts at \(z_0=1/120\), while \(\widetilde D_{X,z}=-1\). Thus physical \(z\ge0\) holds only for \(\delta\le1/120\); equality occurs at the upper rectangle edge. Exact verification shows every other required chart-corner inequality remains nonnegative at this width. Therefore **\(1/120\) is the largest possible uniform rectangle width along the specific lifted direction \(\widetilde D_X\)**. This statement is scoped to this lift; other transverse directions may admit larger regions.

The kernel equality is certified for the declared seven-LR-node distribution and stop-time observer. It is not a declaration that the distinct native X6/Heartbeat internal flow states can be globally identified. The saved original \(D_X\), residual \(K\), and lifted \(\widetilde D_X\) preserve both representations and their provenance.

**Code and execution:** VERIFY_2D.py includes the predecessor's literal rational matrices. VERIFY_RECTANGLE.py imports that local file, verifies the exact kernel and all top-chart rational certificates, and emits the output in EXACT_OUTPUT_RECTANGLE.txt. Both scripts were executed locally with standard-library Fraction, and the full real-parameter theorem follows from the affine proof.

**Next question:** Construct a finite collection of similar kernel-assisted physical lift charts covering a larger high-dimensional stratum of the time-matched F-face pair space, or find an exact physically lawful pair whose smallest coupling requires 15 edges. Independently review the R5 global coverage author proof in PR #1831.

---

## Theorem (all real parameters; genuine 2D statistical family)

Define the sharp positive number for this chosen physical transverse direction:

$$
\epsilon_*=\frac{1111424393}{21632616000}.
$$

For **every real** \((\lambda,\delta)\) in the closed triangle

$$
0\leq\lambda\leq1,\qquad 0\leq\delta\leq\epsilon_*(1-\lambda),
$$

there are lawful FULL_HIST flows \(x\), lawful seedless LR flows \(y\), and a declaration-independent Blackwell Q-transport \(E\geq0\) with **at most 14 positive edges**, exactly matching both stopping times and the four observer coordinates \((e_P,e_Q,T_P,T_Q)\) for every seven-node terminal randomized declaration.

Write the flow coordinates in order \((g,a,b,u,v,w,z)\). Let the frozen predecessor's exact pairs \((X_0,Y_0),(X_1,Y_1)\) and exact support matrices \(A0,AH,BH,B1\), with respective supports \(S_A,S_B\), be defined literally in the standalone VERIFY_2D.py. Define

$$
x(\lambda,\delta)=(1-\lambda)X_0+\lambda X_1+\delta D_X,
\quad
y(\lambda,\delta)=(1-\lambda)Y_0+\lambda Y_1+\delta D_Y,
$$

where

$$
D_X=\frac{1}{1111424393}
(-1802718000,-1802718000,-1802718000,-608417325,-496963350,-608417325,0),
$$

$$
D_Y=\frac{1}{3761}(-6000,-6000,-6000,-2025,-1950,-2025,-600).
$$

Let \(D\) be the signed diagonal seven-by-seven matrix with

$$
D_{0,0}=D_{6,6}=-\frac12,\qquad D_{3,3}=1,
$$

and all other entries zero. The fixed LR nodes are \(r=(1/10,1/2,3/4,1,5/4,3/2,19/10)\). The operation is an exactly balanced transfer between extremal and central LR atoms, since \((r_0+r_6)/2=r_3=1\).

**Two exact 14-edge chart formulas**:

$$
E^A(\lambda,\delta)=(1-2\lambda)A0+2\lambda AH+\delta D,
\qquad 0\leq\lambda\leq\tfrac12;
$$

$$
E^B(\lambda,\delta)=(2-2\lambda)BH+(2\lambda-1)B1+\delta D,
\qquad \tfrac12\leq\lambda\leq1.
$$

Both support sets contain the diagonal positions \((0,0),(3,3),(6,6)\). At their common \(\lambda=1/2\) interface, either formula gives an admissible transport for the same source and target marginals; the coupling need not be unique.

## Complete exact argument

**(1) Preservation identities.** The frozen mass map \(M\) and stop-time maps \(T_P,T_Q\) are affine in all seven flow coordinates. Direct exact substitution shows

$$
M(X_0+D_X)-M(X_0)
=
M(Y_0+D_Y)-M(Y_0)
=
(-\tfrac12,0,0,1,0,0,-\tfrac12).
$$

The two stop-time increments along \(D_X,D_Y\) are equal. The source retains \(g=b\); the target direction retains the F-face equations \(z'=a'/10\) and \(v'-z'=9b'/40\), which imply the full nonlinear seedless condition. The signed diagonal \(D\) has row and column sums given by the common marginal increment and satisfies every LR column-moment identity. Hence each displayed piecewise matrix satisfies all 21 transport equations **as an affine identity** throughout its chart.

**(2) Exact finite vertex certificates.** The original certificates A0/AH/BH/B1 at \((\lambda,\delta)=(0,0),(1/2,0),(1/2,0),(1,0)\) are checked by VERIFY_2D.py. The three new chart certificates are

* A0top: \(A0+\epsilon_*D\) at \((0,\epsilon_*)\);
* AHtop: \(AH+\epsilon_*D/2\) at \((1/2,\epsilon_*/2)\);
* BHtop: \(BH+\epsilon_*D/2\) at \((1/2,\epsilon_*/2)\).

For all seven certificates the exact checker validates nonnegative transfer entries, all 21 equations, every physical capacity inequality for both flows, the F-face equations, total P/Q mass, and both stopping times. Positive-edge counts are 14 except for B1 with 12.

**(3) Convex domain coverage.** The left chart's parameter polygon is

$$
(0,0),\quad (0,\epsilon_*),\quad (1/2,\epsilon_*/2),\quad (1/2,0).
$$

The right chart's triangle is

$$
(1/2,0),\quad (1/2,\epsilon_*/2),\quad (1,0).
$$

These regions exactly partition the closed triangular domain. All physically admissible inequalities and transfer entry inequalities are affine in \((\lambda,\delta)\). Exact verification of the vertices therefore proves **all-real** legality and nonnegativity on the full domain (including irrational parameters), not merely on a finite sample.

**(4) Genuine two-dimensional marginals.** Set \(\nu=M(x),\ \mu=M(y)\). The exact derivatives include

$$
\partial_\delta\nu_0=-\tfrac12,\quad
\partial_\delta\mu_1=0,\quad
\partial_\lambda\mu_1=-\tfrac{367}{24000}.
$$

Consequently

$$
\det\frac{\partial(\nu_0,\mu_1)}{\partial(\lambda,\delta)}
=-\frac{367}{48000}\ne0.
$$

Thus the constructed marginal pair has nonempty two-dimensional relative interior in the selected two marginal coordinates; it is not a duplicate parameterization of the previously proved one-dimensional segment.

**(5) Sharp transverse width on this specific ray.** The source capacity condition \(z\leq a/10\) at \(\lambda=0\) has base slack \(a_0/10-z_0=1/120\). Its derivative with respect to \(\delta\) is exactly

$$
\frac{\partial}{\partial\delta}(a/10-z)
=-\frac{180271800}{1111424393}.
$$

It reaches zero at precisely \(\delta=\epsilon_*\). Therefore every \(\delta>\epsilon_*\) violates that physical inequality already at \(\lambda=0\), **for this fixed transverse direction**. All other vertex constraints remain nonnegative at \(\epsilon_*\), as checked. Hence this value is the **exact maximal wedge width for this chosen direction and triangular scaling rule**.

## Reproduction, source, next question

The self-contained VERIFY_2D.py bundles the four immutable predecessor matrices and exact mass/time formula and uses Python standard-library Fraction only. Run `python VERIFY_2D.py`; EXACT_OUTPUT.txt contains the executed local output. The key claim is a symbolic identity plus convex vertex proof, with exact arithmetic, not a statistical regression. Formal mathematical Result, task CLAIM, independent review and Foundation promotion are separate.

Next: seek a second transverse direction preserving the active \(g\leq1\) and \(z\leq a/10\) facets at \(\lambda=1\), then produce a two-dimensional region with positive width even at that endpoint, or derive a precise support/physical-facet obstruction. The broader open mother question is whether a finite ≤14-edge atlas covers every lawful \(g=b\) physical pair, or whether a lawful pair requires 15 edges. Independent review of the full-model R5 author proof (PR #1831) remains pending.

Control observation for this run: the native EM backend returned BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false on the attempted session and task requests, so no live Researcher-ID, active Owner/CLAIM or registered native checkpoint is asserted. The artifact here is an author-side GitHub evidence branch/PR.
