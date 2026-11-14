# PREFIX-785 — A provenance-linked single source preserves a sharp uniform two-sign margin

Date: 2026-11-14. Status: AUTHOR_PROVED / EXACT_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Scientific source pin: f42f2906d77f24085c123f3ccfe9667d41caa96d (preserved).
Lineage: PREFIX-781–784; research identity EM-DIRECT-E77192; existing Activity RA-66BBE259AEE1AD543D9454A3.

## 1. Motivation and exact model

PREFIX-784 computed two separate sign-loss windows for independently selectable, asymmetrically calibrated corner errors. An actual BRC observer may constrain many apparent corner errors to be functions of one shared provenance-labeled source. It is then important to distinguish the joint attainable observer set from its coordinate-wise box hull.

Consider the following exact external scalar auxiliary observation for any real \(q>0\) and one common real signed-source parameter \(-1\le t\le1\):
\[
\boxed{a(q,t)=(t-q,\;t+3-2q,\;q-t,\;-t-3+2q).}
\]
The first two coordinates have unperturbed coefficients \(A=(0,3)\) and \(B=(1,2)\), so \(A_2 B_1-A_1 B_2=3>0\). The last two coordinates reflect the first two. The source is **one** \(t\), not four independently chosen corner errors. No native Cell/Link/Port/force-source transfer is asserted by this construction.

The quantitative two-sign margin at \((q,t)\) is
\[
M(q,t)=\min\bigl(\max_j a_j(q,t),\ -\min_j a_j(q,t)\bigr)
      =\max\{|t-q|,\ |t+3-2q|\}.
\]
The equality holds because \(a_3=-a_1\), \(a_4=-a_2\); when \(M>0\), both a strictly positive and a strictly negative coordinate exist, each of magnitude at least \(M\).

## 2. Exact minimax theorem

**Theorem 785.1 (source-correlated sharp margin).** For every real \(q>0\),
\[
\boxed{m(q):=\min_{-1\le t\le1}M(q,t)
=\frac{|3-q|}{2}
+\max\!\left(0,\frac{|3q-3|}{2}-1\right).}
\]
Equivalently,
\[
m(q)=
\begin{cases}
2-2q,&0<q\le1/3,\\
(3-q)/2,&1/3\le q\le5/3,\\
q-1,&5/3\le q\le3,\\
2q-4,&q\ge3.
\end{cases}
\]
Consequently the globally uniform, sharp two-sign margin is
\[
\boxed{\inf_{q>0}\min_{t\in[-1,1]}M(q,t)=2/3.}
\]
The unique minimizing \(q\) is \(5/3\); its minimizing source is \(t=1\), producing
\[
 a(5/3,1)=(-2/3,\ 2/3,\ 2/3,\ -2/3).
\]
In particular, **for every** \(q>0\) and every admissible shared source \(t\), the four observed mixed differences contain a strictly positive and strictly negative value, with both magnitudes at least \(2/3\).

**Proof.** The elementary Chebyshev identity for any reals \(t,u,v\) is
\[
\max(|t-u|,|t-v|)=\frac{|u-v|}{2}
  +\left|t-\frac{u+v}{2}\right|.
\]
Apply it with \(u=q\), \(v=2q-3\). The center \(s=(3q-3)/2\) is optimally approximated by \(t=\mathrm{clamp}(s,-1,1)\), at distance \(\max(0,|s|-1)\), proving the first exact formula with an attaining \(t\). For \(q\le1/3\) the center is at most \(-1\), for \(1/3\le q\le5/3\) it lies in \([-1,1]\), and for \(q\ge5/3\) it is at least \(1\). Splitting the final absolute value at \(q=3\) yields the four branches. The slopes in the four open segments are \(-2,-1/2,+1,+2\); thus the unique global minimum is at \(q=5/3\) with value \(2/3\), attained by \(t=1\). The displayed four-tuple establishes sharpness. QED.

## 3. Exact failure of the independent-box relaxation

**Theorem 785.2 (source independence can destroy the certificate).** Replace the joint provenance law
\((u_1,u_2,v_1,v_2)=(t,t,t,t)\), \(-1\le t\le1\), with four independent coordinate bounds
\(|u_1|,|u_2|,|v_1|,|v_2|\le1\). The relaxed observation becomes
\[
\widehat a=(-q+u_1,\ 3-2q+u_2,\ q-v_1,\ -3+2q-v_2).
\]
At \(q=1\), take \(u_1=v_1=1\), \(u_2=v_2=-1\). Then all four coordinates vanish. Nevertheless, the true source-linked class at \(q=1\) has sharp two-sign margin \(m(1)=1\).

**Proof.** Substitute the indicated rational values. The first theorem gives \(m(1)=1\). The independent-box witness uses the incompatible simultaneous source values \(+1\) and \(-1\); it does not belong to the diagonal joint source set \(\{(t,t,t,t)\}\). QED.

**Consequence.** A coordinate-wise interval outer bound may prove strict two-sign persistence when its own feasibility test excludes sign loss. When it admits cancellation, that conclusion can be inconclusive for a provenance-correlated source. The shared source relation can yield a stronger exact certificate, here the uniform \(2/3\) margin, without shrinking any of the four coordinate-wise error ranges.

## 4. Verification, source, and next objective

The companion script PREFIX785_R6_CORRELATED_SOURCE_MARGIN_CHECK.py uses Python standard-library exact Fraction arithmetic: 4,096 deterministic seeded rational \(q\) cases and 24,576 independently checked admissible \(t\) comparisons. It verifies the exact formula against the attaining clamp construction, its four rational branches, positive/negative sign symmetry, the \(2/3\) lower bound, and the independent-box zero witness. Result file: PREFIX785_R6_CORRELATED_SOURCE_MARGIN_RESULTS.json; outcome ALL_CHECKS_PASS PREFIX785 CORRELATED_SOURCE_UNIFORM_MARGIN. The universal conclusion follows from the explicit proof; finite tests are implementation regression.

This is a new algebraic correlated-observer result in the external scalar BRC–Gamma auxiliary family. The coefficients here are a declared illustrative choice, not a recalculation of the pinned 189-layer stop-model coefficients; the original comparator exclusion count is unchanged. The source pin, active P000/ACTIVE worldview, and earlier experimental results remain untouched. The mathematical theorem is not independently reviewed or promoted.

**Next scientific question.** Extract the actual native typed BRC/X6 source-to-observer incidence map, including Cell/Link/Port, branch, signed-source and event-time constraints. Determine whether its attainable scalar corner perturbations factor as independent boxes, as a low-dimensional common-source affine image, or as a general correlated polytope. For an affine common-source class, compute the exact robust mixed-sign margin via provenance-preserving finite rational polyhedral optimization and test it against a box outer bound. If transferring to the 189-layer auxiliary Gamma model, substitute its frozen exact \(A_i,B_i\), and verify the observable map before asserting native physical claims.
