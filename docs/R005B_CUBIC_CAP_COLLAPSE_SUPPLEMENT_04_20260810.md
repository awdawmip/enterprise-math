# R005-B — Cubic Pure-Cap Collapse

Status: `PROVED WIP / DRAFT OWNER SUPPLEMENT / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Horizon-Gap Supplement 02; Prime-Slice / Half-Scale Supplement 03

## 1. Result

The generic pure-cap prime-slice compiler has four lower cutoffs.  In the
cubic case, for every `k>=3`, two of them are automatically dominated.

Write

\[
A=k^3,
\qquad
U=(k+1)^3-1,
\qquad
F=\lfloor\sqrt U\rfloor,
\qquad
S=\lfloor\sqrt A\rfloor,
\qquad
R=\operatorname{nextprime}(F).
\]

Then the non-forced cubic pure-cap witnesses are exactly

\[
\boxed{
\left\{
q\text{ prime}:
\max\left(
\left\lfloor\frac{k^3}{F}\right\rfloor,
\left\lfloor\frac{U}{R}\right\rfloor
\right)
<q\le S
\right\}.
}
\]

Thus cubic pure-cap non-forcing has no remaining higher-power side condition.
It is a short prime interval determined by only two arithmetic walls:

1. the lower **horizon-entry wall** `A/F`;
2. the upper-prime **non-forcing wall** `U/R`.

---

## 2. B21 — cubic cap-collapse theorem

### Theorem

For `k>=3`, suppose q is prime and

\[
q\le S,
\qquad
qF>A.
\]

Then automatically

\[
q^3>U
\]

and

\[
q^2(F+1)>U.
\]

Therefore the generic pure-cap conditions reduce exactly to

\[
q\le S,
\qquad
qF>A.
\]

On this reduced cap, consuming the Supplement-02 theorem,

\[
q\text{ non-forced}
\iff
qR>U.
\]

Equivalently,

\[
\boxed{
q\text{ non-forced pure-cap}
\iff
\max\left(\left\lfloor\frac AF\right\rfloor,
\left\lfloor\frac UR\right\rfloor\right)<q\le S
}
\]

for prime q.

### Proof

For k>=3,

\[
U=(k+1)^3-1<(k+1)^3<k^4,
\]

because `k+1<k^(4/3)` is equivalent to `(k+1)^3<k^4`, true from k=3 onward.
Thus

\[
F=\lfloor\sqrt U\rfloor<k^2.
\]

If `qF>k^3`, then

\[
q>\frac{k^3}{F}>k.
\]

Since q is an integer,

\[
q\ge k+1.
\]

Therefore

\[
q^3\ge(k+1)^3>U.
\]

Also `U>k^2`, so `F>=k`, hence

\[
q^2(F+1)
\ge
(k+1)^2(k+1)
=(k+1)^3
>U.
\]

The two higher-power exclusion conditions are therefore automatic.  The
remaining statements follow by integerizing `qF>A` and `qR>U`. ∎

---

## 3. Relation to the generic four-cutoff compiler

Supplement 03 defined

\[
L_{p,k}=1+\max\left(
\left\lfloor\frac AF\right\rfloor,
\lfloor U^{1/3}\rfloor,
\left\lfloor\sqrt{\left\lfloor\frac U{F+1}\right\rfloor}\right\rfloor,
\left\lfloor\frac UR\right\rfloor
\right).
\]

For p=3,

\[
\lfloor U^{1/3}\rfloor=k.
\]

The proof above gives

\[
\left\lfloor\frac AF\right\rfloor\ge k
\]

for k>=3, so the cube-root cutoff is redundant.

Moreover `U<(F+1)^2`, hence

\[
\left\lfloor\frac U{F+1}\right\rfloor\le F<k^2,
\]

and therefore

\[
\left\lfloor
\sqrt{\left\lfloor\frac U{F+1}\right\rfloor}
\right\rfloor<k
\le
\left\lfloor\frac AF\right\rfloor.
\]

Thus the generic compiler collapses algebraically to

\[
\boxed{
L_{3,k}
=1+\max\left(
\left\lfloor\frac{k^3}{F}\right\rfloor,
\left\lfloor\frac U R\right\rfloor
\right).
}
\]

No asymptotic approximation is used.

---

## 4. Two-wall cubic geometry

Define

\[
Q_H=\left\lfloor\frac{k^3}{F}\right\rfloor,
\qquad
Q_R=\left\lfloor\frac U R\right\rfloor.
\]

Then the cubic pure-cap slice is simply

\[
\boxed{
\max(Q_H,Q_R)<q\le S.
}
\]

The two walls have different origins.

### Horizon-entry wall Q_H

A candidate q must lie above `A/F`; otherwise `A/q>=F` and the first eligible
cofactor remains controlled by the ordinary reciprocal cofactor-prime gap
rather than by the factor horizon.

### Non-forcing wall Q_R

Once q lies in the horizon band, every q shares the first post-horizon prime R.
The product qR overshoots the basin exactly when `q>U/R`.

Thus the cubic pure-cap failure is the intersection

\[
\boxed{
\text{prime q}
\cap
(Q_H,S]
\cap
(Q_R,S].
}
\]

The four-condition factor problem has become a two-wall prime-occupancy
problem.

---

## 5. Examples

The previously recorded examples are reproduced exactly:

| k | `Q_H=floor(A/F)` | `Q_R=floor(U/R)` | S | failing prime slice |
|---:|---:|---:|---:|---|
| 23 | 103 | 108 | 110 | `[109,110]` -> 109 |
| 64 | 500 | 507 | 512 | `[508,512]` -> 509 |
| 120 | 1299 | 1301 | 1314 | `[1302,1314]` -> 1303,1307 |
| 138 | 1604 | 1620 | 1621 | `[1621,1621]` -> 1621 |
| 1005 | 31813 | 31858 | 31860 | `[31859,31860]` -> 31859 |

At k=138 the non-forcing wall dominates almost all available q-room and leaves
one point.  At k=120 the post-horizon gap opens a wider slice containing two
primes.

---

## 6. What remains unresolved

The cubic **pure-cap** problem is now exact and minimal in variables:

\[
F,\ R,\ Q_H,\ Q_R,\ S.
\]

But this does not prove that every possible cubic non-forced witness lies in the
pure horizon cap.  The lower cofactor-gap band remains a separate route, and
R005-A's reciprocal-gap machinery owns that side.

The asymptotic full-forcing question should therefore be split into:

1. **upper horizon cap:** does the interval
   \[
   (\max(Q_H,Q_R),S]
   \]
   contain a prime infinitely often when it is nonempty?
2. **lower cofactor-gap band:** can reciprocal cofactor-prime gaps generate
   non-forced witnesses infinitely often after higher-q-power routes are also
   excluded?

The first question is now a two-scale prime-gap/prime-occupancy problem.  The
second remains a reciprocal-gap problem.

---

## 7. Validation

`cubic_pure_cap_nonforced_interval(k)` implements the two-wall formula.

Independent exact integer validation checked

\[
3\le k<1000
\]

and found exact agreement between the collapsed two-wall formula and the
generic four-cutoff pure-cap compiler at every tested k.

The owner-local unittest locks the same identity over that range, in addition
to the earlier direct-support and generic prime-slice regressions.

No claim of infinitude or eventual disappearance is made from this finite
validation.
