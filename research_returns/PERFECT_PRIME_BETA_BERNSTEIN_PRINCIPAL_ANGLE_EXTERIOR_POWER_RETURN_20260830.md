# Perfect Prime Beta–Bernstein Principal-Angle / Exterior-Power Closure — Research Return

Researcher-ID: `EM-PPTBBPA-6E863B`
Task: `RS-PERFECT-PRIME-BETA-BERNSTEIN-PRINCIPAL-ANGLE-EXTERIOR-POWER`
Publication: `TP2-10717029BFD72A8E1F76`
Claim: `chatgpt-pptbbpa-20260830-1057-6e863b`
Execution record: `ER-4E41ADAD5023F187ED93`

## 1. Terminal verdict

`SUCCESS / STRICT_TRANSVERSALITY_REDUCTION_PROVED`

The parent theorem is not proved here. The all-m target `det(I_(m-1) - Q_m) ≠ 0` remains open.

This execution strictly narrows the geometric route:

1. After removing the alternating Möbius signature, the two Beta–Bernstein half maps are adjoints for positive diagonal Hilbert metrics and yield an exact positive cross-Gram matrix Z.
2. The frozen operator is not the ordinary Hilbert Gram square `ZᵀZ`; it is the signature-twisted operator `ZᵀJZJ`.
3. In the actual AP measure, already at m=2, the nontrivial eigenvalue of K differs exactly from the ordinary squared principal angle between the two monomial/Bernstein subspaces.
4. If only the AP polynomial weight is removed, while retaining the same subspaces, order map, Möbius weights, common positive-measure architecture and Cauchy/STP structure, then `K_m^(0) = I_m` for every m ≥ 2.
5. Therefore the specific factor `ρ_m(u) = (1-u^(m²))^(m-1)` is the indispensable source of transversality. The surviving all-m lemma is an AP Christoffel / finite-difference J-transversality statement.

No Working Truth, Foundation status, novelty, or canonical promotion is claimed.

## 2. Frozen operator and common measure

Put `n=m-1` and

`h_m(q) = 1 / ∏_(ℓ=0)^n (1+q+ℓm²)`,

`H_ij = h_m(i+mj)`,

`w_i = (-1)^i C(n,i)` and `W = diag(w_i)`.

The accepted parent result defines positive normalizers

`e_i = Σ_j H_ij w_j > 0`,
`d_j = Σ_i w_i H_ij > 0`,

with `E=diag(e_i)`, `D=diag(d_j)`, and

`A = E⁻¹ H W`,
`B = D⁻¹ Hᵀ W`,
`K = BA`.

Also `A1=B1=1` and hence `K1=1`.

The common positive measure is

`dμ_m(u) = κ_m (1-u^(m²))^n du`,
`κ_m = 1 / (n! m^(2n))`,

for which

`H_ij = ∫_0^1 u^(i+mj) dμ_m(u)`.

Let `R_jk=(-1)^k C(j,k)` for k≤j. Then `R²=I`, and the accepted quotient representation is

`T_m = RKR = [[1,*],[0,Q_m]]`.

## 3. Exact positive-metric adjointization and the J obstruction

Write

`λ_i=C(n,i)`,
`Λ=diag(λ_i)`,
`J=diag((-1)^i)`,

so `W=JΛ=ΛJ`.

Define positive metrics

`P=EΛ`,
`Q=DΛ`,

and strip the alternating signature:

`X := AJ = E⁻¹HΛ`,
`Y := BJ = D⁻¹HᵀΛ`.

Then exactly

`QY = ΛHᵀΛ = XᵀP`.

Thus X and Y are adjoints for positive diagonal Hilbert metrics.

Put

`Z = P^(1/2) X Q^(-1/2)`.

Its entries are

`Z_ij = H_ij sqrt(λ_i λ_j / (e_i d_j))`.

Equivalently, with

`φ_i(u)=sqrt(λ_i/e_i) u^i`,
`ψ_j(u)=sqrt(λ_j/d_j) u^(mj)`,

we have

`Z_ij = <φ_i,ψ_j>_(L²(μ_m))`.

Hence Z is a genuine positive common-Hilbert-space cross-Gram matrix. It is also a positive row/column scaling of H, so the accepted STP property of H passes to Z.

But the frozen operator is

`K = (YJ)(XJ) = YJXJ`,

therefore

`Q^(1/2) K Q^(-1/2) = Zᵀ J Z J`.

This is the exact obstruction to the naive principal-angle route: ordinary principal angles would produce a positive Gram square such as `ZᵀZ`, whereas the Möbius orientation inserts two signature matrices J before composition.

A square-root-free form is

