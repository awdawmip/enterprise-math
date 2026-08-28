# Perfect Prime Table Route-A Critical Cofactor All-m Proof — Research Return

Task: `RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF`
Publication: `TP2-4EE2618ABEBB6D097023`
Researcher-ID: `EM-PPTA-6D8F31`
Claim: `chatgpt-ppta-20260828-2132-6d8f31`
Execution record: `ER-B05E70EFD72590BCB0BF`

## Terminal verdict

`UNRESOLVED_EXACT_FRONTIER`

No all-\(m\) proof and no exact counterexample was obtained. This execution proves two new all-\(m\) structural theorems for the actual AP kernel, converts the remaining fixed-point problem to an explicit Beta–Bernstein/Mobius quotient determinant of order \(m-1\), and exactly kills the most immediate Perron/ordinary-norm shortcut.

## Exact equivalence chain back to the original cofactor system

Let \(n=m-1\) and
\[
A_{ij}=\prod_{\ell=0}^{m-1}(1+i+mj+\ell m^2),\qquad 0\le i,j<m.
\]
The original critical bidegree-\((m-2,m-2)\) cofactor problem asks whether
\[
D_{ij}=c(i,j)A_{ij}=s_i-t_j
\]
has a nonzero polynomial cofactor \(c\). Equivalently all adjacent mixed differences of \(D\) vanish.

The frozen taskbook transfer in the bivariate falling-factorial basis gives
\[
\text{nonzero critical cofactor}
\iff
\det P_m(L)[T,S]=0,
\]
where
\[
P_m(z)=\prod_{\ell=0}^{m-1}(z+1+\ell m^2),
\qquad
L=X\otimes I+mI\otimes X.
\]
All triangular/falling-factorial basis factors in this frozen transfer are explicit and nonzero; this execution does not change them.

Define
\[
h(q)=\frac1{\prod_{\ell=0}^{m-1}(1+q+\ell m^2)},\qquad
H_{ij}=h(i+mj),
\]
\[
w_i=(-1)^i\binom ni,\qquad W=\operatorname{diag}(w_i),
\]
\[
e_i=\sum_j w_jH_{ij}>0,\qquad d_j=\sum_i w_iH_{ij}>0,
\quad E=\operatorname{diag}(e_i),\quad D=\operatorname{diag}(d_j).
\]
The frozen factorial-Cauchy boundary reduction is, up to the explicit nonzero scalar \((-1)^n/n!\),
\[
Q_{\rm bdry}=
\begin{pmatrix}
E&HW\\
H^TW&D
\end{pmatrix}.
\]
After the fixed checkerboard gauge this is the signed \(K_{m,m}\) Laplacian with edge matrix
\[
C=WHW.
\]
Its spanning-tree cofactor \(\tau_c\) satisfies
\[
\det P_m(L)[T,S]\ne0\iff \tau_c\ne0.
\]

Schur-complementing the left vertex class gives
\[
A=E^{-1}HW,\qquad B=D^{-1}H^TW,\qquad
K=BA=D^{-1}H^TWE^{-1}HW.
\]
Because \(A\mathbf1=B\mathbf1=\mathbf1\),
\[
K\mathbf1=\mathbf1,
\]
and the frozen matrix-tree/Jacobi complement argument gives
\[
\tau_c\ne0
\iff
\ker(I-K)=\operatorname{span}\{\mathbf1\}.
\]
Therefore proving simplicity of the fixed point \(1\) for this exact \(K\) proves the original AP critical nonvanishing theorem, and a repeated fixed point is equivalent to an exact critical cofactor kernel.

## New theorem 1: \((WHW)^{-1}\) is strictly totally positive

The prior AP Beta/Andreief checkpoint proves that \(H\) is strictly totally positive (STP). For any equally sized index sets \(I,J\), Jacobi complementarity gives
\[
\det H^{-1}[I,J]
=
(-1)^{\sum I+\sum J}
\frac{\det H[J^c,I^c]}{\det H}.
\]
The quotient is strictly positive because \(H\) is STP.

Write
\[
W^{-1}=J\Lambda^{-1},\qquad
J=\operatorname{diag}((-1)^i),\qquad
\Lambda=\operatorname{diag}\binom ni>0.
\]
Then
\[
(WHW)^{-1}=W^{-1}H^{-1}W^{-1}.
\]
For the minor indexed by \(I,J\), the two checkerboard factors contribute exactly
\[
(-1)^{\sum I+\sum J},
\]
which cancels the Jacobi sign; all remaining diagonal factors are positive. Hence every minor is strictly positive:
\[
\boxed{(WHW)^{-1}\ \text{is STP for every }m\ge2.}
\]

## New theorem 2: Beta–Bernstein STP factorization of both half maps

Define the lower-triangular binomial Mobius matrix
\[
R_{jk}=(-1)^k\binom jk\quad(k\le j),\qquad R_{jk}=0\quad(k>j).
\]
Binomial inversion gives
\[
R^2=I.
\]
Set
\[
\widehat A=AR,\qquad \widehat B=BR.
\]
Then
\[
A=\widehat A R,\qquad B=\widehat B R.
\]

