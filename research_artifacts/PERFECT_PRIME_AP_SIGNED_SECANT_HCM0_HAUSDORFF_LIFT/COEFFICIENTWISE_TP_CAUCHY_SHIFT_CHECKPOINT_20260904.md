# Perfect Prime AP signed-secant HCM0 Hausdorff lift — research checkpoint

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL CHECKPOINT — HCM0 REMAINS OPEN**

## 1. Frozen boundary

Put

\[
n=m-1,\qquad D=2m-1,\qquad d=n(2m-3).
\]

The accepted predecessor freezes

\[
\widehat B_m(x)=(1+x)^d q_m\!\left(\frac{x}{1+x}\right),
\qquad
q_m(t)=\sum_{a=0}^{d}q_{m,a}t^a,
\]

and

\[
h_{m,a}=\frac{(-1)^a q_{m,a}}{\binom da}.
\]

Its exact coefficient identity is

\[
\frac{[x^k]\widehat B_m(x)}{\binom dk}=(-1)^k\Delta^k h_{m,0}.
\]

Hence the task target remains exactly

\[
\tag{HCM0}
(-1)^k\Delta^k h_{m,0}>0\qquad(0\le k\le d).
\]

Nothing below promotes finite computation to an all-\(m\) HCM0 proof.

---

## 2. Exact finite frontier: full shifted HCM through \(m=12\)

The predecessor verified the stronger shifted inequalities

\[
(-1)^k\Delta^k h_{m,r}>0\qquad(r+k\le d)
\]

exactly through \(m\le10\). Using the same accepted `fractions.Fraction` cofactor/interpolation reconstruction:

- \(m=11\): \(d=190\), all \(18,336\) shifted cells are strictly positive; canonical table SHA-256 `abd4f6a5e6bc97161b151edb28e3017a8d96a03cf1273091860d1c427f8f9d93`.
- \(m=12\): \(d=231\), all \(27,028\) shifted cells are strictly positive; canonical table SHA-256 `e44d1cb01420a206200158046b366e5d6ac953551ebcb580f8f84b6d0c64af40`.

Therefore the current exact discovery frontier is

\[
\boxed{\text{full shifted HCM holds exactly for }2\le m\le12.}
\]

This is finite evidence only.

---

## 3. All-\(m\) coefficientwise strict total positivity of the transformed moment kernel

Let \(b=m^2\) and

\[
\widetilde H_{ij}(x)=\int_0^1u^{i+mj}[1+x(1-u^b)]^n\,du,
\qquad 0\le i,j\le n.
\]

Equivalently,

\[
\widetilde H_{ij}(x)
=\sum_{r=0}^{n}\binom nr x^r\int_0^1u^{i+mj}(1-u^b)^r\,du,
\]

with

\[
\int_0^1u^A(1-u^b)^r\,du
=\frac{r!\,b^r}{\prod_{s=0}^{r}(A+1+bs)}>0.
\]

### Theorem 3.1

For every \(m\ge2\), every minor

\[
\det\widetilde H[I,J](x),\qquad |I|=|J|=q,
\]

is a polynomial in \(x\) whose coefficients in all degrees \(0,\ldots,nq\) are strictly positive.

### Proof

For

\[
I=\{i_1<\cdots<i_q\},\qquad J=\{j_1<\cdots<j_q\},
\]

Andréief gives

\[
\det \widetilde H[I,J](x)
=\frac1{q!}\int_{(0,1)^q}
\det[u_\ell^{i_a}]_{a,\ell}
\det[u_\ell^{m j_b}]_{b,\ell}
\prod_{\ell=1}^{q}[1+x(1-u_\ell^b)]^n\,du.
\]

The product of the two determinants is symmetric. On the ordered simplex

\[
0<u_1<\cdots<u_q<1
\]

both generalized Vandermonde determinants are strictly positive. For every \(0\le k\le nq\), the coefficient of \(x^k\) in

\[
\prod_{\ell=1}^{q}[1+x(1-u_\ell^b)]^n
\]

is a nonzero sum of strictly positive interior terms. Its integral against the positive generalized-Vandermonde product is therefore strictly positive. ∎

