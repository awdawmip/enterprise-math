# RH Kubilius-Alladi cross-scale parity reduction

Status: `RESEARCH FRONTIER / EXACT PROJECT IDENTITIES + PRIOR-ART KUBILIUS INPUT / NOT A PROOF OF RH`
Date: `2026-09-06`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / small-prime Kubilius model / Alladi BRC / cross-scale rough parity`

## 0. Typing guard

P000 is unchanged. Small-prime bits, ordered prime factors, arithmetic log budgets, and transfer operators below are provenance/relation coordinates, not native X6 axes.

BRC discipline remains

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

The full multiplicative endpoint constraint must be retained when it affects future operations.

---

## 1. Boundary-charge correction to the prime-source picture

The exact Stieltjes source identity

`d_y log G1(s,y)=y^-s/logy d(psi(y)-y)`

describes only variation in y. Recovering `G1(s,y)` requires a boundary constant `log G1(s,y0)`, which contains the global `-log zeta(s)` term.

Thus the Dickman Green split

`C_infinity=C_boundary + integral(depth * source)`

has a literal analytic analogue:

- local prime discrepancy contributes the distributed source;
- zero information may remain in the boundary charge.

Freeze:

`LOCAL_PRIME_SOURCE_CONTROL_DOES_NOT_REMOVE_THE_ZETA_BOUNDARY_MODE`.

This explains why extremely accurate prime information below a polylogarithmic cutoff does not by itself imply RH.

---

## 2. Local zero model for the z-hierarchy

The prime-zeta relation

`log zeta(s)=sum_{j>=1}P(js)/j`

implies that near a zeta zero `rho` of multiplicity m, only the `P(s)` channel is singular in `Re s>1/2`; locally, on a punctured neighborhood with a chosen logarithm branch,

`P(s)=m log(s-rho)+analytic`.

Therefore

`prod_p(1+z p^-s)`

has the rank-one local form

`H(s,z)(s-rho)^(m z)`

with H stable/nonzero locally after the noncritical channels are absorbed.

At `z=-1` this has the `1/zeta`-type pole `(s-rho)^(-m)`. Writing `w=z+1`, the complete w-series contains

`(s-rho)^(-m) exp(mw log(s-rho))`.

At `w=1` the infinite exponential exactly cancels the pole. Any finite K truncation remains

`(s-rho)^(-m) sum_{j<=K}(m log(s-rho))^j/j!`

and is still singular.

Freeze:

`FINITE_K_BRC_JET_CANNOT_ANALYTICALLY_REMOVE_A_ZETA_ZERO`.

Growing-depth finite-X BRC, if useful, must prove real-variable finite-scale cancellation and only then pass to a limit; finite analytic Taylor truncation cannot be used to cross a zero.

---

## 3. Critical-line Euler jets are exactly Poisson-binomial survival probabilities

Fix a finite prime set `p<=Y` and put

`a_p=p^-1/2`,
`P_Y(z)=prod_{p<=Y}(1+z a_p)`.

Set `w=z+1`. Then

`P_Y(-1+w)=prod_p[(1-a_p)+a_p w]`.

If `X_p` are independent Bernoulli variables with `P(X_p=1)=a_p` and

`S_Y=sum_p X_p`,

then exactly

`P_Y(-1+w)=E[w^(S_Y)].`

For the regularized primitive extractor

`R_Y(z)=[P_Y(z)-1]/z`,

use `(w^j-1)/(w-1)=1+...+w^(j-1)` to obtain

`R_Y(-1+w)=sum_{k>=1}P(S_Y>=k) w^(k-1)`.

Equivalently, for the higher-duality Euler layer

`Q_k(1/2;Y)=sum_{d>1, d|prod_{p<=Y}p}`
` mu(d) C(omega(d)-1,k-1)d^-1/2`,

we have the exact positive identity

`(-1)^k Q_k(1/2;Y)=P(S_Y>=k)`.

Thus the complete parity-to-prime hierarchy is the survival profile of a Poisson-binomial occupancy variable, and

`sum_{p<=Y}p^-1/2 = E S_Y = sum_{k>=1}P(S_Y>=k)`.

Consequences:

- cancellation occurs inside each divisor-subset layer;
- after the natural `(-1)^k` orientation correction, distinct k layers are nonnegative;
- there is no additional random-sign cancellation across k in this finite critical Euler sector.

Freeze:

`HIGHER_DUALITY_K_LAYERS_ARE_NOT_A_CROSS_K_RANDOM_SIGN_SOURCE`.

---

## 4. Why bare critical-line Euler truncation differs from Cell-constrained BRC

At

`Y=(log X)^2`,

PNT gives

`m_Y=E S_Y=sum_{p<=Y}p^-1/2 ~ logX/loglogX`.

The Enterprise Cell-critical depth is

`K_Cell~(1/2)logX/loglogX~m_Y/2`.

Since `Var(S_Y)<=m_Y`, `S_Y/m_Y ->1` in L2. Hence

`sum_{k>K_Cell}P(S_Y>=k)`
`=E[(S_Y-K_Cell)_+]`
`=(1/2+o(1))m_Y`.

Therefore the first `K_Cell` bare Euler jets at `s=1/2` do not approximate the primitive prime channel at all.

By contrast, the Cell-constrained ordered-factor selector at the same K has only `X^(1/2+o(1))` exceptional integer Cells, by Hardy-Ramanujan.

The difference is the endpoint constraint

`product prime_factors <= X`.

The bare Euler product permits arbitrary subsets even when their product is far beyond X.

Freeze:

`MULTIPLICATIVE_CELL_CUTOFF_IS_ESSENTIAL_INFORMATION`.

Also:

`ANALYTIC_EULER_WEIGHT p^-1/2 != CELL_OCCUPANCY_PROBABILITY`.

---

## 5. Exact Alladi-BRC Gram/Parseval identity

For

`L_k(n;f)=sum_{1<d|n}mu(d)C(omega(d)-1,k-1)f(p_1(d))`,

Alladi duality gives

`L_k(n;f)=(-1)^k f(P_k(n))`.

Therefore, for arbitrary prime test functions f,g,

`sum_{k>=1}L_k(n;f) conjugate(L_k(n;g))`
`=sum_{p|n}f(p)conjugate(g(p)).`

In particular,

`sum_k |L_k(n;f)|^2 = sum_{p|n}|f(p)|^2.`

This is an exact project-derived Gram consequence of the published Alladi identity.

Project interface:

`ALLADI_BRC_PARSEVAL`.

It shows that the complete higher-duality transform retains primitive prime collision energy exactly. It is not a fixed-state compression.

For a truncation at K,

`sum_{k<=K}|L_k(n;f)|^2=sum_{j<=K}|f(P_j(n))|^2`,

so the lost Gram energy is precisely the positive ordered-prime tail.

---

## 6. Squarefree critical prime-source port

For a prime p,

`sum_{n<=X, mu^2(n)=1, p|n}1`
`=X/[zeta(2)(p+1)] + O(sqrt(X/p))`.

This follows elementarily from `mu^2(m)=sum_{d^2|m}mu(d)` after writing `n=pm` and enforcing `(m,p)=1`.

Take

`Y=(logX)^2`,
`f_Y(p)=(p+1)/sqrt(p) 1_{p<=Y}`.

Then

`sum_{p<=Y}p^-1/2`
`= zeta(2)/X sum_{n<=X}mu^2(n)sum_{p|n}f_Y(p)`
`+O(X^-1/2+o(1)).`

Let

`K=floor(logX/(2loglogX))`.

The Hardy-Ramanujan tail `#{n<=X:omega(n)>K}=X^(1/2+o(1))`, together with the polylogarithmic size of f_Y, gives

