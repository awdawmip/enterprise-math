# Perfect Prime AP Christoffel J-Transversality Deformation Flow — Research Return

Researcher-ID: `EM-PPTAPCHR1-72C3D3`  
Task: `RS-PERFECT-PRIME-AP-CHRISTOFFEL-J-TRANSVERSALITY-DEFORMATION`  
Publication: `TP2-7A1C9E54B2306D8F41AA`  
Claim: `chatgpt-pptapchr1-20260830-1614-72c3d3`  
Execution record: `ER-39853B84DC87918FA440`

## Terminal verdict

`SUCCESS / ALL_M_LOCAL_J_TRANSVERSALITY_PROVED / GLOBAL_POINTWISE_CROSSING_FORM_FLOW_EXACTLY_OBSTRUCTED_AT_M=3`.

This execution proves the strict local splitting theorem demanded by the task for every `m>=2`, including the exact first nonzero order at the Cauchy endpoint. It also isolates the first exact obstruction to globalizing that proof by requiring the infinitesimal crossing form to remain nondegenerate on all of `(0,1]`.

It does **not** prove the full all-`m` no-recrossing statement `det(I-Q_(m,t)) != 0` for every `0<t<=1`. The `m=3` obstruction below is an obstruction to the pointwise-derivative / regular-crossing globalization strategy, not a counterexample to the AP parent theorem.

## 1. Frozen deformation and J-defect

Put

- `n=m-1`,
- `a=m^2`,
- `x_i=i+1`,
- `y_j=m*j`,
- `w_j=(-1)^j*C(n,j)`,
- `W=diag(w_j)`,
- `Lambda=diag(C(n,j))`,
- `J=diag((-1)^j)`.

Common scalar normalization is immaterial for the normalized half maps, so use

`H_t(i,j) = int_0^1 u^(i+m*j) (1-t*u^a)^n du`

and hence exactly

`H_t(i,j) = sum_(r=0)^n (-1)^r C(n,r) t^r / (x_i+y_j+a*r)`.

Let

`e_t=H_t w`, `d_t=H_t^T w`, `E_t=diag(e_t)`, `D_t=diag(d_t)`,

`A_t=E_t^-1 H_t W`, `B_t=D_t^-1 H_t^T W`, `K_t=B_t A_t`.

As in the accepted principal-angle reduction, define

`P_t=E_t Lambda`, `Q_t=D_t Lambda`, `X_t=A_t J=E_t^-1 H_t Lambda`

and the symmetric J-defect

`Delta_t = J - Z_t^T J Z_t`,
`Z_t=P_t^(1/2) X_t Q_t^(-1/2)`.

For exact rational work remove the square roots by positive diagonal congruence:

`Gamma_t := Q_t^(1/2) Delta_t Q_t^(1/2)
          = Q_t J - X_t^T P_t J X_t`.

The previously frozen identity gives equivalently

`Gamma_t = J [ D_t W (I-K_t) ] J`.

Therefore

`rank(Gamma_t)=rank(I-K_t)`,

and the known fixed direction is the constant vector for `K_t`, or the fixed kernel vector

`s := (1,-1,1,-1,...)^T`

for `Gamma_t`.  In particular `Gamma_t s=0` for every `t`.

At `t=0` the Cauchy interpolation control gives `K_0=I`, hence `Gamma_0=0`.

## 2. Signed bipartite Laplacian realization

Introduce the symmetric `2m x 2m` matrix

`L_t = [[ W E_t,        -W H_t W ],
        [ -W H_t^T W,   W D_t   ]]`.

It is the signed weighted bipartite Laplacian with edge weights

`c_ij(t)=w_i w_j H_t(i,j)`,

because

`[p;q]^T L_t [p;q]
 = sum_(i,j) c_ij(t) (p_i-q_j)^2`.

The block `W E_t` is invertible for `0<=t<=1`: indeed

`e_i(t)=int_0^1 u^i (1-u^m)^n (1-t*u^a)^n du > 0`.

Its Schur complement is

`W D_t - W H_t^T W E_t^-1 H_t W
 = D_t W (I-K_t)`.