Thus total positivity holds **coefficientwise**, not merely pointwise for \(x\ge0\).

### Corollary 3.2

For \(w_j=(-1)^j\binom nj\),

\[
\sum_{j=0}^{n}w_j\widetilde H_{ij}(x)
=\int_0^1u^i(1-u^m)^n[1+x(1-u^b)]^n\,du,
\]

and

\[
\sum_{i=0}^{n}w_i\widetilde H_{ij}(x)
=\int_0^1u^{mj}(1-u)^n[1+x(1-u^b)]^n\,du.
\]

Every coefficient of every row/column contraction is strictly positive.

---

## 4. Exact mechanism obstruction: TP plus positive contractions is insufficient

Take

\[
\nu=\delta_{1/10}+\delta_{4/5}
\]

and \(\mu_k=\int u^k\,d\nu(u)\). Then

\[
(\mu_0,\mu_1,\mu_2,\mu_3)
=\left(2,\frac9{10},\frac{13}{20},\frac{513}{1000}\right).
\]

For \(m=2\),

\[
H=\begin{pmatrix}\mu_0&\mu_2\\\mu_1&\mu_3\end{pmatrix}
=\begin{pmatrix}2&13/20\\9/10&513/1000\end{pmatrix}
\]

has

\[
\det H=\frac{441}{1000}>0.
\]

With \(w=(1,-1)\),

\[
Hw=\begin{pmatrix}27/20\\387/1000\end{pmatrix}>0,
\qquad
H^Tw=\begin{pmatrix}11/10\\137/1000\end{pmatrix}>0.
\]

Nevertheless the signed \(K_{2,2}\) tree cofactor is

\[
\tau
=\mu_0\mu_1\mu_2+\mu_1\mu_2\mu_3-\mu_0\mu_1\mu_3-\mu_0\mu_2\mu_3
=-\frac{24039}{200000}<0.
\]

Therefore

\[
\boxed{\text{strict TP moment structure + positive binomial contractions}\not\Longrightarrow\text{ signed tree-cofactor positivity}.}
\]

The special finite-difference/Cauchy-shift structure must still be used.

---

## 5. Pure Cauchy shifts: exact Lagrange-transfer factorization

For \(c\ge0\), define

\[
C(c)_{ij}=\frac1{i+1+mj+c}.
\]

Let \(w_i=(-1)^i\binom ni\) and

\[
E_i(c)=\sum_{j=0}^{n}w_jC(c)_{ij},\qquad
F_j(c)=\sum_{i=0}^{n}w_iC(c)_{ij}.
\]

Then

\[
\boxed{E_i(c)=\frac{m^nn!}{\prod_{j=0}^{n}(i+1+c+mj)}>0}
\]

and

\[
\boxed{F_j(c)=\frac{n!}{\prod_{i=0}^{n}(i+1+c+mj)}>0.}
\]

Put

\[
A_c=\operatorname{diag}(w_iE_i(c)).
\]

Let \(Y_j=mj\), let \(\ell_j\) be the degree-\(n\) Lagrange basis on \(Y_0,\ldots,Y_n\), and put

\[
X_{c,i}=-c-i-1,
\qquad
P_c(i,j)=\ell_j(X_{c,i}).
\]

The barycentric formula gives

\[
\boxed{P_c(i,j)=\frac{w_jC(c)_{ij}}{E_i(c)}.}
\]

### Theorem 5.1 — signed quadrature identity

With

\[
D_c=\operatorname{diag}(w_jF_j(c)),
\]

one has

\[
\boxed{P_c^TA_cP_c=D_c.}
\]

### Proof

Let

\[
p(x)=\prod_{j=0}^{n}(x-Y_j),\qquad q_c(x)=\prod_{i=0}^{n}(x-X_{c,i}).
\]

For every polynomial \(R\) of degree at most \(2n\), the rational function

\[
\frac{R(x)}{p(x)q_c(x)}
\]

has zero residue at infinity. Summing residues at the \(X_{c,i}\) and \(Y_j\), then inserting the equally spaced nodes, gives

\[
\sum_i w_iE_i(c)R(X_{c,i})
=\sum_j w_jF_j(c)R(Y_j).
\]

