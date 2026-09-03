# Perfect Prime AP residual Möbius–Bernstein coefficient positivity — Research Return

Researcher-ID: `EM-PPTAPRMBP1-409E2B`  
Task: `RS-PERFECT-PRIME-AP-RESIDUAL-MOBIUS-BERNSTEIN-COEFFICIENT-POSITIVITY`  
Publication: `TP2-8C910B14D7B854905F6E`  
Claim: `chatgpt-perfect-prime-rmbp-20260903-04cd89db`

## Terminal verdict

`EXACT_COEFFICIENT_INTERFACE_REDUCED_TO_A_NAMED_UNRESOLVED_ARITHMETIC_SUBPROBLEM / SIGNED_SECANT_BASIS_HAUSDORFF_LIFT_OPEN / PARENT_NONVANISHING_OPEN`

This return does **not** prove or refute all-\(m\) coefficient positivity of \(\widehat B_m\), and it does not prove or refute the parent determinant nonvanishing theorem.

It does prove a new exact all-\(m\) coefficient representation with two structural consequences that were not part of the frozen input:

1. every nonzero Cauchy–Binet basis term covers all \(m\) outer \(j\)-groups and its full atom minor factors as a fixed outer Vandermonde times an \(n\times n\) **within-group secant-difference determinant**;
2. the endpoint factors \(x^n(1+x)^n\) occur **term by term** in every nonzero basis contribution, rather than being produced by cancellation between signed contributions.

After dividing these forced endpoint factors, \(\widehat B_m\) is an exact signed squared-secant Bernstein expansion.  Its ordinary coefficient positivity is then exactly equivalent to positivity of the initial finite-difference row of a normalized coefficient sequence.  Exact arithmetic reveals the strictly stronger finite pattern that this normalized sequence is fully Hausdorff completely monotone for every \(2\le m\le10\).  The all-\(m\) proof of that signed-secant Hausdorff property is the named residual arithmetic problem frozen here.

## 1. Frozen notation

Put

\[
n=m-1,\qquad b=m^2,\qquad D=2m-1=2n+1,
\qquad d=n(2m-3)=n(D-2).
\]

Use the accepted quantities

\[
y_j=mj,\qquad
z_{j,s}=y_j+bs,
\]

\[
c_{j,s}
=
c_s(y_j)
=
\frac{n!}{\prod_{r=1}^{m}(y_j+bs+r)}>0,
\]

and

\[
w_j=(-1)^j\binom nj.
\]

The frozen transformed Cauchy matrix is

\[
\widetilde H_x=(1+x)^n H_{x/(1+x)}
\]

and the frozen cofactor factorization is

\[
\det \widetilde L_x[\widehat{2m},\widehat{2m}]
=
x^n(1+x)^n\widehat B_m(x),
\]

with

\[
\widehat B_m(x)
=
(1+x)^d q_m\!\left(\frac{x}{1+x}\right),
\qquad
q_m(t)=\sum_{a=0}^{d}q_{m,a}t^a.
\]

No finite positivity observation is used as a symbolic premise below.

## 2. Exact transformed atomic Gram representation

In the polynomial-coordinate model used by the accepted predecessor, gauge-fix the constant coefficient of the right polynomial \(f\) to zero and use coordinates

\[
(g_0,g_1,\ldots,g_n,f_1,\ldots,f_n).
\]

For each atom \((j,s)\in\{0,\ldots,n\}^2\), define the row vector

\[
R_{j,s}
=
(1,z_{j,s},z_{j,s}^2,\ldots,z_{j,s}^n,
-y_j,-y_j^2,\ldots,-y_j^n)
\in \mathbf Q^D.
\]

Under \(t=x/(1+x)\), the transformed atomic weight is exactly

\[
\rho_{j,s}(x)
=
(-1)^{j+s}
\binom nj\binom ns
c_{j,s}\,
x^s(1+x)^{n-s}.
\]

Therefore the gauge-fixed coefficient Gram matrix is

\[
G_m(x)
=
\sum_{j=0}^{n}\sum_{s=0}^{n}
\rho_{j,s}(x)\,
R_{j,s}^{\!T}R_{j,s}.
\]

Let

\[
V_x=\prod_{r=1}^{n}r!,
\qquad
V_y=
m^{n(n+1)/2}\prod_{r=1}^{n}r!.
\]

The left and right polynomial evaluation changes of coordinates have absolute determinants \(V_x\) and \(V_y\).  Adjugate congruence at the one-dimensional gauge kernel therefore gives

