# Height-2 supersingular Frobenius second-digit reduction

Status: `STRICT_LOCAL_REDUCTION / COORDINATE_CORRECTED / EXACT_PARENT_NORMALIZATION_MAP / NO_P3_CLOSURE_CLAIM`

Date: `2026-09-08`

Researcher-ID: `EM-UR24-7C91A0`

Parent continuation: `ur_chisholm_closure_lift_frontier_20260908.md`

## 1. Purpose and correction boundary

The Chisholm–Deines–Long–Nebe–Swisher proof closes the supersingular de Rham coefficient product modulo \(p^2\). This note retains one additional formal p-adic digit and isolates the exact local data needed for a mod-\(p^3\) refinement.

A first draft of this note conflated the coefficients in the original local parameter \(\xi=-x/y\) with those after the quartic-normalized parameter

\[
\widetilde\xi=\Delta_d^{-1/4}\xi
\]

used to invoke Proposition 16. That is not harmless at the second digit. The present version corrects the coordinate system: **all Frobenius-matrix coefficient comparisons below use the coefficients after this quartic normalization.**

As a result, the earlier attempted separate decomposition into an asserted twist digit \(\tau_p\) and a truncated-Clausen digit \(\kappa_p\) is withdrawn. The rigorous residual comparison is compressed instead to one scalar \(\chi_p\), defined only after the twisted Frobenius product and the target weighted sum are both fixed.

This note still does **not** prove the parent `LIFT`, `JT2`, or the weighted Ramanujan congruence modulo \(p^3\).

## 2. Correct supersingular Frobenius coordinates

Let

\[
\widetilde{\mathfrak a}_p,\qquad \widetilde{\mathfrak b}_p
\]

be the \((p-1)\)-st coefficients of the two normalized de Rham eigen-differentials \(\omega,\nu\) **in the quartic-normalized local parameter** \(\widetilde\xi\). Equivalently, if \(a(p-1),b(p-1)\) denote the corresponding coefficients in the original parameter, the change of parameter contributes the \(\Delta_d^{(p-1)/4}\) factor to each coefficient.

For the present \(d=3,\lambda=1/2\) CM specialization, the quartic-normalized curve is over a totally real base and the constant term of the Frobenius polynomial is

\[
b_2=p.
\]

In the supersingular case the square-root Frobenius matrix used in Proposition 16 has the form

\[
M=\begin{pmatrix}u&v\\ w&-u\end{pmatrix}
\]

with

\[
-u^2-vw=p. \tag{D}
\]

The proof of Proposition 16 gives

\[
u\equiv0\pmod p,\qquad v\equiv0\pmod p,\qquad w\in A^\times,
\]

and

\[
1\equiv \frac{v\widetilde{\mathfrak b}_p}{p}\pmod p,
\qquad
1\equiv \frac{w\widetilde{\mathfrak a}_p}{p}\pmod p. \tag{C1}
\]

Consequently \(\widetilde{\mathfrak a}_p\) is divisible by \(p\), whereas \(\widetilde{\mathfrak b}_p\) is a unit.

Write

\[
u=pU,\qquad v=pV,\qquad w=W,\qquad \widetilde{\mathfrak a}_p=pA,
\]

where \(V,W,A,\widetilde{\mathfrak b}_p\) are units modulo \(p\). Define the two coefficient-comparison defect digits

\[
e_a:=\frac{WA-1}{p}\pmod p,
\qquad
e_b:=\frac{V\widetilde{\mathfrak b}_p-1}{p}\pmod p. \tag{E}
\]

These are well-defined by `(C1)`.

## 3. Exact second digit of the twisted de Rham product

Divide `(D)` by \(p\):

\[
-pU^2-VW=1,
\]

hence

\[
VW=-1-pU^2. \tag{VW}
\]

From `(E)`, modulo \(p^2\),

\[
A=W^{-1}(1+pe_a),
\qquad
\widetilde{\mathfrak b}_p=V^{-1}(1+pe_b).
\]

Therefore

