# P017 — Support-Sensitive Cauchy Compression at the Tier-A Splice

Status: `PROVED_WIP TOP-SCALE FACTORABLE-BLOCK CONSTANT + EXACT CHECKER / NOT FULL SIEVE SUM / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- Iwaniec, *A new form of the error term in the linear sieve* (Acta Arith. 37, 1980), Theorem 1;
- Iwaniec–Laborde, *P2 in short intervals* (Ann. Inst. Fourier 31, 1981), Lemmas 2 and 4;
- `docs/P017_P2_A6_ORDER4_GEOMETRIC_BSPLINE_CROSSSTATE_20260826.md`;
- `docs/P017_P2_EXPLICIT_RECIPROCAL_SUM_LEMMA_20260825.md`.

Companion exact checker:

`experiments/p017_p2_support_sensitive_cauchy_compression_20260826.py`.

Purpose: retain, instead of discarding, the source sieve-support condition

\[
m\mid P(z),\qquad n\mid P(z)
\]

inside the Cauchy step for one top-scale factorable geometric block. This is a finite-effectivity result at the conservative Tier-A splice; it does not yet sum all Rosser/Iwaniec factorization pieces or all lower geometric sub-blocks.

---

## 1. Source condition that had previously been thrown away

In the source linear-sieve remainder, the factorable variables satisfy

\[
\boxed{m\mid P(z),\qquad n\mid P(z),}
\]

with factorable coefficients bounded by one. Thus each such variable is squarefree and every prime factor is below `z`.

The preceding coefficient-uniform pressure tests replaced these sparse sets by complete intervals. That is legal but unnecessarily expensive at the finite splice.

For the current a6 order-4 package retain

\[
\theta=\frac{4999}{10000},
\qquad d=\frac59,
\qquad \eta=\frac1{40},
\qquad \rho=\frac65,
\]

and

\[
\mu=\frac{161777}{360000},
\qquad
\nu=\frac{4247}{40000},
\]

so

\[
M=X^\mu,
\qquad N=X^\nu,
\qquad MN=X^{5/9}.
\]

At the conservative Tier-A splice put

\[
K_0=116009280740973308,
\qquad X_0=K_0^2.
\]

---

## 2. Exact prime cutoff and exact short-variable support

Here

\[
z=X_0^{5/54}.
\]

The checker proves by integer exponentiation

\[
1439^{54}<X_0^5<1447^{54}.
\]

Since `1439` and `1447` are consecutive primes, the source condition `p<z` means exactly

\[
\boxed{p\le1439}
\]

at this splice.

Likewise

\[
4203<N<4204,
\]

and

\[
5044<\rho N<5045.
\]

Hence the integer short block is exactly

\[
\boxed{4204\le n\le5044,}
\]

containing `841` integers.

Exact finite factorization of these integers gives

\[
\boxed{
B_N
:=
\#\{n\in[N,\rho N]:n\mid P(z)\}
=325.
}
\tag{S1}
\]

This deliberately retains the prime `2`; no odd-only improvement is consumed here.

---

## 3. Rigorous Rankin bound for the long variable

Let

\[
\mathcal M_z
=
\{m:M<m\le\rho M,\ m\mid P(z)\},
\qquad
A_M=|\mathcal M_z|.
\]

Take

\[
\sigma=\frac35.
\]

For every `m` in this block,

\[
1\le\left(\frac{\rho M}{m}\right)^\sigma.
\]

Therefore

\[
A_M
\le
(\rho M)^\sigma
\sum_{m\mid P(z)}m^{-\sigma}
=
(\rho M)^\sigma
\prod_{p<z}(1+p^{-\sigma}).
\]

Using `1+u<=e^u`,

\[
A_M
\le
(\rho M)^{3/5}
\exp\left(\sum_{p\le1439}p^{-3/5}\right).
\]

The checker upper-encloses each `p^(-3/5)` by exact integer fifth-root arithmetic and proves

\[
\boxed{
\sum_{p\le1439}p^{-3/5}<\frac{1819}{200}=9.095.
}
\tag{S2}
\]

The first eleven positive terms of

\[
\log10
=2\sum_{j\ge0}\frac{(9/11)^{2j+1}}{2j+1}
\]

already exceed `23/10`. Hence

\[
9.095<9.2<4\log10
\]

and therefore

\[
\prod_{p<z}(1+p^{-3/5})<10^4.
\]

Now

\[
M^{2/5}=X_0^{161777/900000}>1.2\times10^6
\]

by exact integer/rational exponent comparisons in the checker. Since `rho=6/5`,

\[
\frac{A_M}{M}
<
\rho\,10^4 M^{-2/5}
<\frac1{100}.
\]

Thus

\[
\boxed{A_M<\frac{M}{100}.}
\tag{S3}
\]

This is intentionally conservative. It is a theorem-grade finite bound, not a Dickman-density heuristic.

---

## 4. Exact supported Fourier diagonal

For the order-4 cutoff

\[
H
=
\rho^2X_0^{d-\theta+\eta},
\qquad
 d-\theta+\eta=\frac{7259}{90000},
\]

the checker proves

\[
814<H<815.
\]

Thus the positive frequencies are exactly

\[
1\le h\le814.
\]

For the exact supported `n`-set from (S1), define

\[
f(s)
=
\#\{(n,h):n\mid P(z),\ 4204\le n\le5044,\ 1\le h\le814,\ hn=s\}.
\]

There are

\[
325\cdot814=264550
\]

such pairs. Exact enumeration gives

\[
\max_s f(s)=5
\]

and, more importantly,

\[
\boxed{
\Delta
:=
\sum_s f(s)^2
=314078.
}
\tag{S4}
\]

This replaces the generic diagonal count of order `H N log(HN)` by the actual supported Fourier diagonal at the splice.

---

## 5. Support-sensitive Cauchy inequality

For one factorable top-scale geometric block, absorb the harmless factors `M/m` and `N/n` into the factorable coefficients; their absolute values remain at most one.

For a phase `xi` in the support of the nonnegative order-4 B-spline, write the positive-frequency form

\[
S_+(\xi)
=
\sum_{m\in\mathcal M_z}a_m
\sum_{n\in\mathcal N_z}b_n
\sum_{1\le h\le814}
 e\!\left(\frac{h\xi}{mn}\right).
\]

Cauchy is now applied only over the active outer support:

\[
|S_+(\xi)|^2
\le
A_M
\sum_{m\in\mathcal M_z}
\left|
\sum_{n\in\mathcal N_z}b_n
\sum_{1\le h\le814}
 e\!\left(\frac{h\xi}{mn}\right)
\right|^2.
\]

Because the summand on the right is nonnegative, the outer sum may then be enlarged to the complete consecutive block `(M,rho M]`. This is the key point: the sparse support is consumed in the Cauchy prefactor `A_M`, while the inner reciprocal exponential sum is restored to the complete block on which the explicit constant `15` is already proved.

Let

\[
L_M=\#\{m:M<m\le\rho M\}.
\]

Since `M>1000`,

\[
L_M\le\frac{201}{1000}M.
\]

The diagonal `h_1n_2=h_2n_1` contributes at most

\[
L_M\Delta.
\]

For the off-diagonal put

\[
k=h_1n_2-h_2n_1\ne0.
\]

Since positive frequencies are being used,

\[
|k|\le \rho HN.
\]

The frozen explicit reciprocal lemma gives, uniformly in every supported pair `n_1,n_2`,

\[
\left|
\sum_{M<m\le\rho M}
 e\!\left(\frac{k\xi}{mn_1n_2}\right)
\right|
\le
15\sqrt{\frac{|k|X_0}{Mn_1n_2}}
\le
15\sqrt{\frac{\rho H X_0}{MN}}.
\]

Consequently

\[
\boxed{
|S_+(\xi)|^2
\le
A_M\left[
L_M\Delta
+15B_N^2H^2
\sqrt{\frac{\rho H X_0}{MN}}
\right].
}
\tag{S5}
\]

No `k`-multiplicity saving is used in (S5); all `B_N^2H^2` pairs are still charged. Thus this bound leaves room for later arithmetic grouping.

---

## 6. Explicit top-block constant

For the nonnegative B-spline, Poisson summation can be written by integrating the phase form against `f(t)`. Since

\[
\int f(t)\,dt=y,
\]

and the negative-frequency part is conjugate to the positive-frequency part for the real sieve coefficients,

\[
\frac{|R_{\rm trunc}^{\rm block}|}{y}
\le
\frac{2\sup_\xi|S_+(\xi)|}{MN}.
\]

Insert (S1), (S3), (S4), `H=814` and `L_M<=201M/1000` into (S5). Squaring the normalized bound, the diagonal contribution is at most

\[
\frac{804\Delta}{100000N^2}
<
\frac{143}{10^6}.
\]

For the off-diagonal, use

\[
\sqrt{\rho H}<32
\]

and

\[
\mu+\frac12-\frac52d
=-\frac{52741}{120000}.
\]

The checker proves by exact integer exponentiation at `X_0` that this contribution to the square of the normalized bound is less than

\[
\frac{27}{20000}.
\]

Since

\[
\frac{143}{10^6}+rac{27}{20000}
<
\left(\frac{39}{1000}\right)^2,
\]

we obtain the finite top-block certificate

\[
\boxed{
\frac{|R_{\rm trunc}^{\rm block}(X_0)|}{y}
<\frac{39}{1000}=0.039.
}
\tag{S6}
\]

The preceding order-4 package independently certified

\[
\frac{|R_{\rm tail}^{\rm block}(X_0)|}{y}<0.019.
\]

Therefore

\[
\boxed{
\frac{|R_{\rm block}(X_0)|}{y}
<0.058.
}
\tag{S7}
\]

This is a block-level natural-interval normalization. It is not yet legitimate to subtract `0.058` directly from the source main coefficient `G_*>0.1148`, because the final sieve-count normalization and the aggregation of factorization/geometric pieces have not yet been closed.

---

## 7. What this changes

Before retaining `m,n|P(z)`, the full-support explicit constant pressure test made even one cross-state block look too expensive near the splice. The source support changes that diagnosis.

At the top a6 order-4 block:

\[
\boxed{
\text{truncated cross-state}<0.039y,
\qquad
\text{tail}<0.019y,
\qquad
\text{total}<0.058y.
}
\]

Thus the terminal reciprocal constant `15` is no longer, by itself, an obstruction at the finite splice.

The remaining issue is more sharply typed:

1. sum or orthogonalize the Rosser/Iwaniec factorization pieces without charging the top-block constant by naive triangle inequality;
2. repeat the support-sensitive analysis over the lower geometric sub-blocks and identify the true worst scale;
3. put the aggregate error and `G_*` onto one final-count normalization.

The source factorization count must not be treated as free: the 1980 construction gives finitely many factorable forms, but its raw number may depend very badly on the sieve epsilon. A new aggregation theorem or a scale-sensitive finite census is still required.

No finite analytic P2 threshold, no P2-in-every-square theorem and no Legendre theorem is claimed here.