\[
\det G_m(x)
=
V_x^2V_y^2\,
x^n(1+x)^n\widehat B_m(x).
\tag{2.1}
\]

This identity was independently checked against the direct canonical cofactor for small \(m\), but (2.1) follows symbolically from the same polynomial-coordinate congruence used in the accepted reduction.

## 3. Nonzero bases must use every \(j\)-group

Apply Cauchy–Binet to

\[
G_m(x)=R^T\operatorname{diag}(\rho)R.
\]

For a \(D\)-element atom set \(I\), write

\[
S_j(I)=\{s:(j,s)\in I\},\qquad k_j=|S_j(I)|.
\]

### Lemma 3.1 — all-group support

If \(\det R_I\neq0\), then every \(S_j(I)\) is nonempty.

### Proof

Suppose exactly \(r<m\) distinct \(j\)-groups are active.  In each active group choose one reference row and subtract it from the other rows in that group.  Every difference row has zero \(f\)-part and zero constant \(g\)-coordinate, hence lies in the \(n\)-dimensional nonconstant-\(g\) subspace.  There are \(r\) reference rows.  Therefore

\[
\operatorname{rank}R_I\le n+r<n+m=D.
\]

So \(\det R_I=0\).  Hence a nonzero basis has all \(m=n+1\) groups active. \(\square\)

For every nonzero basis,

\[
\sum_{j=0}^{n}(k_j-1)=D-m=n.
\tag{3.1}
\]

This identity is the combinatorial source of the first endpoint order.

## 4. Exact row-minor factorization into an outer Vandermonde and secants

For a nonzero basis \(I\), choose canonically

\[
r_j=\min S_j(I)
\]

in each group.  Define the \(n\times n\) secant-difference matrix \(\Delta_I\) whose rows are indexed by
\((j,s)\) with \(s\in S_j(I)\setminus\{r_j\}\), and whose columns are \(\ell=1,\ldots,n\):

\[
\Delta_I[(j,s),\ell]
=
z_{j,s}^{\ell}-z_{j,r_j}^{\ell}.
\tag{4.1}
\]

There are exactly \(n\) such rows by (3.1).

Subtract the reference row \(R_{j,r_j}\) from all other rows in group \(j\), put the \(n\) difference rows first, and reorder the columns as

\[
(g_1,\ldots,g_n\mid g_0,f_1,\ldots,f_n).
\]

The resulting matrix is block triangular:

\[
\begin{pmatrix}
\Delta_I & 0\\
* & \mathcal V_y
\end{pmatrix},
\]

where the \(j\)-th row of \(\mathcal V_y\) is

\[
(1,-y_j,-y_j^2,\ldots,-y_j^n).
\]

Thus, up to an irrelevant orientation sign,

\[
\det R_I
=
\det\Delta_I\,\det\mathcal V_y,
\]

and therefore exactly

\[
(\det R_I)^2
=
V_y^2(\det\Delta_I)^2.
\tag{4.2}
\]

The full \(D\times D\) atom minor has consequently collapsed to one \(n\times n\) squared secant determinant.

## 5. Endpoint factors are termwise, not cancellation artifacts

For a nonzero basis define

\[
A_I=\sum_{(j,s)\in I}s.
\]

Because the \(k_j\) selected layer indices in group \(j\) are distinct elements of \(\{0,\ldots,n\}\),

\[
\sum_{s\in S_j(I)}s
\ge
0+1+\cdots+(k_j-1)
=
\binom{k_j}{2}.
\]

Put \(r_j=k_j-1\).  Since \(\sum r_j=n\) and

\[
\binom{k_j}{2}
=
\frac{r_j(r_j+1)}2
\ge r_j,
\]

we obtain

\[
A_I\ge n.
\tag{5.1}
\]

Similarly, the maximum sum of \(k_j\) distinct elements of \(\{0,\ldots,n\}\) is

\[
k_jn-\binom{k_j}{2},
\]

so

\[
A_I
\le
nD-\sum_j\binom{k_j}{2}
\le
nD-n
=
n(D-1).
\tag{5.2}
\]

Hence every individual nonzero Cauchy–Binet term contains

\[
x^{A_I}(1+x)^{nD-A_I}
\]

with at least \(x^n\) and at least \((1+x)^n\).

This proves a new all-\(m\) structural statement:

> The accepted double-endpoint factor \(x^n(1+x)^n\) is present in every nonzero atomic basis term separately.  Neither endpoint order requires cancellation between bases.

After division set

\[
a_I=A_I-n.
\]

Then (5.1)–(5.2) give

\[
0\le a_I\le d,
\]

and the residual term is

