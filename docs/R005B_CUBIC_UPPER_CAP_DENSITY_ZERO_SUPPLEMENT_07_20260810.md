# R005-B — Cubic Upper-Cap Density-Zero Transfer

Status: `PROVED WIP / EXTERNAL ALMOST-ALL PRIME INPUT / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 02–06

## 1. Result

The unresolved cubic question is whether upper-cap non-forcing occurs finitely
or infinitely often. Current all-interval prime-gap technology does not decide
that.

However, the exact horizon-gap geometry plus classical **almost-all short
interval** results do prove a global sparsity theorem.

Let

\[
\mathcal O_3(K)=\{k\in[K,2K]\cap\mathbb Z:R_kS_k>U_k\},
\]

where

\[
U_k=(k+1)^3-1,\quad S_k=\lfloor\sqrt{k^3}\rfloor,\quad
F_k=\lfloor\sqrt{U_k}\rfloor,\quad
R_k=\operatorname{nextprime}(F_k).
\]

Thus `O_3(K)` is the set of cubic basins whose **raw upper horizon window
opens**. Every actual cubic pure-cap non-forcing event belongs to `O_3(K)`.

Using Jia's 1996 theorem that intervals of length `n^(1/20+epsilon)` contain a
prime for almost all integers n, one obtains

\[
\boxed{|\mathcal O_3(K)|=o(K).}
\]

Consequently,

\[
\boxed{\#\{k\in[K,2K]:\operatorname{NonForcedCap}_{3,k}\ne\varnothing\}=o(K).}
\]

So cubic upper-cap failures have natural density zero.

This is **not** a finiteness theorem. An infinite zero-density exceptional set
remains possible.

---

## 2. External input

Chaohua Jia, *Almost all short intervals containing prime numbers*,
Acta Arithmetica 76 (1996), 21–84, DOI `10.4064/aa-76-1-21-84`, proved the
exponent `1/20` almost-all short-interval result.

For this transfer it is enough to use the following consequence. Choose any
fixed exponent

\[
\boxed{\frac1{20}<\theta<\frac13.}
\]

Then, among integers `n` of size `X`, all but `o(X)` have a prime in

\[
[n,n+n^\theta].
\]

The exact value `1/20` is not structurally important for R005-B; only
`theta<1/3` matters.

More recent work has shortened the almost-all interval further. Those
improvements are not needed for the density-zero theorem.

---

## 3. Cubic horizon scale

For `k` in one dyadic block `[K,2K]`, put

\[
X=K^{3/2},\qquad H=K^{1/2}=X^{1/3}.
\]

The cubic factor horizon satisfies

\[
F_k\asymp X.
\]

From the exact horizon-gap threshold of Supplements 02 and 05,

\[
g_{0,k}=\frac{U_k}{S_k}-F_k\sim\frac32\sqrt{k}.
\]

Hence there is an absolute constant `c>0` such that, for all sufficiently large
`K` and every `k in [K,2K]`,

\[
g_{0,k}\ge cH.
\]

Therefore an opening event `R_kS_k>U_k` forces the actual prime-free interval

\[
(F_k,R_k)
\]

to have length

\[
\boxed{R_k-F_k>g_{0,k}\gg H=X^{1/3}.}
\]

So every cubic upper-cap opening sits inside a genuinely long consecutive-prime
gap at the horizon scale.

---

## 4. One long prime gap creates many almost-all exceptions

Fix a consecutive-prime gap `(P,R)` of length `G=R-P` in the range relevant to
`F_k`, and suppose it contains at least one opening sample `F_k`.

Then

\[
G\gg X^{1/3}.
\]

Because `theta<1/3`,

\[
X^\theta=o(X^{1/3})=o(G).
\]

For every integer `n` satisfying

\[
P+C X^\theta<n<R
\]

with a fixed sufficiently large constant `C`, the whole interval
`[n,n+n^theta]` remains inside the prime-free gap `(P,R)`.

Hence all such `n` are exceptional to the almost-all short-interval theorem.
For sufficiently large `X`, this produces

\[
\boxed{\gg G}
\]

exceptional integers from that one prime gap.

Distinct consecutive-prime gaps are disjoint, so summing over all relevant
opening gaps gives

\[
\boxed{\sum_{\text{opening gaps}}G=o(X).}
\]

---

## 5. The collapse samples are spaced at the same 1/3 scale

The cubic horizon samples themselves satisfy

\[
F_{k+1}-F_k\sim\frac32\sqrt{k}.
\]

Thus throughout `k in [K,2K]`,

\[
\boxed{F_{k+1}-F_k\gg H=X^{1/3}}
\]

for sufficiently large `K`.

A prime gap of length `G` can therefore contain at most

\[
O\left(1+\frac GH\right)
\]

sample horizons `F_k`. Since every opening gap already has `G\gg H`, this is
`O(G/H)`.

Summing over the distinct opening gaps,

\[
|\mathcal O_3(K)|\ll\frac1H\sum_{\text{opening gaps}}G
=\frac{o(X)}{X^{1/3}}.
\]

Since `X^(2/3)=K`,

\[
\boxed{|\mathcal O_3(K)|=o(K).}
\]

---

## 6. Consequence for actual upper-cap non-forcing

Supplement 06 gives the stronger exact event criterion

\[
Q_kF_k>k^3,\qquad Q_kR_k>U_k,
\]

where `Q_k` is the largest prime at or below `S_k`.

Because `Q_k<=S_k`, the second inequality implies

\[
R_kS_k>U_k.
\]

Therefore actual upper-cap failures are a subset of the opening set, and hence
have density zero.

So even if cubic upper-cap failures are infinite, they must be asymptotically
sparse.

---

## 7. Why sparse sampling does not defeat the almost-all theorem

A naive objection is valid but incomplete: the sequence `F_k` has only about
`X^(2/3)` samples below size X, while an `o(X)` exceptional set could in
principle contain all of them.

The transfer does **not** restrict Jia's exceptional set directly to the sparse
sequence. Instead, one opening `F_k` forces a prime-free interval of length
`~X^(1/3)`. That same long gap manufactures `~X^(1/3)` ordinary exceptional
integers for the almost-all theorem.

This exactly compensates for the `X^(1/3)` spacing of the collapse samples.

The argument is therefore a **gap-thickening transfer**:

\[
\boxed{\text{sparse horizon sample}\to\text{long prime-free gap}
\to\text{many ordinary exceptional integers}\to\text{density-zero sample events}.}
\]

---

## 8. Optional modern quantitative refinement

Runbo Li's 2025 preprint *Primes in almost all short intervals II* states a
quantitative theorem: for fixed admissible parameters, intervals of length
`n^(1/22+epsilon)` fail to contain primes for only

\[
O\left(X(\log X)^{-B}\right)
\]

integers `n in [X,2X]`.

If one accepts that preprint input, the same gap-thickening proof upgrades the
density statement to a log-power sparse estimate of the form

\[
\boxed{|\mathcal O_3(K)|\ll_B K(\log K)^{-B}}
\]

with the usual dependence on the fixed theorem parameters.

This quantitative refinement is explicitly **PREPRINT INPUT / NOT REQUIRED**
for the peer-reviewed Jia-based density-zero theorem.

---

## 9. What remains open

The theorem does not answer whether the cubic upper-cap exceptional set is
finite or infinite. It also does not touch the lower cofactor-gap band.

The next structural targets are:

1. upper cap: determine whether the two-boundary-prime event has infinitely many
   solutions despite density zero;
2. lower band: apply the corrected reciprocal-gap criterion separately;
3. only then combine the two bands into a statement about full cubic forcing.

---

## 10. Prior-art boundary

Prime numbers in almost all short intervals are classical analytic number
theory. R005-B claims no novelty for Jia's theorem or later improvements.

The project-side contribution under test is the exact transfer mechanism from
the collapse-derived horizon opening condition to a density statement on the
sampled cubic basins. Historical novelty of that transfer has not yet been
audited.
