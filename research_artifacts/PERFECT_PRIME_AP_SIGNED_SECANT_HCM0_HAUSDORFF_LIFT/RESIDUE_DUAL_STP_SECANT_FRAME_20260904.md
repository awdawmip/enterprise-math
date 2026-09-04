# Perfect Prime AP HCM0 — residue-dual strict-TP secant frame

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL ALL-m STRUCTURAL THEOREM — HCM0 REMAINS OPEN**

## 1. Frozen synchronized quotient form

Put `n=m-1` and

\[
\mu_r=\frac{n!}{\prod_{a=1}^{m}(mr+a)}.
\]

For integers `r0<r`, write

\[
M=r-r_0>0,
\qquad
g_{M,a}(j)=\binom{j+M}{a}-\binom ja,
\qquad 1\le a\le n.
\]

The exact quotient matrix from the previous checkpoint is

\[
Q_{r_0,r}[a,b]
=\sum_{j=0}^{n}(-1)^j\binom nj\mu_{r+j}
 g_{M,a}(j)g_{M,b}(j).
\tag{1.1}
\]

No separation hypothesis `M>=m` is used in the present theorem.

## 2. Residue-duality identity for every polynomial of degree <=2n-2

For `q=0,...,n`, put

\[
\theta_q=\frac{q+1}{m},
\qquad
\eta_{r,q}
=\frac{n!}{\prod_{k=0}^{n}(r+\theta_q+k)}
=B(r+\theta_q,n+1)>0.
\tag{2.1}
\]

### Theorem 2.1 — exact residue duality

For every polynomial `P` with

\[
\deg P\le2n-2,
\]

one has

\[
\boxed{
\sum_{j=0}^{n}(-1)^j\binom nj\mu_{r+j}P(j)
=\frac1m\sum_{q=0}^{n}(-1)^q\binom nq
\eta_{r,q}P(-r-\theta_q).
}
\tag{2.2}
\]

### Proof

As a rational function of a complex variable `z`,

\[
\mu_{r+z}
=\frac{n!}{m^m}
\frac1{\prod_{q=0}^{n}(z+r+\theta_q)}.
\tag{2.3}
\]

Let

\[
D_r(z)=\prod_{q=0}^{n}(z+r+\theta_q).
\]

Divide `P(z)/D_r(z)` into its polynomial part plus its proper rational part.  Since

\[
\deg P-\deg D_r\le n-3<n,
\]

the alternating binomial functional

\[
\mathcal D_n[f]=\sum_{j=0}^{n}(-1)^j\binom njf(j)
\]

annihilates the polynomial part.

At the pole

\[
z_q=-r-\theta_q
\]
we have

\[
D_r'(z_q)
=\prod_{\ell\ne q}(\theta_\ell-\theta_q)
=m^{-n}(-1)^q q!(n-q)!.
\]

Hence the residue of `mu_{r+z}P(z)` at `z_q` is exactly

\[
\frac{(-1)^q}{m}\binom nqP(z_q).
\tag{2.4}
\]

Finally the classical finite-difference Cauchy identity gives, for `alpha>0`,

\[
\sum_{j=0}^{n}\frac{(-1)^j\binom nj}{j+\alpha}
=\frac{n!}{\alpha(\alpha+1)\cdots(\alpha+n)}.
\tag{2.5}
\]

Apply (2.5) to each partial-fraction term with

\[
\alpha=r+\theta_q.
\]
Equations (2.4) and (2.5) give (2.2).  ∎

The identity is self-dual in the following sense: the original integer-node finite difference has been transferred to the `m` fractional Cauchy poles `theta_q`, while the original `m`-step beta denominator has become an ordinary unit-step beta denominator.

## 3. Synchronized secants become positive polynomial secants

At a dual pole `z_q=-r-theta_q` and with `r=r0+M`,

\[
z_q+M=-r_0-\theta_q.
\]

Therefore

\[
g_{M,a}(z_q)
=\binom{-r_0-\theta_q}{a}
 -\binom{-r_0-M-\theta_q}{a}.
\]

Using

\[
\binom{-x}{a}=(-1)^a\binom{x+a-1}{a},
\]
we obtain

\[
\boxed{
g_{M,a}(z_q)=(-1)^{a+1}h_{M,a}^{(r_0)}(\theta_q),}
\tag{3.1}
\]

where

\[
h_{M,a}^{(r_0)}(\theta)
=\binom{r_0+M+\theta+a-1}{a}
 -\binom{r_0+\theta+a-1}{a}>0
\quad(\theta>0).
\tag{3.2}
\]

Let

\[
S=\operatorname{diag}((-1)^{a+1})_{a=1}^{n}
\]

and let `Ghat_M^(r0)` be the `(n+1) x n` matrix

\[
\widehat G_M^{(r_0)}[q,a]
=h_{M,a}^{(r_0)}(\theta_q).
\]

Then Theorem 2.1 applied entrywise to (1.1) gives the exact dual Gram representation

\[
\boxed{
S Q_{r_0,r} S
=\widehat G_M^{(r_0)T}
\widehat D_r
\widehat G_M^{(r_0)},
}
\tag{3.3}
\]

with alternating diagonal

\[
\widehat D_r[q,q]
=\frac1m(-1)^q\binom nq\eta_{r,q}.
\tag{3.4}
\]

Thus the synchronized translation/moment shift converts every row of the quotient frame into a **strictly positive polynomial secant** on the short fractional pole block `(0,1]`.

## 4. All-m theorem: the dual secant collocation frame is strictly totally positive

### Theorem 4.1

For every

\[
m\ge2,\quad r_0\ge0,\quad M\in\mathbb Z_{>0},
\]
all minors of

\[
\widehat G_M^{(r_0)}
\]
are strictly positive.  In particular it is an `(n+1) x n` strictly totally positive matrix.

