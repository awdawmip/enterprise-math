# R749SSJ — Strict six-step raw-ratio growth and two-read continuous-error calibration

Date: 2026-11-16 (Asia/Shanghai). Status: `AUTHOR_EXACT_NOT_REVIEWED`.
Mode: independent portable auxiliary-source mathematics; no shared X6 CLAIM.
Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Predecessors: R749SSI / PR #2560 @ `0465b731bdd411719f75421d5d144f3c69631841`; R749SSF–SSH / PR #2557 @ `d980a326e3036d9d1f821e1b8c56dfdfdaaa5b47`.

## 1. Model and three theorems

Let five distinct positive labeled sources have weights `(1,1,2,3,6)` and let the first weight-one source be marked. For integer `q>=1` define

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]

For one common **real** calibration pair \((e,d)\in[-2,2]^2\) used at both cutoffs, define \(X(q;e,d)=(T_q+e)/(C_q+d)\). This is a scoped extension of earlier bounded integer errors, preserving source labels and exact frozen counts.

**Theorem A (universal sharp six-shift inequality):** For every integer \(q\ge6\) and every real \((e,d)\in[-2,2]^2\),

\[
\boxed{X(q+6;e,d)-X(q;e,d)>1.}
\]

The infimum of the left side over the entire stated domain is **exactly 1**, not attained. Uniformly in the compact error square,

\[
X(q+6;e,d)-X(q;e,d)=1+\frac{115}{6q^2}+O(q^{-3}).
\]

**Theorem B (complete continuous-error recovery from two reads):** For fixed *known* integer \(q\ge6\), set \(x_0=X(q;e,d)\) and \(x_1=X(q+6;e,d)\). The error pair has the exact left inverse

\[
\boxed{d=\frac{T_{q+6}-T_q-x_1C_{q+6}+x_0C_q}{x_1-x_0},\qquad e=x_0(C_q+d)-T_q.}
\]

Theorem A supplies \(x_1-x_0>1\). Thus the ordered two-read observer is injective for all real bounded errors, with no Diophantine integrality requirement.

**Theorem C (one-read loss and future separation):** At \(q=6\), \((e,d)=(0,0)\) and \((50/41,1)\) have the *same* first reading \(50/41\). But at \(q+6=12\),

\[
X(12;50/41,1)-X(12;0,0)
=\frac{12057}{5207}-\frac{881}{380}
=-\frac{5707}{1978660}\ne0.
\]

Thus two scalar readings are minimal for real-error identification among this one- or two-read measurement family. For **integer** bounded errors, predecessor R749SSE already proves a single exact reading is sufficient for \(q\ge6\); the distinction is substantive.

## 2. Exact proof of the strict inequality

Write \(C=C_q,C'=C_{q+6},T=T_q,T'=T_{q+6}\). Define