Taking \(R=\ell_j\ell_k\) yields \(P_c^TA_cP_c=D_c\). ∎

### Corollary 5.2 — pure-shift rank

The signed bipartite Laplacian

\[
L(c)=\begin{pmatrix}
A_c&-WC(c)W\\
-WC(c)^TW&D_c
\end{pmatrix}
\]

satisfies

\[
\boxed{
L(c)=
\begin{bmatrix}I\\-P_c^T\end{bmatrix}
A_c
\begin{bmatrix}I&-P_c\end{bmatrix}.
}
\]

Hence

\[
\boxed{\operatorname{rank}L(c)=m.}
\]

After quotienting the global constant gauge, the kernel has dimension \(n=m-1\). Geometrically, a pure shift imposes only the interpolation relation \(x=P_cy\).

---

## 6. All-\(m\) theorem: every two-shift mixed cell has the correct sign

Fix distinct \(c,d\ge0\). Let \(\tau_{c,d}(z,w)\) be any reduced tree cofactor of

\[
zL(c)+wL(d).
\]

Each pure layer has rank \(m=n+1\) on the \(D=2m-1\) dimensional gauge quotient. Therefore only bidegrees \((m,n)\) and \((n,m)\) can occur:

\[
\tau_{c,d}(z,w)=\alpha_{c,d}z^mw^n+\beta_{c,d}z^nw^m.
\]

### Theorem 6.1 — two-shift sign regularity

For every \(m\ge2\) and distinct \(c,d\ge0\),

\[
\boxed{(-1)^n\alpha_{c,d}>0,\qquad (-1)^n\beta_{c,d}>0.}
\]

Moreover both coefficients vanish to exact order \(2n\) when \(c\to d\). Equivalently,

\[
\boxed{
(-1)^n\tau_{c,d}(z,w)
=(c-d)^{2n}z^nw^n(A_{c,d}z+B_{c,d}w),
}
\]

with \(A_{c,d},B_{c,d}>0\).

### Proof

Use coordinates adapted to \(\ker L(c)\):

\[
r=x-P_cy.
\]

Then

\[
L(c)\sim\begin{pmatrix}A_c&0\\0&0\end{pmatrix}.
\]

Up to a positive square of a coordinate determinant, the coefficient of \(z^mw^n\) is

\[
\det A_c\cdot
\det[(P_c-P_d)^TA_d(P_c-P_d)]_{\mathbb P_n/\mathbf1}.
\]

In polynomial coordinates, \((P_cy)_i=f(X_{c,i})\) and

\[
X_{c,i}=X_{d,i}+(d-c).
\]

Thus

\[
f(X_{c,i})-f(X_{d,i})=(\Delta_hf)(X_{d,i}),\qquad h=d-c.
\]

On the basis \(x,x^2,\ldots,x^n\), the map \(f\mapsto\Delta_hf\) is triangular with diagonal

\[
h,2h,\ldots,nh,
\]

so its determinant is \(n!h^n\). Hence the kernel-restriction determinant contains \((n!)^2(c-d)^{2n}\).

It remains to determine the sign of

\[
G_d=V_d^TA_dV_d,
\]

where \(V_d\) is the \(m\times n\) Vandermonde matrix on \(X_{d,i}\) with columns \(1,x,\ldots,x^{n-1}\). Cauchy-Binet gives

\[
\det G_d
=\sum_{i=0}^{n}(\det V_d[\widehat i])^2\prod_{r\ne i}A_{d,r}.
\]

Because the \(X_{d,i}\) are consecutive with step \(-1\),

\[
(\det V_d[\widehat i])^2=\frac{\Delta_X^2}{i!^2(n-i)!^2}.
\]

After factoring the full Vandermonde square and \(\prod_rA_{d,r}\), the residual scalar has the sign of

\[
\sum_{i=0}^{n}(-1)^i\binom niP(i),
\qquad
P(i)=\prod_{j=0}^{n}(d+i+1+mj).
\]

Since \(P\) is monic of degree \(n+1\),

\[
\Delta^nP(0)=n!\left[\binom{n+1}{2}+\sum_{j=0}^{n}(d+1+mj)\right]>0.
\]

