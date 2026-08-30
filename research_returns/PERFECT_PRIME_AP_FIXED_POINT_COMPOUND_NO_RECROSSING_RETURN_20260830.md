# Perfect Prime AP fixed-point compound no-recrossing — Research Return

Researcher-ID: `EM-PPTAPFPC1-9C4E71`  
Task: `RS-PERFECT-PRIME-AP-FIXED-POINT-COMPOUND-NO-RECROSSING`  
Publication: `TP2-91C7E4A25D0B638F4E1A`  
Claim: `chatgpt-pptapfpc1-20260830-2248-9c4e71`  
Execution record: `ER-9A61F2C308DE475B1C77`  
Reserved Result-ID: `RR-7D4B2E9C1A6F3058C4D1`

## Terminal verdict

`PARTIAL_EXACT_PROGRESS / ADJACENT_CAUCHY_LAYER_NO_RECROSSING_PROVED_ALL_M / FULL_BINOMIAL_INTERFERENCE_OPEN`

Hard target:

`AP_FIXED_POINT_COMPOUND_NO_RECROSSING_PROVED_OR_EXACTLY_OBSTRUCTED`

remains **open**. This execution does not promote finite computation to an all-`m` theorem.

The exact new theorem is narrower but genuinely all-`m`: every adjacent pair of the Cauchy layers underlying the AP Christoffel deformation has only the forced gauge kernel throughout `0<t<=1`. The unique possible nongauge singular parameter is explicit and lies strictly to the right of `1`. For the first AP layer it is

\[
t_* = \frac{3m^2+1}{m^2+1}>2.
\]

The full AP deformation is an `m`-term alternating binomial superposition of these Cauchy layers. Pairwise nonrecrossing does not by itself control interference among three or more layers. The remaining hard target is therefore reduced to one explicit scalar cofactor-positivity/nonvanishing lemma for that binomial superposition.

A finite exact discovery packet for the actual AP cofactor, `m=2,3,4,5`, has a stronger pattern: after removing the forced factor `t^(m-1)`, the Möbius transform to `x=t/(1-t)` has all coefficients strictly positive. This is retained as a proof target and regression guard only.

---

## 1. Frozen AP defect and a canonical scalar invariant

Put

- `n=m-1`,
- `a=m^2`,
- `x_i=i+1`, `i=0,...,n`,
- `y_j=mj`, `j=0,...,n`,
- `w_i=(-1)^i binom(n,i)`,
- `W=diag(w)`.

The accepted deformation is

\[
H_t(i,j)
=\int_0^1 u^{i+mj}(1-tu^{m^2})^n\,du
=\sum_{s=0}^{n}\frac{(-1)^s\binom ns t^s}{x_i+y_j+a s}.
\]

Let

\[
e_t=H_tw,\qquad d_t=H_t^Tw,
\]
\[
E_t=\operatorname{diag}(e_t),\qquad D_t=\operatorname{diag}(d_t).
\]

The accepted signed bipartite Laplacian is

\[
L_t=
\begin{pmatrix}
WE_t&-WH_tW\\
-WH_t^TW&WD_t
\end{pmatrix}.
\]

Its row sums vanish, so the all-ones bipartite gauge vector is always in `ker L_t`. Since `E_t` is positive and hence `WE_t` is invertible on `0<=t<=1`, its Schur complement is, up to invertible diagonal factors, the accepted fixed-point defect:

\[
WD_t-WH_t^TWE_t^{-1}H_tW
\sim D_tW(I-K_t)
\sim \Gamma_t.
\]

Therefore the following are equivalent for `0<t<=1`:

1. the fixed eigenvalue `1` of `K_t` is simple;
2. `rank Gamma_t=m-1`;
3. `rank L_t=2m-1`;
4. any one Laplacian gauge cofactor is nonzero.

Fix the canonical scalar

\[
\tau_m(t):=\det L_t[\widehat{2m},\widehat{2m}],
\]

obtained by deleting the last row and column. This is an explicit maximal proper minor allowed by the taskbook. The hard target is equivalently

\[
\tau_m(t)\ne0
\qquad
(m\ge2,\ 0<t\le1).
\]