### Proof

Set

\[
X_q=r_0+\theta_q>0.
\]

Introduce the rising-factorial basis

\[
\phi_k(X)=\binom{X+k-1}{k}=\frac{(X)_k}{k!},
\qquad k\ge0.
\]

Its generating function is

\[
\sum_{k\ge0}\phi_k(X)z^k=(1-z)^{-X}.
\tag{4.1}
\]

Likewise

\[
(1-z)^{-M}-1
=\sum_{h\ge1}\phi_h(M)z^h.
\tag{4.2}
\]

Multiplying (4.1) and (4.2) and comparing the coefficient of `z^a` gives

\[
\boxed{
h_{M,a}^{(r_0)}(\theta_q)
=\sum_{k=0}^{a-1}\phi_k(X_q)\phi_{a-k}(M).
}
\tag{4.3}
\]

Hence

\[
\widehat G_M^{(r_0)}=\Phi_X C_M,
\tag{4.4}
\]

where

\[
\Phi_X[q,k]=\phi_k(X_q),
\qquad 0\le q\le n,\ 0\le k\le n-1,
\]

and

\[
C_M[k,a]=
\begin{cases}
\phi_{a-k}(M),&k<a,\\
0,&k\ge a,
\end{cases}
\qquad 1\le a\le n.
\tag{4.5}
\]

#### 4.1 `Phi_X` is strictly totally positive

For increasing positive `X_i` and increasing nonnegative integers `k_j`, positive row/column scalings reduce the relevant minor to

\[
\det[\Gamma(X_i+k_j)].
\]

Using

\[
\Gamma(X_i+k_j)=\int_0^\infty t^{X_i+k_j-1}e^{-t}\,dt
\]

and Andréief's identity gives an integral of

\[
\det[t_\ell^{X_i-1}]\det[t_\ell^{k_j}]
\]

over the ordered simplex `0<t_1<...<t_s`.  Both generalized Vandermonde determinants are strictly positive there.  Therefore every minor of `Phi_X` is strictly positive.

#### 4.2 `C_M` is totally nonnegative and has an explicit positive matching minor

The coefficient sequence

\[
\phi_h(M)=\binom{M+h-1}{h}
\]

has generating function `(1-z)^(-M)`.  For integer `M>=1`, its upper Toeplitz matrix is the `M`-fold product of the totally nonnegative geometric Toeplitz matrix generated by `(1-z)^(-1)`.  Hence it is totally nonnegative, and `C_M` is a row/column submatrix of it.

Now fix any selected output columns

\[
1\le a_1<\cdots<a_s\le n.
\]

In the Cauchy-Binet expansion for the corresponding minor of `Phi_X C_M`, choose the intermediate columns

\[
k_i=a_i-1.
\]

Then the selected `C_M` minor is upper triangular with diagonal

\[
\phi_1(M)=M,
\]
so its determinant is exactly

\[
M^s>0.
\]

The matching `Phi_X` minor is strictly positive, while every other Cauchy-Binet term is nonnegative.  Therefore the product minor is strictly positive.  This proves Theorem 4.1. ∎

## 5. Dual Hausdorff representation

The new positive magnitudes also have a beta/moment interpretation:

\[
\eta_{r,q}
=\int_0^1x^{r+\theta_q-1}(1-x)^n\,dx.
\tag{5.1}
\]

With `x=y^m`,

\[
\boxed{
\eta_{r,q}
=m\int_0^1 y^{mr+q}(1-y^m)^n\,dy.
}
\tag{5.2}
\]

Thus residue duality exchanges the two binomial factors that already appeared in the accepted Perfect-Prime geometry:

- original moments use `u^(mr)(1-u)^n`;
- dual pole magnitudes use `y^(mr+q)(1-y^m)^n`.

The fixed alternating signature is preserved, but all secant-frame minors become strictly positive.

## 6. What this theorem does and does not prove

Proved all-`m` here:

1. the residue-duality identity (2.2) for every polynomial degree `<=2n-2`;
2. the exact synchronized dual Gram representation (3.3);
3. strict total positivity of the entire dual secant frame (Theorem 4.1);
4. the dual beta/Hausdorff representation (5.2).

Not proved:

- the mixed-discriminant sign of two different dual frames;
- the separation theorem `M5_BLOCK_SEPARATED_MELLIN_EULER_PENCIL`;
- positive stability/Hurwitzness of the separated pencil;
- full three-support all-`m` sign regularity;
- HCM0 or the parent determinant theorem.

This theorem is nevertheless stronger than the previous original-coordinate Pascal TN statement: after residue duality, **every** secant-frame minor is strict, including minors that vanished at boundary integer rows in the original Pascal representation.

## 7. Next interface

Write

\[
\widehat D_r=J\Lambda_r,
\qquad
J=\operatorname{diag}((-1)^q),
\qquad
\Lambda_r>0.
\]

Then

\[
S Q_{r_0,r}S=Z_M^T J Z_M,
\qquad
Z_M=\Lambda_r^{1/2}\widehat G_M^{(r_0)},
\tag{7.1}
\]

with `Z_M` strictly totally positive up to positive row scaling.  Therefore the surviving three-layer problem has become a pair of **strictly-TP codimension-one frames in one fixed alternating Krein metric**.

The next deterministic targets are:

1. exploit codimension one (`n` columns in `n+1` rows) to reduce the relative `J`-Gram geometry to explicit left-null/barycentric data;
2. test whether the separated transition admits a positive Lyapunov certificate, which would imply right-half-plane generalized spectrum and hence coefficient positivity;
3. independently keep the Mellin-Euler integration-by-parts route, because Hurwitz stability is stronger than coefficient positivity and is not equivalent to it below the separation threshold.
