# #1162 — derivative-free refinement projector stability and finite Basel trace defect

Status: RESEARCH_NOTE / DERIVATIVE-FREE FINITE-RESOLUTION THEOREM PACKAGE / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-refinement-projector-stability-20260908-b62d
Date: 2026-09-08

## 1. Scope correction consumed

This note continues `research_notes/1162_resolution_admissibility_correction_20260907_b62d.md` and preserves the user's correction that microscopic/high-order differentiation is not automatically a stable observable under the rough discrete relation. No derivative in the integer resolution parameter N is used below.

BRC observer typing is applied as follows. Population: one integer refinement orbit `N,qN,...`. Retained observer: finitely many scalar readouts on that orbit. Allowed future operations: integer refinement and finite linear combinations. Nuisance branches: declared correction modes `N^(-2r)`. The quotient invariant below kills those branches exactly and has an explicit transverse-error norm. This is an observer-factorization result, not a positive-mass BRC claim.

## 2. Finite refinement projector

Let q>1 and define the actual refinement shift on sequences

`(E_q f)(N)=f(qN)`.

Assume only the declared finite correction model

`f(N)=a_0 + sum_{r=1}^m a_r N^(-2r)`.

Define

`Pi_(m,q) = product_{r=1}^m (E_q-q^(-2r)I)/(1-q^(-2r))`.

Then exactly

`Pi_(m,q) f = a_0`.

Thus the amplitudes `a_1,...,a_m` are quotientable nuisance data for this declared observer/future-operation scope. They may be arbitrarily large; the projection removes them exactly.

Writing

`Pi_(m,q)=sum_{j=0}^m w_j E_q^j`,

the coefficients alternate in sign and their absolute sum is

`kappa_(m,q)=sum_j |w_j| = product_{r=1}^m (1+q^(-2r))/(1-q^(-2r))`.

Hence if observed samples satisfy

`fhat(q^j N)=f(q^j N)+e_j`,

then

`|sum_j w_j fhat(q^jN)-a_0| <= sum_j |w_j||e_j| <= kappa_(m,q) max_j |e_j|`.

This controls arithmetic, readout and model residual errors once they have been honestly included in the sample error envelope.

## 3. Uniform stability for genuine integer refinement

For every fixed q>1,

`kappa_(m,q) <= kappa_(infinity,q) := product_{r>=1}(1+q^(-2r))/(1-q^(-2r)) < infinity`.

The product decreases as q increases. For every integer q>=2 the worst case is q=2, and in fact

`kappa_(infinity,2) < 2`.

A short proof of the strict bound uses rho=1/4 and

`log kappa = 2 sum_{j>=0} [rho^(2j+1)/((2j+1)(1-rho^(2j+1)))]`.

The j=0 term is 2/3. Bounding the remaining terms by `32/2835` gives

`log kappa < 2/3 + 32/2835`,

while

`log 2 = 2 atanh(1/3) > 2/3 + 2/81`.

Therefore every order-m projector built from integer refinement q>=2 has absolute sup-noise amplification strictly below 2, independently of m.

For dyadic refinement the first norms are

`5/3, 17/9, 1105/567, 3341/1701, ...`,

and the limit is approximately `1.9692603537`.

This is the central stability contrast with microscopic differentiation.

## 4. The q -> 1 differential limit is singular

Put `q=e^h`. Then

`kappa_(m,e^h)=product_{r=1}^m coth(rh)`.

For fixed m and h -> 0+,

`kappa_(m,e^h) ~ 1/(m! h^m)`.

Thus forcing refinement ratios toward one reproduces the expected derivative-like instability.

There is a stronger fixed-span form. If the total available resolution span is kept fixed,

`q^m=R=e^a`, so `q=e^(a/m)`,

then

`(1/m) log kappa_(m,e^(a/m)) -> integral_0^1 log(coth(ax)) dx > 0`.

Hence increasing the cancellation order while keeping the total scale window fixed causes exponential condition growth. Stable high-order elimination therefore requires genuine scale separation; an infinitesimal refinement window cannot be made arbitrarily high order for free.

This quantitatively implements the user's objection to treating microscopic differentiation as a stable primitive.

## 5. Finite model-admissibility test before projection

Do not assume the correction model merely because the projector exists. Define the annihilator

`A_(m,q)(E_q)=product_{r=0}^m (E_q-q^(-2r)I)`.

Every exact member of the declared model satisfies

`A_(m,q)(E_q) f(N)=0`.

This is a finite test using `m+2` actual refinement samples. Its coefficient absolute sum is

`eta_(m,q)=product_{r=0}^m (1+q^(-2r)) = 2 product_{r=1}^m(1+q^(-2r))`,

so a uniform sample error epsilon changes the tested residual by at most `eta_(m,q) epsilon`.

Workflow:
1. test the finite annihilator at the permitted scales;
2. reject/falsify the correction model if the residual exceeds the honest error envelope;
3. only after the model is proved or passes the declared finite test, apply `Pi_(m,q)`.

Passing a finite tolerance test is compatibility, not a theorem that an arbitrary rough sequence has the model globally.

## 6. Exact first-omitted-mode suppression

Let rho=q^(-2). For an unmodelled correction `N^(-2s)` with integer s>=m+1,

