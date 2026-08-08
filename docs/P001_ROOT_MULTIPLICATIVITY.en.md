# P001 — Exact multiplicativity criterion for integer roots

Status: `PROVED`  
Open problem: `P001`  
Scope: ordinary mathematics

## 1. Question

For \(p\ge1\), characterize exactly when

\[
R_p(ab)=R_p(a)R_p(b).
\]

Let

\[
r=R_p(a),\qquad s=R_p(b).
\]

Write the two inputs in their collapse basins as

\[
a=r^p+u,
\qquad
b=s^p+v,
\]

where

\[
u=G_p(a)=a-r^p,
\qquad
v=G_p(b)=b-s^p.
\]

By P002-T01 and P002-T02,

\[
0\le u<\Delta_p(r),
\qquad
0\le v<\Delta_p(s),
\]

with the integer basin width

\[
\Delta_p(k)=(k+1)^p-k^p.
\]

The multiplicativity problem is therefore an exact carry problem inside the product of two integer basins.

## 2. Integer roots are always supermultiplicative

### P001-T01 — Root supermultiplicativity

Status: `PROVED`

For all \(a,b\in\mathbb N\) and \(p\ge1\),

\[
R_p(ab)\ge R_p(a)R_p(b).
\]

### Proof

Since

\[
r^p\le a,
\qquad
s^p\le b,
\]

we have

\[
(rs)^p=r^ps^p\le ab.
\]

Therefore \(rs\) is an admissible integer in the defining maximum for \(R_p(ab)\), so

\[
R_p(ab)\ge rs.
\]

∎

Thus multiplicativity can fail only by an **upward root carry**; it can never fail below the product \(rs\).

## 3. Exact carry load

Expanding the product gives

\[
\begin{aligned}
ab
&=(r^p+u)(s^p+v)\\
&=(rs)^p+s^p u+r^p v+uv.
\end{aligned}
\]

Define the basin-product carry load

\[
L_p(a,b)=s^p u+r^p v+uv.
\]

Then

\[
ab=(rs)^p+L_p(a,b).
\]

The next possible root state after \(rs\) begins at

\[
(rs+1)^p=(rs)^p+\Delta_p(rs).
\]

## 4. Complete multiplicativity characterization

### P001-T02 — Exact no-carry criterion

Status: `PROVED`

For all \(a,b\in\mathbb N\) and \(p\ge1\), with

\[
r=R_p(a),\quad s=R_p(b),\quad
u=a-r^p,\quad v=b-s^p,
\]

we have

\[
\boxed{
R_p(ab)=rs
\iff
s^p u+r^p v+uv<\Delta_p(rs).
}
\]

Equivalently,

\[
R_p(ab)=R_p(a)R_p(b)
\iff
L_p(a,b)<\Delta_p(R_p(a)R_p(b)).
\]

### Proof

P001-T01 already gives \(R_p(ab)\ge rs\). Therefore equality holds exactly when \(ab\) has not reached the next \(p\)-th-power threshold:

\[
R_p(ab)=rs
\iff
ab<(rs+1)^p.
\]

Substitute

\[
ab=(rs)^p+L_p(a,b)
\]

and subtract \((rs)^p\):

\[
L_p(a,b)<(rs+1)^p-(rs)^p=\Delta_p(rs).
\]

∎

This gives the requested necessary and sufficient condition using integers only.

## 5. Multiplicative root carry

Define

\[
K_p(a,b)=R_p(ab)-R_p(a)R_p(b).
\]

By P001-T01,

\[
K_p(a,b)\in\mathbb N.
\]

### P001-T03 — Exact carry characterization

Status: `PROVED`

With \(r,s,u,v\) as above,

\[
K_p(a,b)
=
\max\Bigl\{c\in\mathbb N:
(rs+c)^p-(rs)^p\le L_p(a,b)
\Bigr\}.
\]

In particular,

\[
K_p(a,b)=0
\iff
L_p(a,b)<\Delta_p(rs).
\]

### Proof

For \(c\in\mathbb N\),

\[
rs+c\le R_p(ab)
\iff
(rs+c)^p\le ab.
\]

Using \(ab=(rs)^p+L_p(a,b)\), this is equivalent to

\[
(rs+c)^p-(rs)^p\le L_p(a,b).
\]

Taking the greatest admissible \(c\) gives the result. ∎

So the failure of root multiplicativity is not an unspecified rounding phenomenon. It is an exact integer threshold-crossing count.

