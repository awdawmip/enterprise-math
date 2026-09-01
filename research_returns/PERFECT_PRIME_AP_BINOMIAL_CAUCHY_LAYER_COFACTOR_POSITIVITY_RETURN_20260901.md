# Perfect Prime AP binomial Cauchy-layer cofactor positivity - Research Return

Researcher-ID: `EM-PPTAPBCP1-646AAA`
Task: `RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY`
Publication: `TP2-5A3E91C7D2B40F681AC3`
Claim: `chatgpt-pptabcp1-20260901-0907-r2`
Execution record: `ER-5061202400CCD679FFE6`

## Terminal verdict

`NEGATIVE_BOUNDARY / EXACT_FULL_MULTILAYER_COVARIANCE_REDUCTION / INNER_POSITIVITY_MECHANISM_OBSTRUCTED / PARENT_NONVANISHING_OPEN`

The taskbook permits terminalization either by proving the all-m nonvanishing theorem or by exactly obstructing a declared positivity mechanism while preserving the parent theorem as open. This return takes the second route.

It does NOT prove or refute

`tau_m(t) != 0` for every `m>=2`, `0<t<=1`.

It proves an exact all-m reduction of the complete multilayer cofactor to one `(m-1)x(m-1)` outer determinant and proves that the direct inner conditional-variance / termwise Andreief positivity mechanism is impossible: for every `m>=3`, every inner conditional-covariance block is indefinite. Finite exact arithmetic extends the residual Mobius/Bernstein coefficient-positivity pattern through `m=10`, but that is regression only.

## 1. Frozen model and adjacent-layer theorem

Set

`n=m-1`, `b=m^2`, `x_i=i+1`, `y_j=m*j`,
`w_i=(-1)^i binom(n,i)`, `W=diag(w)`.

The frozen AP moment matrix is

`H_t(i,j) = integral_0^1 u^(i+m*j) (1-t*u^b)^n du
          = sum_(s=0)^n (-1)^s binom(n,s) t^s /(x_i+y_j+b*s)`.

Let `e=H_t w`, `d=H_t^T w`, `E=diag(e)`, `D=diag(d)`, and

`L_t = [[W E, -W H_t W],[-W H_t^T W, W D]]`.

Its all-ones bipartite vector is the gauge kernel. The canonical scalar is

`tau_m(t)=det L_t[hat(2m),hat(2m)]`.

The accepted layer decomposition remains

`L_t=sum_(s=0)^n (-1)^s binom(n,s)t^s M_s`.

The accepted adjacent-layer theorem is reproduced unchanged: `M_s-theta M_(s+1)` has only the gauge kernel on `0<theta<=1`; its unique possible nongauge singular parameter is

`theta_s^* = (((m^2+1)/2)+b(s+1))/(((m^2+1)/2)+b*s) > 1`.

No full-multilayer conclusion is inferred from that pairwise theorem.

## 2. Full multilayer one-dimensional residue

For polynomials `g,f,h,k` of degree at most `n`, represent the bipartite vectors by

`p_i=g(-x_i)`, `q_j=f(y_j)`.

The frozen Cauchy-layer residue is

`B_s((g,f),(h,k))
 = sum_j w_j c_s(y_j)
   [g(y_j+b*s)-f(y_j)]
   [h(y_j+b*s)-k(y_j)]`

with

`c_s(y)=n!/prod_(r=1)^m(y+b*s+r)
       =integral_0^1 u^(y+b*s)(1-u)^n du > 0`.

For the complete AP superposition define

`z_(j,s)=y_j+b*s`,
`lambda_(j,s)(t)=(-1)^s binom(n,s)t^s c_s(y_j)`,
`Dcal_j(t)=sum_s lambda_(j,s)(t)`.

Then exactly

`Dcal_j(t)=integral_0^1 u^y_j (1-u)^n (1-t*u^b)^n du > 0`

for `0<=t<=1`, and

`B_t = sum_j w_j sum_s lambda_(j,s)
       [g(z_(j,s))-f(y_j)]
       [h(z_(j,s))-k(y_j)]`.

Thus every layer, including all three-or-more-layer interference, is present.

## 3. Exact conditional-covariance completion

Define

`mu_j(g) = (sum_s lambda_(j,s) g(z_(j,s)))/Dcal_j`

and