`DWK = AᵀEWA`,

so

`Kᵀ(DW) = (DW)K`.

Thus K is self-adjoint for the nondegenerate signed form `DW=JQ`. The correct geometry is Krein/J geometry, not ordinary Hilbert self-adjointness.

## 4. Distinguished positive-type fixed direction and exact defect matrix

Let

`u=P^(1/2)1`,
`v=Q^(1/2)1`.

From `A1=B1=1` and `A=XJ`, `B=YJ`,

`ZJv=u`,
`ZᵀJu=v`.

Hence

`ZᵀJZJv=v`.

The J-norm of v is positive:

`vᵀJv = Σ_j d_j w_j = wᵀHw
       = ∫_0^1 (1-u)^n(1-u^m)^n dμ_m(u) > 0`.

Define the symmetric J-Gram defect

`Δ_m := J - ZᵀJZ`.

Then for any y,

`ZᵀJZJy=y` iff `Δ_m(Jy)=0`.

Therefore the parent fixed-point uniqueness target is equivalent to

`ker(Δ_m) = span{Jv}`,

or equivalently

`rank(Δ_m)=m-1`.

The corresponding exterior-power witness is

`∧^(m-1) Δ_m ≠ 0`.

This is the exact surviving transversality object.

## 5. Exact counterexample to ordinary principal-angle identification

Inside the actual Hilbert space `L²(μ_m)`, let

`V_m = span{1,u,...,u^n}`,
`W_m = span{1,u^m,...,u^(mn)}`.

Their Gram matrices are

`(G_V)_ij = h_m(i+j)`,
`(G_W)_ij = h_m(m(i+j))`,

and the cross Gram is H.

The standard squared-principal-angle / canonical-correlation operator is

`C_m = G_W⁻¹ Hᵀ G_V⁻¹ H`.

At m=2, exact rational arithmetic gives

`spec(K_2) = {1, 529/1540}`,

whereas

`spec(C_2) = {1, 18515/19968}`.

Since `529/1540 ≠ 18515/19968`, the ordinary principal-angle spectrum does not encode the nontrivial K spectrum even for the actual AP measure.

So a successful Hilbert-space proof, if one exists, must incorporate the Möbius signature / oblique normalization; it cannot identify K with a product of ordinary orthogonal projections.

## 6. All-m adversarial control: the unweighted Cauchy model has K=I

Now change only the AP weight, taking `dμ_0(u)=du`. Retain m, n, the exponent sets, the map `u→u^m`, the Möbius weights, and the definitions of e,d,A,B,K.

Then

`H^(0)_ij = ∫_0^1 u^(i+mj)du = 1/(1+i+mj)`.

Set `x_i=1+i` and `y_j=mj`, so `H^(0)_ij=1/(x_i+y_j)`, a Cauchy matrix.

The finite-difference identity

`Σ_(j=0)^n (-1)^j C(n,j)/(a+mj)
 = n! m^n / ∏_(r=0)^n (a+mr)`

gives

`e_i^(0) = n! m^n / ∏_(r=0)^n (x_i+mr)`,

and similarly

`d_j^(0) = n! / ∏_(r=0)^n (y_j+1+r)`.

Both are positive.

Let `L_j(t)` be the Lagrange basis for the nodes `y_0,...,y_n`. Direct substitution gives

`A^(0)_ij = L_j(-x_i)`.

Thus A^(0) takes values of a polynomial of degree at most n on the y-grid and evaluates it at the -x-grid.

Let `N_i(t)` be the Lagrange basis for the nodes `-x_0,...,-x_n`. Similarly,

`B^(0)_ji = N_i(y_j)`.

So B^(0) performs the inverse interpolation/evaluation map. Hence, for every m≥2,

`B^(0) A^(0) = I_m`,

and therefore

`K_m^(0) = I_m`.

This is an analytic all-m theorem, not a finite-m inference.

Yet `V_m ∩ W_m = span{1}` still holds, because the only common exponent between `{0,...,m-1}` and `{0,m,...,m(m-1)}` is 0. The same positive-measure and Cauchy/STP architecture also survives.

Therefore the package

`COMMON POSITIVE MEASURE + TWO BERNSTEIN/MONOMIAL FLAGS + u→u^m + STP + ONE-DIMENSIONAL SUBSPACE INTERSECTION`

is insufficient for fixed-point uniqueness.

In J-form the same control gives

`(Z_m^(0))ᵀ J Z_m^(0) = J`,

so

`Δ_m^(0)=0`.

The unweighted endpoint is a full J-isometry, with every direction fixed.

## 7. The AP matrix is the exact finite-difference / Christoffel deformation of that control

