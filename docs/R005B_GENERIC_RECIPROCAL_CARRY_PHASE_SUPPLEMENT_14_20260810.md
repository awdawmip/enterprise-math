# R005-B — Generic p-Power Reciprocal Carry and Normalized Gap Phase

Status: `PROVED WIP / DRAFT OWNER SUPPLEMENT / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 02–05 and 12

## 1. Result

The reciprocal carry and paired-gap budget discovered in the cubic knife edge
are not cubic-specific.

For every fixed power

\[
p\ge3,
\]

fix one p-power basin

\[
A=k^p,
\qquad
U=(k+1)^p-1,
\qquad
C=(k+1)^p,
\]

and one consecutive prime gap

\[
a<b
\]

strictly beyond the factor horizon

\[
F_p(k)<a.
\]

Let

\[
m=\left\lfloor\frac{A}{a}\right\rfloor.
\]

Then:

1. the exact integer reciprocal window is terminal in m;
2. every terminal depth has a closed activation threshold;
3. the depth-zero threshold is the existing p-basin hit count plus a second
   reciprocal carry;
4. every unit of left prime lag costs at least one unit of right prime-gap
   surplus;
5. the lower PRE critical exponent is exactly the same
   `1-2/p` that already appears in R005-A T-A22 and in the upper factor-horizon
   gap law;
6. after normalization by `a^(1-2/p)`, the universal phase constants are

\[
\boxed{p/2\quad\text{and}\quad p.}
\]

For p=3 these are exactly the previously observed `3/2` and `3`.

---

## 2. B38 — generic reciprocal integer compiler

The R005-A e=1 failure interval in the cofactor-gap regime is

\[
\frac{U}{b}<q\le\frac{A}{a}.
\]

Since `U=C-1`, its integer points are

\[
\left\lceil\frac{C}{b}\right\rceil\le q\le m.
\]

Thus every integer candidate has the terminal form

\[
\boxed{q=m-j}
\]

with

\[
\boxed{
0\le j\le
J=m-\left\lceil\frac{C}{b}\right\rceil.
}
\]

No p-specific argument is needed.

---

## 3. B39 — generic depth thresholds

Write

\[
g=b-a.
\]

At terminal depth j, q=m-j is captured exactly when

\[
(a+g)(m-j)\ge C.
\]

Hence

\[
\boxed{
G_j^{(p)}(a,k)
=\left\lceil\frac{C}{m-j}\right\rceil-a.
}
\]

In particular,

\[
\boxed{
G_0^{(p)}(a,k)
=\left\lceil\frac{(k+1)^p}{\lfloor k^p/a\rfloor}\right\rceil-a.
}
\]

This is the exact integer activation threshold for the reciprocal quotient
endpoint.

---

## 4. B40 — p-basin hit count plus reciprocal carry

Write

\[
C=a(m+d)+r',
\qquad
0<r'<a.
\]

For p>=3, the PRE condition `a>F_p(k)` forces `a>k+1`; therefore a cannot divide
C.  Hence

\[
\boxed{
d
=\left\lfloor\frac{C}{a}\right\rfloor-\left\lfloor\frac{A}{a}\right\rfloor
=H_{p,a}(k).
}
\]

Exactly as in the cubic case,

\[
\boxed{
G_0^{(p)}
=d+\left\lceil\frac{d(a-m)+r'}{m}\right\rceil.
}
\]

Call the second term eta.  The existing one-bit width carry gives

\[
H_{p,a}(k)
=\left\lfloor\frac{L_p(k)}{a}\right\rfloor
+\varepsilon_{p,a}(k),
\qquad
\varepsilon_{p,a}(k)\in\{0,1\},
\]

where

\[
L_p(k)=(k+1)^p-k^p-1.
\]

Therefore

\[
\boxed{
G_0^{(p)}
=\left\lfloor\frac{L_p(k)}{a}\right\rfloor
+\varepsilon_{p,a}(k)
+\eta_{p,a}(k).
}
\]

So a lower reciprocal prime-gap threshold has exactly the same architecture at
every collapse dimension p>=3:

\[
\text{width baseline}
+\text{one-bit basin carry}
+\text{reciprocal carry}.
\]

---

## 5. B41 — universal unit-cost paired-gap ladder

Since a lies beyond the factor horizon,

\[
a>\sqrt A.
\]

Therefore

\[
m<\frac{A}{a}<\sqrt A<\sqrt C.
\]

For every relevant terminal q<=m,

\[
q(q-1)<C.
\]

Hence

\[
\frac{C}{q-1}-\frac{C}{q}
=\frac{C}{q(q-1)}>1.
\]

Taking ceilings gives the dimension-independent law

\[
\boxed{
G_{j+1}^{(p)}\ge G_j^{(p)}+1.
}
\]

Thus

\[
\boxed{
G_j^{(p)}\ge G_0^{(p)}+j.
}
\]

If the actual right gap has surplus

\[
H=g-G_0^{(p)},
\]

then every captured predecessor-prime lag satisfies

\[
\boxed{j\le H.}
\]

The fixed-slack finite-state theorem from the cubic shell is therefore a generic
p-power fact.

---

## 6. B42 — generic lower boundary-prime compression

Let

\[
Q=\max\{q\le m:q\text{ prime}\}.
\]

The reciprocal integer window contains a prime iff it contains Q:

\[
\boxed{
Q\ge\left\lceil\frac{C}{b}\right\rceil
\iff
bQ\ge C.
}
\]

So the yes/no occupancy state of one PRE cofactor gap is always one boundary
prime plus the quotient/carry threshold state.

Whether such an e=1 failure upgrades to full non-forcing remains a
power-specific factor-normal-form question.  In the cubic q>k regime it does;
this supplement does not assert the same upgrade without checking the relevant
higher-power alternatives for general p.

---

## 7. B43 — generic real PRE critical scale

The real reciprocal interval is positive exactly when

\[
\frac{U}{a+g}<\frac{A}{a}.
\]

Cross multiplication gives

\[
\boxed{
gA>a(U-A)=aL_p(k).}
\]

Thus the least integer real-window gap is

\[
\boxed{
1+\left\lfloor\frac{aL_p(k)}{A}\right\rfloor.
}
\]

At the lower factor-horizon scale

\[
a\asymp F_p(k)\asymp k^{p/2},
\]

we have

\[
L_p(k)=p k^{p-1}+O(k^{p-2}),
\]

so

\[
\boxed{
g_{\rm PRE}\sim p k^{p/2-1}.}
\]

Since

\[
a\asymp k^{p/2},
\]

this is equivalently

\[
\boxed{
g_{\rm PRE}\sim p\,a^{1-2/p}.}
\]

The exponent is exactly

\[
\boxed{1-2/p=\lambda(p,2),}
\]

R005-A's full-forcing short-interval exponent.

---

## 8. B44 — universal normalized gap phase constants

The upper horizon-gap analysis already gives, for fixed p,

\[
g_0\sim\frac p2 k^{p/2-1}
\]

for window opening, and

\[
g_1\sim p k^{p/2-1}
\]

for wall crossover / saturation.

At the horizon scale `a~F_p(k)`, normalize a consecutive prime gap by

\[
\boxed{
c_p=\frac{g}{a^{1-2/p}}.}
\]

Then the three asymptotic phase constants become

\[
\boxed{
\text{upper opening}:\quad c_p=p/2,
}
\]

\[
\boxed{
\text{lower PRE criticality}:\quad c_p=p,
}
\]

\[
\boxed{
\text{upper saturation}:\quad c_p=p.
}
\]

Thus the same gap, as the moving factor horizon sweeps through it, has the
universal leading lifecycle

\[
\boxed{
\text{PRE threshold }p
\longrightarrow
\text{horizon-inside residual threshold }p
\longrightarrow
\text{upper closure threshold }p/2.
}
\]

The cubic constants

\[
3,\quad 3,\quad 3/2
\]

are not isolated numerology.  They are the p=3 row of a generic

\[
\boxed{p/2\ \text{vs}\ p}
\]

factor-horizon phase law.

---

## 9. Relation to the p=2 / p=4 / p>=5 picture

### p=2

The PRE/horizon geometry degenerates because the square factor horizon is exactly
self-aligned, `F_2(k)=k`.  P018 centered shells, not this p>=3 compiler, own the
square exceptional mechanism.

### p=3

The normalized constants are `3/2` and `3`; the current knife-edge analysis is
Supplement 10–13.

### p=4

The normalized exponent is `1/2`, and the factor-horizon drift is exactly the
square-basin interior width.  Thus the same generic phase law meets the Legendre
scale.

### p>=5

The exponent

\[
1-2/p>0.525
\]

is already inside the Baker–Harman–Pintz all-interval range used by R005-A, so
the complete candidate language is eventually forced.  The generic paired-gap
compiler explains the same transition locally at individual cofactor gaps.

---

## 10. Architectural interpretation

R005-A T-A22 originally reached `1-2/p` from witness/cofactor short-interval
geometry.

R005-B has now reached the same exponent three independent ways:

1. upper factor-horizon protecting-gap drift;
2. lower PRE reciprocal-gap activation;
3. exact reciprocal carry thresholds with coarse term `L_p(k)/a`.

Therefore

\[
\boxed{
\lambda(p,2)=1-2/p
}
\]

is not merely an exponent borrowed from an analytic prime-gap theorem.  It is
the intrinsic scaling exponent at which the p-power basin width, factor horizon,
and reciprocal witness language meet.

The constants p/2 and p refine that exponent into a normalized phase geometry.

---

## 11. Ownership / prior-art boundary

The floor/ceiling compiler, Euclidean division and asymptotic binomial expansion
are elementary prior mathematics.  Prime-gap bounds themselves remain external
analytic number theory.  R005-A owns generic witness/forced-core language;
R005-B owns this p-power factor-horizon/carry specialization.

The candidate reusable project contribution is the compiled architecture and its
phase identification.  Historical novelty remains unverified.