`Pi_(m,q)[N^(-2s)]
 = (-1)^m q^(-m(m+1)) [s-1 choose m]_rho N^(-2s)`,

where the bracket is the Gaussian binomial coefficient.

In particular the first omitted branch has the especially simple factor

`Pi_(m,q)[N^(-2(m+1))] = (-1)^m q^(-m(m+1)) N^(-2(m+1))`.

Thus after exact cancellation of m nuisance modes, the first smooth residual is not amplified: it is strongly suppressed. For q=2 the factors are `1/4, 1/64, 1/4096, ...` in absolute value for m=1,2,3,... .

## 7. Pure finite Basel invariant from cycle matrices

Let `L_N=2I-R_N-R_N^*` be the unit-edge cycle graph Laplacian and `L_N^+` its Moore-Penrose inverse. Define the dimensionless finite readout

`b_N = (2/N^2) Tr(L_N^+)`.

Finite effective resistance on the cycle gives

`Tr(L_N^+)=(N^2-1)/12`,

hence

`b_N=(N^2-1)/(6N^2)`.

For every integer q>=2,

`C_(N,q) := (q^2 b_(qN)-b_N)/(q^2-1) = 1/6`.

Equivalently, entirely as a finite graph trace defect,

`1/6 = 2 [Tr(L_(qN)^+) - Tr(L_N^+)] / [N^2(q^2-1)]`.

No limit, no derivative, no trigonometric diagonalization and no pi are needed for this identity. It defines a natural finite discrete Basel coefficient. The classical statement `zeta(2)=pi^2/6` is a separate compatibility/calibration step once angular/Fourier continuum semantics are declared.

For q=2 the invariant is simply

`(4 b_(2N)-b_N)/3 = 1/6`,

and uniform readout error epsilon is amplified by only `5epsilon/3`.

## 8. Higher finite cycle invariants

Define for m>=1

`b_m(N)=2^(2m-1) N^(-2m) Tr[(L_N^+)^m]`.

For the cycle the known exact finite trace/cosecant identities give a polynomial in `N^(-2)` of degree m. The first three are

`b_1(N)=1/6 - 1/(6N^2)`,

`b_2(N)=1/90 + 1/(9N^2) - 11/(90N^4)`,

`b_3(N)=1/945 + 1/(90N^2) + 4/(45N^4) - 191/(1890N^6)`.

Therefore the derivative-free dyadic projectors give, for every finite N,

`-b_1(N)/3 + 4b_1(2N)/3 = 1/6`,

`b_2(N)/45 - 4b_2(2N)/9 + 64b_2(4N)/45 = 1/90`,

`-b_3(N)/2835 + 4b_3(2N)/135 - 64b_3(4N)/135 + 4096b_3(8N)/2835 = 1/945`.

These constants are the finite discrete coefficients later identified in the classical angular compatibility layer with `zeta(2m)/pi^(2m)`.

## 9. Approximate refinement cocycle rigidity for the Basel scalar

Write the affine injection as

`c_q = b_(qN)-q^(-2)b_N`.

If it is N-independent and exact refinement is associative, then

`c_(pq)=c_p+p^(-2)c_q`.

Commutativity of pq gives

`(1-q^(-2))c_p=(1-p^(-2))c_q`,

so there is one common fixed-point coefficient C with

`c_q=(1-q^(-2))C`.

Thus the common fixed point is forced by the multiplicative refinement semigroup, not by a differential generator.

If the cocycle law in both orders has defect at most epsilon, then

`|c_p/(1-p^(-2)) - c_q/(1-q^(-2))|
 <= 2epsilon/[(1-p^(-2))(1-q^(-2))]`.

For p,q>=2 this is at most `32epsilon/9`. Hence even the cross-refinement fixed-point consistency has a finite roughness bound.

## 10. Prior-art boundary

The cancellation mechanism is a geometric-grid instance of classical Richardson/Romberg extrapolation; that general method and its need for an asymptotic/error expansion are established prior art. Stability of generalized Richardson extrapolation has also been studied in the numerical-analysis literature. No novelty claim is made for extrapolation itself.

The project-level candidate synthesis is narrower: exact cycle spectral-trace quotient invariants, an explicit rough-observer factorization, the order-uniform `<2` absolute-noise bound for integer refinement, the singular q->1 limit as the quantitative boundary against microscopic differentiation, and the finite trace-defect realization of the Basel coefficient 1/6.

## 11. BRC resolution

REUSE_APPLIED: observer/future-operation factorization and information-loss audit from the account BRC priority contract. The nuisance amplitudes are explicitly labeled and quotientable because the finite projector kills them under the declared future language. Residual out-of-model information is retained through the annihilator and error envelope.

NOT_APPLICABLE: positive-weight recurrent BRC machinery; the projector has alternating signed coefficients and is a linear quotient, not positive branch mass.

## Next

1. Replace the imported higher-m cycle cosecant formulas by a purely finite graph/forest or characteristic-polynomial derivation, avoiding trigonometric diagonalization.
2. Develop cross-q redundancy as a finite falsifier of the correction model.
3. Determine whether the `<2` uniform refinement stability and q->1 singularity already have an exact published extrapolation-theory analogue; do not claim priority before this check.
4. Keep the classical angular identification with zeta/pi typed as compatibility, not native promotion.
