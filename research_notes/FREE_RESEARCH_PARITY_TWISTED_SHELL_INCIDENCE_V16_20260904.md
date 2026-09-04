# Free Research — Parity-Twisted Shell Incidence and the Radial Krawtchouk Gap

Status: `FREE_RESEARCH_FRONTIER / SIGNLESS_EDGE_AS_PARITY_GRADIENT / PRODUCT_BOUNDED_SHELL_CARRIER / RADIAL UP_DOWN_SPECTRUM_CLOSED / CONSTANT_MINUS_ONE_MODE_ISOLATED / ARITHMETIC CELL_OVERLAP_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parents:

- `FREE_RESEARCH_ADAPTIVE_HISTORY_GAMMA_OVERLAP_V16_20260904.md`;
- `FREE_RESEARCH_UNIFORM_GAMMA_WASSERSTEIN_COUPLING_V16_20260904.md`;
- `FREE_RESEARCH_PI_PRIME_HAMMING_SHELL3_PROVENANCE_20260904.md`.

Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the Hamming/Krawtchouk shell carrier, product-bounded prime histories, signless return field, and finite symmetry calculus.

## 1. Executive advance

The troublesome arithmetic `-1` return mode becomes an ordinary constant mode after twisting history shell `k` by the parity factor `(-1)^k`.

For an action subset `I`, let

\[
F(I):=r\!\left(q_{\prod_{i\in I}a_i}(N)\right),
\qquad
G(I):=(-1)^{|I|}F(I).
\]

Along a Hamming edge `I -> I union {j}`,

\[
\boxed{
G(I\cup\{j\})-G(I)
=(-1)^{|I|+1}
\left(F(I\cup\{j\})+F(I)\right).}
\tag{1.1}
\]

Thus the signless prime-power return defect is exactly the ordinary gradient of the parity-twisted field.

This identifies the correct role of the original Hamming/Krawtchouk geometry:

\[
\boxed{
\text{signless arithmetic transport}
=\text{parity-twisted Hamming gradient}.}
\]

On the ideal logarithmic product-bounded shell incidence, the radial up/down operator can be diagonalized exactly.  Its nonconstant singular values are uniformly separated from one; the first is

\[
\boxed{
\sigma_1=\sqrt{\frac{R-1}{2R}}<\frac1{\sqrt2}.}
\tag{1.2}
\]

Hence every radial nonconstant relation channel has a constant spectral gap.  The sole kernel is the common constant twisted mode, which is precisely the persistent arithmetic `-1` mode.  The entire remaining difficulty is therefore reduced to killing that one constant through endpoint-cell overlap or another scalar anchor.

---

## 2. Product-bounded shell carrier

Fix a history degree `R>=2`.  Give an ordered action tuple

\[
\mathbf a=(a_1,\ldots,a_R)
\]

weight

\[
\prod_{i=1}^R\omega(a_i)
\mathbf1_{a_1\cdots a_R\le N}.
\]

Because the full product is at most `N`, every subset product is also valid.  The entire Boolean activation cube of the tuple therefore exists without moving-cutoff stopping.

The top shell has all `R` actions active.  An adjacent leaf omits one action.  The incidence relation is invariant under every permutation of the `R` history slots.

For the parity-twisted field `G`, every top/leaf edge energy is

\[
\boxed{
|G(\text{top})-G(\text{leaf})|^2
=|r(\text{top endpoint})+r(\text{leaf endpoint})|^2.}
\tag{2.1}
\]

Conditioned on a leaf history, the omitted action is distributed by its positive continuation weight.  Thus the edge energy is the continuation-weighted signless residual energy

\[
\Gamma(\text{leaf endpoint})+e(\text{leaf endpoint})^2.
\tag{2.2}
\]

The nontrivial arithmetic relation field is therefore a genuine Hamming-shell Dirichlet form after parity twist.

---

## 3. Ideal logarithmic simplex

Write action logarithms as

\[
x_i=\frac{\log a_i}{\log N},
\]

and let `s` be the remaining logarithmic slack.  The product-bounded condition becomes

\[
x_1+\cdots+x_R+s=1,
\qquad x_i,s\ge0.
\]

Under the first-mass law, the ideal carrier is uniform Dirichlet measure on this simplex.

For the top shell, the remaining slack `S=s` has density

\[
\boxed{
\nu_R(s)=R(1-s)^{R-1},
\qquad0<s<1,}
\tag{3.1}
\]

that is, `Beta(1,R)`.

If one action is omitted, the leaf slack is

\[
L=s+x_i.
\]

Its density is

\[
\boxed{
\lambda_R(l)=R(R-1)l(1-l)^{R-2},
\qquad0<l<1,}
\tag{3.2}
\]

that is, `Beta(2,R-1)`.

Conditionally on `L=l`, the top slack is uniform on `[0,l]`.  The joint edge density is

\[
\boxed{
j_R(l,s)=R(R-1)(1-l)^{R-2}
\mathbf1_{0\le s\le l\le1}.}
\tag{3.3}
\]

---

## 4. Radial up/down operators

Let `U_R` map a top radial function `g(s)` to its leaf conditional mean:

\[
\boxed{
(U_Rg)(l)=\frac1l\int_0^l g(s)\,ds.}
\tag{4.1}
\]

Its adjoint `D_R` maps a leaf radial function `f(l)` to the top conditional mean:

\[
\boxed{
(D_Rf)(s)
=\frac{R-1}{(1-s)^{R-1}}
\int_s^1 f(l)(1-l)^{R-2}\,dl.}
\tag{4.2}
\]

The operator

\[
T_R:=D_RU_R
\]

is positive and self-adjoint on

\[
L^2(\nu_R).
\]

It preserves every polynomial-degree filtration.

For a monomial `s^j`,

\[
U_R(s^j)=\frac{l^j}{j+1}.
\]

Given `S=s`, write

\[
L=s+(1-s)Z,
\qquad Z\sim\operatorname{Beta}(1,R-1).
\]

The leading coefficient of `D_R(l^j)` is

\[
\mathbb E[(1-Z)^j]
=\frac{R-1}{R+j-1}.
\]

Therefore the diagonal coefficient of `T_R` on degree `j` is

\[
\boxed{
\lambda_j(R)
=\frac{R-1}{(j+1)(R+j-1)}.}
\tag{4.3}
\]

Since `T_R` is self-adjoint and triangular in the polynomial filtration, the orthogonal polynomial of each degree `j` is an eigenfunction with eigenvalue `lambda_j(R)`.

In particular,

\[
\lambda_0=1,
\qquad
\lambda_1=\frac{R-1}{2R},
\]

and `lambda_j` strictly decreases with `j`.

The singular values of `U_R` are

\[
\boxed{
\sigma_j(R)=
\sqrt{\frac{R-1}{(j+1)(R+j-1)}}.}
\tag{4.4}
\]

---

## 5. Bipartite radial Poincare inequality

Give the top and leaf radial spaces equal outer mass `1/2`, and define the normalized bipartite adjacency

\[
\mathcal A_R=
\begin{pmatrix}
0&U_R\\
D_R&0
\end{pmatrix}.
\]

Its spectrum is

\[
\pm\sigma_j(R).
\]

The common constant function on the two shells has eigenvalue `+1`.  The opposite shell-constant function has eigenvalue `-1`.  On the orthogonal complement of the common constant,

\[
\sup\operatorname{Spec}(\mathcal A_R)
=\sigma_1(R)
<1/\sqrt2.
\]

Therefore every radial pair `(f_leaf,g_top)` satisfies

\[
\boxed{
\operatorname{Var}_{\frac12(\lambda_R\oplus\nu_R)}(f,g)
\le
\frac1{1-\sqrt{(R-1)/(2R)}}
\mathcal E_R(f,g),}
\tag{5.1}
\]

where

\[
\mathcal E_R(f,g)
:=\frac12
\int|f(l)-g(s)|^2j_R(l,s)\,dl\,ds.
\tag{5.2}
\]

Since

\[
\frac1{1-\sqrt{(R-1)/(2R)}}
\le\frac1{1-1/\sqrt2}
=2+\sqrt8,
\]

the radial Poincare constant is uniform in the history degree.

Under the parity twist, (5.2) is exactly one half of the signless top/leaf return energy.

---

## 6. The constant mode is exactly the arithmetic obstruction

If the parity-twisted field is common-constant on both shells,

\[
G_{\rm leaf}=G_{\rm top}=c,
\]

then the untwisted arithmetic field has opposite shell signs:

\[
r_{\rm top}=(-1)^Rc,
\qquad
r_{\rm leaf}=(-1)^{R-1}c.
\]

Every signless edge defect vanishes, so the Dirichlet form cannot see this mode.  It is precisely the persistent `-1` return mode isolated by the Selberg return operator.

All other radial variation is controlled with the uniform gap (5.1).  Thus no further spectral-gap search is needed on the nonconstant radial sector.

The remaining scalar problem is only:

\[
\boxed{
\text{prove that one deterministic endpoint field cannot support
opposite nonzero constants on the overlapping top and leaf endpoint laws}.}
\tag{6.1}
\]

In the ideal continuum, the two Beta densities are mutually absolutely continuous, so the common constant is immediately zero.  In the finite arithmetic system, the measures are atomic after quotient projection, and a quantitative common-cell or relation-energy bridge is required.

---

## 7. Ideal top/leaf overlap

The density ratio is

\[
\frac{\lambda_R(s)}{\nu_R(s)}
=\frac{(R-1)s}{1-s}.
\]

The unique crossing is at

\[
s=1/R.
\]

The unmatched mass is

\[
\begin{aligned}
d_R
&=\int_0^{1/R}
\bigl(\nu_R(s)-\lambda_R(s)\bigr)\,ds\\
&=\boxed{\left(1-\frac1R\right)^{R-1}.}
\end{aligned}
\tag{7.1}
\]

Hence the overlap is

\[
\boxed{
L_R=1-\left(1-\frac1R\right)^{R-1}
\longrightarrow1-e^{-1}.}
\tag{7.2}
\]

This is a continuation-weighted analogue of the adaptive Gamma overlap.  Here the limiting overlap remains the constant `1-e^-1`, while the nonconstant radial sector has the uniform incidence gap (5.1).

---

## 8. Exact finite target suggested by the spectrum

Let `mu_(N,R)^top` and `mu_(N,R)^leaf` be the actual endpoint pushforwards of the product-bounded shell edge measure.  A sufficient arithmetic theorem is one of the following equivalent-strength bridges.

### Exact-cell overlap form

Construct a common endpoint submeasure `eta_(N,R)` such that

\[
\eta_{N,R}\le\mu_{N,R}^{\rm top},
\qquad
\eta_{N,R}\le\mu_{N,R}^{\rm leaf},
\]

and

\[
|\eta_{N,R}|
\ge c_0>0
\]

uniformly in a useful range of `R`.

On the common endpoint state `m`, the two parity-twisted values are exact opposites.  If `bar G` is their common shell mean, then

\[
\operatorname{Var}(G)
\ge |\eta_{N,R}|\,|\bar G|^2,
\]

up to the already controlled difference of shell means.  Combining with (5.1) kills the constant mode.

### Block-relation form

Alternatively, show that the value variance lost by replacing exact endpoint cells with logarithmic blocks is dominated by the radial incidence Dirichlet form plus a lower-scale defect.  Then the uniform Poincare gap controls both the nonconstant sector and the block correction.

The second form is weaker arithmetically and is compatible with the full provenance relation field already present in V14--V16.

---

## 9. Current classification

Closed exactly in the ideal radial shell model:

1. parity twist converts signless defects to Hamming gradients;
2. top and leaf Beta laws;
3. the joint incidence density;
4. the full radial spectrum (4.3)--(4.4);
5. the uniform nonconstant Poincare gap;
6. the unique constant `-1` arithmetic mode;
7. ideal overlap (7.2).

Closed structurally in the finite carrier:

1. the product-bounded shell action is permutation invariant;
2. every subset quotient is valid;
3. edge energy is the signless return energy.

Open:

1. a finite arithmetic exact-cell overlap lower bound or block-relation substitute;
2. composition with the residual-energy telescope;
3. elimination of the common twisted constant;
4. a promoted quantitative prime remainder;
5. any RH-scale conclusion.

The main conclusion is:

\[
\boxed{
\text{the remaining obstruction is not a missing spectral gap;
it is the single common constant mode left after a uniform radial gap}.}
\]
