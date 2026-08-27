# P017 — c=103/20 T1–T2 High-Valuation Direct Collapse

Status: `PROVED_WIP ALL RESIDUAL VALUATIONS j>=2 < 0.00012 L23 / ONLY j=1 REMAINS LOAD-BEARING / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Companion checker:

`experiments/p017_p2_c515_t12_high_valuation_direct_collapse_20260827.py`

Refines:

`docs/P017_P2_C515_T12_J2_DIRECT_STATE_COUNT_20260827.md`.

Purpose: extend the direct square-divisor argument from valuation `j=2` to every corrected residual shell `2<=j<=8` and remove all of them from the analytic frontier at once.

---

## 1. Multiplicity decreases with valuation

A residual state on valuation shell `j` is divisible by

\[
r^j q p,
\]

where `r` is the least prime, `q` the second distinct prime and each residual occurrence is indexed by a later distinct prime after `q`.

If there are `k` such later distinct primes, then all prime factors displayed are at least

\[
z=D^{1/6}.
\]

Therefore

\[
n\ge z^{j+1+k}=D^{(j+1+k)/6}.
\]

Since every basin state satisfies `n<D^(9/5)`,

\[
5(j+1+k)<54.
\]

For `2<=j<=8` this gives

\[
\boxed{k\le9-j.}
\tag{HV1}

Thus the residual occurrence multiplicities are at most

\[
7,6,5,4,3,2,1
\]

for `j=2,...,8` respectively.

---

## 2. All high valuations reduce to the square-reciprocal sum

The dangerous least-prime range is the same finite set as in the `j=2` theorem:

\[
1447\le r<D^{73/240}<585015,
\]

containing exactly 47735 primes.

For `j>=2` and `r>=1447`,

\[
\frac1{r^j}
\le
\frac1{1447^{j-2}}\frac1{r^2}.
\]

The frozen square-reciprocal certificate is

\[
\sum_r\frac1{r^2}<\frac{423}{5000000}.
\]

Hence

\[
\sum_{j=2}^8(9-j)\sum_r\frac1{r^j}
<
\frac{423}{5000000}
\sum_{j=2}^8\frac{9-j}{1447^{j-2}}.
\tag{HV2}

The interval-count `+1` contributions have total multiplicity

\[
\sum_{j=2}^8(9-j)=28.
\]

---

## 3. Combined finite bound

Restore the residual kernel and source denominator

\[
\kappa\le\frac{73}{80},
\qquad
\Delta=\frac{93}{20}.
\]

For the P(23)-anchored interval of length

\[
L_{23}=232018561402828200,
\]

the complete high-valuation residual therefore satisfies

\[
\frac{|R_{j\ge2}|}{L_{23}}
<
\frac{20}{93}\frac{73}{80}
\left[
\frac{423}{5000000}
\sum_{j=2}^8\frac{9-j}{1447^{j-2}}
+rac{28\cdot47735}{L_{23}}
\right].
\]

The exact rational checker proves

\[
\boxed{
\frac{|R_{j\ge2}|}{L_{23}}
<
\frac3{25000}
=0.00012.
}
\tag{HV3}

The displayed rational upper bound is approximately `0.00011629`; the decimal is not used in the proof.

---

## 4. Frontier reduction

The corrected residual valuation decomposition is now finite-closed on every shell except one:

\[
\boxed{
\begin{array}{ll}
j=1 &: \text{only remaining load-bearing residual carrier},\\
j\ge2 &: |R|<0.00012L_{23}\text{ in total}.
\end{array}}
\]

This is stronger than separately passing `j=2` through its 254-state inner Rosser support and treating `j>=3` by sieve-depth arguments. The valuation power itself supplies enough direct physical-space sparsity.

The bound concerns the actual residual ordered-pair penalty after the corrected least-shell plus one-pair pointwise credit. It is not added as a separate correction to the source main coefficient; downstream budget accounting must keep that decomposition explicit.

No finite P2 theorem or all-K claim is made.