`Ccal_j(g,h)
 = sum_s lambda_(j,s)g(z_(j,s))h(z_(j,s))
   -(sum_s lambda_(j,s)g(z_(j,s)))
    (sum_s lambda_(j,s)h(z_(j,s)))/Dcal_j`.

Completing the square gives

`B_t((g,f),(h,k))
 = sum_j w_j Dcal_j [f(y_j)-mu_j(g)][k(y_j)-mu_j(h)]
   + Scal_t(g,h)`

where

`Scal_t(g,h)=sum_j w_j Ccal_j(g,h)`.

Evaluation `f -> (f(y_0),...,f(y_n))` is an isomorphism on degree-<=n polynomials, so the right-variable block is exactly diagonalizable. All remaining multilayer singularity is concentrated in `Scal_t` on left polynomials modulo constants.

In the quotient monomial basis `X,X^2,...,X^n`, define

`C_j(t)[r,q]
 = sum_s lambda_(j,s) z_(j,s)^(r+q)
   -(sum_s lambda_(j,s) z_(j,s)^r)
    (sum_s lambda_(j,s) z_(j,s)^q)/Dcal_j`,
for `1<=r,q<=n`, and set

`S_m(t)=sum_j w_j C_j(t)`.

## 4. Exact full-cofactor reduction

Let `V_x` map monomial coefficients of `g` to `(g(-1),g(-2),...,g(-m))`. Then

`abs(det V_x)=prod_(k=1)^n k!`.

The polynomial-coordinate change and the square-completion change are invertible. In completed coordinates the full Gram matrix is congruent to

`S_m^full(t) direct_sum diag(w_0 Dcal_0,...,w_n Dcal_n)`,

where the constant polynomial is the gauge kernel of `S_m^full` and the nonconstant principal block is `S_m(t)`.

Using adjugate congruence for the zero-row-sum Laplacian gives the exact identity

`tau_m(t)
 = [prod_(j=0)^n (w_j Dcal_j(t))] det S_m(t)
   / [prod_(k=1)^n k!]^2`.

This identity also holds at lower rank, when both sides vanish. Since `Dcal_j(t)>0` on `0<=t<=1` and every `w_j` is nonzero,

`tau_m(t) != 0  <=>  det S_m(t) != 0` for `0<t<=1`.

Therefore the original `(2m-1)x(2m-1)` canonical cofactor is reduced exactly to one `(m-1)x(m-1)` outer alternating covariance determinant.

## 5. All-m determinant and inertia of every inner block

Fix `m,j` and `t>0`. Put

`Lambda_j=diag(lambda_(j,0),...,lambda_(j,n))`,
`lambda_j=(lambda_(j,0),...,lambda_(j,n))^T`,
`A_j=Lambda_j-lambda_j lambda_j^T/Dcal_j`.

Then `A_j*1=0`, and `C_j` is its pullback by the nonconstant Vandermonde evaluation map.

For any deleted coordinate, the matrix determinant lemma gives

`det A_j[hat(k),hat(k)] = prod_s lambda_(j,s)/Dcal_j`.

Let

`Delta_j=prod_(0<=r<s<=n)(z_(j,s)-z_(j,r))`.

Adjugate congruence by the full Vandermonde matrix yields

`det C_j(t) = Delta_j^2 prod_s lambda_(j,s)(t)/Dcal_j(t)`.

Hence

`sign det C_j = (-1)^(n(n+1)/2)`.

More strongly, let
`e=# even s in {0,...,n}=floor(n/2)+1`,
`o=# odd s in {0,...,n}=ceil(n/2)`.

The diagonal `Lambda_j` has inertia `(e,o,0)`. Consider

`G_j=[[Dcal_j,lambda_j^T],[lambda_j,Lambda_j]]`.

Its quadratic form equals

`sum_s lambda_(j,s)(r+x_s)^2`.

The invertible change `y_s=r+x_s` shows `In(G_j)=(e,o,1)`. Since `Dcal_j>0`, Schur-complement inertia additivity gives

`In(A_j)=(e-1,o,1)`.

The zero direction is exactly the constant vector. Therefore on nonconstant polynomial coefficients,

`In(C_j)=(floor(n/2),ceil(n/2),0)`.

Consequences:

- for `m=2`, every inner block is strictly negative;
- for every `m>=3`, every inner block is indefinite;
- this is true for every `j` and every `0<t<=1`.