`sum_{p<=Y}p^-1/2`
`= zeta(2)/X sum_{n<=X}mu^2(n)sum_{k<=K}f_Y(P_k(n))`
`+O(X^-1/2+o(1)).`

Finally use `f_Y(P_k)=(-1)^k L_k(n;f_Y)`.

Thus the critical prime source has a pure squarefree/Mobius-support/growing-depth BRC representation with square-root truncation error.

---

## 7. Kubilius independence reaches exactly RH scale at the same cutoff

Let N be uniform on `{1,...,X}` and let

`V_Y(N)=(nu_p(N))_{p<=Y}`.

The classical Kubilius model replaces this vector by independent geometric variables `Z_p` with

`P(Z_p=j)=(1-1/p)p^-j`.

Tenenbaum's optimal total-variation bound (as quoted in Ford's modern account) is

`d_TV(V_Y,Z_Y) <<_epsilon u^-u + X^(-1+epsilon)`,

where

`u=logX/logY`.

At

`Y=(logX)^2`,
`u~(1/2)logX/loglogX`,

we have

`u^-u=X^(-1/2+o(1))`.

Therefore the complete small-prime valuation cube is unconditionally independentizable with RH-scale total-variation error:

`d_TV = X^(-1/2+o(1)).`

This is prior art, not a project theorem.

Freeze:

`SMALL_PRIME_INTERNAL_DEPENDENCE_IS_NOT_THE_RH_BOTTLENECK_AT_Y=(logX)^2`.

---

## 8. Exact cross-scale reduction to one rough-budget response

For each N, write uniquely

`N=D M`,

where D contains all prime powers with `p<=Y`, while `P^-(M)>Y`.