## 6. Geometry inside a pair of basins

For fixed root states \(r,s\), the offsets range over the finite rectangle

\[
0\le u<\Delta_p(r),
\qquad
0\le v<\Delta_p(s).
\]

Inside that rectangle, multiplicativity is the inequality

\[
s^p u+r^p v+uv<\Delta_p(rs).
\]

Because the left side is monotone in both \(u\) and \(v\), the no-carry region is a lower set.

### P001-T04 — Downward closure of the multiplicative region

Status: `PROVED`

Fix \(p,r,s\). Suppose offsets \((u,v)\) satisfy the no-carry criterion. Then every pair

\[
0\le u'\le u,
\qquad
0\le v'\le v
\]

also satisfies it.

### Proof

All coefficients and offsets are nonnegative, so

\[
s^p u'+r^p v'+u'v'
\le
s^p u+r^p v+uv
<\Delta_p(rs).
\]

∎

Thus the multiplicative pairs in each basin rectangle have a monotone staircase boundary rather than an arbitrary pattern.

## 7. Exact one-sided boundary by floor division

Assume \(a>0\), so \(r^p+u=a>0\). Rewrite the carry load as

\[
L_p(a,b)=s^p u+(r^p+u)v=s^p u+av.
\]

### P001-T05 — Maximum admissible second offset

Status: `PROVED`

Fix \(p,r,s,u\) with \(a=r^p+u>0\). If

\[
s^p u\ge\Delta_p(rs),
\]

then no \(v\ge0\) can satisfy multiplicativity.

If

\[
s^p u<\Delta_p(rs),
\]

then the no-carry criterion is equivalent to

\[
v\le
\left(\Delta_p(rs)-1-s^p u\right)\operatorname{//}a.
\]

Inside the actual \(s\)-basin, the largest admissible offset is therefore

\[
\min\!\left(
\Delta_p(s)-1,
\left(\Delta_p(rs)-1-s^p u\right)\operatorname{//}(r^p+u)
\right).
\]

### Proof

The strict integer inequality

\[
s^p u+av<\Delta_p(rs)
\]

is equivalent to

\[
av\le\Delta_p(rs)-1-s^p u.
\]

For positive \(a\), floor division gives the greatest admissible integer \(v\). The basin itself supplies the additional cap \(v\le\Delta_p(s)-1\). ∎

This connects P001 directly back to the P008 order-adjoint/floor-division framework.

## 8. Useful special cases

### Both factors are perfect powers

If \(u=v=0\), then \(L_p(a,b)=0\), so multiplicativity always holds:

\[
R_p(r^p s^p)=rs.
\]

### One perfect-power factor is not enough

If only \(u=0\), the exact condition becomes

\[
r^p v<\Delta_p(rs).
\]

Therefore a perfect-power first factor does **not** guarantee multiplicativity.

For \(p=2\), take

\[
a=4,\qquad b=3.
\]

Then

\[
R_2(a)=2,\qquad R_2(b)=1,
\]

but

\[
R_2(12)=3>2.
\]

### Smallest square-root carry

For \(p=2\), \(a=b=2\):

\[
R_2(2)R_2(2)=1,
\qquad
R_2(4)=2.
\]

Here \(r=s=1\), \(u=v=1\), and

\[
L_2(2,2)=1+1+1=3
=\Delta_2(1).
\]

The carry begins exactly when the load reaches the next threshold.

## 9. P001 resolution

P001 is resolved by the exact integer condition

\[
\boxed{
R_p(ab)=R_p(a)R_p(b)
\iff
R_p(b)^pG_p(a)
+R_p(a)^pG_p(b)
+G_p(a)G_p(b)
<
\Delta_p(R_p(a)R_p(b)).
}
\]

The result also identifies a nonnegative carry count \(K_p(a,b)\), proves the multiplicative region is downward closed within every basin rectangle, and gives an exact floor-division boundary for one offset when the other is fixed.

No real-valued normalization or hidden fractional remainder is needed.

## 10. Prior-art discipline

Integer nth roots, floor/root inequalities, unique integer threshold characterizations, and floor division are established mathematics. A targeted search of current mathlib APIs and integer-root literature during this pass did not locate this exact basin-offset carry formulation as a standard named result. That absence is not evidence of historical priority.

Accordingly, P001-T01–T05 are ordinary mathematical consequences of the stated definitions and are `PROVED`; the exact packaging and historical novelty remain `NOVELTY_UNVERIFIED`.
