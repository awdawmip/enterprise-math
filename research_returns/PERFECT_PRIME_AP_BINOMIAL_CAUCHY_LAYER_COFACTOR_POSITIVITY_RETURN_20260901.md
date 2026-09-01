# Perfect Prime AP binomial Cauchy-layer cofactor positivity — Research Return

Researcher-ID: `EM-PPTAPBCP1-646AAA`  
Task: `RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY`  
Publication: `TP2-5A3E91C7D2B40F681AC3`  
Claim: `chatgpt-pptabcp1-20260901-0907-r2`  
Execution record: `ER-5061202400CCD679FFE6`

## Terminal verdict

`NEGATIVE_BOUNDARY / EXACT_FULL_MULTILAYER_COVARIANCE_REDUCTION / INNER_POSITIVITY_MECHANISM_OBSTRUCTED / PARENT_NONVANISHING_OPEN`

The task hard target

`FULL_AP_BINOMIAL_CAUCHY_GAUGE_COFACTOR_NONVANISHING_ALL_M_PROVED_OR_EXACTLY_OBSTRUCTED`

is satisfied at the taskbook's permitted **mechanism-obstruction** strength, not at the positive parent-theorem strength.

This return does **not** prove or refute

\[
\tau_m(t)\ne0\qquad(m\ge2,\ 0<t\le1).
\]

Instead it gives an exact all-`m` Schur/covariance reduction of the complete alternating binomial Cauchy-layer interference to one `(m-1) x (m-1)` outer determinant, and proves that the most direct coefficientwise / conditional-variance / one-block Andreief positivity mechanism fails for every `m`: every inner signed conditional-covariance block has a fixed mixed inertia (except the one-dimensional `m=2` case, where it is strictly negative). The remaining parent problem is therefore isolated in the *outer alternating interference*, not in any individual positive block.

Finite exact arithmetic further extends the previously known Mobius/Bernstein coefficient-positivity pattern from `m<=5` through `m<=10`. That pattern is retained strictly as a successor target/regression and is not promoted to an all-`m` theorem.

---

## 1. Frozen input reproduced exactly

Put

\[
n=m-1,\qquad b=m^2,\qquad x_i=i+1,\qquad y_j=mj,
\]
\[
w_i=(-1)^i\binom ni,\qquad W=\operatorname{diag}(w).
\]

The accepted AP deformation is

\[
H_t(i,j)
=\int_0^1u^{i+mj}(1-tu^{m^2})^n\,du
=\sum_{s=0}^{n}\frac{(-1)^s\binom ns t^s}{x_i+y_j+bs}.
\]

Let

\[
e_t=H_tw,\quad d_t=H_t^Tw,\quad E_t=\operatorname{diag}(e_t),\quad D_t=\operatorname{diag}(d_t),
\]

and

\[
L_t=
\begin{pmatrix}
WE_t&-WH_tW\\
-WH_t^TW&WD_t
\end{pmatrix}.
\]

The all-ones bipartite vector is the gauge kernel. The canonical cofactor is

\[
\tau_m(t)=\det L_t[\widehat{2m},\widehat{2m}].
\]

The frozen exact layer decomposition is

\[
L_t=\sum_{s=0}^{n}(-1)^s\binom ns t^sM_s.
\]

The accepted adjacent-layer theorem is also retained without modification: for every `s>=0`, `b>0`,

\[
M_s-\theta M_{s+1}
\]

has only the gauge kernel on `0<theta<=1`; its unique possible nongauge singular parameter is

\[
\theta_s^*
=
\frac{\frac{m^2+1}{2}+b(s+1)}
     {\frac{m^2+1}{2}+bs}
>1.
\]

Nothing below infers the full multilayer theorem from that pairwise statement.

---

## 2. Exact one-dimensional layer residue

Represent left/right vectors by polynomials `g,f in P_n`:

\[
p_i=g(-x_i),\qquad q_j=f(y_j).
\]

For the Cauchy layer `s`, the accepted residue formula is

\[
B_s((g,f),(h,k))
=
\sum_{j=0}^{n}
w_j\,c_s(y_j)
[g(y_j+bs)-f(y_j)]
[h(y_j+bs)-k(y_j)],
\]

where

\[
c_s(y)
=
\frac{n!}{\prod_{r=1}^{m}(y+bs+r)}
=
\int_0^1u^{y+bs}(1-u)^n\,du
>0.
\]

Hence for the **full** AP superposition define

\[
z_{j,s}=y_j+bs,
\]

\[
\lambda_{j,s}(t)
=
(-1)^s\binom ns t^s c_s(y_j),
\]

and

