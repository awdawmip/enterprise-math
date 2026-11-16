# R749SSL — Three smoothed observations also fail to identify an unknown cutoff

Date 2026-11-16. AUTHOR_EXACT_NOT_REVIEWED. Independent portable source-observer algebra, continuing R749SSK, under frozen input pin a72226e2430ffa4786321ac86e7f0c599d5f0389 (R749SSJ/PR #2563).

## Model and theorem

Let C_q and T_q be respectively the number of five-labeled-source vectors and the summed first coordinate in

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\}.
\]

Define \(S(q)=18q^4+54q^3-345q^2+2070q-16315\) and
\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-S(q)/108.
\]

The same *real* calibration pair (e,d) in [-2,2]^2 applies across every read. Define the ordered triple \(G_q(e,d)=(Y_q(e,d),Y_{q+6}(e,d),Y_{q+12}(e,d))\).

**Theorem (exact three-read no-go).** There exist admissible error pairs for distinct integer cutoffs q=7 and p=8 with
\[
\boxed{G_7(e,-1)=G_8(e',d').}
\]
The parameters can be specified exactly by an isolated root of a quadratic integer polynomial and rational functions of it. Thus three smoothed reads do not universally identify unknown q under bounded continuous calibration errors.

## Algebraic construction and complete proof

Set
\[
P(e)=5957265452844e^2-5464016404300823e+35816460863863.
\]
Since \(P(0)>0\), \(P(1/100)<0\), and \(P'<0\) throughout [0,1/100], there is a unique real zero \(e_*\in(0,1/100)\). For the q=7 state take \((e,d)=(e_*,-1)\). At p=8 set
\[
H(e)=151241499e-18047271191,
\]
\[
d'(e)=\frac{2(202246101e+4057501031)}{H(e)},\qquad
e'(e)=\frac{3(425014044e^2-46558027037e-65798686651)}{8H(e)}.
\]

For every \(e\in[0,1/100]\), H is negative. Moreover
\[
d'+1=\frac{555733701e-9932269129}{H(e)}>0,\quad d'<0.
\]
For \(N=425014044e^2-46558027037e-65798686651\), the strict inequalities \(1<e'<2\) are equivalent (since 8H is negative) to
\[
3N-8H=1275042132e^2-140884013103e-53017890425<0,
\]
\[
3N-16H=1275042132e^2-142093945095e+91360279103>0.
\]
The displayed signs hold directly for 0<=e<=1/100: the first expression is bounded above by \(1275042132/10000-53017890425<0\); the second is bounded below by \(91360279103-142093945095/100>0\). Hence \(-1<d'<0\) and \(1<e'<2\) on the entire interval, proving admissibility.

The exact source-count anchors are:

| q | C_q | T_q |
|---:|---:|---:|
| 7 | 65 | 91 |
| 8 | 98 | 156 |
| 13 | 506 | 1261 |
| 14 | 662 | 1767 |
| 19 | 2106 | 7447 |
| 20 | 2576 | 9553 |

At each j=0,1,2, convert the q=7 smooth observation to the candidate p=8 raw ratio:
\[
x_j(e)=\frac{Y_{7+6j}(e,-1)+S(8+6j)/108}{(8+6j)^3}.
\]
All three reads arise from one common p=8 pair (e',d') exactly when the linear equations
\[
e'-x_j d'=x_j C_{8+6j}-T_{8+6j}\qquad (j=0,1,2)
\]
are compatible. Their first two equations have a unique solution because
\[
x_1(e)-x_0(e)=-H(e)/17027727360>0.
\]
Their solution is exactly the displayed rational pair (e'(e),d'(e)). Compatibility with the third equation is equivalent to
\[
D(e)=\det\begin{bmatrix}
1&-x_0&x_0C_8-T_8\\
1&-x_1&x_1C_{14}-T_{14}\\
1&-x_2&x_2C_{20}-T_{20}
\end{bmatrix}=0.
\]
An exact rational-polynomial calculation gives
\[
\boxed{D(e)=-P(e)/191164619161600000.}
\]
Each x_j is affine in e; the determinant has degree at most two. The attached standard-library certificate matches D with -P/denominator at the three distinct exact values e=0,1,2, which proves the polynomial identity at every real e. At the isolated root e=e_* the consistency determinant vanishes, completing the three-read collision.

## Reproducibility, scope and next question

The companion Python 3 file R749SSL_THREE_READ_EXACT_OBSTRUCTION_CERT.py computes the five-labeled-source counts, tests the degree-two determinant identity using rational arithmetic, checks the inverse formulas, and certifies all strict bounds on the isolation interval. The JSON R749SSL_THREE_READ_EXACT_OBSTRUCTION_RESULTS.json records PASS and proof obligations. The root is specified by a rational interval and polynomial; numerical root approximation is not evidence.

This proves one real-error three-read collision under the frozen source observer, not a bounded-integer-error counterexample, four-read theorem, signed-native BRC mapping or native X6 time result. The source labels, common-error coupling, ordered observations and cutoff provenance remain explicitly typed. The concrete next step is to analyze four-read cross-cutoff fiber intersections and separately resolve the integer-error observer; any BRC/Port bridge must preserve the future-observer relation exactly.