Thus the quotient J-transversality problem is exactly the nondegeneracy of this Schur complement after its one forced kernel direction.

At `t=0`, `K_0=I`, so `ker(L_0)` has dimension `m`.  If `q_j=f(y_j)` for the unique polynomial `f` of degree at most `n`, the Cauchy/Lagrange identity says

`(A_0 q)_i=f(-x_i)`.

Hence the degenerate kernel is parameterized by

`[p;q]=[(f(-x_i))_i ; (f(y_j))_j]`.

## 3. Exact all-m crossing form at t=0

Differentiate `H_t` at the Cauchy endpoint:

`H'_0(i,j) = -n/(x_i+y_j+a)`.

Restrict the derivative of the bipartite Laplacian to `ker(L_0)`.  For polynomials `f,g` of degree at most `n`, the crossing bilinear form is

`C_m(f,g)
 = -n sum_(i,j) w_i w_j
     [f(-x_i)-f(y_j)] [g(-x_i)-g(y_j)]
     /(x_i+y_j+a)`.

Constants are visibly in the kernel.  The point is that this form is nondegenerate modulo constants for **every** `m`.

### Finite-difference reduction lemma

Set

`N(X,Y)=[f(-X)-f(Y)][g(-X)-g(Y)]`.

Divide in `Q[X,Y]` by `X+Y+a`:

`N(X,Y)=(X+Y+a) R(X,Y)
         + [f(Y+a)-f(Y)][g(Y+a)-g(Y)]`.

Because `deg R <= 2n-1`, every monomial of `R` has either `X`-degree `<n` or `Y`-degree `<n`.  The two alternating binomial functionals

`Phi_x(F)=sum_i (-1)^i C(n,i) F(i+1)`,
`Phi_y(G)=sum_j (-1)^j C(n,j) G(mj)`

annihilate polynomials of degree `<n`.  Therefore the entire polynomial quotient term vanishes after applying `Phi_x Phi_y`.

Using the Cauchy finite-difference identity

`sum_(i=0)^n (-1)^i C(n,i)/(i+1+y+a)
 = n! / prod_(r=1)^m (y+a+r)`,

we obtain the exact one-dimensional reduction

`C_m(f,g)
 = -n sum_(j=0)^n w_j s_j
      delta_a f(y_j) delta_a g(y_j)`

where

`delta_a f(z)=f(z+a)-f(z)`,
`s_j=n! / P(y_j) > 0`,
`P(z)=prod_(r=1)^m (z+a+r)`.

The map

`delta_a : P_n / constants -> P_(n-1)`

is an isomorphism, because a nonconstant degree-`k` polynomial loses exactly one degree and its new leading coefficient is multiplied by `k*a != 0`.

## 4. Nondegeneracy and exact inertia

Let

`V(z)=prod_(j=0)^n (z-y_j)`,
`beta_j=1/V'(y_j)`.

For the arithmetic grid `y_j=mj`,

`w_j = (-1)^n m^n n! beta_j`.

Therefore the reduced form, up to one nonzero common scalar, is

`S(h,k)=sum_(j=0)^n beta_j h(y_j) k(y_j)/P(y_j)`

on `P_(n-1)`.

Suppose `S(h,k)=0` for every `k in P_(n-1)`.  Then the vector

`r_j=beta_j h(y_j)/P(y_j)`

annihilates the `n`-dimensional Vandermonde evaluation space of degrees `0,...,n-1`.  Its orthogonal complement is one-dimensional and is spanned by `(beta_j)`, so

`h(y_j)=c P(y_j)` for every `j`.

Consequently `h-cP` vanishes at all `m=n+1` nodes and

`h-cP=-c V`.

Thus

`h=c(P-V)`.

But the coefficient of `z^n=z^(m-1)` in `P-V` is

`m*a + m(m+1)/2 + m^2(m-1)/2
 = m(3m^2+1)/2 > 0`

because `a=m^2`.  Since `deg h<=n-1`, necessarily `c=0`, hence `h=0`.

Therefore:

**All-m local crossing theorem.**
For every `m>=2`, `C_m` has kernel exactly the constants.  Equivalently the derivative `Gamma'_0` has rank `m-1`.

The inertia is also explicit.  Before restricting to the degree-`<=n-1` evaluation hyperplane, the diagonal weights `w_j s_j` alternate signs.  The hyperplane is `beta^T z=0`.  Its diagonal-form orthogonal complement has squared sign equal to the sign of

`sum_j beta_j P(y_j) / [(-1)^n m^n (n!)^2]`.

The numerator is the `n`th divided difference of the monic degree-`n+1` polynomial `P` and equals

`m(3m^2+1)/2 > 0`.

Hence the restriction removes one sign `(-1)^n`.  Multiplying by the outer factor `-n`, the crossing form `C_m` has

`positive_index = floor((m-1)/2)`,
`negative_index = ceil((m-1)/2)`,
`nullity = 1` before quotienting constants,

or is nondegenerate with those positive/negative indices on the `(m-1)`-dimensional quotient.

This explains why ordinary positive-semidefinite contraction is the wrong geometry: the first AP-sensitive crossing is already genuinely indefinite for `m>=3`.

## 5. Exact vanishing order and strict local splitting

Because `Gamma_t` is rational/analytic at `t=0`, has the fixed kernel vector `s` for all `t`, and its quotient derivative is nondegenerate,

`Gamma_t|_(R^m/<s>) = t Gamma'_0|_(R^m/<s>) + O(t^2)`.

Therefore every quotient determinant representing the nontrivial fixed-space exclusion has exact first order

`ord_(t=0) det(I-Q_(m,t)) = m-1`.

In particular there exists `epsilon_m>0` such that

`det(I-Q_(m,t)) != 0` for `0<t<epsilon_m`.

Thus the AP Christoffel factor creates full transversal rank **immediately** away from the Cauchy endpoint for every admissible `m`.

This is an all-`m` theorem; finite checks are only regression.

## 6. First exact obstruction to globalizing the regular-crossing method

The natural next attempt is to require the instantaneous crossing form `Gamma'_(m,t)` itself to stay nondegenerate on the quotient for every `0<t<=1`.  That would permit a regular-crossing / pointwise inertia-flow globalization.

This condition is **false already for `m=3`**.

For `m=3`, delete the last row and column from `Gamma'_(3,t)`; because the fixed kernel vector `s=(1,-1,1)` has no zero coordinate, the resulting `2x2` determinant detects quotient nondegeneracy of `Gamma'_(3,t)`.

Exact elimination gives

`det( Gamma'_(3,t)[0:2,0:2] )
 = -27 P12(t) /
   [50 A(t)^2 B(t)^2 C(t)^2]`

with

`A(t)=5t^2-42t+420`,
`B(t)=728t^2-7315t+271700`,
`C(t)=2618t^2-23920t+391391`,

and

`P12(t)=
  18677859200 t^12
 -1030450862560 t^11
 +266836318177520 t^10
 -38119126605257040 t^9
 +2666960532445357740 t^8
 -114789507726989038041 t^7
 +2128778523707885528100 t^6
 -21386627649978696405300 t^5
 +141707915785000444930050 t^4
 -538717964929345743542000 t^3
 +1082281784621932214320000 t^2
 -1076281742427279287900000 t
 +410283992369849598000000`.

A rational Sturm certificate gives

- exactly one real root `t_*` of `P12` in `(0,1)`;
- exactly one root in the narrow rational bracket

`4991/5000 < t_* < 9983/10000`

i.e.

`0.9982 < t_* < 0.9983`.

Moreover `gcd(P12,N00)=1`, where `N00` is the numerator of the `(0,0)` entry of `Gamma'_(3,t)`.  Hence at `t=t_*` the derivative crossing form has quotient rank exactly `1`, not `0`.

So the regular-crossing condition fails at a unique algebraic parameter very close to the AP endpoint.

### This is not an AP counterexample

For the same `m=3`, the actual quotient determinant factors as

`det(I-Q_(3,t))
 = 1135134 t^2 A2(t) B6(t) / D(t)`

where

`A2(t)=1413754 t^2-36819435 t+12206367030`,

