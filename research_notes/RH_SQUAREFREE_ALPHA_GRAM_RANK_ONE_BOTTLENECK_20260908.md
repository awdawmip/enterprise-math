# RH squarefree-alpha Gram and mixed-zeta rank-one bottleneck

Status: `RESEARCH FRONTIER / EXACT FINITE GRAM + NEGATIVE ROUTE AUDIT / NOT RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Möbius / squarefree rough factor count / alpha interpolation / Brownian cosine observer / PSD Gram / zeta singularity filtration`

## 0. Context and prior-art boundary

The same-day note

`RH_FRACTIONAL_NODE_ROUGH_BRC_INTERPOLATION_CORRECTION_20260908.md`

showed that Möbius coefficients below the critical support can be reconstructed from bounded fractional rough branches with subpolynomial interpolation total variation.

The present note makes two refinements:

1. because the final target is Möbius, rough prime powers can be projected out at the start, giving an even simpler squarefree alpha family;
2. the natural cross-alpha PSD collision geometry is audited against the first Brownian/cosine RH-equivalent observer.

The Euler products `prod_p(1+z p^-s)` and Selberg--Delange analysis of squarefree factor-count generating functions are classical. The generic Mellin principle that a square-root Möbius-type weighted bound can imply a zeta zero-free half-plane is also classical. The project-specific content here is the prime-cut finite BRC packaging, the exact collision-isometry identity, and the route audit showing where the rank-one zeta obstruction re-enters.

---

## 1. Squarefree alpha branch family

Fix a prime cutoff y and define, for real or complex alpha,

`E_(alpha,y)(s) = prod_(p<=y)(1-p^-s) prod_(p>y)(1+alpha p^-s)`.

For an integer n, write its unique prime-cut factorization

`n=a b`,

where all prime divisors of a are `<=y` and all prime divisors of b are `>y`.

The coefficient is exactly

`e_(alpha,y)(n)=mu(a) mu(b)^2 alpha^(omega(b))`.

Equivalently,

`e_(alpha,y)(n)=mu(n)^2 mu(a) alpha^(r_y(n))`

when n is squarefree, and is zero otherwise, where

`r_y(n)=#{p|n:p>y}`.

Consequences:

- for `0<=alpha<=1`, `|e_(alpha,y)(n)|<=1` Cellwise;
- at `alpha=-1`, exactly `e_(-1,y)(n)=mu(n)` for every n;
- the only sign in a positive-alpha branch is the common small-prime factor `mu(a)`;
- the rough arm is the positive monomial `alpha^(r_y(n))`.

This family is simpler than generalized-divisor branches when the final observer already contains the squarefree projector.

Freeze:

`SQUAREFREE_ROUGH_ALPHA_BRANCH`.

---

## 2. Critical finite interpolation

If `n<=X<=y^K`, then every rough prime factor of n exceeds y, hence

`y^(r_y(n))<n<=y^K`.

Therefore

`r_y(n)<K`.

For any K distinct alpha-nodes `alpha_0,...,alpha_(K-1)` and Lagrange weights `c_j` evaluating a degree-<K polynomial at `alpha=-1`, one has exactly, for every `n<=X`,

`mu(n)=sum_j c_j e_(alpha_j,y)(n)`.

At

`y=(log X)^2`,

one may take

`K=ceil(log X/log y)~(1/2)log X/loglog X`.

Thus the same RH-critical growing BRC depth appears without any rough prime-power multiplicity.

---

## 3. First cosine observer and the alpha=1 pole ground mode

Let

`w(x)=cos(pi x/2)` for `0<=x<=1`,

and

`Q_(X,y)(alpha)=sum_(n<=X)e_(alpha,y)(n) w(n/X)`.

For `X<=y^K`, `Q_(X,y)` is a polynomial in alpha of degree `<K`, and

`Q_(X,y)(-1)=sum_(n<=X)mu(n)w(n/X)`

is the first Brownian/cosine RH-equivalent scalar from the existing project note.

At alpha=1,

