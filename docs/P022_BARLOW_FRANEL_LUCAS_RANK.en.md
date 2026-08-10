# P022 Barlow low-order identifiability: Franel p-Lucas rank layer

Status: `PROVED_WIP + TARGETED_EXECUTABLE_CHECKED`  
Owner: `P022 / program/p022-geometry-v2`  
Scope: global low-order checkpoint identifiability after central-binomial elimination

## 1. Purpose

Write

\[
F_n=\sum_{k=0}^n {n\choose k}^3
\]

for the Franel numbers.  The P022 low-order reduction has already isolated the
pure Franel defects `D_n` at exactly the indices for which `2n-1` is composite.
The remaining global arithmetic question is therefore whether the Franel
sequence supplies enough new valuation information at those indices.

This note records the p-Lucas/rank layer needed for that question.  It does not
claim novelty for the underlying Lucas or reflection congruences.

## 2. Prior-art boundary

The following ingredients are external prior mathematics.

1. Lucas' binomial theorem gives the Franel digit factorization

   \[
   F_n\equiv\prod_i F_{n_i}\pmod p
   \]

   for the base-`p` digits `n_i`.  Malik--Straub, *Divisibility properties of
   sporadic Apéry-like numbers*, Research in Number Theory 2 (2016), article 5,
   DOI `10.1007/s40993-016-0036-8`, supplies broader Apéry-like Lucas-congruence
   context.  The digit factorization used here should therefore be treated as
   prior art, not as an Enterprise Math invention.

2. Jarvis--Verrill, *Supercongruences for the Catalan-Larcombe-French numbers*,
   arXiv:`0905.4187`, Lemma 2.6, prove for every odd prime `p` and
   `0 <= d <= p-1` that

   \[
   F_d\equiv(-8)^dF_{p-1-d}\pmod p.
   \]

   In particular, zero digits are symmetric under `d -> p-1-d`.  The same
   paper also connects the midpoint Franel value to the
   Catalan-Larcombe-French midpoint criterion.

3. Beukers, *p-linear schemes for sequences modulo p^r*, Indagationes
   Mathematicae 35 (2024), 698--707, DOI `10.1016/j.indag.2023.12.003`, gives
   higher-prime-power structure for Franel and related Lucas sequences.  That
   theory is not used in the proofs below, but it is a natural next source for
   controlling valuation multiplicity rather than merely mod-`p` zero sets.

## 3. The complete mod-p zero language

For a prime `p`, define

\[
Z_p=\{d\in\{1,\ldots,p-1\}:F_d\equiv0\pmod p\}.
\]

### Theorem 3.1 — digit-zero characterization

If `n=sum_i n_i p^i` is the base-`p` expansion of `n`, then

\[
\boxed{
 p\mid F_n
 \iff
 \text{at least one digit }n_i\text{ belongs to }Z_p.
}
\]

**Proof.**  Lucas factorization gives

\[
F_n\equiv\prod_i F_{n_i}\pmod p.
\]

Because `F_0=1`, the product vanishes exactly when one nonzero digit factor
vanishes.  This is precisely membership of some digit in `Z_p`.  ∎

### Corollary 3.2 — rank of apparition is a digit

If

\[
r_p=\min\{n>0:p\mid F_n\}
\]

exists, then

\[
\boxed{r_p=\min Z_p<p.}
\]

Consequently, for `n>0`, a prime `p` is a primitive prime divisor of `F_n` if
and only if

\[
\boxed{r_p=n.}
\]

This is stronger than merely saying that a primitive prime must exceed `n`:
the entire first-occurrence question is reduced to the first zero among the
single base-`p` digits.

### Corollary 3.3 — exact block counts and density-one basin

Let `z_p=|Z_p|`.  In the full block `0 <= N < p^L`, exactly

\[
(p-z_p)^L
\]

indices have `F_N` nonzero modulo `p`, and therefore exactly

\[
p^L-(p-z_p)^L
\]

indices are divisible by `p`.  If `Z_p` is nonempty, the divisible proportion
along these `p`-power blocks tends to one.

In particular, if `p` is primitive at `n`, every later index whose base-`p`
expansion contains the digit `n` is also divisible by `p`.  The previously
used witness `n+p` is only the first simple example.  Primitive means
"first appearance", not "permanently private marker".

## 4. Reflection cuts the rank range in half

### Theorem 4.1 — reflected zero set

For every odd prime `p`,

\[
\boxed{d\in Z_p\iff p-1-d\in Z_p.}
\]