The matrix-tree interpretation is signed: `tau_m(t)` is the signed spanning-tree sum of the complete bipartite graph with edge weights

\[
c_{ij}(t)=w_iw_jH_t(i,j).
\]

No positivity of individual edge weights is assumed.

---

## 2. Exact Cauchy-layer decomposition

For a general shift step `b>0` define, for every integer `s>=0`,

\[
H_s^{(b)}(i,j)=\frac1{x_i+y_j+bs}.
\]

Write

\[
e^{(s)}=H_s^{(b)}w,\qquad
E_s=\operatorname{diag}(e^{(s)}),
\]

and similarly `d^(s),D_s`. Define

\[
A_s=E_s^{-1}H_s^{(b)}W
\]

and the corresponding signed Cauchy-layer Laplacian

\[
M_s=
\begin{pmatrix}
WE_s&-WH_s^{(b)}W\\
-W(H_s^{(b)})^TW&WD_s
\end{pmatrix}.
\]

Linearity of `H -> (H, Hw, H^Tw)` gives the exact AP decomposition, with `b=m^2`:

\[
\boxed{
L_t=\sum_{s=0}^{n}(-1)^s\binom ns t^s M_s.
}
\]

Thus the full AP problem is a matrix-valued finite difference of exact Cauchy layers.

---

## 3. Cauchy interpolation model for every layer

Let `q_j=f(y_j)` for the unique polynomial `f` of degree at most `n`. The Cauchy/Lagrange identity gives

\[
(A_sq)_i=f(-x_i-bs).
\]

So `A_s` is exactly the polynomial translation/evaluation map from the `y`-grid to the shifted negative `x`-grid.

In particular, if

\[
R_s:=WE_s,
\]

then the layer Laplacian has the exact rank factorization

\[
\boxed{
M_s=
\begin{bmatrix}I\\-A_s^T\end{bmatrix}
R_s
\begin{bmatrix}I&-A_s\end{bmatrix}.
}
\]

Hence

\[
\ker M_s
=
\{(A_sq,q):q\in\mathbf Q^m\},
\]

an `m`-dimensional Cauchy interpolation graph. This recovers the maximally degenerate Cauchy endpoint without invoking generic total positivity.

---

## 4. All-m adjacent-layer no-recrossing theorem

### Theorem

For every

\[
m\ge2,\qquad b>0,\qquad s\ge0,\qquad 0<t\le1,
\]

the pencil

\[
M_s-tM_{s+1}
\]

has kernel exactly the one-dimensional gauge space.

Equivalently, its canonical gauge cofactor never vanishes on `0<t<=1`.

More sharply, if a nongauge kernel exists for `t!=0`, then necessarily

\[
\boxed{
t=t_s^*
=
\frac{\frac{m^2+1}{2}+b(s+1)}
     {\frac{m^2+1}{2}+bs}
=
1+\frac{b}{\frac{m^2+1}{2}+bs}
>1.
}
\]

Thus there is no nongauge singularity in the task interval.

### Proof

Take `z=(p,q)` in the kernel of `M_s-tM_{s+1}` and put

\[
h_r=R_r(p-A_rq).
\]

Using the factorization above, the top block of

\[
(M_s-tM_{s+1})z=0
\]

gives

\[
h_s=t h_{s+1}=:h.
\]

The bottom block then gives

\[
(A_{s+1}-A_s)^Th=0.
\]

Under polynomial coordinates,

\[
A_{s+1}-A_s
\]

is the evaluation of the translation difference

\[
f(X)\longmapsto f(X-b)-f(X)
\]

on degree-`<=n` polynomials. Its kernel is exactly the constants and its image is the degree-`<=n-1` polynomial evaluation space. The one-dimensional left annihilator of that space on the `m=n+1` consecutive `x`-nodes is

\[
w=(((-1)^i\binom ni))_{i=0}^{n}.
\]

Hence either `h=0` or `h=cw` for a nonzero scalar `c`.

If `h=0`, then `p=A_sq=A_{s+1}q`. The interpolation polynomial satisfies a nonzero translation period `b`; a polynomial with a nonzero period is constant. Thus `z` is only the gauge vector.

