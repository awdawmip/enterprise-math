# RH Green rank-one mode / Alladi critical primitive-source port

Status: `RESEARCH FRONTIER / EXACT PROJECT-DERIVED IDENTITIES + PRIOR-ART INPUT / NOT A PROOF OF RH`
Date: `2026-09-06`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / Dickman delay / Alladi higher duality / rough BRC / critical provenance depth`

## 0. Typing guard

P000 is unchanged. Prime labels and ordered prime factors are arithmetic provenance, not native X6 axes. X6 width remains fixed; the depth of the provenance circuit may grow.

BRC priority remains

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

Positive factorial capacity or shuffle multiplicity must not be identified with signed Möbius cancellation.

---

## 1. Exact rank-one Green invariant for the Dickman delay

Linearize the rough/Dickman transport around the continuum carrier in the form

`(u delta(u))' = -delta(u-1) + q(u)`.

Put

`h(t)=(t+1)delta(t+1)`.

Then

`t h'(t)+h(t-1)=t q(t+1)`.

Define

`C[h](t)=t h(t)-int_{t-1}^t h(s)ds`.

Direct differentiation gives the exact identity

`C'[h](t)=t q(t+1)`.

Hence for the homogeneous delay equation `C[h]` is exactly conserved.

### Unit source at depth v

For an impulsive unit source at depth v, the response `g_v` has

- `g_v(u)=0` for `u<v`,
- `g_v(u)=1` for `v<=u<=v+1`,
- `g_v(u)=1-int_v^(u-1)g_v(s)/s ds` for `u>v+1`.

The shifted response `h_v(t)=g_v(t+1)` satisfies the homogeneous Dickman delay equation and has

`C[h_v]=v-1`.

Consequently the generic late-source response belongs to the dominant class

`g_v(u)~(v-1)/u`.

The special source at `v=1` has zero charge and gives the subdominant Dickman response

`g_1(u)=rho(u-1)`.

Thus the delay propagator has a one-dimensional algebraic dominant mode. A general source has final dominant coefficient

`C_infinity=C_initial+int (v-1)q(v)dv`.

Freeze:

`DICKMAN_DELAY_CRITICAL_MODE_HAS_RANK_ONE`.

This independently matches the earlier Mellin/Newton and prime-only Euler `critical rank = 1` results.

---

## 2. Linear-sieve parity comparison

Classical optimal linear-sieve envelopes may be written

`f(u)=e^gamma(omega(u)-rho(u)/u)`,
`F(u)=e^gamma(omega(u)+rho(u)/u)`.

Hence

`F(u)-f(u)=2e^gamma rho(u)/u`.

This supports the structural reading:

- the common positive background is the dominant Buchstab component;
- even/odd distinction is carried by the Dickman subdominant component.

Therefore the rank-one dominant Green charge must be structurally orthogonalized before parity information can remain at the Dickman scale. Classical sieve parity examples show that fixed-order positive sieve data alone does not accomplish this.

Freeze:

`LINEAR_SIEVE_PARITY_BARRIER_IS_COMPATIBLE_WITH_THE_GREEN_RANK_ONE_SPLIT`.

This is comparison/prior art, not a project proof of a new sieve theorem.

---

## 3. First arithmetic annihilation: Tenenbaum 2026

Tenenbaum proved, for a prime set P having natural density,

`sum_{P^-(n) in P} mu(n) omega(n)/n = 0`,

with effective convergence estimates.

The weight `omega(n)` is the first factor-depth moment. This is an arithmetic analogue of cancellation of a first depth-charge, but its known finite convergence is far weaker than RH scale.

Freeze:

`FIRST_FACTOR_DEPTH_CHARGE_CAN_VANISH_UNCONDITIONALLY`.

Do not identify this alone with the Green rank-one charge without an explicit finite-scale transfer theorem.

---

## 4. Alladi higher duality as a measure-valued BRC transform

For `k>=1`, let `p_1(d)` be the least prime factor of d and `P_k(n)` the kth largest distinct prime factor of n, with the convention `f(P_k(n))=0` if `omega(n)<k`.

Alladi higher duality gives, for any prime test function f,

`sum_{1<d|n} mu(d) C(omega(d)-1,k-1) f(p_1(d))`
`= (-1)^k f(P_k(n)).`

Define the signed prime-valued divisor measure

`nu_{k,n}=sum_{1<d|n} mu(d) C(omega(d)-1,k-1) delta_{p_1(d)}`.

Then exactly

`nu_{k,n}=(-1)^k delta_{P_k(n)}`.

Interpretation:

**the entire signed kth-order divisor subset cloud collapses exactly to one ordered-prime atom while retaining prime size/location.**

Project interface name:

`ALLADI_ORDER_STATISTIC_BRC_TRANSFORM`.

The identity is prior art; the name/interface is project-local.

---

## 5. Exact finite-depth primitive selector

Let

`L_k(n;f)=sum_{1<d|n} mu(d) C(omega(d)-1,k-1) f(p_1(d))`
`=(-1)^k f(P_k(n)).`

Using

`sum_{k=1}^K (-1)^k C(r-1,k-1)`
`= -1` if `r=1`,
`= 0` if `2<=r<=K`,
`= (-1)^K C(r-2,K-1)` if `r>K`,

we obtain the exact identity

`sum_{k=1}^K f(P_k(n))`
`= sum_{p|n}f(p)`
` + (-1)^K sum_{d|n,omega(d)>K}`
`   mu(d) C(omega(d)-2,K-1)f(p_1(d)).`

For `f>=0`, the remainder is equivalently the positive ordered-prime tail

`sum_{k>K}f(P_k(n))`.

Thus the first K duality layers exactly cancel every composite provenance packet of cardinality `2,...,K`; only primitive-prime mass and arity `>K` remain.

Freeze:

`K_LAYER_ALLADI_DUALITY = PRIMITIVE_SELECTOR + HIGH_ARITY_REMAINDER`.

---

## 6. Critical-depth positive capacity law

Take

`y=(log x)^2`,
`lambda=sum_{y<p<=x}1/p = loglog x-loglog y+O(1) ~ loglog x`.

If `N_{>=k}(x;y)` counts integers `<=x` with at least k distinct prime factors exceeding y, factorial moments give

`N_{>=k}(x;y) <= x lambda^k/k!`.

Let

`u_RH~(1/2)log x/loglog x`,
`k=alpha u_RH`, `0<alpha<=1` fixed.

Stirling yields

`lambda^k/k! = x^(-alpha/2+o(1))`,

so

`N_{>=k}(x;y) <= x^(1-alpha/2+o(1)).`

At the full critical depth

`K=floor(log x/(2loglog x))`,

`N_{>=K}(x;y) <= x^(1/2+o(1)).`

This is a positive capacity statement; it does not use signed cancellation.

---

## 7. Hardy-Ramanujan critical residual and the primitive-source lift

The uniform Hardy-Ramanujan bound

`#{n<=X:omega(n)=r}`
`<< X/log X * (loglog X+C)^(r-1)/(r-1)!`

implies, for

`K=floor(log X/(2loglog X))`,

`#{n<=X:omega(n)>K}=X^(1/2+o(1)).`

Let

`Y=(log X)^2`,
`f_Y(p)=sqrt(p) 1_{p<=Y}`.

The full prime-divisor average satisfies

`(1/X)sum_{n<=X}sum_{p|n}f_Y(p)`
`=sum_{p<=Y}p^-1/2 + O(Y^(3/2)/(X logY)).`

The finite primitive selector and the Hardy-Ramanujan tail give

`sum_{p<=Y}p^-1/2`
`= (1/X)sum_{n<=X}sum_{k<=K}`
`  sqrt(P_k(n))1_{P_k(n)<=Y}`
`  + O(X^-1/2+o(1)).`

Hence the sole prime-discrete critical source

`J_1/2(Y)=sum_{p<=Y}p^-1/2 - int_2^Y dt/(sqrt(t)logt)`

has the exact Enterprise internal port

`J_1/2(Y)`
`= (1/X)sum_{n<=X}sum_{k<=K}`
`  sqrt(P_k(n))1_{P_k(n)<=Y}`
`  - int_2^Y dt/(sqrt(t)logt)`
`  + O(X^-1/2+o(1)).`

Applying the measure-valued Alladi transform to each `P_k` converts this ordered-factor average into a signed divisor-BRC cloud.

This closes the representation interface:

`PRIME_CRITICAL_SOURCE -> GROWING_DEPTH_FACTOR_BRC + SQRT_SCALE_TRUNCATION_ERROR`.

It is an exact/equivalent lift, not an estimate of `J_1/2` itself and therefore not an RH proof.

---

## 8. Factorial normalization removes a false high-k obstruction

Alamoudi's rough generating function uses z-derivatives at `z=-1`. Raw derivatives display factorial coefficients. Define instead

`H_r=(1/r!) partial_z^r g(s,y,z)|_{z=-1}`.

After normalization, the N=0 recurrence takes the schematic exact form

