# P017 — Centered Incidence Spectral Frontier after Residual-Energy Compression

Status: `PROVED_WIP CRITICAL PHYSICAL-SPACE BOUND + SPECTRAL-GAP REDUCTION / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`;
- `docs/P017_P2_SUPERROOT_COMPLEMENT_DUALITY_20260824.md`;
- `docs/P017_P2_COLLISION_PACKET_COMPRESSION_20260824.md`;
- `docs/P017_P2_RESIDUAL_ENERGY_COMPRESSION_20260826.md`;
- `docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md`.

Purpose: determine exactly how far the newly proved physical-space residual-energy/support compression can be inserted into a factorable bilinear block before any Fourier/exponential-sum cancellation is invoked.

---

## 1. The centered incidence matrix

Let `K>=2`. For odd integers `m,n` with `mn>K`, define

\[
B_{m,n}=O_{mn}(K)\in\{0,1\},
\]

and

\[
\boxed{
A_{m,n}
=B_{m,n}-\frac{K}{mn}
=e_{mn}(K).
}
\]

Thus a factorable parity-projected bilinear remainder over dyadic boxes

\[
\mathcal M=(M,2M],
\qquad
\mathcal N=(N,2N]
\]

is exactly

\[
\boxed{
\mathcal R(a,b;M,N)
=
\sum_{m\in\mathcal M}
\sum_{n\in\mathcal N}
 a_m b_n A_{m,n},
\qquad |a_m|,|b_n|\le1.
}
\]

The density matrix

\[
P_{m,n}=\frac K{mn}
\]

is rank one:

\[
P=Kuv^{\mathsf T},
\qquad
u_m=1/m,
\quad
v_n=1/n.
\]

So the remaining problem is literally a centered-incidence spectral problem:

\[
A=B-P.
\]

---

## 2. P2-R16 — Exact degree envelope for the active incidence graph

Put

\[
T_K
=
\max_{1\le r<(K+1)^2}\tau(r).
\]

For fixed `m`, every edge `B_(m,n)=1` gives a state

\[
x=mna\in I_K
\]

for a unique odd quotient `a`, because `mn>K`.

There are at most

\[
\frac{2K}{m}+1
\]

states in `I_K` divisible by `m`. For each such state, `n` is a divisor of `x/m`, hence has at most `T_K` choices even before imposing the dyadic restriction `N<n<=2N`.

Therefore every row degree satisfies

\[
\boxed{
\deg_B(m)
\le
\left(\frac{2K}{m}+1\right)T_K
\le
\left(\frac{2K}{M}+1\right)T_K.
}
\tag{R16a}
\]

Similarly,

\[
\boxed{
\deg_B(n)
\le
\left(\frac{2K}{N}+1\right)T_K.
}
\tag{R16b}
\]

Hence the Schur bound gives

\[
\boxed{
\|B\|_{2\to2}
\le
T_K
\sqrt{
\left(\frac{2K}{M}+1\right)
\left(\frac{2K}{N}+1\right)
}.
}
\tag{R16c}
\]

Since `T_K=K^(o(1))`, whenever `M,N=K^(positive exponent)` and both are below the root,

\[
\boxed{
\|B\|_{2\to2}
\le
\frac{K^{1+o(1)}}{\sqrt{MN}}.
}
\tag{R16d}
\]

---

## 3. The deterministic density mode is at exactly the same scale

The rank-one density matrix satisfies exactly

\[
\|P\|_{2\to2}
=
K
\left(\sum_{m\in\mathcal M}\frac1{m^2}\right)^{1/2}
\left(\sum_{n\in\mathcal N}\frac1{n^2}\right)^{1/2}.
\]

Since

\[
\sum_{M<m\le2M}\frac1{m^2}\asymp\frac1M,
\qquad
\sum_{N<n\le2N}\frac1{n^2}\asymp\frac1N,
\]

we obtain

\[
\boxed{
\|P\|_{2\to2}
\asymp
\frac K{\sqrt{MN}}.
}
\tag{R17}
\]

Thus the active incidence graph and its deterministic density mode meet at the same critical operator scale.

This is the physical-space form of the parity/root barrier: support compression alone does not separate `B` from its mean mode by a power.

---

## 4. P2-R17 — coefficient-uniform critical bound

For bounded factorable coefficients,

\[
\|a\|_2\le (M+1)^{1/2},
\qquad
\|b\|_2\le (N+1)^{1/2}.
\]

Combining these with (R16c),