\[
\mathcal D_j(t)
=
\sum_{s=0}^{n}\lambda_{j,s}(t).
\]

Then

\[
\mathcal D_j(t)
=
\int_0^1u^{y_j}(1-u)^n(1-tu^b)^n\,du
>0
\]

for `0<=t<=1`.

The full bilinear form is exactly

\[
B_t
=
\sum_{j=0}^{n}w_j
\sum_{s=0}^{n}\lambda_{j,s}(t)
[g(z_{j,s})-f(y_j)]
[h(z_{j,s})-k(y_j)].
\]

This formula contains all three-or-more-layer interference; no factorwise positivity has been substituted.

---

## 3. Exact conditional-covariance completion

For each `j`, define the signed mean functional

\[
\mu_j(g)
=
\frac{\sum_s\lambda_{j,s}g(z_{j,s})}{\mathcal D_j}
\]

and the signed conditional covariance

\[
\mathcal C_j(g,h)
=
\sum_s\lambda_{j,s}g(z_{j,s})h(z_{j,s})
-
\frac{
(\sum_s\lambda_{j,s}g(z_{j,s}))
(\sum_s\lambda_{j,s}h(z_{j,s}))
}{\mathcal D_j}.
\]

Completing the square gives the exact identity

\[
\boxed{
B_t((g,f),(h,k))
=
\sum_{j=0}^{n}
w_j\mathcal D_j
[f(y_j)-\mu_j(g)]
[k(y_j)-\mu_j(h)]
+
\mathcal S_t(g,h)
}
\]

with

\[
\boxed{
\mathcal S_t(g,h)
=
\sum_{j=0}^{n}w_j\mathcal C_j(g,h).
}
\]

Since evaluation `f -> (f(y_0),...,f(y_n))` is an isomorphism on `P_n`, the first term is an exactly diagonalizable right-variable block. Therefore **all remaining multilayer singularity is concentrated in `S_t` on left polynomials modulo constants**.

In the monomial quotient basis `X,X^2,...,X^n`, let

\[
C_j(t)_{rq}
=
\sum_s\lambda_{j,s}z_{j,s}^{r+q}
-
\frac{
(\sum_s\lambda_{j,s}z_{j,s}^{r})
(\sum_s\lambda_{j,s}z_{j,s}^{q})
}{\mathcal D_j},
\qquad 1\le r,q\le n,
\]

and

\[
\boxed{
S_m(t)=\sum_{j=0}^{n}w_j C_j(t).
}
\]

This is an `n x n = (m-1) x (m-1)` exact rational matrix.

---

## 4. Exact full-cofactor reduction theorem

Let `V_x` be the evaluation matrix from monomial coefficients of `g` to `(g(-x_0),...,g(-x_n))`. Since `-x_i=-1,-2,...,-m`,

\[
|\det V_x|
=
\prod_{k=1}^{n}k!.
\]

The polynomial-coordinate change followed by the square-completion change is invertible and has determinant `det V_x`. In the completed coordinates the full Gram matrix is congruent to

\[
S_m^{\mathrm{full}}(t)
\oplus
\operatorname{diag}(w_0\mathcal D_0,\ldots,w_n\mathcal D_n),
\]

where `S_m^full` has the constant polynomial as its gauge kernel and its nonconstant principal block is `S_m(t)`.

Using the adjugate congruence identity for the zero-row-sum Laplacian (valid also when the rank drops, in which case both sides vanish) gives the exact scalar identity

\[
\boxed{
\tau_m(t)
=
\frac{
\left(\prod_{j=0}^{n}w_j\mathcal D_j(t)\right)
\det S_m(t)
}{
\left(\prod_{k=1}^{n}k!\right)^2
}.
}
\]

Since every `D_j(t)>0` on `0<=t<=1` and every `w_j!=0`,

\[
\boxed{
\tau_m(t)\ne0
\iff
\det S_m(t)\ne0
\qquad(0<t\le1).
}
\]

Thus the original `(2m-1) x (2m-1)` cofactor problem is reduced exactly to one `(m-1) x (m-1)` outer alternating covariance determinant. This reduction uses the complete AP binomial superposition, not individual Cauchy factors.

---

## 5. Inner signed-covariance determinant and inertia — all `m`

Fix `m,j,t` with `t>0`. Put

\[
\Lambda_j=\operatorname{diag}(\lambda_{j,0},\ldots,\lambda_{j,n}),
\qquad
\lambda_j=(\lambda_{j,0},\ldots,\lambda_{j,n})^T,
\]

and

\[
A_j
=
\Lambda_j-\frac{\lambda_j\lambda_j^T}{\mathcal D_j}.
\]

