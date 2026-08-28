# Perfect Prime Table Route-A Critical Cofactor All-m Proof — Research Return

Task: `RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF`  
Publication: `TP2-4EE2618ABEBB6D097023`  
Researcher-ID: `EM-PPTA-6D8F31`  
Claim: `chatgpt-ppta-20260828-2132-6d8f31`  
Execution record: `ER-B05E70EFD72590BCB0BF`

## Terminal verdict

`UNRESOLVED_EXACT_FRONTIER`

No all-\(m\) proof and no exact counterexample was obtained in this execution.  The execution does, however, prove two new all-\(m\) structural theorems for the actual AP kernel and reduces the remaining question to a single explicit \((m-1)\times(m-1)\) Beta–Bernstein/Möbius fixed-point determinant.  It also exactly kills the most immediate Perron/ordinary-norm shortcut for that determinant.

## Mother statement and frozen equivalence chain

For \(m\ge2\), put \(n=m-1\) and

\[
A_{ij}=\prod_{\ell=0}^{m-1}(1+i+mj+\ell m^2),\qquad 0\le i,j<m.
\]

The mother question asks whether every bidegree-\((m-2,m-2)\) cofactor \(c(i,j)\) satisfying

\[
D_{ij}=c(i,j)A_{ij}=s_i-t_j
\]

is zero.  Equivalently the adjacent mixed differences of \(D\) vanish.  The frozen taskbook reduction gives, with

\[
P_m(z)=\prod_{\ell=0}^{m-1}(z+a_\ell),\qquad a_\ell=1+\ell m^2,
\]

and the falling-factorial transfer operator \(L=X\otimes I+mI\otimes X\),

\[
\text{critical cofactor kernel is trivial}
\iff \det P_m(L)[T,S]\ne0.
\]

The same frozen reduction then gives the factorial-Cauchy boundary kernel

\[
H_{ij}=h(i+mj),\qquad
h(q)=\frac1{\prod_{\ell=0}^{m-1}(1+q+\ell m^2)},
\]

with

\[
w_i=(-1)^i\binom ni,\quad W=\operatorname{diag}(w_i),
\]

\[
e_i=\sum_j w_jH_{ij}>0,\qquad d_j=\sum_i w_iH_{ij}>0,
\]

and

\[
E=\operatorname{diag}(e_i),\qquad D=\operatorname{diag}(d_j).
\]

Up to the already-frozen nonzero scalar \((-1)^n/n!\), the duplicated boundary matrix is

\[
Q_{\rm bdry}=\begin{pmatrix}E&HW\\ H^TW&D\end{pmatrix}.
\]

After the fixed checkerboard gauge it is the signed \(K_{m,m}\) Laplacian with edge matrix

\[
C=WHW,
\]

row sums \(r=C\mathbf1=W e\), column sums \(s=C^T\mathbf1=W d\), and tree cofactor \(\tau_c\).  The frozen Jacobi-complement/matrix-tree reduction is

\[
\det P_m(L)[T,S]\ne0
\iff \tau_c\ne0.
\]

Schur-complementing the left vertex class gives the normalized two-step operator

\[
A=E^{-1}HW,\qquad B=D^{-1}H^TW,
\]

\[
K=BA=D^{-1}H^TWE^{-1}HW,\qquad K\mathbf1=\mathbf1,
\]

and

\[
\tau_c\ne0
\iff \ker(I-K)=\operatorname{span}\{\mathbf1\}.
\]

All transformations introduced below are invertible, and all diagonal normalizers used below are strictly positive; therefore they preserve this nonvanishing question exactly.  This execution does not use the sign of the earlier falling-factorial triangular change-of-basis scalar, only its frozen nonzeroness.

## New all-m theorem 1: the inverse signed kernel is itself STP

### Statement

For the actual AP kernel and every \(m\ge2\),

\[
\boxed{\;P:=(WHW)^{-1}\text{ is strictly totally positive.}\;}
\]

This strengthens the previous checkpoint, which recorded entrywise positivity of \((WHW)^{-1}\).

### Proof

The previous exact Beta/Andreief argument proves that \(H\) is STP.  Let \(I,J\subset\{0,\ldots,n\}\) with \(|I|=|J|=k\).  Jacobi complementarity gives

\[
\det H^{-1}[I,J]
=
(-1)^{\sum I+\sum J}
\frac{\det H[J^c,I^c]}{\det H}.
\]

Because \(H\) is STP, the quotient on the right is strictly positive.  Write

