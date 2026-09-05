# BRC boundary-transfer algebra and the spectral formal-phase coordinate

Status: `FREE_RESEARCH / CROSS-LINE THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Primary issue: `#1159`
Cross-line source: `BRC_ROTATION_ATLAS_ALGEBRA_20260905.md`

## 0. Scope

The current BRC program explicitly seeks an algebraic interface in which coordinate behavior is visible in the algebra itself, without erasing axis/frame records.  The #1159 finite Dirichlet program independently produced:

- finite `2x2` transfer recurrences;
- integer decimation maps `R_n`;
- a unique rational formal phase `ell` satisfying `ell(R_n(u))=n^2 ell(u)`.

This note identifies an exact common interface.

The bridge applies to a declared `2x2` invertible boundary-transfer block over a characteristic-zero fraction field.  It does **not** claim that every BRC module is automatically `2x2`, determinant one, or a primitive Cell rotation.  The current BRC Schur-elimination task is the natural place where such a boundary block may arise.

---

## 1. A rational projective trace coordinate

Let `A` be an invertible `2x2` matrix over a characteristic-zero field, with

\[
t=\operatorname{tr}A,
\qquad
\delta=\det A\ne0.
\]

Define the scalar

\[
\boxed{
X(A):=\frac{t^2}{\delta}-2
}
\tag{BT-1}
\]

and its trace-defect form

\[
\boxed{
u_{\rm pr}(A):=2-X(A)=4-\frac{t^2}{\delta}.}
\tag{BT-2}
\]

These are invariant under global scalar rescaling:

\[
X(cA)=X(A),
\qquad
u_{\rm pr}(cA)=u_{\rm pr}(A)
\]

for every nonzero scalar `c`.

This matters for BRC weighted transfer matrices: the coordinate reads the projective transfer geometry rather than an arbitrary common normalization of path weights.

---

## 2. Pure Cayley-Hamilton proof of the decimation law

The elementary `2x2` identity

\[
(\operatorname{tr}B)^2-2\det B=\operatorname{tr}(B^2)
\]

gives, for every `n>=1`,

\[
X(A^n)
=\frac{\operatorname{tr}(A^n)^2}{\delta^n}-2
=\frac{\operatorname{tr}(A^{2n})}{\delta^n}.
\tag{BT-3}
\]

Now set

\[
B:=\frac{A^2}{\delta}.
\]

Then

\[
\det B=1,
\qquad
\operatorname{tr}B=X(A).
\]

For determinant-one `2x2` matrices, Cayley-Hamilton gives the rescaled Chebyshev/Dickson trace recurrence

\[
\operatorname{tr}(B^n)=C_n(\operatorname{tr}B),
\]

where

\[
C_0(x)=2,
\quad C_1(x)=x,
\quad C_{n+1}(x)=xC_n(x)-C_{n-1}(x).
\]

Hence

\[
\boxed{X(A^n)=C_n(X(A)).}
\tag{BT-4}
\]

Define the #1159 integer spectral decimation polynomial

\[
R_n(u):=2-C_n(2-u).
\]

Then (BT-4) is exactly

\[
\boxed{
u_{\rm pr}(A^n)=R_n(u_{\rm pr}(A)).}
\tag{BT-5}
\]

No eigenvalue, trigonometric function, circle, or square-root normalization is used.

Classification: `EXACT_2X2_PROJECTIVE_TRANSFER_ALGEBRA`.

---

## 3. The formal phase becomes an operation-safe scale chart

Let `ell(u) in Q[[u]]` be the unique normalized common linearizer from #1159:

\[
\ell(u)=u+O(u^2),
\qquad
\ell(R_n(u))=n^2\ell(u).
\]

Apply this to (BT-5):

\[
\boxed{
\ell(u_{\rm pr}(A^n))
=n^2\ell(u_{\rm pr}(A)).
}
\tag{BT-6}
\]

Thus for the declared operation “replace a boundary-transfer block by `n` repeated copies”, the nonlinear rational matrix observable is converted into exact multiplication by `n^2`.

This is an operation-safe scalar chart for that **specific scale semigroup**.

It is not a claim that `ell` is a safe quotient for arbitrary BRC path composition, arbitrary port attachment, or arbitrary frame-sensitive observation.  The BRC warning “a scalar summary need not be future-operation safe” remains in force outside the stated power/scale operation.

---

## 4. Relation to the #1159 Dirichlet transfer

The native Dirichlet transfer is

\[
T(u)=
\begin{pmatrix}
2-u&-1\\
1&0
\end{pmatrix},
\qquad
\det T(u)=1,
\qquad
\operatorname{tr}T(u)=2-u.
\]

