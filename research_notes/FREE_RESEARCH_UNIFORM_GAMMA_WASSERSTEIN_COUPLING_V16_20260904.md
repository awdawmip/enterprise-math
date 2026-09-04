# Free Research — Uniform All-Depth Gamma Coupling in Logarithmic Scale

Status: `FREE_RESEARCH_FRONTIER / CONDITIONAL_ONE_STEP_W1 / ALL_DEPTH_ERROR_NO_ACCUMULATION / GROWING_DEPTH_BLOCK_OVERLAP_CLOSED / MATCHED_VALUE_RELATION_ENERGY_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_ADAPTIVE_HISTORY_GAMMA_OVERLAP_V16_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the first-mass discrepancy, Chebyshev floor control, adaptive quotient Markov chain, and finite coupling calculus.

## 1. Executive advance

The fixed-depth restriction in the first Gamma-overlap note can be removed at the level actually needed for logarithmic block coupling.

Let

\[
T=\log N.
\]

After `k` adaptive prime-power quotient steps, let

\[
S_{N,k}:=\frac{\log M_k}{T}\in[0,1]
\]

be the actual remaining logarithmic scale.  Let

\[
G_k:=U_1\cdots U_k
\]

be the ideal product of independent `Uniform(0,1)` variables.

There is a coupling, uniform in the history depth `k`, such that

\[
\boxed{
\mathbb E|S_{N,k}-G_k|
\le\frac{C_*}{\log N}.}
\tag{1.1}
\]

The key cancellation is scale covariance.  At an intermediate logarithmic size `t`, the conditional prime-power ratio differs from a uniform ratio by `O(1/(1+t))` in Wasserstein distance.  Multiplying by the current relative scale `t/T` turns this into `O(1/T)`, independently of how small the intermediate state has become.  The remaining previous-step error is multiplied by a fresh uniform variable of mean `1/2`.

Therefore the all-depth error obeys

\[
D_{k+1}\le\frac C T+\frac12D_k,
\]

and never accumulates beyond `2C/T`.

For `K` equal logarithmic blocks, this gives a block total-variation error

\[
\boxed{
\operatorname{TV}
\bigl(\operatorname{Block}_K(S_{N,k}),
\operatorname{Block}_K(G_k)\bigr)
\ll\frac K{\sqrt{\log N}},}
\tag{1.2}
\]

uniformly in `k`.  Consequently the overlap between the actual depth-`k` and depth-`k+1` laws satisfies

\[
\boxed{
L_{N,k,K}
\ge
1-e^{-k}\frac{k^k}{k!}
-\frac1K
-O\!\left(\frac K{\sqrt{\log N}}\right),}
\tag{1.3}
\]

again uniformly in `k`.

This closes the growing-depth arithmetic-distribution problem.  The only remaining part of the parity argument is value-sensitive: control the relation energy of actual endpoints lying in the same logarithmic block.

---

## 2. One-step conditional logarithmic kernel

For an integer state `m>=2`, put

\[
t:=\log m,
\qquad
R_m(q):=rac{\log\lfloor m/q\rfloor}{t}
\]

for prime powers `q<=m`, with `R_m(q)=0` when the quotient is `1`.  Give `q` probability

\[
p_m(q)=\frac{\omega(q)}{A(m)},
\qquad
\omega(q)=\frac{\Lambda(q)}q.
\]

Let `K_m` be the law of `R_m(q)` and let `U` denote the uniform law on `[0,1]`.

The first-mass estimate

\[
A(x)=\log x+O(1)
\tag{2.1}
\]

implies that the nonfloor ratio

\[
\widetilde R_m(q)=1-\frac{\log q}{t}
\]

has Kolmogorov discrepancy `O(1/(1+t))` from `U`.  In one dimension,

\[
W_1(\operatorname{Law}(\widetilde R_m),U)
=\int_0^1|F_m(u)-u|\,du
\ll\frac1{1+t}.
\tag{2.2}
\]

The floor deformation is smaller.  For `q<=m/2`,

\[
0\le\log(m/q)-\log\lfloor m/q\rfloor
\le\frac{2q}{m}.
\]

Thus

\[
\begin{aligned}
\mathbb E
\left|\widetilde R_m-R_m\right|
&\le\frac1{tA(m)}
\left[
\frac2m\sum_{q\le m/2}\Lambda(q)
+O(A(m)-A(m/2))
\right]\\
&\ll\frac1{t(1+t)}.
\end{aligned}
\tag{2.3}
\]

Here `psi(m)=O(m)` is the existing Chebyshev input.  Enlarging the constant to cover the finite initial range gives

\[
\boxed{
W_1(K_m,U)\le\frac C{1+\log m}}
\tag{2.4}
\]

for every `m>=1`, with an arbitrary absorbing convention at `m=1`.

---

## 3. Scale-covariant recursive coupling

Let

\[
T_{N,k}:=\log M_k,
\qquad
S_{N,k}:=T_{N,k}/T.
\]

Suppose `S_(N,k)` has already been coupled to

\[
G_k=U_1\cdots U_k.
\]

Conditionally on the actual state `M_k`, use an optimal one-dimensional coupling between the next actual ratio `R_(M_k)` and a fresh uniform variable `U_(k+1)`, chosen from a fresh independent quantile seed.  Then `U_(k+1)` is independent of the previous ideal history.

The next scales are

\[
S_{N,k+1}=S_{N,k}R_{M_k},
\qquad
G_{k+1}=G_kU_{k+1}.
\]

Therefore

\[
\begin{aligned}
|S_{N,k+1}-G_{k+1}|
&\le S_{N,k}|R_{M_k}-U_{k+1}|\\
&\quad+U_{k+1}|S_{N,k}-G_k|.
\end{aligned}
\]

The conditional expectation of the first term is bounded by

\[
\frac{T_{N,k}}T\frac C{1+T_{N,k}}
\le\frac C T.
\]

The expectation of the second is

\[
\mathbb E[U_{k+1}]D_k=\frac12D_k,
\]

where

\[
D_k:=\mathbb E|S_{N,k}-G_k|.
\]

Hence

\[
\boxed{
D_{k+1}\le\frac C T+\frac12D_k.}
\tag{3.1}
\]

Since `D_0=0`,

\[
\boxed{
D_k\le\frac{2C}{T}
\qquad\text{for every }k>=0.}
\tag{3.2}
\]

No fixed-depth restriction remains.  Absorption at `M_k=1` causes no singularity because its current relative scale `S_(N,k)` is zero.

---

## 4. From Wasserstein coupling to block total variation

Partition `[0,1]` into the `K` equal blocks

\[
I_j=[(j-1)/K,j/K].
\]

Let `B_K(x)` be the block index.  Couple `S_(N,k)` and `G_k` as in Section 3.  For `0<epsilon<1/(2K)`, different block indices imply either

\[
|S_{N,k}-G_k|>\varepsilon
\]

or `G_k` lies within `epsilon` of an internal block boundary.  Therefore

\[
\Pr\{B_K(S_{N,k})\ne B_K(G_k)\}
\le\frac{D_k}{\varepsilon}
+\gamma_k(\partial_\varepsilon),
\tag{4.1}
\]

where `gamma_k` is the product-uniform law.

Its density is

\[
f_k(s)=\frac{(-\log s)^{k-1}}{(k-1)!}.
\]

Every internal boundary neighborhood lies in

\[
s\ge\frac1{2K}.
\]

Writing `y=-log s<=log(2K)`, uniformly over every `k>=1`,

\[
\frac{y^{k-1}}{(k-1)!}
\le e^y\le2K.
\tag{4.2}
\]

There are at most `K-1` internal boundaries, so

\[
\gamma_k(\partial_\varepsilon)\le4\varepsilon K^2.
\tag{4.3}
\]

Using `D_k<=2C/T` and choosing

\[
\varepsilon=\frac{\sqrt{D_k}}{2K}
\]

gives

\[
\boxed{
\operatorname{TV}
\bigl(B_K(S_{N,k}),B_K(G_k)\bigr)
\le4K\sqrt{D_k}
\ll\frac K{\sqrt T}.}
\tag{4.4}
\]

The bound is uniform in the history depth.

---

## 5. Uniform consecutive-depth overlap

For two probability vectors `p,q`, their overlap is

\[
L(p,q)=\sum_j\min(p_j,q_j)=1-\operatorname{TV}(p,q).
\]

It is Lipschitz in each argument for total variation.  Therefore (4.4) at depths `k` and `k+1` gives

\[
L_{N,k,K}
\ge L_{k,K}-O(K/\sqrt T),
\tag{5.1}
\]

where `L_(k,K)` is the ideal block overlap.

The ideal densities cross once, at `s=e^-k`, so only one block differs from the exact continuum overlap.  Hence

\[
L_{k,K}
\ge1-e^{-k}\frac{k^k}{k!}-\frac1K.
\tag{5.2}
\]

Combining the two proves (1.3).

One may choose, for example,

\[
K=\lfloor T^{1/4}\rfloor.
\]

Then both block-discretization and arithmetic-coupling errors are

\[
O(T^{-1/4}),
\]

uniformly in `k`:

\[
\boxed{
L_{N,k,K}
\ge1-e^{-k}\frac{k^k}{k!}-O(T^{-1/4}).}
\tag{5.3}
\]

---

## 6. Consequence for growing parity depth

Take

\[
k=\lfloor c\log T\rfloor
=\lfloor c\log\log N\rfloor
\]

for any fixed `c>0`.  Stirling gives

\[
e^{-k}\frac{k^k}{k!}
=O(k^{-1/2})
=O((\log\log N)^{-1/2}).
\]

With `K=T^(1/4)`, (5.3) yields

\[
\boxed{
1-L_{N,k,K}
=O((\log\log N)^{-1/2})
+O((\log N)^{-1/4}).}
\tag{6.1}
\]

Thus the **distributional** unmatched parity mass tends to zero at an explicit rate even when history depth grows like `log log N`.

This is stronger than the originally anticipated error `e^k/log N`: scale covariance prevents such accumulation.

---

## 7. What remains value-sensitive

The block coupling inequality gives, for a bounded readout `f`,

\[
\frac12|\mu_{N,k+1}(f)-\mu_{N,k}(f)|
\le
(1-L_{N,k,K})\|f\|_\infty
+\sqrt{L_{N,k,K}\mathcal V_{N,k,K}(f)}.
\tag{7.1}
\]

Section 6 makes the first term explicitly small at growing depth.  The second term is the pooled relation energy of actual depth-`k` and depth-`k+1` endpoints lying in the same logarithmic block.

Wasserstein proximity alone cannot control it for an arbitrary, nonsmooth arithmetic readout.  Doing so would silently assume the very regularity of `r` that the native remainder program is trying to prove.

The remaining theorem is therefore purely an energy intertwiner:

\[
\boxed{
\mathcal V_{N,k,K}(r)
\le
\text{retained }S_3\text{ standard history energy}
+\text{summable residual/lower-scale terms}.}
\tag{7.2}
\]

All distributional and growing-depth errors have now been removed from this target.

---

## 8. Current classification

Closed at research-note theorem strength:

1. conditional one-step `W_1` discrepancy `O(1/(1+log m))`;
2. scale-covariant recursion `D_(k+1)<=C/T+D_k/2`;
3. all-depth coupling `D_k=O(1/log N)`;
4. block total-variation error `O(K/sqrt(log N))`, uniform in `k`;
5. growing-depth overlap formula (1.3);
6. explicit choice `K=(log N)^(1/4)`;
7. unmatched parity mass `O((log log N)^-1/2)+(log N)^-1/4` at depth `c log log N`.

Open:

1. value-sensitive matched block relation energy (7.2);
2. its exact composition with the persistent row mixer;
3. a closed multidepth scalar inequality;
4. any promoted quantitative prime remainder;
5. any RH-scale conclusion.

The frontier has therefore moved from a triangular-array distribution problem to one finite positive relation-energy comparison.
