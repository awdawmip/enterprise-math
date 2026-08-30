# Perfect Prime Beta–Bernstein oscillation / `u -> u^m` order-map closure — Research Return

Task: `RS-PERFECT-PRIME-BETA-BERNSTEIN-OSCILLATION-ORDER-MAP`  
Publication: `TP2-2B3DC53DD4066F464AE9`  
Researcher-ID: `EM-PPTBBOSC-ACA29A`  
Claim: `chatgpt-pptbbosc-20260830-1111-aca29a`  
Execution record: `ER-3F740734DF2A1E27BCD9`

## Terminal verdict

`SUCCESS / ORDER_MAP_OSCILLATION_ROUTE_OBSTRUCTED_WITH_EXACT_MODEL`

This return **does not** give a counterexample to the frozen AP parent theorem
\[
\det(I_{m-1}-Q_m)\ne0.
\]
It proves a sharper negative statement about the current oscillation strategy:

> The package consisting of a common positive one-dimensional measure, the exact
> nonlinear order map \(u\mapsto u^m\), strict total positivity of the two
> normalized Bernstein half maps, all-order strict sign regularity of the raw
> Möbius-differenced kernels, strict first normalized difference, and even total
> nonnegativity of the Pascal-conjugated reciprocal-normalizer matrices is
> **insufficient** to exclude eigenvalue \(1\).

An exact all-\(m\) Cauchy endpoint satisfies all of those structural properties
while its composite is exactly the identity:
\[
K_m^{(0)}=I_m,\qquad
\mathcal T_m^{(0)}=I_m,\qquad
Q_m^{(0)}=I_{m-1}.
\]

Therefore any successful AP proof in this lane must use information that detects
the nonconstant AP Christoffel factor
\[
\rho_m(u)=(1-u^{m^2})^{m-1},
\]
or an equivalent AP-specific invariant.  Generic order-map oscillation plus the
normalizer-sign geometry isolated in the initial checkpoint cannot close the
mother equation by itself.

## 1. Durable frontier retained

Write \(n=m-1\), \(w_i=(-1)^i\binom ni\), and let \(R\) be the lower binomial
Möbius involution
\[
R_{ri}=(-1)^i\binom ri,\qquad R^2=I.
\]

The prior durable checkpoint on this execution branch established for the
actual AP model:

1. the raw common-measure matrices \(M^A=E\widehat A\) and
   \(M^B=D\widehat B\);
2. exact order-map identities
   \[
   (RM^A)_{rk}
   =\binom nk\int_0^1(1-u)^r u^{mk}(1-u^m)^{n-k}\,\mu_m(du),
   \]
   \[
   (RM^B)_{rk}
   =\binom nk\int_0^1(1-u^m)^r u^k(1-u)^{n-k}\,\mu_m(du);
   \]
3. every \(q\times q\) minor of either raw matrix has strict sign
   \[
   \varepsilon_q=(-1)^{q(q-1)/2};
   \]
4. the first normalized differences are strictly negative in every nonconstant
   Bernstein column;
5. naive all-order normalized complete monotonicity is false in the actual AP
   model already at \(m=5\).

The present continuation starts exactly there.  No earlier generic-STP,
entrywise-Perron, ordinary-norm, or falsified full-sign-regular shortcut is
reopened.

## 2. Exact Cauchy endpoint

Replace only the AP Christoffel weight by the constant positive measure
\[
\mu_0(du)=du,
\]
while preserving the same index sets, the same signed binomial vector \(w\),
the same \(R\), and crucially the same order map \(u\mapsto u^m\).

Set
\[
x_i=i+1,\qquad y_j=mj,\qquad 0\le i,j\le n,
\]
and
\[
H^{(0)}_{ij}
=\int_0^1u^{i+mj}\,du
=\frac1{x_i+y_j}.
\]

Define exactly as in the frozen parent:
\[
e_i^{(0)}=\sum_jH^{(0)}_{ij}w_j,\qquad
d_j^{(0)}=\sum_iH^{(0)}_{ij}w_i,
\]
\[
A_0=(E_0)^{-1}H_0W,\qquad
B_0=(D_0)^{-1}H_0^TW,
\]
\[
\widehat A_0=A_0R,\qquad
\widehat B_0=B_0R,\qquad
K_0=B_0A_0.
\]

This is an exact comparison model, not the AP model.

## 3. The order-map oscillation structure survives

The same binomial summation gives
\[
(RM_0^A)_{rk}
=\binom nk\int_0^1
(1-u)^r u^{mk}(1-u^m)^{n-k}\,du,
\]
\[
(RM_0^B)_{rk}
=\binom nk\int_0^1
(1-u^m)^r u^k(1-u)^{n-k}\,du.
\]

Hence the prior Andreief/generalized-Vandermonde proof applies verbatim:
for every \(q\),
\[
\operatorname{sgn}\det (RM_0^A)[I,J]
=
\operatorname{sgn}\det (RM_0^B)[I,J]
=
(-1)^{q(q-1)/2}
\]
for every increasing \(q\)-row and \(q\)-column choice.  In particular, row
reversal makes each raw kernel strictly totally positive.