The actual AP factor is

`ρ_m(u)=(1-u^(m²))^n`.

Expanding,

`ρ_m(u)=Σ_(ℓ=0)^n (-1)^ℓ C(n,ℓ) u^(m²ℓ)`.

For every integer q≥0,

`∫_0^1 u^q ρ_m(u)du
 = Σ_(ℓ=0)^n (-1)^ℓ C(n,ℓ)/(q+1+m²ℓ)
 = n!(m²)^n / ∏_(ℓ=0)^n(q+1+m²ℓ)`.

Multiplying by `κ_m=1/(n!m^(2n))` gives exactly h_m(q).

Thus the actual AP moment matrix is a normalized nth finite difference, with step m², of one-pole Cauchy kernels.

This isolates the only ingredient removed in the all-m degenerate control.

## 8. Strict surviving lemma

For the actual normalized cross-Gram matrix Z_m, define

`Δ_m = J - Z_mᵀJZ_m`.

The Cauchy endpoint has `Δ_m^(0)=0`. The actual AP model has the known positive-type kernel direction `Jv_m`.

The original quotient theorem will follow if one proves the AP Christoffel J-transversality statement

`rank(Δ_m)=m-1`,

equivalently

`ker(Δ_m)=span{Jv_m}`,

equivalently the `(m-1)`st exterior compound is nonzero after removing the known direction.

The gain is falsifiable and strict:

- the zero-deformation endpoint is solved exactly and is maximally degenerate;
- generic common-measure/STP/intersection/principal-angle information survives at that endpoint and is therefore insufficient;
- rank creation can only come from the exact AP polynomial factor `ρ_m`;
- the correct defect is the indefinite J-Gram defect, not an ordinary positive projection defect.

Any future proof that uses `ρ_m` only through positivity is ruled out by the all-m Cauchy control.

## 9. Exact regression certificate

Checker:

`research_checks/PERFECT_PRIME_BETA_BERNSTEIN_PRINCIPAL_ANGLE_EXTERIOR_POWER_CHECK_20260830.py`

Certificate:

`research_artifacts/PERFECT_PRIME_BETA_BERNSTEIN_PRINCIPAL_ANGLE_EXTERIOR_POWER/exact_regression_certificate.json`

Exact `fractions.Fraction` regression was run with actual AP matrices through m=6 and the Cauchy baseline through m=8.

It verifies:

1. the AP finite-difference moment identity;
2. `QY=XᵀP`, `K=YJXJ`, and `DWK=AᵀEWA`;
3. the fixed vector and positive J-norm;
4. finite regression `rank(I-K)=m-1` and `det(I-Q_m)≠0` for m=2,...,6;
5. the exact m=2 ordinary-principal-angle mismatch;
6. the exact Cauchy normalizers, both Lagrange maps, and `B^(0)A^(0)=I` through m=8.

The bounded checks are regression only. The all-m statements are the symbolic derivations above.

## 10. Prior-art / duplication firewall

Cauchy matrices, barycentric/Lagrange interpolation, total positivity, biorthogonality, Christoffel-type polynomial modifications, and Krein/J-space terminology are classical.

A relevant reference is:

Bertola, Gekhtman, Szmigielski, “Cauchy biorthogonal polynomials”, Journal of Approximation Theory 162 (2010), 832–867, DOI `10.1016/j.jat.2009.09.008`.

No novelty is claimed for those classical ingredients.

The task-local contribution is their exact placement around the frozen AP operator, the all-m Cauchy adversarial control `K^(0)=I`, the actual-measure principal-angle mismatch, and the isolation of the AP polynomial factor as the only surviving transversality source.

Method-harvest disposition: `RESULT_ONLY`.

## 11. What is not proved

This return does not establish:

- `det(I-Q_m)≠0` for every m;
- that all nontrivial eigenvalues of K lie in (0,1) for every m;
- a fixed inertia pattern for Δ_m;
- novelty of the classical Cauchy/Krein/Christoffel ingredients;
- Working Truth, Foundation, L4, or canonical status.

It establishes exactly the strict J-transversality reduction described above.

## 12. Smallest next action

Attack only the explicit AP deformation inside `Δ_m`.

A natural exact path is

`ρ_(m,t)(u) = (1-t u^(m²))^n`, `0≤t≤1`,

with t=0 the solved endpoint `K=I` and t=1 the AP target.

The next proof attempt should seek an exact no-zero / inertia-flow / compound-minor statement along this path, or derive a finite-difference formula for the `(m-1)`-compound of `Δ_m` relative to the solved Cauchy endpoint.

No monotonicity or no-zero theorem is claimed here.
