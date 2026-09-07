# RH critical Kubilius suffix coupling, rough-prefix shift, and intensity barrier

Status: `RESEARCH FRONTIER / PRIOR-ART COUPLING + EXACT BRC FACTORIZATION + NO-GO / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / Kubilius model / ordered prime factors / Alladi polynomial / BRC / rough-smooth coupling`
Parent frontier:

- `RH_ALLADI_PASCAL_FRAME_ORDERED_PRIME_EDGE_BRC_20260907.md`
- `RH_GREEN_ALLADI_CRITICAL_PRIMITIVE_SOURCE_PORT_20260906.md`
- `RH_DICKMAN_PARITY_RESOLVENT_CRITICAL_DEPTH_20260906.md`

Public coupling source:

- O. Gorodetsky, *A Kubilius model for sieve-theoretic sequences*, arXiv:2608.14190 (2026), especially the review of Tenenbaum's optimal classical bound and Corollary 2.1.

## 0. Typing and reuse guard

P000 remains unchanged. The small-prime support, rough-prefix depth, prime labels, and product budget below are arithmetic provenance coordinates, not new native X6 axes.

BRC discipline:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

Tool/interface resolution:

`COMPOSE_APPLIED`.

This note composes the existing Alladi ordered-factor carrier, critical-depth cutoff, and BRC observer policy with the classical Kubilius coupling. The Kubilius theorem is prior art. The exact prefix-shift factorization, observer audit, independent edge formulas, and resulting bottleneck classification are project-derived packaging. No generic novelty claim is made.

---

## 1. Kubilius coupling reaches the RH square-root scale at the critical cutoff

Let `N_X` be uniform on the integers `1,...,X`. For every prime `p<=Y`, let

`I_p(N_X)=1_{p|N_X}`.

Let `(B_p)_{p<=Y}` be independent Bernoulli variables with

`P(B_p=1)=1/p`.

The classical Kubilius model, in Tenenbaum's optimal form as summarized in the 2026 source above, gives for every fixed `epsilon>0`

`d_TV((nu_p(N_X))_{p<=Y}, (Geom_p)_{p<=Y})`
`<<_epsilon u^(-u)+X^(-1+epsilon),`

where

`u=log X/log Y`.

Passing from valuations to Boolean support cannot increase total variation, hence the same bound holds for `(I_p)_{p<=Y}` and `(B_p)_{p<=Y}`.

Use the RH-critical cutoff

`Y=(log X)^2`.

Writing

`L=log X`, `ell=loglog X`,

gives

`u=L/(2ell)`

and exactly

`u log u`
`= L/2 - L log(2ell)/(2ell).`

Therefore

`u^(-u)`
`= X^(-1/2 + log(2ell)/(2ell))`
`= X^(-1/2+o(1)).`

Thus

`d_TV((I_p)_{p<=Y},(B_p)_{p<=Y})`
`<< X^(-1/2+o(1))`

in the usual power-scale sense.

Freeze:

`CRITICAL_SMALL_PRIME_SUPPORT -> INDEPENDENT_BERNOULLI_MODEL + RH_SCALE_TV_DEFECT`.

This is an unconditional coupling theorem for the declared small-prime support observer. It is not RH.

---

## 2. Suffix-reindexed and global ordered-factor polynomials

Fix a prime test function supported on `p<=Y`. For an integer `n`, split its distinct prime support into:

- a rough prefix `R_Y(n)={p|n:p>Y}`;
- a small-prime suffix `S_Y(n)={p|n:p<=Y}`.

Put

`h_Y(n)=#R_Y(n).`

Order the small suffix as

`Q_1(n)>Q_2(n)>...>Q_s(n).`

Define the suffix-reindexed polynomial

`U^suf_{n,f}(w)`
`= sum_{j=1}^s f(Q_j(n)) w^(j-1).`

Define the global-rank polynomial

`U^glob_{n,f}(w)`
`= sum_{k>=1} f(P_k(n)) w^(k-1).`

Because every rough prime precedes every small prime in decreasing order,

`U^glob_{n,f}(w)=w^(h_Y(n)) U^suf_{n,f}(w).`