Its projective defect is

\[
\begin{aligned}
u_{\rm pr}(T(u))
&=4-(2-u)^2\\
&=u(4-u)\\
&=R_2(u).
\end{aligned}
\]

Therefore

\[
\boxed{
u_{\rm pr}(T(u))=R_2(u).}
\tag{BT-7}
\]

The projective BRC observable automatically performs the same two-to-one complement quotient that appears in #1159 even-site decimation.

Since

\[
\ell(R_2(u))=4\ell(u),
\]

we also have

\[
\boxed{
\ell(u_{\rm pr}(T(u)))=4\ell(u).
}
\tag{BT-8}
\]

This gives a precise reason the projective transfer coordinate reads a **squared/doubled phase scale** rather than the oriented one-step phase itself.

---

## 5. Why frame/sign information cannot simply be deleted

The projective coordinate is invariant under

\[
A\mapsto -A.
\]

Thus it cannot distinguish the two trace sheets `tr A` and `-tr A`.  In the Dirichlet parameter this is the complement involution

\[
u\longleftrightarrow4-u.
\]

So the rational scalar chart is intrinsically an **unoriented / squared-phase quotient**.

Locally one may adjoin an oriented coordinate `eta` with

\[
\eta^2=\ell(u),
\]

in which repetition acts as

\[
\eta\mapsto \pm n\eta.
\]

Choosing the sign requires a sheet/orientation choice.  This is exactly the kind of information BRC currently retains in the frame variable rather than erasing from the algebra.

Therefore the bridge supports, rather than bypasses, the current BRC design principle:

`PROJECTIVE_SCALAR_COORDINATE != FULL_FRAME_STATE`.

`ORIENTED_PHASE_LIFT_REQUIRES_EXTRA_SHEET/FRAME_DATA`.

---

## 6. Direct relevance to the current BRC Schur-module task

The BRC rotation-atlas program's next unfinished unit is boundary-port Schur elimination with retained frames.  The theorem above supplies a concrete post-elimination test.

If a rotation-stable module produces an invertible `2x2` boundary transfer `A` over the BRC rational-function coefficient field, then the following checks are exact and algebraic:

1. compute `tr A` and `det A` without choosing roots;
2. form
   `u_pr(A)=4-(tr A)^2/det A`;
3. repeat/compose the same module `n` times and independently eliminate the interior;
4. verify
   `u_pr(A^n)=R_n(u_pr(A))`;
5. in formal phase, verify
   `ell(u_pr(A^n))=n^2 ell(u_pr(A))`;
6. under the 24-element atlas variable permutation, verify the scalar is invariant or transforms according to the declared boundary-index action.

Failure of step 4 after Schur elimination would be direct evidence that the chosen scalar block does not represent simple repetition, that a boundary normalization was erased, or that an operation-sensitive frame/port variable has been lost.

This is stronger than comparing numerical roots of two transfer matrices.

---

## 7. General determinant-one specialization

When the boundary transfer is already normalized to `det A=1`, one may retain the signed trace defect

\[
u(A)=2-\operatorname{tr}A.
\]

Then

\[
u(A^n)=R_n(u(A))
\]

directly, without the preliminary projective squaring.  This retains the trace sheet and is the exact #1159 transfer coordinate.

The projective formula (BT-5) is the square-root-free fallback when no canonical determinant-one normalization exists in the BRC coefficient field.

---

## 8. Structural bridge

The cross-line picture is now:

```text
BRC finite path/frame algebra
  -> finite-state lift to ordinary commutative transfer matrices
  -> boundary/Schur module elimination
  -> 2x2 invertible boundary transfer A
  -> rational projective trace defect u_pr(A)
  -> integer decimation semigroup R_n under module repetition
  -> unique formal phase ell
  -> exact algebraic scale coordinate ell(u_pr(A^n)) = n^2 ell(u_pr(A))
```

This is a genuine coordinate-algebra interface: the scale coordinate is forced by finite matrix composition and formal algebra, not imported from Euclidean angle notation.

Freeze at free-research strength:

`BRC_2X2_PROJECTIVE_TRACE_DEFECT -> SPECTRAL_DECIMATION`.

`SPECTRAL_FORMAL_PHASE -> EXACT_OPERATION_SAFE_SCALE_CHART_FOR_REPETITION`.

`FRAME_RETENTION -> NECESSARY_FOR_ORIENTED_LIFT`.

Hard boundary: none of this proves that every BRC module admits a `2x2` boundary transfer, that every such transfer is a primitive P000 Cell rotation, or that the projective scalar alone is a complete BRC state.