\[
x^{a_I}(1+x)^{d-a_I}.
\]

## 6. Exact signed squared-secant Bernstein formula

Define the positive rational weight

\[
\Gamma_I
=
(\det\Delta_I)^2
\prod_{(j,s)\in I}
\binom nj\binom ns c_{j,s}
>0
\]

for every nonzero basis, and define its sign

\[
\varepsilon_I
=
(-1)^{\sum_{(j,s)\in I}(j+s)}.
\]

Combining Cauchy–Binet, (2.1), (4.2), and the termwise endpoint division gives the exact all-\(m\) formula

\[
\boxed{
\widehat B_m(x)
=
\frac1{V_x^2}
\sum_{\substack{|I|=D\\ \det\Delta_I\ne0}}
\varepsilon_I\Gamma_I\,
x^{a_I}(1+x)^{d-a_I}.
}
\tag{6.1}
\]

Since

\[
\widehat B_m(x)
=
\sum_{a=0}^{d}q_{m,a}\,
x^a(1+x)^{d-a},
\]

the triangular Bernstein basis is unique, so (6.1) yields the exact coefficient representation

\[
\boxed{
q_{m,a}
=
\frac1{V_x^2}
\sum_{\substack{|I|=D,\ \det\Delta_I\ne0\\ A_I=n+a}}
\varepsilon_I\Gamma_I.
}
\tag{6.2}
\]

Consequently the ordinary coefficient of \(\widehat B_m\) is

\[
\boxed{
[x^k]\widehat B_m(x)
=
\sum_{a=0}^{k}
q_{m,a}\binom{d-a}{k-a}.
}
\tag{6.3}
\]

Equations (6.1)–(6.3) are the requested exact coefficient interface.  They replace the original \(D\times D\) cofactor coefficient problem by signed sums of squared \(n\times n\) secant minors with explicit positive Cauchy/Beta weights.

The sign problem is still genuine: for fixed \(A_I\), individual bases occur with both signs already at small \(m\).  Thus no false “every basis is positive” claim is being made.

## 7. Exact finite-difference normalization

Define algebraically, without assuming any sign pattern,

\[
h_{m,a}
=
\frac{(-1)^a q_{m,a}}{\binom da},
\qquad 0\le a\le d.
\tag{7.1}
\]

Using

\[
\binom da\binom{d-a}{k-a}
=
\binom dk\binom ka,
\]

equation (6.3) becomes

\[
\frac{[x^k]\widehat B_m(x)}{\binom dk}
=
\sum_{a=0}^{k}(-1)^a\binom ka h_{m,a}.
\]

With the forward-difference operator
\(\Delta h_a=h_{a+1}-h_a\),

\[
\boxed{
\frac{[x^k]\widehat B_m(x)}{\binom dk}
=
(-1)^k\Delta^k h_{m,0}.
}
\tag{7.2}
\]

Therefore the original target is **exactly equivalent** to the initial finite-difference condition

\[
(-1)^k\Delta^k h_{m,0}>0,
\qquad
0\le k\le d.
\tag{HCM0}
\]

This is not a numerical approximation and not an appeal to root locations.

## 8. Stronger Hausdorff lift discovered by exact arithmetic

The exact checker reconstructs \(q_m\) from the canonical cofactor with `fractions.Fraction` arithmetic.  For every \(2\le m\le10\), it verifies the strictly stronger pattern

\[
(-1)^k\Delta^k h_{m,r}>0
\qquad
\text{for every }r,k\ge0,\ r+k\le d.
\tag{HCM}
\]

In particular, all \(q_{m,a}\) have the strict alternating sign

\[
(-1)^a q_{m,a}>0
\]

through \(m=10\).  Neither statement is promoted beyond the checked finite range.

The numbers of exact finite-difference cells checked are:

- \(m=2\): \(3\);
- \(m=3\): \(28\);
- \(m=4\): \(136\);
- \(m=5\): \(435\);
- \(m=6\): \(1081\);
- \(m=7\): \(2278\);
- \(m=8\): \(4278\);
- \(m=9\): \(7381\);
- \(m=10\): \(11935\).

The paired certificate records SHA-256 digests of every exact finite-difference table.  The signed-secant coefficient formula is independently recomputed and matched to the direct cofactor polynomial for \(m=2,3,4\); the full-row-minor/secant factorization is exhaustively checked for all candidate minors at \(m=2,3\).

These are finite regression/discovery facts only.

## 9. Why the Hausdorff lift is mathematically useful

