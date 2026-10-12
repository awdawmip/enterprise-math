# OLD-R fourth-order finite telescoper with fixed diagonal boundaries

Status: BOUNDED PAPER DERIVATION / EXACT RATIONAL CERTIFICATE / LIFT OPEN.
Date: 2026-10-12. No prime computations, remote calls, Source writes, native
mutations, formal Task writes, campaign, or accepted-result changes were made.

This note retains the source-pinned OLD-R constructor from
`OLD_R_RECIPROCAL_KERNEL_BOUNDARY_AND_RATIONAL_NO_GO.md`. It does not define
OLD-R from a reverse carrier, an adjoint pairing, or a proposed lift value.
The finite-adjoint note is used only to identify the unresolved scalar
comparison. The exact identities below hold over the rationals for every
nonnegative truncation index.

## 1. Fixed sequences and the diagonal-band telescoper

Set

\[
B_i=2^{-i}\frac{(1/6)_i(1/3)_i}{(i!)^2},\qquad
D_r=\frac{2^{r-1}(r-1)!^2}{18(5/6)_r(2/3)_r},\quad r\ge1,
\]

\[
H_n=\sum_{r=1}^{n}(1+6(n-r))D_r,\quad H_0=0,
\qquad
R_n=2\sum_{i=1}^{n}B_iH_i,\quad R_0=0.
\]

The OLD-R sum at its fixed endpoint is exactly \(R_m\); reduction modulo
\(p=6m+1\) is a subsequent operation, not part of these definitions.

For every \(n\ge2\),

\[
\boxed{E_n:=H_n-2H_{n-1}+H_{n-2}=D_n+5D_{n-1}.}\tag{1}
\]

**Proof.** For each \(r\le n-2\), its coefficient on the left is

\[
[1+6(n-r)]-2[1+6(n-1-r)]+[1+6(n-2-r)]=0.
\]

The coefficient at \(r=n-1\) is \(7-2=5\), and the coefficient at
\(r=n\) is \(1\). These are all terms. Thus the second difference
annihilates the affine triangular weight in its interior and retains
precisely the last two diagonal bands. No antidifference or infinite
series is required.

This is the finite inner-sum telescoper. Its boundary is not zero and is
not selected by a target scalar.

## 2. Third-order recurrence for the inner triangle

Write

\[
A_n=(n-\tfrac16)(n-\tfrac13),\qquad
P_n=126n^2-117n+41.
\]

The original ratio gives, for \(n\ge2\),

\[
\frac{D_n}{D_{n-1}}=\frac{2(n-1)^2}{A_n},\qquad
2(n-1)^2+5A_n=\frac{P_n}{18}.
\]

Consequently

\[
E_n=\frac{P_n}{18A_n}D_{n-1},\qquad
\frac{E_{n+1}}{E_n}
=\frac{2(n-1)^2P_{n+1}}{A_{n+1}P_n}.
\]

Equivalently, without division by \(P_n\),

\[
\boxed{A_{n+1}P_n(H_{n+1}-2H_n+H_{n-1})
-2(n-1)^2P_{n+1}(H_n-2H_{n-1}+H_{n-2})=0.}\tag{2}
\]

This is an explicit third-order recurrence with fixed coefficients and
the directly constructed initial values

\[
H_0=0,\qquad H_1=\frac1{10},\qquad H_2=\frac{421}{550}.
\]

The derivation proves (2) for all \(n\ge2\). It is not a claim that (2)
is a minimal recurrence.

## 3. Fourth-order scalar OLD-R recurrence

Define \(J_n=R_n-R_{n-1}\) for \(n\ge1\), and extend the boundary by
\(R_{-1}=R_0=0\), so \(J_0=0\). Then

\[
J_n=2B_nH_n\quad(n\ge0).
\]

Let

\[
C_n=(n+\tfrac16)(n+\tfrac13),\qquad
X_n=(n-\tfrac56)(n-\tfrac23),\qquad
Y_n=(n-\tfrac{11}6)(n-\tfrac53),
\]

\[
e_n=J_n-\frac{X_n}{n^2}J_{n-1}
+\frac{X_nY_n}{4n^2(n-1)^2}J_{n-2}\quad(n\ge2).
\]

Since \(B_n/B_{n-1}=X_n/(2n^2)\), equation (1) gives
\(e_n=2B_nE_n\). Equation (2) therefore becomes

\[
\boxed{(n+1)^2A_{n+1}P_ne_{n+1}
-(n-1)^2C_nP_{n+1}e_n=0,\qquad n\ge2.}\tag{3}
\]

In particular, the triangular double sum now satisfies a single explicit
scalar recurrence. For a form with integer polynomial coefficients, put

\[
a_n=(6n+5)(3n+2),\quad c_n=(6n+1)(3n+1),
\quad x_n=(6n-5)(3n-2),\quad y_n=(6n-11)(3n-5),
\]