Then `A_j 1=0`, and `C_j` is the pullback of `A_j` by the nonconstant Vandermonde evaluation map.

### 5.1 Exact determinant

For any deleted coordinate `k`, the matrix determinant lemma gives

\[
\det A_j[\widehat k,\widehat k]
=
\frac{\prod_{s=0}^{n}\lambda_{j,s}}{\mathcal D_j}.
\]

Let

\[
\Delta_j
=
\prod_{0\le r<s\le n}(z_{j,s}-z_{j,r}).
\]

The full Vandermonde matrix `[1 R_j]` sends the constant plus nonconstant polynomial coefficient basis to evaluation values at the `z_{j,s}`. Adjugate congruence therefore yields

\[
\boxed{
\det C_j(t)
=
\Delta_j^2
\frac{\prod_{s=0}^{n}\lambda_{j,s}(t)}
     {\mathcal D_j(t)}.
}
\]

All factors except the alternating `lambda` product have positive sign, so

\[
\operatorname{sgn}\det C_j
=
(-1)^{n(n+1)/2}.
\]

### 5.2 Exact inertia

Let

\[
e=\#\{s:0\le s\le n,\ s\text{ even}\}
=\lfloor n/2\rfloor+1,
\]

\[
o=\#\{s:0\le s\le n,\ s\text{ odd}\}
=\lceil n/2\rceil.
\]

Because `t>0` and `c_s>0`, the diagonal `Lambda_j` has inertia `(e,o,0)`.

Consider the bordered form

\[
G_j=
\begin{pmatrix}
\mathcal D_j&\lambda_j^T\\
\lambda_j&\Lambda_j
\end{pmatrix}.
\]

Its quadratic form is

\[
\mathcal D_j r^2+2r\lambda_j^Tx+x^T\Lambda_jx
=
\sum_s\lambda_{j,s}(r+x_s)^2.
\]

The invertible change `y_s=r+x_s` shows

\[
\operatorname{In}(G_j)=(e,o,1).
\]

Since `D_j>0`, Schur-complement inertia additivity gives

\[
\operatorname{In}(A_j)=(e-1,o,1).
\]

The sole zero direction is the constant vector. The Vandermonde evaluation map is an isomorphism, so on nonconstant polynomial coefficients,

\[
\boxed{
\operatorname{In}(C_j)
=
\left(
\lfloor n/2\rfloor,
\lceil n/2\rceil,
0
\right).
}
\]

Therefore:

- `m=2`: every inner block is strictly negative;
- every `m>=3`: every inner block is **indefinite**;
- this holds for every `j` and every `0<t<=1`.

This is the exact obstruction. The natural idea that the complete AP interference can be decomposed into positive conditional-variance blocks and then closed by termwise Andreief/Cauchy-Binet positivity is false at the block level for all `m>=3`.

An explicit smallest witness is `m=3,j=0,t=1`:

\[
C_0=
\frac1{16120}
\begin{pmatrix}
-2673&-12231\\
-12231&102303
\end{pmatrix},
\qquad
\det C_0=-\frac{6561}{4030}<0.
\]

---

## 6. Forced `t^(m-1)` order is reproduced

At `t=0`, only `s=0` survives in each inner distribution, hence every `C_j(0)=0`.

The first derivative is exact:

\[
\left.\frac{d}{dt}\mathcal C_j(g,h)\right|_{t=0}
=
-n\,c_1(y_j)
[g(y_j+b)-g(y_j)]
[h(y_j+b)-h(y_j)].
\]

Therefore

\[
S_m(t)=tS_m^{(1)}+O(t^2),
\]

where

\[
S_m^{(1)}(g,h)
=
-n\sum_jw_jc_1(y_j)
\Delta_b g(y_j)\Delta_b h(y_j).
\]

This is exactly the quotient crossing form already accepted in the all-`m` Christoffel/Cauchy endpoint analysis. Its nonconstant quotient is nondegenerate for every `m>=2`. Hence

\[
\det S_m(t)
=
t^n\det S_m^{(1)}+O(t^{n+1}),
\qquad
\det S_m^{(1)}\ne0,
\]

and the cofactor reduction gives

\[
\boxed{\operatorname{ord}_{t=0}\tau_m(t)=n=m-1.}
\]

Thus the predecessor's forced vanishing order is reproduced inside the new exact full-multilayer reduction rather than merely cited.

---

## 7. The second Cauchy endpoint and the Mobius variable

Set

\[
x=\frac{t}{1-t},
\qquad
t=\frac{x}{1+x}.
\]

Define the scaled moment matrix

\[
\widetilde H_x
=
(1+x)^nH_{x/(1+x)}.
\]