For the actual AP shifts, the exact Beta representation is
\[
H_{ij}=\kappa_m\int_0^1u^{i+mj}(1-u^{m^2})^n\,du,
\qquad
\kappa_m=\frac{m^{2-2m}}{(m-1)!}>0.
\]
Using
\[
w_jR_{jk}
=(-1)^{j+k}\binom nj\binom jk
=(-1)^{j+k}\binom nk\binom{n-k}{j-k}
\]
and the binomial theorem gives the exact entries
\[
\widehat A_{ik}
=
\frac{\kappa_m\binom nk}{e_i}
\int_0^1
u^{i+mk}(1-u^m)^{n-k}(1-u^{m^2})^n\,du,
\]
\[
\widehat B_{jk}
=
\frac{\kappa_m\binom nk}{d_j}
\int_0^1
u^{mj+k}(1-u)^{n-k}(1-u^{m^2})^n\,du.
\]
Thus every entry is strictly positive.

For a minor of \(\widehat A\), Andreief reduces its sign on
\(0<u_1<\cdots<u_q<1\) to the product of two determinants:
\[
\det(u_r^{i_a})
\]
and
\[
\det\!\left[
\binom n{k_b}(u_r^m)^{k_b}(1-u_r^m)^{n-k_b}
\right].
\]
The first is a generalized Vandermonde and is positive. In the second, factor the positive row terms \((1-u_r^m)^n\) and positive column binomial coefficients, then put
\[
t_r=\frac{u_r^m}{1-u_r^m}.
\]
The determinant becomes the generalized Vandermonde \(\det(t_r^{k_b})>0\). Positive row scaling by \(E^{-1}\) does not change minor signs. Hence \(\widehat A\) is STP. The same proof for \(\widehat B\), using \(u_r\) in the Bernstein factor and \(u_r^{m j_a}\) in the monomial factor, gives
\[
\boxed{\widehat A,\widehat B\ \text{are STP for every }m\ge2.}
\]

This is more specific than generic STP: both positive factors arise from the same one-dimensional AP Beta measure \((1-u^{m^2})^{m-1}du\), with Bernstein coordinates linked by \(u\mapsto u^m\).

## Smallest remaining lemma and why it is sufficient

Since
\[
K=BA=\widehat B R\widehat A R,
\]
conjugate by the involution \(R\):
\[
\mathcal T_m:=RKR=R\widehat B R\widehat A.
\]
Because \(R\mathbf1=e_0\) and \(K\mathbf1=\mathbf1\),
\[
\mathcal T_me_0=e_0.
\]
Therefore, in the splitting
\(\mathbb R^m=\langle e_0\rangle\oplus\mathbb R^{m-1}\),
\[
\mathcal T_m=
\begin{pmatrix}
1&*\\
0&Q_m
\end{pmatrix}.
\]

The smallest explicit unproved lemma left by this execution is:

> **Beta–Bernstein Mobius quotient lemma.** For every \(m\ge2\),
> \[
> \boxed{\det(I_{m-1}-Q_m)\ne0.}
> \]

It is necessary and sufficient because
\[
\det(I_{m-1}-Q_m)\ne0
\iff
\ker(I-\mathcal T_m)=\langle e_0\rangle
\iff
\ker(I-K)=\langle\mathbf1\rangle
\iff
\tau_c\ne0
\iff
\det P_m(L)[T,S]\ne0,
\]
and the frozen transfer then returns to the original mixed-difference system \(D_{ij}=c_{ij}A_{ij}=s_i-t_j\).

## Exact falsification certificate for the naive PF/norm shortcut

A direct Perron-Frobenius proof on \(Q_m\) would require an entrywise-positive quotient, or a simple norm-contraction proof would require a strict operator-norm bound. Both fail exactly already at \(m=4\).

Exact rational arithmetic gives
\[
(Q_4)_{2,0}
=
-\frac{7283935984630293449042423318233298991941765305912087}
{4804527841226553046809847732873233935782957698977851165}
<0.
\]
Also
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
Therefore neither entrywise PF on \(Q_m\) nor ordinary \(\ell_\infty\) contraction can close the all-\(m\) theorem.

The exact regression script is:
`./scripts/check_perfect_prime_table_critical_cofactor_all_m_proof.py --max-m 5`.

Its bounded-\(m\) checks are evidence/regression only. The all-\(m\) STP theorems above are proved analytically by Jacobi complementarity and Andreief/generalized-Vandermonde arguments.

## Previously closed shortcuts respected

This execution does not promote finite-\(m\) verification to proof; does not assume one-sign Cauchy-Binet or spanning-tree summands; does not interpret signed barycentric weights as convex averaging; does not invoke ordinary Schur positivity of the full determinant; does not claim generic STP alone closes the problem; does not assume all principal minors are positive; does not assume right-half-plane spectrum; does not use a separable multivariate multiplier-sequence shortcut; does not use support-parity/same-sign tree arguments; and does not reuse the previously falsified full sign-regularity conjecture for the congruent core \(M\).

## Frontier and next exact action

The hard target remains open. The next execution should attack the Beta–Bernstein Mobius quotient lemma using the common-measure linkage between \(\widehat A\) and \(\widehat B\). A generic theorem for arbitrary STP pairs is not enough. The most promising exact interface is an exterior-power/principal-angle or oscillation argument that uses the shared Beta measure and the order map \(u\mapsto u^m\), while avoiding entrywise positivity and ordinary norm contraction.
