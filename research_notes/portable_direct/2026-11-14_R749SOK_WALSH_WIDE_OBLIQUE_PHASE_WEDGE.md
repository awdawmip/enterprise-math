# R749SOK — Exact widened two-dimensional oblique Walsh calibration-gap phase wedge

**2026-11-14 · Independent portable research · AUTHOR_EXACT_NOT_REVIEWED.** Scientific input frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This note extends R749SOJ on [Draft PR #2383](https://github.com/awdawmip/enterprise-math/pull/2383); it reuses the exact model definitions, R749SOH source-diameter construction and R749SOI zero-gap triangle. No claim about a native X6/V29/V39 event correspondence follows.

## Theorem: widened exact two-dimensional phase formula

As in the predecessor, take \(G=\mathbb F_2^4\), \(\chi_m(k)=(-1)^{\operatorname{popcount}(m\mathbin{\&}k)}\), \(A=\chi_3\), \(B=\chi_{12}\), \(C=AB=\chi_{15}\), and the complete compatible source fiber

$$
F_{t,s}=\left\{\mu_{t,s,h,u,v,w,z}(k)=
\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}\ge0 \quad (k=0,\ldots,15)\right\}.
$$

The minimum worst-case total variation radius among all probability decoders is \(\rho(t,s)\); the corresponding radius restricted to decoders in \(F_{t,s}\) is \(\rho^{\mathrm{cal}}(t,s)\).

**For every real pair** in the closed nondegenerate trapezoid

$$
\mathcal Q=\left\{(t,s):\frac35\le t\le\frac{37}{50},\quad
1-t\le s\le t-\frac1{10}\right\},
$$

the *exact* values are

$$
\boxed{\rho(t,s)=\frac{3-t-2s}{4},\quad
\rho^{\mathrm{cal}}(t,s)=\max\left\{\frac{3-t-2s}{4},\frac{4-2t-2s}{5}\right\},\quad
g(t,s)=\frac{\max(0,1-3t+2s)}{20}.}
$$

Therefore, throughout the interior of \(\mathcal Q\), the oblique line \(3t-2s=1\) is the **true zero/positive calibration-cost phase boundary**: \(g=0\) on \(3t-2s\ge1\) and \(g>0\) on \(3t-2s<1\). It contains the original \((2/3,1/2)\) transition. Its exact area is \(21/625\), 28 times the rectangle proved in R749SOJ. The positive region has area \(91/10000\); the zero region has area \(49/2000\).

## Proof: matching free lower and upper bounds

The trapezoid satisfies \(0\le s\le t\le1\) and \(t+s\ge1\). The two compatible sources

$$
\mu_{\pm}=\mu_{t,s,\,t+s-1,\,\pm(1-s),\,\pm(1-s),\,\pm(1-t),\,\pm(1-t)}
$$

are nonnegative with unit mass in this domain, and their exact total variation distance is \((3-t-2s)/2\), by the explicit 16-atom identity of R749SOH. The triangle inequality implies \(\rho(t,s)\ge (3-t-2s)/4\).

On the *positive-side* quadrilateral

$$
P=\mathcal Q\cap\{3t-2s\le1\}
=\operatorname{conv}\left\{
(\tfrac35,\tfrac25),(\tfrac{37}{50},\tfrac{61}{100}),
(\tfrac{37}{50},\tfrac{16}{25}),(\tfrac35,\tfrac12)\right\},
$$

the explicit free probability center

$$
q_f(k)=\frac{1+A(k)+(2t-1)B(k)+(2t-1)C(k)}{16}
$$

has source worst-case radius at most \((3-t-2s)/4\), as certified for all real parameters by the exhaustive rational joint-polytope calculation below.

On \(\mathcal Q\cap\{3t-2s\ge1\}\), the exact R749SOI zero-side triangle theorem applies because \(t+s\ge1\) and \(t\le1\). It supplies both the free upper bound and a calibrated matching upper bound.

## Proof: calibrated positive lower bound

Finite translation symmetrization by \(3,12\in\mathbb F_2^4\) preserves the fiber and the retained moments \((t,s)\), cancels the four unretained characters, and never increases the supremum TV radius. Therefore any optimal calibrated center can be taken of the form

$$
q_h(k)=\frac{1+tA(k)+sB(k)+hC(k)}{16}.
$$

