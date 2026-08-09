# Legendre Pressure Test — Supplement 17

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact cross-shell separation of first-factor cofactor windows  
Depends on: canonical P017 cofactor-window formula L020–L027, lower-band root packing L051–L052, and P018 T110–T113  
Discipline: finite integer arithmetic only; no prime-distribution estimate and no claim of a Legendre proof.

## 1. L053 — Strict separation of raw cofactor windows

For a prime `p<=k`, write the exact raw first-factor cofactor window as

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

### Theorem

Let `k>=4` and let `p<r<=k` be primes. Then

\[
\boxed{\max W_r(k)<\min W_p(k).}
\]

Equivalently,

\[
\left\lfloor\frac{k(k+2)}r\right\rfloor
\le
\left\lfloor\frac{k^2}p\right\rfloor.
\]

### Proof

It is enough to prove

\[
p(k+2)\le rk,
\]

or

\[
2p\le k(r-p).
\]

If `p=2`, then `r-p>=1` and `k>=4`, so `k(r-p)>=4=2p`.

If `p>=3`, both primes are odd, hence `r-p>=2`; also `p<=k`, so

\[
k(r-p)\ge2k\ge2p.
\]

Thus `p(k+2)<=rk`, which gives

\[
\frac{k(k+2)}r\le\frac{k^2}p.
\]

Taking integer floors proves the claimed strict ordering because the lower endpoint of `W_p(k)` is one larger than `floor(k^2/p)`. ∎

## 2. Sharp finite exception

The threshold `k>=4` is real. At `k=3`,

\[
W_2(3)=[5,7],
\qquad
W_3(3)=[4,5],
\]

so the windows meet at `q=5`. The corresponding basin states are

\[
10=2\cdot5,
\qquad
15=3\cdot5.
\]

## 3. Least-factor stripping is injective

For a composite state `n` in the open square basin, put

\[
p=\operatorname{spf}(n),
\qquad
\Psi_k(n)=n/p.
\]

For `k>=4`, `Psi_k` is injective on all square-basin composite states.

Within one fixed first-prime shell this is immediate. Across different first-prime shells, the two stripped cofactors would have to lie in two distinct raw windows, but L053 makes those windows disjoint.

Hence

\[
\boxed{
n_1\ne n_2\text{ composite in }I_k
\Longrightarrow
\frac{n_1}{\operatorname{spf}(n_1)}
e
\frac{n_2}{\operatorname{spf}(n_2)}
}
\]

for every `k>=4`.

This is stronger than disjointness of the original first-factor shells: their quotient images are disjoint as well.

## 4. Relation to L052 and T113

Canonical L052 says that for `k>=15`, distinct lower-band least primes have disjoint candidate root pairs

\[
\{j_p,j_p+1\}.
\]

L053 acts one level below the root coordinate: the exact integer cofactor windows are disjoint for **all** first-prime shells once `k>=4`, including cases where two windows still land in the same coarse square-root basin for small `k`.

P018-T113 then splits each one of these exact windows at at most one square-root boundary. Therefore the lower-band recursion now has three nested constraints:

1. exact parent cofactor windows are ordered and disjoint (L053);
2. for `k>=15`, lower-band parent root channels are already disjoint (L052);
3. inside each parent window, the actual quotient-root branch is controlled by one exact threshold (T113).

## 5. What L053 does not solve

The injection `n -> n/spf(n)` maps the original `2k`-state basin into a larger cofactor range. It therefore does not by itself produce a cardinality deficit.

Likewise, replacing every exact cofactor window by its full target square basin would discard the gain and reduce the argument to ordinary rough-number bookkeeping.

The next useful step must keep the exact local subwindows and combine them with an original-basin constraint, such as the centered mirror certificates. A candidate should be rejected if it secretly reconstructs the full small-prime sieve.

## 6. Executable validation

The replay adds:

- `src/enterprise_math/p017_cofactor_separation.py`;
- `tests/test_p017_cofactor_separation.py`.

The tests cover strict ordering, zero and positive integer gaps, the arithmetic spacing margin, least-factor stripping injectivity, and the sharp `k=3` exception.

Historical novelty remains `NOVELTY_UNVERIFIED`.