Now suppose `h=cw`, `c!=0`. Since

\[
h_s=cw,\qquad h_{s+1}=cw/t,
\]

we have

\[
p-A_sq=cR_s^{-1}w,
\]
\[
p-A_{s+1}q=(c/t)R_{s+1}^{-1}w.
\]

Subtracting and applying the left annihilator `w^T` of `A_{s+1}-A_s` yields the necessary scalar condition

\[
\frac1t\,w^TR_{s+1}^{-1}w
-
w^TR_s^{-1}w
=0,
\]

so

\[
t=
\frac{w^TR_{s+1}^{-1}w}
     {w^TR_s^{-1}w}.
\]

The alternating Cauchy normalizer is exact:

\[
e_i^{(s)}
=
\sum_{j=0}^{n}
\frac{(-1)^j\binom nj}{x_i+mj+bs}
=
\frac{n!m^n}
{\prod_{j=0}^{n}(x_i+mj+bs)}.
\]

Since `R_s=WE_s`,

\[
w^TR_s^{-1}w
=
\sum_{i=0}^{n}\frac{w_i}{e_i^{(s)}}.
\]

Set

\[
P_s(X)=\prod_{j=0}^{n}(X+mj+bs).
\]

Then

\[
w^TR_s^{-1}w
=
\frac1{n!m^n}
\sum_{i=0}^{n}(-1)^i\binom ni P_s(i+1).
\]

The polynomial `P_s` is monic of degree `m=n+1`, and its `X^(m-1)` coefficient is

\[
mbs+\frac{m^2(m-1)}2.
\]

Using

\[
\Delta^{m-1}X^m
=
m!\left(X+\frac{m-1}{2}\right),
\qquad
\Delta^{m-1}X^{m-1}=(m-1)!,
\]

at `X=1` gives

\[
\sum_{i=0}^{n}(-1)^i\binom niP_s(i+1)
=
(-1)^n\,m!\left(
\frac{m^2+1}{2}+bs
\right).
\]

All `s`-independent factors cancel in the ratio, so

\[
t_s^*
=
\frac{\frac{m^2+1}{2}+b(s+1)}
     {\frac{m^2+1}{2}+bs}
>1.
\]

This contradicts `0<t<=1`. The only kernel on the task interval is therefore the gauge line. ∎

### AP first-layer corollary

For the actual AP spacing `b=m^2` and `s=0`,

\[
\boxed{
t_0^*=\frac{3m^2+1}{m^2+1}>2.
}
\]

So the first Christoffel insertion, viewed as a two-Cauchy-layer pencil, is globally nonrecrossing on `0<t<=1` for every `m>=2`.

This strengthens the previously accepted local `t=0` splitting theorem for the one-factor layer problem: the layer itself cannot recross anywhere in the interval.

---

## 5. Exact one-dimensional residue formula for each layer

The layer quadratic/bilinear form also admits an exact reduction that is useful for the full binomial problem.

Represent bipartite vectors by polynomials

\[
p_i=g(-x_i),\qquad q_j=f(y_j),
\]

and similarly a test vector by `h,k`, all of degree at most `n`. Then

\[
B_s((g,f),(h,k))
=
\sum_{i,j}
\frac{w_iw_j
[g(-x_i)-f(y_j)]
[h(-x_i)-k(y_j)]}
{x_i+y_j+bs}.
\]

Divide the numerator polynomial in variables `X,Y` by `X+Y+bs`. The remainder at `X=-Y-bs` is

\[
[g(Y+bs)-f(Y)]
[h(Y+bs)-k(Y)].
\]

The quotient has total degree at most `2n-1`. Hence every quotient monomial has either `X`-degree `<n` or `Y`-degree `<n`, and one of the two alternating binomial functionals annihilates it.

The exact result is therefore

\[
\boxed{
B_s((g,f),(h,k))
=
\sum_{j=0}^{n}
w_j\,c_s(y_j)
[g(y_j+bs)-f(y_j)]
[h(y_j+bs)-k(y_j)],
}
\]

where

\[
c_s(y)=
\frac{n!}
{\prod_{r=1}^{m}(y+bs+r)}
>0.
\]

