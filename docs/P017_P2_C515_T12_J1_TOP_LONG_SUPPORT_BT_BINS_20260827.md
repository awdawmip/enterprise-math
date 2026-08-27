# P017 — c=103/20 j=1 Top Long-Support Brun–Titchmarsh Bin Refinement

Status: `PROVED_WIP EXPLICIT SUPPORT <1.5 PERCENT / REFINES TOP-LONG SUPPORT NOTE / NOT FULL REMAINDER CONSTANT / NOT CANONICAL`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Refines:

`docs/P017_P2_C515_T12_J1_TOP_LONG_SUPPORT_20260827.md`.

Purpose: replace the uniform lower bound `log(X_1/5)>5` in the top-block Brun–Titchmarsh argument by seven exact bins in the second external prime `q`.

---

## 1. Retained setup

On the top long block

\[
\frac56B<M\le B,
\qquad B=W^{31/36},
\]

a support modulus is safely majorized by

\[
m=rqp\,b_1,
\]

with `1447<=r<q<p` and a hard reciprocal factor satisfying

\[
C_h<\frac{269}{128}.
\]

Fixing `b_1,r,q`, Brun–Titchmarsh gives

\[
\#\{p:X_1<p\le(6/5)X_1\}
\le
\frac{2X_1/5}{\log(X_1/5)}.
\]

If the interval contains an admissible `p>q`, then `X_1/5>q/6`, so it is enough to lower-bound `log(q/6)`.

---

## 2. Elementary exponential comparison

The elementary exponential-series bound

\[
\boxed{e<\frac{68}{25}=2.72}
\tag{BT1}
\]

is certified by summing through `1/8!` and bounding the remaining geometric tail.

Direct integer comparisons then give

\[
\left(\frac{68}{25}\right)^k<\frac{Q_k}{6}
\]

for

\[
\begin{array}{c|rrrrrrr}
k&5&6&7&8&9&10&11\\\hline
Q_k&1447&3000&8000&20000&50000&140000&370000.
\end{array}
\]

Hence, in the seven q-bins beginning at these thresholds,

\[
\boxed{\log(q/6)>k.}
\tag{BT2}

---

## 3. Exact reciprocal-pair bin masses

Let

\[
R_k
=
\sum_{\substack{1447\le r<q,\ rq^2<B\\Q_k\le q<Q_{k+1}}}
\frac1{rq},
\]

with the last interval `q>=370000`.

The checker enumerates ordinary primes only up to `584760`, upper-encloses every reciprocal by a common `10^12` fixed-point integer, and proves

\[
\boxed{
\begin{array}{c|c}
q\text{-bin}&R_k\text{ upper bound}\\\hline
[1447,3000)&458/10^5\\
[3000,8000)&1748/10^5\\
[8000,20000)&2498/10^5\\
[20000,50000)&3100/10^5\\
[50000,140000)&3621/10^5\\
[140000,370000)&1805/10^5\\
[370000,\infty)&216/10^5.
\end{array}}
\tag{BT3}

Using (BT2),

\[
\sum_{1447\le r<q,\ rq^2<B}
\frac1{rq\log(q/6)}
<
\sum_{k=5}^{11}\frac{R_k}{k}
<
\boxed{\frac{1997873}{115500000}}
<0.017298.
\tag{BT4}

---

## 4. Refined support density

The Brun–Titchmarsh count contributes the factor `2/5` in front of (BT4). Hence

\[
\frac{A_M}{(5/6)B}
<
\frac25\frac{269}{128}\frac{1997873}{115500000}
=
\frac{537427837}{36960000000}
<0.01455.
\]

In particular,

\[
\boxed{
\frac{A_M}{(5/6)B}<\frac3{200}=0.015.
}
\tag{BT5}

Thus at most 1.5 percent of the complete top long block must be retained in the outer Cauchy support.

This remains a support theorem only. The next step is to insert (BT5), the 185-state top short support, and the exact `hn` diagonal into a sharp/full-basin reciprocal-Cauchy estimate.

No full remainder bound or finite P2 theorem is claimed.
