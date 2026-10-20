# Perfect Prime Beta-Bernstein Principal-Angle / Exterior-Power Closure - Research Return

Researcher-ID: `EM-PPTBBPA-6E863B`
Task: `RS-PERFECT-PRIME-BETA-BERNSTEIN-PRINCIPAL-ANGLE-EXTERIOR-POWER`
Publication: `TP2-10717029BFD72A8E1F76`
Claim: `chatgpt-pptbbpa-20260830-1057-6e863b`
Execution record: `ER-4E41ADAD5023F187ED93`

## Terminal verdict

`SUCCESS / STRICT_TRANSVERSALITY_REDUCTION_PROVED`

The parent all-m theorem is not proved here. The target `det(I-Q_m) != 0` remains open.

## Exact all-m reduction

Put `n=m-1`, `h_m(q)=1/prod_{ell=0}^n(1+q+ell*m^2)`, `H_ij=h_m(i+m*j)`, `w_i=(-1)^i*C(n,i)`, and `W=diag(w_i)`. The accepted parent result has positive normalizers `e_i=sum_j H_ij*w_j` and `d_j=sum_i w_i*H_ij`, with `E=diag(e_i)`, `D=diag(d_j)`, `A=E^-1 H W`, `B=D^-1 H^T W`, and `K=BA`. Also `A*1=B*1=1`.

The common positive measure is `dmu_m(u)=kappa_m*(1-u^(m^2))^n du`, with `kappa_m=1/(n!*m^(2n))`, so `H_ij=int_0^1 u^(i+m*j) dmu_m(u)`.

Write `lambda_i=C(n,i)`, `Lambda=diag(lambda_i)`, `J=diag((-1)^i)`, so `W=J*Lambda=Lambda*J`. Define positive diagonal metrics `P=E*Lambda`, `Q=D*Lambda`, and strip the alternating signature by `X=A*J=E^-1 H Lambda`, `Y=B*J=D^-1 H^T Lambda`.

Then exactly

`Q*Y = Lambda*H^T*Lambda = X^T*P`.

Thus X and Y are adjoints for positive diagonal Hilbert metrics. Put `Z=P^(1/2)*X*Q^(-1/2)`. Then

`Z_ij = H_ij*sqrt(lambda_i*lambda_j/(e_i*d_j))`,

so Z is an exact positive cross-Gram matrix in the common `L^2(mu_m)` space, and it inherits STP from H by positive row/column scaling.

However the frozen operator is not the ordinary Hilbert Gram square. It is

`K = Y*J*X*J`,

hence

`Q^(1/2)*K*Q^(-1/2) = Z^T*J*Z*J`.

Equivalently, without square roots,

`D*W*K = A^T*E*W*A`,

so `K^T*(D*W)=(D*W)*K`. Therefore the correct geometry is signature/Krein geometry, not an ordinary positive principal-angle problem.

Let `v=Q^(1/2)*1`. The known fixed direction satisfies `Z^T*J*Z*J*v=v`, and its signed norm is positive:

`v^T*J*v = w^T*H*w = int_0^1 (1-u)^n*(1-u^m)^n dmu_m(u) > 0`.

Define the symmetric J-Gram defect

`Delta_m := J - Z^T*J*Z`.

Then `Z^T*J*Z*J*y=y` iff `Delta_m*(J*y)=0`. Consequently the desired fixed-point uniqueness is equivalent to

`ker(Delta_m)=span{J*v}`,

or equivalently `rank(Delta_m)=m-1`. This is the exact surviving exterior-power/transversality target.

## Exact actual-measure principal-angle mismatch

Let `V_m=span{1,u,...,u^n}` and `W_m=span{1,u^m,...,u^(m*n)}` in the actual `L^2(mu_m)` space. With `G_V(i,j)=h_m(i+j)` and `G_W(i,j)=h_m(m*(i+j))`, the ordinary squared-principal-angle operator is `C_m=G_W^-1 H^T G_V^-1 H`.

At `m=2`, exact rational arithmetic gives

`spec(K_2)={1,529/1540}`,

while

`spec(C_2)={1,18515/19968}`.

Therefore ordinary principal angles do not encode the nontrivial K spectrum even for the actual AP measure. Any successful Hilbert-space proof must use the Möbius signature/oblique normalization.

## All-m adversarial control: unweighted Cauchy model