Construct the two compatible source laws with coefficient tuples \((h,u,v,w,z)\):

$$
\mu_A=(1+s-t,\ s-t,\ s-t,\ 0,\ 0),\qquad
\mu_G=(t+s-1,\ s-1,\ s-1,\ t-1,\ t-1).
$$

Their atom probabilities are affine in \((t,s)\). At the four corners of \(P\) every atom is nonnegative and each distribution has mass one (verified exactly by the supplied script), so they remain compatible on all \(P\). Use events

$$
E_A=\{1,2,4,7,8,11,13,14\},\quad
E_G=\{0,1,2,4,5,6,8,9,10,12\}.
$$

Direct Walsh summation gives the two TV event lower bounds

$$
L_A=q_h(E_A)-\mu_A(E_A)=\frac{1+s-t-h}{2},\qquad
L_G=q_h(E_G)-\mu_G(E_G)=\frac{7-3t-5s+h}{8}.
$$

Thus for every calibrated decoder, after symmetrization,

$$
\max_{\mu\in F_{t,s}}TV(q_h,\mu)
\ge\frac{L_A+4L_G}{5}=\frac{4-2t-2s}{5}.
$$

This is strictly larger than the free radius precisely on the interior positive side \(3t-2s<1\).

## Proof: exact calibrated positive upper certificate

Throughout \(P\), use the explicit calibrated center

$$
q_c(k)=\frac{1+tA(k)+sB(k)+\frac{9s-t-3}{5}C(k)}{16}.
$$

Its sixteen probabilities are nonnegative on \(P\), as certified at the parameter corners by exact arithmetic. The following seven-dimensional joint-polytope computation proves the upper bound for *all real parameters* in \(P\).

Use variables \(X=(t,s,h,u,v,w,z)\), 16 source-atom nonnegativity inequalities, and four parameter-facet inequalities, each in integer-coefficient greater-equal form:

$$
5t\ge3,\qquad-50t\ge-37,\qquad-3t+2s\ge-1,\qquad10t-10s\ge1.
$$

These 20 halfspaces describe the compact joint source polytope over \(P\). Any vertex has seven linearly independent tight facets. The accompanying Python standard-library checker enumerates all

$$
\binom{20}{7}=77\,520
$$

active-facet combinations, solves them by fraction-free integer Bareiss elimination, verifies all halfspace inequalities, deduplicates exact rational vertices, and evaluates TV excess using \`fractions.Fraction\`. Exactly **36,512 nonsingular bases**, **1,316 feasible bases** and **80 distinct rational vertices** result. The maximum free and calibrated upper-bound excesses are both *exactly zero*; there are **zero violations** (20 vertices saturate the free bound, 32 the calibrated bound). All candidate distributions are checked for probability nonnegativity and mass one, and all four polygon corners satisfy the compatible-source identities and event dual bound.

Because the TV excess minus the affine target radius is convex on the compact joint polytope, its maximum is attained at a vertex; these exact finite checks certify the uniform bounds for every real parameter. Combining with the analytic lower bounds proves the theorem on \(P\), and the R749SOI theorem covers the remainder.

At the common edge \(3t-2s=1\), the center coefficient satisfies \((9s-t-3)/5=t+s-1\); the two calibrated centers agree and define a continuous piecewise-affine exact optimal predictor on \(\mathcal Q\).

## Reproduction, scope, next question

Run \`python3 R749SOK_WALSH_OBLIQUE_WEDGE_CERT.py\` in this folder and compare the JSON to \`R749SOK_WALSH_OBLIQUE_WEDGE_RESULTS.json\`. All arithmetic is exact integer/fraction arithmetic; no numerical LP approximations or float tolerance are involved. The frozen 16-state auxiliary Walsh model is the theorem's entire scope, independent scientific review remains pending, and native X6/V29/V39 fidelity remains a separate open problem.

The new exact two-dimensional boundary length is the intersection segment from \((3/5,2/5)\) to \((37/50,61/100)\). Next determine the maximal connected region on which the two explicit centers remain minimax, identify the next dual active-facet change, and only then consider a typed BRC/native source correspondence.

**Artifacts:** this complete proof, the exact standalone checker, and its PASS JSON. Both the code and JSON were executed locally and the exact bytes are to be established by immutable GitHub readback.