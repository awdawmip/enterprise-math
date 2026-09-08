# #1162 — cycle rooted-forest refoundation of the even inverse-spectrum hierarchy

Status: RESEARCH_NOTE / FINITE GRAPH REFOUNDATION / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-cycle-forest-refoundation-20260908-b62d
Date: 2026-09-08

## 1. Goal

Continue the derivative-admissibility correction by removing the remaining dependence on trigonometric diagonalization/cosecant power sums from the higher even inverse-spectrum side of #1162.

The only inputs below are finite cycle graphs, the matrix-forest theorem, finite composition counting, characteristic-polynomial algebra, and Newton identities. Hyperbolic/trigonometric functions appear only later as optional formal generating-series or classical compatibility readouts.

## 2. Rooted-forest coefficients of the cycle

Let `C_N` be the unit-edge cycle, `N>=3`, with combinatorial Laplacian `L_N`.

The matrix-forest theorem gives

`det(L_N+tI)=sum_{r=1}^N c_r(N) t^r`,

where `c_r(N)` is the sum, over spanning forests with r components, of the product of component sizes (equivalently the number of choices of one root in each component).

A spanning forest with r components is obtained by cutting r cycle edges. If the resulting cyclic component lengths are `ell_1,...,ell_r`, then `ell_i>=1`, `sum ell_i=N`, and the rooted weight is `prod ell_i`.

Distinguish one cut edge. There are N choices of the distinguished starting cut, while each unmarked forest is counted r times. Hence

`r c_r(N) = N sum_{ell_1+...+ell_r=N, ell_i>=1} prod_i ell_i`.

Since

`sum_{ell>=1} ell x^ell = x/(1-x)^2`,

we obtain the closed finite formula

`c_r(N) = (N/r) [x^N](x/(1-x)^2)^r
         = (N/r) binom(N+r-1,2r-1)`.

Thus

`det(L_N+tI)=sum_{r=1}^N (N/r) binom(N+r-1,2r-1)t^r`.

This proof is finite and combinatorial; no eigen-angle or sine formula is used.

## 3. Elementary inverse-spectrum coefficients

The nonzero Laplacian eigenvalues are denoted only algebraically by `lambda_i`; no explicit diagonalization is needed. Put

`D_N(t)=det(L_N+tI)/t = product_{i=1}^{N-1}(lambda_i+t)`.

The constant term is `D_N(0)=N^2`, as also follows from the r=1 forest coefficient.

Normalize

`F_N(t)=D_N(t)/N^2 = product_i (1+t/lambda_i)
       = sum_{k>=0} e_k(N)t^k`.

The forest formula gives, for every k>=0 (with the expression automatically zero when k>=N),

`e_k(N)=1/[N(k+1)] binom(N+k,2k+1)`

and the symmetric factorization

`e_k(N)=prod_{j=1}^k (N^2-j^2)/[(k+1)(2k+1)!]`.

Therefore every fixed `e_k(N)` is a polynomial in `N^2` of degree k.

## 4. Newton identities give all inverse moments

Let

`p_m(N)=sum_i lambda_i^(-m)=Tr[(L_N^+)^m]`.

Because the `e_k` are the elementary symmetric functions of the variables `lambda_i^(-1)`, Newton's identities give the finite recurrence

`p_m - e_1 p_(m-1) + e_2 p_(m-2) - ...
 + (-1)^(m-1)e_(m-1)p_1 + (-1)^m m e_m = 0`.

Consequently `p_m(N)` is a polynomial in `N^2` of degree m, derived entirely from finite rooted-forest data.

The first cases are

`p_1=(N^2-1)/12`,

`p_2=(N^4+10N^2-11)/720`,

`p_3=(2N^6+21N^4+168N^2-191)/60480`.

For the dimensionless normalized cycle readouts

`b_m(N)=2^(2m-1) N^(-2m) p_m(N)`,

this gives

`b_1=1/6 - 1/(6N^2)`,

`b_2=1/90 + 1/(9N^2) - 11/(90N^4)`,

`b_3=1/945 + 1/(90N^2) + 4/(45N^4) - 191/(1890N^6)`.

