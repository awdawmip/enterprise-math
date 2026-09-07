# RH critical Alladi-Pascal frame and ordered-prime edge BRC

Status: `RESEARCH FRONTIER / EXACT IDENTITIES + OPERATION-SAFE NO-GO + FINITE CHECKER / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / Alladi higher duality / ordered prime factors / BRC / X6 fixed-width growing-depth provenance`
Parent frontier:

- `RH_GREEN_ALLADI_CRITICAL_PRIMITIVE_SOURCE_PORT_20260906.md`
- `RH_DICKMAN_PARITY_RESOLVENT_CRITICAL_DEPTH_20260906.md`

Public identity source: K. Alladi and S. Sengupta, *Duality Between Prime Factors and the Prime Number Theorem for Arithmetic Progressions — Higher Order Dualities*, arXiv:2604.17832 (2026), especially their general duality identity (1.10).

## 0. Typing and prior-art guard

P000 is unchanged. Ordered prime rank, prime label, arithmetic size, and divisor-subset arity are arithmetic provenance coordinates. They are not new native X6 spatial axes.

BRC discipline is mandatory:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

The Alladi higher-order duality and the Pascal/binomial transform are classical/prior mathematics. The contribution of this note is the exact collective packaging, the critical-depth conditioning/state-budget analysis, the operation-safe observer no-go, and the ordered-prime edge carrier selected for the next RH step. No generic novelty claim is made before a broader literature audit.

Tool-reuse resolution:

`COMPOSE_APPLIED`.

The existing project `ALLADI_ORDER_STATISTIC_BRC_TRANSFORM` is composed with the existing critical-depth and BRC observer interfaces. No new top-level BRC family is introduced.

---

## 1. Collective Alladi polynomial

Let the distinct prime factors of `n>1` be ordered as

`P_1(n)>P_2(n)>...>P_r(n)`, where `r=omega(n)`,

and let `p_1(d)` denote the least prime factor of `d`. For any complex-valued function `f` on the primes, define

`A_{n,f}(z)`
`= sum_{1<d|n} mu(d)(1+z)^(omega(d)-1) f(p_1(d)).`

Only `rad(n)` matters in this expression.

Alladi's general higher-order duality states

`sum_{1<d|n} mu(d) C(omega(d)-1,k-1) f(p_1(d))`
`= (-1)^k f(P_k(n)).`

Expanding `(1+z)^(omega(d)-1)` and applying the identity coefficientwise gives the exact finite polynomial law

`A_{n,f}(z)`
`= - sum_{k=1}^r (-z)^(k-1) f(P_k(n)).`

Freeze:

`SIGNED_DIVISOR_SUBSET_CLOUD <-> ORDERED_PRIME_FACTOR_POLYNOMIAL`.

This is a lossless relation. It retains both prime label/size and ordered-factor rank.

Special observers are:

- `A_{n,f}(0)=-f(P_1(n))`, the largest-prime observer;
- `A_{n,f}(-1)=-sum_{p|n}f(p)`, the full prime-support source;
- polynomial coefficients are the complete ordered-factor vector with alternating signs.

Thus the full higher-duality hierarchy is one polynomial carrier, not an unrelated list of fixed-k moments.

---

## 2. Factorial jets and the exact Pascal frame

Put

`u_k(n;f)=f(P_{k+1}(n))`, for `0<=k<r`,

and define the factorial jets at the full-support endpoint `z=-1` by

`j_m(n;f)=(1/m!) partial_z^m A_{n,f}(-1)`, for `0<=m<r`.

Differentiating the divisor form at `z=-1` selects exactly one divisor arity:

`j_m(n;f)`
`= sum_{1<d|n, omega(d)=m+1} mu(d) f(p_1(d)).`

Differentiating the ordered-prime form gives

`j_m`
`= (-1)^(m+1) sum_{k=m}^{r-1} C(k,m) u_k.`

Binomial inversion gives the exact inverse

`u_k`
`= (-1)^(k+1) sum_{m=k}^{r-1} C(m,k) j_m.`

Let `P_r` be the upper Pascal matrix

`(P_r)_{m,k}=C(k,m)` for `m<=k`, and zero otherwise.