For the corresponding Alladi polynomial

`A_{n,f}(z)=-U_{n,f}(-z),`

this becomes the exact factorization

`A^glob_{n,f}(z)`
`= (-z)^(h_Y(n)) A^suf_{n,f}(z).`

This is a serial-composition law:

`ROUGH_PREFIX_SHIFT x SMALL_PRIME_SUFFIX_STATE -> GLOBAL_ORDERED_FACTOR_STATE`.

At the critical cutoff, if `K=floor(log X/(2loglog X))`, then

`Y^(K+1)>X`.

Since each rough prime is greater than Y, every `n<=X` satisfies

`h_Y(n)<=K.`

So the rough-prefix shift has exactly the same growing depth scale as the critical Alladi frame.

---

## 3. Endpoint, parity, and jet consequences

The prefix factor behaves differently under different observers.

### Full-support endpoint

At `z=-1`,

`(-z)^h=1`,

so

`A^glob_{n,f}(-1)=A^suf_{n,f}(-1)`
`=-sum_{p|n,p<=Y}f(p).`

The full-support source is completely blind to the rough-prefix depth.

### Opposite endpoint

At `z=1`,

`A^glob_{n,f}(1)=(-1)^(h_Y(n)) A^suf_{n,f}(1).`

Thus the same carrier reads rough-prefix parity as an exact modulation at the opposite endpoint.

### Factorial jets

Put `t=1+z`. Then `-z=1-t`. If

`j_m^glob=(1/m!) partial_z^m A^glob(-1)`

and `j_m^suf` is defined similarly, coefficient multiplication gives

`j_m^glob`
`= sum_{a=0}^{min(h_Y,m)}`
`  (-1)^a C(h_Y,a) j_(m-a)^suf.`

The rough prefix acts on the suffix jet vector by a signed Pascal convolution. This is an exact BRC provenance action, not an analogy.

Freeze:

`GLOBAL_JET = ROUGH_PREFIX_BINOMIAL_SHIFT(SUFFIX_JET)`.

---

## 4. H2 energy is exactly blind to the rough-prefix shift

On the unit circle,

`|(-z)^(h_Y)|=1`.

Therefore

`||A^glob_{n,f}||_(H^2)`
`= ||A^suf_{n,f}||_(H^2)`

exactly.

Equivalently, the global coefficient vector is obtained by inserting `h_Y` leading zero ranks before the suffix coefficients, so its squared coefficient norm is unchanged.

This yields a sharp observer no-go:

`H2_ENERGY_CANNOT_DETECT_ROUGH_PREFIX_RANK_SHIFT`.

The previous Hardy/Parseval bound is still valid and useful for stability, but by itself it cannot control the missing prefix/suffix coupling. The difficult information lives in phase/rank placement, not in coefficient energy.

This is another instance of the BRC rule:

`SAME_POSITIVE_ENERGY != SAME_PROVENANCE`.

---

## 5. Polynomial-valued independent suffix carrier

The suffix-reindexed state is a deterministic function of the small-prime Boolean vector, so the Kubilius coupling applies directly to it.

For

`f_Y(p)=sqrt(p)1_{p<=Y}`

and `|z|<=1`,

`|A^suf_{n,f_Y}(z)|`
`<= sum_{p<=Y,p|n}sqrt(p)`
`<= pi(Y)sqrt(Y)`
`<= Y^(3/2)`
`= (log X)^3.`

Hence total variation gives the uniform polynomial-value coupling

`sup_{|z|<=1}`
`| E_X A^suf_{N_X,f_Y}(z)`
` - E_B A^suf_{B,f_Y}(z) |`
`= X^(-1/2+o(1)).`

Here `E_B` is expectation in the independent Bernoulli support model.

The independent expectation is explicit. For an arbitrary f on primes `<=Y`,

`E_B A^suf_f(z)`
`= - sum_{p<=Y} f(p)/p`
`    prod_{p<q<=Y} (1-(1+z)/q).`

Proof: in the divisor-subset form, group each nonempty selected divisor subset by its least prime p and sum independently over its possible larger prime members.

Special cases:

- `z=-1` gives `-sum_{p<=Y}f(p)/p`;
- `z=0` gives the expected largest selected small-prime weight;
- `z=1` inserts the small-prefix parity products `prod_{q>p}(1-2/q)`.

Thus the complete suffix polynomial, not only a scalar moment, has an RH-scale independent approximation on the closed unit disk.

Important boundary:

The coupling does **not** approximate the global polynomial away from `z=-1`, because the latter also contains the rough-prefix modulation `(-z)^(h_Y)`. That joint variable must be retained.

---

## 6. Explicit independent ordered-prime edge carrier

Let

`Phi_{>p}(w)`
`= prod_{p<r<=Y} (1-1/r+w/r).`

In the independent model, the suffix-rank vertex table is

`T_B(k,p)`
`= (1/p) [w^(k-1)] Phi_{>p}(w).`

For `p>q`, the consecutive-edge table is

`E_B(k;p,q)`
`= (1/(pq))`
`  prod_{q<r<p}(1-1/r)`
`  [w^(k-1)] Phi_{>p}(w).`

The terminal table is

`B_B(k,p)`
`= (1/p)`
`  prod_{r<p}(1-1/r)`
`  [w^(k-1)] Phi_{>p}(w).`

These formulas have direct meanings:

- choose exactly `k-1` selected primes larger than p;
- select p;
- for an edge to q, select q and forbid every intermediate prime;
- for a terminal at p, forbid every smaller prime.

They satisfy exactly:

`sum_k T_B(k,p)=1/p,`

`T_B(k,p)=sum_{q>p}E_B(k-1;q,p)` for `k>=2`,

and

`T_B(k,p)=sum_{q<p}E_B(k;p,q)+B_B(k,p).`

They also satisfy the ordered-path integration-by-parts identity from the parent frontier.

Consequently the small-prime suffix vertex/edge geometry is explicitly solved under the independent carrier.

---

## 7. The intensity barrier survives independence unchanged

At the full-support endpoint,

`E_B[-A^suf_f(-1)]`
`= sum_{p<=Y}f(p)/p.`

For actual integers,

`E_X[-A^suf_f(-1)]`
`= sum_{p<=Y}f(p) floor(X/p)/X.`

Therefore

`|E_X[-A^suf_f(-1)]-E_B[-A^suf_f(-1)]|`
`<= (1/X)sum_{p<=Y}|f(p)|.`

For `f=f_Y`, this is

`O(Y^(3/2)/X)=X^(-1+o(1)),`

which is even smaller than the general total-variation error.

The continuous prime-density comparison is instead

`I_Y(f)=int_2^Y f(t)/(t log t) dt.`

For `f(t)=sqrt(t)`,

`sum_{p<=Y}f(p)/p-I_Y(f)`
`= sum_{p<=Y}p^(-1/2)`
`  - int_2^Y dt/(sqrt(t)log t)`
`= J_(1/2)(Y).`

Thus the critical source remains exactly after every small-prime support correlation has been replaced by independence.

In Bernoulli-chaos language,

`sum_{p<=Y}f(p)B_p`
`= sum_{p<=Y}f(p)/p`
` + sum_{p<=Y}f(p)(B_p-1/p).`

The centered random fluctuation has mean zero. The prime intensity term is deterministic and contains the full discrete-versus-continuous source discrepancy.

Freeze:

`KUBILIUS_INDEPENDENCE_REMOVES_SMALL_PRIME_CORRELATION, NOT PRIME_INTENSITY_DISCREPANCY`.

Therefore:

`SMALL_PRIME_INTERNAL_CORRELATION != RH_CRITICAL_SOURCE`.

Any claimed RH gain obtained only by decorrelating small-prime divisibility is incomplete.

---

## 8. Conditional rough-branch profile and the late-source barrier

The unconditional suffix law is not the whole RH problem. In a divisor-BRC expansion, fix a Y-rough divisor `a` and restrict to the branch `a|n`.

Writing `n=am`, the small-prime support of n is exactly the small-prime support of m, because every prime divisor of a exceeds Y. As n ranges over multiples of a up to X, m is uniform up to

`U_a=floor(X/a).`