This converts every two-dimensional Cauchy-layer form into a one-dimensional signed evaluation form. It is an exact Andréief/Cauchy–Binet entry point, not a heuristic.

For the full AP deformation,

\[
B_t
=
\sum_{s=0}^{n}
(-1)^s\binom ns t^s B_s.
\]

Thus all remaining difficulty is now concentrated in the interference of these exact one-dimensional residues across `s=0,...,n`.

---

## 6. Why the hard target is still open

The adjacent-layer theorem controls every two-layer face

\[
M_s-tM_{s+1}
\]

exactly. It does **not** imply that the full binomial combination

\[
\sum_{s=0}^{n}(-1)^s\binom ns t^sM_s
\]

stays in the same nonsingular quotient cone. Starting at `n>=2`, at least three layer forms interfere.

No valid induction is available merely by saying that multiplication by another positive Christoffel factor preserves the property. Generic positivity/strict-total-positivity statements are already known to be insufficient for the frozen normalized operator, and the accepted `m=3` derivative singularity and `m=10` non-real quotient pair block the two simplest differential/spectral replacements.

The new exact theorem therefore narrows, but does not close, the full task.

---

## 7. Finite exact actual-AP discovery: coefficientwise positivity after the forced factor

The checker reconstructs the exact cofactor polynomial `tau_m(t)` for `m=2,3,4,5`.

A `(2m-1)x(2m-1)` cofactor of a degree-`n` matrix polynomial has the safe degree bound

\[
\deg\tau_m\le n(2m-1).
\]

The checker interpolates at the full safe bound using exact rational arithmetic and independently evaluates at `t=1/2`.

For every tested `m`:

\[
\tau_m(t)=t^nq_m(t),
\qquad n=m-1,
\]

and the observed exact degree is

\[
\deg q_m=n(2m-3).
\]

Put `d=deg q_m` and make the interval Möbius change

\[
x=\frac{t}{1-t},
\qquad
\widehat q_m(x)
=
(1+x)^dq_m\!\left(\frac{x}{1+x}\right).
\]

Every coefficient of `\widehat q_m(x)` is strictly positive in the exact finite packet:

| `m` | `ord_0 tau_m` | `deg q_m` | positive coefficients of `qhat_m` |
|---:|---:|---:|---:|
| 2 | 1 | 1 | 2 / 2 |
| 3 | 2 | 6 | 7 / 7 |
| 4 | 3 | 15 | 16 / 16 |
| 5 | 4 | 28 | 29 / 29 |

The minimum transformed coefficient equals `tau_m(1)` in these four exact rows and is positive. The certificate records the exact fractions.

This proves positivity only for the listed finite cases. It is **not** evidence authority for the all-`m` statement.

Its value is diagnostic: coefficientwise positivity supplies a concrete stronger lemma whose proof would immediately close the task.

---

## 8. Smallest remaining lemma

A sufficient all-`m` closure statement is:

### `BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_LEMMA`

For every `m>=2`, with `n=m-1`, `b=m^2`, let

\[
L_t=
\sum_{s=0}^{n}
(-1)^s\binom ns t^sM_s.
\]

Let `tau_m(t)` be the fixed gauge cofactor above. Then

\[
\boxed{
\tau_m(t)/t^n>0
\qquad
(0<t\le1).
}
\]

A stronger coefficientwise version suggested by the exact `m<=5` packet is:

after choosing any valid all-`m` degree elevation `D>=deg q_m`, all coefficients of

\[
(1+x)^D q_m\!\left(\frac{x}{1+x}\right)
\]

are strictly positive.

Either statement closes the hard target, because nonzero `tau_m(t)` forces `rank L_t=2m-1`, hence `rank Gamma_t=m-1`.

The adjacent-layer theorem establishes every two-layer obstruction parameter explicitly beyond `1`; what remains is to control the determinant under the full binomial interference.

---

## 9. Route ledger and guards

### Proved in this execution