The standard finite Hausdorff moment criterion says that full finite complete monotonicity (HCM) is equivalent to the existence of a positive measure \(\mu_m\) on \([0,1]\) whose first \(d+1\) moments are

\[
h_{m,a}=\int_0^1 u^a\,d\mu_m(u).
\]

If the all-\(m\) version of (HCM) is proved for the explicit signed-secant sums (6.2), then

\[
q_m(t)
=
\sum_{a=0}^{d}
(-1)^a\binom da h_{m,a}t^a
=
\int_0^1(1-tu)^d\,d\mu_m(u),
\tag{9.1}
\]

and hence

\[
\widehat B_m(x)
=
(1+x)^d q_m\!\left(\frac{x}{1+x}\right)
=
\int_0^1[1+x(1-u)]^d\,d\mu_m(u).
\tag{9.2}
\]

The coefficient formula is then manifest:

\[
[x^k]\widehat B_m(x)
=
\binom dk
\int_0^1(1-u)^k\,d\mu_m(u)>0.
\]

Thus the stronger Hausdorff property gives a concrete positive-measure certificate for every target coefficient simultaneously.  Unlike a fixed-inertia or generic total-positivity assumption, the measure moments here are pinned to the explicit signed squared-secant sums (6.2).

## 10. Named unresolved arithmetic subproblem

Freeze the following exact interface.

### `AP_SIGNED_SECANT_BASIS_HAUSDORFF_LIFT`

For every \(m\ge2\), let \(q_{m,a}\) be the explicit signed squared-secant sum (6.2), let \(d=n(2m-3)\), and define \(h_{m,a}\) by (7.1).

Prove either:

1. the exact target row
   \[
   (-1)^k\Delta^k h_{m,0}>0
   \quad(0\le k\le d),
   \]
   which is equivalent to all coefficients of \(\widehat B_m\) being strictly positive; or, more strongly,
2. the full Hausdorff lift
   \[
   (-1)^k\Delta^k h_{m,r}>0
   \quad(r+k\le d),
   \]
   preferably by constructing or identifying the positive measure in (9.1).

A legitimate obstruction is the first exact \((m,r,k)\) where the relevant signed finite difference is nonpositive.  A failure with \(r>0\) kills only the stronger Hausdorff lift; it does **not** by itself kill the original \(r=0\) coefficient target.  A failure at \(r=0\) is exactly a nonpositive coefficient of \(\widehat B_m\).

This subproblem is not the original determinant restated: its input is the explicit \(n\times n\) secant-minor ensemble (6.2), its endpoint orders have already been removed termwise, and it separates the exact target row from the stronger moment-structure conjecture suggested by all available exact data.

## 11. Endpoint and parent boundary

Because all-\(m\) coefficient positivity has **not** been proved, this return does not invoke positivity of \(\widehat B_m(x)\) for all \(x>0\) and does not claim closure at \(t=1\).

The accepted statements remain unchanged:

\[
\tau_m(t)\ne0
\Longleftrightarrow
\det S_m(t)\ne0
\qquad(0<t\le1),
\]

and

\[
\det \widetilde L_x[\widehat{2m},\widehat{2m}]
=
x^n(1+x)^n\widehat B_m(x).
\]

The parent all-\(m\) nonvanishing objective remains open.

## 12. Verification, reuse, and proof boundary

Paired checker:

`research_checks/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_CHECK_20260903.py`

Compact certificate:

`research_artifacts/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY/signed_secant_hausdorff_certificate_20260903.json`

Validated exact runs in the current execution:

- default checker (`m=2..8`);
- single-case extension `--m 10`;
- independent exact computations for the \(m=9\) and \(m=10\) finite-difference table digests recorded in the certificate.

No floating-point arithmetic is used for any stated finite identity or sign.  Attempts to push direct interpolation to \(m=11\) exceeded the current execution-time budget and produced no accepted mathematical result; no inference is drawn from that computational limit.

No new general-purpose tool family was introduced.  The task reuses the predecessor's exact `Fraction` determinant/interpolation machinery and adds only task-local Cauchy–Binet/secant enumeration and finite-difference verification.

`method_harvest = RESULT_ONLY`.

No Working Truth, Foundation, L4, novelty, historical-priority, canonical-promotion, or parent-objective closure is claimed.

Recommended Driver disposition:

`ACCEPT EXACT_COEFFICIENT_INTERFACE_REDUCTION at the stated strength; preserve all-m coefficient positivity and parent nonvanishing as OPEN; if continued, target AP_SIGNED_SECANT_BASIS_HAUSDORFF_LIFT rather than restarting the full cofactor algebra or recycling the rejected block/inertia routes.`