Therefore

\[
\operatorname{sgn}\det G_d=(-1)^{n(n-1)/2}.
\]

Also

\[
\operatorname{sgn}\det A_c=(-1)^{n(n+1)/2}.
\]

Multiplying gives

\[
\operatorname{sgn}\alpha_{c,d}=(-1)^{n^2}=(-1)^n.
\]

Strictness follows from \(c\ne d\), and swapping \(c,d\) gives the same sign for \(\beta_{c,d}\). ∎

For the accepted Cauchy layers \(c_s=m^2s\), this proves the correct sign for **every multivariate layer coefficient supported on exactly two distinct shifts**, uniformly for all \(m\). The first unresolved cells are genuinely three-or-more-shift mixed discriminants.

---

## 7. Exact small-\(m\) multivariate evidence

Two multivariate lifts were computed exactly for \(m=2,3,4\).

### Positive density basis

For

\[
P(v)=\sum_{r=0}^{n}y_rv^r,\qquad v=1-u^{m^2},
\]

the resulting signed tree cofactor has:

- \(m=2\): 3 nonzero monomials;
- \(m=3\): 18 nonzero monomials;
- \(m=4\): 110 nonzero monomials.

Every nonzero coefficient is strictly positive. The support is exactly the degree-\(D\) monomials with at least \(n\) factors from positive density degree.

### Raw Cauchy-layer basis

For independent layer variables \(z_s\),

\[
H_{ij}=\sum_{s=0}^{n}(-1)^s\binom ns\frac{z_s}{i+1+mj+m^2s},
\]

the exact expansions have:

- \(m=2\): 2 nonzero monomials;
- \(m=3\): 12 nonzero monomials;
- \(m=4\): 80 nonzero monomials.

Every nonzero \(\prod z_s^{\alpha_s}\) satisfies \(\alpha_s\le m\), and

\[
\boxed{\operatorname{sgn}(\text{coefficient})=(-1)^{n+\sum_s s\alpha_s}.}
\]

Theorem 6.1 proves the entire two-support slice of this pattern for every \(m\).

If the all-support mixed-discriminant extension is proved, it immediately yields

\[
(-1)^a q_{m,a}>0
\]

for all \(m,a\). This remains weaker than HCM0 but would remove the raw signed-secant cancellation uniformly.

---

## 8. Current reduction of the open problem

Ruled out:

1. generic kernel TP as a sufficient mechanism;
2. positive row/column contractions as a sufficient mechanism;
3. pure-shift nonsingularity;
4. any two-shift sign obstruction.

The sharp next target is:

> Prove or disprove that every polarized mixed discriminant of the pure Cauchy-shift family \(L(c)\) has sign \((-1)^n\) for arbitrary nonnegative shifts, including confluent repetitions of multiplicity at most \(m\).

Equivalently, prove the all-support extension of Theorem 6.1.

A second viable route is to prove coefficientwise positivity of the multivariate tree cofactor directly in the positive density basis \(P(1-u^{m^2})\). Theorem 3.1 supplies coefficientwise strict TP of all kernel minors, while §4 proves that the special divided-difference/Cauchy-shift relation must enter any successful proof.

---

## 9. Verification boundary

Paired checker:

`research_checks/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT_CHECK_20260904.py`

It provides:

- exact recomputation hooks for the \(m=11\) and \(m=12\) shifted-HCM tables and frozen digests;
- the exact two-atom TP/contraction obstruction;
- exact rational regressions of the Lagrange-transfer identity and pure-shift zero cofactor for \(m=2,\ldots,6\);
- exact two-shift sign regressions for \(m=2,\ldots,6\);
- optional exact SymPy expansion of both multivariate small-\(m\) patterns for \(m=2,3,4\).

The all-\(m\) proofs in §§3, 5, and 6 are symbolic arguments here; finite checker output is regression evidence only.

No `Result-ID` is frozen because the hard target `SIGNED_SECANT_HCM0_ALL_M_PROVED_OR_EXACTLY_OBSTRUCTED` has not yet been reached.

Recommended scheduler state: `ACTIVE / CONTINUE`.