Then exactly

\[
\boxed{
\widetilde H_x(i,j)
=
\int_0^1u^{i+mj}
[1+x(1-u^{m^2})]^n\,du.
}
\]

Every entry is a polynomial in `x` with strictly positive coefficients.

Because `L` is linear in `H`,

\[
\widetilde L_x=(1+x)^nL_{x/(1+x)}.
\]

The canonical cofactor has size `2m-1=2n+1`. The same adjacent-layer local-splitting argument applied at the terminal Cauchy layer `M_n` shows that the reversed cofactor also loses exactly `n` top degrees. Consequently

\[
\deg\tau_m=2n^2,
\]

and after writing

\[
\tau_m(t)=t^n q_m(t),
\qquad
\deg q_m=n(2m-3),
\]

the Mobius/Bernstein polynomial

\[
\widehat B_m(x)
=
(1+x)^{n(2m-3)}
q_m\!\left(\frac{x}{1+x}\right)
\]

satisfies the exact endpoint factorization

\[
\boxed{
\det\widetilde L_x[\widehat{2m},\widehat{2m}]
=
x^n(1+x)^n\widehat B_m(x).
}
\]

Thus the two Cauchy endpoints force `x^n` and `(1+x)^n`. What remains is the sign structure of `Bhat_m`.

The checker verifies with exact rational arithmetic that **every coefficient of `Bhat_m` is strictly positive for `2<=m<=10`**. This is strong finite evidence, but no all-`m` coefficient theorem is claimed here.

---

## 8. Why this terminates the present task but not the parent theorem

The taskbook explicitly permits termination by an exact proof that a declared positivity mechanism fails while the parent theorem remains open.

The new all-`m` facts are:

1. the *complete* multilayer cofactor is exactly equivalent to `det S_m(t)`;
2. every inner signed conditional-covariance block `C_j(t)` is nonsingular with fixed inertia;
3. for `m>=3`, every such block is indefinite;
4. therefore a proof by termwise positive conditional variances / positive inner Andreief blocks cannot work;
5. the only unresolved interference is the outer alternating sum
   \[
   S_m(t)=\sum_jw_jC_j(t);
   \]
6. finite exact evidence through `m=10` says the double-endpoint Mobius/Bernstein residual still has all coefficients positive.

It would be circular to claim the numerically observed fixed inertia of `S_m(t)` as an all-`m` theorem: proving that its inertia cannot change on `0<t<=1` already requires excluding `det S_m(t)=0`, which is exactly the parent target.

So this Result freezes the smallest exact remaining object without overclaim.

---

## 9. Recommended successor theorem interface

The clean next target is no longer the full `2m x 2m` signed Laplacian. It is:

> **OUTER BINOMIAL CONDITIONAL-COVARIANCE DETERMINANT LEMMA.**  
> For `m>=2`, `0<t<=1`, prove
> \[
> \det S_m(t)\ne0,
> \]
> preferably with inertia
> \[
> \operatorname{In}(S_m(t))
> =
> \left(
> \lfloor (m-1)/2\rfloor,
> \lceil (m-1)/2\rceil,
> 0
> \right),
> \]
> or prove all coefficients of the double-endpoint residual `Bhat_m(x)` are positive.

Either statement immediately closes the original `tau_m` target by Section 4.

The existing GSTP route does not supply this: the actual `m=10` quotient already has a non-real conjugate pair, so universal real-positive exterior-cone spectral closure is unavailable while the cofactor remains positive in the finite regression.

---

## 10. Verification boundary

The paired checker uses only exact `fractions.Fraction` arithmetic and verifies:

- the predecessor adjacent-layer candidate root formula in finite regression;
- the exact full-cofactor / outer-covariance equality;
- `D_j>0` in the checked range;
- the exact inner covariance determinant formula;
- the explicit `m=3` indefinite witness;
- nonzero first-order outer determinant in finite regression;
- forced `t^(m-1)` order in the checked range;
- exact Mobius/Bernstein residual coefficient positivity through `m<=8` by default and `m<=10` with `--extended`;
- the double Cauchy endpoint factor bookkeeping.

Finite ranges are regression/discovery only. The all-`m` claims in Sections 3–6 are algebraic proofs in this return.

## 11. Scope and authority

No Working Truth, Foundation, L4, novelty, or parent-objective closure is claimed.

`method_harvest = RESULT_ONLY`.

The exact parent residue remains open:

\[
\det S_m(t)\ne0
\quad\Longleftrightarrow\quad
\tau_m(t)\ne0.
\]

This return's durable value is the exact dimensional collapse and the all-`m` obstruction to the simplest positivity mechanism.
