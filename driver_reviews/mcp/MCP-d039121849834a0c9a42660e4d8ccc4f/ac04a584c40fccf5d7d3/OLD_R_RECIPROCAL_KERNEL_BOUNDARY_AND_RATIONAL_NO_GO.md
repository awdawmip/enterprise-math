# OLD-R reciprocal-kernel boundary and bounded rational-antidifference no-go

Status: BOUNDED LOCAL MATHEMATICS / EXACT SYMBOLIC PREPARATION / NO SCALAR CLOSURE.
Date: 2026-10-11. No remote, Source, native, Task, claim, or accepted-result write was performed. No prime computations were performed.

Inputs read: `SHARED_GAUSS_GREEN_KERNEL_NEXT_UNIT_PREPARATION.md` and `FINITE_ADJOINT_GAUSS_CONCOMITANT_PREPARATION.md` in `cm24-next-p3-20261011`. The unique source-pinned OLD-R constructor is retained literally. This note does not define OLD-R from the reverse carrier, the new pairing, or the proposed lift target.

For p=6m+1, write
\[
 a_i=\frac{(1/6)_i(1/3)_i}{(i!)^2},\qquad
 B_i=2^{-i}a_i,\qquad
 D_r=\frac{2^{r-1}(r-1)!^2}{18(5/6)_r(2/3)_r}.
\]
The pinned sum is
\[
 R_p=2\sum_{i=1}^m B_i\sum_{r=1}^i(1+6(i-r))D_r\pmod p.
\]
All identities below are rational finite identities before reduction unless explicitly marked mod p.

## 1. The reciprocal kernel and reversed Gauss polynomial use one operator

Set
\[
 \mathcal D_m(z)=\sum_{r=1}^mD_rz^r,\qquad
 A_m(z)=\sum_{i=0}^mB_i z^{-i},\qquad
 \theta=z\partial_z,
\]
and
\[
 L=(\theta-1/6)(\theta-1/3)-2z\theta^2
   =(1-2z)\theta^2-\tfrac12\theta+\tfrac1{18}.
\]
The coefficient ratios are
\[
 \frac{B_{i+1}}{B_i}
 =\frac{(i+1/6)(i+1/3)}{2(i+1)^2},\qquad
 \frac{D_{r+1}}{D_r}
 =\frac{2r^2}{(r+5/6)(r+2/3)}.
\]
Consequently, including both finite endpoints,
\[
 \boxed{L\mathcal D_m=\frac z{18}-2m^2D_mz^{m+1},}
\]
\[
 \boxed{LA_m=(m+1/6)(m+1/3)B_mz^{-m}.}
\]
For the first equation, the coefficient of z is
\((5/6)(2/3)D_1=1/18\); all middle coefficients cancel by the D ratio, and the last displayed term is the exact truncation boundary. For the second equation, all coefficients through z^{-(m-1)} cancel by the B ratio. Mod p, m+1/6=0, so LA_m=0. In the notation of the finite-adjoint preparation,
\[
 A_m(z)=V_p\bigl(1/(2z)\bigr)\pmod p.
\]
This explains the common reciprocal kernel. It does not identify its different observers.

## 2. Exact finite residue boundary with a remaining fixed triangular term

Freeze the following independent residual from the same OLD-R coefficients:
\[
 \boxed{T_m=
 \sum_{r=1}^mD_r\sum_{i=0}^{r-1}
      (6(r-i)-1)B_i.}\tag{T}
\]
This is a fixed finite sum. It has not been evaluated or chosen by reading a target scalar.

