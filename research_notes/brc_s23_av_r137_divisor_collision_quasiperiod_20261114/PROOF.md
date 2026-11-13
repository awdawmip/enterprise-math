# R137 — Divisor-collision formula and affine-periodic jump counts for the tied S23 observer

Date: 2026-11-14 (Asia/Shanghai). Status: AUTHOR-SIDE MATHEMATICS / NOT_REVIEWED.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: R136 at immutable commit `73438a02082bf7ee60ccd656f66ac87d753d5a11`.
Scope: the exact external one-parameter S23 auxiliary model, not an X6 native Cell/Link/Port assertion.

## Question and definitions

For integers `K>=2, m>=1`, write `L=K-1` and
\[
 S_i^{(K)}(\theta)=\lfloor(L+i+1)\theta\rfloor-\lfloor(L+i)\theta\rfloor,\quad 0\le i<m,\quad 0<\theta<1.
\]
As proved in R136, the number `J(K,m)` of genuine chronological word-jump locations equals the number of distinct reduced fractions in the union of `{a/n: 1<=a<n, L<=n<=L+m}`. A word appearing at a jump equals its right-hand neighboring word. This result counts *temporal jumps*, not distinct binary words.

Let `phi(q)` denote Euler's totient function, and put
\[
 t_q(L,m)=\left\lfloor\frac{L+m}{q}\right\rfloor-
           \left\lfloor\frac{L-1}{q}\right\rfloor.
\]

## Theorem R137.1 (short exact collision formula)

For all `K>=2, m>=1` the jump count is
\[
 \boxed{J(K,m)=(m+1)(K-2)+\frac{m(m+1)}2
 -\sum_{q=2}^{m}\varphi(q)\big(t_q(K-1,m)-1\big).} \tag{1}
\]
The sum is empty if `m=1`. Consequently, after a totient sieve up to `m`, exact `J(K,m)` can be evaluated with `O(m)` integer divisions and arithmetic operations on `O(\log K+\log m)`-bit integers. The sieve takes `O(m\log\log(m+2))` elementary operations. Thus exact jump *counting* is polynomial in `m` and the binary input length of `K` without generating any of the `J` event fractions.

**Proof.** Every interior cut of `floor(n theta)` is a rational `a/n` with `1<=a<n`. Its reduced denominator `q>=2` divides `n`. There are `phi(q)` reduced fractions with that denominator. In the multiset of all floor cuts for `L<=n<=L+m`, each such fraction has multiplicity `t_q`; in the union its multiplicity is one if `t_q>0`. Each `n` contributes exactly `n-1` cuts, whence the total multiset count is
\[
 C=\sum_{n=L}^{L+m}(n-1)=(m+1)(K-2)+m(m+1)/2.
\]
When `q>m`, two distinct indices in an interval of length `m` cannot both be divisible by `q`, so `t_q<=1`. When `2<=q<=m`, every block of `m+1` consecutive integers contains a multiple of `q`, hence `t_q>=1`. Subtracting exactly `phi(q)(t_q-1)` over `2<=q<=m` removes every duplication once and proves (1). Computing `phi(2),...,phi(m)` by a sieve and the displayed floors gives the stated algorithm. QED.

This is a computational compression of R136's divisor formula, whose displayed sum ranges to `L+m`; it does not claim an algorithm enumerating the distinct words or witnesses.

## Theorem R137.2 (affine quasiperiod and exact first difference)

Define `P_1=1` and `P_m=lcm(2,3,...,m)` for `m>=2`. Then, for all `K>=2`,
\[
 \boxed{J(K+P_m,m)=J(K,m)+(m+1)P_m.} \tag{2}
\]
Moreover,
\[
 \boxed{J(K+1,m)-J(K,m)
 =(m+1)-\sum_{q=2}^{m}\varphi(q)
 \big(\mathbf1_{q\mid K+m}-\mathbf1_{q\mid K-1}\big).} \tag{3}
\]
Thus `J(K,m)-(m+1)(K-2)` is periodic in `K`, with a period dividing `P_m`.