The normalized matrices \(\widehat A_0,\widehat B_0\) are themselves strictly
totally positive.  For \(\widehat A_0\), before positive row normalization the
minor integrand is a product of

- a generalized Vandermonde in the increasing functions \(u^{i_a}\); and
- a generalized Vandermonde in the increasing odds coordinate
  \(u^m/(1-u^m)\).

The same argument for \(\widehat B_0\) uses \(u^{mj}\) and \(u/(1-u)\).
Positive row normalization preserves the strict minor signs.

Likewise the covariance argument from the checkpoint still yields, for every
\(m\ge2\) and \(k>0\),
\[
(R\widehat A_0)_{1k}<0,\qquad
(R\widehat B_0)_{1k}<0.
\]

Thus neither the common measure, nor \(u\mapsto u^m\), nor raw all-order SSR,
nor normalized STP, nor the first strict sign can distinguish this endpoint
from the AP model at the level needed for fixed-point exclusion.

## 4. Closed normalizers

The elementary identity
\[
\sum_{j=0}^n
\frac{(-1)^j\binom nj}{a+j}
=
\frac{n!}{a(a+1)\cdots(a+n)}
\]
gives
\[
e_i^{(0)}
=
\frac{n!\,m^n}
{\prod_{r=0}^{n}(i+1+mr)},
\]
and
\[
d_j^{(0)}
=
\frac{n!}
{\prod_{r=0}^{n}(mj+1+r)}.
\]

Therefore the reciprocal normalizers are polynomial sequences:
\[
s_i:=(e_i^{(0)})^{-1}
=
\frac1{n!m^n}
\prod_{r=0}^{n}(i+1+mr),
\]
\[
t_j:=(d_j^{(0)})^{-1}
=
\frac1{n!}
\prod_{r=0}^{n}(mj+1+r).
\]

The immediate normalizer subproblem identified in the initial checkpoint can
therefore be solved exactly at this endpoint.

## 5. Stronger obstruction: the reciprocal-normalizer Pascal conjugates are TN

Let
\[
J=\operatorname{diag}(1,-1,1,-1,\ldots),
\qquad
P=RJ.
\]
Then \(P\) is the ordinary lower Pascal matrix,
\(P_{ij}=\binom ij\), and
\[
P^{-1}=JR.
\]

Define the Pascal-conjugated number operator
\[
N=P^{-1}\operatorname{diag}(0,1,\ldots,n)P.
\]
Direct binomial inversion gives the exact lower-bidiagonal form
\[
N_{ii}=i,\qquad N_{i,i-1}=i,
\]
with all other entries zero.

For any polynomial \(f\),
\[
P^{-1}\operatorname{diag}(f(0),\ldots,f(n))P=f(N).
\]
Applying this to the two reciprocal normalizers gives
\[
\boxed{
JR(E_0)^{-1}RJ
=
\frac1{n!m^n}
\prod_{r=0}^{n}\bigl(N+(1+mr)I\bigr)
}
\]
and
\[
\boxed{
JR(D_0)^{-1}RJ
=
\frac{m^{n+1}}{n!}
\prod_{r=0}^{n}
\left(N+\frac{1+r}{m}I\right).
}
\]

Every factor on the right is a lower bidiagonal matrix with nonnegative
entries and positive diagonal.  Such a matrix is totally nonnegative, and
products of totally nonnegative matrices are totally nonnegative by
Cauchy–Binet.  Hence, for every \(m\ge2\),
\[
JR(E_0)^{-1}RJ\quad\text{and}\quad
JR(D_0)^{-1}RJ
\]
are totally nonnegative.

This is the decisive strengthening of the negative control.  Even the
most natural finite-difference/Pascal-conjugate sign property suggested by the
initial checkpoint survives at the Cauchy endpoint.

## 6. Exact all-\(m\) identity \(K_0=I\)

