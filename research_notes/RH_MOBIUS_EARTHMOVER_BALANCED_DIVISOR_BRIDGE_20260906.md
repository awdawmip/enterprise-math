# Möbius earthmover / balanced-divisor bridge for RH

Status: `RESEARCH FRONTIER / EXACT REFORMULATIONS + PRIOR-ART-DEPENDENT CAPACITY INPUT / NOT A PROOF OF RH`
Date: `2026-09-06`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / Riesz / Pair-BRC / X6 / divisor geometry / dense divisibility`

## 0. Typing guard

P000 remains unchanged. The arithmetic-value line used below is an ordering/transport fiber on integer Cells, not a new native X6 axis and not a replacement for the six native spatial directions.

BRC discipline is mandatory:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

Positive transport capacity and signed Möbius orientation are distinct objects.

---

## 1. Canonical positive/negative Möbius Cell streams

Let

- `a_1<a_2<...` be the positive squarefree Cells with `mu(a_j)=+1`,
- `b_1<b_2<...` be the negative squarefree Cells with `mu(b_j)=-1`.

Pair equal ranks:

`a_j <-> b_j`.

Write

`A(t)=#{j:a_j<=t}`, `B(t)=#{j:b_j<=t}`.

Since zero Möbius values are excluded from both streams,

`M(t)=A(t)-B(t)`.

### Exact cut-flux identity

For every cut `t`, the number of monotone rank-pair segments crossing the cut equals

`|A(t)-B(t)|=|M(t)|`.

Indeed, if `A(t)>B(t)`, the first `B(t)` pairs have both endpoints on the left of the cut, the next `A(t)-B(t)` positive endpoints have their negative partners on the right, and all later pairs have both endpoints on the right. The other sign is symmetric.

Thus if

`W(X):=sum_j length([a_j,b_j] intersect [X,2X])`,

then exactly

`W(X)=int_X^{2X}|M(t)| dt`

(up to the immaterial integer/continuous endpoint convention).

This is a fully positive quantity after the two sign streams have been defined.

---

## 2. RH as an L1 earthmover criterion

### Theorem (exact equivalent reformulation)

For every `epsilon>0`,

`RH <=> W(X)=O_epsilon(X^(3/2+epsilon))`.

Equivalently,

`RH <=> int_X^{2X}|M(t)|dt = O_epsilon(X^(3/2+epsilon))`.

### Proof: RH => transport bound

The classical Mertens equivalent of RH gives

`M(t)=O_epsilon(t^(1/2+epsilon))`.

Integrating over `[X,2X]` gives the claimed `X^(3/2+epsilon)` bound.

### Proof: transport bound => RH

Assume the dyadic L1 bound for every epsilon. Fix `sigma>1/2` and choose `epsilon<sigma-1/2`. On the dyadic block `[2^k,2^(k+1)]`,

`int |M(t)| t^(-sigma-1) dt`

is at most

`2^(-k(sigma+1)) * O(2^(k(3/2+epsilon)))`

`=O(2^(-k(sigma-1/2-epsilon)))`.

Hence

`int_1^infinity |M(t)|t^(-sigma-1)dt < infinity`

for every `sigma>1/2`.

The standard partial-summation representation

`1/zeta(s)=s int_1^infinity M(t)t^(-s-1)dt`

therefore extends holomorphically to `Re(s)>1/2`. Thus zeta has no zero in that half-plane, and the functional equation forces all nontrivial zeros onto `Re(s)=1/2`.

This is an equivalent reformulation, not a proof.

---

## 3. One-dimensional flow conservation no-go

The rank pairing above is not merely one candidate matching.

On the arithmetic-value line, any transport sending all positive Möbius unit charges to negative Möbius unit charges has net flow through the cut `(t,t+1)` equal to `M(t)` by conservation of charge.

Therefore every L1-distance transport has cost at least

`sum_t |M(t)|`,

while the monotone rank matching attains equality.

Freeze:

`SEARCHING_FOR_A_BETTER_PAIRING != RH_PROGRESS`.

The pairing algorithm cannot reduce the cut flux. The only possible mathematical progress is to estimate the conserved flux itself by exploiting multiplicative/factor provenance.

In BRC language, `|M(t)|` is the mandatory multiplicity of open signed provenance strands through the arithmetic-order cut.

---

## 4. Riesz interface to the earthmover flux

Let

`w_x(n)=n^(-2) exp(-x/n^2)`

and

`P_2(x)=sum_n mu(n)w_x(n)`.

The rank pairing gives absolutely

`P_2(x)=sum_j (w_x(a_j)-w_x(b_j))`.

By the fundamental theorem of calculus along each pair segment and the cut-flux identity,

`|P_2(x)| <= int_1^infinity |w_x'(t)| |M(t)| dt`.

Thus the `X^(3/2+epsilon)` earthmover scale is exactly compatible with the Riesz critical decay `x^(-3/4+epsilon)` under the effective Cell scale `X~sqrt(x)`.

This explains the exponent `3/2` geometrically: `X` Cells times square-root average displacement `sqrt(X)`.

---

## 5. Pair-BRC Gram energy collapsed to one parent Cell

For `sigma>1`, where the following double expansion is absolutely convergent, define

`E_sigma = int_0^infinity |P_2(x)|^2 x^(1-sigma) dx`.

The exact Gram kernel is

`K_sigma(m,n)=C_sigma (mn)^(-sigma) sech^(2-sigma)(log(m/n))`,

with

`C_sigma=2^(sigma-2) Gamma(2-sigma)`.

For squarefree `m,n`, write

`m=g a`, `n=g b`, `g=gcd(m,n)`.

Then `g,a,b` are pairwise coprime and

`mu(m)mu(n)=mu(a)mu(b)`.

Set the squarefree parent Cell

`r=ab`.

Define the positive balanced-divisor observable

`D_sigma(r)=sum_{d|r} sech^(2-sigma)(log(d^2/r))`.

Summing the common core `g` first gives the exact identity

`E_sigma`
`= C_sigma * zeta(2sigma)/zeta(4sigma)`
`  * sum_{r squarefree} mu(r) r^(-sigma)`
`    D_sigma(r) / prod_{p|r}(1+p^(-2sigma)).`

Interpretation:

- `r` is a one-copy parent arithmetic Cell;
- `mu(r)` is the parent orientation;
- `D_sigma(r)` is the multiplicity of balanced divisor splits `d ~ sqrt(r)`;
- the Euler factor denominator is the exact correction left after the common core has been summed.

Thus the two-copy Pair-BRC energy is equivalent, in the absolute region, to a one-copy signed parent-Cell series weighted by a positive divisor-balance cloud.

---

## 6. Positive Fourier representation of the divisor cloud

Let `alpha=2-sigma>0` and `k_sigma(u)=sech^alpha(u)`.

Its Fourier transform is positive:

`hat{k_sigma}(t)`
`= 2^(alpha-1)/Gamma(alpha) * |Gamma((alpha+i t)/2)|^2 >0`.

Therefore

`D_sigma(r)`
`= (1/(2pi)) int_R hat{k_sigma}(t)`
`    prod_{p|r} 2 cos(t log p) dt.`

Re-Eulerizing the squarefree parent series gives locally

`(1+p^(-2sigma)) - 2p^(-sigma)cos(t log p)`
`= |1-p^(-sigma-it)|^2`.

Hence the previous parent-Cell representation exactly reconstitutes

`prod_p |1-p^(-sigma-it)|^2 = |1/zeta(sigma+it)|^2`.

Equivalently,

`E_sigma = (1/(4pi)) int_R`
`|Gamma(1-sigma/2+i t/2)|^2 |1/zeta(sigma+i t)|^2 dt`

in the absolute region.

This is a consistency check and a structural bridge, not a new analytic continuation theorem.

---

## 7. Dense-divisibility input: balanced split capacity is abundant

Public prior art used here:

- Sarajian--Weingartner, *An extension of smooth numbers: Multiple dense divisibility*, JNT 280 (2026), 278--317.

For each fixed recursion depth `i`, their theorem gives uniformly

`D_i(x,y) asy_i x (log y/log x)^(lambda_{1/i})`,

and the same order remains valid when only squarefree members are counted (for `y` above an `i`-dependent threshold).

Take `y=x^theta` with fixed `theta>0`. Then for every fixed `i`, a linear-order family of squarefree parent Cells carries an `i`-level recursively dense divisor structure.

For `i=1`, y-dense divisibility guarantees a divisor `d` with

`sqrt(r)/y < d <= sqrt(r)`.

Therefore

`D_sigma(r) >= 2 sech^(2-sigma)(2 log y)`.

Given any fixed `eta>0`, choosing `theta` sufficiently small gives a linear-order family of squarefree parent Cells with

`D_sigma(r) >= r^(-eta)`

up to a constant depending on `sigma,eta`.

Freeze:

`BALANCED_DIVISOR_CAPACITY_IS_NOT_SPARSE`.

Also, for arbitrarily large fixed `i`, recursively deep composite divisor geometry occurs on a linear-order family. This is compatible with the project architecture

`FIXED_X6_DIMENSION + GROWING_COMPOSITE_BRC_DEPTH`.

---

## 8. Capacity/orientation boundary

Dense-divisibility results count `mu^2` capacity; they do not provide the parity cancellation of `mu=(-1)^omega` required by RH.

Freeze:

`DENSE_DIVISOR_CAPACITY != MOBIUS_ORIENTATION_CANCELLATION`.

An Erdos--Kac theorem is known for the number of prime factors on dense-divisor integers, but Gaussian information near the central scale does not by itself control the parity character at frequency pi. Do not infer Möbius cancellation from a CLT.

This is the exact surviving bottleneck after the current bridge:

1. balanced divisor / composite BRC paths are plentiful;
2. alternative L1 pairing algorithms cannot beat the conserved Mertens cut flux;
3. the missing theorem is signed orientation cancellation on the capacity-rich parent-Cell family.

---

## 9. New smallest research unit

Study the parent orientation discrepancy

`S_sigma(R)`
`= sum_{r<=R, r squarefree} mu(r)`
`  D_sigma(r)/prod_{p|r}(1+p^(-2sigma))`

and its dyadic variants, with primary attention to `sigma` approaching `1/2`.

Desired type of result (sufficient, not asserted): a square-root-scale bound for the weighted parent discrepancy, uniformly enough in the critical parameter, would feed directly into the Gram/Riesz criterion.

The next tests should be:

- split parent Cells by dense-divisor depth and measure signed orientation separately from positive capacity;
- inspect whether known generating functions for `z^omega(n)` on dense-divisor classes can be analytically continued far enough toward `z=-1` to say anything quantitative about the parity character;
- retain full prime-label provenance through any such continuation;
- do not claim that Erdos--Kac/Gaussian distribution controls parity without a high-frequency characteristic-function theorem.

---

## 10. Machine constraints added by this event

- `ARITHMETIC_VALUE_LINE != NATIVE_X6_AXIS`.
- `MONOTONE_MOBIUS_MATCHING = L1_OPTIMAL_1D_TRANSPORT`.
- `ALTERNATIVE_PAIRING_CANNOT_CHANGE_CUT_FLUX`.
- `RH <=> DYADIC_MOBIUS_EARTHMOVER_COST X^(3/2+o(1))`.
- `PAIR_BRC_GRAM -> PARENT_CELL x BALANCED_DIVISOR_CLOUD` in the absolute region.
- `BALANCED_DIVISOR_CAPACITY_IS_ABUNDANT`.
- `DENSE_DIVISOR_CAPACITY != MOBIUS_ORIENTATION_CANCELLATION`.
- `GAUSSIAN_OMEGA_INFORMATION != PARITY_CONTROL`.

No RH proof is claimed.