When `U_a>=Y`, Kubilius gives a branchwise coupling with residual depth

`u_a=log(X/a)/log Y`

and error of scale

`u_a^(-u_a)+(X/a)^(-1+epsilon).`

If `a=X^(alpha+o(1))`, then

`u_a=(1-alpha)L/(2ell)+o(L/ell)`

and

`u_a^(-u_a)=X^(-(1-alpha)/2+o(1)).`

Thus:

- the root branch `a=1` has the full `X^(-1/2+o(1))` coupling;
- later rough branches have progressively weaker coupling;
- the boundary `a>X/Y` has residual depth below one and is outside this small-prime coupling regime.

This is the probabilistic version of the late-source problem already found in the Dickman Green analysis.

A rough-divisor arity

`h=omega(a)`

does not determine `u_a`. Even for fixed h, the product a can range across many scales. Therefore:

`ROUGH_ARITY_WITHOUT_ROUGH_PRODUCT_SIZE = NON_OPERATION_SAFE`.

The necessary repair coordinate is the residual logarithmic budget

`u_a=log(X/a)/log Y`

or equivalently the exact product a.

This is closely analogous to the existing X6 rule that a quotient coordinate needs its lost common-depth repair coordinate to recover native distance.

---

## 9. Semidirect BRC architecture

The critical factor state now separates into:

1. a small-prime suffix path, modeled independently up to RH-scale total variation;
2. a rough branch carrying:
   - exact/significant product scale a;
   - rough arity/parity `omega(a)`;
   - residual budget `u_a`;
3. a semidirect action on the suffix polynomial:
   `A^suf(z) -> (-z)^(omega(a))A^suf(z)`.

This gives the typed architecture

`ROUGH_PREFIX_SCALE_AND_PARITY`
`  semidirect_action`
`SMALL_PRIME_KUBILIUS_EDGE_BRC`.

X6 width remains fixed. The rough action is realized through a composite provenance path of depth at most K, not through new spatial axes.

The result also explains the previous rank-one observations:

- H2 sees suffix energy but erases the monomial shift;
- the endpoint `z=-1` erases rough-prefix depth;
- `z=1` sees rough parity;
- the continuous prime source survives as the one-point intensity mode.

---

## 10. Exact checker

Task-local checker:

`experiments/rh_kubilius_suffix_prefix_shift_check.py`.

It verifies with exact integers and rational arithmetic:

- global polynomial = rough-prefix monomial shift × suffix polynomial;
- the induced factorial-jet binomial convolution;
- H2 isometry under the shift;
- the independent expected suffix polynomial formula;
- independent vertex, edge, and terminal formulas;
- column conservation and edge continuity;
- ordered-path integration by parts.

It does not attempt to numerically certify the asymptotic total-variation theorem.

---

## 11. New smallest research unit

The small-prime suffix is no longer the opaque part. For the current observer class, its entire dependence structure is replaceable by an explicit independent edge carrier at the RH square-root error scale.

The unresolved unit is now the signed sum of **conditional rough-branch coupling defects**.

For a bounded suffix observer F, define

`D_a(F)`
`= E_{m<=X/a} F((1_{p|m})_{p<=Y})`
` - E_B F((B_p)_{p<=Y}).`

The known pointwise majorant is controlled by `u_a^(-u_a)`, but taking absolute values over the rough-divisor branches loses the Möbius cancellation sought.

The next target is to retain the signed rough-divisor provenance and prove cancellation in a quantity of the schematic form

`sum_{a Y-rough} mu(a) W_X(a) D_a(F),`

where the exact weight `W_X(a)` must be derived from the selected rough/smooth or Alladi expansion before any estimate is attempted.

A successful estimate must:

- keep `a` or `u_a`, not only `omega(a)`;
- keep the high/late boundary `a>X/Y`;
- exploit the semidirect phase `(-z)^(omega(a))`;
- avoid replacing `D_a` by its absolute majorant;
- avoid reintroducing `J_(1/2)` as an assumed square-root prime-discrepancy bound.

This is the first remaining location where a new signed BRC mechanism could act without contradicting the current no-go results.

No RH proof is claimed.
