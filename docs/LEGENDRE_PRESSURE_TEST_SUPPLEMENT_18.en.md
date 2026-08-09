# Legendre Pressure Test — Supplement 18

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact cross-shell separation of first-factor cofactor windows  
Depends on: canonical P017 L020–L027, L051–L053, and P018 T110–T113  
Discipline: finite integer arithmetic only; no prime-distribution estimate and no claim of a Legendre proof.

## 1. L054 — Strict separation of raw cofactor windows

For a prime `p<=k`, write

\[
W_p(k)=\left[\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor\right].
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

Thus `p(k+2)<=rk`, so

\[
\frac{k(k+2)}r\le\frac{k^2}p.
\]

Taking integer floors proves the claim because the lower endpoint of `W_p(k)` is one larger than `floor(k^2/p)`. ∎

## 2. Sharp finite exception

At `k=3`,

\[
W_2(3)=[5,7],\qquad W_3(3)=[4,5],
\]

so the windows meet at `q=5`, corresponding to

\[
10=2\cdot5,\qquad15=3\cdot5.
\]

Thus the uniform threshold `k>=4` is sharp.

## 3. Least-factor stripping is injective

For a composite state `n` in the open square basin, put

\[
p=\operatorname{spf}(n),\qquad \Psi_k(n)=n/p.
\]

For `k>=4`, `\Psi_k` is injective on all square-basin composite states. Within a fixed first-prime shell this is immediate; across distinct shells, equal stripped cofactors would have to belong to two different raw windows, contradicting L054.

Hence

\[
\boxed{n_1\ne n_2\Longrightarrow
\frac{n_1}{\operatorname{spf}(n_1)}\ne
\frac{n_2}{\operatorname{spf}(n_2)}}
\]

for composite `n_1,n_2` in `I_k`, `k>=4`.

## 4. Relation to L052, L053 and T113

L052 says that for `k>=15`, distinct lower-band least primes have disjoint candidate root pairs. L054 acts below that coarse coordinate: exact quotient windows are already disjoint for all first-prime shells once `k>=4`, even when coarse square-root basins can still coincide.

L053 is orthogonal: it retains prime-power multiplicity inside a mirror CRT cell and can reduce bounded radius capacity. T113 then splits each exact quotient window at at most one square-root boundary.

The lower-band picture therefore has nested constraints:

1. exact parent quotient windows are ordered and disjoint (L054);
2. stable lower-band root channels are disjoint (L052);
3. full-core mirror CRT can reduce bounded lift capacity (L053);
4. the actual quotient-root branch inside a window is controlled by one threshold (T113).

## 5. What L054 does not solve

The injection `n -> n/spf(n)` maps the original `2k`-state basin into a larger cofactor range, so injection alone gives no cardinality deficit. Expanding exact windows to full target square basins would also discard the gain and fall back to ordinary rough-number bookkeeping.

The next step must preserve the exact subwindows and couple them to an original-basin constraint, especially the multiplicity-sensitive mirror state from L053.

## 6. Executable validation

The replay adds `p017_cofactor_separation.py` and its regression tests. Tests cover strict ordering, zero and positive integer gaps, the arithmetic spacing margin, least-factor stripping injectivity, and the sharp `k=3` exception.

Historical novelty remains `NOVELTY_UNVERIFIED`.
