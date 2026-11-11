# PREFIX-715-R6 — Exact rational multi-witness / multi-bound exclusion certificate

Date: 2026-11-12 (Asia/Shanghai). Scientific input pin (unchanged): `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Parent: PREFIX-675. Reuses PREFIX-710's corrected Gamma maximum, PREFIX-712's fine-grid exclusion, PREFIX-713's witness/moment certificates and PREFIX-714's nonoverlapping union.

Status: `AUTHOR_PROVED / EXACT_FRACTION_TOY_CHECKED / UNREVIEWED / NOT_ADMITTED`. Scope is the **auxiliary two-parameter statistical observer** \(D=[0,1/2]^2\), not a native X6 two-dimensional plane.

## Exact question

For \(Y(p,z)=\max(T_p,T_z)\), where the two independent completion clocks are conditional Gamma clocks in the pinned BRC model, let \(\mu=E[Y]\), \(W=\operatorname{Var}(Y)\), \(t=1/q\), and \(f_t(x)=W(x)-t\mu(x)\). Hence \(V_q(x)=q^2 f_{1/q}(x)\).

A given competitor may fail to exclude a spatial cell uniformly over an interval even though **a family of competitors chosen depending on \(t\)** does exclude it. Likewise a family of independently proved affine upper bounds can outperform each of its members. We turn this into an exact finite certificate.

## Theorem 715.1 — finite rational multi-envelope certificate

Fix any cell \(C\subseteq D\) and a closed real parameter interval \(I=[a,b]\), with rational endpoints. Let \(e_1,\dots,e_k\) be feasible model parameters whose exact rational moments give affine **lower witnesses**

\[
L_i(t)=W(e_i)-t\mu(e_i).
\]

Let \(U_1(t),\dots,U_m(t)\), with rational affine coefficients, be separately proved **uniform upper bounds** satisfying

\[
f_t(x)\le U_j(t)\quad\text{for every }x\in C,\ t\in I,\ j=1,\dots,m.
\]

Define

\[
G(t)=\max_{1\le i\le k}L_i(t)-\min_{1\le j\le m}U_j(t)
=\max_{i,j}\bigl(L_i(t)-U_j(t)\bigr).
\]

Let \(K\) be the finite rational set consisting of \(a,b\) and all intersections strictly inside \(I\) between two *nonparallel* affine lines in the family \(\{L_i-U_j\}_{i,j}\). Then

\[
\boxed{\delta:=\min_{t\in I}G(t)=\min_{t\in K}G(t).}
\]

If \(\delta>0\), the entire **closed** cell \(C\) contains no global maximizer of \(f_t\) for **any** real \(t\in I\). More precisely, with \(H(t)=\max_{x\in D}f_t(x)\),

\[
H(t)-f_t(x)\ge \delta>0\quad(x\in C,\ t\in I).
\]

For each finite \(q\) such that \(1/q\in I\), the unscaled objective satisfies the quantitative margin

\[
\boxed{\max_{D}V_q-V_q(x)\ge q^2\delta.}
\]

If \(\delta\le0\), a minimizer \(t_0\in K\) gives a **certificate-insufficiency witness**, not a counterexample to the mathematical optimizer or the model. All endpoint/intersection values, the margin and the failure locator are exact rationals.

### Proof

Every \(L_i\) is the actual objective at a feasible parameter and hence \(H(t)\ge\max_i L_i(t)\). Every \(U_j\) is an upper bound over \(C\), so \(f_t(x)\le\min_j U_j(t)\). Therefore \(H(t)-f_t(x)\ge G(t)\). The identity for \(G\) shows that it is the maximum of finitely many rational affine lines. It is continuous and piecewise affine. Between consecutive members of \(K\), no two nonparallel lines change their ordering; the active maximum is affine on each such interval. An affine function takes its minimum over a closed interval at one of its endpoints, including if it is constant. Thus the minimum of \(G\) over \(I\) is the minimum over \(K\). Positive \(\delta\) proves strict exclusion; multiply by \(q^2\) for \(V_q\). A nonpositive certificate margin has no implication about whether the true objective reaches the cell bound. QED.

The raw line count is \(r=km\); the candidate count is at most \(2+r(r-1)/2\). Exact rational computation suffices without floating point or scanning an infinite \(t\) interval.

## Exact BRC/Gamma interface and its premises

For a rectangle \([a,h]\) whose coordinatewise survival-tail stochastic order was established in PREFIX-710/711/712, one existing valid affine upper bound is

\[
U_1(t)=E[Y(h)^2]-\mu(a)^2-t\mu(a).
\]

The corner order implies \(\mu(x)\ge\mu(a)\) and \(E[Y(x)^2]\le E[Y(h)^2]\) for all \(x\in[a,h]\); hence \(W(x)-t\mu(x)\le U_1(t)\) for \(t\ge0\). Other affine upper bounds can be added **only after** their cell-uniform validity is proved independently, e.g. by an existing coupled-moment certificate with the correct Gamma clock. This theorem never treats the maximum of stopping counts as the maximum of Gamma completion clocks; that substitution caused PREFIX-709's invalid certificate.

The witness and bound families may depend on the chosen cell but not on an unproved within-cell optimizer. The exact source-reuse decision is `COMPOSE_APPLIED`: combine the existing PREFIX-713 multi-competitor/dual-witness lines and the already valid interval/coupled bounds. No new general-purpose BRC family, Foundation admission or actual new cell count follows automatically.

## Fully verified exact example

Take \(I=[0,1/2]\), one synthetic cell bound \(U(t)=10-3t\), and two synthetic feasible objective curves

\[
L_1(t)=51/5-4t,\qquad L_2(t)=99/10-2t.
\]

The two differences are \(L_1-U=1/5-t\) and \(L_2-U=t-1/10\). Neither single witness excludes the whole interval (the first fails at \(t=1/2\), the second at \(t=0\)). Together they give

\[
G(t)=\max\{1/5-t,\ t-1/10\},\qquad
\boxed{\delta=G(3/20)=1/20>0}.
\]

This proves that selecting one **fixed** competitor passing both endpoints is sufficient but **not necessary** for a finite witness family to certify a whole continuous parameter range. With a weakened first line \(101/10-4t\), the minimum is exactly zero at \(t=1/10\), furnishing the appropriate *failed-certificate* locator. With an additional **assumed independently valid** cell upper bound \(U_2(t)=201/20-4t\), the original combined example improves to \(\delta=3/20\) at \(t=1/20\).

These exact rational toy tests illustrate a general proof; they are **not** measurements of the pinned BRC Gamma model. The numeric union from PREFIX-714 remains unchanged: \(137278/147456\) excluded at all real \(q\ge2\), and \(137494/147456\) for \(12\le q\le24\), at author-level verification, not independent admission.

## Reproduction, limitations and next discriminating experiment

Run `python PREFIX715_R6_AFFINE_ENVELOPE.py` (Python standard library). It writes `PREFIX715_R6_RESULTS.json` and reports `ALL_CHECKS_PASS PREFIX715-R6`. The author locally executed the same exact rational algorithm, including the positive two-witness margin, single-witness failures, nonpositive failure locator and improved multi-bound case. No frozen 189-level recalculation or 384-by-384 BRC scan is claimed; no new BRC grid cells were certified in this unit.

Next use the PREFIX-714 **actual remaining** cell set, the exact Gamma moment witness curves at \((0,149/1000)\), \((0,146/1000)\) and the existing multi-competitors. Combine these only with independently proved cell bounds, run the exact envelope check on \([0,1/2]\) and \([1/24,1/12]\), and count only newly disjoint cells. For failed certificates retain the exact minimizer \(t_0\) and active competing lines to direct local witness search or a tighter valid upper bound. Preserve scientific pin, genuine Owner/CLAIM status, the Source activity boundary, and separate author proof from independent review.