- canonical signed bipartite tree cofactor `tau_m(t)` is equivalent to fixed-point simplicity;
- exact AP decomposition into Cauchy layers `L_t=sum_s (-1)^s binom(n,s)t^s M_s`;
- exact interpolation-graph factorization of every `M_s`;
- all-`m`, all-`s`, all-`b>0` adjacent-layer no-recrossing theorem;
- explicit unique nongauge candidate parameter
  \[
  t_s^*=
  \frac{(m^2+1)/2+b(s+1)}
       {(m^2+1)/2+bs}>1;
  \]
- exact one-dimensional residue formula for each Cauchy layer;
- finite exact actual-AP transformed-coefficient positivity for `m=2..5`.

### Frozen negative boundaries inherited from accepted dependencies

- pointwise nondegeneracy of `Gamma'_t` is false already at `m=3`;
- universal full-spectrum GSTP / positive-real nonfixed spectrum is false at `m=10`;
- ordinary principal-angle/Hilbert contraction does not represent the frozen operator;
- generic Cauchy/STP structure alone does not remove the large fixed space at the unweighted endpoint.

### Not proved

- `tau_m(t)!=0` for all `m` and all `0<t<=1`;
- all-`m` coefficientwise positivity of the transformed cofactor;
- any Working Truth, Foundation, L4, or canonical theorem promotion.

---

## 10. Verification

Exact checker:

`research_checks/PERFECT_PRIME_AP_FIXED_POINT_COMPOUND_NO_RECROSSING_CHECK_20260830.py`

Machine-readable certificate:

`research_artifacts/PERFECT_PRIME_AP_FIXED_POINT_COMPOUND_NO_RECROSSING/exact_certificate_20260830.json`

The checker uses Python standard-library `Fraction` arithmetic only. It:

1. reconstructs the signed bipartite cofactor directly;
2. verifies the adjacent-layer exceptional-root formula for `m=2..8` and `s=0,1,2`, including exact zero at the predicted `t_s^*>1` and nonzero cofactor at `t=1`;
3. reconstructs the actual AP cofactor polynomial at the full safe determinant-degree bound for `m=2..5`;
4. verifies the forced order `m-1`;
5. verifies the observed finite degrees;
6. verifies every coefficient of the Möbius-transformed finite `q_m` is strictly positive.

Items 2–6 are finite regression/discovery. The all-`m` adjacent-layer theorem is the analytic/algebraic proof in Sections 3–4, not an inference from those tests.

---

## 11. Source exposure and provenance

This execution is nonblind. It used the accepted:

- `PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_RETURN_20260830.md`;
- `PERFECT_PRIME_BETA_BERNSTEIN_PRINCIPAL_ANGLE_RESULT_REFREEZE_V2_RETURN_20260830.md`;
- current Driver reviews that freeze the `m=3` derivative and `m=10` GSTP boundaries.

After CLAIM, the closed, unmerged supplemental PR `#947` was inspected as provenance-disclosed background. Its half-Pascal maximal-minor observations are not treated as source authority for this Result. The Cauchy-layer decomposition, adjacent-layer theorem, and explicit exceptional-root formula above are this execution's independently derived mathematical delta.

Cauchy matrices, Lagrange interpolation, Christoffel transformations, total positivity, and Cauchy biorthogonal-polynomial machinery are classical ingredients. No novelty claim is made for those ingredients.

Method-harvest disposition: `RESULT_ONLY`.

---

## 12. Recommended Driver action

Accept this Result as **partial exact mathematical progress**, not as parent closure.

Freeze the all-`m` adjacent-layer theorem and the explicit exceptional-root formula as reusable facts for the Perfect-Prime route. Preserve the full hard target as open.

The unique next mathematical unit is the full-binomial scalar invariant:

`BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_LEMMA`.

The first attack should use the exact one-dimensional residue formula in Section 5 to derive an Andréief/Cauchy–Binet, factorial-Schur, or discrete-sign-regular representation of the canonical gauge cofactor. The finite transformed-coefficient packet should be used only as falsification/regression guidance.

Do not reopen generic GSTP, real-spectrum inertia, pointwise `Gamma'_t` regularity, or ordinary Hilbert contraction as sufficient engines.

No Working Truth, Foundation, canonical promotion, or task completion is requested.