`B6(t)=11760 t^6-15974170 t^5+976346833 t^4
       -10512282495 t^3+40314445885 t^2
       -72293202550 t+55117062000`,

and `D(t)` is the product of the six positive normalizer quadratics

`(5t^2-42t+420)
 (11t^2-133t+14630)
 (455t^2-4048t+46046)
 (728t^2-7315t+271700)
 (952t^2-6825t+33150)
 (2618t^2-23920t+391391)`.

Exact Sturm counts give no root of `A2` or `B6` in `(0,1)`, and

`gcd(P12,A2*B6)=1`.

Therefore `t_*` is a failure of the **derivative invariant**, not a fixed-eigenvalue recrossing.  The actual `m=3` quotient remains nonsingular there.

## 7. Research interpretation

This execution separates the deformation problem into two rigorously different layers:

1. **Local rank creation is solved all-m.**  
   The AP factor contributes a first-order signed Christoffel crossing whose quotient form is nondegenerate for every `m`; the exact quotient determinant vanishing order is `m-1`.

2. **Naive differential continuation is refuted.**  
   The idea “prove `Gamma'_t` never degenerates, then carry the inertia from `0` to `1`” fails at a unique algebraic `m=3` parameter before the AP endpoint.

3. **The true unresolved residue is global and nonlinear in t.**  
   A successful successor must control `Gamma_t` itself (or its `(m-1)` compound / quotient determinant) through derivative singularities.  It cannot rely only on pointwise regularity of the crossing form.

The most promising successor targets are therefore:
- a direct sign/nonzero formula for the quotient compound of `Gamma_t`;
- a signed matrix-tree / bipartite-Laplacian certificate that tolerates singular `Gamma'_t`;
- a higher-order spectral-flow treatment of the isolated derivative degeneracy;
- the separately published GSTP exterior-cone route, if its representation can be completed.

## 8. External prior-art boundary

A targeted external scan located the classical Cauchy-biorthogonal / Christoffel literature, including:

- M. Bertola, M. Gekhtman, J. Szmigielski, **Cauchy biorthogonal polynomials**, *Journal of Approximation Theory* 162 (2010), 832–867, DOI `10.1016/j.jat.2009.09.008`.
- General Christoffel/Geronimus transformation literature for biorthogonal systems.

Those sources support the classical status of Cauchy kernels, biorthogonality, total positivity, Christoffel transformations, and Christoffel–Darboux machinery.  This execution does not claim novelty for those ingredients.  No located source directly supplies the task-specific signed normalized operator identity or the all-`m` crossing/nondegeneracy theorem proved above.

## 9. Verification

Exact deterministic checker:

`research_checks/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_CHECK_20260830.py`

Certificate:

`research_artifacts/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION/exact_local_crossing_and_m3_obstruction_certificate.json`

The checker uses only Python standard-library exact rational arithmetic.  It:

- verifies the two-dimensional-to-one-dimensional crossing reduction directly for `m=2..7`;
- verifies nonzero crossing determinants and the predicted determinant sign pattern;
- reconstructs the exact `m=3` derivative cofactor at 13 rational interpolation points, sufficient for the frozen degree-12 numerator identity;
- performs an exact Sturm root count showing one and only one `P12` root in `(0,1)` and in the stated rational bracket;
- verifies coprimality with the `m=3` quotient-determinant numerator and zero roots of its two nontrivial numerator factors in `(0,1)`.

Finite checks are regression/certification only; the all-`m` local theorem and inertia classification are proved symbolically in this return.

## 10. Terminal scope

Hard-target disposition:

`AP_CHRISTOFFEL_ALL_M_LOCAL_J_TRANSVERSALITY_PROVED_AND_POINTWISE_CROSSING_FORM_GLOBALIZATION_EXACTLY_OBSTRUCTED_AT_M3`.

Unresolved residue:

`ALL_M_GLOBAL_NO_RECROSSING_OF_Gamma_t / det(I-Q_(m,t)) ON (0,1]`.

No Foundation / Working-Truth / parent all-`m` cofactor theorem promotion is claimed.
