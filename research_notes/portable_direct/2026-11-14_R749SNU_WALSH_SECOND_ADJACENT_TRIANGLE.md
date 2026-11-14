# R749SNU — Second exact Walsh wedge, continuous minimax center

Date: 2026-11-14. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED.
Scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Previous work: R749SNS PR #2346 and R749SNT, same research branch. Scope: auxiliary 16-atom Walsh model only.

## 1. Model and theorem

Let \(G=\mathbb F_2^4\), \(\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}\). As in the frozen source model, all compatible laws have the form

\[
\mu_{t,s,h,u,v,w,z}(x)=\tfrac1{16}(1+t\chi_3+s\chi_{12}+h\chi_{15}+u\chi_1+v\chi_2+w\chi_4+z\chi_8)(x),
\]

with sixteen nonnegative masses and zero retained moments at masks 5,6,7,9,10,11,13,14. Define \(\rho(t,s)\) as the smallest worst-case total variation radius over all predictive laws on \(G\), and \(\rho^{\mathrm{cal}}(t,s)\) with the predictor constrained to the same source fiber.

Let \(A=(7/10,1/10)\), \(X=(3/5,3/20)\), \(Y=(3/5,2/15)\). The second **new** triangle is

\[
\mathcal U=\operatorname{conv}\{A,X,Y\}
=\{(t,s):t\ge3/5,\ t+2s\le9/10,\ t+3s\ge1\}.
\]

**Theorem R749SNU.** At every real \((t,s)\in\mathcal U\),

\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=(3+t-s)/8.}
\]

One optimal calibrated center is

\[
q_{t,s}(x)=\tfrac1{16}(1+t\chi_3(x)+s\chi_{12}(x)+(1-t-3s)\chi_{15}(x)).
\]

The new coefficient \(\eta_{\mathcal U}(t,s)=1-t-3s\) equals the R749SNT coefficient \(31/40-3t/4-5s/2\) along the shared side \(AX\), because \(t+2s=9/10\) there. Thus the old and new minimax centers glue continuously, including the vertex \(Y\) where \(\eta(Y)=0\). The triangle has area \(1/1200\) and is disjoint in its interior from all previously proved areas. The total area certified by R749SNS+SNT+SNU is

\[
\boxed{\frac{43}{800}+\frac1{800}+\frac1{1200}=\frac{67}{1200}}.
\]

## 2. Lower and upper arguments

For the unrestricted minimax radius, average any predictor under translations by xor masks 3 and 12. The averaging retains the source fiber and cannot increase maximal TV error; invariant predictors have Walsh support in \(\{0,3,12,15\}\). On the fixed event \(S=\{3,5,7,9,11,13,14,15\}\), all three nonconstant invariant characters have zero sum, so \(q(S)=1/2\). The explicitly compatible source

\[
W_{t,s}=\mu_{t,s,0,s-1,-t,-s,-s}
\]

has nonnegative atoms at all three vertices A,X,Y (and therefore throughout \(\mathcal U\)) and satisfies

\[
W_{t,s}(S)-1/2=(3+t-s)/8.
\]

This proves the desired unrestricted lower bound. Calibration cannot reduce it.

For the upper bound, the proposed \(q_{t,s}\) has correct retained moments and nonnegative sixteen atom masses at A,X,Y, hence throughout the triangle. The source family on this parameter triangle is a bounded, seven-dimensional joint polytope with 16 atom nonnegativity inequalities and three parameter inequalities. Scale all seven variables by 40. The parameter rows are

\[
(1,0,0,0,0,0,0)\cdot y\ge24,\quad
(-1,-2,0,0,0,0,0)\cdot y\ge-36,\quad
(1,3,0,0,0,0,0)\cdot y\ge40.
\]

The companion exact checker enumerates every \(\binom{19}{7}=50,388\) active facet basis, solves with integer Bareiss elimination, checks all inequalities using rational arithmetic and deduplicates vertices. It evaluates

\[
\Delta=\operatorname{TV}(\mu_{t,s,h,u,v,w,z},q_{t,s})-(3+t-s)/8
\]

at every vertex. The complete deterministic output is:

| Check | Value |
|---|---:|
| All active bases | 50,388 |
| Nonsingular bases | 27,600 |
| Feasible active bases | 648 |
| Distinct rational vertices | 132 |
| Equality vertices | 52 |
| Positive excess | 0 |
| Maximum excess | 0 |

Since \(\Delta\) is convex in the joint variables and the bounded polytope is the convex hull of its vertices, these exact inequalities hold throughout the polytope, for all real parameters in \(\mathcal U\). The explicit lower witness and upper certificate together give the minimax equality.

## 3. Exact next boundary

The new outer vertex \(Y=(3/5,2/15)\) has \(\eta(Y)=0\) and radius \(\rho(Y)=13/30\). The previous SNT center along \(AX\) switches continuously into \(1-t-3s\), and the next exposed edge is \(t+3s=1\). The follow-on R749SNV investigates the exact radius for smaller \(s\) at \(t=3/5\), distinguishing a change in the common optimal risk from a nonzero calibration penalty.

## 4. Reproduction, source scope

Run R749SNU_WALSH_SECOND_WEDGE_EXACT_CHECK.py, compare its complete deterministic stdout with R749SNU_WALSH_SECOND_WEDGE_RESULTS.json. It checks all 50,388 bases with integer and Fraction arithmetic, all 132 distinct vertices, positivity of decoder and source, event witness, area, and coefficient continuity on \(AX\). There is no approximate arithmetic in the proof.

This is an author-side auxiliary-model result. Native X6/V29/V39 provenance-preserving correspondence, independent review, and any formal Task Result/Review are separate unresolved obligations. Frozen science, P000, and existing Source task ownership are unchanged.
