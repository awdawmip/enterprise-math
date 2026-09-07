# Height-2 supersingular Frobenius second-digit reduction

Status: `STRICT_LOCAL_REDUCTION / EXACT_PARENT_NORMALIZATION_MAP / NO_P3_CLOSURE_CLAIM`

Date: `2026-09-08`

Researcher-ID: `EM-UR24-7C91A0`

Parent continuation: `ur_chisholm_closure_lift_frontier_20260908.md`

## 1. Purpose

The Chisholm–Deines–Long–Nebe–Swisher proof closes the raw supersingular de Rham coefficient product only modulo \(p^2\). This note retains one additional formal p-adic digit and isolates the exact local data that would be needed for a mod-\(p^3\) refinement.

This is an algebraic reduction of the proof interface. It does **not** prove the parent `LIFT`, `JT2`, or the weighted Ramanujan congruence modulo \(p^3\).

## 2. Supersingular matrix normalization

Use Proposition 16 notation. Let

\[
\mathfrak a_p:=a(p-1),\qquad \mathfrak b_p:=b(p-1)
\]

for the two normalized de Rham coefficient sequences attached to \(\omega\) and \(\nu\).

In the present totally-real base-field normalization, the constant term in the ASD/Frobenius characteristic polynomial is \(b_2=p\). In the supersingular case the degree-\(p\) square-root lift used in the proof has matrix

\[
M=\begin{pmatrix}u&v\\ w&-u\end{pmatrix}
\]

with

\[
-u^2-vw=p. \tag{D}
\]

The proof establishes

\[
u\equiv0\pmod p,\qquad v\equiv0\pmod p,\qquad w\in A^\times,
\]

and

\[
1\equiv \frac{v\mathfrak b_p}{p}\pmod p,
\qquad
1\equiv \frac{w\mathfrak a_p}{p}\pmod p. \tag{C1}
\]

Consequently \(\mathfrak a_p\) is divisible by \(p\), whereas \(\mathfrak b_p\) is a unit.

Write

\[
u=pU,\qquad v=pV,\qquad w=W,\qquad \mathfrak a_p=pA,
\]

where \(V,W,A,\mathfrak b_p\) are units modulo \(p\). Define the two **coefficient-comparison defect digits**

\[
e_a:=\frac{WA-1}{p}\pmod p,
\qquad
e_b:=\frac{V\mathfrak b_p-1}{p}\pmod p. \tag{E}
\]

These are well-defined by `(C1)`.

## 3. Exact second-digit algebra

Divide `(D)` by \(p\):

\[
-pU^2-VW=1,
\]

so

\[
VW=-1-pU^2. \tag{VW}
\]

From `(E)`, modulo \(p^2\),

\[
A=W^{-1}(1+pe_a),
\qquad
\mathfrak b_p=V^{-1}(1+pe_b).
\]

Therefore

\[
\begin{aligned}
\mathfrak a_p\mathfrak b_p
&=pA\mathfrak b_p\\
&=p(VW)^{-1}(1+p(e_a+e_b))\\
&\equiv p(-1+pU^2)(1+p(e_a+e_b))\pmod{p^3}\\
&\equiv -p+p^2\bigl(U^2-e_a-e_b\bigr)\pmod{p^3}.
\end{aligned}
\]

Hence the one-order refinement of the raw de Rham product is controlled by the single scalar

\[
\boxed{
\mathcal F_p:=U^2-e_a-e_b\pmod p.
} \tag{FROB2}
\]

Equivalently,

\[
\boxed{
\frac{\mathfrak a_p\mathfrak b_p+p}{p^2}\equiv\mathcal F_p\pmod p.
} \tag{RAW-DEFECT}
\]

This is stronger than the previous qualitative statement “retain the next height-2 Frobenius digit”: the raw second digit factors into exactly

1. the diagonal Frobenius jet \(U=u/p\bmod p\);
2. the \(\omega\)-coefficient comparison defect \(e_a\);
3. the \(\nu\)-coefficient comparison defect \(e_b\).

No other matrix entry is independently needed at this algebraic level because the determinant relation eliminates \(VW\).

## 4. Twist digit

The 2013 proof applies a quartic normalization/twist. In the present \(d=3,\lambda=1/2\) lane its mod-\(p\) value is the Legendre symbol

\[
\left(\frac{1-\lambda}{p}\right)
=\left(\frac{1/2}{p}\right)=-1.
\]

Let the exact p-adic twist factor appearing in the de Rham-product-to-Ramanujan comparison be denoted \(\Theta_p\), normalized so that

\[
\Theta_p\equiv-1\pmod p.
\]

Define its next digit

\[
\tau_p:=\frac{\Theta_p+1}{p}\pmod p. \tag{TWIST}
\]

Then `(RAW-DEFECT)` gives

\[
\mathfrak a_p\mathfrak b_p\Theta_p
\equiv
p-p^2(\mathcal F_p+\tau_p)
\pmod{p^3}. \tag{TWISTED-DEFECT}
\]

Thus even before the truncated-Clausen correction is considered, the height-2 contribution has been compressed to the two scalars

\[
\mathcal F_p,\qquad \tau_p.
\]

## 5. Truncated-Clausen defect

Let \(W_p\) be the target weighted \({}_3F_2\) truncation. The 2013 theorem proves

\[
W_p\equiv \mathfrak a_p\mathfrak b_p\Theta_p\equiv p\pmod{p^2}
\]