\[
W^{-1}=J\Lambda^{-1},\qquad
J=\operatorname{diag}((-1)^i),\quad
\Lambda=\operatorname{diag}\binom ni>0.
\]

Since

\[
P=W^{-1}H^{-1}W^{-1},
\]

the row and column checkerboard factors contributed by the two copies of \(W^{-1}\) are again
\((-1)^{\sum I+\sum J}\), exactly cancelling the Jacobi sign.  The remaining row/column factors are positive.  Hence every minor \(\det P[I,J]\) is strictly positive.  \(\square\)

## New all-m theorem 2: exact Beta–Bernstein STP factorization of both half maps

### Binomial Möbius involution

Define the lower-triangular matrix \(R\) by

\[
R_{jk}=(-1)^k\binom jk\quad(0\le k\le j\le n),
\qquad R_{jk}=0\quad(k>j).
\]

Binomial inversion gives

\[
R^2=I.
\]

Set

\[
\widehat A:=AR,\qquad \widehat B:=BR.
\]

Then

\[
A=\widehat A R,\qquad B=\widehat B R.
\]

### Exact integral entries

Let

\[
\kappa_m=\frac{m^{2-2m}}{(m-1)!}>0,
\qquad
\rho_m(u)=(1-u^{m^2})^n.
\]

The frozen AP Beta identity is

\[
H_{ij}=\kappa_m\int_0^1 u^{i+mj}\rho_m(u)\,du.
\]

Using

\[
w_jR_{jk}
=(-1)^{j+k}\binom nj\binom jk
=(-1)^{j+k}\binom nk\binom{n-k}{j-k},
\]

and summing the binomial expansion exactly gives

\[
\boxed{
\widehat A_{ik}
=
\frac{\kappa_m\binom nk}{e_i}
\int_0^1
u^{i+mk}(1-u^m)^{n-k}\rho_m(u)\,du
}
\]

where the displayed `nu` is the same integration variable \(u\), i.e.

\[
\widehat A_{ik}
=
\frac{\kappa_m\binom nk}{e_i}
\int_0^1
u^{i+mk}(1-\nu^m)^{n-k}(1-\nu^{m^2})^n\,d\nu.
\]

Likewise

\[
\boxed{
\widehat B_{jk}
=
\frac{\kappa_m\binom nk}{d_j}
\int_0^1
u^{mj+k}(1-\nu)^{n-k}(1-\nu^{m^2})^n\,d\nu.
}
\]

In particular every entry of \(\widehat A\) and \(\widehat B\) is strictly positive.

### Strict total positivity

Take increasing row indices \(i_1<\cdots<i_q\), increasing column indices \(k_1<\cdots<k_q\), and ordered integration variables \(0<u_1<\cdots<u_q<1\).  Andreief's identity expresses a minor of the unnormalized \(\widehat A\) as an integral of the product of

\[
\det(u_r^{i_a})_{a,r}
\]

and

\[
\det\!\left[
\binom n{k_b}(u_r^m)^{k_b}(1-u_r^m)^{n-k_b}
\right]_{r,b}.
\]

The first determinant is a generalized Vandermonde and is positive on the ordered chamber.  For the second, put

\[
t_r=\frac{u_r^m}{1-u_r^m},
\]

which is strictly increasing.  Factoring the positive row terms \((1-u_r^m)^n\) and positive column binomial coefficients leaves

\[
\det(t_r^{k_b})_{r,b}>0,
\]

again a generalized Vandermonde.  Therefore every minor is positive.  Positive row scaling by \(E^{-1}\) preserves all minor signs, so \(\widehat A\) is STP.

The proof for \(\widehat B\) is identical, using \(u_r\) instead of \(u_r^m\) in the Bernstein factor and monomials \(u_r^{m j_a}\) in the other determinant.  Thus

\[
\boxed{\widehat A\text{ and }\widehat B\text{ are STP for every }m\ge2.}
\]

This theorem uses the common AP Beta measure and is stronger/more structured than generic STP of \(H\).

## Exact smallest remaining lemma after the new factorization

Because

\[
K=BA=\widehat B R\widehat A R,
\]
conjugating by the involution \(R\) gives

\[
\mathcal T_m:=RKR=R\widehat B R\widehat A.
\]

Since \(R\mathbf1=e_0\) and \(K\mathbf1=\mathbf1\),

\[
\mathcal T_m e_0=e_0.
\]

Hence, in the splitting \(\mathbb R^m=\langle e_0\rangle\oplus\mathbb R^{m-1}\),