Thus direct conditional-variance positivity, termwise positive inner Andreief, or any proof requiring each `C_j` to be positive/negative definite is exactly obstructed.

Smallest explicit witness: for `m=3,j=0,t=1`,

`C_0 = (1/16120)*[[-2673,-12231],[-12231,102303]]`

and

`det C_0 = -6561/4030 < 0`.

## 6. Forced order at the first Cauchy endpoint

At `t=0` only `s=0` survives, so every `C_j(0)=0`. Differentiation gives

`d/dt Ccal_j(g,h)|_(t=0)
 = -n c_1(y_j)
   [g(y_j+b)-g(y_j)]
   [h(y_j+b)-h(y_j)]`.

Therefore

`S_m(t)=t S_m^(1)+O(t^2)`,

where `S_m^(1)` is the accepted quotient Christoffel crossing form. The already accepted all-m crossing theorem says this form is nondegenerate modulo constants. Hence

`det S_m(t)=t^n det S_m^(1)+O(t^(n+1))`, with `det S_m^(1)!=0`.

The reduction in Section 4 therefore reproduces

`ord_(t=0) tau_m(t)=n=m-1`.

## 7. Second Cauchy endpoint and finite Mobius/Bernstein evidence

Set `x=t/(1-t)`, so `t=x/(1+x)`, and define

`Htilde_x=(1+x)^n H_(x/(1+x))`.

Then

`Htilde_x(i,j)
 = integral_0^1 u^(i+m*j)[1+x(1-u^b)]^n du`.

Every entry is a polynomial in `x` with strictly positive coefficients.

Because `L` is linear in `H`,
`Ltilde_x=(1+x)^n L_(x/(1+x))`.

The terminal Cauchy layer `M_n` has the same nondegenerate adjacent-layer local splitting as the initial endpoint (apply the same finite-difference argument to the backward translation). Thus the reversed cofactor loses exactly `n` top degrees. Consequently

`deg tau_m=2n^2`.

Writing

`tau_m(t)=t^n q_m(t)`,
`deg q_m=n(2m-3)`,

and

`Bhat_m(x)=(1+x)^(n(2m-3)) q_m(x/(1+x))`

gives the exact two-endpoint factorization

`det Ltilde_x[hat(2m),hat(2m)] = x^n (1+x)^n Bhat_m(x)`.

The exact checker verifies that every coefficient of `Bhat_m` is strictly positive for `2<=m<=10`. This is finite evidence only, not an all-m proof.

## 8. Exact unresolved residue

The task terminates here at the permitted mechanism-obstruction boundary.

The parent theorem is now equivalent to the single statement

`det S_m(t) != 0` for every `m>=2`, `0<t<=1`.

Finite exact data suggest the sharper inertia pattern

`In(S_m(t))=(floor((m-1)/2),ceil((m-1)/2),0)`

and the alternative all-m target

`all coefficients of Bhat_m(x) are positive`.

Neither is claimed. Using the observed fixed inertia as a proof would be circular, because preventing an inertia change already requires proving `det S_m(t)!=0`.

The existing GSTP route does not close this residue: the actual AP quotient already has a non-real conjugate pair at `m=10`, while the cofactor remains positive in the finite regression.

## 9. Verification and scope

The paired standard-library checker uses exact `fractions.Fraction` arithmetic. It verifies:

- finite adjacent-layer root regressions;
- direct `tau_m` equals the outer-covariance formula for `m=2..6` at `t=1/2,1`;
- the inner determinant formula and `Dcal_j>0` in those checks;
- the exact `m=3` indefinite witness;
- nonzero first-order outer determinants for `m=2..7`;
- Mobius/Bernstein residual coefficient positivity through `m<=8` by default and `m<=10` with `--extended`.

Finite checks are regression/discovery only. The all-m claims above are the symbolic covariance reduction, inner determinant/inertia theorem, and forced first-endpoint order.

No Working Truth, Foundation, L4, novelty, or parent-objective closure is claimed.

`method_harvest = RESULT_ONLY`.

Recommended next theorem interface:
`OUTER_BINOMIAL_CONDITIONAL_COVARIANCE_DETERMINANT_NONVANISHING_OR_RESIDUAL_BERNSTEIN_POSITIVITY`.