\[
\begin{aligned}
\alpha_n&=1296n^2(n+1)^2a_nP_n,\\
\beta_n&=-72n^2c_n\bigl(a_nP_n+18(n-1)^2P_{n+1}\bigr),\\
\gamma_n&=c_nx_n\bigl(a_nP_n+72(n-1)^2P_{n+1}\bigr),\\
\delta_n&=-c_nx_ny_nP_{n+1}.
\end{aligned}
\]

Multiplying (3) by \(4n^2\cdot18^3\) gives

\[
\boxed{\alpha_nJ_{n+1}+\beta_nJ_n+\gamma_nJ_{n-1}
+\delta_nJ_{n-2}=0.}\tag{4}
\]

Substitution of \(J_j=R_j-R_{j-1}\) yields the promised fourth-order
finite telescoper:

\[
\boxed{\begin{aligned}
0={}&\alpha_nR_{n+1}+(\beta_n-\alpha_n)R_n
+(\gamma_n-\beta_n)R_{n-1}\\
&+(\delta_n-\gamma_n)R_{n-2}-\delta_nR_{n-3},
\qquad n\ge2.
\end{aligned}}\tag{5}
\]

There is no omitted term at \(n=2\): its last value is the fixed boundary
\(R_{-1}=0\). The initial values are

\[
R_{-1}=R_0=0,\qquad R_1=\frac1{180},\qquad
R_2=\frac{4927}{356400}.
\]

For reference, (5) at \(n=2\) gives
\(R_3=7604467/392610240\), also obtained directly from the finite sum.
Since \(\alpha_n\ne0\) over \(\mathbb Q\) for every integer \(n\ge2\),
these fixed boundaries and (5) determine the whole rational sequence.
Equivalently one may start at \(n=3\) from \(R_0,R_1,R_2,R_3\).
This is a genuine higher-order boundary certificate for OLD-R. It
evaluates neither a CM period nor a lift digit.

## 4. Exact terminal specialization and its limitation

This section is symbolic finite-field algebra; no prime was computed or
sampled. Suppose \(p=6m+1\ge7\) is prime. The rational constructors for
\(B_i\) through \(i=m+1\), \(D_r\) through \(r=m+1\), and \(R_n\) through
\(n=m+1\) have denominators that are units modulo \(p\). For \(D_r\),
the numerator factors in the denominator parameters are \(6j+5\) and
\(3j+2\), with \(0\le j\le m\). The former cannot equal \(p\), and is
below \(2p\); the latter is below \(p\). The factorial and powers of
\(2,3\) are also units. The corresponding claim for \(B_i\) follows
immediately from \((m+1)!\) being a unit.

At the terminal index, \(m\equiv-1/6\pmod p\), so

\[
c_m=0,\qquad a_m=6,\qquad P_m=64,\qquad
\alpha_m=9600\pmod p.
\]

Thus, for \(m\ge2\), the terminal specialization of (4) or (5) is
exactly

\[
\boxed{9600\,(R_{m+1}-R_m)=0\pmod p.}\tag{6}
\]

The coefficient is a unit for every prime of the stated form. The
same equality \(R_{m+1}=R_m\) follows directly from
\(B_{m+1}=0\pmod p\), including the exceptional index \(m=1\), for
which the recurrence at \(n=m\) lies outside its proved range.

Equation (6) is the exact terminal collapse. It fixes the next
increment to zero and imposes no condition on the value of \(R_m\).
The recurrence has an explicit right factor \(\Delta R\), so a terminal
condition on the increment cannot supply an additive scalar
normalization. Also, no argument here excludes an interior \(P_n\) from vanishing in
characteristic \(p\); no uniform division by such factors or finite-field
uniqueness is asserted. The polynomial identity (5) itself remains valid without
those divisions.

In particular, neither (5) nor (6) proves the separate first-digit gate
\(U\equiv1\pmod p\), nor the remaining comparison

\[
U\equiv1+p(R_p+6\tau_p)\pmod {p^2}.
\]

Here \(U\) and \(\tau_p\) retain the independent constructors from the
finite-adjoint preparation. No normalization was chosen by reading either target.

## 5. Precisely scoped failed ansatzes

The disjoint note
`polynomial-subhelper/POLYNOMIAL_AND_DIAGONAL_ANSATZ_CHECKS.md` proves two
narrow checks on the fixed weight \(1+6(i-r)\): the prescribed polynomial
adjoint factorization \(Q=i^2q\),
\(S=(r-1/6)(r-1/3)s\), with polynomial \(q,s\), cannot supply the affine
divergence; and one rational simultaneous-diagonal flux cannot supply
it. These statements explain two unsuccessful lower-order approaches.
Arbitrary independent rational two-variable flux pairs remain
unexcluded. They are not needed for the higher-order finite certificate
above. LIFT remains OPEN.

## Verification

`check_fourth_order_telescoper.py` verifies the rational coefficient
identities, the conversion of (3) to (4), the fixed initial boundaries,
and the symbolic terminal evaluation \(n=-1/6\). It also checks the
finite rational constructors through abstract truncation index 10;
there are no modular calculations or selected-prime comparisons.
The proofs above establish all-index validity; the finite checks are
corroboration only.
