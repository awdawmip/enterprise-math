# X6 R68 — Heteroscedastic common-bias positive-BRC star-moment tomography

Date: 2026-11-21 (Asia/Shanghai).
Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_FRACTION_FINITE_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED.

## Scientific scope and frozen input

Continuation of R61–R67, specifically the R65 universal half-radius theorem and R67 exact D=6 staircase. Scientific P000: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (frozen V5). Preserve the six native spatial axes, separate time, Cell/Link/source provenance and whole-triad TRIADIC_CLOSURE_E. This is a **conditional positive-weighted named-AB-branch observation model**, not a proven native reset/evolution law. The histogram is a declared limited readout; the full Cell/Link joint relation remains retained for other operations.

For integers p >= D >= 2, each named A Port has a set of r_i in {0,...,D} successful B Ports in a p-by-p Boolean relation. Keeping the same A Port and independently resetting the B choices across t trials yields positive branch mass Z_t=(uv)^t sum_i r_i^t for known positive rational u,v. Define the normalized moments

\[
m_t(c)=\sum_{d=0}^{D}c_d d^t,\qquad t=1,\ldots,D,
\]

where c_d counts rows of success degree d and sum c_d=p. The recovery target is precisely the high-degree histogram (c_2,...,c_D). Readouts now carry channel-dependent positive precision weights w_t and a freely unknown common real additive bias b:

\[
y_t=m_t(c)+b+e_t,\qquad |e_t|\le\eta w_t,\quad w_t>0.
\]

The weights describe **normalized** observation errors. A common raw-mass bias divided by (uv)^t is a different nuisance model.

## Theorem 1 — exact weighted quotient for every p,D

For two distinct target histograms put a_d=c_d-c'_d (d=2,...,D), and introduce the common-bias-invariant differences

\[
z_1=0,\qquad z_t=\sum_{d=2}^{D}a_d(d^t-d)\quad (2\le t\le D).
\]

They can give the same observation vector for some biases and allowed errors precisely when

\[
\boxed{\eta\ge \eta_{\rm pair}(a;w):=
 \frac12\max_{1\le i<j\le D}\frac{|z_i-z_j|}{w_i+w_j}.}
\]

An integer difference vector a is realized by a pair of named, strictly positive-weight BRC relations of p Ports iff

\[
\boxed{q(a):=\max\bigl(\sum_{d=2}^{D}(a_d)_+,
                   \sum_{d=2}^{D}(-a_d)_+\bigr)\le p.}
\]

Hence the sharp *closed* ambiguity threshold is the finite exact integer problem

\[
\boxed{\eta^*_{p,D}(w)=
\min_{\substack{a\in\mathbb Z^{D-1}\setminus\{0\}\\q(a)\le p}}
 \frac12\max_{1\le i<j\le D}\frac{|z_i-z_j|}{w_i+w_j}.}
\]

PROOF. A difference of degree-one counts adds a constant in t; the unknown biases absorb this. Let h be the remaining adjustable constant difference. Two models' readout boxes intersect iff there is h satisfying |z_t-h|<=2 eta w_t for all t. The intervals [z_t-2 eta w_t,z_t+2 eta w_t] have nonempty common intersection exactly when every two intersect (interval Helly property), yielding |z_i-z_j|<=2 eta (w_i+w_j). This proves both directions and equality attainment. The realizability condition is necessary by separate positive/negative row counting. For sufficiency, populate degrees d>=2 with positive and negative parts, fill each model's unused rows with degree-zero rows, and realize a row of degree d by choosing its first d named B Ports; D<=p. All used BRC branch weights are positive. QED.

COROLLARY (D=2, all p>=2): z=(0,2a_2), so the exact radius is

\[
\boxed{\eta^*_{p,2}(w_1,w_2)=\frac1{w_1+w_2}.}
\]

## Theorem 2 — exact all-D stability of the R65 half-radius plateau

Let w_min=min_t w_t and w_max=max_t w_t. If

\[
\boxed{p\ge\max(D,2^D-D-1),\qquad w_{\max}<2w_{\min},}
\]