\[
\left|
\sum_{m,n}a_mb_nB_{m,n}
\right|
\le
K^{1+o(1)}.
\]

The density piece factorizes exactly:

\[
K\sum_{m,n}\frac{a_mb_n}{mn}
=
K
\left(\sum_m\frac{a_m}{m}\right)
\left(\sum_n\frac{b_n}{n}\right),
\]

and Cauchy gives

\[
\left|
K\sum_{m,n}\frac{a_mb_n}{mn}
\right|
\ll K.
\]

Therefore

\[
\boxed{
|\mathcal R(a,b;M,N)|
\le K^{1+o(1)}
}
\tag{R18}
\]

purely from exact P017 physical-space incidence structure, with no Fourier expansion and no exponent-pair input.

This improves the naive coefficient-uniform level-size envelope `MN` to the square-root critical scale `K`, but it does **not** produce a power below `K`.

---

## 5. Why the raw L2 theorem cannot be mechanically converted into `+1/36`

The residual-energy theorem gives, over the live five-ninth super-root level,

\[
\sum_q|e_q(K)|^2=K^{1+o(1)}.
\]

Applying only Cauchy to a dyadic factorization with `MN=K^(10/9)` gives

\[
|\mathcal R|
\le
(MN)^{1/2}
\left(
\sum_{m,n}|e_{mn}|^2
\right)^{1/2}
\le
K^{19/18+o(1)}.
\]

So energy-only insertion saves `1/18` in the `K` amplitude exponent relative to the naive `K^(10/9)` count, but remains above the critical interval scale.

The degree/mean-mode decomposition (R18) is stronger: it reaches `K^(1+o(1))`.

Therefore the next gain cannot come from taking another square root of the already-proved energy estimate. It must come from cancellation in the **centered operator** `A=B-P`.

---

## 6. The a6 block becomes an explicit spectral-gap target

For the current a6 split, in the `K=sqrt(X)` variable,

\[
M=X^{31/72}=K^{31/36},
\qquad
N=X^{1/8}=K^{1/4},
\]

so

\[
MN=K^{10/9}.
\]

The critical operator scale is therefore

\[
\frac K{\sqrt{MN}}
=K^{4/9}.
\]

The coefficient-vector norm scale is

\[
\sqrt{MN}=K^{5/9}.
\]

Consequently, if one can prove the centered spectral estimate

\[
\boxed{
\|A\|_{2\to2}
\ll K^{4/9-\gamma}
}
\tag{SG-gamma}
\]

for any fixed `gamma>0`, then

\[
\boxed{
|\mathcal R|
\ll K^{1-\gamma}.
}
\]

The actual short-interval length in the a6 package is

\[
y=X^{4999/10000}=K^{4999/5000}=K^{1-1/5000}.
\]

Hence asymptotically it is enough to prove

\[
\boxed{
\gamma>\frac1{5000}.
}
\tag{R19}
\]

This is a much narrower target than replaying the full generic Iwaniec-Laborde power room with explicit constants.

The source Lemma-4 Fourier/Cauchy argument can now be interpreted as one way of proving a substantially stronger centered spectral gap. The P017-specific question is whether the disjoint complement windows, small collision cores and exact square numerator allow a weaker but much more explicit gap `gamma>1/5000`.

---

## 7. Role of collision compression

The frozen same-state collision theorem controls only the diagonal-in-state part of the active incidence second moment. It does not automatically control pairs of moduli which are active at two different states in the square basin.

Thus

\[
\boxed{
\text{same-state collision compression}
\ne
\text{full centered spectral gap}.
}
\]

This explains why the already-proved `K^(1+o(1))` collision tuple envelope cannot simply be substituted for the Fourier off-diagonal in Lemma 4.

What the a6 collision theorem still contributes is precise removal of one structured part of the Gram kernel: every distinct-prime terminal same-state collision has small packet core

\[
Q<z^2+1.
\]

The irreducible residue is therefore a **cross-state centered correlation** problem.

---

## 8. New hard frontier

The previous support/energy question is closed. The exact remaining problem is now:

> prove an explicit centered-incidence spectral gap `gamma>1/5000` for the a6 factorable block, after removing the `Q<z^2+1` same-state collision carrier; or prove that square-complement geometry alone cannot yield such a gap, in which case generic Fourier constants must be paid on the cross-state sector only.

This is the correct insertion theorem target. No automatic addition of `1/36` to the existing Lemma-4 exponent is authorized.

No P2-in-every-square theorem, no Legendre theorem and no finite analytic threshold is claimed here.