Remove only the AP polynomial weight by taking `dmu_0(u)=du`, while retaining m, the two exponent sets, the map `u -> u^m`, the Möbius weights, and the definitions of e,d,A,B,K. Then

`H0_ij = 1/(1+i+m*j) = 1/(x_i+y_j)`

with `x_i=1+i`, `y_j=m*j`, a Cauchy matrix.

The finite-difference identity

`sum_{j=0}^n (-1)^j*C(n,j)/(a+m*j) = n!*m^n/prod_{r=0}^n(a+m*r)`

gives exact positive normalizers. The resulting `A0` is the Lagrange evaluation map from the y-grid to the `-x` grid, and `B0` is its inverse evaluation map. Hence analytically, for every `m>=2`,

`B0*A0 = I_m`,

so

`K0_m = I_m`.

Yet the two subspaces still satisfy `V_m intersect W_m = span{1}`, and the positive Cauchy/STP architecture survives. Therefore common positive measure + STP + the map `u -> u^m` + one-dimensional subspace intersection are insufficient for fixed-point uniqueness. In J form the Cauchy endpoint has `Z0^T*J*Z0=J`, hence `Delta0_m=0`: it is a full J-isometry.

## Exact AP deformation

The actual factor is `rho_m(u)=(1-u^(m^2))^n`. Expanding it gives

`int_0^1 u^q*rho_m(u) du = sum_{ell=0}^n (-1)^ell*C(n,ell)/(q+1+m^2*ell)`

`= n!*(m^2)^n/prod_{ell=0}^n(q+1+m^2*ell)`.

After multiplying by `kappa_m`, this is exactly `h_m(q)`. Thus the actual AP moment kernel is the normalized n-th finite difference, with step `m^2`, of one-pole Cauchy kernels.

This isolates the only ingredient removed in the maximally degenerate all-m control. Any future proof that uses `rho_m` only through positivity is therefore ruled out.

## Surviving all-m lemma

The next load-bearing statement is the AP Christoffel J-transversality lemma:

`rank(Delta_m)=m-1`, equivalently `ker(Delta_m)=span{J*v}`.

In exterior-power language, after removing the known direction, the `(m-1)`-compound must be nonzero. Rank creation must come from the exact AP polynomial/finite-difference deformation, not from generic STP, ordinary principal angles, or common-measure geometry alone.

A natural exact deformation for a subsequent execution is `rho_{m,t}(u)=(1-t*u^(m^2))^n`, `0<=t<=1`, with `t=0` the solved endpoint `K=I` and `t=1` the AP target. A no-zero, inertia-flow, or compound-minor theorem along this exact path would attack the remaining obstruction. No such monotonicity theorem is claimed here.

## Verification

Exact checker:
`research_checks/PERFECT_PRIME_BETA_BERNSTEIN_PRINCIPAL_ANGLE_EXTERIOR_POWER_CHECK_20260830.py`

Certificate:
`research_artifacts/PERFECT_PRIME_BETA_BERNSTEIN_PRINCIPAL_ANGLE_EXTERIOR_POWER/exact_regression_certificate.json`

The checker uses `fractions.Fraction`. Actual AP regression is checked through `m=6`; the Cauchy baseline through `m=8`. It replays the finite-difference identity, positive-metric adjointization, J-self-adjoint identity, distinguished fixed vector, finite quotient determinants, the exact `m=2` principal-angle mismatch, and the Cauchy interpolation identity. Bounded checks are regression only; the statements above labelled all-m are proved symbolically here.

## Prior-art and scope firewall

Cauchy matrices, Lagrange interpolation, total positivity, biorthogonality, Christoffel-type polynomial modification, and Krein/J-space terminology are classical. A relevant reference is Bertola-Gekhtman-Szmigielski, "Cauchy biorthogonal polynomials", Journal of Approximation Theory 162 (2010), 832-867, DOI `10.1016/j.jat.2009.09.008`.

No novelty is claimed for those classical ingredients. The task-local contribution is their exact placement around the frozen AP operator, the all-m Cauchy adversarial control `K0=I`, the actual-measure principal-angle mismatch, and isolation of the AP polynomial factor as the only surviving transversality source.

Method-harvest disposition: `RESULT_ONLY`.

This return does not prove `det(I-Q_m)!=0` for every m, a global `(0,1)` spectral theorem, an all-m inertia law for Delta, or any Foundation/Working-Truth status.