Let F(z)=A_m(z)\mathcal D_m(z). The OLD-R constant-term formula is exactly
\[
 \frac{R_p}{2}
 =\operatorname{CT}_z F(z)\frac{1+5z}{(1-z)^2}.
\]
Here coefficient extraction uses the expansion at z=0, and F is a finite Laurent polynomial. The rational one-form uses
\[
 \frac{1+5z}{z(1-z)^2}
 =\frac1z+\frac1{1-z}+\frac6{(1-z)^2}.
\]
Its residues at 0, 1, and infinity are, respectively,
\[
 \frac{R_p}{2},\qquad
 6F'(1)-F(1),\qquad
 -T_m.
\]
For the last equality, the coefficient of z^{-(k+1)} in the expansion of the rational factor at infinity is 6k-1 for k>=1; the coefficient F_k is \(\sum_{r-i=k}D_rB_i\). The finite residue theorem therefore gives
\[
 \boxed{\frac{R_p}{2}
 =A_m(1)\mathcal D_m(1)
  -6\bigl(A_m\mathcal D_m\bigr)'(1)+T_m.}\tag{BOUNDARY}
\]
Equivalently,
\[
 \boxed{R_p=
 2[A_m(1)-6A_m'(1)]\mathcal D_m(1)
 -12A_m(1)\mathcal D_m'(1)+2T_m.}
\]
The same formula follows by splitting all pairs (i,r) according to i>=r and r>i: the weight in F(1)-6F'(1) is 1-6(r-i). This supplies a direct finite algebraic verification with no analytic convergence requirement.

Under the inherited CM0 condition V_p(1/2)=0,
\[
 A_m(1)=0,\qquad A_m'(1)=-\tfrac12V_p'(1/2).
\]
Thus the exact mod-p specialization is
\[
 \boxed{R_p=6V_p'(1/2)\mathcal D_m(1)+2T_m\pmod p.}\tag{CM-BOUNDARY}
\]
This is a boundary reduction with an explicit residual, not an evaluation of OLD-R. In particular, T_m must remain in any claimed scalar comparison unless it is independently evaluated.

## 3. Proved no-go for the two elementary one-variable rational ansatzes

The following is a characteristic-zero statement about a universal rational certificate. It does not rule out special finite-field certificates of growing degree, a two-variable certificate, a higher-order telescoper, or a different function class.

For the i summation, consider exactly
\[
 \Delta_i[Q(i)B_i]=P(i)B_i,
 \qquad P(i)=1+6(i-r),\qquad Q\in\mathbf Q(r)(i),
\]
where \(\Delta_i H(i)=H(i+1)-H(i)\). Using the displayed B ratio, this requires
\[
 (i+1/6)(i+1/3)Q(i+1)-2(i+1)^2Q(i)
 =2(i+1)^2P(i).\tag{B-GOSPER}
\]
There is no such rational Q. To prove this, take any finite chain of poles of Q in an integer-shift orbit, with its first and last poles alpha and beta. At i=alpha-1 only Q(i+1) has the endpoint pole, so alpha must be 5/6 or 2/3. At i=beta only Q(i) has the endpoint pole, so beta must be -1. These values cannot be endpoints of one integer-shift orbit. Thus Q has no finite poles and is polynomial. At i=-1 the polynomial identity forces Q(i+1) to be divisible by (i+1)^2, so i^2 divides Q(i). If Q has degree d and nonzero leading coefficient, the left side of (B-GOSPER) has degree d+2 because its leading multipliers are 1 and -2. The right side has degree 3. Hence d=1, contradicting i^2|Q. This proves the stated ansatz no-go.

For the r summation, consider exactly
\[
 \Delta_r[Q(r)D_r]=P(r)D_r,
 \qquad P(r)=6(r-i)-1,\qquad Q\in\mathbf Q(i)(r).
\]
Using the D ratio, this requires
\[
 2r^2Q(r+1)-(r+5/6)(r+2/3)Q(r)
 =(r+5/6)(r+2/3)P(r).\tag{D-GOSPER}
\]
Again no such rational Q exists. A first pole alpha in an integer-shift orbit must be 1, from the factor 2r^2 at r=alpha-1. A last pole beta must be -5/6 or -2/3, from the other quadratic factor at r=beta. These are incompatible integer-shift endpoints, so Q is polynomial. Evaluation at r=-5/6 and r=-2/3 forces Q(1/6)=Q(1/3)=0. Thus a nonzero Q has degree at least 2. The leading multipliers 2 and -1 imply that the left side has degree d+2, while the right side has degree 3, forcing d=1. This is a contradiction.

The proof also covers any nonzero affine weight in these same ansatzes. In particular it applies to the OLD-R inner D sum with weight 1+6(i-r), to its swapped B tail, and to both inner sums in (T). An exact SymPy `gosper_term` call returned `None` for the two displayed affine-weight terms as well as the unweighted B and D terms. That call is corroborating algorithm output; the pole/degree arguments above provide the mathematical no-go for the precisely stated rational ansatzes.

## 4. Minimal unresolved interface

The remaining term is exactly (T), and the most compact CM boundary is (CM-BOUNDARY). The D endpoint is the independently fixed single sum
\[
 \mathcal D_m(1)=
 \sum_{r=1}^m\frac{2^{r-1}(r-1)!^2}{18(5/6)_r(2/3)_r}.
\]
No elementary one-variable rational Gosper certificate can eliminate either affine-weight triangular inner sum uniformly in characteristic zero. A further closure therefore needs a genuine two-variable or higher-order adjoint certificate, or an independent evaluation of T_m; it cannot be claimed from the reciprocal-kernel observation alone. No proposed lift equality, divided-M digit, reverse-C value, or CM period normalization was assumed.