`H_r=(A/r)H_{r-1} + (1/r)sum_{i=0}^{r-2}B_{r-i}H_i`,

where on the zero-free contour

`|A|<=loglog y+O(1)`

and `B_m=O(1)` for `m>=2` in the relevant regime.

A positive majorant recurrence

`r h_r = a h_{r-1}+B sum_{i<=r-2}h_i`

has generating function

`h(z)=h_0 exp((a-B)z)(1-z)^(-B)`.

Therefore the factorial-normalized pure z-jets grow at most polynomially in r times polylogarithmic y-factors in this model; for `r<=K~logx/loglogx` this is `x^o(1)`.

Freeze:

`RAW_HIGH_K_FACTORIAL_GROWTH_IS_LARGELY_A_NORMALIZATION_ARTIFACT`.

This does not remove the `1/zeta(s)` analytic obstruction in fixed-k formulas.

---

## 9. Regularized Taylor transport from parity to the primitive-prime channel

In the absolute region `Re s>1`, define

`R_y(s,z)=[prod_{p>y}(1+z p^-s)-1]/z`.

Then

`R_y(s,0)=P_y(s)=sum_{p>y}p^-s`.

At `z=-1`,

`1/(k-1)! partial_z^(k-1)R_y(s,-1)`
`=(-1)^k Q_k(s;y)`,

where

`Q_k(s;y)=sum_{n>1,P^-(n)>y}`
` mu(n) C(omega(n)-1,k-1)n^-s`.

Hence the complete Taylor identity is

`P_y(s)=sum_{k>=1}(-1)^k Q_k(s;y)`.

The K-term remainder has the exact arity expansion

`Rem_K(s)=sum_{m>K}(-1)^(m+K-1)`
` C(m-2,K-1)e_m(s;y)`,

with `e_m` the mth elementary symmetric sum over rough primes.

For real

`a=1+1/logx`, `y=(logx)^2`,

let `lambda=sum_{p>y}p^-a~loglogx`. Since

`e_m<=lambda^m/m!`,

one obtains

`|Rem_K(a)|<=e^lambda lambda^(K+1)/(K+1)!`.

At

`K=floor(logx/(2loglogx))`,

`|Rem_K(a)|=x^(-1/2+o(1)).`

Interpretation:

**the first RH-critical-depth higher-duality jets extract the primitive-prime channel from the parity Euler object with square-root-size absolute Taylor remainder on the Perron side `s≈1`.**

Critical warning:

`PERRON_SIDE_SQRT_TAYLOR_REMAINDER != DIRECT_CONTROL_AT Re(s)=1/2`.

The rough Euler product is not absolutely defined at the critical line, and this calculation must not be used as an RH proof.

---

## 10. Structural synthesis

The current route now has the following exact interfaces:

1. Dickman delay Green operator has one algebraic dominant mode.
2. Continuum parity is the subdominant Dickman branch.
3. Tenenbaum supplies unconditional first depth-moment annihilation.
4. Alladi higher duality supplies a complete measure-valued hierarchy.
5. K layers form an exact primitive selector, cancelling composite provenance up to arity K.
6. At `K~(1/2)logx/loglogx`, the remaining high-arity capacity is already square-root size.
7. The critical prime source can be represented internally by the first K ordered factor coordinates with square-root truncation error.
8. Factorial normalization shows that pure high-k combinatorics are not by themselves fatal.
9. The collective Taylor hierarchy reaches the primitive-prime channel; termwise fixed-k identities remain zero-transparent.

Thus the remaining obstruction is no longer “do we have enough moments?” or “can X6 represent enough factors?”. It is:

**prove RH-strength collective control of the first K ordered-factor / divisor-BRC discrepancy, without assuming square-root prime discrepancy and without collapsing provenance into fixed-k scalar moments.**

---

## 11. Next smallest research unit

Define the critical ordered-factor discrepancy

`Delta_K(X;Y)`
`=(1/X)sum_{n<=X}sum_{k<=K}`
` sqrt(P_k(n))1_{P_k(n)<=Y}`
`-int_2^Y dt/(sqrt(t)logt)`,

with

`Y=(logX)^2`, `K=floor(logX/(2loglogX))`.

By Section 7,

`Delta_K(X;Y)=J_1/2(Y)+O(X^-1/2+o(1)).`

The next research target is to apply the Alladi measure transform before averaging over n, retain the full triangular `(k,p)` provenance table, and search for an operation-safe cancellation or collision inequality across k. Any scalarization that leaves an explicit `1/zeta(s)` factor is zero-transparent and should be rejected.

No RH proof is claimed.