`E_(1,y)(s)=zeta(s) A_y(s)`,

where

`A_y(s)=F_y(s)^2/[zeta(2s)F_y(2s)]`,

and

`F_y(s)=prod_(p<=y)(1-p^-s)`.

The factor `A_y` is holomorphic in a half-plane containing `Re(s)>1/2`, apart from no zeta-zero denominator in that region: `zeta(2s)` is absolutely convergent/nonzero for `Re(s)>1/2`.

Let

`W(s)=int_0^1 x^(s-1)cos(pi x/2) dx`.

The existing Brownian-mode note proved that W has no zeros in `Re(s)>0`. Two integrations by parts also give `W(s)=O_sigma((1+|Im s|)^-2)` on fixed vertical strips with positive real part.

Mellin inversion on `Re(s)>1`, followed by a shift to `Re(s)=1/2+epsilon`, crosses only the simple pole of zeta at 1. The finite Euler factor on the new line satisfies

`|A_y(1/2+epsilon+it)| <= exp(O_epsilon(y^(1/2-epsilon)/log y))`.

Using the classical convexity bound for zeta and the `t^-2` decay of W gives

`Q_(X,y)(1)`
`= W(1) A_y(1) X`
`  + O_epsilon(X^(1/2+epsilon) exp(O_epsilon(y^(1/2-epsilon)/log y)))`.

Since `W(1)=2/pi`, and Mertens' product theorem gives

`A_y(1)~e^(-2 gamma)/(log y)^2`,

at `y=(log X)^2` one obtains

`Q_(X,y)(1)`
`~ (2e^(-2gamma)/pi) X/(log y)^2`.

Thus a positive-alpha branch contains an unavoidable order-`X/polylog(X)` pole ground mode even though the parity endpoint alpha=-1 is conjecturally square-root.

---

## 4. Direct alpha-L2 route is impossible

For every polynomial P of degree `<K`, the shifted Legendre reproducing kernel at the endpoint alpha=1 is exactly K^2. Hence

`|P(1)|^2 <= K^2 int_0^1 |P(alpha)|^2 d alpha`.

Apply this to `P=Q_(X,y)`. At the critical y and K,

`int_0^1 |Q_(X,y)(alpha)|^2 d alpha`
`>= |Q_(X,y)(1)|^2/K^2`
`= X^(2-o(1))`.

Therefore the hoped-for estimate

`int_0^1 |Q(alpha)|^2 d alpha <= X^(1+o(1))`

is false by almost a full power of X.

Freeze no-go:

`ORDINARY_CROSS_ALPHA_L2_IS_DOMINATED_BY_THE_POLE_GROUND_MODE`.

A Lebesgue-alpha Hilbert average followed by extrapolation cannot produce RH scale.

Conversation-local exact numerical pilots up to X=5*10^5 were consistent with the onset of this growth, but the theorem above does not rely on those computations.

---

## 5. Arithmetic collision Gram is exactly stable

The failure of ordinary alpha-L2 is not interpolation instability.

For alpha,beta>=0 define the positive-weight Gram kernel

`G_(X,y)(alpha,beta)`
`=sum_(n<=X)e_(alpha,y)(n)e_(beta,y)(n)w(n/X)`.

Because w>=0 on `[0,1]`, this is PSD. On squarefree Cells,

`e_alpha(n)e_beta(n)=mu(n)^2 (alpha beta)^(r_y(n))`.

Hence

`G_(X,y)(alpha,beta)=sum_(r=0)^(K-1) N_r(X,y) (alpha beta)^r`,

where

`N_r(X,y)=sum_(n<=X, mu(n)^2=1, r_y(n)=r) w(n/X)>=0`.

Thus the branch Hilbert space is exactly the finite moment/RKHS kernel of the positive rough-arity histogram.

Take any K interpolation nodes and let G be their KxK Gram matrix and c the Lagrange vector for alpha=-1. Cellwise interpolation gives

`sum_j c_j e_(alpha_j,y)(n)=mu(n)`.

Therefore exactly