Let
\[
X(z)=\prod_{\ell=0}^{n}(z-x_\ell),\qquad
Y(z)=\prod_{r=0}^{n}(z+y_r).
\]
Because
\[
X'(x_i)=(-1)^{n-i}i!(n-i)!,
\]
the closed normalizer formula implies
\[
\frac{w_i}{e_i^{(0)}}
=
\frac{(-1)^n}{m^n}
\frac{Y(x_i)}{X'(x_i)}.
\]

Consider
\[
G_0:=H_0^TW(E_0)^{-1}H_0.
\]
For \(j\ne k\),
\[
(G_0)_{jk}
=
\frac{(-1)^n}{m^n}
\sum_{i=0}^{n}
\frac{1}{X'(x_i)}
\frac{Y(x_i)}
{(x_i+y_j)(x_i+y_k)}.
\]
The polynomial
\[
p_{jk}(z)=
\frac{Y(z)}
{(z+y_j)(z+y_k)}
\]
has degree \(n-1\).  The Lagrange leading-coefficient identity says
\[
\sum_{i=0}^{n}\frac{p(x_i)}{X'(x_i)}=0
\qquad(\deg p<n).
\]
Therefore every off-diagonal entry of \(G_0\) is zero.

But
\[
A_0\mathbf 1=\mathbf1,\qquad B_0\mathbf1=\mathbf1,
\]
directly from \(e=H_0w\) and \(d=H_0^Tw\).  Hence
\[
K_0=B_0A_0
\]
has row sum \(1\).  Since the preceding calculation makes \(K_0\) diagonal,
every diagonal entry must equal \(1\):
\[
\boxed{K_0=I_m.}
\]

Because \(R^2=I\),
\[
\mathcal T_0=RK_0R=I_m.
\]
Under the frozen splitting
\[
\mathbb R^m=\langle e_0\rangle\oplus\mathbb R^{m-1},
\]
the quotient block is therefore
\[
\boxed{Q_0=I_{m-1}}.
\]
Eigenvalue \(1\) is not merely present; it fills the entire quotient.

## 7. What exactly is refuted

The result refutes the implication
\[
\begin{aligned}
&\text{common positive measure}
+\ (u\mapsto u^m)
+\ \widehat A,\widehat B\ \text{STP}\\
&+\ \text{raw Möbius SSR}
+\ \text{strict first normalized sign}
+\ \text{TN Pascal-conjugated reciprocal normalizers}\\
&\Longrightarrow\quad
\det(I-Q)\ne0.
\end{aligned}
\]

The Cauchy endpoint satisfies the left-hand package for every \(m\ge2\), but
has \(Q=I\).

This is **not** an `EXACT_COUNTEREXAMPLE_TO_PARENT_FOUND`: the Cauchy endpoint
does not have the AP Christoffel factor and therefore is not the frozen AP
operator.

## 8. Smallest surviving AP-specific residue

The actual AP moment kernel is, up to one positive \(m\)-dependent scalar,
\[
H^{AP}_{ij}
\propto
\int_0^1
u^{i+mj}(1-u^{m^2})^n\,du.
\]
The exact obstruction above shows that a proof cannot treat the weight merely
as an arbitrary positive common measure.  The first structure not shared by the
identity endpoint is precisely
\[
\rho_m(u)=(1-u^{m^2})^n.
\]

Therefore the smallest credible continuation is not a stronger generic
variation-diminishing theorem.  It is an **AP-weight-sensitive deformation or
oscillation lemma** that quantitatively changes the identity endpoint when
\(\rho_m\) is turned on and controls the quotient eigenvalue \(1\).

A safe candidate deformation is
\[
\rho_{m,t}(u)=(1-t\,u^{m^2})^n,\qquad 0\le t\le1,
\]
with \(t=0\) equal to the exact identity endpoint and \(t=1\) equal to AP.
This return does not assert that such a deformation is monotone, sign-regular,
or non-singular; those are the unresolved theorems.

## 9. Exact checker

`research_checks/PERFECT_PRIME_BETA_BERNSTEIN_OSCILLATION_ORDER_MAP_CHECK_20260830.py`
retains the prior AP regressions and adds exact rational checks for the Cauchy
endpoint:

- closed \(e_i^{(0)},d_j^{(0)}\);
- \(K_0=I_m\);
- raw SSR in both half maps;
- strict first normalized difference;
- the Pascal number-operator identity;
- both reciprocal-normalizer factorizations;
- finite-range total nonnegativity regression for the two conjugates.

The configured bounded-\(m\) runs are regression only.  The all-\(m\) claims in
Sections 3–6 are proved algebraically above.

## 10. Dedup / independence note

A parallel principal-angle/exterior-power lane independently identified the
unweighted Cauchy endpoint as an identity control.  This return does **not**
claim the bare identity \(K_0=I\) as a new discovery relative to that sibling
lane.

The distinct contribution of this oscillation execution is to show that the
specific structures this lane had isolated as promising also survive at that
identity endpoint:

1. the exact \(u\mapsto u^m\) raw SSR theorem;
2. strict first normalized sign;
3. closed reciprocal normalizers; and especially
4. all-\(m\) total nonnegativity of
   \(JR(E_0)^{-1}RJ\) and \(JR(D_0)^{-1}RJ\)
   via explicit bidiagonal Pascal-conjugate factorization.

Thus the result closes a genuine oscillation-side information gap rather than
merely duplicating the sibling geometric control.

## Terminal disposition

`ORDER_MAP_OSCILLATION_ROUTE_OBSTRUCTED_WITH_EXACT_MODEL`

Unresolved parent residue:
\[
\det(I_{m-1}-Q_m)\ne0
\quad\text{for the actual AP Christoffel weight, for all admissible }m.
\]

Recommended Driver action:

- accept this task at the obstruction terminal class;
- freeze generic common-measure/order-map/SSR/normalizer-TN arguments as
  insufficient;
- if a successor is justified, require it to use
  \((1-u^{m^2})^{m-1}\) essentially, preferably through an exact
  \(t:0\to1\) Christoffel-weight deformation or another explicitly
  AP-sensitive invariant;
- do not reopen generic STP, entrywise Perron, ordinary norm contraction,
  finite-\(m\)-as-proof, or normalized complete monotonicity.