Then, up to diagonal sign matrices,

`j=P_r u`.

Its inverse has entries

`(P_r^-1)_{m,k}=(-1)^(k-m)C(k,m)`.

Consequently:

- `det(P_r)=1`;
- the transform is integer-unimodular;
- it is exactly invertible over every characteristic-zero coefficient field;
- the inverse has the same entrywise absolute values.

Freeze:

`ALLADI_DIVISOR_JETS_AND_ORDERED_FACTORS = TWO_BASES_OF_ONE_EXACT_BRC_STATE`.

No provenance is lost when the whole vector is retained.

---

## 3. Critical-depth conditioning is subpolynomial

The Frobenius norm identity

`||P_r||_F^2`
`= sum_{k=0}^{r-1} sum_{m=0}^k C(k,m)^2`
`= sum_{k=0}^{r-1} C(2k,k)`

gives

`||P_r||_2, ||P_r^-1||_2 <= sqrt(r) 2^(r-1)`

and hence

`cond_2(P_r) <= r 4^(r-1).`

At the RH critical depth, write

`L=log X`, `ell=loglog X`,

`Y=L^2`,

`K=floor(L/(2ell)).`

Then

`K 4^K = X^o(1)`

and

`cond_2(P_K)=X^o(1).`

Therefore the collective Alladi transform at the critical depth is not polynomially ill-conditioned. Raw binomial/factorial coefficients look large termwise, but the full exact basis change costs only a subpolynomial factor on the power scale relevant to RH.

Important population split:

- for `omega(n)<=K`, use the full exact rank-r frame, padded by zero to K coordinates;
- for `omega(n)>K`, retain a separate high-arity repair fiber.

The parent frontier already gives

`#{n<=X:omega(n)>K}<=X^(1/2+o(1)).`

For

`f_Y(p)=sqrt(p) 1_{p<=Y}`,

each such integer contributes at most

`omega(n)sqrt(Y)=O((log X)^2)`.

Hence the normalized high-arity repair contribution is

`X^(-1/2+o(1)).`

It is an RH-scale residual and must not be folded into the first K jets.

Freeze:

`TRUNCATED_JETS_WITHOUT_HIGH_ARITY_REPAIR = INFORMATION LOSS`.

---

## 4. Exact Hardy/Parseval energy law

Because the coefficients of `A_{n,f}` are the ordered-prime weights up to signs,

`(1/(2pi)) int_0^(2pi) |A_{n,f}(e^(i theta))|^2 dtheta`
`= sum_{k=1}^r |f(P_k(n))|^2`
`= sum_{p|n}|f(p)|^2.`

Averaging over `n<=X` and double-counting divisibility gives the exact identity

`(1/X) sum_{n<=X} ||A_{n,f}||_(H^2)^2`
`= sum_{p<=X}|f(p)|^2 floor(X/p)/X.`

For `f=f_Y`,

`(1/X) sum_{n<=X} ||A_{n,f_Y}||_(H^2)^2`
`= sum_{p<=Y} p floor(X/p)/X`
`<= pi(Y)`
`<= Y`
`= (log X)^2.`

Combining this with the Pascal bound gives, on the low-arity population,

`(1/X)sum_{n<=X,omega(n)<=K} ||j(n;f_Y)||_2^2`
`<= K4^(K-1)(log X)^2`
`= X^o(1).`

The inverse frame has the same bound.

Thus the complete critical-depth divisor-jet carrier has subpolynomial average quadratic energy and subpolynomial frame distortion. There is no hidden polynomial explosion in retaining the full Alladi/BRC vector.

This is a stability statement, not cancellation:

`SUBPOLYNOMIAL_FRAME_ENERGY != RH_SIGNED_SAVING`.

Evaluation at `z=-1` still reads the coherent full-support mode

`-A_{n,f}(-1)=sum_{p|n}f(p).`

---

## 5. The `(k,p)` light cone and the exact critical corner

Define the ordered-prime incidence table

`T_X(k,p)`
`= (1/X) #{n<=X : P_k(n)=p}.`

It satisfies two exact laws.

### Column conservation

