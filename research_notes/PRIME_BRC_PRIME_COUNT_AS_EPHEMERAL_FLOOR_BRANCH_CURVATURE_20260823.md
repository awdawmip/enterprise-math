# Prime-BRC Prime Count as Ephemeral Floor-Branch Curvature

Status: `L3 OWNER-LOCAL / PROVED EXACT REFORMULATION / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. Prime-valued floor support

Let

\[
\mathcal F(x)=\{\lfloor x/j\rfloor:1\le j\le x\},
\qquad
\mathcal G(x)=\mathcal F(x)\cap\mathbb P.
\]

For an odd integer `n>=5`, define the newly born prime support

\[
N(n)=\mathcal G(n)\setminus\mathcal G(n-1).
\]

The owner-local odd jump theorem gives

\[
|N(n)|
=\mathbf1_{\{P^+(n)^2\ge n\}}.
\]

Thus `N(n)` is either empty or a singleton.

## 2. One-step ephemeral support theorem

Let

\[
K^2<n<(K+1)^2
\]

be odd. Then

\[
\boxed{
\mathbf1_{\{n\text{ prime}\}}
=
|N(n)\setminus\mathcal G(n+1)|.
}
\]

### Proof

If `N(n)=empty`, then `n` has no prime factor above `sqrt(n)` and is composite.

Otherwise `N(n)={q}`, where

\[
q=P^+(n)>\sqrt n>K.
\]

Write

\[
n=a q,
\qquad 1\le a<q.
\]

The branch-lifetime theorem gives exact lifetime `a`.

- If `a=1`, then `n=q` is prime and `q` leaves immediately at `n+1`; hence `q notin G(n+1)` and the ephemeral support has size one.
- If `a>1`, then `n` is a large-prime-tail composite and the entering branch persists at least through `n+1`; hence `q in G(n+1)` and the ephemeral support is empty.

Therefore the formula holds. ∎

## 3. Exact square-basin prime-count formula

For `K>=2`, every prime strictly between consecutive squares is odd. Hence

\[
\boxed{
\pi\big((K^2,(K+1)^2)\big)
=
\sum_{\substack{K^2<n<(K+1)^2\\ n\text{ odd}}}
\left|
\big(\mathcal G(n)\setminus\mathcal G(n-1)\big)
\setminus\mathcal G(n+1)
\right|.
}
\]

Every summand is `0` or `1`.

Thus Legendre's conjecture is exactly the positivity statement

\[
\boxed{
\sum_{n\in I_K^{\rm odd}}
|\text{ephemeral prime branches born at }n|>0.
}
\]

## 4. Why scalar second differences are insufficient

The scalar count

\[
G(n)=|\mathcal G(n)|
\]

forgets branch identity. At the even step `n+1`, many unrelated prime labels can enter or leave simultaneously. Therefore a scalar second difference of `G` does not isolate the branch born at `n`.

The exact formula requires the set-valued correlation

\[
\big(\mathcal G(n)\setminus\mathcal G(n-1)\big)
\cap\mathcal G(n+1),
\]

which retains the identity of the same branch across time.

This is a direct no-resurrection example: once prime-label identity is erased, one cannot infer whether the specific entering branch persisted.

## 5. BRC interpretation

The three-time support pattern is

```text
absent at n-1
   -> present at n
      -> absent at n+1    : prime

absent at n-1
   -> present at n
      -> still present n+1: large-prime-tail composite.
```

Hence prime detection is a local temporal-curvature observable on branch support, not merely a current-state occupancy count.

Freeze:

`SQUARE_BASIN_PRIME_INDICATOR_EQUALS_EPHEMERAL_PRIME_FLOOR_BRANCH = true`.

`LEGENDRE_EQUALS_POSITIVITY_OF_EPHEMERAL_BRANCH_CURVATURE_SUM = true`.

`SCALAR_G_SECOND_DIFFERENCE_IS_NOT_BRANCH_IDENTITY_SUFFICIENT = true`.

This is an exact reformulation, not a proof of the positivity statement.