**Proof.** Each `t_q(K-1,m)` depends only on `K-1 mod q`: shifting the interval by `q` preserves its number of multiples of `q`. Every `q<=m` divides `P_m`; therefore the correction in (1) is unchanged when `K` increases by `P_m`, while the linear term grows by `(m+1)P_m`. For one-step shifts, the old index `K-1` leaves the window and the new index `K+m` enters, so `t_q` changes by the difference of the two displayed indicators, establishing (3). QED.

## Theorem R137.3 (smallest word-length with downward jump-count increments)

For `m=1,2,3,4,5`, `J(K+1,m)>=J(K,m)` for every integer `K>=2`. For `m=6` and every `r>=0`,
\[
 \boxed{J(24+60r,6)=169+420r,quad
        J(25+60r,6)=167+420r.}
\]
In particular, genuine chronological jump *counts* can fall when `K` increases even though the total number of raw floor cuts rises.

**Proof.** Put `h=m+1`. If `q\mid h`, then `q\mid(K+m)` is equivalent to `q\mid(K-1)`; that term in (3) vanishes. For `m<=5`, the sum of `phi(q)` for `2<=q<=m` with `q\nmid h` is at most `h`: explicitly it equals `0,1,2,5,6` for `m=1,2,3,4,5`, compared to `h=2,3,4,5,6`. Even if all remaining indicator differences are `+1`, equation (3) is nonnegative. For `m=6,K=24`, the exiting index is `23`, not divisible by any `2<=q<=6`; the entering index is `30`, divisible by `q=2,3,5,6`, whose totients sum to `1+2+4+2=9`. Equation (3) gives `7-9=-2`. Equation (1) gives `J(24,6)=169`, `J(25,6)=167`; period (2) with `P_6=60` gives the infinite arithmetic progressions. QED.

## Corollary R137.4 (effective saturation obstruction)

Let `F_m=1+sum_{q=1}^m(m+1-q)phi(q)` be the classical finite Sturmian word count. The R136 right-continuous jump bound gives `|V(K,m)|<=J(K,m)+1`. Therefore `J(K,m)+1<F_m` is a certificate of *non-saturation* computable in time polynomial in `m, log K`. This is a necessary-condition test; above the bound, repeated words may still prevent saturation.

For comparison against the already-preserved R136 first-saturation values: at `m=10`, the first `K` passing the event-count necessary condition is `12`, while actual first saturation is `25`; at `m=20`, those values are `42` and `113`. The gap identifies word *recurrence/collision* rather than event-generation counts as a significant remaining problem.

## Exact verification and reproducibility

Companion `check_r137.py` uses Python's exact `Fraction` for an independent event-union construction. It reports `R137_COLLISION_QUASIPERIOD_PASS` after:
- 2,370 pairs `(m,K)`, `1<=m<=30,2<=K<=80`, checking (1) against R136's full totient divisor union;
- 408 pairs `(m,K)`, `1<=m<=12,1<=K<=34`, checking the divisor formula against an independent set of all reduced rational events;
- 224 period identities `1<=m<=8,2<=K<=29`, checking (2);
- all `P_m` residue classes for `m<=6`, checking nonnegative increments for `m<=5` and two negative classes for `m=6`;
- the exact `m=6, K=24,25` witness, and the finite necessary-threshold comparison for `m<=20`.

The algebraic identities and the smallest-length claim are proved above; these finite tests check implementation and example values. No independent mathematical review is asserted.

## Next question

Classify `V(K,m)` directly by *word recurrence* over the Farey cells instead of counting its chronological events. Seek a polynomial-bit decision/certificate for each specified mechanical word when `K=Theta(m^2)`, with explicit nonmonotone `K` examples and a potential determination of first/eventual saturation thresholds. Keep the frozen science pin and the separate X6-native transfer question.