\[
G(q,e,d)=(T'+e)(C+d)-(T+e)(C'+d)-(C+d)(C'+d).
\]

Since \(C_q\ge C_6=41\) for \(q\ge6\), both denominators are positive and

\[
X(q+6;e,d)-X(q;e,d)-1
=\frac{G(q,e,d)}{(C+d)(C'+d)}.
\]

The exact generating functions are

\[
\sum_{q\ge1}C_q z^{q-1}
=\frac1{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{q\ge1}T_qz^{q-1}
=\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

On changing denominators to \((1-z^6)^6\) and \((1-z^6)^7\) respectively, numerator degrees are at most 22 and 28. Consequently for each residue class \(q\bmod6\), starting at \(q\ge36\), \(C_q,T_q\) are exact polynomials in \(q\) of degrees at most 5 and 6. For fixed errors, \(G\) is therefore a residue-class polynomial of degree at most 11.

For every \(r\in\{0,\ldots,5\}\) and \(e,d\in\{-2,-1,0,1,2\}\), evaluate the 12 exact integers \(G(36+r+6j,e,d)\), \(j=0,\ldots,11\). Compute the forward-difference coefficients \(a_i=\Delta_6^iG(36+r,e,d)\). The attached dependency-free Python certificate checks all **150** cases:
- \(a_0,\ldots,a_8>0\);
- \(a_9=a_{10}=a_{11}=0\);
- every \(a_8=69552\), the smallest positive Newton coefficient over all cases.

The degree bound makes the identity
\[
G(36+r+6j,e,d)=\sum_{i=0}^{11}a_i\binom ji>0
\quad(j\in\mathbb Z_{\ge0})
\]
a rigorous *infinite* certificate. The remaining \(6\le q\le35\) and 25 integer error pairs are all evaluated exactly (750 cases), with smallest \(G=39\) at \(q=6,e=2,d=-2\).

Extend from the integer grid to **all real errors** using the exact identity

\[
G(q,e,d)=T'C-TC'-CC'+e(C-C')+d(T'-T-C'-C)-d^2.
\]

For each fixed \(d\), \(G\) decreases in \(e\) because \(C'>C\), hence its minimum is at \(e=2\). The function \(d\mapsto G(q,2,d)\) is concave with second derivative \(-2\); its minimum over \([-2,2]\) is attained at \(d=-2\) or \(d=2\). Both endpoints are among the verified integer cases. Thus \(G>0\) on the full square and Theorem A's strict inequality holds.

The exact eighth Newton difference \(69552\) means the leading coefficient of \(G\) on *every* residue class is
\[
[q^8]G=\frac{69552}{8!6^8}=\frac{23}{22394880}.
\]
Also \(C_q=q^5/4320+O(q^4)\), giving
\[
q^2(X(q+6)-X(q)-1)\longrightarrow
\frac{23}{22394880}\cdot4320^2=\frac{115}{6}.
\]
All coefficients and errors range over a finite number of residue classes and a bounded parameter square, so the \(O(q^{-3})\) expansion is uniform. Therefore 1 is the largest universal lower-bound constant. QED.

## 3. Exact inverse and noise propagation

The identities \(T+e=x_0(C+d)\) and \(T'+e=x_1(C'+d)\) prove Theorem B by subtraction and substitution. Theorem C follows from the displayed exact source counts \(C_6=41,T_6=50,C_{12}=380,T_{12}=881\).

If the two **raw-ratio** readings are perturbed by \(|\eta_i|\le\delta<1/2\), apply the inverse formula to \(u_i=x_i+\eta_i\). Exact algebra yields
\[
\widehat d-d
=\frac{(C_q+d)\eta_0-(C_{q+6}+d)\eta_1}
{(x_1-x_0)+(\eta_1-\eta_0)}.
\]
Consequently
\[
|\widehat d-d|\le\frac{\delta(C_q+C_{q+6}+4)}{1-2\delta},\qquad
|\widehat e-e|\le\delta(C_q+2)+|u_0|\,|\widehat d-d|.
\]
For integer errors a conservative sufficient condition
\(\delta<1/[2(C_q+C_{q+6}+5)]\)
allows \(\widehat d\) to be rounded, followed by rounding \(u_0(C_q+d)-T_q\) to recover \(e\). The stated bound is sufficient, not claimed optimal.

The pre-existing smooth observer is \(Y(q;e,d)=q^3X(q;e,d)-S(q)/108\) with
\(S(q)=18q^4+54q^3-345q^2+2070q-16315\).
For each **known** cutoff, conversion from \(Y\) back to \(X\) is exact, so the same two-read injection applies to the known-\(q\) smooth observer pair. Its noise error must first be scaled by the appropriate \(q^{-3}\) factor; this theorem does not assert a uniform absolute \(Y\)-noise bound.

## 4. Evidence, scope and next question

Companion files: `R749SSJ_SIX_STEP_CONTINUOUS_CALIBRATION_CERT.py` and `R749SSJ_SIX_STEP_CONTINUOUS_CALIBRATION_RESULTS.json`. Run Python 3 in the same directory. Only standard-library integer operations and `fractions.Fraction` are used. The `PASS` result verifies six known exact count anchors, 750 finite inequalities, 150 complete positive Newton certificates, coefficient 115/6, the exact single-read fiber witness and a rational inverse sample. The generating-function degree argument and concave endpoint extension are written above and jointly establish the infinite real-parameter theorem.

Status: author exact proof and independent local computation, not an independent Driver review or Foundation admission. Scientific carrier: five positive *labeled* sources with a common-error update; no signed-native BRC/Cell/Port/X6 identification is asserted. The shared `RS-X6-NATIVE-TIME-DYNAMICS` Task has separate formal ownership.

**Open frontier:** For unknown integer cutoff \(q\ge6\), determine whether the ordered smooth pair \((Y(q;e,d),Y(q+6;e,d))\), with a common bounded integer or real error pair, identifies \(q\) and the error coordinates globally. Prove an exact cross-cutoff injectivity theorem or find a collision; then obtain a scale-dependent noise radius. Any future BRC source-port mapping must keep the five labels, the common-error relation and the six-step observation operation.
