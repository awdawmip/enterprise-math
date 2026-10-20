# BRC_FEATURE_LIFT_INERTIA — signed Fock representation of higher-order Xi comparison carriers

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`

Status:

`FINITE_FEATURE_LIFT_FOUND / CUBIC_LORENTZIAN_SIGNATURE_PROVED / LINEAR_MONOTONE_FEATURE_WINDOW / SIGNED_FOCK_BRC_FORMULATION / RH_NOT_CLOSED`

## 1. From centered polynomial carriers to a finite bilinear feature metric

Consider a centered degree-`m` comparison exponent

`L_m(s)=-(tau/2)s(s-1)+sum_(d=3)^m a_d P_d(s)`,

where `P_d(s)=s^d-s` for odd `d` and `P_d(s)=s^d-s^2` for even `d`.
For the reversed-Hankel block put

`s=D-i-j`, `D=r-1`.

Expand `L_m(D-i-j)`. Terms depending only on `i`, only on `j`, or on neither can be removed
by a positive diagonal congruence. The remaining mixed polynomial is symmetric in `i,j` and
contains only monomials

`i^p j^q`, `p,q>=1`, `p+q<=m`.

Therefore, with

`Phi_m(i)=(i,i^2,...,i^(m-1))^T`,

there is an explicit real symmetric `(m-1)x(m-1)` matrix `A_m` such that the retained
comparison block is positive-diagonally congruent to

`boxed: K_m(i,j)=exp(Phi_m(i)^T A_m Phi_m(j)).`

Hence determinant sign and inertia are unchanged by passing to this finite feature metric.

This is an exact representation, not an asymptotic expansion.

## 2. Exact signed Fock / Cauchy--Binet expansion

Diagonalize

`A_m=Q^T diag(lambda_1,...,lambda_L) Q`

on its nonzero range and define

`psi_l(i)=(Q Phi_m(i))_l`.

Then

`K_m(i,j)=product_l exp(lambda_l psi_l(i)psi_l(j))`

has the absolutely convergent feature expansion

`K_m(i,j)=sum_(n in N^L) w_n Psi_n(i)Psi_n(j)`,

with

`w_n=product_l lambda_l^(n_l)/n_l!`,
`Psi_n(i)=product_l psi_l(i)^(n_l)`.

Let `F_(i,n)=Psi_n(i)` and `W=diag(w_n)`. Formally `K=F W F^T`; truncating the occupation
set makes this finite-dimensional, and the absolute-weight kernel

`sum_n |w_n|Psi_n(i)Psi_n(j)`

is finite at every matrix entry. Thus finite Cauchy--Binet followed by monotone/absolute
convergence gives

`boxed:
 det K_m
 =sum_(S, |S|=r)
   det[Psi_n(i)]_(i,n in S)^2
   product_(n in S) w_n.`

Every evaluation determinant is squared and hence nonnegative. All branch signs live in the
feature weights.

This is a natural **signed/amplitude BRC carrier**:

- branch token: a finite set of feature occupation vectors;
- amplitude: squared generalized-Vandermonde evaluation times `|w|`;
- sign: parity of occupation in negative eigen-directions of `A_m`.

No hidden matrix-sign operation remains in the branch definition.

## 3. Quadratic carrier as the rank-one special case

For `m=2`,

`A_2=[-tau]`.

There is one negative feature direction and

`K_2(i,j)=exp(-tau i j)=q^(ij)`,

the exact q-Vandermonde model of the published cubic-wedge proof.

Thus the q-Pascal calculus is the rank-one negative-metric member of the feature-lift family.

## 4. Cubic carrier is intrinsically Lorentzian

Retain the cubic coefficient

`a_3=f'''(k)/3!`.

Expanding

`a_3(D-i-j)^3`

and discarding row/column-only terms leaves

`6D a_3 i j -3a_3(i^2j+i j^2)`.

Hence

`boxed:
 A_3=
 [[-tau+6D a_3, -3a_3],
  [-3a_3,          0   ]].`

Its determinant is

`boxed: det A_3=-9 a_3^2.`

Therefore:

- if `a_3=0`, the cubic lift collapses back to the rank-one quadratic carrier;
- if `a_3!=0`, `A_3` has exactly one positive and one negative eigenvalue.

So a nontrivial cubic comparison carrier is necessarily a **Lorentzian two-feature model**.
There is no legitimate inference that the quadratic q-Pascal inertia simply persists after
adding the cubic mode.

## 5. A theorem-grade linear window for monotone eigen-features

The published all-degree Xi bound gives specifically

`|a_3|<=3*40^3/k^2=192000/k^2`.

The curvature window gives

`tau>1/(2k)`.

Thus

`|a_3|/tau<384000/k`.

If

`boxed: k>4,608,000 r`,

then

`12r |a_3|/tau<1`.

This has three consequences.

### 5.1 Strong negative diagonal entry

With `D=r-1`,

`A_11=-tau+6D a_3<-tau/2`

(the negative-`a_3` case is even more negative).

### 5.2 Negative eigen-feature is strictly increasing

Let `lambda_-<0` be the negative eigenvalue. An eigenvector can be written

`(1,rho_-)`, `rho_-=(-3a_3)/lambda_-`.

Since `|lambda_-|>=|A_11|>tau/2`,

`|rho_-|<6|a_3|/tau<1/(2r)`.

Thus

`psi_-(i)=i+rho_- i^2`

satisfies, for `0<=i<r-1`,

`psi_-(i+1)-psi_-(i)=1+rho_-(2i+1)>1/(2r)>0`.

### 5.3 Positive eigen-feature is also strictly increasing

Writing the positive eigenvector as `(rho_+,1)`, the product relation
`lambda_+ lambda_-=-9a_3^2` gives

`|rho_+|=|lambda_+/(-3a_3)|=3|a_3|/|lambda_-|<1/(2r)`.

Hence

`psi_+(i)=i^2+rho_+ i`

is strictly increasing as well.

Therefore, throughout the explicit linear window `k>4,608,000r`, the cubic carrier is an
exponential kernel on two **ordered** feature coordinates, one negative-metric and one
positive-metric.

## 6. The negative-mode kernel is already sign-regular

The pure negative component is

`K_-(i,j)=exp(lambda_- psi_-(i)psi_-(j))`, `lambda_-<0`.

Because `psi_-(0)<...<psi_-(r-1)`, the classical strict total positivity of the exponential
kernel `exp(xy)` implies that, after reversing the columns, `K_-` is strictly totally positive.
Thus its ordered minors have the expected sign-regular signature

`(-1)^(s(s-1)/2)`

at order `s`.

So one full part of the cubic inertia problem is already closed on a **linear** `k/r` scale.

## 7. Why the positive feature cannot be discarded by a generic closure rule

The full cubic kernel factors entrywise as

`K_3=K_- o K_+`,

`K_+(i,j)=exp(lambda_+ psi_+(i)psi_+(j))`, `lambda_+>0`.

`K_+` is strictly totally positive because `psi_+` is ordered. However, total positivity is not
preserved by arbitrary Hadamard products in general; therefore no generic theorem permits us to
conclude that `K_- o K_+` retains the sign-regularity of `K_-`.

This kills a tempting but invalid shortcut.

The correct representation is the signed Fock expansion of Section 2, where occupation of the
positive and negative metric directions is retained explicitly.

## 8. New hard bridge

The degree-ladder problem is now sharpened to

`LORENTZIAN_FOCK_DOMINATION`:

> in the Xi-admissible parameter region, control the signed Fock branch sum of the cubic
> Lorentzian feature metric relative to its exactly sign-regular negative-mode kernel, and then
> iterate the construction as quartic and higher feature directions are activated.

This is more structured than arbitrary matrix inertia:

- the feature metric has finite rank;
- its signature is explicit at cubic order;
- the matrix entries are exponential bilinear kernels on a discrete moment curve;
- branch amplitudes are squares of generalized Vandermonde determinants;
- all cancellation is isolated in signed feature weights.

## 9. Relation to the carrier-order ladder

`BRC_CARRIER_ORDER_LADDER.md` shows that retaining more modes reduces the analytic-tail exponent
toward the RH-critical linear scale. The present file identifies the nonperturbative object that
must replace the q-Pascal scalar carrier when that refinement happens:

`scalar q metric -> finite signed feature metric A_m -> signed Fock BRC`.

Thus the two research axes now meet exactly.

## 10. Classification

Proved here:

- finite bilinear feature lift for every fixed polynomial carrier order;
- exact signed Fock/Cauchy--Binet determinant representation;
- cubic metric signature `(1 positive, 1 negative)`;
- explicit `k>4,608,000r` monotone-feature window;
- exact sign-regularity of the pure negative cubic feature kernel.

Open:

- signed Fock domination after the positive feature is restored;
- higher-order feature-metric signature/stability;
- RH.

Final status: `RH_NOT_CLOSED`.