\[
\mathcal T_m=
\begin{pmatrix}
1&*\\
0&Q_m
\end{pmatrix}.
\]

Therefore the following explicit lemma is sufficient and necessary for the actual AP mother question:

> **Beta–Bernstein Möbius quotient lemma.** For every \(m\ge2\), with \(\widehat A,\widehat B,R\) exactly as above,
> \[
> \boxed{\det(I_{m-1}-Q_m)\ne0.}
> \]

Indeed

\[
\det(I_{m-1}-Q_m)\ne0
\iff \ker(I-\mathcal T_m)=\langle e_0\rangle
\iff \ker(I-K)=\langle\mathbf1\rangle
\iff \tau_c\ne0
\iff \det P_m(L)[T,S]\ne0,
\]

and the frozen transfer equivalence then returns to the original mixed-difference system.

This quotient lemma is the smallest explicit unproved lemma left by this execution.  Unlike the previous abstract STP fixed-point statement, both positive factors in it are now given by explicit Bernstein moment kernels over the *same* one-dimensional AP Beta measure.

## Exact kill certificate: ordinary PF / standard norm contraction does not close the quotient

A tempting next step is to hope that \(Q_m\) is entrywise positive (so Perron-Frobenius applies directly), or at least that \(\|Q_m\|_\infty<1\).  Both are already false exactly at \(m=4\).

With the definitions above, exact rational arithmetic gives

\[
(Q_4)_{2,0}
=
-\frac{7283935984630293449042423318233298991941765305912087}
{4804527841226553046809847732873233935782957698977851165}
<0.
\]

Moreover the absolute row sum of row \(0\) is

\[
\sum_j |(Q_4)_{0j}|
=
\frac{86153363870599096214802924793062676898819}
{79519723295283910628602867362432728239040}
>1,
\]

with exact excess

\[
\frac{6633640575315185586200057430629948659779}
{79519723295283910628602867362432728239040}>0.
\]

Thus neither entrywise PF on \(Q_m\) nor the ordinary \(\ell_\infty\) contraction is a valid all-\(m\) shortcut.  This is separate from, and consistent with, the previously frozen failure of full sign-regularity for the congruent core \(M\) at \(m=6\).

## Exact computational artifact

`./scripts/check_perfect_prime_table_critical_cofactor_all_m_proof.py --max-m 5`

performs exact rational regression checks for:

- \(R^2=I\);
- STP of \(H\), \((WHW)^{-1}\), \(\widehat A\), and \(\widehat B\) for the bounded regression range;
- finite nonvanishing of \(\det(I-Q_m)\) in that range (evidence only);
- the exact \(m=4\) negative quotient entry and \(\ell_\infty\)-norm kill certificate above.

The bounded checks are not used as proof of either all-\(m\) STP theorem; those follow from Jacobi complementarity and Andreief/generalized-Vandermonde arguments above.

## Previously closed shortcuts respected

This execution does **not** use any of the taskbook's closed shortcuts:

- no finite-\(m\) verification is promoted to an all-\(m\) theorem;
- no claim that raw Cauchy-Binet/tree summands have one sign;
- no signed-barycentric-as-convex-average argument;
- no ordinary Schur positivity assumption for the final determinant;
- no claim that generic STP alone proves the mother theorem;
- no all-principal-minors-positive shortcut;
- no right-half-plane spectral assumption;
- no multivariate multiplier-sequence shortcut;
- no support-parity/same-sign tree argument;
- no reuse of the falsified full sign-regularity conjecture for the congruent core \(M\).

## Frontier and next exact action

The hard target remains unresolved.  The next proof should attack the Beta–Bernstein Möbius quotient lemma, exploiting *both* facts simultaneously:

1. \(\widehat A\) and \(\widehat B\) are STP Bernstein moment matrices;
2. they arise from the same measure \((1-u^{m^2})^{m-1}du\), with the two Bernstein coordinates linked by the strict order map \(u\mapsto u^m\).

A generic theorem about arbitrary pairs of STP matrices is insufficient: even normalized STP pairs can have a repeated eigenvalue \(1\).  Any successful oscillation/principal-angle theorem must therefore use this common-measure linkage (or an equally specific AP identity).

Recommended next action: derive an exterior-power or principal-angle representation of the quotient operator \(Q_m\) from the two common-measure Bernstein systems, strong enough to exclude eigenvalue \(1\), without requiring entrywise positivity or an ordinary operator-norm contraction.