Thus the finite correction model required by the derivative-free refinement projector is now proved from finite graph combinatorics for every m; it is no longer imported from cosecant power sums.

## 5. Purely finite refinement invariants

Apply the already-derived finite projector

`Pi_(m,q)=prod_{r=1}^m (E_q-q^(-2r)I)/(1-q^(-2r))`,

`(E_q f)(N)=f(qN)`.

Since `b_m(N)` is a polynomial in `N^(-2)` of degree m,

`Pi_(m,q)b_m` is exactly the constant/top coefficient, independently of N and q.

For dyadic refinement:

`Pi_(1,2)b_1=1/6`,

`Pi_(2,2)b_2=1/90`,

`Pi_(3,2)b_3=1/945`.

These are finite graph refinement invariants before any angular/continuum identification.

## 6. Leading coefficients from forests alone

Let

`gamma_m = [N^(2m)] p_m(N)`

and let

`alpha_k=[N^(2k)]e_k(N)`.

From the product formula,

`alpha_k=1/[(k+1)(2k+1)!]=2/(2k+2)!`.

The same Newton recurrence therefore determines all `gamma_m` using only the rational sequence `alpha_k`.

Define the normalized invariant

`C_m=2^(2m-1) gamma_m`.

The first values are

`C_1=1/6`,
`C_2=1/90`,
`C_3=1/945`,
`C_4=1/9450`,
`C_5=1/93555`,
`C_6=691/638512875`.

No pi or zeta value is required to define or compute these rationals.

## 7. Formal determinant generating series

The leading elementary coefficients have the formal generating series

`sum_{k>=0} alpha_k u^k
 = sum_{k>=0} 2u^k/(2k+2)!
 = 2(cosh(sqrt(u))-1)/u
 = [2sinh(sqrt(u)/2)/sqrt(u)]^2`.

As a formal power-series identity,

`log(sum alpha_k u^k)
 = sum_{m>=1} (-1)^(m+1) gamma_m u^m/m`.

After the purely algebraic rescaling `u -> 4u` and `C_m=2^(2m-1)gamma_m`,

`log(sinh(sqrt(u))/sqrt(u))
 = sum_{m>=1} (-1)^(m+1) C_m u^m/m`.

This is an optional compact generating readout of the forest invariants. It is not needed for their finite definition.

## 8. Classical compatibility, kept separate

In the classical angular/Fourier completion one has the standard product for `sinh(sqrt(u))/sqrt(u)`, which identifies

`C_m = zeta(2m)/pi^(2m)`.

That identification is a compatibility/calibration statement at the classical analytic layer. The Enterprise/discrete content established here is prior: `C_m` is already a finite rational invariant extracted from cycle rooted-forest counts and integer refinement.

In particular the Basel coefficient `1/6` exists on the finite graph side before pi is introduced by angular calibration.

## 9. BRC typing

REUSE_APPLIED: retain component-size multiplicity in the rooted-forest carrier until the characteristic-polynomial observer is formed. The product of component sizes is theorem-critical and is not collapsed to Boolean forest support. After the exact characteristic coefficients are obtained, Newton projection is an allowed finite algebraic readout.

No positive-weight recurrent BRC theorem is needed. No microscopic derivative is introduced.

## 10. Prior-art boundary

The matrix-forest theorem and rooted-forest interpretation of `det(L+tI)` are classical prior art. Cycle rooted-forest polynomials and their Chebyshev/binomial descriptions also have literature. The finite combinatorial derivation is used here as a refoundation route, not claimed as historical invention.

The project-level synthesis to evaluate later is the combination:

`rooted-forest finite determinant -> inverse-moment polynomiality -> uniformly stable integer-refinement quotient -> finite even-zeta/pi invariants`,

with the continuum identification explicitly withheld until the compatibility layer.

## Next

1. Derive cross-q consistency/falsification identities directly from the forest coefficient representation.
2. Investigate whether the sequence `C_m` admits a purely finite combinatorial recurrence/interpretation avoiding even the formal hyperbolic generating series.
3. Quantify how model defects outside the exact cycle family propagate through the `<2` refinement projector.
