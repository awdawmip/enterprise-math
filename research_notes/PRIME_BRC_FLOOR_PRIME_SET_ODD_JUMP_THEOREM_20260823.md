# Prime-BRC / Floor-Prime-Set Odd Jump Theorem

Status: `L3 OWNER-LOCAL / PROVED ELEMENTARY THEOREM / EXTERNAL CONJECTURE CONNECTION`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. External problem

For a positive integer `x`, define

\[
\mathcal G(x)=\left\{\left\lfloor\frac{x}{n}\right\rfloor:1\le n\le x\right\},
\qquad
G(x)=|\mathcal G(x)\cap\mathbb P|.
\]

Randell Heyman proved the odd-prime and odd-semiprime increments and stated the three-distinct-odd-prime conjecture

\[
G(p_1p_2p_3)-G(p_1p_2p_3-1)
=
\begin{cases}
0,&p_1p_2>p_3,\\
1,&p_1p_2<p_3,
\end{cases}
\]

for `2<p1<p2<p3`.

The theorem below proves a stronger formula for every odd integer `x>=5`.

Novelty status beyond the cited Heyman conjecture is **not independently certified**; current web audit on 2026-08-23 found the three-prime statement still listed as open by MathDB.

## 2. Membership counter

For integers `x>=1,m>=1`, define

\[
J_x(m)=
\left\lfloor\frac{x}{m}\right\rfloor
-
\left\lfloor\frac{x}{m+1}\right\rfloor.
\]

Then

\[
\boxed{m\in\mathcal G(x)\iff J_x(m)>0.}
\]

Indeed `floor(x/n)=m` precisely when

\[
\frac{x}{m+1}<n\le\frac{x}{m},
\]

and `J_x(m)` counts the integers in this interval.

Also

\[
\boxed{
J_x(m)-J_{x-1}(m)
=
\mathbf1_{m\mid x}-\mathbf1_{m+1\mid x}.
}
\]

This follows from

\[
\left\lfloor\frac{x}{d}\right\rfloor-
\left\lfloor\frac{x-1}{d}\right\rfloor
=
\mathbf1_{d\mid x}.
\]

## 3. No prime can leave when x is odd and x>=5

Let `x>=5` be odd.

If an odd prime `r` were to lose one unit in its membership counter, the second indicator above would require

\[
r+1\mid x.
\]

But `r+1` is even while `x` is odd, impossible.

The only even prime is `r=2`. Although `3|x` can make `J_x(2)=J_{x-1}(2)-1`, both counters remain positive for `x>=5`:

\[
J_y(2)=\left\lfloor\frac y2\right\rfloor-\left\lfloor\frac y3\right\rfloor>0
\qquad(y\ge4).
\]

Thus

\[
\boxed{
\mathcal G(x-1)\cap\mathbb P
\subseteq
\mathcal G(x)\cap\mathbb P
}
\]

for every odd `x>=5`.

## 4. Which prime divisors enter?

Let `p|x` be an odd prime and write

\[
x=ap.
\]

At `x`, `p` is certainly in the floor set because

\[
\left\lfloor\frac{x}{a}\right\rfloor=p.
\]

At `x-1`,

\[
\begin{aligned}
J_{x-1}(p)
&=\left\lfloor\frac{ap-1}{p}\right\rfloor
 -\left\lfloor\frac{ap-1}{p+1}\right\rfloor\\
&=a-1-\left\lfloor\frac{ap-1}{p+1}\right\rfloor.
\end{aligned}
\]

Now

\[
J_{x-1}(p)=0
\]

iff

\[
\left\lfloor\frac{ap-1}{p+1}\right\rfloor=a-1.
\]

Since `(ap-1)/(p+1)<a`, this is equivalent to

\[
(a-1)(p+1)\le ap-1.
\]

Cancelling gives

\[
\boxed{a\le p.}
\]

Equivalently,

\[
\boxed{p^2\ge x.}
\]

Therefore a prime divisor of `x` is newly added to the floor-prime set exactly when it lies at or above the square-root frontier.

## 5. Main theorem

### Theorem — odd floor-prime-set jump formula

For every odd integer `x>=5`,

\[
\boxed{
G(x)-G(x-1)
=
\#\{p:p\mid x,\ p\text{ prime},\ p^2\ge x\}.
}
\]

There is at most one such prime divisor. Hence, writing `P^+(x)` for the largest prime factor,

\[
\boxed{
G(x)-G(x-1)
=
\mathbf1_{\{P^+(x)^2\ge x\}}.
}
\]

For odd prime `x`, this gives the known `+1` result for `x>=5`. For odd semiprime `x=pq`, the largest factor always satisfies `q^2>=pq`, recovering Heyman's semiprime theorem.

## 6. Heyman's three-prime conjecture

Let

\[
x=p_1p_2p_3,
\qquad 2<p_1<p_2<p_3.
\]

Then

\[
p_3^2\ge x
\iff
p_3\ge p_1p_2.
\]

Equality is impossible because `p3` is prime while `p1 p2` is composite. Therefore

\[
\boxed{
G(x)=
\begin{cases}
G(x-1),&p_1p_2>p_3,\\
G(x-1)+1,&p_1p_2<p_3.
\end{cases}}
\]

which is exactly the published three-prime conjecture.

## 7. Prime-BRC interpretation

The quantity `J_x(m)` is a one-step quotient-support multiplicity. The increment

\[
J_x(m)-J_{x-1}(m)
=
\mathbf1_{m|x}-\mathbf1_{m+1|x}
\]

is a signed two-boundary carry. For odd `x`, parity kills the negative channel for every odd prime, so the only possible new prime branch is a divisor crossing the exact square-root frontier.

Thus the external conjecture is resolved by the same structural ingredients isolated in Prime-BRC:

```text
floor quotient support
+ signed boundary carry
+ parity
+ square-root frontier
-> exact one-bit jump law.
```

## 8. Boundaries

This theorem is independent of Legendre's conjecture and does not prove Prime-BRC's main prime-gap target.

It does provide an externally stated test where the square-root frontier / signed-carry viewpoint yields a strict theorem stronger than the conjectured special case.

Freeze owner-local result:

`ODD_FLOOR_PRIME_SET_JUMP_CLASSIFIED_BY_LARGEST_PRIME_SQRT_FRONTIER = true`.

`HEYMAN_THREE_PRIME_FLOOR_SET_CONJECTURE_FOLLOWS = true`.

External novelty / publication-priority status remains `NOVELTY_AUDIT_REQUIRED`.