\[
\begin{aligned}
\widetilde{\mathfrak a}_p\widetilde{\mathfrak b}_p
&=pA\widetilde{\mathfrak b}_p\\
&=p(VW)^{-1}(1+p(e_a+e_b))\\
&\equiv p(-1+pU^2)(1+p(e_a+e_b))\pmod{p^3}\\
&\equiv -p+p^2\bigl(U^2-e_a-e_b\bigr)\pmod{p^3}.
\end{aligned}
\]

Thus the one-order refinement of the **quartic-normalized supersingular de Rham product** is the single scalar

\[
\boxed{
\mathcal F_p:=U^2-e_a-e_b\pmod p.
} \tag{FROB2}
\]

Equivalently,

\[
\boxed{
\frac{\widetilde{\mathfrak a}_p\widetilde{\mathfrak b}_p+p}{p^2}
\equiv\mathcal F_p\pmod p.
} \tag{RAW-DEFECT}
\]

This is a strict reduction: the determinant relation eliminates the product \(VW\), so the raw second digit needs only

1. the diagonal Frobenius jet \(U=u/p\bmod p\);
2. the combined coefficient-comparison jet \(e_a+e_b\bmod p\).

Separately computing higher digits of \(V\) and \(W\) is unnecessary for this observer.

## 4. Why the sign is negative here

Theorem 1 of Chisholm–Deines–Long–Nebe–Swisher gives the target weighted Ramanujan truncation with sign

\[
\operatorname{sgn}\cdot\left(\frac{1-\lambda}{p}\right)p.
\]

For the present target primes,

\[
\operatorname{sgn}=-1
\]

because the CM reduction is supersingular, while

\[
\left(\frac{1-\lambda}{p}\right)
=\left(\frac{1/2}{p}\right)=-1.
\]

Hence the weighted target is \(+p\pmod{p^2}\).

By contrast, Proposition 16 is applied **after the quartic local-parameter normalization** and yields

\[
\widetilde{\mathfrak a}_p\widetilde{\mathfrak b}_p\equiv-p\pmod{p^2}.
\]

The opposite first-digit signs are therefore expected and encode the quartic/differential/hypergeometric comparison. They must not be erased by identifying twisted and untwisted coefficient coordinates.

## 5. Rigorous comparison defect with the weighted Ramanujan truncation

Let

\[
W_p:=\sum_{k=0}^{p-1}(6k+1)
\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k}.
\]

The proved first-digit statements are

\[
W_p\equiv p\pmod{p^2},
\qquad
\widetilde{\mathfrak a}_p\widetilde{\mathfrak b}_p\equiv-p\pmod{p^2}.
\]

Therefore the following **complete comparison defect** is well-defined:

\[
\boxed{
\chi_p:=
\frac{W_p+\widetilde{\mathfrak a}_p\widetilde{\mathfrak b}_p}{p^2}
\pmod p.
} \tag{COMPARE2}
\]

This scalar packages exactly the one-extra-digit information lost when passing from the quartic-normalized de Rham product to the weighted truncated \({}_3F_2\) observer. It may contain contributions from the quartic normalization, the differential combination defining the \((6k+1)\)-weight, and the truncation/Clausen comparison. No unproved splitting among those contributions is assumed.

Using `(RAW-DEFECT)`,

\[
W_p
\equiv
-\widetilde{\mathfrak a}_p\widetilde{\mathfrak b}_p+p^2\chi_p
\equiv
p+p^2(\chi_p-\mathcal F_p)
\pmod{p^3}.
\]

Hence

\[
\boxed{
\frac{W_p-p}{p^2}
\equiv
\chi_p-\mathcal F_p
\equiv
\chi_p-U^2+e_a+e_b
\pmod p.
} \tag{W2JET}
\]

Thus the full weighted mod-\(p^3\) strengthening is equivalent to the two-coordinate identity

\[
\boxed{
\chi_p\equiv U^2-e_a-e_b\pmod p.
} \tag{HEIGHT2-LIFT}
\]

## 6. Exact normalization map to the frozen Enterprise parent LIFT scalar

To avoid the parent notation collision, write

\[
g:=\sum_{k=0}^{p-1}B_k,\qquad
h:=\sum_{k=0}^{p-1}(12k+1)B_k,
\qquad \widehat G_p:=g/p.
\]