`c^T G c = sum_(n<=X)mu(n)^2 w(n/X)`.

By squarefree density and partial summation,

`c^T G c ~ (12/pi^3) X`.

Freeze:

`FRACTIONAL_PARITY_INTERPOLATION_IS_AN_EXACT_COLLISION_ISOMETRY`.

The exponential `ell^1` interpolation total variation disappears completely in the correct arithmetic collision metric. Thus interpolation conditioning is **not** the power-scale obstruction.

---

## 6. Generic Gram duality is still far too weak

Let B be the weighted branch feature matrix

`B_(n,j)=sqrt(w(n/X)) e_(alpha_j,y)(n)`,

so `G=B^T B`.

Let

`u_n=sqrt(w(n/X))`

and

`m=B^T u`,

so that

`c^T m=Q_(X,y)(-1)`.

The canonical Hilbert-dual quantity is

`m^T G^+ m = ||Proj_col(B) u||_2^2`.

It cannot be `X^o(1)`. The vector corresponding to the branch alpha=1 lies in `col(B)` for any K exact nodes, and therefore the variational characterization gives

`m^T G^+ m >= Q_(X,y)(1)^2/G_(X,y)(1,1)`.

But

`G_(X,y)(1,1)=sum_(n<=X)mu(n)^2 w(n/X)~(12/pi^3)X`.

Consequently

`m^T G^+m >= X^(1-o(1))`.

So generic Cauchy--Schwarz in the collision Gram cannot prove the required coherence even though the primal target vector has perfect square-root collision norm.

Freeze distinction:

`COLLISION_NORM_STABLE != OBSERVER_DUAL_NORM_SMALL`.

The missing information is the signed orientation of the interpolation endpoint relative to the large observer ground modes.

---

## 7. Mixed target--branch overlaps expose the zeta obstruction directly

Define the mixed coefficient

`h_(alpha,y)(n)=mu(n)e_(alpha,y)(n)`.

For squarefree n=ab as above,

`h_(alpha,y)(n)=mu(a)^2 mu(b) alpha^(omega(b))`.

Its Dirichlet series is

`H_(alpha,y)(s)`
`=prod_(p<=y)(1+p^-s) prod_(p>y)(1-alpha p^-s)`.

For every fixed `0<alpha<=1`, factor

`H_(alpha,y)(s)=A_(alpha,y)(s) zeta(s)^(-alpha)`

on `Re(s)>1`, where

`A_(alpha,y)(s)`
`=prod_(p<=y)(1+p^-s)(1-p^-s)^(-alpha)`
` * prod_(p>y)(1-alpha p^-s)(1-p^-s)^(-alpha)`.

For p>y the logarithm of the local ratio is `O_alpha(p^(-2s))`; hence the infinite rough product converges normally in `Re(s)>1/2`. The finite small-prime product is nonzero in `Re(s)>0`. Therefore `A_(alpha,y)` is holomorphic and nonzero in `Re(s)>1/2`.

At alpha=1 this simplifies to

`H_(1,y)(s)=F_y(2s)/[zeta(s)F_y(s)^2]`.

Thus every fixed positive-alpha mixed overlap retains a negative power of zeta as its only critical singular factor.

### Fixed-alpha square-root bound is RH-strength

Let

`J_(alpha,y)(X)=sum_(n<=X)h_(alpha,y)(n)w(n/X)`

with y and alpha fixed. If, for every epsilon>0,

`J_(alpha,y)(X)=O_epsilon(X^(1/2+epsilon))`,

then Mellin transformation gives a holomorphic continuation of

`W(s)A_(alpha,y)(s)zeta(s)^(-alpha)`

to `Re(s)>1/2`.

The cosine Mellin factor W and `A_(alpha,y)` are nonzero there. A zeta zero rho in that half-plane would make `zeta^(-alpha)` either a pole (when the local exponent is integral) or a non-removable branch singularity. Hence such a bound forces the zeta zero-free half-plane `Re(s)>1/2`, and therefore RH by symmetry.

