# P017 — Adaptive Primorial-Length Anchor Descent

Status: `PROVED EXACT ARITHMETIC SPECIALIZATION + EXPLICIT-ROUTE TOOL / NOT A P2 THEOREM / NOT CANONICAL`

Date: `2026-08-23`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

## 1. Interval freedom inside one square basin

The full consecutive-square basin has integer width `2K`:

\[
I_K=\{K^2+1,\ldots,K^2+2K\}.
\]

Hence any integer length

\[
K\le L\le2K
\]

can be used to define a shorter target interval

\[
J_{K,L}=\{K^2+1,\ldots,K^2+L\}\subset I_K.
\]

Finding a `P2` in `J_{K,L}` is sufficient for the full square basin.

## 2. Exact scale-stripping identity

For integers `A>=0`, `L>=1`, define

\[
H_d(A,L)=
\left\lfloor\frac{A+L}{d}\right\rfloor
-
\left\lfloor\frac A d\right\rfloor.
\]

### Theorem

If `e|L`, then for every `b>=1`,

\[
\boxed{
H_{eb}(A,L)
=
H_b\!\left(\left\lfloor\frac A e\right\rfloor,\frac L e\right).
}
\]

### Proof

Write

\[
A=eA_0+r,\qquad0\le r<e,\qquad L=eL_0.
\]

Then

\[
\begin{aligned}
H_{eb}(A,L)
&=\left\lfloor\frac{A_0+L_0+r/e}{b}\right\rfloor
 -\left\lfloor\frac{A_0+r/e}{b}\right\rfloor.
\end{aligned}
\]

Because `A0,L0` are integers and `0<=r/e<1`, for any integer `n` and positive integer `b`,

\[
\left\lfloor\frac{n+r/e}{b}\right\rfloor
=\left\lfloor\frac n b\right\rfloor.
\]

Thus

\[
H_{eb}(A,L)
=\left\lfloor\frac{A_0+L_0}{b}\right\rfloor
 -\left\lfloor\frac{A_0}{b}\right\rfloor,
\]

which is the claimed identity. `QED`

## 3. Exact remainder descent

Define the sharp floor discrepancy

\[
r_d(A,L)=H_d(A,L)-\frac L d.
\]

Under `e|L`, the theorem immediately gives

\[
\boxed{
r_{eb}(A,L)
=r_b\!\left(\left\lfloor A/e\right\rfloor,L/e\right).}
\]

Thus an anchor divisor of the interval length is not merely a modulus with zero error when taken alone: it can be stripped from **every mixed modulus** before the hard remainder is estimated.

In particular, if `b=1`,

\[
\boxed{H_e(A,L)=L/e,\qquad r_e(A,L)=0.}
\]

## 4. Adaptive primorial choice

Let

\[
Q=P(u)=\prod_{p\le u}p
\]

be a primorial satisfying `Q<=K`, and set

\[
\boxed{L_Q=Q\left\lceil\frac KQ\right\rceil.}
\]

Then

\[
K\le L_Q<K+Q\le2K,
\]

so

\[
J_{K,Q}:=(K^2,K^2+L_Q]
\]

lies entirely inside the consecutive-square basin.

Because `Q|L_Q`, every squarefree sieve modulus `d` admits the canonical split

\[
d=e b,\qquad e=(d,Q),
\]

and the complete small-prime part `e` can be stripped exactly:

\[
\boxed{
H_d(K^2,L_Q)
=H_b\!\left(\left\lfloor K^2/e\right\rfloor,L_Q/e\right).
}
\]

All prime factors of the remaining hard modulus `b` are `>u`.

This is an exact `W`-trick-like reduction with **zero pre-sieve floor error**, made possible by choosing the interval length inside the available square basin.

## 5. Threshold diagnostic at `x=10^31`

At the Campbell finite/asymptotic splice scale, take

\[
K=\lfloor\sqrt{10^{31}}\rfloor=3162277660168379.
\]

The largest consecutive small-prime primorial below `K` is

\[
\boxed{P(41)=304250263527210},
\]

while `P(43)>K`.

Hence

\[
L=11P(41)=3346752898799310,
\]

and

\[
\boxed{L/K\approx1.05833619.}
\]

So at the finite splice point one can remove every prime `p<=41` from the hard denominator while increasing the target interval length by only about `5.84%` over `K`.

For the balanced reference level

\[
D=x^{9/16}\approx2.74\times10^{17},
\qquad z=x^{3/32}\approx806,
\]

a squarefree hard modulus after stripping `P(41)` has all prime factors at least `43`.  The product of the ten smallest primes starting at `43` already exceeds `D`, so at this threshold the stripped hard modulus has at most **nine** such prime factors.  Before the stripping, the corresponding smallest-prime product count is about fourteen.  This finite-depth comparison is a threshold diagnostic, not an asymptotic theorem.

## 6. Relationship to the centered `K`-anchor

The earlier special interval

\[
(K(K+1),K(K+2)]
\]

has length exactly `K`, so every `e|K` strips exactly.  That is the special case `L=K` of the present theorem after translating the left endpoint.

The adaptive primorial construction is stronger for explicit sieve engineering because it does not depend on the arithmetic factorization of `K`: the interval length is chosen to manufacture the desired anchor divisor.

## 7. Prior-art boundary

The floor identity itself is elementary Euclidean division, and pre-sieving / `W`-tricks are classical.  No historical novelty is claimed for those ingredients.

The project-specific point is the **use of the free interval length inside a consecutive-square basin** to make a chosen primorial divide the target length, thereby eliminating its floor remainders exactly before the P017/Chen bilinear tail is estimated.

## 8. Remaining question

This exact descent does not itself prove `P2`.  The load-bearing analytic issue remains the super-root tail after stripping:

\[
b>1,\qquad p|b\Longrightarrow p>u.
\]

The next quantitative task is to combine this anchor descent with a fixed-depth/well-factorable linear-sieve decomposition and determine whether the explicit section-5 constant at `x>=10^31` falls below the balanced positive main-term budget.