Every integer divisible by `p` places `p` at exactly one ordered-prime rank, so

`sum_{k>=1} T_X(k,p)=floor(X/p)/X.`

### Support light cone

If `P_k(n)=p`, then `n` contains `k` distinct primes at least `p`; therefore

`p^k<=n<=X`.

Hence

`T_X(k,p)=0` whenever `p^k>X`.

A useful positive envelope is

`T_X(k,p)`
`<= (1/p) lambda_X(p)^(k-1)/(k-1)!`,

where

`lambda_X(p)=sum_{p<q<=X}1/q`.

This follows by choosing the `k-1` larger distinct prime divisors and bounding the corresponding elementary symmetric sum by its factorial-moment majorant.

Now use the critical choices `Y=(log X)^2` and `K=floor(log X/(2loglog X))`. They satisfy exactly

`Y^K<=X<Y^(K+1).`

Thus the rectangle

`1<=k<=K`, `p<=Y`

touches the arithmetic support light cone at its upper-right corner. The Hildebrand cutoff and the Alladi depth are conjugate coordinates of the same product constraint.

The number of vertex coordinates is at most

`K pi(Y) <= KY = O((log X)^3/loglog X)=X^o(1).`

So retaining every prime label `p<=Y` and every critical rank `k<=K` is compatible with a subpolynomial state budget. There is no power-scale reason to erase prime labels here.

Freeze:

`RH_CRITICAL_KP_CARRIER_SIZE = X^o(1)`.

This is a representation-size statement, not a fast-construction algorithm.

---

## 6. Exact rank-one longitudinal mode and a k-only no-go

For any prime test function `f`, the table source is

`S_X(f)`
`= sum_p f(p) sum_k T_X(k,p)`
`= sum_p f(p) floor(X/p)/X.`

For a finite K-table, split off the high-rank leakage as an explicit repair coordinate. On the low-arity population the source depends only on the column-sum vector

`c_p=sum_k T_X(k,p).`

Write the table as

`T = (1/K) 1_K c^T + T_perp`,

where `1_K^T T_perp=0`.

Then `S_X(f)` reads only the rank-one longitudinal component `(1_K)c^T`; all transverse rank fluctuations are invisible to this observer.

Consequences:

1. If a map acts separately inside every fixed-p column and preserves column totals, it leaves `S_X(f)` exactly invariant.
2. If the map is invertible, such as a full Pascal basis change, the source is merely represented by the transformed left functional; no saving has occurred.
3. If a quotient deletes the column total, it is not operation-safe for the family of prime-source observers unless the total is retained as a repair coordinate.

Therefore:

`K_ONLY_FOURIER_PASCAL_KRAWTCHOUK_MIXING -> NO_PRIME_SOURCE_POWER_SAVING_BY_ITSELF`.

This is the table-side version of the rank-one obstruction: the difficult prime-location source is a coherent longitudinal mode, not a high-k conditioning problem.

The result does not say that the Alladi transform is useless. It says the transform must be composed with a mechanism that also acts on prime label/size or on adjacent ordered-prime provenance.

---

## 7. Minimal dynamical repair: ordered-prime edge BRC

The vertex table loses adjacency along each integer's ordered-prime path. Define the edge carrier

`E_X(k;p,q)`
`= (1/X) #{n<=X : P_k(n)=p, P_(k+1)(n)=q}`

for `p>q`, and the terminal carrier

`B_X(k,p)`
`= (1/X) #{n<=X : omega(n)=k, P_k(n)=p}.`

They obey exact path-continuity laws:

`T_X(k,p)=sum_{q>p} E_X(k-1;q,p)` for `k>=2`,

and

`T_X(k,p)=sum_{q<p} E_X(k;p,q)+B_X(k,p)` for every `k>=1`.

For one ordered path

`p_1>p_2>...>p_r`

and arbitrary `f`, discrete integration by parts gives

`sum_{j=1}^r f(p_j)`
`= r f(p_r)`
` + sum_{j=1}^{r-1} j (f(p_j)-f(p_(j+1))).`

Averaging yields the exact source decomposition

`S_X(f)`
`= sum_{k,p} k f(p) B_X(k,p)`
` + sum_{k,p>q} k(f(p)-f(q)) E_X(k;p,q).`