in this lane, so the residual

\[
\kappa_p:=
\frac{W_p-\mathfrak a_p\mathfrak b_p\Theta_p}{p^2}
\pmod p \tag{CLAUSEN2}
\]

is well-defined.

Combining `(TWISTED-DEFECT)` and `(CLAUSEN2)` yields the exact normalized weighted second digit

\[
\boxed{
\frac{W_p-p}{p^2}
\equiv
\kappa_p-\mathcal F_p-\tau_p
\pmod p.
} \tag{W2JET}
\]

Therefore the desired weighted mod-\(p^3\) strengthening is equivalent to

\[
\boxed{
\kappa_p\equiv \mathcal F_p+\tau_p\pmod p.
} \tag{HEIGHT2-LIFT}
\]

This is a strict three-source factorization of the missing second digit:

- `FROB2`: height-2 Frobenius/de Rham matrix jet;
- `TWIST`: one additional digit of the quartic CM normalization;
- `CLAUSEN2`: one additional digit of the truncated Clausen comparison.

## 6. Exact normalization map to the frozen parent LIFT scalar

To avoid the parent notation collision, write

\[
g:=\sum_{k=0}^{p-1}B_k,\qquad
h:=\sum_{k=0}^{p-1}(12k+1)B_k,
\qquad \widehat G_p:=g/p.
\]

The frozen finite Clausen product is an exact finite convolution. For degrees \(n<p\), the product coefficients coincide with the target weighted \({}_3F_2\) coefficients, while the degrees \(p\le n\le2p-2\) form the finite convolution tail \(T_p\). Hence

\[
\boxed{gh=W_p+T_p.} \tag{FINITE-CLAUSEN}
\]

The accepted parent theorem gives

\[
T_p\equiv p^2R_p\pmod{p^3}. \tag{TAIL}
\]

Since \(p\mid g\), divide the resulting identity by \(p^2\). Modulo \(p\),

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

Therefore the frozen parent `LIFT` residual is **exactly the weighted second p-adic digit**, with no missing proportionality factor or sign:

\[
\boxed{
\mathcal L_p:=
\frac{\widehat G_p h-1}{p}-R_p
\equiv
\frac{W_p-p}{p^2}
\pmod p.
} \tag{LIFT=W2}
\]

Combining `(LIFT=W2)` with `(W2JET)` gives the exact bridge between the Enterprise parent language and the supersingular height-2 Frobenius language:

\[
\boxed{
\mathcal L_p
\equiv
\kappa_p-\mathcal F_p-\tau_p
\equiv
\kappa_p-U^2+e_a+e_b-\tau_p
\pmod p.
} \tag{MASTER-LIFT}
\]

Thus the normalization-map problem left open in the first version of this note is now closed.

No termwise identity such as \(R_p=\kappa_p\) is implied or needed. The equality is at the level of the **complete normalized second-digit obstruction**.

## 7. New smallest interfaces

The parent `LIFT` has now been strictly factorized into four local/finite coordinates:

1. `FROB-DIAG`: compute/prove \(U=u/p\bmod p\);
2. `FROB-COMP`: compute/prove \(e_a+e_b\bmod p\) (the two defects are only needed through their sum);
3. `CM-TWIST`: compute \(\tau_p\bmod p\);
4. `CLAUSEN2`: compute \(\kappa_p\bmod p\).

The desired theorem is the single equality

\[
\boxed{
\kappa_p-U^2+e_a+e_b-\tau_p\equiv0\pmod p.
} \tag{LOCAL-LIFT}
\]

The determinant identity shows that separately computing \(V\) and \(W\) beyond what is needed for \(e_a+e_b\) is unnecessary information inflation. The frozen reflected scalar \(R_p\) also no longer has to be separately matched to one local Frobenius coefficient: its role is already incorporated exactly through `(LIFT=W2)`.

## 8. BRC information audit

The previous carrier

\[
(\widehat G_p\bmod p^2,h\bmod p^2,R_p)
\]

and the new carrier

\[
(U,e_a+e_b,\tau_p,\kappa_p)
\]

have now been proved equivalent **for the sole future observer “does the weighted second digit vanish?”** through `(MASTER-LIFT)`.

This does not license arbitrary replacement for other future operations. In particular, no claim is made that the four local coordinates reconstruct \(R_p\), \(\widehat G_p\), or \(h\) individually. The quotient is operation-safe only at the declared LIFT observer.

`BRC_REUSE_RESOLUTION = REUSE_APPLIED + COMPOSE_APPLIED`.

## 9. Freeze

`RAW_DERHAM_P3_DEFECT = STRICTLY_REDUCED_TO U^2-e_a-e_b`.

`WEIGHTED_P3_DEFECT = STRICTLY_REDUCED_TO kappa_p-F_p-tau_p`.

`PARENT_LIFT_NORMALIZATION_MAP = PROVED_EXACTLY_AT_SECOND_DIGIT_OBSERVER`.

`PARENT_LIFT = EQUIVALENT_TO kappa_p-U^2+e_a+e_b-tau_p = 0 mod p / OPEN`.

`JT2 = OPEN`.

`NEW_THEOREM_CLAIM = NONE`.

`FINITE_SCAN_PROMOTION = NONE`.

`NEXT_ACTION = attack the four-coordinate local identity, first seeking structural cancellation between the coefficient-comparison sum e_a+e_b and the truncated-Clausen defect kappa_p before separately computing all four coordinates`.