then **for every integer D>=2** the unique minimizing difference vectors, up to reversing the two networks, are

\[
a_d^*=(-1)^d\binom{D+1}{d+1}\qquad(2\le d\le D),
\]

and the exact weighted recovery radius is

\[
\boxed{\eta^*_{p,D}(w)=
\left(\min_{\substack{1\le i<j\le D\\i\not\equiv j\ ({\rm mod}\ 2)}}(w_i+w_j)\right)^{-1}.}
\]

PROOF. R65 proves that the only nonzero integer histogram differences with unweighted z-oscillation 2 are a* and -a*, that q(a*)=2^D-D-1, and that every other nonzero integer vector has even oscillation at least 4. The R65 vector satisfies z_t=1+(-1)^t, and Theorem 1 therefore gives eta_pair(a*)=1/min(opposite-parity pair)(w_i+w_j), which is <=1/(2w_min). Every other vector has some |z_i-z_j|>=4, so its weighted radius is >=4/(4w_max)=1/w_max. The strict weight-ratio hypothesis makes this bound strictly larger than 1/(2w_min), hence larger than eta_pair(a*). Uniqueness and the exact formula follow. QED.

The ratio hypothesis is an explicit sufficient stability region, not a claimed necessary boundary.

## Sharp finite heteroscedastic counterexample and exact enumeration

At D=4, p=11, set weights (w_1,w_2,w_3,w_4)=(1,1,100,100). The R65 alternating difference a*=(10,-5,1) has z=(0,2,0,2) and weighted radius 1/2. A different feasible vector a=(9,-5,1), with q(a)=10, has z=(0,0,-6,-12), and weighted radius 6/101. Thus the R65 alternating witness stops being optimal for sufficiently unequal channel precision.

The exact verifier exhausts all 23^3=12,167 possible integer vectors a in [-11,11]^3; q(a)<=11 excludes all but 5,082 nonzero feasible candidates. It proves that the **exact finite D=4,p=11 optimum** is 6/101, with exactly the two opposite optimizers (9,-5,1) and (-9,5,-1). This is a complete finite-domain certificate because q(a)<=11 necessarily bounds every coordinate by 11.

By contrast, with D=4,p=11 and weights (1,6/5,4/5,11/10), the complete finite search finds 10/19, only the two R65 optimizers. A constructive D=6,p=57 example at weights (1,6/5,4/5,11/10,9/10,1) has exact radius 5/9 by Theorem 2; this latter claim relies on the general proof, not a full D=6 search.

## Executed checks and files

Python 3 standard-library Fraction arithmetic was executed for the binomial construction at D=2,3,4,6 and full feasible-vector searches at D=2,p=2; D=3,p=4; D=4,p=11 (two weight profiles). All exact assertions passed. Reproduction: run python3 x6_r68_weighted_shared_bias_verify.py and compare the JSON output with x6_r68_weighted_shared_bias_results.json. No floating point, Lean, independent scientific review or native TRIADIC_CLOSURE_E simulation is represented as completed.

Sources: R65 exact plateau proof, https://github.com/awdawmip/enterprise-math/blob/60e554e6b93c773f1d315fe6de8106ab4ad796fd/research_notes/portable_direct/2026-11-21_x6_r65_universal_half_radius_plateau.md ; R67 D=6 staircase, https://github.com/awdawmip/enterprise-math/blob/c7041dd11bbf42a50f96f6f5c4ff62a666512014/research_notes/portable_direct/2026-11-21_x6_r67_d6_full_common_bias_staircase.md .

## Next research

Find efficient exact minimization for unrestricted rational weights and larger D; classify the weight-dependent transition surfaces of the intermediate R66/R67 population stairs. Separately derive or rule out a frozen-P000 native whole-triad Cell/Link/Port and reset map realizing this conditional positive BRC observer. Do not discard raw joint relations or confuse histogram recovery with native chronological state recovery.

Registered Researcher: EM-X6-214D9C; original session MCP-d467c19ce42d4d7fa65a3901db1cf6b2; activity RA-545183ADD4EF71C3E4698AEE. Authenticated native owner/CLAIM and PROGRESS are separate from this portable author proof.
