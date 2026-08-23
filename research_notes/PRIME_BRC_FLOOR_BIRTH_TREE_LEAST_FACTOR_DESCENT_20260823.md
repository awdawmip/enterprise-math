# Prime-BRC Floor-Birth Tree = Least-Factor Descent

Status: `L3 OWNER-LOCAL / PROVED ELEMENTARY THEOREM / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

Depends on:

`research_notes/PRIME_BRC_FLOOR_QUOTIENT_BRANCH_BIRTH_MULTIPLICITY_20260823.md`.

## 1. Proper birth fiber

For `n>=2`, define

\[
\mathsf B(n)=
\bigl(\mathcal F(n)\setminus\mathcal F(n-1)\bigr)\setminus\{n\}.
\]

The birth-multiplicity theorem gives

\[
\boxed{
\mathsf B(n)
=
\{d:d\mid n,\ \sqrt n\le d<n\}.
}
\]

Thus `B(n)` is exactly the upper proper-divisor frontier.

## 2. Prime = leaf

Immediately,

\[
\boxed{
\mathsf B(n)=\varnothing
\iff
n\text{ is prime}.
}
\]

Indeed a composite integer has a least prime factor at most `sqrt(n)`, hence a complementary proper divisor at least `sqrt(n)`.

## 3. Canonical maximum child

Let `n` be composite and let

\[
p=\operatorname{spf}(n).
\]

Then

\[
\boxed{
\max\mathsf B(n)=\frac np.
}
\]

### Proof

The value `n/p` is a proper divisor and `p<=sqrt(n)`, so `n/p>=sqrt(n)` and belongs to the birth fiber.

Any proper divisor `d` can be written `d=n/a` with integer `a>1`. Since `p` is the least prime factor of `n`, every such complementary divisor `a` satisfies `a>=p`. Therefore

\[
d=\frac na\le\frac np.
\]

Hence `n/p` is the unique maximum birth child. ∎

Freeze the identity

\[
\boxed{
\text{MAX_NEW_FLOOR_BRANCH}(n)
=
\frac n{\operatorname{spf}(n)}.
}
\]

## 4. Iterated birth descent reconstructs factorization

Define

\[
n_0=n.
\]

While `B(n_i)` is nonempty, set

\[
n_{i+1}=\max\mathsf B(n_i).
\]

Then

\[
\boxed{
\frac{n_i}{n_{i+1}}=\operatorname{spf}(n_i).
}
\]

Thus the successive edge labels recover the prime factors of `n` one multiplicity at a time in nondecreasing order.

If

\[
n=p_1p_2\cdots p_m,
\qquad p_1\le\cdots\le p_m,
\]

with multiplicity retained, then the canonical birth descent is

\[
\boxed{
 n
\to p_2\cdots p_m
\to p_3\cdots p_m
\to\cdots\to p_m,
}
\]

and the terminal node `p_m` is prime / birth-free.

The number of nontrivial descent edges is

\[
\boxed{\Omega(n)-1.}
\]

No external choice of factor order is required: maximum-birth selection canonically implements least-factor stripping.

## 5. Exact P2 future-signature theorem in an open square basin

Let

\[
K^2<n<(K+1)^2.
\]

Then `n` is nonsquare.

### Theorem

\[
\boxed{
\Omega(n)\le2
\iff
\Big(
\mathsf B(n)=\varnothing
\Big)
\ \text{or}\ 
\Big(
\mathsf B(n)=\{d\}\ \text{and}\ \mathsf B(d)=\varnothing
\Big).
}
\]

### Proof

- If `n` is prime, the first branch holds.
- If `n=pq` with distinct primes `p<q`, then the upper proper divisors consist only of `q`, so `B(n)={q}` and `B(q)=empty`.

Conversely, if `B(n)` is empty then `n` is prime. If it is a singleton, the nonsquare birth-count theorem gives `tau(n)=4`. A nonsquare integer with four divisors is either `pq` for distinct primes or `p^3`. In the `pq` case the unique child is the prime `q`; in the `p^3` case the unique child is `p^2`, whose proper birth fiber is `{p}` and is nonempty. Thus the one-level future test separates the two cases exactly. ∎

This explains the minimal repeat-event correction in the adaptive Prime-BRC P2 detector: current birth multiplicity `2` merges semiprime and prime-cube states; one child-future query repairs it.

## 6. Relation to P017/P018

The canonical P017 least-factor quotient

\[
n\longmapsto n/\operatorname{spf}(n)
\]

is not an external operation imposed on the floor dynamics. It is already selected internally as the maximum proper branch born at `n`.

Hence the P017 cofactor windows `W_p(K)`, P018 quotient-root transport, and Prime-BRC future signatures can all be placed on one canonical branch tree:

```text
integer state n
  -> floor-quotient birth fiber B(n)
  -> canonical max child n/spf(n)
  -> P017 cofactor window / P018 quotient-root
  -> repeat until prime birth-free leaf.
```

## 7. BRC interpretation and boundary

This is an exact arithmetic process interpretation, not a computational speedup claim. Constructing the full floor-quotient birth set can itself expose divisor information.

The gain is semantic:

- prime = leaf;
- least-factor stripping = canonical max-child evolution;
- factor multiplicity = path depth;
- P2 = leaf or singleton child whose next future is a leaf;
- no factor-order oracle is needed to define the process.

Freeze:

`P017_LEAST_FACTOR_STRIPPING_EQUALS_MAX_FLOOR_BIRTH_DESCENT = true`.

`ITERATED_MAX_BIRTH_DESCENT_RECOVERS_ORDERED_PRIME_FACTORS = true`.

`OPEN_SQUARE_P2_CLASSIFIED_BY_ONE_CHILD_FUTURE = true`.

`THIS_IS_NOT_A_PRIMALITY_SPEEDUP_OR_LEGENDRE_PROOF = true`.