This is the zero-set form of the Jarvis--Verrill reflection congruence.

### Corollary 4.2 — half-prime rank bound

Whenever `r_p` exists for an odd prime `p`,

\[
\boxed{r_p\le\frac{p-1}{2}.}
\]

**Proof.**  Reflection sends the first zero `r_p` to another zero
`p-1-r_p`.  Minimality of `r_p` gives

\[
r_p\le p-1-r_p.
\]

Rearranging yields the result.  ∎

### Corollary 4.3 — strengthened primitive-prime bound

If an odd prime `p` is primitive at `F_n`, then `r_p=n`, hence

\[
\boxed{p\ge2n+1.}
\]

The only even primitive case is `p=2` at `F_1`.

This is the numerically relevant strengthening of the earlier p-Lucas bound
`p>n`.

## 5. Direct consequence for the Barlow pure-defect layer

At a composite boundary `2n-1`, the central-binomial coordinate `A_n` has a
triangular multiplicative expression in earlier `A_j`, and the resulting pure
Franel defect has the form

\[
D_n=F_n\prod_{j<n}F_j^{-\alpha_{n,j}}.
\]

Suppose `p` is primitive at `F_n`.  Then every earlier `F_j`, `j<n`, has
`v_p(F_j)=0`, so

\[
\boxed{v_p(D_n)=v_p(F_n)>0.}
\]

For every earlier defect `D_m`, `m<n`, all Franel factors occurring in its
triangular definition also have index `<n`, hence

\[
\boxed{v_p(D_m)=0.}
\]

Thus primitive rows, ordered by their first-zero indices, give a triangular
valuation certificate.  Its diagonal entries are exactly the primitive
valuations `v_p(F_n)`.  If each chosen primitive valuation is one, the finite
prefix certificate is unimodular, not merely full rank over the rationals.

Corollary 4.3 adds a useful separation from the already-solved `A` layer:
through segment `n`, the central-binomial prime basis is exhausted by primes
at most `2n-1`, while an odd primitive Franel pivot satisfies `p>=2n+1`.
Therefore such a primitive row is automatically beyond the current
central-binomial prime cutoff and is intrinsically a pure-defect witness.

## 6. Midpoint divisibility is not primitive divisibility

Jarvis--Verrill's results imply the prior-art midpoint criterion

\[
\boxed{
 p\mid F_{(p-1)/2}
 \iff
 p\equiv5\text{ or }7\pmod8
}
\]

for odd primes `p`.

This supplies a large structured source of Franel divisibility, but it does
not solve the primitive-rank problem.  For example,

\[
Z_{29}=\{12,14,16\},
\]

so `29 | F_14` at the midpoint while `r_29=12`.  Likewise a forced midpoint
zero may have an earlier reflected pair of zeros.  Midpoint congruences must
therefore not be promoted into a primitive-divisor theorem.

## 7. Global question after this compression

For the P022 global `(J1,J2,J3)` route, the primitive sufficient condition can
now be stated without any finite-window language:

> For every relevant `n` with `2n-1` composite, does there exist a prime `p`
> such that `r_p=n`?

Any such prime is automatically at least `2n+1` when `n>=2`.

A positive answer for all relevant `n` gives the infinite triangular defect
certificate immediately.  A proof for an infinite subfamily of relevant
indices already gives the first genuine infinite theorem family beyond the
finite `N=150` certificate.

Failure at one index would only show that primitive divisors are a sufficient
mechanism rather than the mother mechanism: the previously observed segment
`n=67` already shows that global dependence detection can continue without a
local new-prime pivot.

## 8. Executable checks in this owner generation

`src/enterprise_math/p022_barlow_franel_lucas_rank.py` packages:

- `F_0=1` correctly as the Lucas unit;
- the digit-zero language and exact block counts;
- rank-of-apparition extraction;
- Jarvis--Verrill reflection checks and the half-prime rank bound;
- the midpoint criterion as prior art;
- the strengthened `p>=2n+1` primitive-divisor necessity.

`tests/test_p022_barlow_franel_lucas_rank.py` uses an independent local
`sum(comb(n,k)^3)` oracle instead of reusing the production Franel helper for
its expected values.  It checks zero digits, ranks, reflection, midpoint
behavior, block counts, and small primitive examples including the sharp cases
`(n,p)=(2,5),(3,7),(6,13)`.

The open research frontier is now existence and multiplicity of first-zero
primes, not another determinant enlargement.