The frozen finite Clausen product is an exact finite convolution. For degrees \(n<p\), the product coefficients are exactly the coefficients of \(W_p\); degrees \(p\le n\le2p-2\) form the finite convolution tail \(T_p\). Therefore

\[
\boxed{gh=W_p+T_p.} \tag{FINITE-CLAUSEN}
\]

The accepted parent reduction gives

\[
T_p\equiv p^2R_p\pmod{p^3}. \tag{TAIL}
\]

Since \(p\mid g\), divide by \(p^2\). Modulo \(p\),

\[
\begin{aligned}
\frac{W_p-p}{p^2}
&\equiv
\frac{gh-p}{p^2}-R_p\\
&=
\frac{\widehat G_p h-1}{p}-R_p.
\end{aligned}
\tag{PARENT-W2}
\]

Thus the parent LIFT residual is **exactly the weighted second p-adic digit**:

\[
\boxed{
\mathcal L_p:=
\frac{\widehat G_p h-1}{p}-R_p
\equiv
\frac{W_p-p}{p^2}
\pmod p.
} \tag{LIFT=W2}
\]

Combining `(LIFT=W2)` with `(W2JET)` yields the corrected master interface

\[
\boxed{
\mathcal L_p
\equiv
\chi_p-U^2+e_a+e_b
\pmod p.
} \tag{MASTER-LIFT}
\]

Therefore

\[
\boxed{
LIFT\iff \chi_p\equiv U^2-e_a-e_b\pmod p.
} \tag{LOCAL-LIFT}
\]

There is no missing proportionality constant or sign at the **complete LIFT observer**. No termwise identification of \(R_p\) with a single Frobenius or comparison coordinate is asserted or required.

## 7. New smallest interfaces

The previous four-coordinate draft is replaced by two combined coordinates:

1. `FROB2`: \(\mathcal F_p=U^2-e_a-e_b\), the next supersingular height-2 Frobenius/de Rham digit;
2. `COMPARE2`: \(\chi_p\), the one-extra-digit comparison from the quartic-normalized de Rham product to the weighted truncated hypergeometric observer.

The remaining theorem is simply

\[
\boxed{\chi_p-\mathcal F_p\equiv0\pmod p.}
\]

This is strictly smaller and safer than separately postulating twist and Clausen digits before deriving their exact normalization.

## 8. BRC information audit

The frozen parent carrier

\[
(\widehat G_p\bmod p^2,h\bmod p^2,R_p)
\]

and the new pair

\[
(\mathcal F_p,\chi_p)
\]

are equivalent only for the declared future observer

\[
\text{“does the weighted second p-adic digit vanish?”}.
\]

No claim is made that \((\mathcal F_p,\chi_p)\) reconstructs \(R_p\), \(\widehat G_p\), or \(h\) individually. The quotient is operation-safe only at the LIFT observer.

`BRC_REUSE_RESOLUTION = REUSE_APPLIED + COMPOSE_APPLIED`.

## 9. Freeze

`JT0 = PROVED_BY_PRIOR_ART`.

`UR = PROVED_BY_PRIOR_ART_PLUS_FROZEN_EQUIVALENCE`.

`RAW_TWISTED_DERHAM_P3_DEFECT = STRICTLY_REDUCED_TO U^2-e_a-e_b`.

`UNSUPPORTED_SEPARATE_TWIST_PLUS_CLAUSEN_DIGIT_SPLIT = WITHDRAWN`.

`PARENT_LIFT_NORMALIZATION_MAP = PROVED_EXACTLY_AT_SECOND_DIGIT_OBSERVER`.

`PARENT_LIFT = EQUIVALENT_TO chi_p-U^2+e_a+e_b = 0 mod p / OPEN`.

`JT2 = OPEN`.

`WEIGHTED_W3 = OPEN`.

`NEW_THEOREM_CLAIM = NONE`.

`FINITE_SCAN_PROMOTION = NONE`.

`NEXT_ACTION = compute or structurally identify COMPARE2 chi_p and FROB2 in the same quartic-normalized coordinate system; prioritize proving their equality directly rather than decomposing chi_p without a coordinate-level derivation`.