This is the first carrier in the current route that simultaneously preserves:

- ordered-factor depth;
- prime label/size;
- adjacent provenance;
- the exact full-support source;
- a local continuity law.

Project interface name:

`ORDERED_PRIME_EDGE_BRC`.

It is not a new native space and is not yet a cancellation theorem.

### Observer-specific compression at the critical cutoff

For

`f_Y(p)=sqrt(p)1_{p<=Y}`,

edges with both endpoints above Y have zero weight. An edge from `p>Y` to `q<=Y` has weight

`f_Y(p)-f_Y(q)=-sqrt(q)`,

independent of the exact value of p. Therefore all above-Y predecessors can be combined into one typed boundary port `HIGH_Y`, while:

- every low-low edge `p>q`, `p,q<=Y`, is retained;
- every terminal label `p<=Y` is retained;
- every high-to-low entry is retained by `(k,q,HIGH_Y)`.

This quotient is operation-safe for the declared `f_Y` observer. Its coordinate budget is at most

`O(K pi(Y)^2)=O((log X)^5/loglog X)=X^o(1).`

Thus even the minimal joint edge repair remains subpolynomial at the critical scale.

---

## 8. What has and has not advanced

### Exact advances

1. The whole Alladi hierarchy is one finite polynomial carrier.
2. Ordered-prime values and divisor-arity Möbius jets are related by an integer-unimodular Pascal frame.
3. At RH critical depth the frame condition number is `X^o(1)`.
4. The complete low-arity jet carrier has `X^o(1)` average H2 energy.
5. The critical `(k,p)` rectangle is exactly the product light-cone corner `Y^K<=X<Y^(K+1)`.
6. The vertex and observer-adapted edge carriers both have `X^o(1)` coordinate budgets.
7. The prime source lies in one column-sum longitudinal mode, proving a k-only transformation no-go.
8. The ordered-prime edge carrier supplies an exact depth-label continuity equation and an exact path integration-by-parts formula.

### Boundaries

- A well-conditioned basis change is not signed cancellation.
- Small coordinate count is not a fast algorithm.
- Positive H2 energy does not imply decay of the coherent longitudinal mode.
- The edge identity rewrites the source but does not yet bound its discrepancy.
- No estimate proved here improves the known zero-free-region bound or proves RH.

---

## 9. Exact checker

Task-local checker:

`experiments/rh_alladi_pascal_ordered_prime_frame_check.py`.

It verifies, using only Python's standard library:

- the collective Alladi polynomial identity through rank 9;
- the divisor-jet/Pascal transform and exact inverse;
- Pascal matrix inversion through rank 12;
- the exact averaged Hardy/Parseval law;
- column conservation and the support light cone;
- edge continuity;
- path integration by parts.

The finite checker is a regression certificate for the identities, not evidence for an asymptotic theorem.

---

## 10. New smallest research unit

The representation problem is now essentially closed at power scale: the necessary critical carrier is lossless, subpolynomially conditioned, and has subpolynomial coordinate count.

The unresolved problem is a dynamical discrepancy estimate.

Construct a continuous Dickman/prime-density edge carrier

`(E_X^cont, B_X^cont)`

with the same boundary/divergence semantics as `(E_X,B_X)`, and study the signed difference under the exact functional

`L_f(E,B)`
`= sum k f(p)B(k,p)`
` + sum k(f(p)-f(q))E(k;p,q).`

The first target should be weaker than RH:

prove any fixed power gain over the generic longitudinal estimate for the discrete-minus-continuous edge flux, while retaining the high-arity repair and the `HIGH_Y` boundary port.

A valid mechanism must couple rank with prime scale/ratio. It must not:

- act only in k;
- erase prime labels;
- replace the high-arity tail by zero;
- take absolute values before the edge divergence;
- interpret positive edge capacity as Möbius cancellation;
- assume square-root control of `theta(t)-t`.

Candidate next state:

`(k, log(p/q), q, boundary_type, multiplicity/provenance)`,

implemented as fixed X6 local ports composed over growing depth.

No RH proof is claimed.