Define

`S_Y(U)=#{m<=U:P^-(m)>Y}`,
`R_Y(U)=sum_{m<=U,P^-(m)>Y}mu(m)`,

and the bounded rough parity bias

`G_Y(U)=R_Y(U)/S_Y(U)`

when the denominator is nonzero, with value 0 otherwise.

Given the exact small-prime valuation vector D:

- if D is not squarefree, `E[mu(N)|D]=0`;
- if D is squarefree,
  `E[mu(N)|D]=mu(D)G_Y(X/D)`.

The independent Kubilius model assigns each Y-smooth integer d the exact probability

`P(D_*=d)=V(Y)/d`,

where

`V(Y)=prod_{p<=Y}(1-1/p)`.

Since the conditional observable is bounded by 1, total variation gives

`M(X)/X`
`=V(Y) sum_{d squarefree,P^+(d)<=Y} mu(d)/d G_Y(X/d)`
`+O(X^-1/2+o(1)).`

This is the central new reduction.

Conditioning the geometric model on its small-prime part being squarefree, the bits are independent

`B_p~Bernoulli(1/(p+1))`.

If

`C_Y=prod_{p<=Y}(1-1/p^2)`,
`D(B)=prod_{p<=Y}p^(B_p)`,

then equivalently

`M(X)/X`
`=C_Y E[(-1)^(sum B_p) G_Y(X/D(B))]`
`+O(X^-1/2+o(1)).`

Thus RH is reduced, up to an already RH-scale error, to a parity correlation on an independent small-prime cube acting on a one-dimensional remaining-budget response.

---

## 9. Product-difference operator form

Let

`F_X(t)=G_Y(X e^-t)`

and let `T_h F(t)=F(t+h)`.

Then the preceding signed expectation is exactly

`D_Y F_X(0)`,

where

`D_Y := V(Y) prod_{p<=Y}(I-p^-1 T_(log p)).`

Therefore

`M(X)/X = (D_Y F_X)(0)+O(X^-1/2+o(1)).`

This is an operation-safe compression of the small-prime subset to its product/log-budget coordinate because all future rough evolution depends on the small part only through `X/D`.

Project interface name:

`KUBILIUS_SMALL_PRIME_PARITY_BRC_OPERATOR`.

---

## 10. Small-prime parity itself is only logarithmically mixed

Under the conditional squarefree Bernoulli model,

`E[(-1)^(sum B_p)]`
`=prod_{p<=Y}(p-1)/(p+1)`
`asymp C/(logY)^2`.

Equivalently, under the unconditioned geometric model,

`E[mu(D_*)1_{D_* squarefree}]=V(Y)^2`.

Thus the small-prime parity bias is only logarithmically small, far above `X^-1/2`.

Therefore RH cancellation cannot come from small-prime internal independence alone.

Freeze:

`RH_REMAINDER = CROSS_SCALE_SMALL_LARGE_PARITY_COUPLING`.

The product budget `D M<=X` is the only coupling left after Kubilius independence of the small-prime cube.

---

## 11. Poisson-Dirichlet macro limit does not control this microscopic boundary layer

Billingsley/Poisson-Dirichlet theory controls normalized large ordered factors `log P_k/logX`. Quantitative couplings can achieve expected total log-factor displacement `O(loglogX)`.

The current critical source uses primes

`p<=Y=(logX)^2`,

whose normalized coordinates satisfy

`log p/logX=O(loglogX/logX)->0`.

Thus it lies in the microscopic zero-end boundary layer of the Poisson-Dirichlet process. Moreover the observer `sqrt(p)` has growing Lipschitz constant in log-coordinate.

Freeze:

`POISSON_DIRICHLET_MACRO_LIMIT != MICROSCOPIC_PRIME_SOURCE_CONTROL`.

This is a prior-art boundary, not a new probabilistic theorem.

---

## 12. New smallest target: projected Dickman stability

Let `F_cont` be the continuum rough-parity/budget response obtained from the Dickman-Buchstab model at the same threshold.

The exact Kubilius reduction shows that a full pointwise estimate

`F_X(t)-F_cont(t)` uniformly small

is stronger than necessary and risks re-entering Hildebrand-type RH-equivalent smooth-count control.

It suffices to control only the parity-BRC projection

`(D_Y(F_X-F_cont))(0)`.

Candidate target:

`PROJECTED_DICKMAN_STABILITY:`

`|(D_Y(F_X-F_cont))(0)| <= X^(-1/2+epsilon)`

for every epsilon>0, with a separately verified RH-scale bound for the continuum term.

This permits large pointwise discrete errors so long as they lie nearly orthogonal to the complete small-prime parity operator.

This is now the preferred smallest research unit.

No RH proof is claimed.