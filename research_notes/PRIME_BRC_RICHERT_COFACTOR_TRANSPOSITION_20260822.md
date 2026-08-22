# Prime-BRC — Richert Cofactor Transposition / Prefix Recoalescence

Status: `L3 OWNER-LOCAL RESEARCH NOTE / PROVED FINITE IDENTITIES / NO P2 CLAIM`
Date: `2026-08-22`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. Purpose

Connect the exact P017 first-factor cofactor windows to the weighted sifting term used in Campbell's 2026 explicit P3 theorem for consecutive-square intervals. The goal is not to claim P2. The goal is to change the order of two operations:

`sum shell remainders -> absolute value`

instead of

`absolute value shell remainder -> sum`.

The legality comes from L054: the exact cofactor windows are pairwise disjoint.

## 2. Exact shell transposition

For a prime `p<=k`, let

\[
W_p(k)=\left[\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor\right].
\]

For `z<=p`, an element `n=pq` in the square basin is free of prime divisors `<z` iff its cofactor `q` is free of prime divisors `<z`. Hence

\[
S(\mathcal A_p,\mathcal P,z)=S(W_p(k),\mathcal P,z).
\]

For `k>=4`, L054 gives

\[
p\ne r\Longrightarrow W_p(k)\cap W_r(k)=\varnothing.
\]

Thus for ordered primes

\[
z\le p_1<\cdots<p_m<y
\]

we may form genuine disjoint prefix sets

\[
Q_j=\bigsqcup_{i\le j}W_{p_i}(k).
\]

## 3. Abel-prefix recoalescence theorem

Let

\[
w_1\ge w_2\ge\cdots\ge w_m\ge0,
\qquad w_{m+1}=0.
\]

Then for any additive set functional `S` on disjoint unions,

\[
\boxed{
\sum_{i=1}^m w_i S(W_{p_i})
=
\sum_{j=1}^m (w_j-w_{j+1})S(Q_j).
}
\]

Proof: the coefficient of `S(W_{p_i})` on the right is

\[
\sum_{j\ge i}(w_j-w_{j+1})=w_i.
\]

For Richert weights

\[
w_i=1-\frac{\log p_i}{\log y},
\]

this is the exact discrete form of the prefix-integral representation.

## 4. Aggregate remainder identity

For squarefree `d` built from primes `<z`, write

\[
r_i(d)=|W_{p_i,d}|-\frac{|W_{p_i}|}{d}.
\]

Because the windows are disjoint,

\[
|Q_{j,d}|=\sum_{i\le j}|W_{p_i,d}|,
\qquad
|Q_j|=\sum_{i\le j}|W_{p_i}|,
\]

hence

\[
\boxed{
r_{Q_j}(d)=\sum_{i\le j}r_i(d).
}
\]

For the square basin this is equivalently

\[
r_i(d)=H_{p_i d}(k)-\frac{H_{p_i}(k)}d.
\]

## 5. BRC-before-absolute-value inequality

Fix any common finite collection `D` of squarefree sieve moduli. Then

\[
\boxed{
\sum_j(w_j-w_{j+1})\sum_{d\in D}|r_{Q_j}(d)|
\le
\sum_iw_i\sum_{d\in D}|r_i(d)|.
}
\]

Proof: for every `(j,d)`,

\[
|r_{Q_j}(d)|
=\left|\sum_{i\le j}r_i(d)\right|
\le\sum_{i\le j}|r_i(d)|.
\]

Multiply by the nonnegative Abel increment, sum over `j,d`, and exchange sums. The coefficient of `|r_i(d)|` is again `w_i`.

This is an unconditional semantic gain: prefix recoalescence never worsens a remainder bound when the same modulus set is used.

## 6. Reciprocal sawtooth form

Let `L=k^2` and `U=k(k+2)`. For the interval-multiple count,

\[
H_m(k)=\left\lfloor\frac U m\right\rfloor-
\left\lfloor\frac L m\right\rfloor.
\]

Therefore

\[
r_p(d)=H_{pd}(k)-\frac{H_p(k)}d
\]

is an exact reciprocal fractional-part discrepancy. Writing `{x}` for fractional part,

\[
\boxed{
r_p(d)=
\left\{\frac L{pd}\right\}-\left\{\frac U{pd}\right\}
-\frac1d\left(
\left\{\frac Lp\right\}-\left\{\frac Up\right\}
\right).
}
\]

Thus the unresolved analytic task is a prefix sum of reciprocal sawtooth discrepancies over primes, not a new divisibility predicate.

## 7. Campbell interface and scope boundary

Campbell's 2026 explicit P3 proof bounds the weighted sifting term shell-by-shell and bounds its remainder contribution using `|r_p(d)|<=1` before summing over `p`. The present transposition shows that the square-basin cofactor geometry permits a lawful alternative ordering for a common sieve-level slice:

`disjoint cofactor windows -> prefix union -> aggregate remainder -> absolute value`.

This note does not claim that Campbell's varying levels `D_p` can simply be replaced by one larger level. The main-term/remainder tradeoff must be re-optimised for each prefix. In particular, a P2 result would require proving that aggregate cancellation is strong enough to support a materially higher effective sieve level or an Iwaniec/Type-II-style flexible remainder.

## 8. Numerical pressure-test status

Owner-local experiments, restricted to squarefree `d|P(z)` but before imposing the exact Campbell `d<QD_p` level geometry, gave prefix-recoalesced / shellwise weighted L1 remainder ratios approximately

- `k=10^4`: `0.182`;
- `k=10^5`: `0.116`;
- `k=10^6`: `0.092`.

These are diagnostics only. They are not theorem evidence and are not used in Sections 2–5.

## 9. Current hard target

Freeze the next question as

\[
\boxed{
\text{Can }R_t(D)=\sum_{d<QD}|r_{Q_t}(d)|
\text{ be bounded strongly enough to raise the usable prefix sieve level?}
}
\]

A mere reduction of the raw remainder is insufficient. The full upper-sieve main term `F(log D/log z)` plus the aggregate remainder must improve.

## 10. Negative boundary

Do not claim:

- `P2 proved`;
- `parity barrier bypassed`;
- arbitrary signed cancellation inside Boolean BRC;
- varying Campbell levels are automatically compatible with the common-cutoff inequality;
- numerical cancellation ratios imply a power saving.

The durable result here is the exact transposition and the BRC-before-absolute-value inequality.