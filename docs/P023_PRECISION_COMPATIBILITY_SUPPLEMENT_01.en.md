# P023 — Precision Compatibility Supplement 01

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact compatibility of P007 quotient/multiple-collapse operations with a P018 floor-precision projection

## 1. Setup

Fix a positive precision ratio `r` and define

\[
\pi_r(n)=Q_r(n)=n//r.
\]

For a positive divisor `d`, recall

\[
Q_d(n)=n//d,
\qquad
D_d(n)=d(n//d).
\]

P023 asks whether the fine operation descends to the coarse `\pi_r` states.

## 2. P023-T08 — Quotient is always precision-compatible

For all positive `r,d` and all `n in N`,

\[
\boxed{
\pi_r(Q_d(n))=Q_d(\pi_r(n)).
}
\]

Equivalently,

\[
Q_rQ_d=Q_dQ_r=Q_{rd}.
\]

Hence exact quotient requires no repair detail to operate on these coarse precision states.

### Proof

By associativity of integer floor division by positive integers,

\[
(n//d)//r=n//(dr)=(n//r)//d.
\]

## 3. P023-T09 — Exact classification for same-space multiple collapse

The map

\[
\pi_r\circ D_d
\]

descends through `\pi_r` if and only if

\[
\boxed{d\mid r\quad\text{or}\quad r\mid d.}
\]

Thus the compatibility classification is exactly comparability in the divisibility order.

### Case 1: `d|r`

Write `r=ds`. For

\[
n=qr+t,
\qquad 0\le t<r,
\]

we have

\[
D_d(n)=qr+d(t//d).
\]

The remainder term satisfies

\[
0\le d(t//d)<r,
\]

so

\[
\boxed{
\pi_r(D_d(n))=q=\pi_r(n).
}
\]

Therefore the induced coarse map is the identity.

### Case 2: `r|d`

Write `d=rs`. Then

\[
\pi_r(D_d(n))
=
\frac{rs(n//rs)}{r}
=
s(n//rs).
\]

Using

\[
n//(rs)=(n//r)//s,
\]

we obtain

\[
\boxed{
\pi_r(D_d(n))
=
D_s(\pi_r(n)).
}
\]

Thus the induced coarse operation is exactly `D_(d/r)`.

## 4. Incomparable parameters: uniform explicit witness

Assume neither `d|r` nor `r|d`.

### If `d<r`

Take

\[
x=r,
\qquad
y=(r//d+1)d.
\]

Since `d` does not divide `r`,

\[
r<y<r+d<2r,
\]

so

\[
\pi_r(x)=\pi_r(y)=1.
\]

But

\[
D_d(x)=d(r//d)<r,
\]

whereas `D_d(y)=y>=r`. Hence

\[
\pi_r(D_d(x))=0,
\qquad
\pi_r(D_d(y))=1.
\]

### If `d>r`

Write

\[
d=kr+s,
\qquad 0<s<r.
\]

Take

\[
x=d-1,
\qquad y=d.
\]

Then

\[
\pi_r(x)=\pi_r(y)=k,
\]

but

\[
D_d(x)=0,
\qquad
D_d(y)=d,
\]

so

\[
\pi_r(D_d(x))=0,
\qquad
\pi_r(D_d(y))=k>0.
\]

Thus no induced coarse map exists.

## 5. Structural consequence

This gives a concrete arithmetic instance of the P023 descent criterion:

- `Q_d` respects every floor-precision quotient;
- `D_d` respects `Q_r` exactly along divisibility-comparable scale pairs;
- incomparable scales necessarily require additional detail if one wants to predict the coarse result of `D_d`.

The classification also echoes P007's existing divisibility-comparability theorem for commutation of same-space multiple collapses, but the present statement is a different question: **descent through a precision quotient rather than commutation of two endomaps on the same state space.**

## 6. Executable audit

- `src/enterprise_math/p023_precision_compatibility.py`
- `tests/test_p023_precision_compatibility.py`

The tests verify the quotient identity over bounded ranges, the exact divisibility classification for positive parameters, the two induced coarse maps, and the explicit incomparable-parameter witnesses.