So attempting to control any one positive-alpha mixed Gram entry at the desired square-root scale already reaches RH strength.

Freeze:

`FIXED_POSITIVE_ALPHA_MIXED_OVERLAP_SQRT_BOUND => RH`.

---

## 8. Finite cross-alpha deflation cannot cancel zeta-zero singularities

Take distinct fixed numbers

`0<alpha_1<...<alpha_m<=1`

and constants `r_j`, not all zero. Consider

`L(s)=sum_j r_j H_(alpha_j,y)(s)`.

Let rho be a zeta zero of multiplicity q. On a slit neighborhood of rho,

`H_(alpha_j,y)(s)`
`=C_j (s-rho)^(-q alpha_j)(1+o(1))`,

with `C_j!=0`.

The term with largest alpha has strictly strongest singular exponent. Multiplying by `(s-rho)^(q alpha_m)` and letting s tend to rho shows that holomorphy can hold only if `r_m=0`. Induction forces every positive-alpha coefficient to vanish.

Therefore no nontrivial finite linear combination of distinct fixed positive-alpha mixed symbols is zero-transparent.

Freeze no-go:

`FINITE_POSITIVE_ALPHA_DEFLATION_CANNOT_REMOVE_THE_ZETA_ZERO_MODE`.

This does not contradict the exact finite coefficient interpolation: coefficient support truncation carries a high-support remainder, and—as already frozen—high coefficient support does not imply removal of analytic singularities.

The only remaining possible escape is genuinely scale-growing/coefficient-local rather than a fixed analytic combination.

---

## 9. Squeezing the alpha window has an unavoidable conditioning tradeoff

Suppose K exact interpolation nodes are confined to `[0,A]` and one extrapolates to alpha=-1. Map `[0,A]` affinely to `[-1,1]`. The target maps to

`t_*=-1-2/A`.

For the degree K-1 Chebyshev polynomial, every exact evaluation formula with total variation Lambda satisfies

`Lambda >= |T_(K-1)(t_*)|`.

For small A,

`log Lambda >= (K-1)[log(4/A)+O(A)]-O(1)`.

At

`K~(1/2)log X/loglog X`,

requiring only subpolynomial interpolation cost `Lambda=X^o(1)` forces

`log(1/A)=o(loglog X)`,

or equivalently

`A=(log X)^(-o(1))=X^(-o(1))`.

Thus one cannot make every positive alpha polynomially tiny while retaining a subpolynomial finite-depth extrapolation condition number.

This is a conditioning theorem only. It should not be upgraded to a zeta-zero lower bound without a separate uniform singularity-to-coefficient argument for scale-dependent alpha.

---

## 10. Current frontier

The squarefree alpha family resolves several architectural questions:

1. rough prime powers are unnecessary for the Möbius endpoint;
2. positive-alpha branches are Cellwise bounded;
3. the RH-critical K-depth interpolation is exact;
4. interpolation is perfectly conditioned in the arithmetic collision Gram;
5. ordinary alpha-L2 is destroyed by the pole ground mode;
6. generic Gram duality has a polynomially large observer norm;
7. projecting onto fixed positive-alpha ground directions exposes `zeta^(-alpha)` and is already RH-strength;
8. no finite fixed-alpha linear deflation cancels all zeta-zero singularities.

Therefore the next admissible question is **not** another fixed-alpha Hilbert norm or finite deflation.

The possible remaining lane is:

`SCALE-GROWING K BRANCHES + COEFFICIENT-LOCAL PROVENANCE TRANSFORM`

that exploits finite-support arithmetic before analytic continuation and preserves the exact collision isometry, while producing a nontrivial bound on the endpoint/observer coherence.

A useful next object is the positive rough-arity histogram

`N_r(X,y)`

and its parity Fourier coefficient. The challenge is to exploit cross-r structure (Buchstab/Dickman recurrence and prime-discrete errors) rather than sectorwise Cauchy--Schwarz, because sectorwise RMS is strictly stronger than RH and discards the decisive alternating cancellation.
