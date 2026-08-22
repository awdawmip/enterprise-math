# Prime-BRC — Richert Cofactor Transposition / Prefix Recoalescence

Status: `L3 OWNER-LOCAL RESEARCH NOTE / PROVED FINITE IDENTITIES / NO P2 CLAIM`
Date: `2026-08-22`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. Purpose

Connect P017 first-factor cofactor geometry to the weighted sifting term in Campbell's 2026 explicit P3 theorem. The goal is not to claim P2. The exact gain is to allow

`sum shell remainders -> absolute value`

instead of

`absolute value shell remainder -> sum`.

## 2. Endpoint discipline

Canonical P017 uses the full open consecutive-square basin

\[
I_k=\{k^2+1,\ldots,k^2+2k\},
\]

so its raw cofactor window is

\[
W_p(k)=\left[\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k^2+2k}{p}\right\rfloor\right].
\]

Campbell instead uses

\[
\mathcal A(k^2)=\mathbb Z\cap(k^2,k^2+2k),
\]

which excludes the final integer `k^2+2k`. Therefore the exact Campbell-compatible subwindow is

\[
\boxed{
W_p^C(k)=\left[\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k^2+2k-1}{p}\right\rfloor\right].
}
\]

Every `W_p^C` is a subwindow of `W_p`, so L054's strict cross-shell separation immediately implies the Campbell subwindows are pairwise disjoint for `k>=4`.

For `z<=p`, an element `n=pq` of Campbell's `A_p` is free of prime divisors `<z` iff `q` is free of those primes. Hence

\[
\boxed{S(\mathcal A_p,\mathcal P,z)=S(W_p^C(k),\mathcal P,z).}
\]

All Campbell-facing statements below use `W_p^C`, not the one-state-larger canonical P017 window.

## 3. Abel-prefix recoalescence theorem

Let

\[
z\le p_1<\cdots<p_m<y
\]

be primes and set

\[
Q_j=\bigsqcup_{i\le j}W_{p_i}^C(k).
\]

Let

\[
w_1\ge\cdots\ge w_m\ge0,
\qquad w_{m+1}=0.
\]

Then

\[
\boxed{
\sum_{i=1}^m w_i S(W_{p_i}^C,z)
=
\sum_{j=1}^m(w_j-w_{j+1})S(Q_j,z).
}
\]

For Richert weights

\[
w_i=1-\frac{\log p_i}{\log y},
\]

this is the exact discrete prefix form of Campbell's weighted sifting term.

## 4. Aggregate remainder identity

For squarefree `d|P(z)`, define

\[
r_i^C(d)=|(W_{p_i}^C)_d|-\frac{|W_{p_i}^C|}{d}.
\]

Disjointness gives

\[
\boxed{r_{Q_j}(d)=\sum_{i\le j}r_i^C(d).}
\]

Equivalently, if

\[
H_m^C(k)=\left\lfloor\frac{k^2+2k-1}{m}\right\rfloor-
\left\lfloor\frac{k^2}{m}\right\rfloor,
\]

then

\[
\boxed{r_p^C(d)=H_{pd}^C(k)-\frac{H_p^C(k)}d.}
\]

Writing

\[
A_p=\left\lfloor\frac{k^2}{p}\right\rfloor,
\qquad B_p^C=\left\lfloor\frac{k^2+2k-1}{p}\right\rfloor,
\]

nested floor division gives the exact residue form

\[
\boxed{
r_p^C(d)=\frac{(A_p\bmod d)-(B_p^C\bmod d)}d.}
\]

## 5. BRC-before-absolute-value theorem

Fix any common finite collection `D` of squarefree sieve moduli. Then

\[
\boxed{
\sum_j(w_j-w_{j+1})\sum_{d\in D}|r_{Q_j}(d)|
\le
\sum_iw_i\sum_{d\in D}|r_i^C(d)|.
}
\]

This follows immediately from

\[
|r_{Q_j}(d)|=\left|\sum_{i\le j}r_i^C(d)\right|
\le\sum_{i\le j}|r_i^C(d)|
\]

and Abel summation. Thus, whenever the same modulus slice is legal on both sides, prefix recoalescence before absolute value can never worsen the remainder estimate.

## 6. Second-order reciprocal-floor form

Define

\[
A_t(x)=\sum_{z\le p<t}\left\lfloor\frac{x}{p}\right\rfloor.
\]

For a prime prefix `z<=p<t`, its aggregate remainder is

\[
\boxed{
R_t^C(d)
=
[A_t((k^2+2k-1)/d)-A_t(k^2/d)]
-\frac1d[A_t(k^2+2k-1)-A_t(k^2)],
}
\]

with floors interpreted through the preceding exact residue formula. Since

\[
A_t(x)=x\sum_{z\le p<t}\frac1p-
\sum_{z\le p<t}\left\{\frac{x}{p}\right\},
\]

the entire linear reciprocal-prime main term cancels in this scale-difference. The analytic obstruction is therefore a second-order fractional-part discrepancy, not the first-order Mertens term.

## 7. Campbell interface

Campbell's Proposition 3.5 applies the explicit linear sieve separately to each `A_p`, at level

\[
D_p=X^{1/2-\alpha}/p,
\]

and its remainder is

\[
\sum_{d\mid P(z),\ d<QD_p}|r_p(d)|.
\]

The present theorem permits a different legal organisation for a common level slice:

`disjoint cofactor subwindows -> prefix union -> aggregate remainder -> absolute value`.

It does **not** prove that Campbell's varying `D_p` may simply be replaced by one larger common level. The real question is whether the aggregate prefix remainder stays small enough that Lemma 2.2 can be applied to each prefix at a materially larger optimised `D_j`, after paying the corresponding upper-sieve main term `F(log D_j/log z)`.

## 8. Numerical status and correction

Earlier owner-local cancellation ratios were computed on the full P017 window. Because Campbell omits the final state, those numbers are retained only as historical diagnostics and must not be quoted as exact Campbell-set values. The structural theorem is unaffected; Campbell-compatible numerical experiments must use `W_p^C` going forward.

## 9. Current hard target

\[
\boxed{
\text{Optimise for each prefix }Q_j:
|Q_j|V(z)F(\log D_j/\log z)+
\sum_{d<QD_j}|r_{Q_j}(d)|.
}
\]

The route survives only if the optimised `D_j` is systematically larger than the per-shell Campbell level and the full weighted bound improves enough to matter for the P2 Richert inequality.

## 10. Negative boundary

No claim is made that:

- P2 is proved;
- the parity barrier is bypassed;
- numerical cancellation is a power saving;
- arbitrary signed cancellation is available in Boolean BRC;
- the endpoint difference is negligible in an exact proof.

The durable result is the exact Campbell-compatible transposition, Abel prefix identity, and BRC-before-absolute-value inequality.